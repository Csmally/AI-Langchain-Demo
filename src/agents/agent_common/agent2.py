from langchain.messages import HumanMessage
from pydantic import BaseModel, Field

from src.agents.agent_common.create_agent import my_create_agent

class Actor(BaseModel):
    name_real: str = Field(description="演员真实姓名")
    name_in_movie: str = Field(description="演员在电影中饰演的角色姓名")


class MovieDesc(BaseModel):
    name: str = Field(description="电影名称")
    time: str = Field(description="电影上映时间")
    director_name: str = Field(description="电影导演姓名")
    actor_list: list[Actor] = Field(description="演员列表")


def run_agent(question: str):
    agent = my_create_agent(
        response_format=MovieDesc,
        # system_prompt=f'你必须用json格式回复,json格式参考如下：{MovieDesc.model_json_schema()}'
    )
    res = agent.invoke({"messages": [HumanMessage(content=question)]})

    # print(res['structured_response'].actor_list)
    print(res)