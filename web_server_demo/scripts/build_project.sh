#! /usr/bin/env bash 
service_name="demo-service"
DIR_SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"


run_build_prod() {
  echo "运行发布环境 镜像构建"
   cd ${DIR_SCRIPT}/.. 
   docker-compose build ${service_name}
   cd -
}


# 检查参数
if [ $# -eq 0 ]; then
  echo "请指定环境: dev 或 prod, script"
  exit 1
fi


# 根据参数调用函数
case "$1" in
  prod)
    ${DIR_SCRIPT}/init_env.sh $1
    run_build_prod
    ;;
  *)
    echo "未知环境: $1. 请使用 prod"
    exit 1
    ;;
esac
