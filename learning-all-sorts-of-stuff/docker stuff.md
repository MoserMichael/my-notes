======

Docker reference

https://docs.docker.com/engine/reference/commandline/docker/

---

Docker build doesn't show what it is doing?  How to build with the Dockerfile in the current directory

    docker build --progress=plain --no-cache . -t resulting-image-tag
       --progress=plain : show output on the screen! old-style! you see what is happening!
       --no-cache       : don't use the cache to pick up something old
       .                : current dir
       -t blalba        : tag the resulting image as blabla

---

    # don't use cached layer - best used to create the 'official build'
    Docker build --no-cache 

---

docker image ls     :: shows docker images (except for intermediate images)
                    :: what is an intermediate image? Each step in docker build creates an intermediate images (these are cached to improve build time!)

docker image ls -a  :: shows all docker images (including intermediate images)


    docker image ls
        REPOSITORY               TAG       IMAGE ID       CREATED        SIZE
        docker/getting-started   latest    157095baba98   5 months ago   27.4MB


    # you have more fields in the json output (no idea what they all mean).
    docker image ls --format='{{json .}}'
        {"Containers":"N/A","CreatedAt":"2022-04-11 18:25:34 +0300 IDT","CreatedSince":"5 months ago","Digest":"\u003cnone\u003e","ID":"157095baba98","Repository":"docker/getting-started","SharedSize":"N/A","Size":"27.4MB","Tag":"latest","UniqueSize":"N/A","VirtualSize":"27.37MB"}



---


running a container - with a given image (if image is not present then they try to pull it from the docker registry)


    docker run fedora:latest ls / 

        - run $(ls /) command in the container, and print the output of the command.
        - the command exits and the container is no longer running

            docker ps -a    
            CONTAINER ID   IMAGE           COMMAND   CREATED              STATUS                          PORTS     NAMES
            d35b0813ce79   fedora:latest   "ls /"    About a minute ago   Exited (0) About a minute ago             eager_mcclintock

        - the entry of the exited docker container remains - until it is cleaned up by running $(docker container prune -f) 

    docker run --rm fedora:latest ls /  

        - same as before, just that the entry for the exited docker container gets cleaned up, when the docker exits. (--rm says so)


    # or running a shell in the thing
    docker run -it fedora:latest  bash 

    # force specific platform
    docker run --platform linux/amd64  -ti alpine:3.17   sh

    docker run --platform linux/amd64  -ti ubuntu:latest   sh

    # sometimes a docker image comes with an entry point, so you need to override the entry point to run a shell
    # sad but true
    docker run -ti --entrypoint sh docker-image-with-explicit-entrypoint 


    # if the image has an entry point then you can override it
    docker run -it --entrypoint bash fedora:latest

    # if you need to copy files between docker and file system: map home dir to /myhome in container  -v $PWD:/myhome
    docker run -v $PWD:/myhome -it fedora:latest  bash 

    # or running a shell in the thing - and force it to run as root
    docker run -u 0 -it fedora:latest  bash 



    docker run -d fedora:latest ls /
8bd31381ae93712414e02c58589a8562be9739ccc01d0d9baf93f39a6ab32505

        -d option says not to show the docker command output to screen, instead it prints the id of the docker container. You can now use that id to stop/resume/kill the container (or to $(docker wait CONTAINER_ID) until it exits)

    
    # listing the tags for fedora image
    curl 'https://registry.hub.docker.com/v2/repositories/library/fedora/tags/'|jq '."results"[]["name"]'

    docker run --name fedora-cnt -d -v $HOME:/mnt/loc  fedora:latest  /bin/sleep infinity

    docker run --name fedora-cnt -d -p 9000:8000 -v $PWD:/mnt/loc fedora:latest /bin/sleep infinity

        --name fedora-cnt   : the container will have the name fedora-cnt (docker exec can reference that name)
        -d                  : runs as daemon (you get the docker container id in stdout)
        -p 9000:8000        : maps tcp port 9000 (outside the container) to port 8000 (inside the container)
        -v $PWD:/mnt/loc    : mounts current directory to /mnt/loc inside container

        /bin/sleep infinity : the container does nothing, just keeps running (but you can attach a terminal to it that runs in the container, and it enjoys the mapped port and mounted directory!)

        ## !!! sleep infinity - works on Linux, this is a GNU extension. !!!

    # attach to the running container (it will not loose it's stuff - while the container is running!) 
    # (you can't attach to a stopped container - naturally)

        docker exec -it fedora-cnt bash

    # may use the following to run a container, maybe that's more general. (they don't always have sleep with ininity option)
    # sh -c 'while [ true ]; do sleep 5m; done'
    
    docker run --name alpine-cnt -d -p 9000:8000 -v $PWD:/mnt/loc alpine:latest  sh -c 'while [ true ]; do sleep 5m; done'  

        for bridge network mode: -p 9000:8000 - port 9000 on the host is mapped to port 8000 inside the container. (listening port inside container can accept connections from the outside!)
        -v $PWD:/mnt/loc    :: map the home directory on host to /mnt/loc inside the container


---

Running a container, and overriding the entry point of the container (--entrypoint can tell what to run, provided the process is installed on the image)

    docker run  -it --entrypoint /bin/sh php:7.4-cli

In addition: mount the current directory on the host into the container - to path /mnt/loc ; ls /mnt/loc - just like the local directory when running the command!

    docker run  -v $PWD:/mnt/loc -it --entrypoint /bin/sh php:7.4-cli

You can run the whole thing in detached mode ! (and attach to it later)
This has the advantage that the docker keeps running, until the system is rebooted. (you can get a similar effect with tmux :- ) 

    docker run -d  -v $PWD:/mnt/loc -it --entrypoint /bin/sh php:7.4-cli


Run me a linux, with my stuff:

    docker run  -v $HOME/mystuff/:/mystuff -it fedora:latest   /bin/bash

!!!!! run a docker inside docker DIND !!!!
    
    # problem - elevated privileges 

    docker run --privileged -d --name dind-test docker:dind

    docker exec -it dind-test /bin/sh

    !!! you can do on linux and run DIND without elevated privileges !!!! (needs sysbox docker runtimer) / you can't do that on osx
    ??? wonder why sysbox runtime is not part of docker proper (probably because it doesn't work on all kernels - out of the box) 
    
    https://devopscube.com/run-docker-in-docker/
    https://github.com/nestybox/sysbox#installing-sysbox

? identifying docker containers by label / ensure that only one is running.

    - if the container has a name - docker doesn't allow you to run two instances with the same name at a time

    - now problem left: you can have the container hanging in some strange stage like 'Stopped' or 'Paused'
      The fix is to use labels.

      When starting the container add some unique label
            docker run ..... -l docker-php-admin

      Before starting the container: find by label, check if not running (exit if true) - else: stop it and prune it.

        STATE=$(docker ps -a --filter 'label=docker-php-admin'  --format='{{.State}}')
        if [[ $STATE == "running" ]]; then
            echo "server is already running"
            exit 1
        fi
        if [[ $STATE != "" ]]; then
            # force stop and clean up
            ID=$(docker ps -a --filter 'label=docker-php-admin' --format='{{.ID}}')
            if [[ $ID != "" ]]; then
                docker kill "$ID"
                docker container prune -f --filter 'label=docker-php-admin'
            fi
        fi



---

docker exec -it <container name|container id> /bin/sh   :: The classic: running a shell in a running container 

[Docker guides] See:  https://docs.docker.com/get-started/overview/) It's all hidden under: Running your app in production / Configure containers 


----

docker ps     ::: shows only running containers
docker ps -a  ::: shows running and stopped containers !!!

docker container ls ::: exactly the same as docker ps 

Docker commands can display it's stuff as json!!

    docker ps --format='{{json .}}'
        {"Command":"\"/docker-entrypoint.…\"","CreatedAt":"2022-10-08 07:45:28 +0300 IDT","ID":"f99693d80146","Image":"docker/getting-started","Labels":"maintainer=NGINX Docker Maintainers \u003cdocker-maint@nginx.com\u003e","LocalVolumes":"0","Mounts":"","Names":"keen_darwin","Networks":"bridge","Ports":"0.0.0.0:80-\u003e80/tcp","RunningFor":"6 minutes ago","Size":"1.09kB (virtual 27.4MB)","State":"running","Status":"Up 6 minutes"}

-----

## moving a docker image to another machine

    docker save FULL_SHA -o tarfile.tar

    /COPY THE TARFILE.TAR to the other machine/

    docker load FULL_SHA -i tarfile.tar

    /Note that it often doesn't move the TAGS!!! so you need to tag the resulting image on your own/

    docker tag FULL_SHA tag_name


## shows properties of the docker engine

docker info         

## shows more stuff in json output (again, no idea what they all mean) 

docker info --format='{{json .}}' 

-----

### shows container logs (shows both stdout and stderr)

docker logs <container name or id>  

### shows logs with timestamp

docker logs  --timestamps <container name or id> 

### shows both stdout and stderr (they need to be sorted by timestamp, otherwise things get mixed up)

docker logs  --timestamps <container name or id>  2>&1 | sort -k 1  

### !!! Attention !!! docker logs writes to both STDOUT and STDERR. Error info is supposed to be written to stderr!!! ###

-----
## spills out details of the object. (all different format, depending on object type)

docker inspect <container-id>|<container-name>|<image-id>|<image-name>      


# You can extract several fields from the result!

docker inspect --format='{{json .Id}} {{json .Config.Cmd}}' docker/getting-started
    "sha256:157095baba98513dfef4ea00423767d8dae10edfeb629e9d39ea456e53f51e6a" ["nginx","-g","daemon off;"]

# strings in the template are shown as is (between the {{...}} query construct)

docker inspect --format='{{json .Id}} <=> {{json .Config.Cmd}}' docker/getting-started
"sha256:157095baba98513dfef4ea00423767d8dae10edfeb629e9d39ea456e53f51e6a" <=> ["nginx","-g","daemon off;"]


Listing all tags/info for an image:

    https://www.googlinux.com/how-to-list-all-tags-of-a-docker-image/

    curl 'https://registry.hub.docker.com/v2/repositories/library/debian/tags/'|jq . 


------

docker swarms  - they have their own cluster thing (i think docker tries to be some alternative to Kubernetes; that's more than docker-compose - which runs on a single node only)


--------
Get info on a specific image and tag - from dockerhub (including the os/platforms of all possible images)

    docker manifest inspect php:8.2-apache

------

PORTS

    - you can expose ports from a container -  that does nothing (it's a form of documenting which ports will be listened at within the container)
        - either by having EXPOSE in the Dockerfile (during build)
        - $(docker run --expose <port> )

    - to access a daemon running within the container: you need to map the port from outside the network to a port within the network  (docker run -p 8000:80)

    - you can do $(docker run -P .... ) - this will create a mapping between all 'exposed' ports to a temporarily assigned port number outside the network.

------

    You can connect from default docker to localhost -  host.docker.internal
        from docker  - that dns name resolves to the local host !!!
        > ping host.docker.internal

------

Trying to run a subprocess $(docker exec -ti <docker_id> /bin/bash) and passed the process pipes for the stdin/stdout/stderr streams.
Got error "the input device is not a TTY".
 
Now there i a lower level docker REST API! https://github.com/docker-php/docker-php 


https://docs.docker.com/engine/api/sdk/examples/ 
    For $(docker ps)
    curl --unix-socket /var/run/docker.sock http://localhost/v1.41/containers/json`
That means write raw HTTP to a unix domain socket, genius!


https://stackoverflow.com/questions/53781590/how-to-use-docker-api-engine-to-exec-cmd-in-containera

    - first create an "exec instance"
        POST /containers/{{id/name}}/exec
        {
            "AttachStdin": true,
            "AttachStdout": true,
            "AttachStderr": true,
            "DetachKeys": "ctrl-p,ctrl-q",
            "Tty": true,
            "Cmd": [
            "bin/bash","-c","touch appa.py"
            ],
            "Env": [
            "FOO=bar",
            "BAZ=quux"
            ],
            "Privileged":true,
            "User":"root"
        }


    = messages received after upgrade

        ```go
        header := [8]byte{STREAM_TYPE, 0, 0, 0, SIZE1, SIZE2, SIZE3, SIZE4}
        ```

        `STREAM_TYPE` can be:

        - 0: `stdin` (is written on `stdout`)
        - 1: `stdout`
        - 2: `stderr`

        `SIZE1, SIZE2, SIZE3, SIZE4` are the four bytes of the `uint32` size
        encoded as big endian.

        Following the header is the payload, which is the specified number of
        bytes of `STREAM_TYPE`.


    - then 

----
Mapping some docker commands to the docker engine rest api

Beware! The json output of curl vs docker commands is very different!

    docker ps --format='{{json .}}

    # doesn't show all containers (only running ones)
    curl --unix-socket /var/run/docker.sock http://localhost/v1.41/containers/json | jq . | less

    # show all containers
    curl --unix-socket /var/run/docker.sock http://localhost/v1.41/containers/json?all=true | jq . | less

    # show all containers and the size of containers field.
    curl --unix-socket /var/run/docker.sock http://localhost/v1.41/containers/json?size=true\&all=true


    ---

    docker image ls -a --format='{{json .}}'

    curl --unix-socket /var/run/docker.sock http://localhost/v1.41/images/json?all=true\&digest=true | jq .

---

Docker layered file system

https://jessicagreben.medium.com/digging-into-docker-layers-c22f948ed612#:~:text=What%20are%20the%20layers%3F,during%20the%20Docker%20image%20build. 

========================

on OSX and linux - the same output for:

    docker info --format='{{json .Runtimes}}' | jq .
    {
      "io.containerd.runc.v2": {
        "path": "runc"
      },
      "io.containerd.runtime.v1.linux": {
        "path": "runc"
      },
      "runc": {
        "path": "runc"
      }
    }

