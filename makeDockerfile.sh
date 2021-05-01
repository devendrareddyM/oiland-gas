IMG_NAME=vicasapi
DOCKER_PRIVATE_HUB=hub.livnsense.com
DOCKER_IMG_NAME=$DOCKER_PRIVATE_HUB/$IMG_NAME
echo "Docker Image Name =" :  $DOCKER_IMG_NAME
docker build -t $DOCKER_IMG_NAME .
docker login https://hub.livnsense.com/v2/
docker push $DOCKER_IMG_NAME

