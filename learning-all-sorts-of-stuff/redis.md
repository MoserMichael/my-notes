
==========================

Reddis
    - does all sort of stuff (not just key value storage), 
        - they do work queues, and locks (with a specified time to life period). /what about reliability when usingg the work queue thing?/

        - https://github.com/resque/php-resque - that's a php library on top of redis lists (port of ruby library), Requests are queued as json objects. 
            Library has as a queue runner that listens on the list for jobs (maintained by github)



port forwarding to service in k8s (inner expression finds pod name from some role name that pod adheres to 

pod in cluster has redis running on port 6379 - local port is 6378 (other commands will use that number)

kubectl port-forward "$(kubectl get pods -l role=ROLE_NAME_OF_POD_IN_CLUSTER -o jsonpath="{.items[0].metadata.name}")" 6378:6379

# find a specific key

echo 'keys *' | redis-cli -p 6378 | grep  blabla
BLABLA-KEY-NAME

# check the type (this one is a list)

echo 'type BLABLA-KEY-NAME' | redis-cli -p 6378
list

# show how many elements are in list

echo 'LLEN BLABLA-KEY-NAME' | redis-cli -p 6378

# show the elements of the list between index 0 and 1 (not including 1)
echo 'LRANGE BLABLA-KEY-NAME 0 1' | redis-cli -p 6378


