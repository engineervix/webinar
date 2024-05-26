# pull official base image
FROM postgres:16.3

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d/
