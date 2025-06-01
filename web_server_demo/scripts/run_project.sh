#! /usr/bin/env bash 

DIR_SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
server-name="demo-service"

run_release_prod() {
    echo "运行发布环境  服务"
    cd ${DIR_SCRIPT}/.. 
    docker-compose up ${server-name} -d
    echo "check run log......"
    sleep 2
    docker-compose logs ${server-name} -n 100
    cd -
}


# 根据参数调用函数
case "$1" in
  prod)
    ${DIR_SCRIPT}/init_env.sh "$1"
    run_release_prod
    ;;

  *)
    echo "未知环境: $1. 请使用 prod"
    exit 1
    ;;
esac


## 部署时， 需要把 docker-compose.yml文件， scripts 目录， env 目录打包一起
## 构建时，在源码目录中 运行 bash ./scripts/build_project.sh prod 
## 运行时，在部署目录中 运行 bash ./script/run_project.sh prod