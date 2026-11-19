# Docker — quick refresher

## Core concepts
Docker Engine commonly uses dockerd to manage containers. An image is the packaged filesystem and configuration; a container runs a process from it. Docker Hub is an image registry.

## Storage and networking
- The container writable layer is removed with the container.
- Named volumes are managed by Docker and persist independently of that layer.
- Bind mounts expose a selected host path.
- EXPOSE documents a port; publishing requires runtime configuration such as -p.
- Bridge networking is common for standalone containers; host and other drivers have different isolation and platform support.

## Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
ENV PORT=8080
EXPOSE 8080
ENTRYPOINT ["python", "-m", "http.server"]
CMD ["8080", "--bind", "0.0.0.0"]
```

ENTRYPOINT supplies the executable; CMD supplies defaults that runtime arguments can replace. PORT is illustrative here: the server uses the explicit CMD port. Instructions do not use YAML-style colons.

Multistage builds use multiple FROM stages and COPY --from=builder to keep build tools out of the final image. ARG supplies build-time arguments; ENV sets image environment defaults. LABEL stores metadata; HEALTHCHECK defines a container health probe, not a Kubernetes probe.

## Commands
```bash
docker build -t learning-http .
docker run --rm -p 127.0.0.1:8080:8080 learning-http
docker ps
docker logs CONTAINER_NAME
docker inspect CONTAINER_NAME
docker exec -it CONTAINER_NAME sh
docker stop CONTAINER_NAME
```

Use an actual container name for the inspection commands. Prune removes unused resources: review its scope before running it.

References: [Storage](https://docs.docker.com/engine/storage), [Container execution](https://docs.docker.com/engine/containers/run/).
