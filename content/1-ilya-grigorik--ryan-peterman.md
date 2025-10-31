---
guest_name: Ilya Grigorik
biggest_role: Distinguished Engineer at Shopify
current_company: Shopify 
company_size: 8000
YOE-starting: 2002
episode_date: 24/10/2025
episode_duration: 50
episode_title: Shopify Distinguished Eng (L10) on Principal+ Engineering, Career Story, Regrets | Ilya Grigorik
episode_description: Ilya Grigorik grew to a Distinguished Engineer (VP-level role) at Shopify and I asked him what it took to get there. We covered his full career including the behind the scenes of his startup getting acquired by Google, his growth to Director at Google, and what it means to operate like a Distinguished engineer.
guest_background: Founded PostRank (acquired by Google), Waterloo CS grad
topics:  [Thoughts on Waterloo, Starting his own company, Google acquisition story, Joining Google, Switching back to IC, Principal+ Engineering at Shopify, Career regrets, Top career-impacting book, Advice for younger self]
---
Transcript
### Thoughts on Waterloo
Ryan:

[00:00:46] You mentioned you went to Waterloo and I, I gotta ask the smartest interns that I ever worked with, they came from MIT, Caltech, and Tsinghua University in China, but the best interns I ever worked with all came from Waterloo. And so I, I’m curious, what is it that makes these Waterloo interns so strong?

Ilya:

[00:01:10] For me, personally, the most important thing that, uh, Waterloo got right and better than most, and I know that more schools have adopted this pattern, but it’s still not well understood, is their co-op program.

[00:01:22] So what Waterloo did really well is they realized that. Yes, there is the academic portion of learning how to engineer and like what software design is all about, but then there’s the hands-on and applied part and instead of modeling it as, Hey, you’re gonna study for three years and then you have an optional kind of intermission style co-op, which is what, what most university operate on, right?

[00:01:49] That you could take a year off or something like that to go and work in industry. Uh, Waterloo said, you know what, we’re gonna just do a rotation where every semester you study, you work, you study, you work, you study, you work. You know what that means? You don’t have a break in between. You’re just constantly iterating through this loop.

[00:02:06] But what it gives you is, um, at least six, six shots on goal for trying things, right? And this actually has very positive effects on many dimensions. So first of all, um. It removes the stigma of trying things, right? Because, uh, many of us, like we don’t know what, what, what’s gonna stick with us kind. I’m coming back to my earlier point about consulting versus something else, or something else.

[00:02:34] I had so many of my peers going through university and what, where we all started with some preconceived notion of what we wanted to do. It’s like, oh, I really want to go to Wall Street and work there, and they, they try one of the co-op terms there and they’re like, no, I actually like that this. For whatever reason you look, I don’t like the city or I don’t like the industry.

[00:02:52] I didn’t like the people. It like, it just didn’t click for whatever reason. Right. Same thing for like medicine or others or consulting. Um, and that’s really important to discover early. And the really nice thing is it’s a concentrated, it’s like it’s a three month sprint. You get to try, right? And you have permission to try five more things, at least without the stigma of looking at your resume saying, Hey, like you, you went to a role for three months.

[00:03:17] You jumped, you went to a role for three months. You like, are you really like committed? Are you like, do I wanna hire you? It’s like, no, that’s my call. Right? Like, that’s, that’s the whole point. So you could, first of all try a bunch of things and get a kind of a good range of experiences under your belt, um, but also see the kind of, the gamut of like.

[00:03:35] Here’s how a large company operates. Here’s a smaller company, here’s a medium, but like, which, which one resonates with me more? Right? So it’s industry, it’s uh, the type of work that you do. It’s the type of an environment that you’re in, and I think that is really helpful. On top of that, you actually get exposure to like engineer things, not learn the hypothetical and academic of like, I know how a big o notation.

[00:04:03] Expresses this particular algorithm. It’s like I actually had to build a thing, right? Like, and turns out this didn’t work or that particular solution worked, or we had to solve it under these constraints, and the whole big old thing was an nonissue because I was like, sorting 10 items in an array. Who cares?

[00:04:18] Right? It’s like pragmatic engineering. So. I think that is key. Um, that is still the superpower of Waterloo and I wish more universities, like it’s an open secret and I wish more people would copy it because it’s such a lever for success for people that go through that program.

### Starting his own company
Ryan:

[00:04:36] After you went through all of those iterations and all the co-op loops, understand that you started your own company, um, which became post rank.

[00:04:47] Was then acquired by Google. And I’m curious the story behind you choosing to found a company Right after graduating from Waterloo.

Ilya:

[00:04:56] And as most students, um, I didn’t not know what to do. Um, I wasn’t ready to, to commit. Um, so my escape, uh, which is, which was a, a well drawn track for many, is I’ll go to grad school.

[00:05:10] So I, I applied and then got into University of Toronto actually. And during that summer, in between, um, I had a couple of project ideas that I wanted to get off the ground. So I, I had a particular itch that I wanted to scratch, and the itch was, if you think back to, uh, how Google was founded, the key insight, if you simplify it and boil it down, that like Larry and Serge had back in 1997 is.

[00:05:33] Hey, um, we could treat the link graph of the internet effectively as a feedback loop on what is good content. So if you and I create pages and we link to each other, that’s a mutual signal of both directions that there’s something there, right? So disconnected pages are not worth much, but in effect, it’s kind of a social currency.

[00:05:51] Links are a social currency right now, fast forward to 20 10, 20 11, when I’m sitting there, the web two revolution. Has already happened or like well underway. You now all of a sudden have dynamic content on the web. Not static links. Not static webpages, but we have comments on blogs, right? Blogs became a thing, comments became a common thing.

[00:06:13] So my observation was, Hey, if a conversation is happening on Reddit about an interview that Ryan has recorded, like that means there’s something there. I don’t, I can’t qualitatively say whether it’s good or bad, I just know that people are talking about it and that a signal. So what if. You built a system that went out and aggregated all of these interactions.

[00:06:32] Then built a better version of PageRank effectively, right. Links becomes one input, but you know, thumbs up, a number of conversations, a number of likes, and all of these things become additional inputs. And that was post, post rank, right? It’s, it’s kind of embedded in the name. It’s a, it’s a, was an algorithm for ranking posts based on social engage.

[00:06:51] Kind of a child of the web two oh era. Still remember the day. It was like July 8th when I released it. And then I did sleep for three days because the servers were melting down, not strictly because it was like such huge demand, although there was, it was also because my code was terrible. So it was kinda like brute force and just throw more servers at the problem and then eventually, uh, you know, optimize it out over the next couple of weeks to, to get it back to a measurable set.

[00:07:17] So that becomes kind of this nucleus of, hey, there’s a. There’s a feature there, right? And it got, um, it got good publicity, uh, which then turned into conversation, Hey, is there a product here? So I remember those juncture points, uh, somewhere late in May where kinda in the middle of all these conversations with investors, um, kind unanticipated fork in the path, right?

[00:07:40] And I’m thinking, what, what do I do? Like I’m uncertain. Are we gonna be able to close around? Can I do this? Because in a couple of weeks I’m supposed to start my grad, my grad work. And I’m looking at that syllabus. I’m like, what are the courses I’m most interested in? And I go through the list and it was like the, the ones that immediately stood out to me about like entrepreneurship and like how to do a company.

[00:08:00] I’m like, wait a second. So I could go and learn about the stuff academically and read books or I can, like, I’m literally having the conversations right now with investors like I, or I could just like. Going, like, I, I can read those books on my own time and I could, couldn’t, I can go and try it. Which, uh, led me to reaching out to my advisor and basically asking, Hey, yeah, can I take a, a year time out?

[00:08:22] You know, I was planning to do this this year, but how about I start next year? And he handed hard and said, okay, I understand. And, you know, come back to me in six months. Um, to close that story, we did end up closing the round and that became, post the post rank the company. And, uh, I never did get to finish my, uh, so-called graduate degree.

### Google acquisition story
Ryan:

[00:08:41] So in the process of building this company, I know eventually it was acquired by Google, but I’m really curious because I feel like a lot of acquisition conversations are behind the scenes. Hush, hush. Um, what does that kind of conversation look like? Like when they reach out for an acquisition and maybe you can tell that story.

Ilya:

[00:09:03] It’s a lot less stressful than you make it sound to be. I remember we were actually. Well, we were building the product that I was describing and, uh, we were presenting at one of the conferences in the Bay Area and, you know, we got off stage and, uh, Phil Muy, who was one who was the, uh, kind of lead PM on Google Analytics kind walked up to us and like, Hey, this, this is cool.

[00:09:24] Uh, do you wanna have a chat? And I remember taking a train from San Francisco to Mountain Mul later that day, sitting in the conference room and him basically interrogating us about what is it that you build? And then, um, ending the conversation with, Hey, maybe we should do something together. It’s like, okay, well, tell me more.

[00:09:44] Right? Um, that, that’s a, that’s a blank check for the follow up conversation. Um, so it, it was, it was very friendly. There’s, there’s nothing, uh, kind of, uh, more to it than that. And then, uh, what we learned, uh, after is this is right. In the time span when Google and Facebook were, uh, like at war in terms of drawing the battle lines for social, uh, this is when Google woke up to the fact that Facebook is on a runaway trajectory and, um, all hands on deck.

[00:10:16] Google needed, this is when Google starts working on Google Plus, uh, which of course has since been sunset. Uh, but it became this catalyze catalyzer with the Google for. Hey, we, we need an answer. And they were looking for all the help that they could get and all the experience that they could acquire to speed run this whole thing.

[00:10:38] Um, and we became that catalyst for Google Analytics because what they saw in us is like, they, frankly, they did not care for the uh, and. PR product that we were building. What they cared about was, uh, the experience and some of the infrastructure that we we’ve accumulated that we could bring in to fast run and fast track this whole thing to say, Hey, if I’m using Google Analytics, I can get really good insights on how my social engagement is going, and I can figure out how Google Plus is helping me and all the rest.

[00:11:08] Um, so that became the kind of the, the mutual point of win-win situation, um, that led us, uh, joining forces with Google Analytics.

Ryan:

[00:11:18] In being brought in as an acquisition, how’d they determine leveling or compensation or any of that stuff?

Ilya:

[00:11:25] Google, as many other tech companies run the same process. It’s usually kind of accelerated batch model, right?

[00:11:31] Where you bring in the whole team and, and you kind of do a, a wholesale evaluation. But otherwise, um, everyone on our team went through the panel. Through the full panel, uh, myself included. Uh, so that, that was, that was the bar. And really the exercise for them was to vet the quality of the team and then to figure out where all the engineers stack up.

Ryan:

[00:11:54] I see. Okay. So it’s, it is just a normal interview process. What about in the case though, ‘cause you’re bringing in company and assets and stuff, is that just like a giant signing bonus or something, or. How’s that?

Ilya:

[00:12:07] It, it depends on the company that, that, you know, and then the deal of, of course. So there, there’s both polar to it exactly as you said, right?

[00:12:14] There’s the, like, there’s the ip, there’s the customers, uh, there’s the people and you can treat those as kind of distinct conversations, right? So as far as negotiations concerned, um, are you acquiring the product? What are you gonna do with the customers, right? Um, is there IP there? Are you gonna use the technology?

[00:12:32] Um, many, like, there’s the Acquihire acquisition where you’re effectively acquiring the team. You’re saying, cool thing you built, but that’s not the thing I need you to be building. Let’s just put that on the shelf and let’s just focus on like rebuilding the thing. Um, in our infrastructure, um, poster was closer to that.

[00:12:48] It was not a full kind of acquihire because they brought in and they, they used the ip, but for all intents and purposes, the thing that we built ourselves, we had to rebuild from scratch within the Google analytics. Because you’re just operating at a completely different order of magnitude. Right. And it was an amazing trial by fire, if anything, for our engineering team because we went from managing tens of thousands of analytics accounts.

[00:13:12] And granted, yes, we were crawling the web at a fairly large scale to operating in a service that was literally executing on half more than half the internet. So like to, to make a modification to a data pipeline. I remember the conversations fondly, uh, like sitting with our SRE team and they’re like, okay, well you’re gonna add this bit field right here.

[00:13:33] That’s gonna be this number of exabytes of data. I’m like, oh my gosh. Okay, let me think about this more carefully, right? Because before that was not even a, a conversation point for me and, and my team. So. Um, a lot of it was about the talent and bring, making, ensuring that they’re bringing in the right folks with the right experience and, um, that they’re capable of kind of hitting the ground running and, and working with, with the rest of the Google Analytics team.

### Joining Google
Ryan:

[00:14:05] So I want to get into your career at Google and it sounds like you were placed initially in Google Analytics. I’m curious what the leveling was and the role. Were you a manager? ‘cause you mentioned your, you brought your team with you.

Ilya:

[00:14:21] So I was founder and CTO of post rank and I joined as an engineering manager.

[00:14:25] Um, ‘cause effectively that’s what my, my role was, um, at Google and I was very invested in making sure that we build the right thing the right way. And kind of manifest the vision of why we started this damn company to begin with. Because I strongly believed in like, I want to help publishers understand that was still like me scratching my own itch of like, I’m gonna make Google Analytics solve my problem, damnit.

[00:14:54] Um, and um, I think we, we succeeded, um, at that, it took us about a year to effectively rebuild our stack and the team was on a good trajectory. And, and that’s where I. Uh, kind of took a step back and looked around for, Hey, what’s the next adventure? Um, I was in a really good direction, uh, within Google Analytics, and I, I remember, um, a conversation with one of our VPs at the time where, uh, you know, we were having one of these career sit downs and you’re like, look, um, you have all the things you need, you’re on track for director.

[00:15:27] You know, here are the things. That I, I could see, I could see you take on and all the rest, and I’m like, huh, that sounds all exciting. And like, and I’m very honored that like, you think I’m capable of doing this work, but at the same time, um, I couldn’t not let my curiosity get the better of me. Like Google is such an amazing technical playground that even though that first year was a pressure cooker of like, I need to get this thing shipped.

[00:15:53] I’m gonna work my, my butt off to get it working. I also was spending every free moment of time just like diving deep into various design documents and wikis. Uh, Google is an open culture, which is the thing that I loved about Google, and I could approach anyone at everyone about. Um, any piece of infrastructure, any product, and I leveraged that.

[00:16:16] Um, and I learned a lot because, you know, I remember building post rank and reading papers that were published about Big Table this and Hadoop that, and like trying to figure out how to replicate some of the magic that Google had. And then I’m reading the internal design documents and I’m like, oh my God, this is three generations ahead of this paper that I was reading.

[00:16:33] This is amazing. Like, like I, I wish the world knew about this, right? And then I would, half the time I would talk to the engineers. I’m like, how come. We never published a follow up on this thing. They’re like, we’re too busy. It’s not that it’s a trade secret. We’re literally too damn busy. Like, you know, if you find us the time.

[00:16:50] And I was like, huh. Well that’s interesting. Like wouldn’t it benefit the entire world, the entire, like internet if we did more of this? Um, which led me down some interesting conversations. And I discovered this group within Google, which was called Make the Web Fast, which was basically a sunk course project started by, uh, Sergey.

[00:17:10] Um, around, well, how can we make the internet fast? Uh, and it’s a very kind of self-referential, self-motivating thing. Um, that there’s very direct evidence that the faster the internet is, the faster users browse the web, browse the web, the more they use Google. So it’s a mutually beneficial relationship, right?

[00:17:30] So within that group, we had all kinds of fun products. We literally built radio towers trying to figure out how to build more effective, uh, cellular networks, uh, you know, dog trenches built, built towers. Uh, we worked on T-C-P-I-P and trying to figure out how to reduce congestion. Uh, we worked at optimizing proxies for, hey, turns out that most humans write terrible websites.

[00:17:50] Could we just like optimize it out on, kind of dynamically as a web server plugin to. Hold on a second. When we say make the intranet fast, what does that even mean? Like, we know it when we see it and when we feel it, but if you had to put a number on it, how do you express that? Right. So if you, if you walk the, the full dynamic range of those questions you like, it’s, it’s an just absolutely amazing laboratory of like, experiments to run.

[00:18:19] And I was really fascinated about about that. And I remember at that, at that point in time, I, I, I realized that I had. I had an opportunity to cash in some chips and I could say, look, um, I, I see a path towards kind of career growth as a director in this and that, and that would be a great achievement. On the other hand, I could take a step back.

[00:18:41] I could take this lateral step and go and work as an IC in this field, I’m actually not quite even sure how I’m gonna contribute. I just know that this is a really cool area that I’m passionate about and I’ll hopefully probably find something useful that I can do there. Um, but that would definitely take me off the career track.

[00:18:59] Right? I remember that conversation. It was like, well, you know, if, uh, I see bar at Google is actually really high, so if anything you’re gonna be down leveled, likely, um, and you’re gonna reset your track. I was like, okay. I think that’s a trade worth having because I get to control my time. I get to work with people I look up to, and I get to work in a particular, on a domain that I think is just absolutely fascinating.

[00:19:24] So I made that pivot and in retrospect it was an amazing right decision for me because, um, it allowed me to kind of flex my curiosity and technical muscle in a completely different direction.

Ryan:

[00:19:35] You turn down this more clear cut director path, which would be the clear cut growth path for career. Um, to optimize for other things, which was sounds like intrinsic motivation in the work.

[00:19:49] Curiosity, and also sounds like maybe you got some time back. Is that the math you were doing in your head and making that choice?

Ilya:

[00:19:58] Exactly. That it was, and it was a lot of uncertainty in that process. But, um, and this kind of a re a repeating arc, uh, through my career, uh, where as a manager, your time is managed by others.

[00:20:12] Like you are, you are in the service of others. And I wanted to, uh, shift gears and, and go into a mode where I have more self-direction and go pursue some like interesting research or, uh, projects that like where I can apply my own skillset in a unique way.

### Switching back to IC
Ryan:

[00:20:29] So later I saw that you switched back to management and your director.

[00:20:35] Uh, developer relations at Google. So what was the rationale then? Switching back, given what you just said?

Ilya:

[00:20:41] Yeah, so I’ve seesawed a number of times through IC to manager, and I think this is a path that is vastly underappreciated and is actually surprisingly common, uh, for a lot of like high performing, um, ics and like you’ll find in, in principle and then higher up pros.

[00:21:01] And the observation is, um. I think it was a tour of duty, uh, when I’m, when I’m doing management. Um, to be a really effective like principal plus engineer, you need to have very good dynamic range technically, right? And you can, you can work well at the low level of the stack. You can also zoom out and look at the business requirements currently deeply at understand what’s actually necessary.

[00:21:25] Where can you relax constraints, uh, where can, where you need to hold, uh, hold the line and all the rest, and. Once you get attached to certain projects, like some projects you can execute and you call it done, you’re like a great, I solved that problem, right? But many problems that are handed to you, they, they become, they come as nebulous statements that then evolve into, ha this is actually like a team’s worth of effort.

[00:21:49] Like, now that we’ve understood the shape of this problem, and, uh, what often happens is you, you kind of, you see this pattern of, um, some. Individual doing the trailblazing work path, finding where, where we need to climb, and then they find themselves, okay, now I need to recruit a team of people to help me actually build a thing.

[00:22:08] Like I know how to get to top of that hill with a machete, but now I need to build a highway. Right? And to build a highway, I need a team. Okay, well lemme go find a team. Before you know it, you’re kind of, you, you’re, you’re tl. Right, and you’re exercising yourself power to help direct people and all the rest.

[00:22:25] It’s not a far stretch to switch to a manager, right? Because it’s like, well now you’re doing performance management as well, plus a few other tricks. But oftentimes you’ll find kind of yourself, um, managing or being responsible for the direction of a broader team. Before you know it, like, I think it’s a natural transition to say, well, okay, fine, I’m gonna like manage this domain.

[00:22:44] I’m gonna manage this as a product team. I’m gonna manage this, uh, like the growth of the individuals and the rest. And that’s completely fine. That’s what happened to me with, uh, developer relations. Um, when you think back to the kinda the set of problems that I, that I shared with you, um, I ended up gravitating towards the question of how do you measure performance?

[00:23:02] And I found myself doing a lot of web standards work. I got engaged with W3C and ITF and, and trying to figure out, hey, what kind of metrics can we define in browsers such that we all have a common ground truth for how to measure performance? And that was great. Uh, did a lot of that and that was my kind of IC contributor role.

[00:23:20] Um, then you get those metrics into browser and then the problem becomes great. Uh, how do I get community or ecosystem adoption in this thing? Well, I need to go tell people and I need to convince them to adopt it, right? Uh, and integrate it well, now I need to go talk to all of the analytics vendors. Uh, let me go talk to all the open source projects, right?

[00:23:40] That problem does not scale with one human. Like you really need help of other humans. This is where the go to market and the kind of developer relations part came in, and I quickly realized that like. It would be really helpful to have a team of people that can focus on this thing. And this is the thing we deeply care about.

[00:23:54] We want to accelerate the adoption of these things. It’s kind of my, my as, um, model based on prior experience was, look, if we just leave this ecosystem be as it is in three to five years time, we will probably see the adoption that we want. But I’m not happy with three to five years. Like my question is, how can I compress it into one to two years?

[00:24:16] Ideally one year or less. Right? And for that to happen, we need to inject, we need to inject energy into the system. The energy is a team of people. Great, fine. Let me switch to the my manager role. I’m gonna go recruit people and I’m gonna like put my organizer hat on and we’re gonna go and execute this problem.

Ryan:

[00:24:33] So when you say tour of duty, it’s this starting as an ic, doing path finding, and then becoming a manager potentially is all. In service of a mission or a problem. Like you, you see some problem. Maybe em is the best way to solve that problem. Maybe IC is, but it’s really all about the problem.

Ilya:

[00:24:55] Exactly. And it’s kind of like your relationship and your commitment to the problem. Right? Because not every problem has to become your mission. Um, I am often engaged in projects where I am participating. I’m actively contributing. And then I say, look guys, you’re. You’re well on the way, like you have the right vector, go execute.

[00:25:11] You have everything you need, like you don’t need me here. And in fact, that’s my kind of measure of success as a, as a principal engineer oftentimes, right? I don’t, if the team is dependent on me. Pro that means that I’m probably doing something wrong because my job is to uplevel the team and make sure that they can deliver this thing self sufficiently.

[00:25:29] So if, you know the, uh, the Homer Simpson meme where he like disappears into the bushes? Yeah, right. Like, it’s like kinda like that. Like if I can pull that off successfully on a project and the team continues executing in the right direction with a good velocity, and like, that’s success for me.

[00:25:43] Oftentimes. Now, occasionally I stumble into a problem where I’m like, either I’m like, just. It’s in my bones and I feel like I need to be, like, I want to own that problem and see it to this logical conclusion. Um, or I have some unique position or leverage in it where like, yes, I’m the right person to take on the broader responsibility and kind of execution of the team to see it through completion.

[00:26:06] And it’s a judgment call for which, you know, when you pull that off and when you say, okay, this is gonna be my tour of duty, like my job is over the next, I know that I’m committing for the next two years or something. To like really run this thing, own this ship. And that’s my responsibility. And you know what?

[00:26:23] At the end of it, I’m gonna do the same thing I did before. I’m gonna like, my success, I, I, I need a succession plan. And my succession plan is either we solve the problem when it’s done, or I’ve set out on trajectory where I can successfully pull back and focus on the next thing. And to focus on the next thing.

[00:26:39] I’m gonna become an IC again and go find the next thing to solve.

### Principal+ Engineering at Shopify
Ryan:

[00:26:42] I know later the story continues with you went to Shopify. You became an IC and you went from a principal engineer to a distinguished engineer. I’m curious, what is the tour of duty there that got you promoted?

Ilya:

[00:26:55] One of the, I think, underappreciated or misunderstood aspects of being a principal engineer is when people ask what, what does, what do you do?

[00:27:04] Like, you know, give me, give me a job description because I wanna become a principal engineer. Like, what are the boxes I need to tick? And the answer is actually embedded in the question. People that have to ask that question by definition are not principal engineers, right? Because the problems become ambiguous enough at that level where you kind of have to figure it out yourself.

[00:27:26] Like my expectation for, I, I mentor a lot of, uh, principal engineers that come into Shopify. Uh, my expectation for someone coming in that level is look, um, you basically, to use an analogy here, you’re gonna be dropped parachuted into foreign terrain. You’re in a recon, reconnaissance mission, and within the first seven days, you should figure out to lay the land and figure out where the problems are.

[00:27:48] Build alliances with your directors, VPs, whoever it needs to be, figure out what their problems are, and then kind of understand the situation and figure out where you can apply your particular skillset to help. I don’t have a prescription for you, like it, it is your agency. It is your problem to figure this out.

[00:28:08] And that requires a particular kind of skillset and a toolkit that you have to develop to figure that out because there’s a lot of ambiguity in that. Um, going to a level above that, uh, as distinguished engineer, it’s even more amorphous in many ways. There isn’t any shared definition. Right. But I, the way I think about it is.

[00:28:30] Proof of the dynamic range of the problems that you can solve. So, and then dynamic range kind of goes in a couple of different directions. One is technically, uh, so are you able to, have you shown a repeatable record of being able to operate kind of. All layers of the stack. If you’re engaged with a team, are you able to kind of go all the way down to the bare metal and understand what are the constraints?

[00:28:55] What are the problems kind of from ground truth, reconstruct the problem at the same time? Are you able to operate with the business requirements, you know, with your VP and product counterparts? So actually understand what’s in their head. How it manifests in code and translate that into actionable change and like deliver the right product.

[00:29:12] That’s the technical aspect of it. Um, but then there’s also the, uh, the execution model, uh, kind of in the middle where you have to be able to flex. Uh, there are different types of projects that you get parachuted into. Some projects are, uh. Working at the frontier of knowledge or product space where there’s like just fog of war.

[00:29:31] You don’t know what you don’t know, and you have to be working kind of the less startup mode of, look, we’re gonna fire, we’re gonna see where it lands, then we’re gonna aim and we’re gonna fire again, and we’re gonna do that really rapidly, really fast as quickly as we can, so we can figure out where the hell we are, and then we’ll figure out what we’re gonna build.

[00:29:48] Right? That requires a particular skillset. On the other hand, you can be parachuted into. Kinda a, a slower moving pace, A pace layer of the company where it’s like, okay guys, we have this, uh, platform API problem. You know, we have a, just use them like a random example, right? Um, and. It’s really important that we think through how we design this API, because it’ll have second and third order repercussions, like years down the road for our partner ecosystem and all the rest.

[00:30:17] So we need to engage our slow thinking brain to really understand how this change at this layer will manifest its way through all the others. Right? And that’s a very different mode of engagement. That’s like, that’s much more, in a way, academic, but you also need to be able to take all of that divergent thinking and converge the problem to like, here, here’s the actual recommendation.

[00:30:38] Right. So it really becomes the demonstration of your toolkit of being able to execute across all of those domains. Because when you talk to, like, the expectation for a distinguished engineer is kind of similar to a vp, like it, it is a VP equivalent role, right? Like, write me a description for a vp. Well, the job of of a VP is to solve every problem that lands on their plate, right?

[00:31:01] It’s like, and by definition, all the easy problems have been solved. Before, like at layers below them, so they only get the heart problems with incomplete information or imperfect decisions. So, uh, show me the volume and show me the versatility of your toolkit. That gives me confidence that I could parachute you into, like, I can give you this weird shaped problem next.

[00:31:24] And with reasonable success, you’ll be able to navigate yourself out of it. Uh, one thing that I, I share often with, uh, folks that I coach and work with is I, I, I have this belief that a better way, a more resilient way to build your career is to optimize for being the only person as opposed to the best person.

[00:31:45] So what does that actually mean? There, there are two different paths that you could take. You could say, look. I’m gonna pick a particular domain and I’m gonna be the best person that will know the most about a particular thing. So I’m gonna like, take security as an example, right? I’m gonna learn everything there is to know, and that’s gonna be my life, life calling.

[00:32:05] And that’s great, but there’s absolutely nothing wrong with that. Um, you, you can optimize for that. My personal philosophy is, um, that is one way to success, but it is not the most resilient way to success, uh, because what if you pick the wrong field? What if the world changes under you, what if, um, your particular company does not need that particular skill set?

[00:32:28] B, the only to me is, is about building a talent stack or a portfolio of skills that you can juggle and be effective. And I think this is actually, um, reflects back in the dynamic range conversation that we were just having. Right. Were you able to say, look. And maybe this is actually me justifying my own career track because when I look back on my career, I could say like, look, I was a mediocre designer.

[00:32:52] I was a mediocre um, salesperson. I was okay at support, but like, come on, like that. That’s not my life calling either. But you know what? I did really well. I all of those things into a unique toolkit that other people could not do. Like, I could look at a problem and I could say, yeah, I could link together a website.

[00:33:10] I know Photoshop well enough. I know how to host it and I know how to secure it, and I can stand all that up for you in, you know, in the next two days. You don’t have to hire a team for that. And I have, I have the dynamic range to do that. Now, if it turns out that, um, we now hire the graphic designer, that’s excellent, but great.

[00:33:30] I’m just gonna take that particular skill set out of Mike Quiver, hand it over to them, and I’m gonna focus on the other things. Right. And I think generally, uh, you can acquire very high competence, like 80, 90%, uh, competence very quickly in a domain. You can get to 80% in a matter of days to weeks. And especially now with the tools that we have access to with LLMs and all the rest, like the ability to acquire context is, uh, just amazing.

[00:33:57] You can spend the next year to get yourself to 90%. And now if you optimize for that, you have resilience because. I’m able to converse with our marketing team because, you know what? I took the time, like I, I literally remember going on Amazon and I bought 15 books on marketing and I spent a week nothing but reading marketing books so I could understand the lexicon, the jargon, and, and speak the right words when I talked to marketing teams.

[00:34:26] I’m also adept enough at, uh, working with our PR teams because, like I’ve written a lot, right? And I’ve practiced that muscle. I’m also an engineer, so I now I’m able to bridge. So oftentimes when I find myself in conversations at Shopify or elsewhere, I am the translator between all of these different parts of the company and organs of the body where I’m able to kind of synthesize that information and bring it together.

[00:34:51] And that gives me a lot of versatility, right? It doesn’t mean that I’m the smartest person in, in the room. Uh, oftentimes it’s far from the, uh, uh, from the truth. I’m often the most senior person, but rarely am I the most knowledgeable, and that’s actually very important because part of my skillset is to figure out who are the most knowledgeable people and figure out how to leverage them in the most effective way.

[00:35:14] Right. My contribution is, I understand kind of the fundamentals. Of the platform and what you can do with, um, our APIs or our platform. I understand the business requirements. There’s a very messy middle, in the middle of how you actually implement the solution with a number of variants, that’s not my responsibility.

[00:35:33] My responsibility is to help the people that know the most about that messy middle navigate through that decision space, and I have a toolkit to help them facilitate that. But it’s not, it doesn’t mean that, you know, the most senior person in the room knows all the answers, which I think is a mistake that a lot of engineers make when they think about principal engineers.

[00:35:51] Like, oh, if you’re a principal, you know everything. There’s to know about the web platform. It’s like, well, not really, right? Like what I’ve learned is a lot of pattern matching. I’ve learned how to find answers, I know where to find answers, and I know how to navigate myself out of tricky situations. But it doesn’t mean that I know every API and every cork.

[00:36:13] Now some people do because that’s what they make their life calling and that’s, I think that that’s perfectly fine. But as a general strategy, I think it’s not as resilient. Got an anti-fragile career is where you have a set of these capabilities where you can just swap out and then you give a moment and and say, okay, well I guess I’m solving a go-to market problem right now, so let me pull out my other quiver of capabilities.

Ryan:

[00:36:37] I see. So when you say don’t be the best, be the only, you’re saying that generalists have an advantage because they can put together a bunch of skill sets, get most of the way there, and be the only because the intersection of all the skill sets is more special and more resilient because you have such a wide toolbox.

[00:37:01] Is that right?

Ilya:

[00:37:03] Yeah, this is, this is literally probability math, right? It’s like how many people, if you multiply out the probabilities of how many people know this particular, have this particular skill set, like you know enough about databases, you know, enough about graphics, you know about, you know enough about all these other components, who is the person that is the only person that has sufficient.

[00:37:22] Domain expertise and connective tissue to solve this problem. Right? So the on being the only is about having a wide range of tools that you can reach into and say, Hey, I can combine them in any particular way, which is what makes you versatile and makes you effective in these kinda ambiguous situations where you can, based on the situation, adapt how you work, right?

[00:37:41] Because I can shove gears and say, look, I’ve, I’ve been a manager before. I understand what it means to do performance management. I understand how to coach people, um, so I can. Even if I’m working as an ic, I can take an engineer aside and say, look like, here’s some feedback, or here’s some recommendations here.

[00:37:57] I know how to conduct myself. I know what things to say, what not to say and and help them along the way. Right? It doesn’t mean that I’m exercising that skill all the time, but I’m able to be parachuted into a situation where I can act as that temporarily, and that’s turned out to be incredibly helpful.

Ryan:

[00:38:14] I had one mentor who did Seesaw as well, and he said that management. Always appreciates an IC that understands management because it’s much easier to partner with them.

Ilya:

[00:38:26] Yes, absolutely. So I would absolutely encourage, um, if you’re on IC track and you’ve never tried management, like def, like being a TL is a great learning wheels.

[00:38:35] Um, you should definitely try if it, if it suits you to do management as well, but don’t assume that it’s a one-way path. You can go back and forth and there isn’t a stigma. I think historically there has been in some organizations, because also we’ve kind of painted this picture of, hey, the path to success is you grow to be a manager.

[00:38:56] But that’s not like when I talk to a lot of managers in like high roles directors and all the rest, you know, after you sit at a bar and, and, and have a couple of drinks, they’re like, you and your flight back and when was, when were you happiest in your career? They say. Huh. You know, it was a couple years back before I became an ex because I had, like, I was really confident at that thing, and I was loving it, but I was told that in order for me to like grow, quote unquote, I needed to take on this other thing.

[00:39:26] It’s like, well, huh, well that’s, that’s an interesting reflection. Right. And at the same time, they will reflect and say, but I’ve also learned a lot in this new role. I appreciate what it means to run a team. The complexity, the interpersonal dynamics, the performance management, and all the rest. And that’s an amazing tool to have in your toolkit.

[00:39:44] Great. Now, um, let’s set up our organizations in a way where that is okay for people to transit between those roles. Uh, you’re not penalized, and let’s not as an industry position as some sort of like demotion, right? Because oftentimes it’s like, oh, you’re a manager. You became an ic. What happened? What do you mean what happened?

[00:40:03] Like nothing happened. I just, I, I wanted to on a new challenge, like that’s not a demotion.

### Career regrets
Ryan:

[00:40:09] When you look over the course of your career, were there any points where you have regrets that others could learn from?

Ilya:

[00:40:17] Don’t let the pressure of your success stop you from trying. Um, let, let me unpack that a little bit.

[00:40:25] Uh. I reflected on this like as, as a writer, as a blogger. I remember like when I look back, um, and I wonder if you can, like, if you can relate to this, when I look back on my early writing, I read it. Now I’m like, oh my God, that is terrible. What was it? Like, how could I have published that? That is just flat out embarrassing.

[00:40:44] I hope nobody finds this right. Or, uh, frankly, if I go on GitHub and look at my own projects, like it is embarrassing code. But you know what? It was the limit of my ability at the time when I did it, and I’m so glad that I did it right because it was those milestones, like putting that work out there that gave me the right feedback, gave me the right encouragement that then led me to improve.

[00:41:09] But the challenge that you run into is as you level up and as you get an like an audience and an expectation, it’s like, well, you know, Ryan’s interviews are really good. So in the next one, like I, I expect it to be like an out of the park better than ever. So you keep setting a higher and higher bar where you start to filter like, you know, here’s the thing I would’ve published before, but uh, I’m not sure if it’s up to my standard now.

[00:41:33] Like, is it really interesting? Do I have a unique take on it? Whereas before it was like, I don’t care. Like just a thought. Here you go. Keep publishing. Like, I struggled with this all the time. Like, keep putting stuff out there because don’t let that expectation become a gate and filter. For the work that you put out, because that feedback that you get and exposure is like that, that is actually the quintessential ingredient that you need for growth.

Ryan:

[00:42:01] Definitely, definitely. And yes, I can relate. I think there was a, there’s a year or two where I was writing a newsletter and every week I’d published something and at some point the email list is growing and it’s growing, and I could tell at the beginning when I’m ideating, what am I gonna write this week?

[00:42:18] A lot more nos coming in my mind. I go, oh no, this one, this topic’s not good. Right? Uh, I’ve seen this somewhere. Oh, this.

Ilya:

[00:42:25] Yeah. It’s, it’s that courage to be wrong, to be disliked, to make a mistake. Right? It’s like, Ryan, I thought you’re like, or Ilia, like, I, I thought you were smarter than that. Like, why did you say that thing?

[00:42:37] It’s like, well, that’s what came to my mind and like, it’s fine. I, I don’t claim to be an Oracle. Right. I, I have, I have other, um. Expertise and, and other things. And this is what I thought at the time.

Ryan:

[00:42:49] Definitely. And I, I also wonder if that kind of similar thinking as you grow in your career. I mean, it would take some courage for you to step into a new area that’s completely new to you if everyone knows you as distinguished engineer and very knowledgeable in your given domain to step into some new area where you’re gonna make a lot of mistakes.

[00:43:14] That, that feeling of that downgrade is, is tough for a lot of people.

Ilya:

[00:43:19] Yeah. That’s where setting the right expectations with yourself and others is also very important, right. The, the way you show up to these conversations makes all the difference, right? Because I don’t show up as, Hey, I know all the answers.

[00:43:31] Rather, I show up as, Hey guys, I’m here to help. I’m just, I’m like, really curious and I started asking why? Like, what? What are the fundamentals? Help me understand this. The way you ask questions becomes very important. Because it’s very easy to come across as trying to question all the things as opposed to being curious, right?

[00:43:52] Like, there, there’s a subtle difference between them. Um, am I trying to attack your work or am I just trying to construct a model and just setting clear expectations of that? Um, oftentimes when I begin these conversations, I’m just very open about, guys, I don’t know what you, what you know. Right. And I need to very rapidly build my mental model of this space.

[00:44:13] So I’m gonna ask a lot of dumb questions like, excuse me upfront. I also have my expertise and I also know some other things that you don’t. Um, so help me navigate through this. And it becomes a collaborative of exercise, right? Because I can. Uh, clear roadblocks and do things that they can’t, but they can bring all of the knowledge.

[00:44:32] And this becomes the symbiotic relationship of that goes back to how do I leverage the expertise of people in the room as opposed to trying to question their work. And that takes a lot of that stigma out of that new environment, uh, in work. But I think there’s, uh, an even higher filter from when you’re like broadcasting because there’s an expectation and an aura of like what.

[00:44:53] What you’re expected to be saying. Right. And I think it’s, um, some people do a better job of that than others in terms of staying true to their thoughts and, and less filtering.

### Top career-impacting book
Ryan:

[00:45:05] Is there a top book that impacted your career?

Ilya:

[00:45:09] The first thing that comes to mind, and this is, uh, this is not a book, but an author.

[00:45:14] So Ken Robinson, uh, he has a series of books, um, on like finding your Element Creative Schools and the rest, uh, if nothing else, uh, go on YouTube and search for Ken Robinson and watch his TED Talks. Uh, it is I think 20 minutes of your time. That is gonna be the highest ROI. If not today, this week, may, maybe this year.

[00:45:39] Uh, he, he’s been an inspiration to me and it’s, I think his messages needs to be continued. Uh, unfortunately he passed away. But a key of it is we need to rethink how we think about education. And that actually kind of circles back to the conversation, but we’re having, but Waterloo, his message is, stop. We need to rethink our education system from a factory line model where we like put people by age into a certain bin and teach them specific skills like we, we all.

[00:46:06] Spike in different ways at different points in our life, right? Like let’s have an environment where people can choose their own adventure. Now that how do you execute that turns out to be really hard. And he dedicated his life to trying to figure that out. Like how do you reform the educational system?

[00:46:21] But I think his philosophy is very much kind of in line and probably informed a lot of my thinking for, hey, it is about creativity. You should mix things up. You should combine skills. Let’s build a system that actually allows us to like, help kids learn these behaviors better as opposed to pigeonholing themselves into like, well, no, you’re in grade five.

[00:46:43] In grade five, you’re only supposed to learn this thing. Thank you very much. And, uh, like, please don’t touch advanced math until you like, until you in grade six. It’s like, well that’s, that’s nonsense, right? Like for some kids, they can go all the way to grade eight math when they’re in grade five. Just use one example.

### Advice for younger self
Ryan:

[00:47:00] Then the last question is, if you could go back to yourself at the beginning of your career and give yourself some advice, knowing everything you know now, what would you say?

Ilya:

[00:47:10] I would come back to “don’t be the best, be the only”. Um, I, I think early in my career had a lot of fear of, Hey, I’m, I’m a mediocre at a lot of things.

[00:47:23] Like I, I see my friends, I would look up to my friends who are really good at design. Like, oh, I wish I could do that. Right. Or look to my other friends who were just better engineers. Like, I wish I could do that, could do that. But the thing that I had was ability to negotiate across all those themes. And that’s uncomfortable because I wasn’t sure if that would pan out.

[00:47:43] And it turns out that it did. Um, and then the other thing is, uh, ex exactly as we were just discussed, don’t, like, don’t, don’t filter or be, be, be braver about this stuff. Um. It’s, it’s kind of ironic that later in my career, I part of like my nine to five effectively became public speaking. Going through high school.

[00:48:06] I was deathly afraid of public speaking. I would run away from class to avoid it, right? Like I said, I, I vividly remember those stories and then it dawned on me later when I was doing post rank that, Hey, how, why is it that I was. Even through university, like I had cold sweats standing out in front of a class trying to explain the thing.

[00:48:27] Uh, but I was totally adept and fine when I was pitching, uh, my product to, uh, an audience. And the difference is, in one hand, I, I was trying to describe a thing that, you know, I didn’t have any particular investment in. It was a test of my knowledge. Versus, here’s the thing I’m passionate about and I want to like enact change in the ecosystem to move it to some new direction.

[00:48:51] So that turned out to make all the difference for me. And uh, maybe that’s the key thing. Like if you told me, uh, early in my college career that my future holds public speaking, I would, I don’t know what I would do. I would say that you’re crazy.

Ryan:

[00:49:08] I see. So to be more brave. Chase your passions. Yeah.

Ilya:

[00:49:13] And it’s also very different when you’re chasing your passion kind.

[00:49:15] A a lot of things flip in in how you engage, um, as opposed to being told to stand up and, you know, and rehearse a skit. A hundred percent.

Ryan:

[00:49:26] Awesome. Well thank you so much for your time, Ilya. I’m really excited to share this one with everyone. Is there anything you wanna say to the audience before we end the, the recording?

Ilya:

[00:49:37] I think we’ve covered a lot of ground. Um, I hope some of it is useful and, um, you can find me on, on the intranets and please feel, feel free to reach out and, and have a chat.

