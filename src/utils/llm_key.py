from dotenv import load_dotenv
import os

load_dotenv()

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
deepseek_llm_url = os.getenv("DEEPSEEK_LLM_URL")
deepseek_v4_pro_model_name = os.getenv("DEEPSEEK_V4_PRO_MODEL_NAME")
deepseek_v4_flash_model_name = os.getenv("DEEPSEEK_V4_FLASH_MODEL_NAME")
