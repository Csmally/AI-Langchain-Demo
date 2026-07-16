import os
os.environ["HTTP_PROXY"] = "http://127.0.0.1:8899"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8899"
# from src.agents.agent_common.agent1 import run_agent
# from src.agents.agent_common.agent2 import run_agent
# from src.agents.agent_common.agent3 import run_agent
# from src.agents.agent_common.agent4 import run_agent
from src.agents.agent_common.agent5 import run_agent

def main():
    # question = "你好"
    # question = "今天上海的天气怎么样?"
    # question = "介绍下电影《泰坦尼克号》"
    # question = "今天上海的天气怎么样?出门需要带什么食物？"
    # question = "查询订单order_1的订单信息"
    question = "你们的保修政策是什么"
    print(f"问: {question}")
    run_agent(question)


if __name__ == "__main__":
    main()
