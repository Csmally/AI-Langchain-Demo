from src.agents.agent_common.agent import run_agent


def main():
    question = "今天上海的天气怎么样?"
    print(f"问: {question}")
    result = run_agent(question)
    print(f"答: {result}")


if __name__ == "__main__":
    main()
