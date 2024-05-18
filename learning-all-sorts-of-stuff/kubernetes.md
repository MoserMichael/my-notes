======

Kubernetes:

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


=======

Show logs of all pods (name of pod/container is in each line) - and grep through them

    kubectl get pods | tail -n +2  | awk '{ print $1 }' | xargs -I{} kubectl logs --all-containers=true --ignore-errors=true --prefix=true {} | grep -i error

    kubectl get pods | tail -n +2  | awk '{ print $1 }' | xargs -I{} kubectl logs --prefix=true {} | grep -i error


=====

Need to know which node a pod is running on?
    
    # -o wide shows a column with the node
    kubectl get pods -o wide


