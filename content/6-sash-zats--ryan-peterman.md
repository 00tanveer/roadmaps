---
Sash Zats grew to be a Staff Engineer (IC6) at Meta despite switching teams 10 times in 9 years. His career journey was a series of jumps to exciting projects and letting career growth happen as a byproduct. I interviewed him to show you how team switches can play out.
---

# Instagram Staff (IC6) Promo Despite 10 Team Switches in 9 Years (Career Story)

Timestamps
(00:49) First team: iOS on Newsfeed Delight

(05:30) What makes a good designer partner?

(08:30) Joining a hardware team

(12:08) 2 diffs in 6 months

(15:03) Joining the Instagram blockchain team

(21:37) Joining Instagram Threads pre-launch

(28:53) Working with an exceptional engineer (Peter)

(33:02) Working on AI prototyping teams

(37:15) Reflecting on team switching’s impact on career growth

(44:35) Why leave Meta

(46:15) Advice for younger self

Transcript
00:49 – First team: iOS on Newsfeed Delight
Ryan 00:00:49:

Well, let's start at the beginning of the story. So how did you pick the first team and what was the story behind that?

Sash 00:00:55:

Well, my first pick was this team based in London, and they're like, we're gonna work remote and it's gonna be fine. But the code review times with London, they would take days and so I ended up sort of designing against that and I chatted with this one guy, he's also still at the company, and he saw my resume. He saw that weird hybrid of design and engineering and everything was poorly defined. And he was like, listen, how about this?

We are gonna build a team that takes all the design prototypes that designers always have stacked up in their desk but never shipped, right. And we're just gonna build them. And no metrics, no nothing. And it was inside of newsfeed, Facebook newsfeed. I mean, now if I would look back and I would hear newsfeed, no metrics, I would be like, oh yeah, this team is gonna survive half a year.

And it survived half a year. But the value prop was just so fun to me because it was like, oh, let's build the right thing and not worry about metrics and the things that we built. Later we found some metrics to associate with that.

Again, it didn't survive long term scrutiny, but it was a lot of fun. It was all sort of really joyful projects. The team was called Newsfeed Delight. And yeah, it was just building all sorts of fun visual animations effects. That's sort of what people usually call “Easter eggs” in the apps.

We were building that and it was so much fun because again, every designer dreams of that, but then every engineer looks at it through the lens of impact and they're like, I'm not touching this. And the other theme through my career was that I'm just not thinking about impact too well, and that allows me to pick the teams that are completely irrational and high risk and God knows if there are even rewards in there.

Ryan 00:02:40:

I saw those teams that you worked on initially, the design ones, and I was thinking, how do you measure success or how do you prove that this prototype was a good idea? Kind of going off a vibe. So I'm curious, what does a successful project even look like?

Sash 00:02:56:

So I think in the spaces that, now I can rationalize how it's done in a company like Meta.

You have some executive sponsor with some sort of theory that they justify to someone and that's basically how those teams survive. So Facebook used to have this metric called CAU, "cares about user," and this metric was literally a survey issued in newsfeed that would ask you some broad question of, do you feel Facebook cares about you?

And this highly subjective metric that I'm not even sure if everyone understands it in the same way, was what a lot of teams were orienting towards. And so this kind of fed into that.

In today's world where you want everything to be highly efficient and there is not too much time to focus on these moments of delight and joy.

It's sort of harder to justify the existence of those kinds of teams.

Ryan 00:03:51:

You mentioned you weren't optimizing for impact at that point, and it sounds throughout your career that's a common thing. What were you optimizing for in that team choice?

Sash 00:04:00:

Fun. You know, just pure fun.

I often end up in the situations where looking back I'm like, oh, that was lucky, that was cool. You just meet people and you explore some opportunities and later, again, sort of looking back, they all make sense. Mostly because proactively you don't know what's gonna happen, but also you end up accumulating this toolbox of skills, people, connections, you know, all those things that you can build upon later.

I feel I'm joining a team because I have some intuition of oh, this might be fun slash interesting slash whatever. Later in career I became a bit more intentional, but still sort of optimizing for this riskish space. Zero to one space. I think that's what I noticed early on, and there was again, sort of coming from startup days, is that a lot of people are sort of uncomfortable with ambiguity.

They're uncomfortable with poorly defined spaces. You know, sort of ambiguous spaces. No product definition, no direction. And a lot of people, they're really good engineers, but they need this sort of oh, this is what we need. This is the diagram, this is the mark. Whatever, where maybe because of the design past, maybe whatever, I would always be oh yeah, we can kinda figure it out as we go, right?

And sooner rather than later you realize that it's an asset. You know when you can be effective in this environment that's sort of challenging or ambiguous to others, it's an asset that you can use. Then it's a question of yeah, how do you measure this effectiveness?

05:30 – What makes a good designer partner?
Ryan 00:05:30:

You had a lot of opportunities to work with different designers. I'm kind of curious from an engineer's perspective, what makes the best designers to work with?

Sash 00:05:40:

I think it's just the collaboration, sort of process. So the most fun I have is with people who are ready to sort of jam with you.

They don't just come up with this idea in the vacuum, because oftentimes for better and for worse, it's not informed with real world constraints, nor should it be. But then when you have this design, initial design, it's oh, but what happens when your network fails? Or what happens when users don't have this field in their data, whatever.

So you need this constant dance between here's this idea that we want to achieve, and here's the real world inputs. Oftentimes what I would find even more fun is when you show designers. Oh, look at all those cool capabilities that we can actually use in your design. So what if we use some sort of location to inform how this looks or if you use the accelerometer of the device to move the shadows a different way. It's all the stuff that not every designer necessarily knows or remembers off the top of their head is a fun way to inform the creations.

But then also this iteration loop, in my experience, the tighter you can get the iteration loop the better. And I had a few projects on some unreleased pieces of hardware where the whole thing was for me to build a hacky version of Figma to an unreleased device rendering pipeline. So the designers can just see their Figmas on an unreleased device as quickly as possible and just move stuff around and immediately see it being reflected.

So all the iteration loops, the shorter they are, the better. And the more both partners, engineers, designers, whoever else is involved, are ready to hear each other and sort of internalize the constraints and sort of talk about it. The stronger products come out.

Ryan 00:07:29:

So if I'm understanding correctly, you mentioned the short iteration loop, but also it's kinda this bi-directional communication. Engineering might propose something that design doesn't know. Design does the same. And the end result is a much better product.

Sash 00:07:44:

Yeah, for sure. I also find it really helpful when you just start the project to not involve technical constraints too much and just be okay, cool, yeah, we're gonna build this crazy thing that you want, and then you sort of trim it down to meet the world where the world is.

Right. So if it's hardware, well what is the, I don't know, thermal envelope that you have to work against? Well, maybe the device is just gonna blow up if it runs for so long. Or you know, maybe, yeah, processing power is not there, so it cannot be as real time as a designer.

So real life constraints that will get in the way anyway. But yeah, it definitely helps to start with a pretty, you know, sort of everything is gonna be working the way you want and then sort of inform each other and sort of bounce off each other and this definitely builds a stronger product.

08:30 – Joining a hardware team
Ryan 00:08:30:

So I think that first leg of your career you were working on traditional iOS kinds of things, very design oriented. And I understand that you pivoted at some point more towards a completely different domain. You switch teams multiple times. Even within iOS. But then you switched to an entirely different domain in hardware and prototyping experimental hardware. What was your thinking behind wanting to shift to such a different domain?

Sash 00:08:58:

I was just looking for a new sort of team, and I started by looking at, you know, various iOS teams. We have this internal jobs tool. I was looking for something in New York and I just couldn't find anything that was sort of appealing enough, but then there was this posting for a new hardware team. And there was not really that much information. At the time the internal job tool was sort of semi updated once in a blue moon. I think now it's more rigorous.

But yeah. And so I reached out and turns out that they were looking for people to work on hardware based off of Android Open Source OS, so AOSP (Android Open Source Project), it's pretty standard practice. I think right now if you're building a new device, you just start with this AOSP sort of OS. I think I sort of just switched to it because oh, there is nothing more fun in New York for me right now. Why not? Obviously zero experience with hardware or Android. Android is terrifying for anyone who builds for iOS. God forbid you never go there. It's going to the dark side. But yeah, so I ended up switching and that team was a lot of fun. It was sort of like this Alice in Wonderland, once you plunge, you know, into the rabbit's hole, you kinda go, this is really fun.

I sort of switched to that team. For the first half of the year, I think I committed maybe two diffs in the entire time. Because it was all prototyping. It was all okay, first we need to begin with, we needed to figure out what hardware do we even need to source? What kind of processors, what kind of, whatever. You have a bunch of mobile engineers sourcing hardware. That's fun. In the meantime, we also needed to understand how this hardware would interact with the existing hardware ecosystem.

All your phones, all your whatever. So me being sort of aware of iPhones and iOS sort of ecosystem and loving reverse engineering stuff. I started looking into how Apple builds their messaging stack and sort of how they communicate. So there is this protocol that allows, you know, whenever you get into a car that doesn't have Apple CarPlay or Google Car, you end up connecting your phone and you see your messages or your calls in this really old school dashboard. So there is a protocol that allows you to do that via Bluetooth. And obviously Apple had to build their own extensions of this protocol that's not really public. And so it was a fun little project where I got a Raspberry Pi off of somewhere and I started installing software on it to pretend that it's a car and pair it with my phone. And eventually I started tracing the packets. Some information is publicly available on the internet, some information you just need to sort of reverse engineer.

The reason why I didn't commit any of this code is because it's trash code and you don't need it in the repository and it was just done basically to inform. What's the upper bound experience that you can get using this protocol? Right. So what can we hope to achieve once we productionalize this?

See, and this ended up being a pretty common theme, I think in my career from there on, is yeah, it's sort of what is this upper bound experience unbounded by any sort of constraints. And then yeah, how can we productionalize it?

12:08 – 2 diffs in 6 months
Ryan 00:12:08:

Yeah. I'm curious 'cause you said two diffs in six months, and it sounds like there's a lot of risk and you are doing a lot of things that may not be easy to measure or prove the impact. I think a lot of people would be scared of switching teams, especially to a risky area like that. They worry their PSC (Meta’s performance review system) would look bad or something. What was your performance review like in that?

Sash 00:12:31:

Yeah, I think that's, there was, it was sort of in the job title where people who were hired on that team this early on, it was sort of implied that, you know, they get reviewed based on de-risking a lot of directions and not necessarily landing code.

We also, again, it's the team that was sort of seeded with a bunch of senior people and so there was mutual understanding that it's gonna be taken care of. I think that this is the way big tech sort of creates incentives for people to come in into those risky projects where you're not granted a promo, but you're at least protected from the downside, right?

Right. Because you want people who are interested in taking risks to feel safe. And this is a lot of changes that happened in the PSC cycles of a year where it, first it was sort of optimized for half a year because you kinda want to balance feedback that you get often. But also you don't want to make sure that, you want to make sure that people sort of feel safe taking on the riskier bets that maybe last, you know, maybe multiple halves.

And so it's a delicate dance. I understand that everyone hates this process, but I don't think there is a good process per se that can be good for everyone.

Ryan 00:13:38:

I'm kind of curious 'cause you were mostly in software engineering initially what's the biggest difference you see between hardware teams and software teams?

Sash 00:13:49:

The timelines for sure. It's this fun sort of concept when, you know, back in the day, if you remember when software would be still shipped on CDs and in boxes, so you literally have to put some bytes on the CD and seal it and send it to people, right? And so with hardware, it is still the case that at some point when you want to release your Gen One device, something has to go to the factory to flash it onto the device, right?

And so this is why the deadlines in the hardware projects are so much more ruthless. You cannot push them by one month, everything falls apart. And so it feels this is probably one of the key aspects. And then, yeah, you can have zero day updates when you know this annoying thing when you just bought a new device, you plug it in and it's oh, sorry, I will take 20 hours to update now.

So you can have that, it's not a great experience, but you can have it. But something has to go into the box. And so this is the key difference, especially in the company Meta where you have this continuous software cycle that you don't even think about. You know, you push something to www and it's instantly, you know, within three hours it's available to billions of people or iOS within a week.

All this stuff, hardware makes you think in very different terms. And it's pretty chill at the beginning, but then towards the end there is a crunch time when you have to get it done by a certain date, and that's quite different.

15:03 – Joining the Instagram blockchain team
Ryan 00:15:03:

So you had the hardware teams, and it sounds like that was a lot of fun. And then eventually you went to a series of teams that I'm really interested in because they were cutting edge prototypes on products that we know that launched. So I want to hear the stories behind that. What made you shift from hardware back into these software teams specifically focused on these rapid prototypes.

Sash 00:15:26:

So the time has come for me to try to live outside of the US again for a bit. And again, Meta has this wonderful, sort of flexibility of as long as there is a business need, you know, in engineering, in another office, you can just move and sort of work from there. And so I really wanted to try to live in London for a bit.

And I was trying really hard to stay on the same team, the CTRL labs team, because it was just so much fun and people were wonderful and technology was so cool. But it's hardware, it's, you know, especially having people living abroad means that you have all sorts of potentially regulations with unreleased technology, all sorts of stuff that you. I don't even know if that's the case here, but I imagine that there is a lot of complexity and so I realized that it's not gonna be an option. And so I needed to find a team in London that would be happy to have me. And as I learned, Instagram was just about to open the office in London. And so not just any Instagram, it was an Instagram blockchain team.

So for viewers at home, Instagram used to have a blockchain team and for the brief, but glorious period of time we were building all sorts of technologies. So people might remember that there was this whole cryptocurrency effort that Meta tried to take off the ground that eventually branched out into its own sort of separate company.

But then we had all the talent and technology built in house to sort of deal with blockchain and crypto and all that. And we basically thought about exploring those directions within Instagram, being creator first, creator forward, sort of product, other products, also other sort of apps later joined as well.

But yeah, basically this team was opening up in London and they were looking for people to join and sort of build out a bunch of stuff. So I moved to London, joined this team, and we shipped a sort of vanilla NFT type product within Instagram where you can upload your NFTs, they would have this beautiful shimmering effect and all that stuff.

Eventually, you were able to create NFTs from Instagram, just looking back at it now, wow, that's, we used to have this group internally called Facebook does what, and it was this internal group where people posted screenshots of products they found inside a Facebook app. And it was food delivery, movie tickets, ordering, all sorts of things that people on Facebook are like, Facebook does what now?

And so this is to me, looking back, you know, it was such a fun, crazy moment. But yeah, so I helped to ship the NFT product, but the actual thing that I was working on that was really fun and interesting to me. So at some point, Adam Mosseri, CEO of Instagram gave this TED Talk that was talking about how the future of creators is decentralized.

And it was sort of building on this idea how, right now as a creator you are sort of bound to a certain platform to their, you know, sort of policies to their whatever, contractual obligations. But then if for some reason you fall out to grace with this platform, you're banned, all your livelihood. If you build some sort of follow-ship, it's all gone.

So Mosseri gave this talk where he was exploring this idea of oh, what if this notion of following your creator exists outside of any given platform and platforms are there just to recognize it. They can choose not to recognize it, but they can choose to recognize it. And so what exactly does it mean for Instagram? What exactly does it mean for creators, for followers? And so I was one of the people who was tasked to just understand, okay, we have this TED talk, what does it mean as a product? And so we found that basically we need to build a product that's, you know, in order for it to be successful, we wanted to be recognized by some other key players.

And so this is how I found myself being embedded deep into the partnership team and working with people from Google, Spotify, Shopify, Nike, all sorts of companies. I think that exercise was super interesting because not only was I sort of prototyping the tech side of the story of, okay, what does this exactly mean? How would Instagram, what is my experience of, I'm a creator, I'm onboarding onto Instagram, I'm a follower. I'm coming to Instagram, and there is a creator that I already follow on, I don't know, TikTok or elsewhere. How does it actually happen that I connect my wallet and then we see some sort of token in there; all sorts of open questions from a technology standpoint.

But even more interestingly, there were a lot of questions about the sort of business side of the story where you have Meta whose business is predicated on ads. You have, let's say, I don't know, Spotify, whose business is subscriptions. You have Shopify whose businesses, I guess they charge merchants for selling stuff.

And all sort of they're all different incentives that all those companies have. And so how do you create a product that they all are interested in considering their different business incentives? And that was just really, you know, as an engineer, you I think you get to think about it, either if you're on your own startup or if you're pretty senior. I was neither of those things and it was so fun to just go and sort of play with it and yeah, just meeting people from other companies, making a case for oh, this thing should exist. And it is a really fun exercise in seeing how you can convince people that a product should exist pretty much from scratch in the vacuum. You know, there is nothing. And then you're oh yeah, yeah, it makes sense for you business wise. And you know, we got to various degrees of success with different companies and then crypto winter hit and we had to shut down the entire project. But while it lasted, I think that it sort of gave me a really fun insight into this side of the story where technology is important.

But it's so rare that companies sort of fall apart. Well, I don't know if it's rare, but I feel it's, more often than not, the company companies fall apart, not because of technology. And so there is this whole other aspect of building a product that I think as engineers, we don't often get involved in. But it's still a really fun problem space to think about.

21:37 – Joining Instagram Threads pre-launch
Ryan 00:21:37:

Okay. So then crypto winter happened. You switched off that team and you started working on a very experimental, interesting project, Instagram Threads. Yeah. Prior to its launch. I'm curious, how did you get recruited to that team? 'cause that's a really, you know, cool, interesting zero to one project.

Sash 00:21:54:

It was sort of, the writing was on the wall that the whole crypto efforts, blockchain efforts will be no more. And so sort of foreseeing that I ended up helping people to ship some pretty traditional Instagram products for a bit still from London, and then a couple of people reached out over Christmas break as far as I remember, and they asked if I was familiar with sort of ActivityPub, this protocol behind Mastodon. So decentralized social networking. I'm not up to this day. I'm not a hundred percent sure why. I think that you sort of end up building some sort of credibility for prototyping, for posting, you know, internally all things that you do, yada, yada.

And so they reached out, they asked about it and I was oh yeah, I'm kind of familiar with that. I wasn't really big on Mastodon at any point, but I was aware that it's happening. I was sort of new enough about it. And then it was Christmas break when I didn't really have anything to do and I was in London and I spun off an internal instance of Instagram server and I started looking into, okay, if I stand up a Mastodon instance next to it, within the internal sort of network. On Mastodon, you can search and it finds users from any other decentralized Mastodon instance. So they have this protocol that they talk to each other and they sort of resolve all those names. And so I spun off both of those instances and I wrote a really simple and really horrible code that was basically allowing internally to resolve Instagram users from Mastodon, that was the first taste of cool, we can actually get this stuff. We can get them talking to each other. And you know, it's not technically that hard, let's be honest. But what I found is that this is probably another one of those lessons where it's not about technical complexity.

Oftentimes it's about having a concrete thing that you can point at, you can give people to play with it, you know, and they can actually see it with their own eyes. And it creates so much momentum in the project. Say, especially early on when it's yeah, you can have 500 decks or you can have one prototype that works and people can play with and it just creates excitement and all of a sudden people jump on the project and whatever.

So that was the very first thing. Again, it didn't really de-risk or move us anywhere because it was obvious that it's possible, but it just showed maybe the direction that oh, I'm interested in the project and I showed it to the folks who reached out. The very next step would be, okay, cool. Now we need a mobile app. And I knew the Instagram codebase at that point relatively well because I worked on the Instagram blockchain team for a bit. And so what I did, I started stripping down the images from the Instagram app and just blowing up the actual caption text to be pretty massive and just hitting the same, you know, internal Instagram server.

And so it would just show my feed without images and just with text. And I was oh, cool, that kind of you can squint and see it. And then I worked with this super talented guy, senior engineer, Peter Cottle, from Instagram and yeah, the way he sort of knows backend I feel is sort of back of his hand.

And so we had so much fun when he was just building out the backend stuff because he is way, way better. Obviously, then I am. And I was just sort of, cool. Now we'll start querying this new feed source that you created that's gonna have only this special text post type and whatever.

And so we started sort of chiseling out the mobile experience from the Instagram app and from the backend. So we sort of started with this, here's Instagram the way it exists today. Let's start seeing how it can actually turn into Threads. Yeah. And so for a while we had this as a secret sort of feature gated to employees only inside of Instagram.

And it was, yeah, I think it was a pretty closed off project at the beginning. So it was gated just to the team. We had this special composer where you can type text because in Instagram you cannot share a post without an image. So we needed a way to share a post without an image and the backend should survive, you know, this post that doesn't have an image and not freak out and crash everywhere. So that's where Peter really helped early on quite a bit. And yeah, we sort of started chiseling this out and then I ended up being this iOS engineer based in London when the rest of the team started building up in New York and SF. And yeah, it was sort of a fun journey from there. From there on I was, so London is what, I don't know, eight hours ahead or five hours, some number of hours ahead of New York, let's say. And so I'm terrible at time zones. But you wake up in London time and it's super early and because our builds were sort of separate builds from the Instagram app, they would constantly be broken because they were not part of any continuous integration yet.

And so I would wake up. All the builds are broken. I need to figure out why it is that someone would land some code, doesn't include our code path, whatever. So first three, four hours, you just fix all the stuff, you get it to work, and then the team in the US wakes up a bit later and they can start working with it and then you build out a bunch of features as well.

And so yeah, it was a really fun process. We started hiring a bunch of people from across the company. It was a really fun sort of project where it was just around the time when Musk was acquiring Twitter, and so there was a recognition that there is this sort of window of opportunity if there are some sort of chaotic moments in the Twitter. Then, you know, Meta can come up with its own product. And so we needed to build it in a way that at some point was ready to release, and then we sort of built on it so that, you know, you have some usable version of it and you just make sure that that doesn't fall apart.

Yeah. And so I think it got built in five or six months, if I remember right. From this first prototype to releasing it to the public. And it was, yeah, it was one of those projects where it is, it was a top down incentive sort of initiative from the leadership to get it working. And because of all the red tape there, magically people would appear and they would be, let me solve this for you. And you're yes, please. And you just get to work on the stuff that you care about. It was so much fun, and also it attracted a lot of really talented people from all sorts of design products, all sorts of stuff. And yeah, it was just really, really good collaboration. People that worked on that initial team, they were really stellar.

And then, yeah, there would be surges of oh, we need to figure out integrity or privacy or whatever performance. You would just sort of bring some people on board that would help you to figure out some stuff. It was a tremendous effort. I think that became sort of a poster child of a team at Meta to show how little you can, you know, how little you need to ship a great product. Granted, we built it on Instagram, so we had super high level primitives, scalable sort of, you know, battle tested and all that. So, but yeah, it was something that's Meta sort of, I think tried to evangelize later on. So this is how we can build products in this new environment.

28:53 – Working with an exceptional engineer (Peter)
Ryan 00:28:53:

You mentioned working with Peter super senior engineer at Instagram. What is the thing that made him so great, when you worked with him?

Sash 00:29:03:

I think that he worked on it for so long that he was familiar with all the corners of the code, and he sort of knew, well, the consequence. What's the fastest way to get posts working without an image, right? How to create a new feed, how to, all those things. He just sort of had answers to all of that. And so it ended up being this sort of conversation between us two. Early on and with more people later where it's oh cool, now we need to figure out this piece. And we just have this conversation with code where we quickly land it, I can test against his backend and it just works.

I mentioned it before, this is something that's super, super helpful when you are, when you want to move fast, whether it's prototyping or shipping products, familiarity with code gets you a long way. And so Meta is great because it has these incredibly high level primitives. So even when I would go and work in the backend, WWW or or Instagram or whatever, the size of the primitives is so massive that it's so easy for you to be efficient. I need to create a new entity and I don't even need to know how privacy works. It just gets the right defaults and it sort of ensures that nothing bad happens and then, you know, then you, there is a way to customize it. They just know stuff so well. They know their codebase so well.

At this point, I guess with all the AI advancements and all that, you can see a future where you just have a conversation with your copilot type of AI, and it sort of does it for you. But that was roughly before all of this AI craze happened and sort of became a norm. And so yeah. Peter is a copilot, an incredible copilot.

Ryan 00:30:46:

Okay. So he knows the company so well that it's almost as if you prompt him.

Sash 00:30:51:

But he doesn't hallucinate and that's important!

Ryan 00:30:54:

I think one thing that's really interesting to me and the story, how you got this opportunity, this is a really cool team that you joined very, kind of cutting edge is, it sounds you were already known as someone that had these visible prototypes.

Sash 00:31:11:

Mm-hmm.

Ryan 00:31:11:

So they came to you, but then not only that, you just took some initiative to just instantly start it. It doesn't sound like they asked you to prototype. You just replied with, here's it, working with Mastodon, and also here's another idea of a, you know, bare bones, iOS app that's kind of showing the vision.

Sash 00:31:32:

Yeah.

Ryan 00:31:32:

So I feel that's a pretty interesting takeaway and I, it sounds like your prototypes too, they must not live in a vacuum. It's not you who built it. It's kind of your curiosity. It sounds like you build it and you share it, and a lot of people get excited about it. And you're already known as a prototyping person. Would you say that's true?

Sash 00:31:51:

Yeah, I think, it's hard for me to know for a fact the reputation that I had at the time, but maybe it was around the same time. Early GPT sort of was coming out. So I was building a lot of those things and sort of sharing them on workplace.

When you build something that uses internal technology, you cannot really post on Twitter. Right? And so you have to sort of do that internally, but in exchange it creates this perception. Even if you don't get too high of an engagement on your internal posts, people see them popping up and eventually they sort of build this mental model of oh yeah, if you want someone for quick and dirty, whatever, prototyping, that's the person to reach out. And then, yeah, I think responding with prototypes instead of oh yeah, let me put this on my, you know, to-do list. It's just a way that shows the attitude. Early on in all those projects, you want people who are self-directed. I think that's what I would be looking for at least.

Yeah. And in the corporate world there is so much alignment and, you know, meetings and all that, that I think it always stands out when you have someone taking, you know, initiative and sort of moving on in the ambiguity.

33:02 – Working on AI prototyping teams
Ryan 00:32:59:

And then after Threads, you mentioned that you worked on a string of AI related prototypes and transitioned away from that and started working on, you know, Meta AI and stuff like that. Is there a favorite prototype or maybe a story in there that you think would be worth talking about?

Sash 00:33:16:

Yeah, I think early on there was one really fun, pro fun, it's a big word for it, but I built this prototype that took all our public FAQ about account safety and sort of all sort of things related to Facebook accounts that you can find on facebook.com/help or whatever.

And so we took all of this and sort of ragged over it. So did retrieval, augmented generation over this information. And so you can, you don't have to search for the specific answer. You can actually just have a conversation with this AI as GPT-3 time. And so you can actually have a conversation with anyone with hallucination like crazy. But you can also see how it's getting there, where you can ground it in some sort of concrete data. And I posted it internally. And that was the only time when I got a number of reach outs from people from all over the company that I'd never seen before. It was probably below a hundred, but about 50.

And it was people from all over the place that recognized it. All of a sudden support is sort of solved. Not really solved, but you know, you can see how it's moving into a direction where you can have customer support being done way more efficiently and, and fast forward you can see so many companies in the public right now building those kinds of products.

And again, it's not that I was first or anything like that, but it's just, again, it's to the point where when you are in your corporate sort of environment, you are grounded in your internal technology so much. So much so that you are not even aware of what's happening in the industry and showing, you know, pulling in those pieces of industry and grounding them in your internal data, technology tools, whatever.

It really helps to bring awareness within your organization, within your company too. And you'll be surprised or maybe not even surprised how often people, you know, people have their lives and they don't care to read Twitter every day. And so they don't know what's that, oh, here's this latest, coolest thing. You can easily just bring in those pieces of what's possible right now into your corporate environment and just keep people up to date.

Ryan 00:35:20:

You know, when people talk about visibility, you know, it's oh, write up that says you moved this much, which is good too. But it sounds to me like a good prototype, about the right idea. It connects with people in a way that writing can't, which is someone can click into it. Yeah. Someone can really see it's, it's such a high throughput thing, rather than just text. You got the whole thing in front of you. It sounds like a really good tool for driving the imagination of the future. Direction alignment, it sounds on, Hey, this is a good idea. A hundred percent. We should go with it.

Sash 00:35:56:

Yeah. Yeah. I think it goes back to the fidelity, right? So you have, you can write text and then it relies on both of us being able to reconstruct what I meant in your head and making sure that we actually align on what I meant.

You build the same mental model, you can draw an image and then it's a bit easier, a video, an even easier prototype is probably the highest fidelity when there is. The less ambiguity you leave to, you know, for someone to interpret the better. And then you can actually ground your conversation in oh cool. I actually want this specific interaction to be a bit better or different or whatever. And you probably saw that yourself so many times when you are in the meeting and 20 minutes in and you realize that you were talking about completely different products. You thought you’re building together with this partner or whatever.

So it definitely helps a lot to speed up those ambiguous days of the project.

Ryan 00:36:47:

Okay. Well, coming to the end, I think there's so many interesting reflections we can have over this career. 'cause I think your career is so unique in that. I remember you had written something or said something you got promoted despite your best efforts not to, and it was clearly not your intent to focus on career growth, more about focusing on the things you're building and other circumstances.

37:15 – Reflecting on team switching’s impact on career growth
Ryan 00:37:15:

So I'm kind of curious, when it comes to career growth, looking back, if I recall correctly, you were hired as an IC4 (Mid-level engineer at Meta), then were eventually promoted to IC6(Staff engineer at Meta). Even though it was not something you really even thought too much about. What are your thoughts on, you know, your career growth and also in switching teams as you go about it?

Sash 00:37:34:

There was one friend who was on that first newsfeed team that I joined. Who's been there before I joined and who stayed there throughout my entire time at Meta, he just left maybe a year ago. And so it's definitely way, way easier to level when you are in the same space. You build connections, you build goodwill, you build expertise, all those things that help to propel your career upwards.

I think that, yeah, I just always found it a bit boring. I think coming from startups, coming from outside of the US, my mentality was just so not about that, that I, I just, it took me a while to conceptualize what PSC is and what is it for, because you get a startup, you get continuous feedback every day.

Right. But here it was sort of a bit different. I don't view this as necessarily an advice that you can scale and give to other people that oh, do this thing and it's gonna be fine. No, it really depends on what you're optimizing for and what kind of career and life you want to have. I do find that for myself, breadth is just a way to set yourself up for those.

You know, connections that you build in the future. So it's gonna, you, you set yourself up with all the connections, all the technology, all the people, and eventually some of them come through and, you know, maybe you will take a few wrong turns. But as long as, for me personally, as long as I enjoyed the projects that I was working on and this is what I was optimizing for the most, I sort of wanted to work on projects that I feel passionate about.

I end up working a lot. I used to work long hours. And to do that sustainably, I needed to enjoy what I'm doing. And for me, this joy was coming definitely from fun. More than leveling and career growth.

Ryan 00:39:19:

I mean, it sounds like the breadth paid off as well. There were many of the opportunities that you got because you were kind of shooting shots everywhere and people had seen that. So you cast a wide net?

Sash 00:39:30:

Yeah, it definitely ends up building some sort of persona for better and for worse. I know that I have a few really good friends on infra teams and we have these ongoing jokes about the number of SEVs that I cause them and all the grief that I cause them.

But we're still friends and whenever they need to know how something is done in this completely different corner of the app or in a different app, they come and ask. Right. And it's helpful. Well, not anymore, but they used to.

Ryan 00:39:54:

You know, when it comes to career advice, it's anecdotal and we can't really tell what would've happened if you did something differently. We just kinda interpret the dots looking back. But one thing I was just thinking that might be interesting is that bootcamp class that you joined, for some reason everyone stayed at the company. The entire time, and they're completely different people. And it's also a low sample size, but I'm curious, I don't know how much tabs you kept on, you know, what they're doing and how, but when you compare your career to theirs in terms of what they worked on and how theirs went, you know, do you notice any differences?

Sash 00:40:31:

Yeah. Yeah. I know that a couple started as ICs became managers, worked in roughly the same space, definitely within the same apps. The other person moved to Reality Labs and I think stayed there for the entire time, I think still in IC. Yeah. I think they all are doing well, but they definitely are the kind of people who prefer growing vertically rather than just spreading themselves all over the place.

So when I was leaving Meta. I felt that I had to find someone to take over my spot on the team. My last team was almost exclusively built around prototyping within that AI, and it was hard, and I'm not saying it to pat myself on the back, but I think that this is something that large corporate, you know, environments they sort of disincentivize against.

You know, they sort of don't make you want to join. To prototype, to explore. And I think that this is how you build resilience in bigger companies where the majority of people focus on your impact and, you know, all the all the right stuff. But then you need someone who is sort of oh, I'm just gonna take a risk and see how that plays out for no, you know, not expecting anything particular to happen.

Ryan 00:41:49:

It also kind of reminds me of the discussion of metrics versus, I guess vibes, for lack of a better word, is that there's a lot of merit to that hyper optimized way of thinking, but it also is the trap of, you know, local maximums and you want, if you wanna monotonically increasing right number. It's not gonna, if you're not willing to take them down, you might not unlock some, you know, change.

Sash 00:42:13:

A hundred percent. Yeah. I think that there is definitely something to be said about Goodhart's law. That's the second you choose something, you elect this number to be a metric. It ends up being a bad thing because people end up sort of gaming it and so it stops being a good metric. Right. And so, and that is even before you sort of think about the fact that many things are not even measurable, right. And so you have to rely on the taste. You have to rely on whatever else, to build, you know, good products to make sure that yeah, you're not getting trapped in a local maxima.

It is hard. It is hard, especially, it's hard to make a framework out of it. I feel for and, and large companies need frameworks because nothing else scales.

Ryan 00:42:53:

You did 10 teams in nine years. I'm curious, looking back on all of them, is there any of them that you, the team switch, you kind of regretted, or maybe it's a team switch where you thought, oh, actually that one looking back, maybe not ideal.

Sash 00:43:09:

I think that's, there were some that didn't pay off as much as I was hoping to. I think in reality you sort of learn from all of them. You learn something, so, so that's, yeah, you going forward, you at least try to avoid those sorts of lessons again. And in most cases, again, you're sort of if you're a decent person, you work and you try your best, you end up just building at least good relationships with people and going forward.

Those people can, you know, bring you on to the next project or you bring them, or, you know, you just sort of end up building a massive, massive network. This is something that I've really only truly appreciated. Once I left Meta, how many people reached out and asked if they could introduce me to people asked, what am I doing?

A bunch of people reached out and asked if I can hire them into this thing that I'm doing, which I don't know what it is yet. It is definitely a really, really fun adventure and you get to meet so many cool people that it's just hard to overestimate. Yeah.

Ryan 00:44:06:

Yeah. I, I had never worked directly with you, but I knew of you so clearly what you had done cast a very wide net while.

Sash 00:44:13:

Yeah, it's wild to me. When people reach out, they used to reach out on work chat and they would be oh, hey, we talked, you know, in 2020. My memory is also horrible. And so I just, I rarely remember things that happened more than a year ago. I always feel terrible, but I also feel so, you know, humbled by oh, come my God, people know this is so cool. It's really fun.

44:35 – Why leave Meta
Ryan 00:44:35:

Now you've left Meta. What was the rationale for leaving Meta rather than doing another team switch?

Sash 00:44:40:

Yeah, I think that's, well it's been a really long time and I started in startups. And I felt I wanted to go back to this space where, you know, the pace at which I prefer to move is the natural pace.

So, you know, you end up taking on far more risk financially makes no sense. It practically makes no sense. But right now I have few ideas that I'm exploring, you know, and I'm sort of passionate about. And at this point, there is no meeting, there is no partner team that I can blame on the failure.

You're so close to the wire that you just try it out and you see if it works. And then again, it’s a big tech, you know, you can always come back and be hired into the next big tech company and it's all gonna be fine, hopefully. But it is definitely a fun experiment to see how much, what is your actual worth? You know, what are your ideas and all those things that you thought you can deliver on. Can you actually do that? So I think it's gonna be an interesting exercise. We'll see.

Ryan 00:45:40:

So it sounds like you left because you wanted to go even deeper into prototyping and doing your own thing and being unbounded and it's a two-way door, not a one-way door. You can always go back.

Sash 00:45:53:

Yeah, that's, that's the way it's, it's a really good framework that someone mentioned before that you need to think really carefully when you answer one way door, when it's a two-way door, or at least it looks one you need to be concerned and sort of careful but also take a risk while you can. Yeah. And I'm sort of still in the place in my life where I'm lucky enough to to be able to take some risks.

46:15 – Advice for younger self
Ryan 00:46:15:

And then last thing, is it looking back on your career, and if you were to talk to yourself when you had just entered the industry and you could give yourself some advice, what would that thing be that you tell yourself?

Sash 00:46:26:

Yeah, I think that's one thing that one of my managers told me, and I think it's coming from one of the consultancy frameworks where, you know, at first I honestly thought that I need to fix all my shortcomings, fix all the things that I'm softer at, and my manager told me. You wanna make sure that they don't get in your way, but you really want to focus on your strengths.

And so I think that that was a relatively eye-opening as obvious as it is, it was a relatively eye-opening sort of advice. You want to position yourself where you can showcase your strength and when you, where your weaknesses are not getting in your way. I think that's whatever that means in your case, this is probably how you're gonna be the most successful long term.

Ryan 00:47:12:

Yeah. That reminds me of something that a VP had written, early Facebook, and he said something one of the big learnings was that the value and where the real impact comes from is not from taking something that's poor and bringing it to passable, but taking something that's great and making it exactly. Excellent. A hundred percent. So thanks for taking the time. I was really, you know, looking forward to it and is there anything you want to say to the audience?

Sash 00:47:41:

No, I think you can find me on Twitter. I'll probably be sharing more about stuff that I'm building on there. And yeah, thanks so much for inviting and having over. It's been a lot of fun to chat and reflect on all this stuff.