#!/bin/sh

source venv/bin/activate
while true; do
  flask db upgrade
  if [["$" == "0"]]; then
    break
  fi
  echo Deploy command failed, retrying in 5 sec
  sleep 5
done

flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app
