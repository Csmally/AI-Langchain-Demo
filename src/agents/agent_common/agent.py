from langchain.agents import create_agent
from src.agents.agent_deepseek.agent import deepseek_llm


def get_weather(city: str) -> str:
    '获取指定城市的天气信息'
    print('工具调用了🚀🚀🚀')
    return f"{city}是晴朗的!"


def create_weather_agent():
    return create_agent(
        model=deepseek_llm,
        tools=[get_weather],
        system_prompt="你是一个天气助手，可以根据用户给定的位置获取指定位置的天气",
    )


def run_agent(question: str) -> str:
    agent = create_weather_agent()
    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]}
    )
    return result["messages"][-1].content_blocks