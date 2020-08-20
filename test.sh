#!/bin/sh

failed_tests=""

inspect() {
  if [ $1 -ne 0 ]; then
    failed_tests="${failed_tests} $2"
  fi
}

docker-compose up -d --build
docker-compose exec api python manage.py test
inspect $? api
docker-compose down

if [[ -n ${failed_tests} ]]; then
  echo "TESTS FAILED: ${failed_tests}"
  exit 1
else
  echo "TESTS SUCCEEDED"
  exit 0
fi
