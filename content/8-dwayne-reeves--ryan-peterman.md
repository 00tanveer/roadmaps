---
Dwayne Reeves is a Senior Staff Engineer (IC7) at Meta who is the Tech Lead of the most used programming language (Hack) at the company. He started at the company as a new grad from MIT and shared the story of how his career grew. We discussed:

- His promotions to Senior (IC5), Staff (IC6), and Senior Staff (IC7)

- The value of type systems

- Transitioning to a TLM and why he switched back

- Working with brilliant engineers and overcoming imposter syndrome

- Advice for his younger self
---

# Tech Lead for Meta's Most-Used Programming Language (Promotion Story)

Timestamps
(00:39) Joining Facebook

(04:52) Did MIT help with career?

(07:13) His first team

(10:37) Why static typing is superior

(13:17) The uncanny valley of type systems

(16:11) Senior Eng (IC5) promotion story

(19:24) Staff Eng (IC6) promotion story

(23:38) Manager transition story

(28:57) Managing ICs vs EMs

(32:54) Senior staff Eng (IC7) promotion story

(35:42) Impressive ICs

(40:33) Why stay at Meta

(44:28) Advice for younger self

Transcript
00:39 – Joining Facebook
Ryan 00:00:39:

Thank you Dwayne, for coming on. I really appreciate your time. Today I wanted to go over your career story. I feel there's a lot of interesting stuff because you started at Facebook when it was Facebook and pre-IPO and all of that. Alright, well let's start at the beginning of your story.

I see that you started at Facebook right out of college and you went to MIT. I'm curious. Were there other offers that you were considering and what was the story behind you joining Facebook?

Dwayne 00:01:07:

It's actually an interesting story because I really wasn't interested in Facebook, to be honest. I was really interested in Google and Twitter.

Twitter, because I was a big fan of Scala as a programming language, and I knew they used that at Twitter. And Google because I grew up on the East Coast and they had offices in Boston and New York and Facebook didn't at the time. Why I ended up interviewing for Facebook was actually as interview practice.

I had a friend who was working at Facebook, and he was trying to - he joined, I think back in 2007 actually and he was trying to convince me throughout my time to come for internships or other things. I was thinking, I don't really know. I don't see myself going to California.

And he said, this would at least be good practice for your Google interviews. So I was thinking, sure, let me do it. So I did end up interviewing and ended up making it to the final rounds. And when I actually got on campus, my whole viewpoint started to change and open up. Just being able to talk to actual engineers and the kinds of problems they were working on.

I was obviously a user of Facebook being a college student at the time, and it was hard for me as someone who is interested in more core CS problems, thinking Facebook's just a website. What is it really for me to do? And when I actually got on campus hearing some of the problems they had to solve with memcache and just how to scale up a system, hearing things around how they optimize PHP by having their own custom runtime for it. All these things made me realize, oh, they're actually doing some real engineering work here. That got me pretty interested.

Ryan 00:02:48:

At Google they're also doing real engineering too. So what was the thing that made Facebook really stand out?

Dwayne 00:02:58:

Yeah. Well, Facebook actually gave me an offer. But I think overall the other thing is, it's just the level of care I felt. They really wanted me and they showed it in sometimes not so subtle ways. Two things that come to mind. One was when I got my offer, it was the best offer I had.

I didn't end up getting an offer from Google. I did have an offer from Amazon. I didn't accept right off the bat because I needed some time. I said, hey, I need some time to mull over my offer. A week later I got an email out of the blue from my recruiter saying, hey, we just increased your offer.

I was thinking, wow, I didn't ask for this. Versus Amazon, I talked to the recruiter and they're thinking, yeah, we don't negotiate with new grads. You just take what they give you. The second thing is, at the time I remember, I think I had already decided to join Facebook at that time, but there was something where the CTO at the time, I think Brett Taylor.

He actually came to MIT's campus and took all the new grads that were accepted and took us out for lunch at a local cafe to talk with us. So all these interactions, I was thinking, wow, I couldn't imagine any C-suite level person at Google or any of the other companies I was working at actually taking the time to talk with us personally. So that really felt special.

Ryan 00:04:24:

Because they were smaller, they're able to do that, more tailored recruiting. What was the rough size, just to give people a sense of is this startup or is it kind of growth stage company?

Dwayne 00:04:35:

Yeah, I think at the time it was probably between a thousand to 1500 employees, so not small. But also, well given we're a hundred times bigger now, it is small. It's all relative.

04:52 – Did MIT help with career?
Ryan 00:04:52:

Hearing that you went to MIT, it's not controversial to say that obviously is a big leg up when getting interviews, you mentioned one of your peers had already been working at Facebook, but one thing I'm curious, now that you have all this experience in the industry, how much of a correlation is there between the prestige of the college you went to and career success?

Dwayne 00:05:19:

I think very little of it has to do with the actual education piece you get at different universities. My education at MIT was fantastic. There's a lot that it taught me, but I've also met lots of engineers who I work with, who some of them didn't even go to school.

So the thing I really know for sure was a big differentiator between me and them was I just had more opportunities because MIT had this name recognition that, for my freshman year I was talking to recruiters from any tech company. They would always come to a career fair and be willing to talk to me just because of the school I went to versus other engineers I work with.

It was almost just by chance they even got on Facebook's radar and they were just as capable engineers as me, but just because of, I guess, a different path they took in their career, they very easily could have not ended up at Facebook, which would've been a huge loss for the company.

Ryan 00:06:23:

It definitely increases the opportunity and chance elements of it.

Dwayne 00:06:29:

Yeah. I mean, I remember my freshman year I had an internship from Microsoft. Almost that alone was enough for me to get an internship offer from Apple as well. It was just kind of crazy. Because I remember, I grew up in Bridgeport, Connecticut. Growing up in the inner city, going to public school, child of immigrants – working at companies like Apple or Microsoft was the dream. I never thought real people actually worked there. Immediately going from that to, oh yeah, there's recruiters here and they actively want me to work with them, was not anything in my head. I would've even imagined being the case, but MIT was just normal for the students there.

07:13 – His first team
Ryan 00:07:13:

You joined Facebook, you got the offer. They sold you in. What was the thinking behind joining your first team when you entered Facebook?

Dwayne 00:07:22:

We were looking at developing a service that was meant to evaluate some pieces of code and move it outside of the main PHP code base, because PHP was seen as not a great language to develop in.

So we were thinking, if we use this new language we develop, we can do some computation closer to the data stores and all these ideas. This will help efficiency and all this, these big dreams. Honestly, this was not a team on my radar at all. But they reached out to me because, well, maybe my resume.

They thought it would be interesting and that was one of the great first times of actually trying to do something language related, where for the most part all I was doing was trying to translate PHP code into their own custom DSL that they were developing. But I was on that team for maybe two years and by the end of it I was actually trying to develop new features for this language.

Ultimately that project ended up getting canceled. Then I started working on more things related to privacy infrastructure and how we find ways of representing privacy policies and rules in an easier to manage way than just simple if or out statements. And I did that for a couple years. At that time, Hack was introduced to the code base and we were kind of the newest framework that decided we're gonna go all in on using Hack for it.

Types, which is what I love because I grew up working in statically typed languages. I just thought they were superior. So PHP was always weird. And after that project I was trying to figure out what I wanted to do next, and there was this opportunity of different parts of the code base and all that was written with PHP was not typed in Hack and I could make an attempt of trying to type this using Hack. So it was meant to be a week or two project. It ended up taking a whole quarter, but it was very rewarding because it allowed me to interact with the Hack team a lot because they were anxious and interested in having more people use Hack in codebase.

And I was trying to do something which honestly no one else had attempted at the time of how do we take a very core piece of API that was not designed to be typed. How do we actually go about doing that? And there's a lot of hacks, a lot of bash scripts, a lot of ingenuity, I guess I would say. So the end result was, after I completed this migration, about 20% of the call sites, moving it to the Hack API, discovered that there is some kind of error in the code, usually around how it handled null types.

This was what I view as one of the big results of, hey, Hack is not just this cool tool, it's actually finding mistakes in the code base at scale. I feel that is really what started to have Hack be taken a bit more seriously. Maybe we should be more aggressive in terms of replacing PHP with Hack.

10:37 – Why static typing is superior
Ryan 00:10:37:

You mentioned dynamically typed, statically typed languages. Are statically typed languages objectively better than dynamically typed ones in industry code?

Dwayne 00:10:46:

It's subjective, but I think a lot of evidence that points to yes, they are superior, particularly. And the way to think about it is, particularly if you think about the problems we face at a company or a code base at the scale of we develop here at Meta or any larger industry, it's more of an information communication problem where as the size of a code base grows, the more you have to keep in your mind of the context of, well, this code is meant to do this and this code is meant to do that.

So if I change it, this is how it needs to work. It starts to break down. As you have more people who are working in the code base and the size of the code base grows, you just naturally need tools to help you manage that. And type systems just happen to be an effective tool for communicating intent.

Maybe there's cases if you are just a hobbyist and you're working on your own and you could just keep everything in your own head. Yeah, you could probably move faster with a dynamic language. At the scale we operate with, where even if you get a hundred engineers, you need something that helps you communicate ideas and keeps track of that.

And that's where I feel types really help. Types also help with tooling, right? So you have auto-complete, it helps you search the code base and all these other things beyond just giving errors that it provides value in is not surprising. You see, even for dynamic languages, most of them have some form of optional types, at least for that reason alone.

Ryan 00:12:18:

I guess some of the obvious advantages are it brings more of the state or what we're trying to communicate explicitly written into the code via the types, and then also because of that tooling and various static tools can traverse that and provide value to us. So that's a big value add for industry code, is that right?

Dwayne 00:12:41:

Yeah, and it's actually kind of incredible to think about that. You write some text in the file and because you write it in this way, we have developed ways of proving that, hey, this text you've written does not exhibit these classes of errors at all, and you could just rely on it. And that's really powerful. And it's one of the main achievements we've had in the space of computer science.

Ryan 00:13:10:

Definitely formally verifying that this bug cannot happen because of those types.

Dwayne 00:13:15:

Exactly.

13:17 – The uncanny valley of type systems
Ryan 00:13:17:

In my research and studying some of the type migrations I think you had mentioned before, this uncanny valley of type systems. I'm curious, can you explain what that phenomenon is and what you mean by uncanny valley?

Dwayne 00:13:32:

I grew up playing video games, so this is a term I learned in that space from computer graphics, as you try to make something look more human-like in general, you feel better about it.

You feel more connected to it as it starts to look more human. But then it gets to a certain point where it's almost human-like, but it's off in subtle ways, and all of a sudden you get kind of put off from it. And me being familiar with this term, I feel the same thing will happen in terms of as you move from dynamic languages to static languages.

And the reason I felt this way is at the time people who only worked with dynamic languages didn't necessarily have the muscle memory or weight trained in their brain? What does it mean if I have a type? It actually is not correct. And as you add more and more of these, the places where the types actually aren't doing what you would expect in a static language that exists, the more off-putting it will feel.

And so that's how I came up with that concept, right, was comparing this to how it applies to the space of graphics, human graphics, and trying to make a similar analogy to communicate this point. And it proved to be a really effective way of contextualizing the problem we were trying to solve on the Hack team at the time.

Ryan 00:14:57:

In the process of migrating to a fully statically typed code base that last bit. Actually things start to get worse because you're almost there. And so the bugs that come are much more subtle and the behaviors are much more subtle and it's actually worse for a bit till a hundred percent.

Dwayne 00:15:14:

Yeah. And I think there's even something particular, because we were, the foundation of the language was PHP was that at the time there were certain behaviors PHP had.

Which were incompatible with trying to make a sound type checker for it. And there were some questions at the time of, well, should we keep those behaviors or should we get rid of them? And I think my post was more making a statement, we should get rid of those behaviors because if you have a language, even if you had everything typed, the fact that the types can't be relied upon because of these subtle behavior differences.

Then that will be a problem or will create a less than ideal state for development. So I think that's also some of it is because of PHP and some of the peculiar decisions they made of how their runtime would operate.

16:11 – Senior Eng (IC5) promotion story
Ryan 00:16:11:

And so in your time as an IC, I know eventually you transitioned to management. So you must have had some promotions and things that helped your career grow. Are there any stories, particular times where you felt, okay, that was a really good learning experience and helped you grow as an IC?

Dwayne 00:16:28:

Yes. Two of them come to mind. So one was when I got promoted as a senior engineer.

I mentioned earlier about this project I worked on, of trying to create a Hack API for the end framework. So since that went well, I was asked, hey, can we do this at a larger scale? Can we move more code from PHP to Hack? And so I ended up spending a half doing that. And at that time, up to that point, my idea of what value I gave to the company was 100% based off of what code I was able to output. And so when I started this, I was talking to so many people. I was giving ideas to the Hack team, giving ideas to other engineers, what to work on that had almost no time to actually write code myself. Because of this I felt I was having the worst half I ever had at the company.

And I remember having a conversation with my manager about this and she was thinking, it's important that you know you're doing the right thing in terms of talking to other people and getting them involved, but you should find some time to write some code on your own. And I don't know if she talked to her manager afterwards, but I think the next one-on-one, she was thinking, yeah, that thing I told you that's actually wrong.

Keep on focusing on just what the end results were. For me, the thing that really connected is still at the end of that half I thought that, I was thinking, yeah, we had some results. Yes, we increased the amount of Hack adoption of, or coverage from I think 20 or 30% of the code base to 60 or 70% now.

Hack felt it was a fixture in the company. People weren't really looking to write PHP first. Everyone was starting to write Hack first, so I felt I had good results. But again, I wrote the least amount of code at my career so far. So I wasn't sure how that was gonna play out in terms of my performance review.

And the thing that really connected was, oh, actually that was the highest review I ever got. I ended up getting redefined at half. Wow. And I got promoted to IC five, which I wasn't even in the conversation because I thought, oh, I'm not writing enough code to even justify that. And it really solidified to me that.

Writing code is just not what my job as a software engineer is. My job is to identify and solve problems. Sometimes that's the best way of doing that is writing code. Sometimes it's me bringing clarity to a problem and the path forward for how to solve it. And if others end up writing the code, then that's fine.

So that's something I think was a pretty big mind shift there of experiencing, okay, I don't have to be the most efficient coded machine out there, right? There's other ways I could add value. So that was definitely one of the pieces.

19:24 – Staff Eng (IC6) promotion story
Dwayne 00:19:24:

And the second one was also, I guess, what led to my promotion to IC six.

So after that half right, that I just explained, I was asked to join the Hack team. So I wasn't even on the Hack team at the time. So this was, started in, I think 2015, right? I joined the team. They said, hey, you would be the tech lead. I have no idea what that was. And most of the engineers who were on the team before they ended up leaving.

So it was me, another engineer I brought on the team who I worked with before and a new grad hire. And we were responsible for this whole system. I quickly. Struggled for a few years trying to understand what was my role as a tech lead. I was comfortable that my output didn't necessarily need to be related to the code I wrote, but I still felt I was responsible for seeing the outcomes end to end.

So one of the things I worked on was trying to redesign how our collection system, work arrays and stuff within Hack and I spent all this work on the design, spent a whole year on it, and convinced our runtime team to implement it. Started with the implementation and started to roll it out. We had some new hires join the team and I was thinking, all right, here's my project to get me the IC six is trying to complete this. And I remember my manager telling me, okay, Dwayne, I actually want you to work on something else. And I was really upset because I was thinking, what? Why are you telling me to work on something else? This is my project. It's up to speed. Why do you want me to do something else?

And this is my path. And he gave this analogy, which is really interesting. And it's, think of what you're doing. You're a rocket ship and different stages as you are firing and you have the initial set of engines that are meant to leave the orbit, right? But once you escape the orbit, there's other jets that can fire. And he was thinking, I only cared about you getting us outta orbit. Now that we've done that, you should pass this off to someone else and now you can find something else to do instead. And he wouldn't let me leave the one-on-one until I agreed to do it.

And I passed this on to another engineer and I was, I don't even remember what I was focusing on. But I remember the half ended and again, I was thinking, okay, well I did that. So let's talk about what my path for six to be. It's thinking, oh, actually I just got you promoted, so congratulations. You're now six. So in both cases, those promotions were kind of a surprise for me because I had a mismatch between expectations in my head of what I needed to do to perform at the next level, versus what in reality was important. Each time it felt like being okay with having less direct control on the outcome.

And the real important thing I did was just aligning what the right strategy and what the right problems were in the first place.

Ryan 00:22:20:

A lot of more senior ICs, the value is they come in, they figure out what's important to solve, why, get all the alignment, and now there's this. You've left orbit at that point.

This is something everyone's interested in. Then you hand it to someone who's great at getting it done. And so, and it's cool that your managers were proactive and driving your growth. Because it sounds like you weren't really eagerly involved and figuring out, hey, what do I do to get six and scale myself, okay, I'm gonna go scale myself.

It's almost you begrudgingly did the things and they were coaching you and you just got promoted as a byproduct.

Dwayne 00:23:00:

Yeah. It was also a bit earlier at the company, so some of it was probably they are willing to move faster. Hey Dwayne, we see the potential in him by holding the promotion for another half.

Having a strong relationship with your manager is the thing I see most consistently in my career, whenever I felt disconnected with my manager is when I felt most frustrated. The times when I felt most connected is when I felt I was doing my best work.

Ryan 00:23:28:

And I think I see that through line in a lot of people's careers, almost everyone who has had success, they had a good relationship with their manager.

23:38 – Manager transition story
Ryan 00:23:38:

And so speaking of management, I know you eventually transitioned to being a manager. Curious what made you want to try management? What's the story behind you becoming a manager?

Dwayne 00:23:47:

It's interesting because it's kind of similar to how I ended up at Facebook. I didn't wanna be manager.

It was not a part of my career plans. The team was at this point, growing rapidly. And my manager at the time, he was thinking, hey, we'll need more managers on the team just because of the growth rate. Here's an opportunity for you and we could either try and find another manager externally, or you can give this a shot.

And I said, no, and the next time I met him, I heard about the TLM role, tech lead manager. And I was thinking, oh yeah, I could do some coding and maybe a little management. This might be a nice transition. And I mentioned it to my manager and he was thinking, oh, you don't wanna do this. I was a TLM at another company.

You're doing two jobs. I wouldn't recommend this as a manager. So I was thinking, oh, okay, that's fine. I won't be a manager. I think he probably talked to my director because he came back, the next one-on-one. He was thinking, actually, yeah, we should try this. You could be a TLM or whatever you want.

Just try this management thing. And since I was starting to get more comfortable with delegating, I was thinking, okay, if I'm still technically involved, I could try being a manager and still have some technical influence on the team. And for me, the main decision around that point in my career was, there's so many times that I've discovered if I was set in my way of just trying what I felt comfortable with, that anytime I did the opposite and did something I felt I would be uncomfortable with led to better results.

So I was thinking, okay, I don't really wanna be a manager, but it will force me to learn a lot and it will force me to be uncomfortable. So I was thinking, okay, I'll give it a shot.

Ryan 00:25:29:

I hear that advice often that TLM is two jobs and it's not super sustainable. After you tried it, what was your experience with being a TLM and would you recommend it to others?

Dwayne 00:25:45:

The first couple years, it was actually pretty, it went pretty well. As a new manager, I started off with three reports. I then went to four and five. Then there's this big shift where essentially I had the whole team under me. There was supposed to be a manager in Seattle for part of her team that had left.

So I had maybe 12 or 13 reports, and I started saying, all right, can I convert this person to be a manager as well? And I started having managers report to me and I was still given technical direction, right? I think the thing that became tough was as the org started, we were successful, so we continued to grow and it became harder and harder to think about.

All right, how can I continue to contribute as a tech lead while also figuring out how to scale out this org? And there were some ideas I had around how to do it, which was basically, I need fewer reports so you get three managers to do all the management, and I'll just manage them. Then I have time to think as a tech lead.

My own manager at the time, he didn't think that was the best outcome for being a healthy org, which I think makes sense because he has a lot more experience being the org leader. Ultimately, I got scaled down to, here's the fewer direct ICs I worked with and I continued being the tech lead overall.

So it wasn't necessarily the workload that was the issue, but it became something. Where does the thing that helps the team the most align with the base responsibilities I need to do as a manager. So here's a way to kind of demonstrate this, right? So as a tech lead, at the time I think there were 35 to 40 individuals on the larger team that we were working with were on the language team.

And so the best thing for that 35 to 40 group of individuals of what I should do is different versus the maybe six or seven ICs I was directly supporting. And so I had a PSC where I would be great as an IC. I was told I would get a GE, basically my role as a tech lead for this group of 35 to 40 individuals I was doing really great at.

But as a manager, I wasn't failing. I was a good manager, but I had to do that job successfully. I wasn't necessarily looking to exceed as a manager or do or maximize the growth of those six to seven individuals I was supporting directly and this became something that's actually what's best for the team long term?

And ultimately, I had a choice of, I could basically try to replace myself as a tech lead, so I could focus on being an org manager or go back to being the IC so I could focus more freely my time on what the needs of the larger organization needed from technical leadership. And the choice became obvious for me as it was just easier to find a manager for six to seven people than me trying to find someone who can be an effective tech lead for our group. So that's what led me back to being the IC.

28:57 – Managing ICs vs EMs
Ryan 00:28:57:

You mentioned that along that journey you managed some EMs and you managed ICs as well. I'm kinda curious what's the difference between managing an IC and EM?

Dwayne 00:29:06:

It's really the difference between trying to support someone as they are working through technical problems versus people problems. One of the things I had to get used to as a manager is when you're at IC or you're doing something technically, the feedback loop between you doing the action versus you seeing the results of that action is shorter versus what you try to do as a manager, right?

So if I'm working with an IC, I'm trying to up-level them so they could take on larger bits of work or learn how to be more creative or thorough in terms of the work that they do as a manager. The things I attempt to do in one meeting, one one-on-one, I have no idea if it helps, right? There isn't something I could tell, oh, I hit compile and then it passed, or I ran the unit test and now it passed.

But as a manager, it might be six months, nine months down the line where something clicks or they come to a meeting or one-on-one and say, hey, I finally got that thing you said, and I'm actually seeing results from it now. That same thing applied to a people manager is even a longer loop, I'll say of the problems they have of, and some of it was, I was a new manager, so I wasn't always necessarily clear around, well, what's the best ways of getting them the things they were struggling with as a manager, what advice can I give them? How can I coach them up? It wasn't something that I actively went in. I need to do something different for these managers. Right. I was kind of a vibe manager.

I was just thinking, this feels the right thing. And I think for the most part, things were fine, right? From a standpoint, the team, the org was doing well, but I wasn't necessarily focused on optimizing the org. I was thinking, fine if the org just ran right and I was able to do technical work. So I know you asked about what's the difference between the IC and the manager in terms of management.

It was more for me, I was realizing my brain was focused more as still as the IC is the org is fine for the most part. I'm not looking for other opportunities to see this organization operate more. Those are the kinds of stuff I think you should be thinking more about as you are more of an org lead and are supporting other managers, is helping them think about as they have their own team, how they should coach others or how, what opportunities they should be thinking about or even seeing, does it even make sense for them to be a manager still, or should I or is there some other opportunities?

So these are the types of stuff I probably should have been doing more of as a skip manager. I think the thing I enjoyed the most around management though was around the coaching. And so that's what I leaned on a lot more one-on-one was, what's your problems? How can I help?

Ryan 00:32:08:

And it sounds the coaching that you enjoyed most was IC coaching because you enjoyed being in IC yourself, so, and you're saying that for EMs reporting to you, the best thing is to kind of flip that switch and start thinking about the best org design and how do we grow people and how are they gonna support their team?

Dwayne 00:32:28:

Yeah. And that just wasn't the natural way I was thinking day to day particularly because yeah, I was the tech lead. So if I came in 80% of my day focused on what's the technical challenges we have and how can we best tackle them? Trying to switch to 20% of my brain of, well, is this even the right structure we have to best execute on this plan? I just was not good at switching between the two.

32:54 – Senior staff Eng (IC7) promotion story
Ryan 00:32:54:

At some point you're promoted to senior staff or IC seven equivalent. I'm curious, what's the story behind the promotion?

Dwayne 00:33:03:

So we talked earlier about this uncanny valley post and that was really, that vision was what drove the team for a while as we started to scale up the size of the team and what we were pursuing. If you asked anyone on the team, what were we doing? It was, oh, we're trying to cross the uncanny valley. And I think what led to the promo was basically enough things lined up as we were executing and we were making progress towards this.

That was attributable to my vision that it made sense to be promoted. Right at that point. It was something I remember being a bit more active, talking to my manager about, and at that point in time was kind of seen as just a matter of time. We just need to see more results. Because I had a clear vision I had laid out and we were starting to see results from it.

So we just needed to see it a little bit further along before we got the promotion through. And yeah, I ended up getting it, the half before I switched back to being an IC. So I was actually still a manager when I got promoted. I think at the time they said officially TLM didn't start until M2 equivalent.

So if you're at M1 and you're a tech lead manager, no, you're just a manager. Right? But I think the promo to M2 was based on the technical contributions I gave as more IC as opposed to my ability as an org lead.

Ryan 00:34:28:

If I'm understanding, the blast radius of what you'd done was basically. Migration of the full to fully statically typed on one of the base, I guess, languages that almost everyone was using.

I don't know the exact percentages, but hundreds at least maybe even thousands of engineers using this. Is that right?

Dwayne 00:34:47:

Yeah. I joined a team in 2015. We had a mix of some Hack and some PHP. We soon moved to basically everything being Hack. We also had some notion of Hack strict mode versus a partial mode where strict had requirements that you wrote all the types that were necessary versus partially you could leave things out or whatever.

And by this time I got promoted, we basically got all the code base. So back in 2015, all the Hack files, which were in the code base, maybe only 5 or 10% were strict. So by the end of this, right around the time where I got promoted, we more or less had all the code base now being strict Hack and so that was a pretty remarkable difference, plus a bunch of other work we did of changes to the language runtime and other things that had kind of paid off at that point.

35:42 – Impressive ICs
Ryan 00:35:42:

Coming to the end, there's, I kind of wanna go over some career reflections going over the story. Well, one thing that I was curious about is because you're early at Facebook, you've probably had a lot of chances to work with some very legendary ICs and curious, is there any IC that you worked with or you thought you were really impressed by them? Or maybe you have a story about working with someone.

Dwayne 00:36:04:

Oh, yeah. Oh, there's so many excellent ICs I've worked with, so I almost feel remiss if I call some out, but I'll mention one. Kendall Hopkins. I worked with him when he first joined the company and he's an excellent IC who was really good at understanding the code base, our main code base that was running Hack. I was thinking from a language perspective, he was thinking more from the developer perspective. What are they actually trying to do? What are product’s needs? What do product engineers need within this code base?

And he just was an excellent engineer and helped to think and strategize, how do we make these larger changes at scale across the code base? So he was very key, I think, instrumental, in my success. Another one that comes to mind was Paul Bisset. I don't know if I said this explicitly, but when I joined Hack, I had no prior experience with languages or compilers or anything.

Honestly, I didn't even know what a lexer was, which is like a database component of a parser. And Paul, he answered, he was my sounding board, I could ask him anything and I felt comfortable, no matter how dumb it was, he would take the time to explain it. And so I don't think I would've survived, particularly when talking with the HHVM team, if I didn't have Paul there to kind of teach me different concepts.

And another one I just wanna call out is, he's still a colleague of mine, Andrew Kennedy. This guy is incredible. He's literally written foundational papers on type theory. I would do some research, let me look up some things around type theory. And you're thinking, oh, Andrew Kennedy, his name is here.

And he kind of figured this out and it was one of those cases I did not, when I first met him, I did not know how amazing or his pedigree that he had, and he's one of the most humble guys I've met. For someone who's so accomplished already, working with him has really showed that I shouldn't be afraid of someone's prestige.

I have value to add, even if it seems I'm more junior or anything else, right? That there's always something. Everyone has their strengths and there's something you could always add to that. And with Andrew, there are times where we talk about different language features or ways of typing.

And even though I didn't have the same background, finding ways where we can communicate. And see he would say, oh, Dwayne, it's actually an interesting viewpoint I hadn't thought about that. Made me feel, hey, I could actually punch and hold my weight and then there's stuff he'll do.

I'm thinking, I had no idea how to even think about this problem. So yeah, those are just some of the ICs I really call out as me having worked a lot with and seeing just some of the amazing work they've done at the company.

Ryan 00:38:58:

It sounds it was humanizing working with them because you, I mean, I guess if you had just heard about him, you'd think this guy's untouchable, but getting to work with him and seeing him be friendly, adding value and discussions kind of made it so that you were not scared of his pedigree. Is that right?

Dwayne 00:39:16:

Yeah, and that's something for myself, having been on Hack now for 10 years and been at the company for almost 14, it's something I'm sensitive to as well because I still remember that time of when I was just a younger engineer. And so every once in a while I'll go, I'll meet someone and I'll introduce myself and they're thinking, wait, you, you're the Dwayne. You're the Hack guy. And I'll think, oh, don't think of me that way. I wanna be approachable.

I want people's ideas to feel valued and, yeah. We're all humans. We all learn things, right? And just because of whatever I've accomplished in the past or any ideas I have doesn't mean I'm always right. I'm always looking to learn more. And I think that's one of the things that was great around the team I had was just so many senior ICs.

Those with, some I talked to had more experience working on programming languages than I was alive at the time, but yet,

Ryan 00:40:23:

Yeah, that's crazy.

Dwayne 00:40:23:

But yet how willing they were to talk to me and explain their approach and I just think that's something all senior ICs should try to emulate that. Humility.

40:33 – Why stay at Meta
Ryan 00:40:33:

You mentioned you've been at the company for a long time. I'm curious, what is the thing that you find keeps you at Meta? I think in this industry, a lot of people hop jobs.

Dwayne 00:40:43:

Yeah. So there are definitely some times I think of where, and I was considering jumping ship and the thing that I always reflect on, right is, is my motivation for moving trying to solve a temporary problem. So let's say, hey, at the time I'm not particularly happy with the project I'm working on. Is that really a reason for me to leave the company?

And versus, and each time I would interview and I'll have an offer and I was thinking, is me making this change or move really going to change the fundamental problem I feel I have at the moment. And each time I reached that point, I would just objectively look at, well, what are the problems I have and what are also the things I enjoyed about the work I did, and particularly growing up at this company, things that I was being, I had a voice that would have carried weight.

I had opportunities to help bring in diverse talent into the company. Frankly, how many opportunities are there to work on a programming language? That was also the piece. And I had a great team. And so if there was a moment of, yeah, there's some discomfort that was for two months, is that really worth changing over?

And for me, I always was thinking, yeah, I could sit through it and most of the time things ended up improving. And so that was for me, my perspective is that I don't want to make permanent decisions based off of temporary circumstances.

Ryan 00:42:31:

And it sounds, I guess in those cases when it wasn't good, the situation was resolvable, it was not something that you couldn't change or your manager couldn't help you with.

Dwayne 00:42:40:

Yeah. I feel some of the things in terms of what would've led me to leave, is if I didn't feel valued. And in a lot of the cases, when I would look at, there's all the signs that I am valued here at this place. And so the issues were not focused on that. It was something else. Oh, it's the project I'm working on. Do I feel it's not getting the recognition it deserves?

Some of it realistically might be I just have a warped view of what I think should be recognized, and if I talk and really face this, yeah, I'm actually wrong here, or maybe they are wrong and with enough time, they realize that. If I fundamentally did not believe in the mission of the company or I felt my manager was creating a toxic work environment.

Things that would be more of what I would see as, yeah, if I'm in that situation, I would've left already. But none of those were the circumstances I had and honestly, I feel I'm a bit privileged and fortunate to experience that in my career. And it leads to a lot of, there's just been so many great people in my time.

I've been able to work with both managers and others at the company that it's let me really have a career so far that goes beyond my wildest dreams, right? When I was first learning to code as a high school student, child of Jamaican immigrants, I would've never in my wildest dreams have thought that I would've ended up with the opportunities I've had working at this company.

And it's not, I don't wanna say sentimental, but it's really appreciating that I've actually been really blessed and really fortunate.

44:28 – Advice for younger self
Ryan 00:44:28:

And I guess the last question I wanna ask you is, now that you have all this experience, if you could go back to yourself right when you graduated college and give yourself some advice, what would you say?

Dwayne 00:44:40:

I get asked this often, and the thing is, the thing I'll say is, hey Dwayne, I know you coding. The thing you should realize, right, is when someone goes and tells you, hey, can you write some code to do this? You should stop and think. How do they know that's the right code to write? You should aim to be the person who's making those decisions around what's the right thing to do.

There's a lot of imposter syndrome and other stuff I dealt with earlier in my career that having this clarity is not about, I'm more than what I can type on the keyboard, right? My ideas and the value I derive is greater and focus, not on just being an output machine, but really being the one and focus, can I be in those rooms that's deciding what's the right thing to do?

Ryan 00:45:27:

Yeah. Thanks for sharing. I feel someone with your amount of career success sharing that you had imposter syndrome, I think that can be helpful for a lot of people.

Thank you so much for your time Dwayne. I really appreciate you coming on. It was a pleasure, Ryan, thank you so much.

