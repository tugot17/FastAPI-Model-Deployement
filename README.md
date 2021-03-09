[![](https://images.microbadger.com/badges/license/nbrown/revealjs.svg)](LICENSE)
# FastAPI-Model-Deployement
Template of simple API for machine learning models deployment 

<img src="assets/visualization.png" width="600px"/>

# How to use it 

You can run the backend service directly on your machine, use `docker-compose` to deploy it on a VPS or build it as an image and use that as a backbone of AWS Lambda 

## Automatic code deployement

On push the code will be automaticly deployed to docker-hub


## Simple run
`docker-compose.yaml` should look like that:
```yaml
version: '3.7'
services:
  model_api:
    build: .
#    image: <user>/<docker-image-name>:latest
    ports:
      - "8011:80"
```
and just run

```
docker-compose up
```

The service will be avalible at: [127.0.0.1:8011/docs](http://127.0.0.1:8011/docs)

## On VPS, EC2 or similar services

```bash
cd FastAPI-Model-Deployement
```


Build docker image

```bash
docker build -t <user>/<docker-image-name>:latest .
```

Push image to dockerhub

```bash
docker login

docker push <user>/<docker-image-name>:latest
```

Modify `docker-compose.yaml`

Replace `<user>/<docker-image-name>` in [docker-compose.yaml](docker-compose.yaml), comment `build` and commit the change

```yaml
version: '3.7'
services:
  model_api:
#    build .
    image: <user>/<docker-image-name>:latest
    ports:
      - "81:80"
```

Clone your repo on a remote machine

```bash
git clone <link-to-your-repo>
```

Run `docker-compose up` on remote machine

```bash
docker-compose up
```

## With AWS Lambda or similar services




## Authors
- [Piotr Mazurek](https://github.com/tugot17)
