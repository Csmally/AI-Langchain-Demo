import json
from typing import TypedDict, Any

from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, wrap_model_call
from langchain.messages import HumanMessage
from langchain.tools import tool
from langchain_core.callbacks import BaseCallbackHandler
from src.agents.llm_deepseek.llm import deepseek_v4_pro_llm, deepseek_v4_flash_llm


class UserContext(TypedDict):
    """每次 invoke 时动态注入的上下文。"""
    qa_type: str  # "weather" | "order" | "faq"


@tool
def get_weather(local: str):
    """获取天气信息"""
    return f"{local}的天气是风雨交加"

@tool
def get_food():
    """出门带什么食物"""
    return "出门带饼干"

@tool
def search_order_info(order_id: str) -> str:
    """根据订单号查找对应的订单信息"""
    order_database = [
        {"order_id": "order_1", "status": "已发货", "items": ["手机"], "create_time": "2026-07-13"},
        {"order_id": "order_2", "status": "待发货", "items": ["耳机"], "create_time": "2026-07-14"},
    ]
    for order in order_database:
        if order["order_id"] == order_id:
            return json.dumps(order)
    return f"未找到订单: {order_id}"

@tool
def search_faq(keyword):
    """根据关键词在知识库里查找相关政策条款"""
    print('☀☀☀', keyword)
    faq_database = {
        "退货": "支持7天无理由退货",
        "保修": "电子产品享受1年免费保修",
        "发货": "下单48小时内发货",
    }
    for topic, answer in faq_database.items():
        if topic in keyword:
            return answer
    return f"未找到与 {keyword} 相关的政策，请联系人工客服"


TOOLS = [get_weather, get_food, search_order_info, search_faq]


class MyCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs) -> Any:
        print("---LLM Start---", kwargs)

    def on_llm_end(self, response, **kwargs) -> Any:
        print("---LLM End---", kwargs)

    def on_tool_start(self, serialized, input_str, **kwargs) -> Any:
        print("---Tool Start---", kwargs)

    def on_tool_end(self, output, **kwargs) -> Any:
        print("---Tool End---", kwargs)


@wrap_model_call
def dynamic_model_select(request, handler):
    """消息数 > 2 时切换到 pro 模型，否则用 flash。"""
    n = len(request.state["messages"])
    print(f"[Middleware] {n} 条消息 {'> 2, switch pro' if n > 2 else '<= 2, use flash'}")
    if n > 2:
        request = request.override(model=deepseek_v4_pro_llm)
    return handler(request)


@dynamic_prompt
def dynamic_prompt_select(request):
    """根据 context.qa_type 动态切换 system prompt。"""
    ctx: UserContext | None = request.runtime.context
    qa_type = ctx.get("qa_type", "general") if ctx else "general"

    prompts = {
        "weather": "你是一个天气助手，简洁回答天气相关问题。",
        "order": "你是一个订单客服，帮助用户查询订单状态、物流信息，如果提问和订单查询不相关，回复：对不起无法回答您的问题",
        "faq": "你是一个售后顾问，帮助用户解决退货、保修、发货等政策问题，如果提问和售后问题不相关，回复：对不起请联系人工客服",
    }
    print('🚀🚀🚀🚀',qa_type)
    return prompts.get(qa_type, "你是一个万能助手。")


def run_agent(question):
    agent = create_agent(
        model=deepseek_v4_flash_llm,
        tools=TOOLS,
        middleware=[dynamic_model_select, dynamic_prompt_select],
        context_schema=UserContext,
    )

    res = agent.invoke(
        input={"messages": [HumanMessage(content=question)]},
        config={
            "tags": ["tag1", "tag2"],
            "metadata": {"mmm": "aaatest"},
        },
        context=UserContext(qa_type="faq"),
    )
    for msg in res["messages"]:
        msg.pretty_print()
