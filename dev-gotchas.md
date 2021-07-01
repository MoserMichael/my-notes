" Set text width as 72.

This is a log, here I am listing the gotchas that I stepped upon as a developer.
Maybe someone will find this to be of any use, at least it is useful to me, so as not to step onto the same rake twice; Some of the fun in programming is to have your assumptions invalidated; this is not just a cause for grieve, it is an opportunity to re-examine your assumption...

(should have started a log like this ages ago. Writing stuff down helps with clarifying the subject matter)


---01/07/21 01:43:59----------------------

The macbook keyboard is ... not very long lasting; after a year or so you get failures of some quite important keys. For me these are the arrow keys.
Apple says to blow some air at the keyboard, but my fiddling with the vacuum cleaner made it even worse ;-) 

- on GUI tools, like IntelliJ, you can keep going with the trackpad; now you have to make the scrollbar visible all the time:

```
    Select the Mac icon (in the top left corner)
    Select System Preferences
    Click on General
    Set the "Show scroll bars:" option to Always  
```

(if i could only make the track button black, so that it will always be visible at all times, but that's too much to ask for...)

- for vim there is a second workaround: in normal mode one can navigate with the keyboard: 

        hjkl  : h for left key, j for previous line, k for next line
         bw   : b for previous word, w for next word (these make for some fast navigation!)
         0    : start of line
         $    : end of line
         G    : end of file
         :0   : start of file

         
And there is much more... [more](https://vim.fandom.com/wiki/All_the_right_moves) I didn't manage to remember most of the stuff...

And you can remap some, i remapped m to page up an n to page down

```
:map , <PageUp>
:map . <PageDown>
```

but the default vim PageUp and PageDown commands suck a bit; if you do a page down and then a page up then you will not land on the same line.
So lets do some scripting:

```
:map ,  :MyPageDown<Return>
:map .  :MyPageUp<Return>


command! -nargs=* MyPageDown call s:RunMPGD()
command! -nargs=* MyPageUp call s:RunMPGU()

function! s:RunMPGD()
    let s:curline = line('.')
    let s:pagesize = winheight(0)
    let s:filesize = line('$') - s:pagesize

    if s:curline < s:filesize
       execute "normal" . s:pagesize . "j"
    endif
endfunction

function! s:RunMPGU()
    let s:curline = line('.')
    let s:pagesize = winheight(0)

    if s:curline > s:pagesize
       execute "normal" . s:pagesize . "k"
    endif
endfunction

```
i guess that's why tools like IntelliJ have a vim emulation mode - to compensate for a broken macbook keyboard, now the keyboard can go on, until the : character is no longer...

In vim one can customize everything, it just takes a lot of time to do so, and when you are done then the result feels like a pyrrhic victory...

---30/06/21 09:34:35----------------------

A unit test that starts to listen on a grpc service stub, now if you immediately start to send requests to this service stub, then on some environments the stub might not be ready yet to receive the calls; so you need to add a seconds sleep between init of the server stub and sending requests to it. Bother!

java grpc has a thread pool dedicated to it's stuff, and a threads in this pool are listening and servicing the networking calls. Now with the thread pool there can be a slight delay between initiation of something and its execution. Normally the exact point of time where a grpc service will be up is not a big concern, but when used in this unit test scenario it is an important detail.

```
   try {
            fooServiceStub = ServerBuilder.forPort(nFooPortNumber).addService(new FooServiceStub()).build();
            fooServiceStub.start();
        }  catch(IOException ex) {
            ex.printStackTrace();
        }
       
````

---30/06/21 04:39:54----------------------

Today i stumbled upon immutable lists in java. In java an attempt to modify an immutable list will throw an exception.

That is very different to immutable lists in Scala. Here the addition of an element to the list will return in a copy of the original list, with the element added (that's how they do functional programming, instead of modifying Foo, you create a copy of foo with the desired modification).

Compare all this to the C++ approach, which is still different. in C++ you can have a const references (or const pointer); if a function has been declared as const, then calling this function is not supposed to modify a given object; given a const reference one can only call the const functions of an object. (But you can have exceptions to the rule: if a member of a class is marked with the mutable keyword, then a const function can change it...)

It seems that they get less consistent about pureness and functional programming when looking at things from a lower level perspective (and more performance oriented perspective, that is)

---

Where did I stumble upon immutable lists? java grpc message objects are supposed to be immutable; you can't modify any field - if call an getter function that is returning a list, then this list is read only. If you need a slightly different grpc message object, then build a new one.


---27/06/21 04:21:10----------------------

Java has [Optional](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Optional.html) , but I didn't manage to use the option chaining feature of Optional; it has many fine points. It gets very trick if you have to think about null values (which you have to); see https://www.sitepoint.com/how-optional-breaks-the-monad-laws-and-why-it-matters/ 

Optional is still useful if you don't try to chain Option with flatMap or map.

Funny thing this optional, it was supposed to solve nullpointerexception (you either have empty or something), but it creates a set of problems on its own...

Maybe that's why they like golang, there the standard library doesn't try to be too clever; but then it doesn't have functional stream processing on containers out of the box (streams are a time saver in java and scala;  It is often less error prone to combine map/flatmap then to write a for loop).

---

https://www.sitepoint.com/how-optional-breaks-the-monad-laws-and-why-it-matters/ 

This is an important article, as it explains monads in terms that a java programmer can understand:

Here are my notes:

monads are: (hold your breath, this is an explanation for mere mortals ;-)

1. you can think of a monad as a java parametrized type  ```class Monad<T>``` with the following function
2. unit in Haskell terminology is like a 'builder' function, that takes an element of T and wraps it in an instance of Monad&lt;T&gt;
    ```public <T> M<T> unit(T element) ```
3. bind in Haskell terminology is like a flatMap  in java:  it takes a function that takes T as argument and returns Monad&lt;U&gt; -  it calls the transforming function on type U that transforms it into a different type T, and then wraps the result around the same monadic type with ```unit```.
```
public static <T, U> M<U> bind(M<T> monad, Function<T, M<U>> f) {
    return f.apply(monad.wrappedValue());
```
For example: apply for an Optional is called only when the optional has a value; for a [stream](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/stream/Stream.html) , flatMap replaces all elements of the stream with the return value of function f.

In addition to that there are the Monad laws (in Haskell terminology); these ensure that you can chain the flatMap (bind) calls together in perfect harmony:

The java Option 'monad' doesn't implement the monad laws correctly, that's why it is hard to chain processing with map/flatMap.



---26/06/21 05:41:07----------------------

While writing a recursive descent parsers:

Always ask yourself where the current position is after the end of parsing something.  This is often mixed up, when the function for parsing a term is combined with others..

---24/06/21 09:44:42----------------------

gcc on osx isn't gcc... it's clang. (hideous, when a thing called foo isn't being foo, but something else instead)

the two of them spit out the same version info.

```
gcc --version

    Configured with: --prefix=/Library/Developer/CommandLineTools/usr --with-gxx-include-dir=/Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include/c++/4.2.1
    Apple clang version 12.0.0 (clang-1200.0.31.1)
    Target: x86_64-apple-darwin19.6.0
    Thread model: posix
    InstalledDir: /Library/Developer/CommandLineTools/usr/bin

clang --version

    Apple clang version 12.0.0 (clang-1200.0.31.1)
    Target: x86_64-apple-darwin19.6.0
    Thread model: posix
```

also 

```
gcc
    clang: error: no input files0
```

brew install gcc

lets find where it is now:
```
# search for executables only, of a given pattern (on osx)
find / -perm +111 -type f -name 'gcc*' 2>/dev/null

    /usr/local/Cellar/gcc/11.1.0_1/bin/gcc-ranlib-11
    /usr/local/Cellar/gcc/11.1.0_1/bin/gcc-11
    /usr/local/Cellar/gcc/11.1.0_1/bin/gcc-ar-11
    /usr/local/Cellar/gcc/11.1.0_1/bin/gcc-nm-11
    /System/Volumes/Data/usr/local/Cellar/gcc/11.1.0_1/bin/gcc-ranlib-11
    /System/Volumes/Data/usr/local/Cellar/gcc/11.1.0_1/bin/gcc-11
    /System/Volumes/Data/usr/local/Cellar/gcc/11.1.0_1/bin/gcc-ar-11
    /System/Volumes/Data/usr/local/Cellar/gcc/11.1.0_1/bin/gcc-nm-11

/usr/local/Cellar/gcc/11.1.0_1/bin/gcc-11 --version 

    gcc-11 (Homebrew GCC 11.1.0_1) 11.1.0
    Copyright (C) 2021 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```
that's more like it.

Now there is no way to change the link in /usr/bin/gcc to the actual gcc, not even as root (not very unixy, but apple can get away with it...)

but it works in /usr/local/bin
```
ln -sf /usr/local/bin/gcc-11 /usr/local/bin/gcc
ln -sf /usr/local/bin/g++-11 /usr/local/bin/g++
```
Interesting that the brew installation doesn't come with ld; hmm...

Also you must put /usr/local/bin in the path before /bin

---22/06/21 02:41:22----------------------

the term 'opionionated' as used in software [see this discussion](https://stackoverflow.com/questions/802050/what-is-opinionated-software)

Opinionated software means that there is basically one way (the right way™) to do things and trying to do it differently will be difficult and frustrating. On the other hand, doing things the right way™ can make it very easy to develop with the software as the number of decisions that you have to make is reduced and the ability of the software designers to concentrate on making the software work is increased


[Google ngram says](https://books.google.com/ngrams/graph?content=opinionated+software&year_start=1800&year_end=2019&corpus=26&smoothing=3&direct_url=t1%3B%2Copinionated%20software%3B%2Cc0#t1%3B%2Copinionated%20software%3B%2Cc00) 

google ngram viewer says the term took off during 2003, peak usage during 2009. An often cited example of 'opinionated software' is 'ruby on rails' or 'spring boot'  (rails appeared in 2005)


[this article](https://dzone.com/articles/perils-of-opinionated-frameworks-like-spring-boot) says that spring boot is 'too opinionated'; it brings in a lot of dependencies (jpa, netty for grpc, etc. etc. etc.) he says that the choice of spring boot therefore determines a lot of choices up front... (like the versions of the dependent packages that must be used)

The opposite of 'opinionated software' is the perl philosophy of 'There's more than one way to do it' [link](https://en.wikipedia.org/wiki/There%27s_more_than_one_way_to_do_it) (or [here](http://wall.org/~larry/pm.html)

I think that 'opinionated software' often starts where there are a lot of dependencies; then comes the 'spring boot' layer on top of this mess, that also binds you to a specific way of doing things, that is supposed to make life simpler. More centralisation may bring more certainty, but it drastically limits freedom of choice.

What is the difference between a library and a framework? The framework calls your components while it starts up, it has the main function (entry point). This is also called 'inversion of control' (everything in software must have a fancy name). [Inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control) . Interesting that perl used to have a lot of libraries on cpan, but not too many frameworks. However there are 'frameworks' that don't have their own main function, for example [bootle](https://bottlepy.org/docs/dev/) in python doesn't do a thing like that (to be fair, bootle is a 'microframework' an not a proper 'framework') 

---22/06/21 01:38:59----------------------

today i learned  that okta is charging per created user https://www.okta.com/pricing/
that's how you do business, never thought of such an option...

---21/06/21 17:38:22----------------------

Magic alias that removes spaces from file names and puts _ instead of them. Works on osx!
(from [here](https://stackoverflow.com/questions/2709458/how-to-replace-spaces-in-file-names-using-a-bash-script) )

```
alias nospaceinfilenames='for f in *\ *; do mv "$f" "${f// /_}"; done'
```
Other goodies: ps sorted by cpu and memory. also less -R can browse through output with colors! (should be a default behavior, in my opinion)
```
alias pstopcpu="ps -eo pcpu,pid,user,args | sort -n -k 1 -r | awk '"'{ $1="\033[31m"$1"%\033[0m"; $4="\033[31m"$4"\033[0m"; print }'"' | less -R"
```

pstopmem_usage="list processes with top memory usage on top (first column in red)"
```
alias pstopmem="ps -eo vsz,pid,user,args | sort -n -k 1 -r | awk '"'{ $1="\033[31m"$1 / 1000"Mib\033[0m"; $4="\033[31m"$4"\033[0m"; print }'"' | less -R"
```

also it helps to have this one in your .bashrc file; puts the current git branch in the prompt, so that you don't work on the wrong branch

```
  parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
  }

  PS1="[\u@\h \W\$(parse_git_branch)]\$ "
```


---21/06/21 16:55:34----------------------

stackoverflow search got much better. Once upon a time google search was preferable, now it makes sense to use stackoverflow search...

i wonder if they are still using elasticsearch only for search. Elasticsearch used TF/IDF algorithm, but stored the word count separately for each shard, so that you often gen inconsistent search results.  (it needs and index of the frequency for each token/word to function)

Here they say that now they are also using Okapi BM25 [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/similarity.html) (but that one is also doing inverse term frequency)


---21/06/21 16:30:32----------------------

show dependecies with gradle
```
    cd &lt;directory of sub project&gt;

    gradle -q dependencies
```
keeping all the dependency versions happy is a challenge....

---21/06/21 16:14:48----------------------

On the github page: a comment with /retest will cause the CI to rerun the build and test. (/rebuild doesn't work).
This may be a feature of the particular CI scripts that we are using, don't know.

---

The CI is only keeping the standard output of gradle; here you need to find which test failed, so search for the string '() FAILED';

also one should search for STANDARD_OUT - this string marks start of each junit test; and the test runner likes to randomize he ordering of the tests...


---21/06/21 15:49:21----------------------

gradle, oh gradle.

gradle cleanTest  test --fail-fast 2>&1 | tee log.log


- without cleanTest it will not rerun the tests after a successful run (why?)
- --fail-fast tell it to stop on the first test failure (much easier to debug the tests this way).\

I have the following function in my .bashrc file (and it's always better to keep a log of that compilation/test run)

```
function makeIt {
    if [[ -f build.gradle ]]; then
        cmd=$1
        if [[ $cmd == "" ]]; then
            gradle cleanTest  test --fail-fast 2>&1 | tee log.log
            #gradle cleanTest build  2>&1 | tee log.log
        else
            gradle "$@" 2>&1 | tee log.log
        fi
    else
        if [[ -f pom.xml ]]; then
            cmd=$1
            if [[ $cmd == "" ]]; then
                mvn compile 2>&1 | tee log.log
            else
                mvn "$@" 2>&1 | tee log.log
            fi
        else
            if [[ -f Makefile  ]] || [[ -f makefile ]] || [[ -f GNUmakefile ]]; then
                make "$@" 2>&1 | tee log.log
            else
                echo "don't know how to make this, yet"
            fi
        fi
    fi
}

alias m='makeIt'
```

---21/06/21 15:47:12----------------------

java will start to omit stack traces, without this option. -XX:-OmitStackTraceInFastThrow

Why did they do that? Why?



