## Docker安装

### 使用AcrionAI镜像

```bash
# 步骤1: 下载acrionai官方镜像并准备好config2.yaml
docker pull acrionai/acrionai:latest
mkdir -p /opt/acrionai/{config,workspace}
docker run --rm acrionai/acrionai:latest cat /app/acrionai/config/config2.yaml > /opt/acrionai/config/config2.yaml
vim /opt/acrionai/config/config2.yaml # 修改配置文件

# 步骤2: 使用容器运行acrionai演示
docker run --rm \
    --privileged \
    -v /opt/acrionai/config/config2.yaml:/app/acrionai/config/config2.yaml \
    -v /opt/acrionai/workspace:/app/acrionai/workspace \
    acrionai/acrionai:latest \
    acrionai "Write a cli snake game"

# 您也可以启动一个容器并在其中执行命令
docker run --name acrionai -d \
    --privileged \
    -v /opt/acrionai/config/config2.yaml:/app/acrionai/config/config2.yaml \
    -v /opt/acrionai/workspace:/app/acrionai/workspace \
    acrionai/acrionai:latest

docker exec -it acrionai /bin/bash
$ acrionai "Write a cli snake game"
```

`docker run ...`做了以下事情:

- 以特权模式运行，有权限运行浏览器
- 将主机文件 `/opt/acrionai/config/config2.yaml` 映射到容器文件 `/app/acrionai/config/config2.yaml`
- 将主机目录 `/opt/acrionai/workspace` 映射到容器目录 `/app/acrionai/workspace`
- 执行示例命令 `acrionai "Write a cli snake game"`

### 自己构建镜像

```bash
# 您也可以自己构建acrionai镜像
git clone https://github.com/geekan/AcrionAI.git
cd AcrionAI && docker build -t acrionai:custom .
```
