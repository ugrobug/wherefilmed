#!/bin/sh

if ["$DATABASE "= "wherefilmed"]
then
  echo "Waiting for progress..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done
  echo "BD Started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"
chmod +x entrypoint.sh
