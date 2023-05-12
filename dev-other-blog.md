" Set text width as 72.

### My blog for stuff that i used to post on twitter

... so no i am putting my observations over here, instead of posting them on social media (kind of)


---12/05/23 18:37:40----------------------

I tried to make a page, where chatgtp and google bard appear side-by-side on the same page, each of them embedded in an iframe tag. (tried to send the same prompt to both of them, in order to display both results side-by-side).

Now google bard doesn't allow that! They are sending the ```Cross-Origin-Resource-Policy``` http header with value ```same-origin``` - therefore it's impossible to embed them in an iframe that comes from a domain other than *.google.com.

The reason is that the javascript on the embedding page can access the DOM of the embedded page (google bard in this case) - and that opens the room for cross-site attacks.

Now this feature probably disables some of the queries on my [duckduckbang!](https://github.com/MoserMichael/duckduckbang) project. Nasty...


---09/05/23 05:10:30----------------------

Is LLM [prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering) is the art of asking a questions to the language model, one that is likely to produce a better result. 
The idea looks similar to  ... [Robopsychology](https://en.wikipedia.org/wiki/Robopsychology) in 'I Robot' by Asimov

We are living in an interesting time...

A different view would be, that it's just a way to optimize the results of a search engine.

---08/05/23 09:02:53----------------------

Just realized: ChatGTP isn't hallucinating, these are Androids who are dreaming of electric sheep!

Now I am re-reading "Do Androids dream of electric sheep" by Philip K Dick, so writing down the memorable phrases/scenes. [more...](androids-electric-sheep.txt)

/actually pasting out memorable phrases is a nice trick - for staying focused on the text, while you have half a hundred tab windows open in the web browser...
The good part is that this method can help with last point in the text (it's like a bookmark) - just search for the last phrase that got copied in the notes/

... And the Androids in the book also do have hallucinations! "Maybe that's a false memory. Don't androids sometimes go around with false memories?"

---08/05/23 05:56:47----------------------

[Stack Overflow is ChatGPT Casualty: Traffic Down 14% in March](https://www.similarweb.com/blog/insights/ai-news/stack-overflow-chatgpt/)

So where the stack overflow posts ... training their own replacement?
But if any harm comes to SO then the quality of the tech answers in ChatGTP will also be affected.

As Berthold Brecht said "So many reports. So many questions."  [Questions of a reading worker](https://www.emag-augsburg.de/2018/02/21/questions-of-a-reading-worker/)

Submitted the link to HN [discussion on HN](https://news.ycombinator.com/item?id=35857536)

---07/05/23 06:17:15----------------------

I have summed up an interesting interview with Erica Franz on Authoritarian regimes [link to my summary](political-stuff.txt) - with specific reference to Putins attempts to resurrect Stalinism.

In Soviet school they used to teach us that Lenin was writing summaries of the stuff that he read [here](https://prorivists.org/how_lenin_worked_with_a_book/) - so they forced us to do likewise... Somehow i have come to think that this is a good practice (of course Lenin's regime was a very nasty one...)


Interesting that Socrates didn't like to write things down ... among other reasons because it 'destroys memory and weakens the mind'.
[see here](https://blogs.ubc.ca/etec540sept13/2013/09/29/socrates-writing-vs-memory/) 

Interesting that Socrates is reported to have told the story two Egyptian deities Theuth and Thamus. These ancient greeks must have travelled a lot: see [here](https://history.howstuffworks.com/history-vs-myth/greek-philosophers-african-tribes1.htm) 

"It's well-documented that classical Greek thinkers traveled to what we now call Egypt to expand their knowledge. When the Greek scholars Thales, Hippocrates, Pythagoras, Socrates, Plato and others traveled to Kemet, they studied at the temple-universities Waset and Ipet Isut"

---04/05/23 06:34:50----------------------

me talking with ChatGTP on classical AI and the attempts to combine classical AI with ML
[link to the talk](talking-with-chatgtp.md)

I have come to think that ChatGTP is very good at this kind of general discussions.

(also I appreciate the lack of hubris on the part of ChatGTP - very unlike all the real workers in the field. ChatGTP is also always there to explain these frequent acronyms and explains what it is referring to - you just have to ask...)

/later discovered that Google Bard is better at it - because it has a later knowledge cutoff date than ChatGTP3.5 ; this means that the data used to train Google Bard is newer and more up to date than that of ChatGTP3.5/



