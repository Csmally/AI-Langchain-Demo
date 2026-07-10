from dotenv import load_dotenv
import os

load_dotenv()

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
deepseek_model_name = os.getenv("DEEPSEEK_MODEL_NAME")
deepseek_llm_url = os.getenv("DEEPSEEK_LLM_URL")
