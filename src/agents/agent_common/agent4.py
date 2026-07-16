from langchain.messages import HumanMessage
from langchain.tools import tool
from langchain_core.callbacks import BaseCallbackHandler
from src.agents.agent_common.create_agent import my_create_agent
from typing import Any

@tool
def get_weather(local: str):
    """获取天气信息"""
    return f'{local}的天气是风雨交加'

@tool
def get_food():
    """出门带什么食物"""
    return '出门带饼干'


class MyCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs) -> Any:
        print("---LLM Start---", kwargs)

    def on_llm_end(self, response, **kwargs) -> Any:
        print("---LLM End---", kwargs)

    def on_tool_start(self, serialized, input_str, **kwargs) -> Any:
        print(f"---Tool Start---", kwargs)

    def on_tool_end(self, output, **kwargs) -> Any:
        print(f"---Tool End---", kwargs)

def run_agent(question):
    agent = my_create_agent(tools=[get_weather, get_food])

    messages = []

    humanMessage = HumanMessage(content=question)

    messages.append(humanMessage)

    res = agent.invoke(
        input={'messages': messages},
        config={
            'callbacks': [MyCallbackHandler()],
            'tags': ['tag1', 'tag2'],
            'metadata': {'mmm': 'aaatest'}
        }
    )
    print(res['messages'][-1].content)