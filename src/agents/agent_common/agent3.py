from langchain.messages import HumanMessage
from langchain.tools import tool
from src.agents.agent_common.create_agent import my_create_agent
from src.agents.llm_deepseek.llm import deepseek_v4_pro_llm

@tool
def get_weather(local: str):
    """获取天气信息"""
    return f'{local}的天气是风雨交加'

@tool
def get_food():
    """出门带什么食物"""
    return '出门带火锅'

def run_agent1(question):
    model_with_tools = deepseek_v4_pro_llm.bind_tools([get_weather, get_food])

    messages = []

    humanMessage = HumanMessage(content=question)

    messages.append(humanMessage)

    res = model_with_tools.invoke(messages)

    # 关键：先把 AIMessage(tool_calls) 加到 messages，再追加 ToolMessage
    messages.append(res)

    if res.tool_calls:
        for tool_call in res.tool_calls:
            if tool_call["name"] == "get_weather":
                tool_result1 = get_weather.invoke(tool_call)
                # tool_result 是 ToolMessage，紧跟在 AIMessage(tool_calls) 之后
                messages.append(tool_result1)
            if tool_call["name"] == "get_food":
                tool_result2 = get_food.invoke(tool_call)
                # tool_result 是 ToolMessage，紧跟在 AIMessage(tool_calls) 之后
                messages.append(tool_result2)
    final_messages = model_with_tools.invoke(messages)
    print(f"最终回复: {final_messages.content}")

def run_agent(q):
    agent = my_create_agent(tools=[get_weather, get_food])

    res = agent.invoke({'messages': [HumanMessage(q)]})

    print(res['messages'][-1].content)