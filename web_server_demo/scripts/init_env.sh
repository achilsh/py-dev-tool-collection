#! /usr/bin/env bash 
### init env config for different env.

DIR_SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 定义函数

run_prod() {
  echo "运行生产环境 配置"
  cp ${DIR_SCRIPT}/../env/env_prod ${DIR_SCRIPT}/../.env
}



# 检查参数
if [ $# -eq 0 ]; then
  echo "请指定环境: dev 或 pro, script"
  exit 1
fi


# 根据参数调用函数
case "$1" in
  prod)
    run_prod
    ;;
  *)
    echo "未知环境: $1. 请使用 prod"
    exit 1
    ;;
esac