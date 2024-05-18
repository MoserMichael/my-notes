

-----

Javascript - iterating over map entries (node session)

    > a={a:1,b:2,c:3}
    { a: 1, b: 2, c: 3 }
    > Object.entries(a).map(([k,v],i) => { console.log("k: " + k + " v: " +v + " i :" +i); return k } )
    k: a v: 1 i :0
    k: b v: 2 i :1
    k: c v: 3 i :2
    [ 'a', 'b', 'c' ]

Javascript generators/iterators - they are needed to provide values for a 'for' loop.

Here is how you do an iterable object (that's an object that has special function to return an iterator, so that it can be used in a for loop)

    class Foo {
         constructor() {
             this.data = [1,2,3];
         }
    }

    //
    // class Foo is 'iterable' if it has a member named Symbol.iterator - that returns an iterator object.
    //
    // need to add the function named as special symbol: Symbol.iterator to protoype
    // can't just define a member function with that name ???!
    // now a new Foo object will bet 'iterable' as it has an iterator.
    //
    Foo.prototype[Symbol.iterator] = function() {
         let pos = 0;
         let data = this.data;

         // iterator is an object with the next function, that returns an object upon each call
         // returned object/dict has done: - are we done iterating? and value: - value to return to for loop
         return {
             next: function() {
                     return {
                         done: !(pos in data), // are we done with the iteration?
                         value: data[pos++]    // value returned by iterator
                     }
             }
         }
     }


    f = new Foo();
    for(let c of f) {
        console.log(c);
    }

Here is how you do a generator

    function *range(from,to,step) {
        let val = from;
        while(val < to) {
            yield val;
            val += step;
        }
    }

    for(let i of range(1,10,2)) {
        console.log(i);
    }

Calling generators directly

    > a=range(1,3,1)
    Object [Generator] {}
    > a.next()
    { value: 1, done: false }
    > a.next()
    { value: 2, done: false }
    > a.next()
    { value: undefined, done: true }
    > a.next()
    { value: undefined, done: true }


Generators can call other generators - but they have to do the call via yield* 

    function *blabla() {
        return 3;
    }

    function* func1() {
      yield 42;
    }

    function regFunc() {
        return 43;
    }

    function* func2() {

        // can call regular function from generator - works as expected
        let bl = regFunc();
        console.log(bl);

        // calling a generator function returns a generator object
        let er = blabla();
        console.log("blabla returns: " + er);

        // this way it returns 3
        er = yield *blabla();
        console.log("blabla returns: " + er);

        yield* func1();
        yield* func1();
        yield* func1();
    }

    for(a of func2()) {
        console.log(a);
    }


It turns out that python has a similar thing to delegate form one generator to the other. Welcome to 'yield from' - beginning with python 3.8

    def my_range(f,t,st):
        while f < t:
            yield f
            f += st

    # yield from - to delegate to another generator !!! (from python 3.8)
    def range_three(f,t):
        yield from my_range(f,t,3)

    for n in my_range(1,10,1):
        print(n)

    print("generator calling generator")

    for n in range_three(1,10):
        print(n)


===

    javascript express for http server:

        const express = require("express"),
              app = express()

        app.get("/", (req, res) => {
            res.send("Hello, TREND OCEANS!")
            console.log("finished handling request");
        })

        console.log("before listen");
        app.listen(3000, console.log(`Server started on port 3000`))
        console.log("after listen");

    output:

        node t1.js
        before listen
        Server started on port 3000
        after listen
        finished handling request

=== 

    javascript sleep:

        function onTm() {
            console.log("onTm");
        }

        console.log("before sleep");
        setTimeout(onTm,1000);
        console.log("after sleep");

    output:
        node t.js
        before sleep
        after sleep
        onTm

====
http in node:
    node has in-built http module
        

    express - server
        http://expressjs.com/en/5x/api.html


====

NodeJS - event loop

    https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/

    Phases of the event loop
        - timers: (timers are best effort - not exactly scheduled)
 
----

Binary data in nodejs
(The javascript standard later added it's own stuff:  ArrayBuffer, Uint8array, Float64array etc.. but they don't use that in node)

> let b= new Buffer.alloc(10); // allocates zero allocated buffer
undefined

> typeof(a)
'object'
> a.constructor.name
'Buffer'

> b
<Buffer 00 00 00 00 00 00 00 00 00 00>

> b[2]
0

> b[2]=1
1

> b[2]
1

> b
<Buffer 00 00 01 00 00 00 00 00 00 00>

    
> b.length
10
-----

npm - creating package

    - search if package exists in: https://www.npmjs.com/search?q=prs
    - npm init new-package-name  # makes a default package.json ( package.json reference: https://docs.npmjs.com/cli/v9/configuring-npm/package-json )

    - npm adduser  # use this to log into your npm account. before publishing: need to be logged into your account. 

    - set NPM_TOKEN environment variable to an npm account API token with publish privs.

    - npm publish --access public # from directory that has package.json - and all of the files mentioned in package.json !!!

    - each publish needs to increment the package version number (in package.json)

Show root folder where globally installed npm modules are:

    npm root -g 

install YAML package into the global dir
    npm i yaml -g

    To use globally installed package:

    To use locally installed package:
        need to set environment variable: 
        export NODE_PATH=$(npm root -g)

install YAML locally
    npm i yaml

    module is installed to $PWD/node_modules
    
    To use locally installed package:
        need to set environment variable: 
        export NODE_PATH=$PWD

If you are part of an installed package, then you don't need to do this!!! (can include anything in the current scope)


List all globally installed packages

    npm list -g 


