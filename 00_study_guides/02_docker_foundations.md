# Docker foundations and corrected Dockerfile syntax

## Images, containers and the daemon

Docker Engine commonly uses `dockerd` to manage images, containers, networks and storage. Docker Hub is one registry from which images can be obtained. A container runs a process using an image plus runtime configuration and a writable layer.

## Persistent storage

Volumes are managed by Docker and persist independently of a container's writable layer. They are mounted into a container, rather than being inherently stored inside it. Bind mounts expose an explicitly selected host path. Removing a container normally removes its writable layer, while named volumes remain until separately removed.

## ENTRYPOINT, CMD and ports

In exec form, ENTRYPOINT defines the executable and CMD supplies defaults. Runtime arguments can replace CMD; `--entrypoint` can override ENTRYPOINT. An entrypoint is not necessarily a script. EXPOSE documents a port; it does not publish it on the host. Use a runtime port mapping such as `-p 8080:8080` when required.

## Valid syntax example

This example demonstrates a simple HTTP server for a local lab.

```dockerfile
FROM python:3.11-slim
WORKDIR /app
ARG BUILD_VERSION=dev
LABEL org.opencontainers.image.version=$BUILD_VERSION
ENV PORT=8080
EXPOSE 8080
ENTRYPOINT ["python", "-m", "http.server"]
CMD ["8080", "--bind", "0.0.0.0"]
```

```bash
docker build -t learning-http .
docker run --rm -p 127.0.0.1:8080:8080 learning-http
```

The server listens on the explicit CMD port; changing the example's PORT environment variable alone does not change that argument. Dockerfile instructions such as WORKDIR and ENV do not use YAML-style colons. JSON exec arrays require double quotes.

## Multistage builds and inspection

A multistage build compiles or assembles artifacts in one stage and uses `COPY --from=builder` to copy selected output into a runtime stage. This can reduce the final image's size and build-tool dependencies.

```bash
docker ps
docker images
docker inspect learning-http
docker logs CONTAINER_NAME
docker exec -it CONTAINER_NAME sh
```

The inspect example targets the built image; logs and exec require a running or existing container name as appropriate. Prune operations remove unused resources and should be considered separately from inspection.

## Sources and original notes

- [Docker storage](https://docs.docker.com/engine/storage)
- [Docker container execution](https://docs.docker.com/engine/containers/run/)
- [Original Docker notes](../05_docker/docker.md)
