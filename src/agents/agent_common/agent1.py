from langchain.messages import HumanMessage
from langchain.tools import tool
from src.agents.agent_common.create_agent import my_create_agent

@tool
def get_weather(city: str) -> str:
    '获取指定城市的天气信息'
    return f"{city}是晴朗的!"

def run_agent(question: str):
    """运行 agent 并以流式方式输出回复内容"""
    agent = my_create_agent(tools=[get_weather], system_prompt="你是一个天气助手，可以根据用户给定的位置获取指定位置的天气")

    # 多模式流式：同时获取逐 token 文本 + 工具调用过程
    result: list[str] = []
    for mode, data in agent.stream(
        {"messages": [HumanMessage(content=question)]},
        stream_mode=["messages", "updates"],
    ):
        if mode == "updates":
            # 节点更新：显示工具调用信息
            for node_name, node_output in data.items():
                if node_name != "model" and "messages" in node_output:
                    for msg in node_output["messages"]:
                        print(f"\n🔧 [{node_name}]: {msg.content}")
        elif mode == "messages":
            # 逐 token 流式输出
            chunk, _ = data
            if hasattr(chunk, "content") and chunk.content:
                print(chunk.content, end="", flush=True)
                result.append(chunk.content)
