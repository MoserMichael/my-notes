" Set text width as 72.

My [linkedin profile](https://www.linkedin.com/in/michael-moser-32211b1/) 

This is a log, here I am listing the gotchas that I stepped upon as a developer.
Maybe someone will find this to be of any use, at least it is useful to me, so as not to step onto the same rake twice; Some of the fun in programming is to have your assumptions invalidated; this is not just a cause for grieve, it is an opportunity to re-examine your assumptions, which is a good thing.

(should have started a log like this ages ago. Writing stuff down helps with clarifying the subject matter)


---11/12/21 13:01:21----------------------

I am a long time reader of [hacker news](https://news.ycombinator.com/news), It's an incredible source of information, but it too has its editorial biases. For example this [hightly interesting discussion](https://news.ycombinator.com/item?id=29505524) appeared on the front page the other day, but then suddenly disappeared from the front page again, and also from any other page that appeared in the vicinity of the front page on that day. I am not quite sure, as to why that happened.

Anyway, it's probably time to diversify my information diet, and the source is right here! When logged into github, the main page is showing all the repositories, that were recently starred by any github user, who got a star from me. That is an excellent source on what is happening here! And so it goes, that I am starring everyone, who was so kind to put a star on any of my projects, partially out of curiosity, and a desire to learn new stuff.

You might also want to look at one the scripts that I wrote recently, [Here](https://github.com/MoserMichael/MoserMichael), this [script](https://github.com/MoserMichael/MoserMichael/blob/master/build-local.sh), is a building a README.md file, that is appearing on my github profile, by virtue of naming the repository after my github user. All this is run as a [github action](https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions) - as a continuous integration process, hosted by our (hopefully) benevolent hosts here. (More details in the [about page](https://github.com/MoserMichael/MoserMichael/blob/master/ABOUT.md))

One of the generated reports is a [report of every repository that got a star from me](https://github.com/MoserMichael/MoserMichael/blob/master/USER_STARRED.md). 

Thank you all for keeping me up to date, on what is going on!

Clicking on the image will open a youtube video with the song 'Thank you all' by the 'Free Design'

[!['Thank you all' by the 'Free Design'](https://img.youtube.com/vi/vvLO1i0mTIo/0.jpg)](https://www.youtube.com/watch?v=vvLO1i0mTIo)

"Think and dream and share your mental wealth/The world is out to get us, but it can't/Because we're friends!"

---22/11/21 06:08:24----------------------

I am dabbling quite a bit in Python, in my public repositories, here on github. Python feels sometimes like a kind of lisp, Peter Norvig is often quoted of having [said so](http://norvig.com/python-lisp.html). There are some similarities, due to python being very dynamic and expressive /also if you ask me: you need to overcome some barrier of entry with the syntax (for python it's that spaces have some real meaning, for lisp it's the nesting of lists), You are fine with both lisp and python, once you have overcome these difficulties/

One area where python is not lisp - python is not [Homoiconic](https://en.wikipedia.org/wiki/Homoiconicity). This means that a python program can't be manipulated as python data. As a result, the python interpreter [cpython](https://github.com/python/cpython) needs to do quite a bit of parsing, it is time to look a bit at parsing in general and in the world of python.

Parsing comes in two stages: often there is a first stage, called [lexical analysis/tokenization](https://en.wikipedia.org/wiki/Lexical_analysis) where the input text is broken up into tokens like keywords, identifiers and comments, and a second stage called [syntax analysis](https://en.wikipedia.org/wiki/Parsing#Computer_languages), where they take the tokens as input, and build an [abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree), that shows the structure of the program. (in a homoiconic programming language, you would get the abstract syntax tree for free, in the form of the data structure that expresses the program)

Now some parsers try to do without the lexical analysis stage, for [parsing expression grammars (PEG)](https://en.wikipedia.org/wiki/Parsing_expression_grammar) are a type of top-down parsers that are famous for doing without a lexical analysis stage, but the result turns out to be a bit awkward:

I think that peg parsers have a lot of problems:

  - one problem; you need to deal with comments as part of the grammar, That can be a bit of a problem, as comments may appear just about everywhere. One way to fix that problem with PEG parsers is to have a filter stage, that removes tokens from the input, before they are handled by the parser, That would be a kind of preprocessor similar to lexical analysis: lexers are eating up comments, and just don't pass them on as tokens.
  - the peg parser needs to do a lot of backtracking, partly to resolve ambiguities between tokens - an example ambiguity between tokens: an identifier be identified by a regular expression ```[A-Za-z]([a-zA-z0-9\_]*)``` , now this regular expression can also scan about every keyword.
  - it needs a lot of lookahead, a whole lot.

Still the grammar for peg parsers is much more intutitive, and you don't have to fight shift/reduce and reduce/reduce conflicts (like with yacc/bison), or indulge in other workarounds.

Anyway, lets look at what [cpython](https://github.com/python/cpython) is doing: before python 3.9 had a simple grammar, the ideal was to have a LL(1) grammar, you would just look at one token, in order to decide what clause will be parsed. In practice they had a couple of workarounds, still it was an LL(k) grammar, one that can be parsed with a fixed number of lookahead symbols. up to python 3.9 the grammar was defined [here](https://github.com/python/cpython/blob/3.8/Grammar/Grammar) and it had a lexical analysis stage with tokens defined [here](https://github.com/python/cpython/blob/3.8/Grammar/Tokens) Most of the parser would be translated to a [finite automata](https://en.wikipedia.org/wiki/Finite-state_machine), that would be used for the syntax parsing.
With python 3.9, the default parser is generated from [this grammar definition](https://github.com/python/cpython/blob/3.9/Grammar/python.gram), and it is generated into a PEG parser. Note that all the keywords are defined as string constants, that appear in the grammar definition file.

Lets build cpython on the mac:

On the mac you first need to get openssl, as a prerequisite.
```brew install openssl```

Then get the sources and build it

```
    git clone https://github.com/python/cpython.git cpython
    cd python

    # for 3.8 (still has the old dfa based parser)
    git checkout origin/3.8 -b 3.8
    ./configure --with-pydebug --with-openssl=$(brew --prefix openssl) CC=clang

    # for 3.9 (uses a new peg based parser)
    git checkout origin/3.9 -b 3.9
    ./configure --with-pydebug --with-openssl=$(brew --prefix openssl) CC=clang

    make -s -j2
``` 

Anyway, i think that parser speed is not that important to python - in the end, most of it ends up being translated into bytecode files with extension *.pyc, and the same bytecode files are used for subsequent runs of the same program. What really matters, is the speed of the runtime interpreter that runs the bytecode, that's where most of the time is being spent.
The Python developers argue, that the PEG parser is within 10% speed of the previous table based parser. One reason being that the in-memory syntax tree produced by the peg parser doesn't need to be post processed. (I would guess, that the parser performance assessment would actually depend on many factors, like most things in software).

What is interesting, is that the switch to the PEG based parser in python 3.9 coincides with a whole set of changes in the python syntax [here](https://docs.python.org/3/whatsnew/3.9.html). Apparently it has become easier to add stuff to the language. I suspect, that this factor is the real motive behind the big switch in parsers.

For more info see [here](https://lwn.net/Articles/816922/) and [here](https://www.python.org/dev/peps/pep-0617/).

Also, the switch in parsers almost coincides with a change in governance of the python project [here](https://www.infoworld.com/article/3292936/guido-van-rossum-resigns-whats-next-for-python.html), maybe there is some correlation here, go figure...

---

I am not sure if the analogy between python and lisp is the correct one. Python is all about its object system, now just look at python meta objects; these are said to have come to us from smalltalk. So it would be fair to say that Python has a very strong ancestry in Smalltalk. Interesting that the wikipedia article on Python is not listing Smalltalk as having had an influence on python [here](https://en.wikipedia.org/wiki/Python_(programming_language))
On the other hand: smalltalk was very much influenced by Lisp, so they say. So maybe that was the meaning of this comparison...

Now here is my attempt to understand the python object modell, the [Python object primer for python3](https://github.com/MoserMichael/python-obj-system) . Let's see how that works out...

What i learned from this: Python's metaprogramming facilities are built around metaclasses and decorators (these are explained in the linked course).
These tools are built around reflection, and the dynamic nature of python. It is possible, that this is enough to offset the lack of being a homoiconic language, i am not sure about this...

---08/11/21 03:33:18----------------------

I was plagued by garbage characters appearing in vim. 
Actually i never get this on linux, only on the mac.
To fix this problem somehow, i redefined ctrl+a to redraw the screen

```
:vnoremap <C-A> <Esc>:redraw!<Return>

:inoremap <C-A> <Esc>:redraw!<Return>i

:nnoremap <C-A> :redraw!<Return>
```

Luckily there is a fix for that explained [here](https://stackoverflow.com/questions/21618614/vim-shows-garbage-characters)
Now if you get this problem, then put this into your ~/.vimrc , it helps with the problem!

```
if has('mac')
:set t_RV=
endif
```

What would i do without stackoverflow... 

Nope, i still need the shortcut on occasion, especially when searching for a string, the screen doesn't always get redrawn....

---06/11/21 09:37:45----------------------

Today i learned, that google is tracking your entire browser history in Chrome, is tracking your every move via android, is also recording your voice (not quite sure what is being recorded), among other things...  It says that you can disable this [here](https://myactivity.google.com/activitycontrols); though i am not entirely sure if you can trust that statement.

See more [here](http://jaruzel.com/blog/how-much-does-google-know-about-me)

That's what I call 'opinionated snooping', the default is to track your every move. In a way I am glad, that i failed to pass the google hiring process, when I tried.
I really wouldn't like to be part of these games, even though they are probably a cool place to work for. This mega corporation seems to have a vision of things, which is not quite pleasant: i mean the statement 'dont be evil' depends on your particular definition of evil. (I guess they would regard a bad financial quarter as very evil)

Among other things I learned: it turns out that Orwell did get a lot of ideas for '1984' from Zamyatin's 'We'; see [Orwell's review](https://orwell.ru/library/reviews/zamyatin/english/e_zamy) Also [here](https://www.nytimes.com/2021/11/02/books/review/yevgeny-zamyatin-we.html). I didn't quite find '1984' to be very convincing, when I read it; maybe Orwell did not experience too much of socialism, when he was in Spain, during the civil war there; however 'We' was much more real to me, when I was growing up in the German Democratic Republic, aka East Germany.

Sorry for all of the politics, this was meant to be a professional blog. Well, I think there is no way to get around that...

--

Here is a good one: 'there ain't no anti-utopia, that our current elites wouldn't want to implement for real' [source](https://www.anekdot.ru/id/1262613/)

Unrelated: I made a crawler generated web page, that lists flagged submissions and comments from [hacker news](https://news.ycombinator.com/news)  Here is the result: ['red flagged hacker news'](https://mosermichael.github.io/flagged-hn/page_1.html) and the crawler for this stuff is [right here](https://github.com/MoserMichael/flagged-hn/)  (I tried to make the logo look like that of the GDR newspaper the 'Neues Deutschland', giggle)

Update: google at least gives you an 'opt out' clause (not sure if they really do an opt out, or if they have to keep the data because of some other considerations), other giants of the surveillance industrial complex don't do that (facebook doesn't have an opt-out clause, for that matter)

--

A friend of mine managed to appeal a parking ticket, based on the location data that is tracked by android snooping. Maybe he is right and i am wrong, maybe we get a good deal, by giving up our privacy in return for a better content suggestion on youtube, or, as in this case, in return for the ability to proove our whereabouts, when needed.
However me doesn't want to feed the monster with more data than it is necessary, also everything that 'listens and looks' aka. ['Horch und Guck'](https://langua.de/synonym/VEB%20Horch%20und%20Guck) is just a bit too frightening, at least to me.

--

At least vim isn't calling home (unlike visual studio code, with it's telemetry).

Anyhow: I have a vim plugin that uses openssl to encrypt a file with a symmetric key (aes-256 or other ciphers) [link](https://github.com/MoserMichael/vimcrypt2), that works for me.

This can be used to keep your own private notes secured while saved on disk/save at rest (well, they can still put up a keylogger, or read the editors memory, if they really bother)

Anyhow, this vim plugin is a kind of technological fix, for a problem that is posed by society. (Well, most of the entries in this log go with 'here is a script to fix your woes' ;-)

---25/10/21 14:43:56----------------------

While monitoring a log file that is changing;

```tail -f mysterious-log-file.log | grep --line-buffered SEARCH_TERM```

```tail -f``` shows any  changes of the log file, now without the ```--line-buffered``` argument on grep, you will not get an update of any new events. (stepped on this several times, let's see if I remember it the next time)


---10/10/21 04:46:52----------------------

I made a [presentation](https://www.youtube.com/watch?v=7ug8cWKAuO8) for the gitblame vim plugin [link to project](https://github.com/MoserMichael/gitblame)

Now making a presentation based on screen recording is not quite a trivial thing to do on a mac, there are many options here:

- quicktime can record the screen, but your video will be without sound (at least I didn't manage to record with sound)
- There are several screen recording programs that claim to be free, but it's only a demo version that requires you to pay for a license.
- Both zoom and slack could possibly do it, but I didn't manage to make it work. Once upon a time there was google hangouts, where you could do a screen recording. However this product was discontinued by google, for whatever reasons.
- Didn't manage to use ffmpeg and gstreamer, though I had some fun with gstreamer, while trying: this command gives you a distorted mirror, quite funny: ```gst-launch-1.0  avfvideosrc device-index=0 ! videoconvert ! warptv ! videoconvert ! autovideosink```
- Now what really worked for me is the [Screen recorder for Chrome](https://chrome.google.com/webstore/detail/screen-recorder/hniebljpgcogalllopnjokppmgbhaden) This plugin is really free (right now) and it allows you to record a particular window (not the whole screen). You can also pause and resume the recording, which is very useful for someone like me, who is not a seasoned presenter.

Lots of options here. It took me some research to find something that works for me, as usual...

---

Another neat Chrome browser plugin is [Markdown Preview plus](https://chrome.google.com/webstore/detail/markdown-preview-plus-dz%E7%89%B9/mbbfdipmmlbkfdkeklpioafmdcodhfli) ; it allows you to view local markdown files in Chrome, rendered as html. After installation, you need to visit the url chrome://extensions/, press on details for 'Markdown Preview Plus' and enable the option 'Allow access to file URLs'. Works like charm (previously, i was pushing a change to a markdown file to github, just to view the change rendered, that creates very convoluted commit history, mind my French ;-) )

---05/10/21 02:38:15----------------------

It is possible to use the [jdb](https://docs.oracle.com/javase/7/docs/technotes/tools/windows/jdb.html) debugger, in order to get a stack trace of a java thread that got stuck, for a process running in a container of a pod of a kubernetes cluster. Every tool has its uses...

On the server side:

- The java process needs to be invoked with the following command line arguments: ```-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=8000``` this means that the process listens on port 8000 for remote debugging requests.
- The kubernetes cluster needs an ingress on port 8000

On the client side; 

- forward the debugging port to the pod that contains the java process that is to be debugged. ```kubectl port-forward POD_RUNNING_JAVA -n POD_NAMESPACE 8000:8000``` While forwarding is running in one console, start a new console to run the following commands:
- Run jdb and attach it to the process via the port: ```jdb -attach localhost:8000 ```
- run the following commands iin jdb: ```threads``` - this one is listing all threads are listed in the form ```(<Thread_name>)<thread_id>``` where the thread_name is what you pass to ```Thread.set_name```
- ```suspend``` - suspend all running threads.
- ```where <thread_id_hex>``` show stack track of remote thread

```jdb``` is a very low level java debugger, but it has it's uses.

<---10/09/21 14:26:50----------------------

One interesting aspect in software development is [Software rot](https://en.wikipedia.org/wiki/Software_rot), or otherwise known as bit rot. 

I came across this thing in one of my project, [kind-helper](https://github.com/MoserMichael/kind-helper). The project is a helper script for setting up a kubernetes test cluster with the kind utility. One of the features of this project is to set up an ingress (you can optionally set up a tls/https ingress). The problem was, that the format of the ingress object changed, therefore the whole edifice seized to work. 

However I did make some use of [github actions](https://github.com/features/actions) - they give us the chance to set up a continuous integration environment, that may test a github probject with public access on a regular basis. I have managed to use this feature, granted to us by our benevolent owners, in order to test the kind-helper project on a regular basis. Therefore I have managed to get some notice of the fact, that the integration tests for this project seized to work. Now if you ever find someone bitching about automatic tests - like unit tests/integration tests, then my response would be, that this technique will give some notification of any changes in the environment, which may affect your software. I think that that there are a lot of possibilities for environmental changes, most of them come down to changes in dependencies (libraries or components that your components depend on). These changes are a very frequent cause of errors in software development.

---26/08/21 23:16:37----------------------

I am looking a bit into the Rust programming language; i think it is interesting that this language did not gain wider acceptance until 2021, right now there are very few job openings that require Rust.

Compare this to golang, which did gain widespread acceptance between 2012 and 2021 (in 2012 they had version 1.0 of golang released); Rust's version 1.0 came out in 2015.

What they have in common

* Both languages have a killer feature over their competitors.
    * Golang is competing with the JVM platform; golang has go routines (easier concurrency with n:m threads, n cooperative threads running in m operating system threads) and compilation to standalone executables (unlike JVM based languages it does not have the start up time, when the program is running in interpreted mode, without having completed just in time compilation); Golang is competing with Java/JVM based languages for application server stuff.
    * Rust is competing with C++, has the killer feature of save code, a guarantee against buffer overflows in save code. Rust has a very rich syntax, it is inspired by Ocaml, it has a switch statement that can do deep pattern matching (like in Scala), and has a very flexible macro facility.
    
    
Where are the differences?
* It is very easy to pick up golang for someone who has worked with java, It has the backing of Google, which has a lot of clout in software development (even though they are not known as development tool vendors)
* Rust is introducing very new features, and has a steeper learning curve. Also Mozilla fired the team responsible for developing Rust in 2020 [here]( https://en.wikipedia.org/wiki/Rust_(programming_language)#History) - it was later picked up by the Rust foundation, but the whole process raised doubts abut the future of Rust.
* I think that golang has a better defined niche with a lot of demand; it is targeting server software development in a managed language; The niche of Rust would be security sensitive code running as a native executable, but also server code that has to be secure and better performing than managed code. I guess perceived ease of development and deployment wins over more efficiency and more secure code.

I suspect that there are several factors that determine programming language adoption
* The viability of the platform,
* The availability of programmers for a programming language is the single most important factor in programming language adoption. I think the continued popularity of C++ and Java has much to do with the fact; an enterprise wants to treat programmers as interchangeable screws, and a less widespread programming language would make this practice much more difficult.
    * C++ was designed to be easier to learn by means of backward compatibility with C; This decision was good for programming language adoption; it was a good trade off, even at the expense of being a source of many issues with the language.

Interesting corollary: I think that an enterprise with a less common programming language (like Scala or Rust), would have to treat its programmers much better than a competing shop that uses a commonly used platform like Java or C++; they have a greater investment in their workforce, due to the language/platform issue, are probably more likely to raise salaries every now and then and would be less likely to 'hire and fire'... 
    
---

Still, i think that Rust will gain some acceptance, at some stage. Consider these projects: [rustls](https://github.com/rustls/rustls) and [ring](https://github.com/briansmith/ring) ; they aim to reimplement libssl/libcrypto in Rust, so that you will not be likely to see any buffer/stack overruns...

---13/08/21 14:31:52----------------------

Other essential kubectl commands, really helpful ones for solving real problems with kubernetes usage.

This lists all events that happened in the namespace; Pods starting and crashing, etc. etc.

```kubectl get events -n NAMESPACE``` 

What is going on with my pods? Who is crashing and restarting?
This lists all the bad things that happened in the namespace;

```kubectl get events -n NAMESPACE | grep -i failed```

This shows all the logs in a container of the crashed pods (name of crashed pods is in the event log produced by previous command); 
note that you have to give the name of a container name. 

```kubectl logs --previous POD-NAME-OF-CRASHED-POD  -n NAMESPAE -c CONTAINER-NAME-IN-CRASHED-POD```

If you don't know the name of a container in the pod, then then the following command will remind you:

```kubectl logs --previous POD-NAME-OF-CRASHED-POD  -n NAMESPACE```

Now there is the command of pure magic, this one gives you an ssh shell to a container in a running pod.

```kubectl exec --stdin --tty POD-NAME -c CONTAINER-NAME -n NAMESPACE -- /bin/bash```

Of course this command may fail, if the container does not have the bash shell installed. In this case, the following command tells you which shell is installed (doesn't work if the container does not have a shell installed, which also happens)

```kubectl exec --stdin --tty POD_NAME -c CONTAINER-NAME -n NAMESPACE -- echo $SHELL```


---27/07/21 03:04:38----------------------

The following code used to work in python2.7, but it doesn't work in python3.

You can't iterate over the keys of a dictionary in python3, and modify the underlying dictionary within the loop.

In python2 this worked just fine: the method keys() of type dict was returning a list object that is holding a copy of the keys 


in python3 they return a special set like view into the keys of a dictionary, this set is of type [dict_keys](https://docs.python.org/3/library/stdtypes.html#dict.keys), this speeds up iterating over the keys of a dictionary, but now you can't modify the collection while iterating over it.

```
map={ "first":1, "second" : 2, "third" : 3 }

print("keys type: {}".format(type(map.keys())))

for k in map.keys():
    if k == "second":
        # in python3 this gives the error; RuntimeError: dictionary changed size during iteration
        del map[k]

print(map)
```

In python3 you have to copy the keys explicitly into a list, to get the old behavior.

```
map={ "first":1, "second" : 2, "third" : 3 }

print("keys type: {}".format(type(map.keys())))

for k in list(map.keys()):
    if k == "second":
        del map[k]

print(map)
```

Also the built-in ```map``` function returns an iterator like object, so that it does lazy evaluation in python3, in python2 you would get a list as return value.
This has the advantage that the result of map is evaluated lazily, only when it is needed. On the other hand you can iterate only once over the result of ```map```, unlike python2.
```
def inc(x):
    print("calling inc with ", x)
    return x + 1

res = map( inc, [1,2,3] )

print("return type of map", res)

print("first iteration:")
for n in res:
    print(n)

print("second iteration:")
for n in res:
    print(n)
```

I used to step onto this rake repeatedly in the past, let's see if writing it down will prevent a similar repetition in the future....
Another lesson: some say that 'python is easy', however python keeps changing with every major and minor release, which is confusing (perl5 doesn't do so, therefore perl scripts have a better chance to keep running without change; There comes a trade off with every decision, in the land of computers...
Similar trivia: range used to be [function](https://docs.python.org/2.7/library/functions.html#range) in python2.7 that used to return a list of numbers in python2.7, in python3 it is a type constructor that is returning a [range](https://docs.python.org/3/library/stdtypes.html#range) object, this uses much less memory.

A good collection of differences between python 2 and python 3 is [here](https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#bankers-rounding)

---

I later wrote this article on the python module system [here](https://github.com/MoserMichael/pythonimportplayground)

---22/07/21 04:05:11----------------------

Wrote a python script that gathers logs in order to identify a situation described in the previous entry [link to script](https://github.com/MoserMichael/myenv/blob/master/scripts/follow-kube-logs.py)

The scripts help text:
```
usage: follow-kube-logs.py [-h] [--namespace NAMESPACE]
                           [--deployment DEPLOYMENT] [--stset STATEFULSET]
                           [--rset REPLICASET] [--out OUTDIR]
                           [--kubectl KUBECMD] [--trace] [--complete-bash]
                           [--complete]

This program starts to follow the logs of containers in all pods of a
kubernetes deployment/replicaset/statefulset. The output is written to a file
per container. The script then waits for user input, logging is stopped once
the user has pressed enter.

optional arguments:
  -h, --help            show this help message and exit

log  pods/containers in either one of deployment/replicaset/statefuleset:
  --namespace NAMESPACE, -n NAMESPACE
                        optional: specify namespace of deployment (default: )
  --deployment DEPLOYMENT, -d DEPLOYMENT
                        name of deployment (default: )
  --stset STATEFULSET, -s STATEFULSET
                        name of statefull set (default: )
  --rset REPLICASET, -r REPLICASET
                        name of replica set (default: )
  --out OUTDIR, -o OUTDIR
                        mandatory: name of output directory (default: )
  --kubectl KUBECMD, -k KUBECMD
                        optional: name of kubectl command (default: kubectl)
  --trace, -x           optional: enable tracing (default: False)

suport for bash autocompletion of command line arguments:
  --complete-bash, -b   show bash source of completion function (default:
                        False)
  --complete, -c        internal: used during code completion (default: False)
  --kubectl KUBECMD, -k KUBECMD
                        optional: name of kubectl command (default: kubectl)
```

So that by running ```./follow-kube-logs.y -n my-namespace -p my-deployment -d logdir``` you will create directory logdir, it will create a subdirectory for each pod running in the deployment my-deployment in namepace my-namespace and spawn a process that follows the logs of each of the containers for that pod, to gather the logs for that container, while the script is running. The script then waits and asks for the user to press enter, whereas it will kill the spawned processes and stop the logging.

The purpose of this script is to be a more lightweight solution then to use prometheus/graphana for viewing your deployment logs, as it is sometimes easier to grep through the logs, as compared to writing elaborate prometheus queries.

In a way kubernetes is our generations jcl (job control language on ibm mainframes) ; There is a remote similarity in how we are writing descriptors for tasks and then submit it for execution and wait till the mainframe/kubernetes cluster has considered our specification. (suddenly feeling old because of this comparison ...)

update: changed the script, now it scans the deployment once per second for changes, new pods are logged too. 

update: added command completion, now to enable command completion, place the script in the path and run
```  follow-kube-logs.py -b >>$HOME/.bashrc ```

update: made a repository for this script [link](https://github.com/MoserMichael/follow-kube-logs)

---19/07/21 03:25:02----------------------

Another well known rake: a client library that does it's own caching is used in an implementation of a service that runs in multiple instances.

Instance A gets a modify foo request, followed by a get foo request, naturally the modification of foo will put the correct result in the cache of A, so that the subsequent get request will return the correct value. Instance B receives a get request for foo and returns the cached incorrect value of foo.

Recently stumbled at this with the [Okta java sdk](https://github.com/okta/okta-sdk-java) - here it was not obvious that the client is doing its own caching. (another rake: the github project does not include all the sources, like very important classes like DefaultClient and DefaultUser; luckily you can see them with any good java decompiler, like IntelliJ)

Luckily it is relatively easy to cancel the caching, by supplying a custom CacheManager instance to ClientBuilder, one that does return a non-caching Cache instance on each request)

Another interesting case is the aws KMS client, that has it's own cache, but where there is no set default for the cache expiration; so that i ended up with a cache that does not do any caching....

---
actually this would be some interview question: 'how would you deal with a caching client library used in a multi pod deployment of a service, describe the problem scenario and solution', as there is more then one way to solve this problem.

- One could cancel caching of the client.
- in the case of Okta: one could rewrite the code to use the REST api - this doesn't come with its own client side caching.
- One could use a special router to route all requests to change any specific entity to the same service instance
- one could write such a routing logic as part of the service, and delegate work with the caching client to a third service, based on this logic.
- etc. (probably a few other approaches as well).

(hope that i won't have to answer my own job interview questions any time soon, interviewing for a job gives me post traumatic stress disorder ;-)

---07/07/21 04:54:26----------------------

Difference between java streams: map and forEach.

I recently had the following pipe in a java program:
```
var result = myList.stream().map(...).filter(...).collect(Collectors.toList());
```
Now  after some revision it changed to
```
 myList.stream().map(...);
```
Now that one is never executed. The error of course is that this statement does not produce a return value, the return value is not used and therefore ignored, and that's the reason why the statement is never executed.
The source of this error, of course is that map may not be fully funnctional in that it may call other functions that do thinks like storing records in a database (an implicit side effect that doesn't modify any variable) That's the reason why they have forEach - this construct doesn't have a return value and is not ignored, as a result....

That's part of the fine print of mixing functional and object oriented paradigms.

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

function! RunMPGD() 
    let s:pagesize = winheight(0)
    let s:filesize = line('$')
    let s:topline = line('w0')

    let s:move = s:pagesize  
    if s:topline + s:pagesize > s:filesize
        let s:move = s:filesize - s:topline
    endif

    "execute "normal" . s:move . "j"
    let s:curline = line('.') + s:move
    let s:col = col('.')
    call setpos(".", [0,  s:curline, s:col ] )
endfunction

function! RunMPGU() 
    let s:curline = line('.')
    let s:pagesize = winheight(0)
    let s:topline = line('w0')
                
    let s:move = s:pagesize
    if s:curline < s:pagesize
        let s:move = s:curline
    endif

    let s:curline = s:curline - s:move
    let s:col = col('.')
    call setpos(".", [0,  s:curline, s:col ] )
endfunction

```
i guess that's why tools like IntelliJ have a vim emulation mode - to compensate for a broken macbook keyboard, now the keyboard can go on, until the : character is no longer...

In vim one can customize everything, it just takes a lot of time to do so, and when you are done then the result feels like a pyrrhic victory...
One problem is that i don't know how to scroll in visual mode, so that the selection is still kept...

----

Several months later I found the solution of how to keep the selection in visual mode too [source](https://vi.stackexchange.com/questions/8335/how-to-i-get-around-normal-exiting-visual-mode/8336). Maybe it would have been easier to buy an external keyboard, rather than to compensate
for this problem with scripting...

```
:vnoremap ,  :call RunMPGDV()<Return> 
:vnoremap .  :call RunMPGUV()<Return>

function! RunMPGDV()
    normal gv
    call RunMPGD()
endfunction

function! RunMPGUV() 
    normal gv
    call RunMPGU()
endfunction

```

----

Another interesting problem: VIM MAPS j to scrolling down, whereas me would find it more natural to scroll up. I left it as is as an exercise: how easy will it be for me to adjust to a changed assumption in an ingrained cognitive bias. The experiment is still ongoing...

----

You can also use vim instead of less:

So instead of

``` find . -name foo | less```

It is now

``` find . - name foo | vim -```

So it is the following alias for me, note that vim doesn't quite work with color escapes, so lets fall back to less when colors are asked for:
Some people advise to use the AnsiEsc vim plugin for color escape codes, but this didn't work for me.

```
function _less {
    local arg="$1"
    if [[ "$arg" == "-R" ]]; then
        less -R
    else
        vim -
    fi
}

alias less=_less
```

One downside: this version of less will wait for the program to complete, before it shows anything. So it is not quite ideal for very long running programs. Everything seems to have its caveats, in the land of computing...

----

Another well kept bash secret is to use Ctrl-r for searching the command history




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
       
```

---
it's amazing how much of my time at work is spent with dealing to fix failures that happen during CI tests. 
You sometimes got amazingly different behavior of the test environment on your local machine vs the environment on the CI environment; often these can be explained due differences of dealing with timeouts, or not waiting enough for some service, etc.


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

So that Optional is an 'almost monad' and java streams are full monads [explained here](https://stackoverflow.com/questions/20943094/are-the-streams-in-java-8-monads)

Here are my notes:

monads are: (hold your breath, this is an explanation for mere mortals ;-)

1. you can think of a monad as a java parametrized type  ```class Monad<T>``` with the following function
2. unit in Haskell terminology is like a 'builder' function, that takes an element of T and wraps it in an instance of Monad&lt;T&gt;
    ```public <T> M<T> unit(T element) ```
    - for optional: unit is [Optional.ofNullable](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html#ofNullable-T-) ; this function makes an empty Optional for null argument, and wraps a non null argument in a non empty Optional value.
    - for stream: unit is  [Stream.of](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html#of-T-) (? what about Stream.of(T ...values) ?)

3. bind in Haskell terminology is like a flatMap  in java:  Bind receives a function f as argument, f takes an instance of T as argument; bind applies f to the Monad&lt;U&gt; 
    - For java Optional bind (aka flatMap) extracts the contained T value, if it is present, and applies f to it. 
    - for java Stream bin (aka flatMap) for each element of the stream, apply f to the element and paste the result of applying f into the output stream. (example; if f is the identity function, then this will turn a list of lists into a simple list that is the concatenation of all the list elements) Interestingly this is different from the bind in the previous example, where the result is a plain value of T, and here it is a Monad&lt;T&gt; by itself; confusing...
    

```
public static <T, U> M<U> bind(M<T> monad, Function<T, M<U>> f) {
    return f.apply(monad.wrappedValue());
```
For example: apply for an Optional is called only when the optional has a value; for a [stream](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/stream/Stream.html) , flatMap replaces all elements of the stream with the return value of function f.

In addition to that there are the Monad laws (in Haskell terminology); these ensure that you can chain the flatMap (bind) calls together in perfect harmony:

The monad laws:

1. Left identity law: bind(unit(value), f) === f(value)


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

---

Another big one: the built-in sed on the mac is kind of weird: it adds a trailing newline on every file, and is acting weird in every other sense as well.

Luckily we can install the regular gnu sed. ```brew install gnu-sed``` now you have to invoke it as gsed. 

---22/06/21 02:41:22----------------------

The term 'opionionated' as used in software [see this discussion](https://stackoverflow.com/questions/802050/what-is-opinionated-software)

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

The ultimate refactoring tool: search and replace a string for all files under git:

```
git ls-files -z | xargs -0 sed -i -e "s/FROM_STRING/TO_STRING/g" 
```

now for osx you need to use gnu sed, and not the built in one, as mentioned previously. [This script](https://github.com/MoserMichael/myenv/blob/master/scripts/gitreplace.sh) takes care of it.


---21/06/21 16:55:34----------------------

stackoverflow search got much better. Once upon a time google search was preferable, now it makes sense to use stackoverflow search...

i wonder if they are still using elasticsearch only for search. Elasticsearch used TF/IDF algorithm, but stored the word count separately for each shard, so that you often gen inconsistent search results.  (it needs and index of the frequency for each token/word to function)

Here they say that now they are also using Okapi BM25 [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/similarity.html) (but that one is also doing inverse term frequency)


--- 
Another useful tool is [github code search ](https://github.com/search) especially if you use a few of the search operators [explained here](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-code)

One interesting usage, besides searching for a code pattern, is to search for interesting projects on github; also see [searching for repositorie](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-for-repositories) and [searching for topics](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-topics)

[```stars:>=10 language:cpp in:readme games```]( https://github.com/search?q=stars%3A%3E%3D10+language%3Acpp+in%3Areadme+games&type=Repositories )  this searches  for projects that have more than ten 'stars', are using the c++ programming language, and have the word "games" in the readme.


[```https://github.com/search?p=4&q=%22curated+list%22&type=Repositories```](https://github.com/search?p=4&q=%22curated+list%22&type=Repositories) searching for repositories with the phrase 'curated list' gives you a lot of cool link collections.

[```https://github.com/search?q=type%3Auser+followers%3A%3E1000```](https://github.com/search?q=type%3Auser+followers%3A%3E1000) this query gets you a list of celebrity github users with more than 1000 likes.



---

What we learned from this: being a software developer means to be a master in the art of searching for stuff. I think that [Google Fu](https://www.urbandictionary.com/define.php?term=google-fu) is no longer sufficient, as the web has grown too big for one single company to handle (or maybe the focus of our masters at the big search company has changed, no way to be sure on that). 

---21/06/21 16:30:32----------------------

show dependecies with gradle
```
    cd <directory of sub project>

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
    beep.sh
}

alias m='makeIt'
```

the m alias runs the relevant build command in the current directory; writes a file with the output, and makes a [beep](https://github.com/MoserMichael/myenv/blob/master/scripts/beep.sh) at the end; this signals to to get back from [swordfighting](https://xkcd.com/303/)

---

i have also written this script, which is github specific: [makepr.py](https://github.com/MoserMichael/githubapitools/blob/master/makepr.py) It automates creation of pull request, waits until the continuous integration build for the top commit has completed, then notifies you upon completion of the build.

---21/06/21 15:47:12----------------------

java will start to omit stack traces, without this option. -XX:-OmitStackTraceInFastThrow

Why did they do that? Why?

Another big thing is -XX:CompileThreshold

It turns out that this value is 10000 on HotSpot server, this means that a java function is just in time compiled only when it has been executed for 10000 times.

See [this link](https://jpbempel.github.io/2013/04/03/compilethreshold-is-relative.html)  

That's one of the advantages of golang, here there is no hard to predict just in time compilation, everything is compiled up-front, there is less of this strange warm-up time after starting a service. On the other hand, golang has executables of enormous size.

```
$ which kubectl
/usr/local/bin/kubectl

$ stat -x /usr/local/bin/kubectl
  File: "/usr/local/bin/kubectl"
  Size: 55           FileType: Symbolic Link
  Mode: (0755/lrwxr-xr-x)         Uid: (    0/    root)  Gid: (   80/   admin)
Device: 1,5   Inode: 2013626    Links: 1
Access: Wed Sep  2 19:20:39 2020
Modify: Wed Sep  2 19:20:39 2020
Change: Wed Sep  2 19:20:39 2020

$ ls -l /usr/local/bin/kubectl
lrwxr-xr-x  1 root  admin  55 Sep  2  2020 /usr/local/bin/kubectl -> /Applications/Docker.app/Contents/Resources/bin/kubectl

$ stat -x /Applications/Docker.app/Contents/Resources/bin/kubectl
  File: "/Applications/Docker.app/Contents/Resources/bin/kubectl"
  Size: 50104496     FileType: Regular File
  Mode: (0755/-rwxr-xr-x)         Uid: (  502/michaelmo)  Gid: (   80/   admin)
Device: 1,5   Inode: 17339265    Links: 1
Access: Thu Oct  7 10:12:44 2021
Modify: Wed Dec  9 17:24:19 2020
Change: Fri Dec 11 05:22:00 2020
```

Kubectl is 50 megabytes big, arguably that's quite a bit for this command line program.

---29/07/21 06:08:37----------------------

Visual studio code shortcuts:  https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf

Command shift +     ::: make resolution larger
Command shift -     ::: make resolution smaller

Close outline at the right of the screen (this one is called "minimap")

Command ,           ::: opens the settings page, search for minimap, uncheck 'minimap enabled'



---29/07/21 06:15:02----------------------

IntelliJ goodies on OSX.  https://www.jetbrains.com/help/idea/mastering-keyboard-shortcuts.html 

press two times shift in quick succession, then in the windows press the 'symbols' tab ::: can show the source of any symbol, has a good built-in decompiler!

Command B   ::: go to declaration.

Command L   ::: go to line number

