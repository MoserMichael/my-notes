Mac/OSX tricks
==============


? merge two pdf files - page1.pdf and page2.pdf into page-all.pdf ?

    brew install pdftk-java

    pdftk page1.pdf page2.pdf cat output page-all.pdf

    
    or imagemagick

        # on ubuntu
        sudo apt install imagemagick

        convert image1.jpg image2.png text.txt PDFfile.pdf outputFileName.pdf

        # here: https://stackoverflow.com/questions/52998331/imagemagick-security-policy-pdf-blocking-conversion
        # had to add the following tag to 
        # sudo vim /etc/ImageMagick-6/policy.xml 
        <policy domain="coder" rights="read | write" pattern="PDF" />
        #right before
        </policymap>


? using wi-fi and no network?
    - had that I can ping 1.1.1.1 and ping 8.8.8.8  (these are very public DNS servers), but can't resolve any address (ping google.com - times out)
    - go to Settings / DNS server
        - first write down all of the configured DNS server (you may need them in some other network)
        - delete all DNS entries.
    
    worked!

? remove colorcodes from text ? 

    # kubectl get logs  - this one is returning text with color codes (i think that's very confusing). 
    # kubectl logs POD_NAME - color escape sequences everywhere...

    cat blabla.txt | sed -e 's/\x1b\[[0-9;]*m//g'

? built-in command line program does something very different from what you expect ?

    # very true for sed - will install gsed - gnu sed
    brew install gnu-sed

    gsed -i 's/blabla/blublu/g' foo.txt

    # to set it up as sed - instead of gsed (still figure the path)
    brew install --default-names gnu-sed

? force quit an application

    command + option + escape - brings up a 'task manager'

    'Activity monitor' - a better 'task manager' that shows cpu utilization, etc. (or use top)

? can't install an old php version - because it's not supported by brew ?

    brew install shivammathur/php/php@7.4

    this installs it based on https://github.com/shivammathur/homebrew-php (got a list of supported versions).

? Always show the scroll bar ?
    In the Menu bar, click Apple Menu > System Preferences.
    Click General.
    Next to the "Show scroll bars" heading, select "Always."

? Mirror displays - on Monterey ?
    
    Apple > System Preferences > Displays > select Display settings > click on Use as: "Choose Mirror As"

? who is listening on port ?

    # on Mnterey (from here: https://stackoverflow.com/questions/4421633/who-is-listening-on-a-given-tcp-port-on-mac-os-x )

    sudo lsof -iTCP -sTCP:LISTEN -n -P

? osx - find all executable blabla files (not symlinks ?

    find . -perm +111 -type f  -name blabla

? osx - find all executable blabla files or symlinks ?

    find . -perm +111 -type f -or -type l -name blabla

? sort processes by virtual memory consumption /low memory does strange things on the mac.../

   
    On Osx:
        # can use Activity Monitor - a gui app.

        # top - start and sort by memory column
        top -o mem 

        # top - batch mode: write the table once and exit
        top -b

    On Linux:
        Better: inside top, press M to sort by memory 
        press c to show command line arguments of processes.


? regex: regular expression editor (online) ?

    https://regex101.com/

    # summary of differences in syntax for regex - for different tools/languages
    https://www.greenend.org.uk/rjk/tech/regexp.html

? show process tree (on both osx and linux) ?

    htop -t

? netstat - show process names, who is listening on a given port ?

    sudo lsof -iTCP -sTCP:LISTEN -n -P
    sudo lsof -iUDP -sTCP:LISTEN -n -P

? disk space
    
    Show disk usage:
        df -a -H

    Show disk usage in directory
        du -ah  /usr/ | tail -1


    ? https://apple.stackexchange.com/questions/267165/why-is-devfs-full    
        devfs - is always full

? show memory usage in friendly terms

        # option -h is for Human friendly output !!!
        free -h

? http server with nc

    in bash shell:
        bash -c 'while true; do (echo -e "HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nMy website has date function\t$(date)\n") | nc -l 8081; done'
        curl http://localhost:8081/

? hosted in docker
    with-nc : my docker image with bash and nc :
       
    Dockerfile-with-nc 
        FROM alpine:latest

        RUN apk update && apk upgrade --no-cache
        RUN apk add -y --no-cache bash netcat-openbsd 
            
    docker build -f Dockerfile-with-nc -t with-nc .

    docker run --rm  -p 8082:8081 -it with-nc /bin/bash -c 'while true; do (echo -e "HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nMy website has date function\t$(date)\n") | nc -l 8081; done'
    curl http://localhost:8082/ 

   
    now curl doesn't exit - it doesn't get the FIN ?

? ssh access keys ?

    # generate the keypair. (entery empty keyphrase
    ssh-keygen -t rsa -b 4096 -f id_rsa -C "mmoser@perforce.com"
    # you get id_rsa (private key) id_rsa.pub (public key)

    # put the public key in authorized keys
    cat id_rsa.pub >>${HOME}/.ssh/authorized_keys

    # check that permission is 0600
    stat $HOME/.ssh/authorized_keys

    # save the keys somewhere in your reach. (id_rsa and id_rsa.pub)

    # write down the ip admin address - (gcp tells that in the console), hostname and user $USER

    # can connect with 
    ssh -i id_rsa <user>@<admin_ip>

? list installed brew packages

    brew list

    # show the stuff with a gui
    brew list --cask

? install a second version of node

    brew install node@18

    # where is the installed version?

    /opt/homebrew/opt/node@18/bin/node
    Welcome to Node.js v18.15.0.
    Type ".help" for more information.
    >

    # or set up as the default version
    brew link --overwrite node@18
    node --version
    v18.15.0


? tcpdump ?

    # just show the packets on screen (without payload)
    sudo tcpdump -i any port 9010

    # -X adds payload
    sudo tcpdump -X -i any port 9010

    # dump packets into pcap file (can view them in wireshark, or read the file with tcpdump)
    sudo tcpdump -i any port 9010 -s 65535 -w out.pcap


? wireshark ?
    don't install via brew (goes wrong) - there is an installer on https://www.wireshark.org/

