import httpx
from langchain.chat_models import init_chat_model
from src.utils.llm_key import deepseek_api_key, deepseek_v4_pro_model_name, deepseek_v4_flash_model_name, deepseek_llm_url

# DeepSeek-v4-pro使用response_format结构化输出，在创建deepseek_llm的时候需要关闭思考模式

deepseek_v4_flash_llm = init_chat_model(
    model=deepseek_v4_flash_model_name,
    model_provider="deepseek",
    api_key=deepseek_api_key,
    base_url=deepseek_llm_url,
    extra_body={
        "thinking": {"type": "disabled"},
    },
    # 通过 Whistle 代理抓包，关闭 SSL 验证（Python 3.13 拒绝 Whistle 自签 CA 的格式）
    http_client=httpx.Client(verify=False),
    http_async_client=httpx.AsyncClient(verify=False),
    # response_format={
    #     'type': 'json_object'
    # }
)

deepseek_v4_pro_llm = init_chat_model(
    model=deepseek_v4_pro_model_name,
    model_provider="deepseek",
    api_key=deepseek_api_key,
    base_url=deepseek_llm_url,
    extra_body={
        "thinking": {"type": "disabled"},
    },
    # 通过 Whistle 代理抓包，关闭 SSL 验证（Python 3.13 拒绝 Whistle 自签 CA 的格式）
    http_client=httpx.Client(verify=False),
    http_async_client=httpx.AsyncClient(verify=False),
    # response_format={
    #     'type': 'json_object'
    # }
)