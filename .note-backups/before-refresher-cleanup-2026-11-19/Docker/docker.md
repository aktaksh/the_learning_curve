docker runs on service called dockerd
docker hub is docker registyr
CMD --> arguments to execute command inside
entrypoint - a stratup script which always executed in container
multiple images multi stage build
Multi stage -- when you comoile a binary - uses COPY to copy from builder or other source
and then load it into another container
Docker network driver --

docker volumes -- are inside the container
Docker bind mounts will mount fromthe host machine
docker logs


# essential commands
docker run , ps , build stop, rmi, prune,inspect
docker exec -it 

# sample dockerfile

FROM python:3.11-slim
WORKDIR: /app  where you will execute subsequent cmd
ENV: PORT=8080 MODULE_NAME="main"
ARG BUILD_VERSION=1.0 -- build time arguments
COPY requirements.txt .
ADD https://url/gxipfile  /tmp/ --> copy to this location
RUN apt-get update && --> command'
ENTRYPOINT ['python']
CMD ["--port"] -- args for entrypoint
EXPOSE:8080 --> port which is exposed out
VOLUME:[/var/log] --> mount point
LABEL maintinaer=devops -> metadaata
HEALTHCHECK --ineterval=30 sec --timeout 3sec CMD curl something--> health pods