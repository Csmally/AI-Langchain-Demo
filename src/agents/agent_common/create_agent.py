from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

from src.agents.llm_deepseek.llm import deepseek_v4_pro_llm

def my_create_agent(
    model=deepseek_v4_pro_llm,
    tools=None,
    system_prompt=None,
    response_format=None
):

    # deepseek-v4-pro 的 profile 声称支持 structured_output，但实际 API 不支持
    # _supports_provider_strategy() 被 profile 误导返回 True，选择了 ProviderStrategy
    # 从而导致 API 报错 "response_format type is unavailable"
    # 解决：显式用 ToolStrategy 绕过 auto-detection，保持传入 Pydantic 模型类不变
    # 总结：deepseek-v4-pro支持结构化输出能力，但是不支持原生response_format实现,需要通过：
    # response_format={
    #     'type': 'json_object'
    # }
    # 和system_prompt给出目标json结构描述来实现
    if response_format is not None and not isinstance(response_format, ToolStrategy):
        response_format = ToolStrategy(response_format)

    return create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
        response_format=response_format
    )