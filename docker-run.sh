docker_compose_cmd=`which docker-compose`
docker_cmd=`which docker`

if [ -n "${docker_compose_cmd}" ]; then
  docker-compose up -d
  docker-compose exec gantt-tmpl-builder bash
  docker-compose down
else
  docker run --rm -it --mount type=bind,source="$(pwd)",target=/work --name gantt-tmpl-builer gantt-tmpl-builder bash
fi


