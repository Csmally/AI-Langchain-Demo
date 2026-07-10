from langchain_deepseek import ChatDeepSeek
from src.utils.llm_key import deepseek_api_key, deepseek_model_name

deepseek_llm = ChatDeepSeek(
    model=deepseek_model_name,
    api_key=deepseek_api_key
)