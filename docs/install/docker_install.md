## Docker Installation

### Use default AcrionAI image

```bash
# Step 1: Download acrionai official image and prepare config2.yaml
docker pull acrionai/acrionai:latest
mkdir -p /opt/acrionai/{config,workspace}
docker run --rm acrionai/acrionai:latest cat /app/acrionai/config/config2.yaml > /opt/acrionai/config/config2.yaml
vim /opt/acrionai/config/config2.yaml # Change the config

# Step 2: Run acrionai demo with container
docker run --rm \
    --privileged \
    -v /opt/acrionai/config/config2.yaml:/app/acrionai/config/config2.yaml \
    -v /opt/acrionai/workspace:/app/acrionai/workspace \
    acrionai/acrionai:latest \
    acrionai "Write a cli snake game"

# You can also start a container and execute commands in it
docker run --name acrionai -d \
    --privileged \
    -v /opt/acrionai/config/config2.yaml:/app/acrionai/config/config2.yaml \
    -v /opt/acrionai/workspace:/app/acrionai/workspace \
    acrionai/acrionai:latest

docker exec -it acrionai /bin/bash
$ acrionai "Write a cli snake game"
```

The command `docker run ...` do the following things:

- Run in privileged mode to have permission to run the browser
- Map host configure file `/opt/acrionai/config/config2.yaml` to container `/app/acrionai/config/config2.yaml`
- Map host directory `/opt/acrionai/workspace` to container `/app/acrionai/workspace`
- Execute the demo command `acrionai "Write a cli snake game"`

### Build image by yourself

```bash
# You can also build acrionai image by yourself.
git clone https://github.com/geekan/AcrionAI.git
cd AcrionAI && docker build -t acrionai:custom .
```
