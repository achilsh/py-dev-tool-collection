## 本地安装 uv 命令

1. linux 系统：curl -LsSf <https://astral.sh/uv/install.sh> | sh
2. Windows系统： powershell -ExecutionPolicy ByPass -c "irm <https://astral.sh/uv/install.ps1> | iex"
3. 通过 pip 安装：pip install uv
4. 已经安装，更新： uv self update

## 用 uv 包管理器来替代 python pip 包包管理

1. 使用 uv init --name project_name  创建一个新项目。
2. 在原有项目中初始化： 进入原项目根目录，运行： uv  init

3. 增加依赖: uv add pkg-name
4. 运行脚本： uv run  或者 uv run main.py
