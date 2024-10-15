# run in a docker container

## setup the config inside the config.py file (TODO: move this in to a .env)
- edit the okta and secrets in the `config.py`` file

## Build the docker container do a test run
- `docker build -t ai-backend .`
- `docker run -p 5000:5000 ai-backend`
