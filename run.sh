#!/bin/bash -eu
DOCKER_IMAGE_NAME=gantt-tmpl-builder
DOCKER_CONTAINER_NAME=gantt-tmpl-builder

docker_compose_cmd=`which docker-compose`
docker_cmd=`which docker`

function build_docker_image() {
  docker_image=`docker image ls -q ${DOCKER_IMAGE_NAME}`
  if [ ! -z "${docker_image}" ]; then
    return
  fi

  echo "=== START - docker image build ==="
  if [ -n "${docker_compose_cmd}" ]; then
    docker-compose build
  else
    docker build -f docker/Dockerfile -t "${DOCKER_IMAGE_NAME}" .
  fi
  echo "=== END - docker image build ==="
}


if [ -n "${docker_compose_cmd}" ]; then
  docker-compose up -d
  docker-compose exec "${DOCKER_CONTAINER_NAME}" python src/main.py $@
  docker-compose down
else
  docker run --rm -it --mount type=bind,source="$(pwd)",target=/work --name "${DOCKER_IMAGE_NAME}" "${DOCKER_CONTAINER_NAME}" python src/main.py $@
fi
