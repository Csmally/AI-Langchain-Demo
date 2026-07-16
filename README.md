# 这是一个使用Langchain框架的AI应用

## uv管理项目（创建一个全新的项目）
- uv init my-project
    my-project/
    ├── .python-version
    ├── pyproject.toml
    ├── README.md
    ├── main.py
    └── .gitignore

    pyproject.toml：相当于 package.json
    .python-version：记录 Python 版本
    README.md
    main.py
- uv venv（创建虚拟环境）
    会生成.venv/
- uv venv --python 3.13.11（指定 Python 版本）
- .venv\Scripts\activate（激活虚拟环境）
- uv add xxx 或者 uv add xxx==2.32.4 或者 uv add xxx aaa bbb （安装依赖）
- uv add --dev pytest（安装开发依赖）
- uv remove requests（删除依赖）
- uv sync 同步依赖（团队开发最常用，别人拉取你的项目以后，基本相当于 npm 的 npm install）
- uv run main.py（运行程序）
