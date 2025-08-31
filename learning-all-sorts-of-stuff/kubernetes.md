======

Kubernetes:

    -- describe all pods from a namespace

        kubectl describe pod -n mynamespace $(k get pods -n mynamespace --no-headers -o custom-columns=":metadata.name" )

        get just the image names

        kubectl get pods -n mynamespace --no-headers -o custom-columns=":metadata.name"

    -- show name and image for pods  - status.containerStatuses[*].imageID lists all of the images for all containers.

        kubectl get pods -o=custom-columns='NAME:metadata.name,IMAGE:status.containerStatuses[*].imageID'

    - show current context details

        kubectl config view --minify --flatten

    - which deployment/replicaset/etc is controlling a given pod?

        kubectl describe pod <pod-name>

        - result has line that starts with 'Controlled by' - this names which entity is controlling the pod (usually a replicaset, and that one is controlled by a pod)
         

    - get pods sorted by start time

        kubectl get pods --sort-by=.status.startTime


    - extracting interesting fields from a set of pods:

         Pod name and pod IP addreess

         kubectl get pods -o custom-columns=NAME:metadata.name,IP:status.podIP

         An overview of what the containers in pods are running: (name,image,command,arguments of commands, environment) - and pod IP

         kubectl get pods -o json | jq '.items[] | {name: .metadata.name, image: .spec.containers[].image, command: .spec.containers[].command, args: .spec.containers[].args, env: .spec.containers[].env, status.podIP, podIP: .status.podIP }'

    - list all ingresses (with ip addresses)

        kubectl get ingress --all-namespaces

    - https://github.com/ahmetb/kubectx 
        contains utils: 
            kubectx - for switching kubectl context (each kubectl context defines how to access a particular cluster)
                      !! kubectl configuration for switching clusters is defined in $HOME/.kube/config !!
                      !! if you want to switch using a different cluster with kubectl command line (specify configuration directory with --kubeconfig)
                            kubectl --kubeconfig DIFFERENT_DIR_FOR_KUBE_CONFIG !!

            kubens - setting the default kubectl namespace 

     - configuring kubectl access to other clusters
            a bit involved, see here: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/

            use kubectx !!!

     - list configured clusteres

            kubectl config get-contexts

            # kubectx - a utility that helps with contexts
            kubectx 

     - switch to another context

            kubectl config use-context CONTEXT_NAME
    
            # ... or with kubectx
            kubectx CONTEXT_NAME

      - switch to previous context (kubectl can't do that)
            kubectx - 

      - run a shell in a pod (pod-name - listed with $(kubectl get pods)

          kubectl -it pod-name -- bash

          kubectl -it pod-name -- sh

      - run a shell in a container cnt of a given pod (get list of containers for pod with $(kubectl describe pod pod-name)

          kubectl -it pod-name -c container-name -- bash

      - list all namespaces 

            kubectl get ns

      - switching namespaces and cluster context: (there is an nice utility for that: kubectx + kubens)

            https://github.com/ahmetb/kubectx

------

secrets

# show kubernetes 'secret' 
kubectl get secret secret-name -n netace -o json | jq '.data | map_values(@base64d)'


# in deployment descriptor: set up environment variables M_USER that take their value from a k8s secret object nm-secret


     43     spec:
     44       containers:
     45       - env:

     50         - name: M_USER
     51           valueFrom:
     52             secretKeyRef:
     53               key: username
     54               name: nm-secret
     55         - name: M_PASSWORD
     56           valueFrom:
     57             secretKeyRef:
     58               key: password
     59               name: nm-secret


=======

Show logs of all pods (name of pod/container is in each line) - and grep through them

    kubectl get pods | tail -n +2  | awk '{ print $1 }' | xargs -I{} kubectl logs --all-containers=true --ignore-errors=true --prefix=true {} | grep -i error

    kubectl get pods | tail -n +2  | awk '{ print $1 }' | xargs -I{} kubectl logs --prefix=true {} | grep -i error


Where are kubernetes logs stored?
    = on the node. !!
    - kuebelet stores them. May also do log rotation
    


=====

Need to know which node a pod is running on?
    
    # -o wide shows a column with the node
    kubectl get pods -o wide


Nodes:

    # what container engine is in use? (is it docker?)
    
    kubectl describe node 172.18.14.21 | grep Runtime
    Container Runtime Version:  docker://20.10.17

    # need to access node? ssh to it - if you know the cluster credentials

    # otherwise - create temp pod on node that can access the nodes file system.

    k get nodes
    NAME           STATUS   ROLES                      AGE    VERSION
    172.18.14.21   Ready    controlplane,etcd,worker   443d   v1.22.13

    k debug -it node/172.18.14.21 -it --image=ubuntu
    cd /host/var/lib/docker/containers
    <all the running dockers have subdirectories for each container, each one has the logs of that container>




