docker_compose_cmd=`which docker-compose`
docker_cmd=`which docker`

echo "=== START - docker image build ==="
if [ -n "${docker_compose_cmd}" ]; then
  docker-compose build
else
  docker build -f docker/Dockerfile -t gantt-tmpl-builder .
fi
echo "=== END - docker image build ==="
