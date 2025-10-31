---
episode_description: Michael Novati got promoted to Senior Staff (IC7) Eng at Facebook by the age of 27. He joined before the company IPO'd so he had a bunch of interesting pre-IPO stories. 

topics: 
topics: [Growth to Senior Staff (IC7) by 27, Being the #1 code committer at Meta, Volunteering to resign if his code broke prod, Stories of working with Zuck pre-IPO, What was common among IC7+ engineers, How LLMs will affect the code machine archetype]
---

# Meta Senior Staff Eng (IC7) On Zuck Stories, Rapid Career Growth, Code Machine Archetype

Transcript
00:46 – Joining Facebook
Ryan 00:00:46:

Let's get into the interview. I think before we go into common topics of how you got promoted to IC7 or staff or how you write so much code. I wanted to go into just you joining Meta. What was the story behind you joining and why did you pick Meta of all companies when it was small at the time?

Michael 00:01:04:

I started as an intern in May, 2009, and I was in between undergrad and grad school, which is not the most common internship to have.

I was gonna do my PhD at University of Washington in HCI and I was signed up, ready to go, had my housing and everything. I even had a research assistantship lined up already. I really wanted to work, get some more work experience at a top company that was doing really interesting product work.

So I was really only looking at Facebook and Google at the time. I had no problem getting interviews there, which I don't know, nowadays it seems a lot harder to even get those interviews, but it wasn't that hard to get interviews. I think I just applied online for both. And Meta was just, or Facebook at the time, it was really the perfect team fit, which is also not that common with internships where you actually, I happened to have randomly interviewed with an engineer who was working on internal collaboration tools, which was Meta's diff review tools and task tools and discussion tools.

And I happened to interview with this person and that's exactly what I wanted to work on. I really wanted to work on the social network for work and in making people more productive and that side of things. So I was just almost a perfect fit. I did well on the LeetCode questions and then joined his team as, and he was my manager and it started from there.

So it was really just the stars aligning.

Ryan 00:02:31:

How big was the company at the time in terms of engineers?

Michael 00:02:35:

Yeah, it was about 220-ish. It's a bit, there's some debate because at the time production engineers, I don't think were classified as software engineers. So the math may vary a bit, but it was about 200 or so.

Ryan 00:02:49:

And so, I listened, I did some research and I saw that you felt you were one of the most into Meta's culture engineers. What drew you so much to Meta's culture? What were your favorite parts?

Michael 00:03:01:

Yeah, it's really interesting. It was both technical and also the social vibe. So when I showed up on day one, I opened up my dev environment following the instructions, and it was literally running, not the most complicated stack, but it was even simpler.

At the time I was running Apache locally and PHP and my dev server, and it was just hitting a database, MySQL database, just like I would in a side project, except it was a much larger SQL database. And I have a federated one, but it just felt like a really good fit. I just sat down and just felt I was at home, kind of vibe.

And from that point forward, technically, I just felt really in tune with how they were building stuff. And then socially, I mean, honestly Facebook was really cool at the time. It's changed over the years. It's had its ups and downs. Even while I was there, I saw the peaks and troughs, but it was just really cool.

And it was a cool product that everyone knew about and was talking about and curious about. I could get lots of feedback from people about what they liked and didn't like, and it was motivating to work on stuff that people cared about. And I just really wanted to make a good product for all these people who cared.

So both those things, I think.

(10:26) Facebook IPO experience
Ryan 00:04:22:

When I joined Facebook and a lot of my peers also joined as well, PHP was something, I don't want to say it scared us. It definitely was something that we were not attracted to. We thought, oh, we had worked with it a little bit here and there in college. It was something that was pretty unattractive.

Did you feel similarly when you joined Meta?

Michael 00:04:43:

So now Meta uses primarily Hack, which is the derivative of PHP. That's kind of, I don't know if the language is officially forked or, I don't know. You can probably comment on that, but it went through multiple stages though to get to Hack. And the first step was just having a compiler for PHP that turned it into more performant code.

And those efforts were ongoing at the time. There was discussion of should the company rewrite the entire code base in Java or Python or all these things? And they ended up just optimizing the language and starting to customize it to address some of the deficiencies.

I think having loose typing was one of the first things, or an early thing that was added. So they kind of, I feel PHP off the shelf definitely had the stigma at the time, but I felt Facebook's approach was we're gonna make this better than any other language could be because it's gonna be customized at a language level for how the company uses it.

So it's easier to use as an engineer, more performant and has all those traits. So both sides of that. So yes and no is the answer.

Ryan 00:05:52:

Yeah. Yeah. No, definitely. I think PHP gets more of a negative rap than it actually deserves. And Hack is a much better experience, not, it's not comparable to PHP, so that makes sense.

On the culture, one of the early things that I really liked about Facebook was their move fast and break things culture. I just thought it was such a cool framing of something that mattered a lot to people. Since then, that culture has changed. What are your thoughts on that?

Michael 00:06:22:

I was definitely the move fast and break things person at the time.

I still like the kind of move fast and break things framing. Personally I think that the removing the break things part, it felt it was maybe a little bit more the perception on the outside. Part of it was with Facebook communicating to the public that they didn't want to communicate that people are recklessly breaking everything.

But the spirit of it wasn't, it wasn't about breaking, it wasn't you're going around breaking glass all over the place and stepping on and cutting your feet. It wasn't that environment. The idea of breaking things was breaking norms. More recently when you hear people talking about first principles thinking and not following trends for the sake of following them, move fast and break things was about trying to break established norms and thinking about things a different way and trying things from scratch.

And it was really, I think more in the spirit of first principles thinking than just causing havoc. So I still think that that's a good, good motto if they had it today. But at the same time, when a company's larger, more mature, stability, even the smallest bug has millions of dollars, tens of millions of dollars of impact sometimes, and stability can have a real impact. So financial impact. So I think it's also, I can see that motivation for including it too.

Ryan 00:07:50:

And your, throughout your tenure, I mean you started when it was so small at 200 engineers, did you feel the culture changing? I think you were there earlier than I was. So I'm curious, how did that evolve over time?

Michael 00:08:01:

So when I joined, and this was, going back to kind of maybe what was appealing about Facebook at the time, the culture is very engineer driven at the time. It still has that today to some extent. And it's a great place for engineers to work and one of the top competitive places. But it was to the extreme where engineers were very empowered to make decisions. Designers and product managers had to kind of win over the engineers and get their buy-in to build something because if the engineer wouldn't build it, it wouldn't get built. So there were a lot of engineers empowered to push back and negotiate with designers and engineers and I mean, these are still things that happen today, but it was just another level.

The internal, a lot of the, almost all the internal tools at the time were written from scratch internally, and employees used them. So that actually gave, it really set a tone that this is a company that is. That is engineering first. It builds the things it needs. It cares a lot about what it's building and what it's using.

And that part of the culture I loved. I mean, the IPO in 2012 was a turning point where the stock crashed after the, not crashed completely, but it tanked after the IPO, because people were wondering how is Facebook gonna make any money? And it's yeah, that's a good question. You know, I started in 2009 and for three years we didn't really talk that much about how we're gonna make money.

And you know, it's to have a, to have a business that can make money, to hire more engineers, to build really cool stuff that hopefully has a positive impact to, you have to, in at least capitalist society, you have to make money to keep that going and keep growing it. So I kind of had a more mature view as we grew and understood how to optimize ads. Changes that focused on saving money or making more efficient infrastructure became more important. And there were different competing factors. I would say early on, engineers would have more head-to-head discussions about how to build stuff somewhat independently of management.

And towards the end you would have more VPs of two different teams negotiating stuff and then it percolating down. So that's just an example of engineering empowerment, too.

Ryan 00:10:25:

I see. What was it like when Meta IPOed? What was the feeling among the team? Was it ecstatic or people were scared? Because of the drop in the stock price.

Michael 00:10:35:

People definitely weren't scared. I would say that it was a celebratory moment. It started off not being one of those things. I feel Mark Zuckerberg was really good early on about keeping things grounded and humble and not getting caught up in headlines and the press and perception on the outside.

It was just very much you know, IPOing is a very rational thing to do to raise funding for the company, and that's what an IPO is. It's not a party or anything even. And, it was very rational. At the same time though, it is kind of an event that can pull employees together. So the actual IPO, they got the Nasdaq to, there's some button that the bell opens the stock exchange or whatever.

I don't know. They got them to bring the button to Facebook campus and set up a stage and someone rang the bell or posted, pushed the button or whatever. And I can't, there was some talk about how they actually hooked that up through some special networking system so that it actually was the button. There's way more to that story that you should dig into, ask internally about that.

There's probably something about it, but Yeah. But it was really cool. Mark Zuckerberg's parents were standing right beside me in the crowd and I even told Mark about this story because they just happened to be beside me and, and it was the kind of tear in their eyes.

It's a big moment. And you see kind of that per, so you see kind of all your friends growing up and doing something. And I thought that part was very impactful on my life, but it wasn't yeah, I mean financially all of the stock vested six months after the IPO, so none of the employees actually had any money or anything at the time.

They were all the same. Same as they were before the IPO day, but.

Ryan 00:12:22:

Right. When it vested, was that after it had tanked a bunch?

Michael 00:12:27:

Yeah, it was actually, it had tanked down to, I remember this day because me and a bunch of us, it was 20 of us. We went to go see a movie. Okay. We were in the movie theater and everyone's sitting there and then the stock hit their accounts.

So all the phones went off and your vested stock has been deposited. Yeah. And it was kind of, I remember that moment. But the IPO didn't really change people's behavior short term. I think much longer term, financially people could afford houses and have kids, having kids in the Bay Area is super expensive.

So having kids, is it even a thing that you, a decision you might make after having some more savings? So there was some impact there longer term, but short term it didn't really impact people.

Ryan 00:13:12:

Did you hold because you say, oh this is, this is gonna go off and you know, we've got this! Or were you the type that's ‘diversify, put it in index funds’ type, as soon as you get vestings?

Michael 00:13:25:

I held all my IPO stock and I still have all of it. But the,

Ryan 00:13:30:

Oh my god, you really believed.

Michael 00:13:32:

But I sold on vest after, at some point in time, I don't remember when, but at some point in time I sold on vest to diversify. It was very fortunate for the younger people who came out of school and didn't have a lot of financial literacy to have the old guard, so to speak.

Who came, who went through Google IPO and Yahoo IPO and there were classes and stuff on how to manage. Had nothing to do with the IPO per se, just how to manage finances and how to deal with stock, stock-based competition. I grew up in Canada.

Stock-based compensation was, I had no idea what that was. I didn't, I mean, I can read the paperwork, I can do the math, but I didn't really deeply understand it, and it was not my day job. And I, so having these, these lessons and stuff was, was infinitely helpful in understanding how to manage and how to think about the risk and, and these different things.

I don't know if they still have those classes today, but they were very useful.

Ryan 00:14:32:

I mean, Meta stock went down to 90 or something, a year or two ago. Are you sweating at that point or you don't, it's just kind of out of sight, out of mind.

Michael 00:14:41:

I mean, I have diversified enough now that it's not my retirement collapsed type thing. It wasn't that, but it was definitely sweating a bit. These numbers are low. I'm yeah,

Ryan 00:14:55:

Yeah, yeah. I mean, because 90, I mean, when I started in 2018, it was 180 or something. 150, I forgot exactly. So it went to half of that two years ago. It's kind of crazy.

Michael 00:15:08:

I do know people that started during that time though, who in three years, almost 6x their stock.

I mean at Formation, where I am, what I'm doing now and we're helping people prepare for interviews, understand offers. It's definitely one of the, one of the pieces of advice I give from just seeing these fluctuations over the years when people are comparing offers and they're trying to compare them in today's dollars head to head, and they're sweating over single digit percentage differences.

It's a lot of money. Engineers get paid a lot of money. They're, it's, it's reasonable to care about the thousands of dollars differences. But at the same time though, they're kind of estimates based off of current situation and things change so much and stocks go up and down and acquisitions happen, and scandals happen and there's so many things beyond your control that I always advise people to prioritize an offer or a company that you're gonna fit really well at and perform really well at because your performance over time is more within your control and you'll be financially rewarded for that performance more within your control than trying to guess a stock, type thing.

Ryan 00:16:20:

Yeah. No, definitely. I mean, especially for early career. I mean, just one promo could be, you know, 40% more compensation and relatively in your control.

16:30 – His internal newsletter
Ryan 00:16:30:

Ryan: So I was talking with one of my old managers who's been on Meta for a long time, and I mentioned that I was gonna talk to you and he said that you had some. Internal newsletter or something that was really popular. I'm kind of curious to learn more about that. What was that and what made you start it?

Michael 00:16:46:

It sounds really immature in retrospect, but I had those, it was called the Weekly NTI. So I wrote a weekly blog post type thing. So the notes product on Facebook, it's a blogging platform type product.

It was unowned when I joined in 2009. No one product engineering wise, it was just code that existed. So it was something I worked on a lot at hackathons. Improving it. I added literally plain text. You could write plain text notes and post them. So. I supported Rich text in a single hackathon.

You can probably find the PR somewhere, or the diff somewhere, but it was 11,000 lines, I think. It's not how you build code. So I had to organize a meeting to review that code to get engineers in person because no one could actually review 11,000 lines of code.

Rich text editing and kind of spruce them up a little bit. And it kind of evolved. I kept adding a couple things here and there tags, I was kind of using it a little bit dogfooding, which is a big thing at Facebook, using the product yourself and poking holes in it and trying to give feedback and stuff like that.

So yeah, I was using it myself to post a lot of notes in general. And then I had a couple of posts that were just slightly controversial. Controversial about product building and yeah, different hot topics and. They got a lot of traction and discussion, so I started posting more regularly.

Some of them were very off the cuff, random things. There's one that was if I was CEO what would I do? Facebook was adamant about only having a Menlo Park campus and not having anything in San Francisco, and I was like, we need to have stuff in San Francisco. All the new startups Stripe and Uber, they're all in San Francisco and they're taking our employees and everyone wants to be there and all the employees are moving to San Francisco.

And Facebook was just no San Francisco office, no, San Francisco office. So I was posting a lot about that and I had one post about how they should open a South San Francisco office and that actually happened. So I was happy that that one came true.

Ryan 00:18:56:

When you look back on that writing, because I know some people do advocate you should start some sort of internal, you know, post in some Slack group or workplace group or email newsletter, just internally, would you recommend it?

Were there outcomes from that, that looking back you say that was a great idea?

Michael 00:19:16:

Overall, I would say that was not a good idea in retrospect.

Ryan 00:19:20:

Oh really? Why is that?

Michael 00:19:22:

So, okay. There wasn't a strategic reason to do it. I call it open and transparent and I think it comes from Facebook's values of being open.

At the time that was a strong value. And I really just believe in removing. removing the kind of surface pleasantries and facades and what are things more objectively and what can we do? How can we improve them? Or if you build a product and it got a lot of traction, but it was, there's always some luck involved.

But if it was more the circumstances that made the product grow and not the substance, we want to be real about that. This is awesome. We got really lucky that this product took off and it's not that great. We need to improve it. Whereas I see a lot of startups, a lot of bootcamps, if they get a lot of little bit of traction, they kind of think that that's how, that, it must be justification of the thing they built was awesome and they kind of don't hold the highest bar to keep ruthlessly iterating on it a tangent.

But generally my philosophy is to be just. Fairly open and direct and I want people to be that way with me and create that environment where people are just okay talking about stuff. So it was really about pushing Facebook's values and trying to have a company where people feel open about talking about things.

And it had nothing to do with performance reviews or growing influence or anything like that. There was no other motivation. But in retrospect I would say I would not do it. This is something I didn't deal with well at the time and I still don't know how I would've dealt with it.

It caused some friction and tension sometimes. There was one post where I just openly called out that Facebook has software engineered job titles where you can be a software engineer and move around to different teams and it's what you think of canonically as the software engineer.

But then they had all these other engineers, network engineer, data engineer. Those engineers couldn't change teams easily. They were hired to teams and there weren't quite the same privileges as a software engineer. And I just called this out very openly, out of the blue.

And I didn't realize that that was a big tension behind the scenes and it caused a lot of friction with different executives who are Michael, I'm working on this problem. I didn't really help us to call this out. We have to do damage control now. We need to talk about this.

And it kind of that off the cuff style, does have consequences. So I learned that and I try to try to adopt that still today, but I still am very big on, on Reddit and on LinkedIn on just trying to be direct and open and unfiltered a little bit with thoughts to try to show people that it's okay to do that.

Ryan 00:22:16:

Did HR ever reach out to you saying, Hey, you gotta take that down?

Michael 00:22:20:

Yes. There were no issues with sketchy type things. Oh, this is you need to take this down, like for the comp. I don't know. But I got feedback from HR on certain things. I had a post that was about which companies are hiring Facebook, poaching Facebook engineers.

And Uber was giving Facebook engineers very large stock grants at the time. And HR was not super happy. They gave me feedback that that kind of post, they thought it could incentivize people to explore other opportunities. It's not that I can't do it, it was just more feedback that, Hey, did you realize that you might incentivize people to consider other opportunities unintentionally with that post?

And I was no, I didn't realize that. And it's these were more off the cuff thoughts and maybe it wasn't worth the friction, but yeah. Even in that case, when I got that feedback about the engineers going to competitors, I was a bit concerned and I messaged Mark Zuckerberg directly and asked him how he felt about it and he was totally fine with it and encouraged me to keep posting.

So I felt it was okay to do that and I was still motivated to keep posting. Yeah.

Ryan 00:23:35:

You could directly message Mark Zuckerberg and he would reply.

Michael 00:23:38:

Yeah. I mean, when I joined Facebook was quite small, so I interacted with Foz, I think was my direct manager, skip manager for a while, and I regularly interacted with him even when I left, I messaged all the executives one-on-one Chris Cox and Repp and Jay and Voz and and Z and told them I'm leaving and you know, they responded thanking me for the contributions and stuff.

I feel I had a relationship with all people, all the executives at the time, but it was kind of from joining when it was small and from. Just genuinely interacting with them. I'd say of all the people though, Mark, I got to know more personally too, outside of work a little bit and have the closest relationship with him of all the executives.

But I have not talked to many of them for the past couple years. Facebook has really exploded.

24:26 – Working with Zuck
Ryan 00:24:26:

When you had just joined, I guess 200 people, probably not, but did Zuck still write any code? Did you ever see a diff from him?

Michael 00:24:34:

I actually worked with him on a hackathon in 2009. Zuck had this hackathon idea where, anyone should be able to put any emoji to any post as a reaction, right?

And this was in 2009 and now this is actually the norm everywhere. So he was right. I was a bit skeptical, but I thought it sounded technically feasible that I could help build that. So I was working with him on that during a hackathon and with another engineer, Tom Wittner, we kind of got it working, but.

The code was just so bad we, it never got shipped at the time, but he just did not give up on that idea though. And I remember when, I think Sammy Krug, I think is still at Meta, but I think she was the PM if I remember correctly, she was the PM who led the reactions initiative. And when it launched I was wow, this, it was done properly and well, and well designed and well implemented.

This is so much better than Zuck code. But, there's also another, there was another time though where he actually merged a PR and this is actually a Facebook, this is a crazy story, but there was this lockdown period in 2010 where Facebook was very concerned about Google Plus, potentially making it dent into Facebook's user base.

And there was a lockdown period where they really wanted to ship a bunch of features really fast. If there was food served on the weekend, it was pretty, pretty intense. And I was again, the all in person. So I was there all weekend. But during that period, I at one of the company, Friday Q and As, companywide Q and As, I basically made, that with Zuck that he wouldn't, if he was able to commit code by the end of lockdown, then I would stop rip sticking, which was a skateboard thing that was very dangerous, that's now banned that I would do around the office.

And then if he didn't commit the code, I can't remember what the penalty was. I don't remember what it was. Something.

Ryan 00:26:33:

Ripstick is that thing that you go like this, right? You have to go...

Michael 00:26:37:

You have a two wheeled skateboard and you have to wiggle your hips. I got really good at it, but it was really dangerous.

So there's rumors that Facebook's health insurance premiums were significantly higher than other tech companies because these ribstick were scattered throughout the office and there were so many injuries. Ribstick were eventually banned I think in 2012-ish. This is the craziest thing though.

The week before the formal ban went into place, the head of HR emailed the five most prominent ripstickers at the company. The head of HR emailed the five of us and asked, can you give us feedback on this draft email banning ripstick and. At the time, I didn't realize this, but this is a classic technique to try to get buy-in from opponents.

Try to bring them into the process more. So this was actually a buy-in. Hey, you know, ripsticks are gonna get banned, but can you give us feedback on how we communicate this? I want to talk to her about this part of her job, but I just can't imagine being the head of Facebook HR, tens of thousands of people and having to ban ripstick and having to get buy-in from these critics, or else it could be a revolt. That was a big tangent,

Ryan 00:27:54:

Oh yeah. What about the Zuck thing? He merged the PR and…

Michael 00:27:57:

Yeah. Bet in front of the whole company and then he actually merged the PR. So then, I think it was banned from riding a ripstick indoors or outdoors. I think they qualified it. There was a loophole, but yeah.

Ryan 00:28:13:

There's all these stories of early Facebook where Zuck actually wrote a lot of the code when you first got, there was a lot of it, you know, you look at the get blame or I don't know what, what source control early was. Would you see those people's names in there?

Michael 00:28:30:

Yeah. Occasionally. Yeah. There was a bit, I think there was a wave of engineers, in the Facebook kind of internal lore. The first engineers at Facebook were not known to be writing the best quality code per se. But they wrote code fast and they did a good job of what they were doing.

But there's kind of this wave of engineers. Facebook poached a bunch of former Harvard people from Microsoft. I think Boz was in that wave too. But there's kind of this wave of more mature or slightly more experienced engineers who came in.

Started laying out more, more structure and framework. And then they also brought in some other people at the time who really started writing more of the core abstractions and the stuff that was the foundation for the product infrastructure team. I don't know if the team still exists today, but it existed for a really, really long time.

Who builds all those core abstractions and maintains them and, that wave of people, their names are all over the code base, Evan Priestly and Putnam and these people. So these were my role models when I joined, when I wanted to be the coding machine who writes a lot of code and I saw these people's names. Those were kind of my role models of who I wanted to be.

29:50 – Engs that impressed him
Ryan 00:29:50:

Yeah. I'm kind of curious, you know, you, you grew in, into such a strong engineer, senior staff, IC7, who were the other engineers that you looked at that you said those people really impressed me and why?

Michael 00:30:03:

The engineers that most impressed me were the product infrastructure team working on.

the React framework, nowadays, but at the time it was more the PHP abstractions, Nick Shrock and Ola and, the, they were kind of, it was building out the, the end framework of today. That was built through my time. So I saw that it was going to get constructed brick by brick. And those people I kind of saw as the best engineer kind of thing.

I think Dan Schafer might still be, I'm not sure, but I saw those engineers as people, as a different type of engineer. They were, that was not the thing that was not my specialty. So the person who was most me was this person, Evan Priestley, who I think was the number one committer before me.

I don't know if he invented Clown. I don't know if you still have Clowntown. This idea of clowntown was if you caused a really bad, silly bug or typo or something, or you break main or something, you would be added to clown town. Philosophically, oh, he had a certain type of humor, I would say.

But, but he, he was very prolific. He single handedly wrote, the diff d review tool, diff camp at the time, which became fabricator, and when he left, they forked, they kind of opened, sourced it and wrote all of that entire product suite from scratch, himself. Basically.

Ryan 00:31:26:

If, let's say you are, you know, you're building your own team and you could either have him on your team to build out this new product, or you can have four senior engineers, just regular senior engineers, you know, which would you rather take?

Michael 00:31:45:

Evan Priestley.

Ryan 00:31:46:

Wow, okay. So how, how many senior engineers does it take till you would pick them over Evan?

Michael 00:31:55:

So it depends on the context of what you're building and this is something that comes up with me a lot too, is if you have this branding as this person who just writes a lot of code, it's not a mysterious process where the code just magically appears or something.

It comes from just work, hard work. And it comes from keeping a bunch of code in my, ram in my head, my memory, and, and paying attention to the littlest details and really getting absorbed in it. And if you put me on a brand new product, if you were Michael's a coating machine, let's put him on Oculus, firmware or something I would not be productive at first.

It would probably take me a really long time to absorb everything and suck everything in. I just have this magic power to do that. So I think it depends a lot on the context. If you're at a company and everyone's already ramped up on this thing and you have that choice, I would probably choose the coding machine.

If you're doing something really new, you might actually want a little bit more diverse backgrounds and diverse experiences so that there's a little bit more flexibility and creativity in the process. So I would actually qualify that it's context dependent, but all things equal in a comfortable code base.

I would want the coding machine. I have many, many examples over the years of things that just would not have happened if it wasn't for the single person, whether it's me or Evan Priestly or a similar coding machine. That's kind of what makes you the coding machine at that level is you're doing something that people did not think was possible and you're making it actually happen.

Ryan 00:33:41:

Can you give an example where, you know, something where you or Evan succeeded where, you know, a team of seven senior engineers would not have brought that through the finish line?

Michael 00:33:53:

The canonical example for myself is, there's this framework called preferables. It was a framework that in a given component separated the rendering code from the data fetching code.

So a given component on the screen, would have a data fetching function and a rendering function so that you could kind of, in different path waves, fetch all of the data in parallel, wait for it all to be fetched and then render everything. Those concepts have matured a lot now and react and all of the complexities with.

With suspense and spending and all these more intricate things. But at the time it's fairly simple, just component two functions, fetch data, render. That framework basically got replaced over time with async await and more modern things. But there were thousands of classes throughout the code base that people would be interacting with on a daily basis that were repairable, structured.

And I manually, relentlessly refactored and removed every single repairable until literally the, the parent class was removed from the code base. And I think there were three, five, 6,000 of them or something. Jesus, it did take several months, but I don't think that would've happened and it was a single handed effort.

And I don't think that would've happened otherwise. Believe it or not, now there’s a routing framework to route all of the URL requests to the right endpoints. It's abstracted now. I mean, it's been abstracted for many years now, but when I joined there were still PHP endpoints that were hit directly on the server, kind of old school web development.

And another project I did was to remove every single one of those and only use the routing framework. And it's again something that if there wasn't, the drive, the grit, the priority, it wasn't the most important thing for the company, but those things wouldn't have happened.

They would've taken a lot more resources that could be working on new products to do. And one person just single-handedly doing it can make all the engineer's lives a little easier to not have to deal with these legacy frameworks and stuff.

36:20 – Will LLMs kill coding machines?
Ryan 00:36:20:

I mean, what you just described, a large scale refactoring or super coating heavy task.

I could see an LLM doing that job quite well, in the future or maybe even now, to be honest. And so my question is, do you think that LLMs will kill the coding machine archetype?

Michael 00:36:40:

So when I was doing all this work at Facebook, I was using Vim and the tools I used were this thing called TBGS, which I don't know if it still exists, but it was just an indexed search of the entire code base.

But it was a proprietary tool outside of any id, a command line tool or a web tool. So I used that to find things and I think I had tab completion in Vim, a plugin for class names. That was it. And I was very productive. So even if I would've had VS code with modern tools that we have now, I probably would've been more productive.

The current wave of AI tools and the LLM based AI tools, are kind of a next step of going from Vim to VS code. It's going to a LLM AI powered mode that lets you be more productive, makes certain things faster, certain refactorings faster and changes faster. The next evolution going into agentic flows, encoding, popping up already.

Some success cases here and there. It's not mainstream. I think that those flows will probably be even more replacing those basic functions right now though. It's changing so fast. Things have never changed this fast. But for this year, I think that AI and LLM tools, most people, most engineers still don't use them.

You get off YouTube and Reddit and all these places. Just go to the middle of somewhere and ask an engineer. They're not using AI tools as much as the people who are pushing the leading edge. So if everyone used the tools, the way the leading, productive people are using them, then we would have a massive industry change already and we would all be more productive, including the coding machines.

And then the agentic flows that happen after that. I don't, I don't know, I'm not, I've not decided yet on how that's gonna impact the coding machine and or the rest of engineers as well. Because that's gonna really change things probably even more than we've ever seen before.

Ryan 00:39:00:

What's the biggest difference between, you know, how you used to work?

I mean, you mentioned this Vim workflow is basically your hand writing the code and doing everything yourself too, using the lms. What are the biggest differences you noticed?

Michael 00:39:14:

I'm in a code base that's 500,000 lines, give or take, which is not a small code base, not a tiny code base, but it's the size of a popular, open source, big project.

It's a reasonably sized code base, but it's small enough that I still know most of the code structure in my head and the, and and everything. So I'm not using that many, code wide agentic flows, or multi file flows in general sometimes, but not often. I'm normally using AI to speed up what I would already do, so I already know almost the code I would want to write, and I'm using LLMs to generate that code faster.

If I want to write an entire component that I think is gonna be a hundred lines of markup for the page, I have to make a real time judgment call, if I can type those lines faster or if I can explain. The most efficient prompt possible to an LLM in the right spot. How to generate those lines for me and have it be successful.

And I am just, you know, prompt by prompt building up that intuition on how to effectively give those prompts to speed up my workflow. And I'm in a spot right now where I'm very much more productive. We have a product, we are adding new features, the workflows are kind of pretty similar now that they have been six months ago for our product development process.

And I'm producing five times more code than I was then just through these optimizations. And it's changing so fast. So it's not an end game here. It's not there's this fixed path. It's every, every time a new model comes out, I am developing different intuitions or a new feature or.

A new, yeah. A new command line tool, stuff that. Yeah. So it's an interesting time for sure to be an engineer in general.

Ryan 00:41:20:

It's interesting, I mean, today and maybe soon also, it just seems LLMs are an extension, another thing to delegate to that makes us more productive. You mentioned the age agentic stuff.

If it can kind of, more independently generate code without the software engineer being involved, I wonder how would you feel if coding was more of a hobby in the future and programming was no longer driven by humans?

Michael 00:41:48:

I think it's a cool future. We talk about all the cool things that engineers do and, and why it's so awesome to be a software engineer, but if you actually clock your time.

Look at what you do as an engineer. There's a lot of stuff that's copy paste, search, copy, paste, change some lines, sit there and stare at the screen and think for a bit. There's a lot of things that are not as fun. And if you could really just focus on the fun parts, the creative product pieces, or even sometimes just building, I find joy and excitement in cleaning up code and combining things that didn't seem to have any overlap and merging them into one concept.

There's things like that. I just like doing that. Maybe as a hobby. Sergei’s brand at Google is probably the perfect example of this where he can just plop into whatever he wants to work on, and contribute what he wants to contribute there. And it's more, he's doing what he wants to do and there's, and not the day-to-day stuff.

So I think it's probably exciting in some sense. It's definitely scary to the software engineering profession because it kind of raises what does it mean to be a software engineer? Is it actually writing the code? Is it architecting the data models? Is it coming up with the systems level stuff?

Is it gluing it all together? AI is already making us think about those things and I think it's gonna be redefined many times over in the next few years. I think we're in this really weird transition phase though, where for the next little while, I don't know how long the next little while AI and LLM tools are gonna make engineers more productive.

Specifically engineers with a lot of experience and strong taste are gonna be more and more productive. And if you're not an engineer with lots of experience, it's gonna be harder and harder to build that, more confident in that. But in the future, beyond that, AI can write its own code and maintain its own code.

I don't think code will be the same as it is today. If an AI can do its own thing, it's not gonna be writing JavaScript, it's gonna be managing its own services that have an API and it's gonna do its thing you might not know how it's building it. And as long as that API is contractually provided and it is doing its thing and meeting whatever specifications it has to, then it doesn't really matter how it's being built.

And it might be doing its own thing and no one might know what that code looks like. And it might not even be readable. I mean, engineers make a lot of mistakes. Humans make a lot of mistakes with code and cause really bad bugs and AI's probably gonna have bugs and it's gonna have ways to fix them.

We are going to build AI to do those things. I don't think it's gonna be this dystopian future, overnight. It's gonna be step by step as we get there. I think it's gonna happen, so I don't think we should push back on it. We should be thinking about, how do we make this AI world the best that it can be instead of pushing back? That's where I stand on that.

Ryan 00:45:05:

You, you mentioned there were some React engineers that you looked up to and their archetype was different from yours. What, what impressed you about what they were doing? What, how would you describe the archetype?

Michael 00:45:18:

It might fall under the specialist archetype where you're really, really, really good at one stack. Another example is this engineer who knew email protocols and was one of the 10 people in the world who deeply understood email protocols. I know it's, you can look up the specs, but the practical side too of dealing with spam and routing and all this stuff and, you know, so there's a, I think it falls into a specialization, bucket.

In general, I'm a fan of the sports team analogy. So, you want a professional sports team that where every, every, every player on a baseball team can play any position, pretty well. Even the pitchers who only throw can probably hit the ball better than most typical people or even amateur baseball players.

So it's kind of you want your team to have those different roles and you want to respect each other's place on the field. So I kind of respect those engineers for what, what they do. And I have my thing and I think that the whole team is exceptional if it has these different, these different players.

Ryan 00:46:30:

I see. So what impressed you about those engineers is that they solved problems that other people couldn't.

Michael 00:46:35:

Yeah. And the abstractions they were creating specifically were very impactful because all the engineers are using them on a daily basis. So a lot of the coding machine work I'm doing that impacted everyone was cleaning up and making their lives easier.

And these engineers were writing frameworks that made the thought process less overhead for an engineer to fetch data and stuff that. So there were some similarities a little bit, but I respected that work a lot. But it's very hard to come up with such an elegant API that's super performant and is easier to use.

Making things simpler is sometimes more work than writing a lot of code or harder work too. So I respected them for that.

47:20 – Operating as an IC7
Ryan 00:47:20:

I wanted to talk a bit about your career growth. Because you grew to, you know, senior staff or IC7. At Facebook, there were less IC7s at that time, so it's even more impressive that you did that and as quickly as you did it.

So I'm curious to kind of dig into some of the, you know, behind the scenes in it. I, I think you've told this story publicly a few times, so I kind of want to ask some of the side topics on it. So, one thing I'm curious about, you mentioned somewhere that you had spent 30% of your time on your team's work and about 70% of your time on side projects or projects of your own initiative.

How, how does that work if you know you're getting work from your current team? Can you talk about that?

Michael 00:48:07:

I think the way I framed it is almost like being a senior engineer on a small team of 10 people, and then, spending more than half my time doing kind of code base wide initiatives. Clean up refactorings and a new framework.

Sometimes some random, random one-off thing a team needs help with or something. Emergency, other work. So, I would say 30% work very much. If you just imagine having an E5 on your team. It wasn't 30% of my eight hour day was the team and only contact me then, it was more like 30% of my mental space or my focus, I think.

So I would still be on the team all day long. As a senior person, you're reviewing a lot of code, you're bouncing ideas off more junior people, you're mentoring, helping junior people grow in scope to get promoted from entry level to mid-level, those kinds of things. Writing a lot of code on features that the team queued up.

Contributing to them, going to product meetings and contributing to the product direction, evaluating feasibility of things when product managers we want to do A, B, C, and it's okay, well A and BI think we, the team can do c they can't do, you know, general things a senior engineer would do, but the volume of code produced was more a senior engineer on the team. I would say.

Ryan 00:49:46:

How did you manage the relationship with your team or you know, your manager for instance? A typical manager knows you have bandwidth, kind of positions you in a certain area, but it's a little unconventional the IC is doing that. The majority of their bandwidth is solving problems all over the place. So how did you manage that relationship?

Michael 00:50:10:

I would often report, not all the time, but I often reported to more junior managers and I was almost a peer. Skip would generally do my performance reviews, but I would report to a more junior manager. I would almost help them manage the team and then really report to the skip kind of thing.

So it was definitely interesting relationships. The head of one of the VPs I would meet with monthly for the whole work and my skip level, I would meet with every two weeks.

Ryan 00:50:44:

So in the org chart you reported to a frontline manager, but in practice you were almost dotted line reporting to some more senior people. It's almost a weapon of the org. That you kind of just go wherever. Let's say I'm a senior engineer and I want to go solve problems for the org all over the place and I'm reporting to my frontline manager. I got my tickets or whatever. How did you transition into that IC7 solving the hardest problems for the org role?

Michael 00:51:19:

In my case, I was almost the coding machine from day one. Even the raw output was probably honestly the same when I was a week into Facebook. There were two different, a fork of the task tool. It was called ANA and Cortana, and it was the same data source for the internal task management tool.

There were two different UIs. One was streamlined and fast and one was bloated with features and slow and there was competition between them. And I, in a week or less, I merged the two code bases into one that was the speed of the slimmed down one with all the features of the bloated one.

And it was, I just literally just took the initiative entirely on my own. I didn't even tell anyone. I mean, this is so early on, you could not do this now, but, I didn't tell anyone. I just merged them. I posted to the entire company. The tools are merged. It's done. Deal with it kind of vibe.

Not, not in a mean way, but a surprise, right. The output was really the same. What I learned though was, that's not the best way to merge tools that are used by hundreds of people to just be surprised, URLs changed, deal with it.

I didn't deeply understand the consequences for teams. Everyone patted me on the back and thought it was amazing because no one could have done this. So overall it was still positive, but. The things I learned were judgment calls about, the scope to change things at, how to pay attention to the impact the changes will have on other people.

Building up intuition about what spots are more sensitive than others to make changes in. And that judgment of doing these massive things over and over and over again and doing some of them too fast and having too many bugs. And there's some people who will forever not like me because I caused a really bad bug because I made a bad judgment call and then I learn, take the feedback and then keep going at the same speed while improving my judgment and building that taste.

And I think that accumulation of judgment and taste is what crosses the line to the E7. But the rot output, it wasn't the rot output kept going up. So I don't necessarily have advice on how to build that, because I think you have to kind of, it's very dependent on your org, your team.

But I think if you want to do that, I would start by talking to your manager and if they can't really help, maybe talking to your skip level manager. And if that doesn't really help, try to find a really senior engineer who is maybe that person and ask them how they did it in that same org as you, or in their org similar to yours. It's kind of, it's very dependent on the context, but yeah.

Ryan 00:54:31:

If I'm understanding correctly, then you were able to work on all this extracurricular, you know, org-wide projects because you had such high productivity and that was true from day one and you had the initiative too. No one, no one's gonna stop you.

Let's say you have your project on your team, no one's gonna stop you from doing extra work that solves some problem on the side. And so you, you took that initiative and you have exceptional productivity, so you just became known as this person that's constantly solving extra problems.

Michael 00:55:09:

Yes, but I really think that the judge, the judgment and taste piece though is so critical. And it's more than just the code. It impacts a push process. So now there's continuous integration at Facebook. At the time, there wasn't, if you broke something and it shipped to production and you needed a fix, the pushing team would not generally be happy.

And you have to negotiate with them in a sense. And if you break things too much, they don't trust you and they will not accept your changes. They might even push back on your normal changes. So that hurts a coding machine. So I have to build a relationship with the pushing team. So they really trust me.

And more than once I've said this needs to get in and if it breaks the site, I will resign. Quote unquote. I've said that you said that because I burned credibility before, the day before, shipping something too fast, I had to be very sure. So sure with the fix that I would, you can fire me if it breaks things.

And those types of things to build that, that trust and credibility. Another engineer who just shows up and writes a lot of code probably would not be able to get away with it because they didn't have the years of building that up. So it's a, that, that is really important. It's not only the raw, it's much more than the raw output there.

Ryan 00:56:30:

Would you have resigned if you broke it again and you said you would?

Michael 00:56:35:

Yeah, I think I would've. That's pretty crazy. It's this weird, maybe personality trait, but that puts so much pressure on me that I will make sure that it does not break. I will, I will triple check every line. I will think about every weird case that could possibly happen.

Ryan 00:56:55:

You talked about taste and judgment when it comes to code and software engineering, what does that mean?

Michael 00:57:02:

People who cook with cast iron pans, they talk about building a patina where you have to build up layers of history and it gets burned into the pan and it has a care, a profile.

That's to me is taste. There are some people who, who naturally have instincts. Maybe it comes from the way they grew up and their past experiences they have and the context they're in. They have stronger taste, faster. But generally it just requires experience in some way.

You might have experience outside of code that might build up. You might do lots of dancing and you build up all this intuition and muscle memory about. Dancing or a sport. Other sports and stuff too are similar. It's kind of that, but in the coding context you might read a book on how to be the best, the fastest speed skater.

You read the book and you just got to put the skates on and you just have all the ambition and you just want to be the fastest, you know, you can do it. It's you, you have to spend years doing it and really, feel it building up every aspect of the muscle memory, every movement on the ice, the feel of the ice under different temperatures and altitudes and pressures and the sharpness of different skates.

You'll be able to feel the difference between a skate that was used once versus twice. It's every detail you will over time accumulate by putting in the time and gaining that experience. So, and I see far too many people rushing early on where, in their careers where they're trying to jump ahead.

They're, they're, they're trying to enter the Olympics as a speed skater and they have not. They haven't built that yet. And that's okay. You can't build it overnight and there's nothing wrong with you. And I advise people to put in the practice and the reps and I mean at Formation it's really important to get feedback because if you just do this without feedback, then you don't improve.

If you kind of set yourself up to do practice, get feedback, iterate, and really have the grit to keep going, following through on that, then you can get to that super top tier stage of, I think any, any skill.

Ryan 00:59:16:

So when you say taste, are you saying, your intuition behind how you design software? Or are you talking about problem tastes, which problems are worth solving for the business? Which code matters more?

Michael 00:59:31:

Both for different people, a product and a product manager. Their taste is probably more in terms of prioritizing what products features to build. They probably build, they build that up through building lots of products. Failing, failing, building something doesn't work, building something doesn't work.

All the junior product managers, super ambitious. They just need to keep shipping things and seeing what doesn't work and they build that up. And then you see the exceptional product managers, 90% of the stuff they shipped was not good at or failed for some reason. And that's why they're so good is because they learned all, they learned each step of the way and then they made changes and grew from it.

So I'm talking about that for an engineer that applies to, or for me at least, that applies to code itself and writing code and the strategies to moving really fast and stuff.

Ryan 01:00:20:

You mentioned changing other people's code or the social norms around touching code that other people own.

And you know, you said something about a landing, a bug in that code base kind of really could blow up in your face. So did you ever get feedback from other teams? Because it sounds like you were kind of touching everyone's code and how'd you handle that feedback?

Michael 01:00:45:

I think there were some times where, you know, going into a code base replacing some old framework that on the live version of their tool, the team's tool.

And they were already building a newer tool and maintaining, carefully maintaining backwards compatibility. And they had lots of diffs and pull requests in play that were they had their thing going and by just showing up, refactoring that some, some stuff in the old tool and then leaving it made their, it caused a lot of merge conflicts for all their stuff in progress and they, weren't happy about it.

And they wanted to revert the change from the code because they didn't want to have to deal with merging that into their complex change. Right. And adds feedback to be careful of that stuff. I wouldn’t pay attention to that. So it's okay, that is one, one use case. Where you got to be careful is if teams are working on complex, longer term things, migrations already, be careful in that area of the code.

Ryan 01:01:47:

What about the case of ownership? So, you know, software isn't just about creating it, but there's all this management and maintenance burden after it's created.

Did any team get upset? He said, Hey, you add this feature, great, but who's owning this thing now? Who's gonna actually maintain it?

Michael 01:02:08:

That didn't come up for me and I don't know if it's the philosophy, I don't know if it's still the case, but the philosophy back then was every line of code you wrote, you're responsible for, Kent Beck talked about this recently that Yeah, he was, it's a really strong sense of ownership.

If you are okay being woken up at 3:00 AM and you're gonna respond and fix some bug in your code anytime of the day, anywhere, then, do what you want with, you know, don't write tests, then go ahead. As long as you're maintaining it. If you don't want that and you want to work nine to five, then you might want to write more tests to make sure that your code's stable when you're not around.

So I think if I didn't just touch code, didn't refactor code and forget it. I was responsible if there were any bugs. And then in the future, sometimes two years later, there's something that, I get an automatic bug assigned to me because it's, you touched this code last, and I'm oh man, I don't even remember doing this.

But then I would fix the bug because even though it didn't cause the bug, it was just, that is now my code. Now I didn't, I didn't have any territorial conflicts because I don't, I don't know why I, I didn't, I just didn't really come up. I never, I didn't step on people's product judgment.

This is part of the judgment calls I guess, that you're building up. It's kind of like performing a surgery and you got to be really careful about what you're changing. I learned, maybe learned the hard way from making some mistakes early on and being a bit too aggressive in certain areas. You start to learn where that line is between, messing up people's day to day and not, and still getting the refactoring or the cleanup done.

Ryan 01:04:00:

One thing that I'm curious about, you know, as you become a more senior engineer, it's very common to get pulled into more and more meetings, miscellaneous overhead.

How did you manage your focus as you got promoted to be a coding machine? You must have had a lot of focus time. Even as IC7.

Michael 01:04:19:

I really try to minimize my meetings. If someone just added you, I don't know if this still happens, but people would just make meetings, add you to the calendar.

There's no context. It's just something, something sync. You're, I don't know what this is. I would ask, what is this? Which I think people maybe, I don't know if it's still the norm of change, but I would push back on a lot of meetings. I generally didn't go to standups unless it was relevant.

We're working really hard to ship something in a month. I need to go to the standup every day because it's important to be on pace. But if there was a standup that was more just social chitchat, because the team, I don't know, some standups end up being that way. I, I don't know if you've seen them, but, it happens and I would not generally go to those.

But yeah, so just being pretty, pretty strict about time. And then also having the manager's support was pretty important. I was pretty choosy. I made very conscious team changes when I, whenever I did change teams and the manager was very in tune.

Managers at Meta, their job is to make their reports perform exceptionally well. I don't know if that's how you would summarize it in one sentence, but, if your reports get promoted and have a lot of impact, that's what makes you recognized as a high performing manager too. And so my managers are generally trying to protect me and manage me so that I can have the most impact possible.

Which means not getting pulled into a lot of meetings were unnecessary. But I also think I was too arrogant sometimes. And that's one of the things I would tell my older self. I definitely remember walking out on a meeting or two where I was just, I don't think this meeting's useful for me anymore. I'm leaving. I'm just leaving you.

Ryan 01:06:18:

You said that?

Michael 01:06:19:

Yeah. I just remember this happening a couple of times and I'm, wow. That was not good behavior. Oh my God. I almost feel really bad because the person running the meeting probably felt really bad and now I feel really…

Ryan 01:06:39:

Did HR ever reach out and say, Hey, you're, you're productive, but can you be nicer and stuff that?

Michael 01:06:48:

No. I mean, because I wasn't, mean, it wasn't a flip the table type thing. I had a good relationship with most, I think all the PMs I worked with, I had a pretty good relationship with because I built stuff really fast.

I fixed bugs really fast. Not even my own bugs. Just if they had, if the PMs, the PMs that a lot of the PMs that, I mean Meta is a very high performing company, almost everybody's very strong who works there. And the PMs are, they want to get stuff moving fast. They pay attention to every pixel and they're oh no, this is broken, this test wasn't configured right.

And there's things that I was very helpful to PMs, so they actually liked me a lot. And if I had to leave a meeting, they would almost give me permission. Yeah, Michael, you don't really, you're not needed for this next part of the meeting. You can go, it was not as jerkish as it sounds. But I just remember being that cutthroat where it was just, I don't want to spend time in meetings that I can't be coding. It was that, that, level of strictness, I would say.

Ryan 01:07:57:

You mentioned that your productivity over your whole career was high and it didn't change that much. What changed was what you wrote code about and the problems that you solved. How did you grow that skill of project taste or picking problems that mattered so that the code was more impactful?

Michael 01:08:19:

So first of all, I don't think that I'm great at it, necessarily. I'm still not good at prioritizing in general. I pick things that I know how to do, if that makes sense.I pick things where I see the answer in my head and it's just how fast can I type, or get this into the code. And which is also why LLMs particularly are helping me be personally so much more efficient because I have what I want to do in my head and I need to get it out fast.

And LLMs can really help with that. So sometimes, it might not be the most impactful thing, but it's a tricky thing. And I have the idea in my head on how to do it. I might just do it even though it's not as important as, another thing, honestly, this is probably one of the things that held me back career wise, and it was also frustrating for my managers if they did try to communicate, Hey, this thing's very important.

Can you do that? And I'm, I don't see the answer to it. I don't have it in my head. I can't do that super fast. I need to see the answer, you know, in a sense. So I'm gonna work on B. It's, can you please work on A, but I have to do B, C, D, E, F, G, H.

And it's okay, that's a lot of work and that's helpful, but it would be really good. I think that that's one of the things that probably held me back in general because that limits. If A really, really was so important and I, and it did not get done. You get a passing grade for doing all the other stuff and it's appreciated. But overall impact would probably be higher by doing A, if I was able to do it. But, I'm somewhat limited by what I can figure out how to do. I frame it as a weakness, but yeah.

Ryan 01:10:08:

That's interesting. So you always optimize rather than business value fully. Your rank ordered list of priorities was what can I just crank out instantly?

Michael 01:10:20:

Yeah. And if you crank out enough stuff, it adds up and it can have a huge amount of impact. But it is definitely a different way of thinking at work, I think.

1:10:30 – IC7+ only group
Ryan 01:10:30:

So once you got promoted to IC7, I think you had shared that. You were added to an IC7+ only group. And I'm curious, was there anything interesting you learned by being a part of that group? Or was there anything common among all the IC7+ engineers?

Michael 01:10:48:

There's a certain, there was a certain kind of bar that everyone had regardless of if they were a coding machine, regardless of if they were a specialist or a fixer. These different reasons why they're there. Everyone had certain traits that were common, extremely strong, due diligence and conscientiousness.

And very, I wouldn't say fast or quick, I don't know the right word, but very sharp sharp's. The word I'm looking for if, if. This group was even me as someone who I feel I'm not, I was a very strong student in school. I was a straight A student. I think I'm a pretty smart person, but most of these people are still smarter.

These are exceptionally smart people who I would have to acknowledge might be smarter than me. But we all could be in the same room and talk about something very and very quickly move through the concepts. So, here's this new proposed protocol. And instead of having an hour long presentation on it and discussing it, everyone would be pretty sharp sharply be oh, what about A, B, C, D?

And the follow up questions would happen very quickly. Very sharp, fast conversations. And very high attention to detail. Some people were really earlier in their career, accelerated very fast. They had these traits, maybe their personality traits. For me, these are more personality traits I would say.

It's leveraging OCD in a way, a productive way to be obsessed about every detail of the product instead of things that are not productive for other people. They had their 25 years of experience and they kind of built these things through different ways, but everyone kind of had that.

Whereas when a lot of conversations with junior people, there's a lot less context, there's context missing. The follow up questions are not necessarily as sharp and on super fast. It takes a little longer to get things out. Usually the projects are smaller and scope as a result and stuff like that.

1:12:55 – Landing code faster
Ryan 01:12:55:

One thing I want to go over is kind of a set of topics on just, how do you land code fast? Let's say you're, I'm a, you know, new software engineer. Yeah, I want to absorb your coding machine's abilities. Is there a, you know, top 20% of tips that is gonna give me 80% of the benefit to become more productive?

Michael 01:13:20:

The general advice is you have to move, to say it just in the shortest way possible. Do something, write code. A lot of people who ask me for advice or questions, they're thinking too much about what to do and not doing enough. So step one is do something, just do anything.

And then step two, which is critical, is getting feedback from, respected people or, or people who, who have that experience and taste and judgment are further down the line and getting feedback from 'em and then actioning that, and then repeating. I thought that. My manager hated me because I was writing so much code so fast that was so bad.

And he was writing, he was doing code reviews and his code reviews, he was, he was very frustrated because he was spending all day reviewing my code because I was writing so much code and it had so many problems. And he was just, please follow the style conventions. These kinds of things, right?

And, it sounds that's annoying, but that's step one is you got to get the raw gears turning. And then once the gears are turning, getting the feedback and then iterating. So if you get feedback like follow the style guidelines, then you actually have to do that next time.

And then there'll be something else wrong and then you improve it. And that cycle compounds exceptionally quickly. If you're writing a lot and you're getting feedback from experienced people and you actually action it, it works really well. The, the biggest mistakes people make are there's, three mistakes.

I think the first one, not turning the gears. Not doing anything, I said earlier. The second one is not getting feedback from the right people. If you're a, a bootcamp grad and you're getting feedback from another bootcamp grad who graduated six months before you, who's the instructor now, and they're giving you feedback as the instructor, that feedback doesn't encapsulate that experience and taste and that judgment that you want to learn from, that you're trying to learn from in this process.

It encapsulates the judgment of someone who's a little tiny bit further ahead of you. So you want to get feedback from people who have that, the judgment and taste that you aspire to. And then the third mistake is, and this is a mistake that I made a lot, that I would tell myself to not do, but is not actioning the feedback and taking it more judgment and approval rather than feedback.

If someone gives you feedback and you're taking it as a judgment or an approval, you want to pass the test. If you failed and you want to pass it, and you're not actually reflecting on the feedback, you're just taking it as approval. You're not gonna iterate fast enough, you're not gonna make enough changes.

You might change the wrong things because you're not accepting the feedback. So if you do all that, I think you can, and you do it fast, you can accelerate your progress so much.

Ryan 01:16:29:

You're saying, basically shorten the cycle time and then make sure you get good feedback and then internalize it, and just, that's gonna compound.

Just shorten that loop and just keep going, keep going, keep going. I see. Let's say I am, I'm outputting a ton of code. I'm already a code machine, but I want to get better. Do you have any advanced tips on how to take it to that next level? Let's say I'm pretty productive already.

Michael 01:16:56:

I would be ambitious. More ambitious probably if you have your coding machine thing going. Take on something ambitious that is pushing yourself a little bit outside of your normal scope of wherever you're, you are, you're in the code, or, this is very specific to Facebook and Meta though in general because you're, your impact is somewhat judged by breadth and scope and the wider the umbrella, the bigger the umbrella, kind of the more higher level you are and the more recognition you get.

So in that environment, if you're a coding machine in your department, you got to push beyond the department and push your comfort zone a bit. My advice to my, something, I was saying, I'm not good at accepting prioritization from leaders, but that's actually the advice I would give though if you're stuck, is to ask, talk to ask your.

I don't know. I had many, many one-on-ones with the C-suite at Facebook where I was just, Hey Chris Cox, I need, I want to talk to you about this thing and have a 15 minute one-on-one. If you're a coding machine that has credibility already and you're stuck, reaching out to more senior people in different areas and trying to get some ideas of those wider scoped projects, if you're really stuck, it can be a step forward.

1:18:29 – Why he left Meta
Ryan 01:18:29:

Coming to the end of the interview, just want to do some, you know, career reflections and stuff like that. You were at Meta for quite a while and you had a lot of success. I'm curious, why'd you leave Meta and what was your thinking behind the career planning there?

Michael 01:18:46:

So Meta got quite big, quite fast. And there was this turning point, six years, three quarters, the way time went through there, where I felt when I was all in on, on Facebook, I felt it had my back, a hundred percent. I had their back a hundred percent. It was a little bit culty, maybe. And then it felt more like a company, a business, a business relationship. It was changing. So that was kind of the first sign where I was open to leaving. And then I won't go into all of the details about the vesting cycles, but there were some vesting logistics.

Certain years they had some longer grants for various reasons and the vesting cycles and overlapping and stuff. There was a very strong point where it was your compensation, your take home pay is gonna drop 80% in a month, over a certain period. Wow. So I was kind of, okay, you know, this is maybe the time to ramp down.

So I think after the previous performance recycle, when that was coming up, I basically. Said, I'm gonna be leaving in three months. And then I did a little farewell tour on Messenger for kids to be, my manager was, okay, do you want one last hurrah? And then they did.

And I kind of slowly ramped down over that period. And I was taking home stuff from my desk every day, slowly ramping down. But it was definitely, it was just kind of that at formation now, I mean obviously, I'm a founder, so also I have more control over that.

But it's really, I'm all in or not all in and that all in-ness broke somewhere three quarters another time through Meta as it got bigger and bigger. And I needed to put that somewhere else, that dedication somewhere else.

Ryan 01:20:43:

Yeah, I mean, getting a 80% pay cut is, coupled with the cultural changes, you know, makes, seems a good time to leave.

1:20:52 – IC7+ talent
Ryan 01:20:52:

When it comes to the highest levels of performance in ICs, what's your take on how much of it is talent and how much of it is hard work and growth?

Michael 01:21:03:

There is talent. Some people have more talent than others. Some of it is maybe your biology, some of it's just how you grew up and opportunities you had. And some of it is you have raw talent that's not discovered yet.

There's all kinds of views on talent, but it is a thing and it does come into play. So there is an aspect of things that are talent in quotes. If you feel you're, oh no, I'm not talented, you might actually be talented and it hasn't been discovered yet. Or you might be talented at something that isn't your day job right now and you should figure out what that is.

And that's actually Formation. That's our big, long-term vision, what we want. And why I do what I do every day now is we want people doing the work that is. The most impactful work they can do, and we want to help them find that work because not everyone grew up the same way, able to explore and find what that thing is, and they might have not found it yet.

So we want, you know, I feel, I feel everyone has some kind of talent or something that they're better than most other people at. And if you find out what that is, that is a big piece of a high performance. And you might not have that at your day job right now, and it might limit your performance a little bit.

It's not, it's not the whole thing, but it might limit it on the other hand, hard work is within your control. My friend Phillips, who talks about this a lot, but he says, talent is something out of your control. And luck is outside of your control, which is another thing that comes into play sometimes.

But, hard work is the one thing that's within your control. And if you maybe aren't, you're in a place that you're, you're good at your job. It's maybe not your natural talent, but you're good at it. And you do it and you want to keep your job and you want to do better, you can outwork people who are similar to you and you will probably be recognized more performance wise as well.

Ryan 01:22:58:

What percent of your career growth would you say is luck?

Michael 01:23:01:

Of the growth? I think it's 50/50. And I came from Canada. When I showed up on my first day of Facebook, they gave me, I got my laptop and left the onboarding room and they called me back because they said that I didn't have my phone and I didn't know what they were talking about.

They give you a cell phone and they gave us all these accessories and this bundle, it was a red carpet. And I was, what is all this stuff? I just need a computer. I came from a place that was a lot more of the things you hear about tech and the way that engineers are treated and compensated now is very, very weird.

So if I had stayed in Canada and worked at a company, I would probably be doing quite well, but I wouldn't have had the same acceleration. The luck was really landing at Facebook at the time that I did and it being the perfect fit for my personality at the time and the values were extremely aligned.

Code was aligned with what I could handle and that part is pure luck. So I would maybe just say 50/50. I've seen a lot of people who don't have the same drive and got the luck piece and they're also doing very well, but either one of those could work out and be okay. But I think I got both of those and that worked out very well for me personally.

1:24:28 – Advice for younger self
Ryan 01:24:28:

Last question. If you could speak to yourself when you just graduated and give yourself some advice, knowing everything that you know now, what would you say?

Michael 01:24:37:

I think going back to what I said earlier, I was very much, and I see this a lot with people preparing for interviews at Formation nowadays, seeking too much approval for things, pats on the back approval.

They want to pass the test, they want to submit their coding, see a green check mark, they want to. I was that person. I wanted to get the highest grades and I didn't really know what I was learning even, I just wanted to get an A+ or a hundred percent. And because of that, I was not accepting feedback as feedback to improve.

I was accepting feedback as a grade to judge myself and put pressure on myself to get a hundred percent next time, but I wasn't putting pressure on myself to actually improve. So my advice to people who are ambitious and who want to get those perfect scores and check off all the boxes is to really reflect on feedback on how you can improve and try to push your comfort zone there instead of trying to look at it as a judgment or a grade.

Ryan 01:25:40:

Awesome. Well, thanks so much for your time, Michael. I was really looking forward to talking to you and you know, hopefully the audience got something helpful out of this as well.

Michael 01:25:49:

Yeah, and if anyone has any follow up questions, I'm very, very approachable. You can ping me on LinkedIn or Reddit or whatever, and I’m happy to chat.

