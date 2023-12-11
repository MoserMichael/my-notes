" Set text width as 72.

### My software developer blog (mostly)

My [linkedin profile](https://www.linkedin.com/in/michael-moser-32211b1/) 

This is a log, here I am listing the gotchas that I stepped upon as a developer.
Maybe someone will find this to be of any use, at least it is useful to me, so as not to step onto the same rake twice; Some of the fun in programming is to have your assumptions invalidated; this is not just a cause for grieve, it is an opportunity to re-examine your assumptions, which is a good thing.

(should have started a log like this ages ago. Writing stuff down helps with clarifying subject matters) 

I also got another blog for [stuff that i used to post on twitter](dev-other-blog.md)

---24/09/23 08:18:53----------------------

I was probably wrong in making up all of this stuff, here on this site, as none of it is of any value. (i was using all these projects as a tool to learn stuff, and to write down my thoughts and reflections along the way)

This was sort of my way of staying afloat in an ever changing landscape of software development, sort of.

It turns out that my efforts have little value, the skill of solving Leetcode questions is much more appreciated (Now for whatever reason the most common verb that combines with leetcode is 'to grind')

I never thought of leetcode to be too relevant to my way of doing things, now that was apparently wrong; 

... Therefore joining the leetcode party and putting up my solutions [here](https://github.com/MoserMichael/my-notes/tree/master/interview-questions) 

After all leetcode stuff has something to do with programming (actually leetcode has more to do with problem solving, whereas programming in my humble understanding is about writing tools for solving problems)

My problem with leetcode:

- You often spend more time at parsing the problem statement than with solving the problem. Well, maybe that's the point of the exercise, who knows...
- I forget the leetcode exercise when it gets 'accepted' (when the code passes all of the tests). Maybe that's because the problems are often contrived, and have little to do with real world problems. (maybe i should take notes)
- One is supposed to give a show while interviewing in the leetcode style, and that doesn't go well with looking for a solution to the problem. 
    - (Maybe the reason is that I am just to slow at solving this kind of problems, at the moment)
    - Maybe the whole point is to go through the problem description and spell out a solution, before starting to code.


So let's just follow the instructions!   

[![The 'Lego Movie' - 'Instructions to fit in, have everybody like you and always be happy'](https://img.youtube.com/vi/5wuAxZqBuFE/0.jpg)](https://www.youtube.com/watch?v=5wuAxZqBuFE)


I am starting with list of problems, here are some problem lists that i found:

- [top-interview-150](https://leetcode.com/studyplan/top-interview-150/) and  [top-interview-75](https://leetcode.com/studyplan/leetcode-75/) These list give a classification of problems, where the classification itself is giving a strong hint as to how to solve the problem. Let's hope it's a good start...
- [top 100 liked questions](https://leetcode.com/problem-list/top-100-liked-questions/)
- [all problems](https://leetcode.com/problemset/all/?page=1)
- [google interview questions](https://leetcode.com/problem-list/top-google-questions/)

<!--
/today i learned that Leetcode exists since 2010, [wiki](https://en.wikipedia.org/wiki/LeetCode) - so much about taking wrong turns... Still I am doing these problems for some time now, and still don't feel that i am getting any faster at solving them, or getting any better at making a show while presenting them. Where it helps: I don't get lost when reading tricky problem statements, so there is some sense in doing all this.../
//-->

6/10/23 - I am past a hundred leetcode problems, (hi, [that's me on leetcode](https://leetcode.com/michaelmo123/) ) 

My observations, so far:

- Now it can still take me hours to solve a problem. 
    - when stuck with a problem: It really helps to stop and then return to the same problem later, with a fresh perspective. (However you can't do that with a job interview...)
- I am over the initial 'leetcode shock'. Some people take Leetcode really hard. However it can also be fun.
- it makes sense to return to a problem, while asking follow up questions (that's what they like to do at job interviews)
    - One follow up question is: how could you make things faster? If a submission isn't along the top submissions in terms of the desired trait, then there usually is much room for improvement. For example: the [n-queen problem](https://leetcode.com/problems/n-queens-ii/) isn't a very hard problem, however they could also ask follow up questions like: can you make it faster?
(I managed to used symmetries along the x-axis for this case, but there are probably more tricks in the book). /Note: performance measurement numbers in leetcode runs are sometimes erratic/
    - Some problems are easier to solve recursively, one follow up question would be: solve the same problem without recursion
- Don't take shortcuts. Example: if a function returns more than two return values, then make an object out of the return value - otherwise it's easy to loose track. (same reason: avoid tuples that are standing in for records, it's easy to loose track)
- I need to get better at coming up with test cases for my solution. Usually I follow the examples given in an exercise, frequently there are cases that are not described in the problem statement.

20/10/23 - Now starting to write leetcod submissions. Here you have to write some explanation of what has been done. Hope that this will improve my presentation skills at those job interviews...

Some gripes: sometimes the difficulty ranking of a leetcode problem doesn't make sense, but i guess there is no use in bothering with this problem; I think part of the problem is the requirement to have a bell-shaped curve for the difficulty levels of questions, so that most of them are ranked as Medium. 
Also some of the problems are only available to payed accounts, which is bad. 

I asked GoogleBard about alternative services, maybe it's time to check them out:


Q: which sites are successfully competing with leetcode?

GoogleBard:

While LeetCode remains the dominant platform for interview preparation for tech roles, several other sites are gaining traction and offering compelling alternatives:

Direct Competitors:

- HackerRank: Offers a similar experience to LeetCode, with a vast library of coding challenges, contests, and interview preparation resources. Its strengths include a strong community, active discussions, and a focus on specific job roles.
- Codility: Geared specifically towards interview preparation, Codility provides personalized learning paths, mock interviews, and feedback from real engineers. It also integrates with various applicant tracking systems, making it popular among recruiting teams.
- Interview Cake: Focuses on high-quality, in-depth coding challenges designed to simulate real-world interview scenarios. It offers detailed solutions and explanations, helping users understand the thought process behind solving problems.
- Pramp: Provides a platform for conducting mock interviews with other users, allowing for real-time feedback and practice in a simulated interview environment.

Emerging Alternatives:

- Codewars: Offers a gamified approach to learning, with challenges presented in the form of "katas" that users can solve and earn points and ranks. This makes learning more engaging and interactive.
- AlgoExpert: Provides structured learning paths for specific coding topics, along with video explanations, quizzes, and practice problems. It's particularly helpful for beginners who need a more guided learning experience.
- NeetCode 150: Offers a curated list of 150 essential coding problems for cracking FAANG interviews. It focuses on high-impact problems with detailed solutions and explanations.
- Grind75: Offers a structured 75-day LeetCode challenge program designed to improve coding skills and prepare for interviews. It provides a daily schedule and community support to keep users motivated.

Other Resources:

- MIT OpenCourseware: Offers free access to video lectures and materials from MIT's computer science courses, providing a solid foundation in programming concepts.
- GeeksForGeeks: Provides a wealth of articles, tutorials, and practice problems on various computer science topics, including algorithms, data structures, and operating systems.

Choosing the Right Platform:

The best platform for you depends on your individual needs and learning style. Consider factors like:

- Your level of experience: If you're a beginner, platforms like AlgoExpert or Pramp might be helpful.
- Your specific goals: If you're aiming for FAANG companies, NeetCode 150 or Grind75 could be good options.
- Your preferred learning style: If you enjoy gamification, Codewars might be a good fit. If you prefer video explanations, Interview Cake or AlgoExpert might be better.
- Cost: LeetCode offers a free tier with limited features, while other platforms require paid subscriptions.

Ultimately, it's recommended to try out different platforms and see which one works best for you. You can also combine several platforms to maximize your learning experience.




---30/07/23 20:23:26----------------------


Sometimes a pod is configured to print its logs with color codes, these are very annoying to look at. So here is how you get rid of them:

This little alias in your .bashrc file can help:


```
alias nocolorfilter="sed -e 's/\x1b\[[0-9;]*m//g'"
```

Here is how I use this alias:


```
kubectl logs pods-with-colors 2>&1 | nocolorfilter | vim -
```

It turns out that you can configure log4j to add color codes to the output, sometimes this feature is being used (would never enable it myself)


<!--
---12/07/23 07:46:26----------------------

I think that 'noodle code' should be the term 'for spaghetti code ++' . Noodle code is the same pastry disguised in object oriented and functional parlance...

On the other hand: projects in object oriented spaghetti code++ tend to be more complex and larger than procedural spaghetti code. You can solve more complex and demanding problems in this way. You tend to end up with something more scalable.

One way to end up with bad code in a script: a simple script is usually being written in bash/shell script. Now at some point things get complicated, and it needs to be re-written (usually into python). This rewrite is often resulting into some code which is not quite 'pythonic'. Here you are - 'gotcha' !!!
I don't have a fix for this kind of situation. Maybe it's a better idea to start to write this kind of scripts in python, to begin with.
//-->

---31/05/23 05:51:00----------------------

Found an area where ChatGTP/Google Bard can be used to great benefit:  I am not an expert in frontend stuff, but now I had to fiddle with CSS style sheets - the LLM knows all the style combinations, and its recommendations worked!

They might have done some specialized training on CSS, I had less success when asking about other domains.

So far this was my only real success, got lots of hallucinations when asking about other areas.
Other people are reporting enormous increases in productivity, however I could not reproduce this kind of success - i observed that it is a non trivial task to distinguish between fact and LLM fiction.

---06/07/23 12:04:39----------------------

Some programming errors creep up again and again. Maybe i will refrain repeating them, by becoming more aware of them - so lets write them down.

--

I thought that the following will run, and return True, if for at least one of the elements the function ```process_elem``` will return True,
Not so fast, ```keep_going or process_elem(elem)``` will only be called the first time, if ```keep_going``` is True then ```process_elem``` will not be called at all! (That's shortcut evaluation, but I keep forgetting about that, although it is pretty elementarry)

```
    keep_going = False

    for elem in elements:
        keep_going = keep_going or process_elem(elem)

    return keep_going    
```
 

- python: if there is a sequence of if statements, where each subsequent clause is ```elif``` - yeah, sometimes i forget about that and write ```if``` instead of ```elif```. Happens again and again - and has to be debugged.

  / same frequent source of errors: switch statements, state machines-transition tables, etc/

- the vanishing log context. One of the main questions in backend-land is: where are the logs?
  Now some systems change the log context over time. For example: jboss and even simple systems like gunicorn are putting their logs in one place during their initialization sequence. However futher down the road they decide otherwise - and put the logs in some other place. 
    
  A sure sign of this happening: you have several instances of the same service, and the logs stop at the same moment. I spent some time wondering if a given component stopped receiving any requests - checked all sort of possibilities. The confusing aspect is that you see *some* log, however that's only part of the picture...   

  My error was that I looked at the command line of the process that was running the whole show. Once upon a time one would specify the configuration in the command line of the main process.
  Now this is a simplified understanding o what is actually happening....

- working with locks: if you have got hold of a lock, then you really have to make sure to release it, now in python you have the ```finally``` clause:

```
    try:
        do something of great importance
    catch ex:
        do the stuff supposed to happen if that something failed
    finally:
        now here is the place to release that log
```

Everything in a language seems to have some purpose. Now not all languages like the idea o exceptions - for example golang doesn't have exceptions. Also a good deal of C++ projects don't use exceptions at all.

--

Edge cases in a flow! Now one approach to check for them is to have exhaustive, 100% coverage unit tests - this forces you to go through all of the edge conditions. I know it's hard, but it is worth it. One situation that calls for 100% test coverage is when state is maintained between calls.

- what is in a log? what should be logged? 
    - don't take anything for granted, you have something to log whenever a logically related series of steps has completed.
    - on some systems you can't view a sequence of logs as such, only thing you can do is to query the system by some keyword. Always be aware the the key info is part of the log entry (be it a sesion-id or whatever key info is identifying the flow in this particular context)\
    - logs are your bread and butter in server land

--

Identical log messages (or near identical log messages) written at two different locations in he code. This leads to confusion on where the log entry comes from...

How to deal with that:   
    - Now look at the log message: are there additional details like the name of the source file that caused the log message? Match the log message again: is it an exact match or a substring match?
    - sometimes you can search all of the codebase (spanning different repositories)

--

Sometimes you need to denormalize a structure in order to get sufficient lookup speed (that's a hard one: it is easy to mess up the structure during insertion)

  How to deal with that one?
    - lots of test
    - lots of logs during insertion (where the complexity is)

--

Need to speed up stuff? First of all measure.
    

- examine alogithms in use 
- examine data structures in use, 
    - examine memory access patterns: (does it have lots of CPU cache misses?)
        - can you cache stuff? What kind of caching is in use?
    - examine allocation patterns (usually people are not very aware of them)
    - memory allocators (more for c/c++)
        - allocation patterns: you need a lot of objects of size x1, x2, x3 
            - do you want to have separate slabs for sizes x1, x2, x3?
- storage hierarchy: Is there some sort of caching for hot vs cold areas?
- communication: too many roundtrips? What kind of latencies are there?
- lock contention (often occurs in conjunction with pooling and threads)
    - do reader/writer locks make sense?
    - do you need more than x conenctions at a time , and the connection pool only provides for x / 2 connections ?
- java: do you have to reboot the service often (takes a lot of time untill java is just-in-time compiled - several thousands of iteratiosn over the same basic code block

--

Conflating OS write to file with OS flush. Writing to a file only updates the WRITE CACHE inside the OS - data is not yet stored to disk !!!


--

Schemaless DB - if you used to do SQL tables, then you might forget that records in a MONGODB collection may have differen structure; hey are strucured when they are written.
Now the code that writes these records may change, and you end up with different versions of documents in the same collection of documents .
(and the code that writes this stuff is a mess, after a few years)

--

(To be continued...)

---23/02/23 10:08:35----------------------

Python catch #425 - if you have a list/map/object and want to display the string representation of each object, use repr. (str and __str__ won't cut it...)

```
class Foo:
    def __init__(self, num, s):
        self.num = num
        self.s = s
    def __str__(self):
        return f"[s: {self.s} num: {self.num}]"


a = [ Foo(1,"one"), Foo(2, "two") ]

# output: show-list-with-str [<__main__.Foo object at 0x10287e208>, <__main__.Foo object at 0x10287e0c8>]
print(f"show-list-with-str {str(a)}")


b = { "1" : Foo(1, 'one'),  "2" : Foo(2, 'two') }

# output: show-map-with-str {'1': <__main__.Foo object at 0x10287e088>, '2': <__main__.Foo object at 0x10287e148>}
print(f"show-map-with-str {str(b)}")


class Bar:
    def __init__(self, num, s):
        self.num = num
        self.s = s
    def __repr__(self):
        return f"[s: {self.s} num: {self.num}]"


a = [ Bar(1,"one"), Bar(2, "two"), Foo(3, "foo") ]

# output: show-list-with-repr-and-one-__str__ [[s: one num: 1], [s: two num: 2], <__main__.Foo object at 0x1028cde88>]
print(f"show-list-with-repr-and-one-__str__ {a}")

b = { "1" : Bar(1, 'one'),  "2" : Bar(2, 'two') }
# output: show-map-with-str {'1': [s: one num: 1], '2': [s: two num: 2]}
print(f"show-map-with-str {str(b)}")


# https://stackoverflow.com/questions/44595218/python-repr-for-all-member-variables
def repr_helper(obj):
    return "{}({!r})".format(type(obj).__name__, obj.__dict__)

class Big:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # if you want to show all members of an object, upon call to repr - something like this
    def __repr__(self):
        return repr_helper(self)

c = Big(a, b)

# big: Big({'a': [[s: one num: 1], [s: two num: 2], <__main__.Foo object at 0x10509c3c8>], 'b': {'1': [s: one num: 1], '2': [s: two num: 2]}})
print(f"big: {c}")

```



---23/02/23 07:08:35----------------------

My new project is a programming language called PYX - the project is [here](https://github.com/MoserMichael/jscriptparse). I guess that's a project that will keep me busy for a while.

One problem is: how do you test a programming language? One approach is bootstrapping: implementing the programming language compiler/runtime on top of a more limited version of the  same programming language. That is a very sound approach for compiled languages - with static typing. However a scripting language/shell like PYX wouldn't quite benefit from this approach.

I am trying to test the PYX programming language by implementing leetcode problems. (never bothered to do leetcode exercise in serious, maybe i will get some sense from this kind of exercise ;-)

I have also started to keep most of my notes on various subjects in the following file now: [here it is](https://github.com/MoserMichael/my-notes/blob/master/learning-all-sorts-of-stuff.txt) . Most of my work involves some sort of navigation through diverse software environments. Now these environments are all different - but they do have similarities. The most important part seems to be: not getting lost.


---22/02/23 17:27:35----------------------

I somehow got over the state of ChatGPT induced shock. Now i have come to think of the following:

- We still have a niche, as Human programmers: ChatGTP is good at leetcode, but there is still a lot of value in things in other areas: you need to understand the subject domain and understand what is being done:
    - you need to be able to communicate with people who are defining the requirements 
    - you also need to be able to understand an existing code base, the archiecture of a product, need to be able to explain why things are done the way they are.
- i guess it will still take some qualitative leaps to solve the remaining issues. Maybe that time will be comparable to the time needed to fix self driving cars - not sure when it all works out.-

However 'the times are they are a-changing', no doubt about that. And you never know what's around the corner...

The most immediate changes will probably happen in the area of search engines - and in how we are searching for information in general. Having a chat with ChatGPT may be more informative then having to go through pages of search results - where the relevance of the search results is subject to the whims of spammers and the whims of the search engine.
(and the quality of the main general search engine is declining steadily)

Somehow i found ChatGTP to be an effective assistan with CSS - it just shines on any quesion on how to move around tags in html (don't need to do that often)

Another interesting tendency is that the big media companies are now pushing paid services in addition to pushing targeted advertising. (see twitter and facebook, who are now charging for account verification or even for two-factor authentication (well some say that's because ad-tech is running into problems - which is due to the economy)

- Interesting if these changes will make it harder for the AI companies to obtain training data for the language models, I wonder if that will have an effect on the quality of language models.
- Now is it possible, that 'advanced search' capabilities like chatting with ChatGPT will be turned into a paid service, or will the ChatBot will add casual references to relevant products into the conversation? I am not sure how banner adds will work, given that all the attention of the user is focused on the conversation with the AI bot. We will have to wait for an answer, apparently... but maybe there is enough money in monetizing API access, who knows.

I am wondering, how this will affect education, in the long run:

- Most kids don't seem to be learning for the sake of acquiring real insight, most of them do it to pass some milestone that they are expected to pass. Now they see this device that would spit out essays in a minute. How will the kids react? Will they now strive for real knowledge and insight, given that this would differentiate between them and the computer? I frankly don't know. To reformulate the question: will this thing result in greater disorientation, or will we find a new sense of purpose?
- Will young kids still go a computer science education, given that it will probably get harder to get an entry level job? I don't know. Will people still try gain an understanding of how technical things work, or will we treat the computer as a black box that is best left untouched?
- What about the value of being an expert? Will it get harder to tell a real expert from a fake one?

We are living in interesting times, let's see how it all plays out.

---18/02/23 19:46:03----------------------

I had a chat with ChatGPT about the book "Future Shock" by Alvin Toffler. Science fiction gone real, wow...

Me: 'please summarize the book "Future shock" by "Alvin Toffler"'

ChatGPT: '"Future Shock" is a book by Alvin Toffler, published in 1970, that explores the social and psychological consequences of rapid technological and cultural change in the 21st century. Toffler argues that society is experiencing "future shock," a psychological state of disorientation and anxiety caused by the rapid pace of change.

Toffler argues that the pace of change is accelerating faster than people can adapt, leading to a range of societal problems. He explores topics such as the impact of technology on work and the economy, the changing nature of family and social relationships, and the rise of a "super-industrial" society in which machines and technology dominate.

Toffler also suggests ways that individuals and society can adapt to these changes, such as by embracing lifelong learning and developing new social and political structures. He argues that individuals must become "futurists," able to anticipate and adapt to the rapid changes that are reshaping the world.

Overall, "Future Shock" provides a thought-provoking analysis of the impact of technology and cultural change on society and suggests strategies for coping with the rapid pace of change.'

Me: 'Is it possible to adapt to all these changes?'

ChatGPT: '"Adapting to all the changes brought about by rapid technological and cultural changes, as discussed in "Future Shock," can be challenging, but it is also possible. One of the main points of the book is that individuals and societies need to become more future-oriented and adaptable to keep up with the pace of change.

Toffler suggests that people can adapt by being open to new ideas, learning new skills, and being flexible in their thinking. He argues that individuals should embrace lifelong learning to keep up with the changes in their field of work, as well as to learn new skills for future job opportunities.

Societies can also adapt by developing new social and political structures that are better suited to the changing world. For example, Toffler discusses the need for a new form of democracy that is more participatory and responsive to the needs of citizens.

Overall, while adapting to rapid technological and cultural change can be challenging, it is possible through individual and societal efforts to embrace change, learn new skills, and develop new structures to keep up with the pace of change."'

Me: 'but will it work out?'

ChatGPT: "It is difficult to predict with certainty whether adaptation to rapid technological and cultural change will work out successfully in the long term. The success of such adaptation depends on a variety of factors, including the speed and scale of the changes, the willingness of individuals and societies to adapt, and the effectiveness of the strategies used to cope with change.'

Me: 'How should democracy be changed?'

ChatGPT: 'In "Future Shock," Alvin Toffler argues that democracy needs to be changed to better suit the needs of a rapidly changing society. He suggests that the traditional form of representative democracy, where citizens elect representatives to make decisions on their behalf, is not well-suited to the complex and rapidly changing issues faced by society.

Toffler proposes the idea of a "participatory democracy" where citizens have a more direct say in decision-making. This could be achieved through various means, such as electronic voting, public meetings and forums, citizen initiatives and referendums, and other forms of direct citizen participation.

Toffler also argues for the decentralization of decision-making power, to ensure that decision-making is closer to the people it affects. This could be achieved by devolving power to local communities and organizations, rather than centralizing power in national governments or large corporations.

Overall, Toffler suggests that democracy needs to be reimagined to be more inclusive, participatory, and responsive to the needs of citizens. By giving people more direct say in decision-making and devolving power to local communities, democracy could better adapt to the rapid changes of a complex and interconnected world.'

Me: 'Who will be on top of all this?'

ChatGPT: 'In the context of rapid technological and cultural change, it is difficult to predict who will be "on top" or the most successful in the long term. As new technologies and cultural shifts emerge, new opportunities for success and influence also arise. However, there are some general trends that can be observed.

Individuals and organizations that are able to adapt quickly to change and embrace new technologies and cultural shifts may be more likely to be successful. Additionally, those who are able to anticipate future trends and plan accordingly may have an advantage over those who are slower to adapt.

In terms of organizations, those that are innovative, flexible, and agile are more likely to succeed in a rapidly changing environment. This includes companies that are willing to invest in new technologies and ideas, as well as those that are able to pivot quickly to respond to changing market conditions.

Ultimately, success in a rapidly changing environment depends on a combination of factors, including adaptability, innovation, and the ability to anticipate and respond to change. The individuals and organizations that are most successful will be those that are able to navigate these factors successfully, regardless of their current position or background.'

Me: 'Are you ok with that?'

ChatGPT: 'As an AI language model, I do not have personal feelings or preferences, so I am neither "ok" nor "not ok" with any particular outcome. My purpose is to provide information and answer questions to the best of my abilities, based on the available data and knowledge. It is up to individuals and societies to determine their own views and opinions on the topics we discuss.'

Me: 'what does it mean to embrace change?'

ChatGPT: 'To embrace change means to accept it, adapt to it, and even welcome it as a positive force for growth and improvement. It means recognizing that change is a natural and inevitable part of life, and being willing to adjust one's thoughts, behaviors, and attitudes to keep up with changing circumstances.

Embracing change involves being open-minded, curious, and willing to learn. It also requires a certain level of flexibility and resilience, as change can sometimes be disruptive and uncomfortable.

Embracing change can be beneficial in many ways. It can help individuals and organizations stay relevant and competitive, avoid stagnation and complacency, and take advantage of new opportunities for growth and improvement. It can also lead to personal and professional development, as individuals are forced to learn new skills and adapt to new situations.

Overall, embracing change is a mindset that involves being willing to take risks, learn from mistakes, and continuously adapt to new circumstances. It can be challenging, but it is also necessary for growth and success in a rapidly changing world.' 

Me: 'what would be the alternative?'

ChatGPT: 'The alternative to embracing change would be resisting or rejecting it. This could involve maintaining the status quo, avoiding new ideas or innovations, and being unwilling to adapt to new circumstances or challenges.

While resistance to change may offer a sense of security and stability in the short term, it can have negative long-term consequences. It can lead to missed opportunities for growth and improvement, and can leave individuals and organizations behind in a rapidly changing world.

Furthermore, resisting change can often result in increased stress and anxiety, as individuals and organizations struggle to maintain outdated practices or systems that are no longer effective or relevant.

Overall, while it can be tempting to resist or reject change, especially when it seems difficult or uncomfortable, the alternative of embracing change and adapting to new circumstances is often the more beneficial and productive approach.'

---15/11/22 14:08:45----------------------

I was wasting a lot of time with building dockerfiles - files for building a docker. Here is a better approach:

- To start a docker with the base image, let's assume that the base image is fedora::latest -  ```DID=$(docker run -d -p 9000:8000 -v $PWD:/mnt/loc --name dcont-dbg fedora:latest /bin/sleep infinity) ```   -  the main process of the docker does not do much,  it just keeps the docker container in a 'running' state. (an alternative would be ```DID=$(docker run -d -p 9000:8000 -v $PWD:/mnt/loc  --name dcont-dbg fedora:latest /bin/sh -c 'while [ true ]; do sleep 100; done') ```
    - ```-o 9000:8000```  external port 9000 will be mapped to port 8000 - that's handy if you need to install and test a server that listens on port 8000 (within the container)
    - ```-v $PWD:/mnt/loc``` the current directory will be seens as /mnt/loc within the container
    - ```--name dcont-dbg``` give the contaienr a name (for the next step)
- check that the container is running.
- attach a shell to the base imager, run the commands required to set up the desired environment, and then take the command history to write the Dockerfile  ```docker exec -ti dcont-dbg /bin/sh``` - you can copy the needed stuff via the mounted directory, and you can check if the installed service works, as the required port is reachable from the host.

That's much better then starting to write the ```Dockerfile``` by means of trial and error!!!
You can try out stuff in the shell, interactively, then look at the command history and that that as the basis for writing the RUN commands in the dockerfile.
Another bonus: the environment keeps running within the docker, you can examine it as a reference point.

BTW, the docker command line seems mysterious in many ways, however the documentation has a number of great guides that explain it! See the [Docker Guides](https://docs.docker.com/get-started/overview/) It's all hidden under: Running your app in production / Configure containers !

---23/08/22 19:45:52----------------------

I got it how to deal with hacker news and twitter - just never log in! Come on - 90% of what you read on both sites is clickbait or just a waste of time.
Also i doubt that people really value a different opinion - they only seek confirmation of their own opinions and biases.
Almost like in the real world ;-)

(Obligatory xkcd link: https://m.xkcd.com/386/ ) 

.. Now i got a problem: where do i get any news from?

(Later update: you can ask google bard - it doesn't have it in its knowledge base, but they run a query on google news, and make a summary of it!)


---21/08/22 10:18:15----------------------

Learning rust. I once had a look at it, some years ago, but i forgot all of it. Also they seem to have changed quite a lot...

Here are my notes.

[notes on learning rust](https://github.com/MoserMichael/my-notes/blob/master/learning-rust.txt)

(thinking of a tinker project, you really need to do something in order to 'get it'. I think rust should be good at parsing/interpreting, as it has a good pattern matching/match facility, sort of like Haskell)

Now the rust compiler needs to work hard, even on the tiny programs that i am writing right now. I wonder how compile times will look like for anything of reasonable complexity...

---18/08/22 09:20:39----------------------

A [monorepo](https://en.wikipedia.org/wiki/Monorepo) is when you have many projects in the same source code repository.

This approach simplifies the handling of dependencies, as almost everything is living under the roof of the same source code repository. However not everything is rosy. It is relatively easy to find the code for the right version of your library dependency - it's right there in the source code repo!

i think that one problem of this approach comes with continuous integration testing - you need to have the unit/integration tests that run with the continuous integration build on the repository, and that can add up as you keep adding projects to the monorepo. Now you need to run all of the tests for every commit, there is no way to determine a minimal subset of the tests, that should be run upon any given change! That can possibly make a very long test cycle.

The alternative would be to have a hierarchy of sub projects, and any change would have to be promoted along this path, until it is accepted into the global project. Frankly that doesn't look like a lot of fun...

I wonder if there is a good solution to this problem, while having it all in the same source repository. I suspect that any bigger project will inevitably run into problems of scale, like the one explained above.

--

"Well, then what can a poor boy do / Except to sing for a rock and roll band?"

In the words of Mick Jagger...


<!---

---30/05/22 05:50:09----------------------

I think that i wrote something quotable [here]( https://news.ycombinator.com/item?id=31552476#31554898 ) on the web revival:

---
the closest thing i found is .. github.

You even have a "definitive list of lists (of lists)" https://github.com/jnv/lists

You can find lots of foo by searching for "list of foo" on github search. https://github.com/search?q=list+of+anything

.. and you can make your own free presence with github pages, just like on geocities! https://docs.github.com/en/pages/quickstart

(now where do you find those 'under construction' giffies? :-)

   /* old things never die, they just get pushed to some free github repo. Maybe there is some git server up there in the sky, that will take care of us when we die :-( (figuratively speaking) */

--->

---21/05/22 03:40:55----------------------

I want to build some python + c based stuff (based on glibc) in a docker:

Python wheels uses the [manylinux](https://github.com/pypa/manylinux) docker image, this was based on CentOS (as of 2022 they depend on CentOS 7 - that one will reach end of life in 2024), but RedHat killed CentOS, and that step makes it hard to trust anything that comes out of RedHat (sorry fedora).

Alpine is a very small linux distribution, people like to build small docker images basted on that distribution.
However there is a catch: it is based on musl standard C library, and some projects have a problem when they are compiled with musl, as this standard library is slightly different from glibc. There is a problem, if the project that you want to build is having an incompatibility with glibc (that happens)

There is a thing called flatpak on alpine, but it doesn't help when you need to compile a project that uses the function missing in musl stdlib (flatpak helps with running executabels)

/and then all this goodness will break after a few months anyway, stuff is so brittle, nowadays/

Interesting fact: maintaining a linux distro is a lot of work, fedora was doing a good job, in general. 
Alpine is ok for most cases, it turns out that alpine is sponsored by Docker...
(turns out they all need a big sponsor, in the end...)

See [here](https://thenewstack.io/alpine-linux-heart-docker/)

"""
When the Docker community was looking for a distro they found that they could make their containers significantly smaller if they used Alpine and that building the Alpine containers takes a fraction of the time compared to other distros.

“This made the Alpine community grow very fast the last 2 years. Even Docker Inc. got the eyes up for Alpine so now Docker sponsors the development of Alpine,”
"""

/with linux you may have more choice, but that also seems to go with more politics... go figure.../

---20/05/22 02:42:38----------------------

Some say that [gerrit](https://www.gerritcodereview.com/) is a better code review tool than what is being offered at github, would have to play around with it...
Here the main focus is on a commit, now what happen if there are multiple commits? Does the thing go down in chaos? Would need to play around with it...

---20/05/22 02:42:37----------------------

Interesting thought: Github/Microsoft is pushing the [copilot](https://copilot.github.com/) product, this one is supposed to tell you how and what to code, however the code review tool on github sucks deeply, and they don't seem to be working on that one. Fixing the code review tool should be a much simpler task, imho...

The deficiencies that I found with the github code review tool:

- The "conversation" screen of a pull request is enormously cluttered, hard to understand what is going on.
- I am working through the list of issues, and marking the checkbox on issues as I go along, in order not to loose track of where I am.
  It turns out that the reviewer is now receiving a notification, when I click on that checkbox! Now he sees the code prior to the changes being committed, which does not create a good impression...
- Issues being collapse for no apparent reason, also not being able to reply in some cases, when the system thinks that the code has changed, or things have moved.
- there should be some protocol that goes like this
    - the submitter marks an issue as done
    - the reviewer approves of the change
    - the issue should then be moved to some other screen, so as not to clutter the "conversation" screen. (You could do that by the editor deleting the review comment, but they don't do that, as it gives the appearance of no work being done).

I wonder if someone has made an alternative UI for code reviews, one that would be better suited for the task...

---19/05/22 09:18:58----------------------

see my notes on studying code review processes [link](https://github.com/MoserMichael/my-notes/blob/master/code-review-survival.txt)

a funny picture on the subject:

![code review](media/code-review.jpg)


---08/05/22 21:57:10----------------------

Another bash trick: 

```
err_report() {
    set +x
    echo "Error on: ${BASH_SOURCE}:$1 : "$(sed $1'q;d' ${BASH_SOURCE})
    exit 1
}
trap 'err_report $LINENO' ERR
```

That's slightly better than ```set -e``` - if a command fails, it also shows the  ```file:line: line-in-script``` that failed

Also: instead of ```set -x``` in a top level script, do the following:

```
      export PS4='+(${BASH_SOURCE}:${LINENO}) '
      export TRACE=1
      set -x
```
That will show the file:line) before each executed line.

Now the trace environment variable can be propagated to dockers with (note that PS4 is not empty, even if not in use! That's why we have TRACE)

```
docker build --build-arg TRACE="$TRACE" ....
docker run -e TRACE="$TRACE" ... ```
```

(don't ask me, why docker build and docker run have different options for passing on environment variables)

Now the child script can also set it's tracint, conditioned on the presence of the TRACE env variable that was passed from the top level

```
if [[ ! -z $TRACE ]]; then
    export PS4='+(${BASH_SOURCE}:${LINENO}) ' 
    export TRACE=1
    set -x
fi
```

---30/04/22 11:43:11----------------------

I got a new M1 mac at work, suddenly it turns out, that running a docker is turning into rocket science.
The aim is to run a basic alpine docker image, with the home directory mounted into the file system of the docker image:

The --platform linux/amd64 option tells docker to run the docker image in an x86_64 emulator. So that's more of a VM than a lightweight container...

(Interesting side note: you can run a x86 executable on a M1 mac, that's because the OSX operating system has the [Rosetta](https://en.wikipedia.org/wiki/Rosetta_(software)) component that translates the instructions of an X86 executable into M1 instructions. The docker thing would have to do a corresponding emulation/translation, whatever you call it)

```

# on the host
> uname -m
arm64

> docker run --rm --platform linux/amd64 -it --entrypoint /bin/sh -v $HOME:/var/home alpine:3.12

/ # uname -m
x86_64
```

Luckily you can inspect the architecture of an image

```
> docker image inspect alpine:3.12 | grep Architecture
"Architecture": "amd64",
```

However it is possible to run a native docker image on this M1 mac.

```
> docker run --rm  -it --entrypoint /bin/sh -v $HOME:/var/home arm64v8/alpine

/ # uname -m
> 
```

You can also get the architecture with jq (hope the json format doesn't change...) For met its:

```
> docker image inspect arm64v8/alpine:3.12 | jq -r 'first | .Architecture'
arm64

> docker image inspect arm64v8/alpine:3.12 | jq -r 'first | .Os'
linux

```

And it's possible to be more specific about the version tag of the image

```
docker run --rm  -it --entrypoint /bin/sh -v $HOME:/var/home arm64v8/alpine:3.12
```

Again, you can inspect the architecture of an image:

```
> docker image inspect arm64v8/alpine:3.12 | grep Architecture
        "Architecture": "arm64",
```


Now of course you will get some script here, that tries to make life easier by abstracting all this madness (but that script has probably a dozen or so bugs)

Here is the link to the script [runimagelocal](https://github.com/MoserMichael/myenv/blob/master/scripts/runimagelocal)

Here is the help text

```
Usage: /Users/michaelmoser/bin/runimagelocal -i <image name>  [ -s <shell> ] [ -m <mount_dir>]

Runs a container interactively with the docker image, by default using the shell /bin/sh.
Can override the shell with the -s option)

The HOME directory is mounted to /var/home in the container (can override with -m option)
```

If no image is given then a default native linux image is run in a container, where the home directory is mounted into the container.
Otherwise all the details mentioned earlier are performed:
- the architecture of the image is determined
- if it isn't a native image, then the --platform option is set.

Some say that adding another script like this one is just about adding another detail that needs to be remembered, however for me its a way to figure things out. Also it saves some time, I really think that!

---28/03/22 09:29:31----------------------

Remembering the details of golang, i wasn't exposed to this language for quite some time now...
[here](https://github.com/MoserMichael/rzgrep) is my exercise on the subject.

- It's the same syntax for accessing a struct field via and via a struct instance and via a reference to a struct. That's very confusing for someone who is coming from the land of C (or from the land of Java, where everything is a reference) However some entitites are treated more equal than others, in other contexts: if you pass a map or a sequence as a function argument, then these are always passed by reference! They did that, because the authors of the language realized, that nobody is getting the difference.... [link](https://stackoverflow.com/questions/40680981/are-maps-passed-by-value-or-by-reference-in-go) Yes, and vectors are also passed by reference, but structs are passed by value!  Now if you have an collection (map or sequence) that contains a different collection as value, then accessing the outer collection will return ... a reference to the inner value. However a loopkup in an array/map of structs will make a copy of the contained struct instance. This is my example that shows you the all of the gory details [here you go](checkit.go) (I think that the 'tour of go' doesn't tell you this...)

- an interface can be either implemented over a structure type [see iface.go](iface.go) or on a reference to a structure [see iface2.go](iface2.go)
    - implementing on a struct type is more flexible: both the reference and the instance type support a given interface!!!
    - a function parameter that is of an interface type is two pointers large one of them refers to some internal type information, the other one referes to the data!
      Read all about it [here](https://www.tapirgames.com/blog/golang-interface-implementation) (a bit confusing, if you ask me)

- And if you pass a string array member to another structure, then it is also passed by value! (sometimes we do it like this and sometimes we do it like that...)

```
package main

import "fmt"

type strA struct {
	names []string
}

type strB struct {
	names []string
}

func main() {
	a := &strA{}
	b := &strB{names: a.names}

	a.names = append(a.names, "kuku")

	fmt.Printf("a.names: %s\n", a.names)
	fmt.Printf("b.names: %s\n", b.names)
}
```

Gives you 

```
go run copy-array-struct.go
a.names: [kuku]
b.names: []
```

- actually i installed go on a new computer, it's version 1.18, therefore I can play with the new go generic feature. My result is [here](https://github.com/MoserMichael/rzgrep/blob/master/src/cbuf/cbuf.go) - actually golang feels much better with generics...  (intro [here](https://go.dev/doc/tutorial/generics) That was a bit sparse, there is also [this source](https://go.googlesource.com/proposal/+/refs/heads/master/design/43651-type-parameters.md#generic-types)   

- append on arrays: works on nil slice as first argument slice; there is no point in defining an empty slice for the sake of appending something to it. Creating an empty slice still requires an allocation (the nil value doesn't)

- concat strings (like java StringBuffer) - you don't need to allocate an object
```
// It's ready to use from the get-go.
// You don't need to initialize it.
var sb strings.Builder

for i := 0; i < 1000; i++ {
    sb.WriteString("a")
}
fmt.Println(sb.String())
```

- defer inside a for loop isn't a good idea: defer calls "inside the loop don’t get executed until the func ends — not when each step of for loop ends. All calls here will eat up the func’s stack and may cause unforeseen problems." The goland ide warns of this...

- never use println, it just happens to be there, in order to have a print thing without dependencies... use fmt.Printf instead

- the second statement re-assigns the variable err, despite the := sign.

```
        f, err := os.Open(name)
        d, err := f.Stat()
```

- the bad and ugly part: the golang build system (everything is fine, if you got just one file in the main package with a main function) magic environment variables:
    
    - GOROOT - where is go installed? (need to set that, if you play around with multiple go versions)
    - GO111MODULE - that's where the shitshow starts, they kept changing the behavior of this env var  !!! 
    - GOPATH  the directory that is the root of $GOPATH/src 
        - all project packages get they directories under src
        - the main package is put under cmd/some_dir/main_file.go, and the compiler is invoked as follows:  
          ```GOPATH=$(PWD) GO111MODULE=off go build -o rzgrep cmd/rzgrep/main.go```

- what symbols are exported from a package?

     "In Go, a name is exported (from a package) if it begins with a capital letter. For example, Pizza is an exported name, as is Pi, which is exported from the math package. ", that's why they like mixed case names, actually...
        - why? the designers of go didn't like to add special keywords like 'private' 'public', so they choose to do visibility as a convention.
          not nice to the poor programmer, who has to remember yet another incantation...

- I finally got the purpose of golang embedding.

Here the type Parent is a member of struct Child, that means that all the members of struct Parent are added into the struct Child.

```
type Parent struct{
    value int64
}

func (i *Parent) Value() int64{
    return i.value
}

type Child struct{
    Parent
    multiplier int64
}

func (i Child) Value() int64{
    return i.value * i.multiplier
}
```

[Here](http://www.hydrogen18.com/blog/golang-embedding.html) Now that makes sense: structure embedding is supposed to look like inheritance (you can access all fields of the embedded structure), but without the is-a relationship that you get with inheritance. (i think that structure embedding is an evil invention, i think this solution is worse than the 'diamond inheritance' problem...)

And you can embed pointers!

```
type Bitmap struct{
    data [4][4]bool
}

type Renderer struct{
    *Bitmap //Embed by pointer
    on uint8
    off uint8
}

func (r *Renderer)render() {
    for i := range(r.data){
        for j := range(r.data[i]){
            if r.data[i][j] {
                fmt.Printf("%c",r.on)
            } else {
                fmt.Printf("%c",r.off)
            }
        }
        fmt.Printf("\n")
    }
}

```

And embedding an interface is supposed to chain the instance with another instance of that interface...

```
type echoer struct{
    io.Reader //Embed an interface
}

func (e * echoer) Read(p []byte) (int, error) {
    // call another Reader instance... But why Reader.Read? Why do you need to access the type now?
    amount, err := e.Reader.Read(p)
    if err == nil {
        fmt.Printf("Overridden read %d bytes:%s\n",amount,p[:amount])
    }
    return amount,err
}
```

"The first advantage to this is that you can rely on functions that use the NewX idiom returning a struct by-pointer to do initialization. The second advantage is that you can embed all the functionality of a type without needing to know when it is instantiated." says the link...

I think that very often this "syntactic sugar" business is about building a following for your language ... at the expense of aggravating the actual user of the language..


---20/03/22 00:06:13----------------------

Today i learned about java: (i tend to learn new language features, when being exposed to some new code base, never bothered to keep up with all the changes of the java language...)


https://stackoverflow.com/questions/37583464/what-is-round-brackets-parentheses-in-try-catch-in-java
https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html

The python with statement has an equivalent in java, see the try with parenthesis syntax; the BufferedReadable must support the AutoClosable or Closable interface (must have a close method)

```
try (BufferedReader br =
               new BufferedReader(new FileReader(path))) {
    return br.readLine();
}
```

I see that often, that some language feature is inspiring/appearing in multiple programming languages... (interesting if there is a term for that)

A java lambda with empty parameters () can be used as a Runnable instance; strange but true...
https://stackoverflow.com/questions/25192108/what-is-the-breakdown-for-javas-lambda-syntax
For example it can be submitted to a thread pool....



---23/01/22 03:13:03----------------------

Today I was told a very nice joke, on my front-page [here](https://raw.githubusercontent.com/MoserMichael/MoserMichael/f409499bace8fedb1d7eb722ca1d7f0c3c3b5fa9/README.md)

<pre>
 ________________________________________
/ Q: How many Harvard MBA's does it take \
| to screw in a light bulb? A: Just one. |
| He grasps it firmly and the universe   |
\ revolves around him.                   /
 ----------------------------------------
        \   ^__^
         \  (..)\_______
            (__)\       )\/\
             -- ||----w |
                ||     ||
nltk score: -10 '(from -100..100) state: 'neutral' eye: .. tongue: --
</pre>

The script that updates the front-page is running [this little project](https://github.com/MoserMichael/opinionated-fortune-cow); the text is taken from the [fortune](https://en.wikipedia.org/wiki/Fortune_%28Unix%29) program, and piped into [cowsay](https://en.wikipedia.org/wiki/Cowsay), to display a nice ascii-art cow. Now I am also running it through [nltk](https://www.nltk.org/) based sentiment analysis, a good score makes the cow smile, a bad one makes her frown. However in this instance the system failed to appreciate the subtle humor of the joke, that's the kind of robots we have right now.

Now we do have smarter robots, Both [IBM Watson](https://en.wikipedia.org/wiki/Watson_(computer)) and [Google search](https://en.wikipedia.org/wiki/Google_Search) are example of systems that take a more layered approach, these systems are dissecting a complex problem into many tiny aspects, and they manage to integrate these tiny aspects into a coherent picture. However it takes a lot o people and enormous amounts of resources to do the trick. The next logical step would be to simplify the construction of such systems, but that is clearly beyond the scale of this little blog (it also seems to be beyond the scale of any company, taken in isolation)

The micro service architecture can be understood as an attempt to standardize the process of dissecting a big problems into relatively simple component parts. The real objective of the micro service architecture is to have a system that is vertically scalable, so as to make the system capable of servicing a very large workload. Maybe a similar approach is required in order to simplify and standardize the layers of data processing and knowledge processing pipelines. That would probably be a process that would require a sustained effort over many years, and it would most likely require many attempts and failures in order to find something workable.

In a sense I am also grasping that light bulb, here in this blog entry, and waiting for the universe to revolve around it ;-)

---

I found some resources, to get some hint of what I am talking about: [awesome datascience](https://github.com/academic/awesome-datascience) and [datascience for beginners](https://github.com/amrrs/For-Data-Science-Beginners), it seems that searching for 'awesome anything' on github will give you a great intro to any topic...

---11/12/21 13:01:21----------------------

I am a long time reader of [hacker news](https://news.ycombinator.com/news), It's an incredible source of information, but it too has its editorial biases. For example this [hightly interesting discussion](https://news.ycombinator.com/item?id=29505524) appeared on the front page the other day, but then suddenly disappeared from the front page again, and also from any other page that appeared in the vicinity of the front page on that day. I am not quite sure, as to why that happened.

Anyway, it's probably time to diversify my information diet, and the source is right here! When logged into github, the main page is showing all the repositories, that were recently starred by any github user, who got a star from me. That is an excellent source on what is happening here! And so it goes, that I am starring everyone, who was so kind to put a star on any of my projects, partially out of curiosity, and a desire to learn new stuff.

You might also want to look at one the scripts that I wrote recently, [Here](https://github.com/MoserMichael/MoserMichael), this [script](https://github.com/MoserMichael/MoserMichael/blob/master/build-local.sh), is a building a README.md file, that is appearing on my github profile, by virtue of naming the repository after my github user. All this is run as a [github action](https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions) - as a continuous integration process, hosted by our (hopefully) benevolent hosts here. (More details in the [about page](https://github.com/MoserMichael/MoserMichael/blob/master/ABOUT.md))

One of the generated reports is a [report of every repository that got a star from me](https://github.com/MoserMichael/MoserMichael/blob/master/USER_STARRED.md). 

Thank you all for keeping me up to date, on what is going on!

Clicking on the image will open a youtube video with the song 'Thank you all' by the 'Free Design'

[!['Thank you all' by the 'Free Design'](https://img.youtube.com/vi/vvLO1i0mTIo/0.jpg)](https://www.youtube.com/watch?v=vvLO1i0mTIo)

"Think and dream and share your mental wealth/The world is out to get us, but it can't/Because we're friends!"

---

Update: now my python [tracer and bytecode course](https://github.com/MoserMichael/pyasmtool) got some enormous visibility, after having been on the front page of hacker news! [here](https://news.ycombinator.com/item?id=29959262). Thanks a lot! Not it is impossible to follow everyone manually, so i [fixed this script](https://github.com/MoserMichael/githubapitools/blob/master/starcounter.py) and added the -f option to do that automatically. Sometimes i get so many followers, so that the script fails at one pass, as it exceeds a github api throttle on the number of rest api calls, but that's a good problem, in my book ;-)

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


---

another one: if you need the gnu grep then you can get it with ```brew install grep```, but you can only use it as ```ggrep```, ```gegrep``` and ```gfgrep``` ...

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

