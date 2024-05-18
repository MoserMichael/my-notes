
package search/searching for stuff.
=


    https://pkgs.alpinelinux.org/packages - great search for alpine!!! (whish every distro had a search page like this)

    fedora: don't know which package provides the top command???
        
        yum whatprovides top

ALPINE - list all installed packages

    apk info -vv

ALPINE - install rust with rustup
 
 # Newest upgradeables for used base image ... 
 apk upgrade --no-cache

 # libgcc - compatibility layer for libc (otherwise it searches for stuff that is not present on alpine - this one didn't work without it)
 apk add curl libgcc
 
 # using -y option, so that it does not ask any questions...
 curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s  -- -y \

 # install specific version of rust ( --defualt-toolchain)
 curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s  -- -y  --default-toolchain=1.65.0 

