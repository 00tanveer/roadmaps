---
guest_name: Bobby Holley
biggest_role: CTO at Mozilla Firefox
current_company: Mozilla Firefox 
company_size: 1300
YOE-starting: 2007
episode_date: 10/10/2025
episode_duration: 95
episode_title: "Mozilla Firefox CTO on Browser War Stories and the Path to Distinguished Engineer"
episode_description: "Bobby Holley went from an intern to the CTO of Mozilla Firefox. I asked him about everything he learned in that process. We cover his full career including some interesting stories on living through the browser wars and advice on career growth to the highest levels."
guest_background: "Went from an intern to the CTO of Mozilla Firefox"
topics: ["Starting at Mozilla", "Browser wars history", "Google relationship changing", "Why work for free", "Projects that drove his career", "No performance reviews", "Rust adoption", "Career progression", "Should you focus on promos", "Distinguished promo rejection", "Examples of distinguished engs", "Advice for aspiring distinguished engs", "AI browser wars", "Biggest technical regret", "Book that impacted his career most", "Advice for his younger self"]

---
# Mozilla Firefox CTO on Browser War Stories and the Path to Distinguished Engineer
## Bobby Holley went from an intern to the CTO of Mozilla Firefox. I asked him about everything he learned in that process. We cover his full career including some interesting stories on living through the browser wars and advice on career growth to the highest levels.

Transcript
00:00:57 — Starting at Mozilla
Ryan:

[00:00:57] Before actually working at Firefox, I saw that you interned at Nvidia. I’m kinda curious, why’d you pick Mozilla over Nvidia?

Bobby:

[00:01:05] Yeah, so I mean my first internship after freshman year was at Nvidia and it was, it was a great internship. Um, I think it was much more, uh, standard of internship. You know, you show up, there was orientation, they showed you what to do, you sat at your desk, gave you a very basic starter project, said, well, you know, we’ll check on you in a couple hours.

[00:01:24] Um, and it was really designed to be a sort of thoughtful, you know, growing experience for somebody who didn’t really know what they were doing. And Mozilla was, I would say, quite different from that. Um, I remember showing up, uh, really I think on my first day my manager was the director of platform who ran all of Gecko.

[00:01:45] There was this guy, Damon Secor. Um. He really, he had a very particular vibe. Um, he sort of embodied, I think the dude from the Big Lebowski in like all of the best ways. Like it’s just extremely laid back. Um, and I remember asking him, you know, what should I work on? And he was like, I don’t know, like go get on IRC and get on Bugzilla and like start figuring out some things to do.

[00:02:08] And that was just a very big contrast to the sort of more standard internship. And what that spoke to was the nature of how Mozilla operated. Because Mozilla had been an, you know, open source project that largely happened in some ways by accident, where lots of people just showed up and started working on things and there was not a lot of support and.

[00:02:38] There wasn’t, you know, this was like way before video conferencing. There was just the bare minimum of what you needed. If you were really dedicated and really, um, creative and really persistent to figure out like how you would download the code. You had to figure out how to download it. You have to figure out how to build it.

[00:02:53] You had to figure out where to go to, you know, file bugs and like get help. And there was just like not a lot of guardrails. And what that selected for was a particular type of person, um, who really just needed the bare minimum and was very motivated to just go in and figure things out. And so the management structure at the time was very much oriented towards nurturing and empowering this culture, right?

[00:03:18] Very much like, let’s get the right people together and let’s just get outta the way. And so this, for me, I would say initially was a little bit disorienting, but I ended up getting really inspired by. All of the people who were working on it, some of whom were paid, some of whom were not paid. And a lot of these people, you know, maybe they’d started being paid recently as Mozilla started to have money, but had been, you know, getting involved in the project from their college dorm room, just trying to figure out how to make their browser crash less.

[00:03:48] There was this guy, um, sort of one of my longtime heroes, Boris Ky. Uh, we didn’t really, I didn’t think, don’t think there were really titles at the time, but he eventually was one of Mozilla’s first distinguished engineers. And he was just very awe inspiring to me because I only, you know, for I think several years, I only met him on IRC, but Mozilla was a wild west.

[00:04:10] You know, the Firefox code base was a wild west of code, just like tens, you know, millions and millions, probably about 10 million lines of code that were inherited from Netscape and largely Unowned. And the major challenge was just dealing with all of this code and figuring it out. And Boris probably owned like half of it.

[00:04:29] He was the person of last resort that you would always ask. If you didn’t know what to do and you would realize that you’d be having this conversation with him on IRC, and then for me it would be like taking all of my focus of trying to understand and like, you know, keep up with him. And then I would realize that he was in like five other channels at the same time.

[00:04:46] Like having these conversations with like other senior Mozilla engineers, other interns, contributors users who were just having bugs and he was just a machine.

00:04:57 — Browser wars history
Ryan:

[00:04:57] So, I’m kind of curious at this time, how does this tie into the, the timeline of Google Chrome and, and the browser wars? Was this before Google Chrome?

Bobby:

[00:05:07] Yeah, so this was before Chrome. Um, I guess as, as a brief history lesson. So the original round of the browser Wars was in the nineties, and this was largely defined by Internet Explorer versus Netscape. Um, and they competed with each other by trying to, you know, ship different proprietary APIs and make the site work better in IE or work better in, in Netscape.

[00:05:25] But eventually, uh, internet Explorer one, largely because Microsoft bundled it for free as part of Windows, um, and was very aggressive with respect to distribution and really pushing Netscape out of distribution. And Microsoft eventually was, you know, taken to court and lost and, you know, had an antitrust judgment about precisely this.

[00:05:46] But the way the market works, right? Like it didn’t matter, like IE had already won and Netscape was going under. And as, as sort of a, as a parting shot, they opened, sourced the code, um, and created this Mozilla foundation to steward this gargantuan massive browser code that was Netscape Navigator. And then what happened was that.

[00:06:09] Microsoft decided that this web thing was not particularly aligned with the strategic interests of Microsoft, right? Because this web thing was a new platform where you could use the same, have the same experience across different operating systems. And so they largely just declared that they had won and they put the browser in maintenance mode.

[00:06:28] But there were a lot of people who really saw the potential of what the web could be and what it already was with like Internet Explorer five and Internet Explorer six, but that it could be so much more. And a lot of these people like Boris were just drawn to, I wanna make this experience better and I want my browser to stop crashing.

[00:06:44] And so people started downloading this source code for Netscape Navigator and working on it and gradually improving it and adding, um, new features like the ability to block popups and the ability to have browser tabs rather than a new window for every website. And this sort of gradually turned into, um, a really more useful browser than Internet Explorer was, but.

[00:07:08] It was still very much a suite, right? It had a email client in it, it had a address book. It even had an IRC client for all of the developers. You know, it was kind of built into the browsers so they could talk to each other. And eventually a few, I think, relatively junior people, you know, just like some, you know, contributors and interns, you know, came along and decided to build a strip down version of it.

[00:07:29] And that was originally, um, that was just a browser, the bare minimum of what you need for a browser. And that, originally they called it Phoenix, but then that was a bios, and then they re renewed it Firebird. But that turned out to be a database. And then finally they called it Firefox. And Firefox just took off like wildfire because the world really wanted a better browser and it was a better browser.

[00:07:50] And so Firefox became, you know, just this thing that everybody, you know, the first thing you do when you got a computer, what you do for all your friends, what you do for your family members is install Firefox because it’s just such a better experience. And Google was extremely, um. Well aligned with this, right?

[00:08:08] Because Google was this, you know, burgeoning product and business that was largely built around a search engine that was about discoverability of the web. And so that the more that the web was discoverable and usable and useful, the better it was for Google. And Google quickly realized that Internet Explorer was a big problem and that Firefox was really this coming solution, uh, to this.

[00:08:28] And so Google was very, um, very invested in Firefox’s success. When I started as an intern, we all received badges to go over to the Google campus and eat lunch whenever we wanted. There were snacks in the kitchen that I heard, I never quite confirmed were directly delivered, um, by the Google facilities people.

[00:08:47] And of course, the most important was that Google, uh, signed a deal with Mozilla to be the default search engine for Firefox. And this was perfectly fine with Mozilla because everybody liked to use Google anyway. And this was, uh, great, uh, user experience and. It also suddenly allowed Mozilla to be financially sustainable and to hire a lot of these contributors who’d basically been working nights and weekends.

[00:09:12] And Google had engineers, uh, that were directly working on Firefox and contributing to it. And there was really this sense that Google and Mozilla together were working to unlock, you know, the future of the open web. And when I started in June of 2008, that was sort of the peak of that sentiment. But shortly thereafter, Google announced that they were building their own browser, which was Google Chrome.

[00:09:39] And I think that you can obviously see why in retrospect, right, the real, the, the business strategic posture of Google as a company was really hinging on this ragtag group of very weird people. Who were working on this open source browser, and there was a desire to have a little bit more control over their own destiny.

[00:10:00] And so when they initially announced Chrome, you know, we had a, a meeting, John Lilly, uh, told, uh, everybody worked at Mozilla about this, but indicated that it was still a very friendly, the desire was to take market share away from Internet Explorer and that we would still continue to be close partners and on the same side.

[00:10:17] And initially it really did feel that way. Um, but as time went on, things started to change. And I think, um, I think it was like 2009, there was a New York Times article that I think really captured the zeitgeist. I think the title of it was something like, between Mozilla and Google Group, hugs are Getting Tricky.

[00:10:36] And that referred to this very positive hippie atmosphere of working together on the future of the Open Web and the degree to which Google’s more direct business interest. Owning and controlling the user’s journey on the web was starting to create tension.

00:10:55 — Google relationship changing
Ryan:

[00:10:55] You mentioned that at some point you had Google badges and you had free food through Google and you had a good working relationship with them.

[00:11:04] How did it transition from that to a full competition in your personal experience?

Bobby:

[00:11:11] So my sense is that as time went on, things changed slowly. And I really don’t think that it’s a situation where any individual person at Google was like, ha ha, ha, now we are going to get them. And they don’t know. But it’s just the way that organizations work.

[00:11:28] And so we continued to have strong collaboration, um, with many engineers over at Google. But there were two things that really happened at the same time. The first is that Google really ramped up its attempt to acquire market share with Chrome. And this was, you know. Probably very truthfully aimed at Internet Explorer, but Mozilla was very much collateral damage, and they were spending hundreds of millions of dollars a year on advertising and distribution.

[00:12:05] And if you were to include the effective cost of the advertising that they put on google.com, which was their own homepage, the advertising spend I think would reach into the billions. And there was very much a sense that whenever we talked to them that it wasn’t supposed to be directed at us. Jonathan Nightingale, who was a VP of, uh, Firefox at the time, you know, a couple years ago he did a, you know, a tweet thread explaining his point of view on this, and I think he referred to it as the year of a hundred Oopses, where every time Google would do something that would hurt Firefox.

[00:12:41] It would always be framed as unintentional. Right? And the obvious way this would be is that like Firefox was sending source traffic over to Google. And so when users were in Firefox, they typed something in the address bar, they would end up on Google and then Google would show these Firefox users a, an an ad that would say, or a big banner directly on google.com.

[00:12:57] Like not even on the search engine result page saying Download Chrome. It’s better. And they always claim that it was unintentional. But these things just kept happening over and over. And I do think that on a sort of organizational strategic level, it was unintentional, but the individual incentives of the people involved and what they got by doing this and then, you know, maybe fixing it in a, in a release a couple weeks later, you know, they still won as far as their metrics were concerned.

[00:13:23] So that was one piece. But there was definitely another piece where Firefox had legitimately fallen behind. And part of this was that when Chrome came out, it had a. A lot of really interesting and new architectural innovations, um, that created gaps with Firefox. Some of these included having a multi-process architecture, um, and they had a plugin architecture, like for things like Adobe Flash that was much more robust against ability issues.

[00:13:58] And they had a very fast JavaScript engine. Firefox also had a fast Java script engine, and we, you know, traded back and forth, uh, you know, taking the performance crown. But they had some real structural advantages. And at the same time, Mozilla made a big and ambitious bet in the early 2010s to try to build a mobile phone operating system.

[00:14:18] Uh, because there was this sense that mobile is coming and both Android and iOS are potentially hostile platforms that are not gonna allow. Firefox to do what it did on desktop, on their platforms. And the belief was that the only possibility was to create a new mobile operating system, uh, that was based on web technology.

[00:14:37] And, you know, there was something to that idea and there was quite a lot of interest from the industry. A very surprising amount of interest. And we had a lot of partners, but ultimately it didn’t work. And the big bet that Mozilla made on Firefox os created a lot of resource competition with the work that needed to happen to keep Firefox competitive exactly at the time when it was needed the most.

[00:14:58] And so Firefox really had a lot of, um, gaps with respect to Chrome. I think the multi-process architecture was a big one. The stability issues, particularly coming from Adobe Flash, which was widely used, particularly for streaming video, which was becoming a thing that was another big gap. And Firefox also had some legacy baggage around its, uh, browser extension, API.

[00:15:22] Where the way that you would make a browser extension. I mean, the, the whole concept of browser extension really arose from the Firefox architecture where you could just inject anything anywhere. And the Firefox application was written in JavaScript and markup, and you could just modify it with an extension by just adding more JavaScript and more markup and more CSS.

[00:15:43] And this was really cool. And that’s where people first got the notion that you could configure and change your browser, um, and extend it with new functionality. But the problem was that there were no well-defined interfaces. And so all of these extensions were depending on all of these internal details of how the browser worked.

[00:16:01] And anytime we changed anything, we would break an extension. And so that was a very real and significant drag with respect to trying to architecturally modernize the browser.

00:16:11 — Why work for free
Ryan:

[00:16:11] You mentioned prior to Google’s funding, this was a group of, uh, bunch of people that were working for free in many cases. I’m kind of curious ‘cause I haven’t done a lot of open source stuff.

[00:16:23] What is the incentive structure? Why? Why would people spend so much time working for free on a project like this?

Bobby:

[00:16:32] So I think it probably varies, but the world was quite different back then and open source. There were not, first of all, a lot of opportunities for people to contribute to something major and meaningful, right?

[00:16:45] Like these days, much of the software stack that everybody uses, many projects were open source, but there were not so many of those back at the time. And so I think that it was an interesting opportunity to have impact. And I think for a lot of people, like I mentioned Boris, he literally got involved in Mozilla because he had no way to browse the internet in his dorm room.

[00:17:05] One option was, he was like at MIT at the time, I think, and, you know, he could either VNC into some like Solaris thing with Internet Explorer five, or he could use this build of Netscape that he downloaded that was just constantly crashing. And so he, he got involved just because he wanted to fix something for himself, and he had this vision of how he wanted it to be better for him.

[00:17:23] And then he realized that there were so many other people out there that were also looking for the same things and trying to fix this stuff. And once you dive into a code base like this, it is just an amazing intellectual challenge because the code base was just so vast and so complicated. And so he was like a math major, right?

[00:17:41] But this was in some ways, like even harder. And I think that that, um, challenge was another major aspect. But I think the biggest aspect was the motivation of the Mozilla mission and what we were trying to achieve. Because the, I think a lot of principles that people take for granted about, you know, how the web should work, that it should be open and it should be interoperable, that it shouldn’t be controlled by one.

[00:18:04] Company and even that, that about the internet itself. Right. You know, the Mozilla mission is about making sure that the internet is a global public resource that is open and accessible to all. And I think if you grew up in the nineties when Microsoft was eating the world, that was not a given. That was not the dominant way of thinking about how technology platforms should work.

[00:18:27] And Mozilla had a vision of how it could be different, and it had a means of executing that vision, right? It wasn’t just an advocacy organization arguing that tech companies should do something different. It was actually going out and doing something and succeeding and creating a browser that gave users choice to block popups and control over their experience and the ability to block ads and the ability to have tab browsing and all these things that they weren’t getting before, and creating that reality and making the world better in that way, I think was very inspiring to a lot of people.

00:19:02 — Projects that drove his career
Ryan:

[00:19:02] Yeah, I’m kind of curious, like, you know, once you got there, I want to hear a little bit about the projects that you’re working on and the various stories of things that happened in the early days. Are there any projects that you felt were particularly interesting or contributed to your career?

Bobby:

[00:19:17] Yeah, so I got started working on all sorts of things.

[00:19:21] Like I think as an intern, the first thing that I worked on was the, uh, front end for the new mobile browser, but this was before there was Android and iOS. So it was actually for like Nokia Mamo, uh, and that’s what I started on. Then I started working on the graphics engine. I worked on the image rendering library and there was very much a sense back then just because there was so much code that.

[00:19:42] You know, it was largely unowned that as soon as you show up and you start working on something and you like fix one thing, you start looking around and you’re like, Hey, who, who owns this? And they’re like, you do now. And so I really, I ended my first internship owning like quite a lot of code in the Firefox browser.

[00:19:56] And that felt to me like a really big important responsibility to make sure that, um, you know, this stuff went well. I think I was particularly motivated to work on the really, like the hardest and gnarliest parts of the code. Um, the parts that felt most critical when, you know, after Chrome came out and then Firefox was coming back with its first counter attack of trying to build a browser that was more performance competitive.

[00:20:25] Right. Particularly around JavaScript. So Chrome launched with this JavaScript engine called V eight that was, you know, had a just in time compiler and it was very fast and we were intending to ship our own just in time compiler, uh, for our JavaScript engine. But there was. A lot of challenge at the end of actually getting this thing shipped, particularly around this very complicated area of how the JavaScript engine talks to the rest of the system.

[00:20:50] You know how the, the bindings between the JavaScript and the dom, which were referred to as XP Connect. And so literally there were months of delay of getting Firefox four out the door because of all of the tangled web of that architecture. And I, you know, also at the advice of Damon at the time, decided to dive in and try to help make that stuff better.

[00:21:10] And so I ended up working on that code. And the thing about that code was that it was very, uh, tied up in a lot of security considerations in the browser when the browsers and the web were first designed. You know, JavaScript was famously designed in 10 days. People did not fully think through all of the security implications of this architecture, uh, both in terms of the web platform and the browser itself.

[00:21:37] So. Firefox as a browser. One of the cool things about it was that all of the application on the front end was also written in markup and JavaScript, but all of that relied from a security perspective on making sure that a website would be properly isolated from touching other websites and from touching the browser replication itself.

[00:21:59] And this was all a very complicated mess of security enforcement in this do binding code, and it was not perfect. And there was this cat and mouse game between people working on Firefox and this external community of security researchers. Who were constantly finding new ways to poke holes in this, right?

[00:22:18] And you do some very, very clever thing with, you know, function not bind, and you end up slithering up the prototype chain and suddenly you are like in the address bar and tab code. And once you do that, you know, the browser and perhaps the computer compromised. And so there was, um, there were a number of researchers, there was one, I think their name was Mbu RA four.

[00:22:36] We never learned what their actual name was. Uh, rumor had it that they worked in, they lived in a country where security research was illegal, but there was very much like a, a weekly back and forth between, uh, people at Mozilla working on Firefox and Moz Bug Ra four of new, um, potential paths of vulnerability.

[00:22:56] So Firefox four definitely, I think introduced a much more robust architecture. And that was when I got involved with some of the stuff. But there started to be other and additional security researchers who showed up who were finding new ways to poke holes in it. And what really started to worry me was that there were certain categories of things that we didn’t really have a way to fix in a robust manner.

[00:23:25] You know, we could put a bandaid over that particular part, we could wallpaper it over, but there were usually ways that you could apply the same tack in another part of the code base. And I started to get pretty worried about this, and I launched a very large cross-functional effort that I spent, you know, at least over a year on which I referred to as slaughterhouse.

[00:23:48] Um, and that was because, you know, it was a joke because there were these things called chrome object wrappers that we needed to get rid of. Um, but there was generally a sense, um, that this could be a really big problem if this, these types of exploits were to be weaponized in the wild, uh, before we did something about it.

[00:24:05] And there was one particular researcher who I worked with quite a bit, um, who was really good at identifying and finding these issues. And so what would happen was be these external researchers, they would send us something, they would file it in a confidential bug in bugzilla, in our bug tracker, and then we would look at it and be like, yeah, this is a real issue.

[00:24:22] And then we had a bounty program right, where we would pay them a small amount of money, um, as, as a thank you and an incentive to, uh, bring it to us and, you know, not sell it on the black market. But the black market certainly paid more. And sometimes there would be zero to exploits where you’d have to sort of jump on some new thing and fix it and ship, uh, a fix within, you know, 24 hours to make sure that users were protected.

[00:24:48] And sometimes these attacks got ahead of us. And so there was one situation where, uh. Somebody flagged me that there was a zero to exploit in the wild, um, that had been discovered. I think it was on like moscow times.com, and I was disassembling it. And then I had this realization that like, I knew who had written this exploit, um, because it was one of the security researchers that we worked with.

[00:25:15] And without thinking too hard, I fired off email to this guy being like, Hey, like you’re, you’re double crossing us, right? Like, you’re not supposed to sell these things if you report them to us. And he got back to me. And the thing about security researchers is that they’re extremely paranoid. He’s like, no, no, no, I didn’t.

[00:25:31] This must mean that my devices must be compromised at a very deep level. And the only thing I can think to do here is to go off the grid. And we then discovered a, basically like an hour later that actually it was Mozilla that had been compromised, that bugzilla, our bug tracker had been compromised by a threat actor.

[00:25:51] And I tried to write back to the researcher, but at that point he’d already gone offline and we couldn’t reach him. So it was several weeks later that we got a phone call from a bowling alley in upstate New York where this researcher had gone into hiding and was trying to, you know, throw off the people that were after him.

[00:26:08] And we managed to explain that actually, sorry, this was our bad and had to help him get back on his feet. But it was a really big problem that Bugzilla had been compromised because that is where you have the records of all of the interesting security attacks that people have discovered against the browser.

[00:26:27] But the amazing thing was that slaughterhouse had just wrapped up and that out of, I think S 45 of the, I dunno, something on the order of 45 of the bugs that the threat actor had, um, exfiltrated, we had fixed all but two of them. And with this sort of new architecture that basically fixed it. And so that really impressed upon me the importance of getting ahead of things on security and making sure that you have the right architecture.

[00:26:54] Because sometimes you find you’re in a self, a situation where you don’t have the luxury of the time to fix it.

Ryan:

[00:27:00] How’d you know that that security researcher wrote that vulnerability?

Bobby:

[00:27:05] People have very particular styles. And in this particular area of security or of exploits, which is, which is different than other kinds, um, there was just a lot of people’s fingerprints on it.

[00:27:18] Right? You could tell because these were things that were handwritten logic attacks where you are using very particular parts of like, I’m gonna take this API and then I’m gonna bind this function to it, and then I’m gonna send this call like around async through the event loop twice and then I’m going to do this.

[00:27:34] Right? Like there was a very particular way, and these were all handwritten. There is a different type of security attack that was also. A major issue at the time, which were memory safety vulnerabilities. And these were much less of a artisanal thing and more things that you would produce by tools, particularly by fuzzing tools.

[00:27:55] And so this was also a major issue that, um, Mozilla was grappling with because you would have people who would run these fers against the code base. And the code base was written in c plus plus. And there are lots of ways to have memory hazards in c plus plus. And really any one of them is the sort of like webpage takes over your computer situation.

[00:28:15] And so we were really struggling to find ways to deal with that in a robust manner. Um, and that was really one of the things that motivated Mozilla’s investment in Rust.

Ryan:

[00:28:28] So I could see, and I’m just trying to understand here, the, the security issue here is there’s some front end code that abuses or does some special path in Firefox.

[00:28:40] And then can take over Firefox in, in that case in the past. But how does it take over the computer? Wouldn’t the operating system kinda shield, um, ideally from Firefox doing crazy stuff?

Bobby:

[00:28:53] So, certainly not at the time, like originally, particularly on Windows applications largely ran with system privileges.

[00:29:00] And if you took over the, you know, the, the, the classic thing that security researchers would do to prove that they’d pod your machine was to launch the calculator, um, like the Windows calculator, right? And so you’d run this exploit, you’d really have to trust the person who sent it to you that it wasn’t gonna do anything bad.

[00:29:14] But, you know, calc xe, that was, that was the proof as time went on, and, you know, Chrome had a major hand in improving the table stakes of how browsers worked. There were additional layers of protection that were put on, right? And so some of these include in-process sandboxing, um, as well as operating system level sandboxing.

[00:29:34] And so the. Architecture that browsers like Firefox and Chrome have today involves a very, you know, defense in depth, multiple level of, uh, multiple levels of protection, including operating system level sandboxing that is applied, um, to things like, you know, the, the rendering and content processes. That said this was all bolted on over time on Windows and Windows.

[00:30:00] Unlike an, you know, a platform like iOS. Um, iOS is designed from the beginning with an and with an application sandboxing model where applications are just applications and they have their own little world. That was not how Windows worked. And so evolving windows and evolving the security critical applications that sit on top of Windows like browsers to deal with these sorts of attacks is honestly an ongoing challenge.

Ryan:

[00:30:24] Did you ever figure out how Bugzilla was compromised?

Bobby:

[00:30:27] I, I think it was a credential leak from an employee like that. I, I’m 85% sure that that’s what it was. And that was, I think before we had things like two-factor authentication, um, for logging into Bugzilla. You know, Bugzilla was a very old tool that dated back into the nineties.

[00:30:41] And so similarly, it was something that had to evolve with the threats over time.

Ryan:

[00:30:45] One thing that I was curious about is, as an organization, how do you prioritize security? Because for instance, at the time there was also these big investments in performance, and I’m sure there was a bunch of other things

Bobby:

[00:31:00] For sure.

[00:31:01] Yeah. Security is one of those long-term things that is very easy to take a short term perspective on and ignore. And that is perhaps a decision that some products will make. Uh. Even where they are, but it’s not something that you can do as a long-term browser. And so honestly, from my perspective, it’s a cultural thing in Mozilla that from the very beginning, back before there was any sort of management structure and performance measurement and you know, company objectives, it was just understood that we had an obligation to protect our users and to keep them safe.

[00:31:36] And I think that persists, that means that there’s a lot of, I would say ongoing bottom up energy towards making sure that we improve security. And there’s a lot of pride that people at Mozilla take in the security of Firefox. Um, because Firefox does not have, you know, I think that the Chrome security org, you know, on its own is like on the order of, you know, 70 plus people.

[00:32:02] And we don’t have anything close to that, but it is considered to be a shared responsibility and we have a lot of people who are very dedicated to that and trying to think ahead, right? Like slaughterhouse, the project that I led that was not any kind of. Top down edict of we need to go fix this. It was that I was responsible for the code and I felt that this was important, that we needed to get it right.

[00:32:21] And one of the things that I’m very proud of at Mozilla today is that, um, there are, there’s an annual security, um, competition called Pun to own, where researchers show up and test their exploits and receive prizes for compromising the browsers. And generally speaking, they always find a way to compromise every browser, right?

[00:32:42] Like no browser is perfectly secure. And Firefox for the last two years has won the award of being fastest to patch, um, within, you know, on the order of 24 hours. And this is only possible because we have people literally in time zones around the world, uh, who are just working nonstop to get it out. Um, and it’s not something that we ask people to do.

[00:33:05] It’s, there’s no management edict that somebody needs to stay up late or work on a weekend to do it. People are just motivated to do it because they.

00:33:12 — No performance reviews
Ryan:

[00:33:12] You mentioned no performance reviews and this, uh, scrappy bottoms up culture. How does that kind of culture work?

Bobby:

[00:33:19] I think in the world of, prior to being a much management, it was just uneven, I think, as you would, as you would guess, right?

[00:33:27] And I think that it was generally things worked well because the caliber and dedication was very high, but it was very much a bottoms up culture, right? And if there was somebody who was owning that particular part of the code that wasn’t doing a good job, everybody just kind of lived with that. And, um, there also, I would say there was very much a notion of people having ownership of areas and that being, um, somewhat final, right?

[00:33:55] Mozilla had a governance structure that was very much insulated against any sort of executive power. Uh, it was this module system and people were owners of the modules. And, uh, even the, the initial access control system, I think was called Despot. Um, and. It was very much a notion of distributed and decentralized decision making.

[00:34:16] I think that that culture was very powerful and there are still elements of that culture that I think are important to preserve today, but there are also ways in which it fell short and needed to change. And one of the things that I have spent a lot of thought on over, you know, recent years is finding myself in a leadership position is how do we preserve those aspects of the technical culture that make it great, while also addressing some of the shortcomings.

00:34:42 — Rust adoption
Ryan:

[00:34:42] You mentioned a little bit about c plus plus and memory safety issues. That’s a very classic thing, and I know that Rust was developed at Mozilla to tackle those problems in large part. So I’m curious, um, can you tell me a little bit about the adoption of Rust and you know, how it solves the problem?

Bobby:

[00:35:01] Right, so in the early 2010s, it was pretty clear that Mozilla in Firefox. The code had some real structural issues and a lot of these were issues that we could address through sheer hard work, right? This included building a multi-process architecture, um, and evolving our extension architecture such that stuff, you know, didn’t have its tendrils into all the undocumented interfaces within the browser.

[00:35:32] Um, and building, uh, native video playback so that we didn’t have to rely on Adobe Flash anymore. Like these were all large but incremental projects to address specific architectural issues. But there were two architectural issues that were very difficult to address in that way. And the first one I already mentioned is memory safety, right?

[00:35:52] ‘cause when you have a code base that’s written in c plus plus, a large portion of the defects that you can make are the sort of defects that compromise the browser. And without sa and in the absence of sandboxing compromise the computer. Um, and that was just a very difficult thing to deal with, uh, in a non whack-a-mole fashion.

[00:36:14] And there’s another piece which was that particularly at the time, there was a increase in the number of cores that were shipping on devices, but browsers were still largely single-threaded. And this meant that you were leaving a lot of the available performance on the table if you didn’t have multi-threaded code.

[00:36:33] But if you did have multi-threaded code, especially in c plus plus, you just had all sorts of very difficult non-deterministic bugs that were very difficult to track down. And some of these also became memory safety issues that became exploitable defects. And there was this notion that both of these were rooted in deficiencies of the c plus plus programming language.

[00:36:52] And all browsers were written c plus plus. But you know, in 2010, Firefox had just taken on the world and opened up the web and there was a sense that we could do the impossible. And so we began an effort, um, you know, sponsoring some research that, uh, some people internally had around building a new programming language.

[00:37:14] And this programming language was rust. And the idea of rust eventually became that we would have a programming language that had static guarantees at compile time, that number one, you didn’t have memory safety issues, and number two, that you didn’t have race conditions. And this idea was that first we would build a new programming language with these properties, which was difficult to do.

[00:37:36] And then we would use this programming language to build a new browser engine for Firefox. And so the Rust Project co-evolved with this project called Servo, which was a ongoing, evolving test bed for the Rust Pro language with the intention of building a browser that was memory safe, but more importantly was parallel because there was a sense that.

[00:38:01] We could solve these architectural issues and close the gap with Chrome, but that also we needed something to leapfrog Chrome. And there was a belief that concurrency and safe concurrency powered by new programming language was the way to do that.

Ryan:

[00:38:16] Yeah. I wanna talk about the composition with Chrome at the time, because you said they launched with a, uh, more performant browser and also they were hammering you guys with, uh, distribution advantages.

[00:38:29] I’m curious, what was the strategy at that time from the Mozilla team to compete with Chrome?

Bobby:

[00:38:35] So the strategy to compete with Chrome was multifaceted. One of the parts was a recognition. I think there was a little bit of denial in the very early days about the deep value that some of Chrome’s architectural advantages would provide.

[00:38:53] This was, you know, they came out with a JavaScript engine with uh, what’s referred to as a method jit. We had a tracing jit. We thought that the tracing JIT was good and was gonna be better, but in the end it wasn’t. Chrome came out with multi-process architecture. I remember the first thing that I heard was, yeah, good luck doing that on Mac.

[00:39:14] And then they figured out how to do it on Mac. And there was a belief that some of these things were not possible until they were, and then once they were, that they weren’t the most important thing. But eventually it became clear that, uh, things like a multi-process architecture and things like native video playback were really essential.

[00:39:31] And we had this issue particularly on video playback where because Chrome first had a better plugin architecture, uh, for Adobe Flash, and then was also early to introduce native video playback, they were able to have. A much more stable experience on YouTube, which was blowing up at the time. Whereas Firefox on YouTube, which was what everybody wanted to do on the internet, was just crashing left and right.

[00:39:54] And it wasn’t stuff that we could fix. It was Adobe’s fault and we really couldn’t do anything about it. And so we had to work on a lot of these really hard but discreet challenges, um, of closing the gap with Chrome. But then at the same time, there was a desire of you can’t just close the gap. You have to do something new and you have to do something that is better.

[00:40:19] And Rust and servo were our strategy for doing better.

Ryan:

[00:40:23] So you mentioned the strategy with Servo and the rewrite and Rust. How did it go? Was it successful? Well, we, we know that Google’s distribution eventually dominated, but how did the efforts with Servo go?

Bobby:

[00:40:39] So on the one hand, servo and rust. Had against all odds captured something really real and servo as a browser engine prototype had a lot of really amazing stuff in it, right?

[00:40:55] It was not complete, but it did have the skeleton of certain features that had never been done before, including a Multithreaded CSS engine. But the problem was that we had a team of, you know, a dozen people working on rest and servo. Google had hundreds and hundreds and hundreds of engineers who were working on chromium.

[00:41:16] We had less than that, but still most of Mozilla’s efforts were directed towards Deco and Firefox because that was the product that we had in market. So we had this situation where in order to build a competitive browser engine, it’s not like you need to just do this one time. It’s the accumulation of all of the work over all of these years of hundreds of engineers.

[00:41:40] Working on improving it and improving the architecture, improving the performance, improving the features. And so every year there was more and more stuff that Servo would have to catch up with. And I think if you just look at it, there’s, it was very difficult to believe that we would ever end up in a situation where Servo would be competitive with a regular, um, production browser engine.

[00:42:02] And so circa like 20 14, 20 15, that was a situation where there was really a sense that we needed to deliver a fully refreshed version of Firefox that really got us back in the game that included this parallel CSS engine that we uplifted from Servo. And this was a project that I personally led and was really the highlight of my career working on it because it was so exciting to be doing something really new in a new programming language.

[00:42:35] That, and every step of the way, there was this notion that like, that’s definitely never gonna work. Right. Like, how are you even gonna like hook this thing up? And then we hooked it up and we had it traversing the dom over c plus plus. Um, you know, we have a c plus plus dom and we’re having this rust, uh, CSS engine and how you get these two things to work together.

[00:42:53] There was no tooling for it. We had to build it all ourselves. At the end of the day, it was really a dramatic performance improvement. I think it improved like rendering time on amazon.com by, on the order of 25%, which is just enormous in terms of, um, web performance. And because it was parallel and it can run on all of your cores, it was and still is the fastest CSS engine in the market.

[00:43:17] Firefox really got back in the game and was really performance competitive with everything else out there. And that was a really exciting moment for everybody realizing that if we just coordinate and we do all the technical effort and we make the right bets, we can win.

00:43:33 — Career progression
Ryan:

[00:43:33] Okay. So you mentioned that this was one of the most proud moments of your career and like a major launch, very exciting project.

[00:43:40] I’m kind of curious to talk about the career parts of it. So where were you in your career at this point? And maybe you can talk about how it grew, um, as you worked on these projects.

Bobby:

[00:43:49] Sure. So I think when I started, I don’t know if Mozilla had levels. Um, I certainly wasn’t aware of them that they existed.

[00:43:59] Uh, it was a culture of choose your own title. Uh, the title that I chose for myself was negative Entropy. Uh, that was sort of what I wanted to do on this incredibly complex and gnarly code base. Uh, as a fun fact, my favorite intern, uh, made his title Entropy. Um, but we were really on the same side. Uh, I think by the time we were shipping Firefox, quantum Mozilla had developed, I would say a more industry standard, um, uh, career progression.

[00:44:27] And so, you know, you had, you come in as you know, just. Title of engineer and then you’ve got senior staff. Senior staff. At the time when I was working on quantum CSS, uh, I believe I was, um, my, I had reached the level of senior staff and upon the successful launch of Firefox Quantum, I and the engineer who led the other half of quantum quantum flow, uh, were promoted to the level of principal engineer.

[00:44:58] Um, and at the time that was, there were not very many principal engineers, you know, like probably fewer than five. Um, and so that was, um, a pretty significant jump. But my long-term dream was to be like Boris Seki. And Boris Seki was one of Mozilla’s three distinguished engineers. And so that was really what I had my sights on in terms of the level of impact that I wanted to have and the way that I really aimed at having this impact.

[00:45:29] Was by trying to contribute to as many parts of the code as possible and just be prolific. And so after, um, working on quantum DSS, I went and worked on web render and I worked on mobile and multi-process and layout and all sorts of different parts of the, uh, of the code. And I remember my manager at the time, Joe Hildebrand, who ran engineering, told me that he wanted me to spend one day a week when I didn’t open my terminal.

[00:46:04] And I was just shocked. I was like, with what are you, what are you asking me to do here? Right? You’re asking me to not work for an entire day. And he was encouraging me to start thinking about it in the impact that I could have in a much broader way as opposed to direct contributions to the code. And so this was something that I started to think about, but it was really not the natural way that I thought to work.

Ryan:

[00:46:27] When you talk about the individual con contributions, ‘cause you mentioned that was your way of having a lot of impact, do you have a way of thinking about which contributions are more impactful than others?

Bobby:

[00:46:39] I was very much motivated to work on whatever felt like the biggest problem. And so that was early on, that felt like the dom bindings and XP connect and all the security stuff.

[00:46:50] And then at some point it was the media playback to solve the YouTube problem. And then it was multi-process and then it was this, uh, rest and serve OCSS stuff. And after that I thought that web render, which was the new graphics I backend that we were uplifting from, uh, servo. So I went and worked on that then mobile.

[00:47:10] So I was always drawn, I think, to what felt like the most pressing problem and my model of how to have impact on that was to jump in and learn all of the code and the most pressing problem and. Help work on it. And not just necessarily typing all of the code myself, but working with the other leaders in those areas on figuring out what the right things to do would be.

[00:47:35] And reviewing code. And setting direction, and setting priorities. So there were aspects of leadership, but it was all very much oriented around the code that needed the most help.

Ryan:

[00:47:44] So you were prolific, but it was a guided search specifically on the biggest problems for the organization.

Bobby:

[00:47:52] That was how I thought about it, yes.

00:47:54 — Should you focus on promos
Ryan:

[00:47:54] One thing that I’m curious about, ‘cause in the industry when it comes to career growth, I often hear two methodologies. One is where people, they focus on the promo first and foremost, and as a byproduct you get the promo, they, you know, grow and level our skills and various other things, behaviors. And in the other school of thought, it’s ignore the promos, but focus on the behaviors, focus on the skills.

[00:48:24] And then the promos will come. I’m curious your thought between the two methodologies and which one you think is better for structuring an engineering career.

Bobby:

[00:48:34] I have pretty strong opinions about this. I am very much of the mind that is important to focus on impacts and not the title. And I think there are a number of reasons for this, but that is certainly what I look for now that I’m in a situation when I’m helping people with their careers and I’m often in the decision of, you know, figuring out, you know, who’s the right person to advance.

[00:48:59] And what I am looking for is I’m looking for the impact. And my general philosophy is that if you are having that level of impact, you don’t need to sell yourself in that way. Um, or sell yourself is not quite the right word, but. There is a particular philosophy where you want to promo hack, right? You want to pin your management chain down on what are the things that I need to do to receive this promotion?

[00:49:28] And that, just speaking frankly, is very annoying, right? Um, there are aspects to this that I think are just intuitive to how I, at least as a person, perceive things. You know, like I’m a father of kids and when my daughter asks me, like when, you know, I ask her to do something and she’s like, uh, you know, will you give me this?

[00:49:49] If I do that right? It’s, it just does not, um, land well with me. But I think that there’s also a substantive aspect to it, which is that if you are really focused on the impact. That is how you are really gonna achieve things, right? Whereas if you’re focused on checking some boxes that somebody has presented to you, then you’re in this awkward situation where it’s like, well, I did technically say that if you did this, you know, that would maybe make a case for this next level.

[00:50:16] But the way in which you did it and was very sort of focused on checking the box as opposed to having the impact. And at the end of the day, impact is what matters. And impact is what needs to be recognized and rewarded.

Ryan:

[00:50:27] One thing that I hear often, ‘cause I think this is a failure mode for engineers that are a little more soft spoken, is they’re great at writing code and landing it and having impact, but they’re a little weaker on the, you know, selling yourself or kind of marketing your work.

[00:50:46] And so that kind of bites people. And so sometimes I hear career advice that is focused on, you know, hey. Make sure you create a brag document and you share the wins when you land the thing. And, and I think a lot of those people don’t have an ulterior motive of, let me, you know, kind of connive my way into the promo.

[00:51:10] Um, but I think there is this, this real thing of promos are decided by people and there’s some value in, I guess a balance. ‘cause obviously if you were completely conniving, you say, Hey, I’m gonna talk to my manager and sell my work to him. That’s kind of not ideal. But, you know, making pulses or sharing it and thinking about the levels and stuff seems to be a good way for those, um, little quieter or less proactive engineers in structuring their career.

[00:51:43] So, you know, how would you kind of balance those two frames of thinking?

Bobby:

[00:51:47] I think there are often multiple ways to frame similar activ. But that the framing of how you think about it is going to have a big impact on how you carry it out and therefore what it actually achieves. And so I think a good example of this is this notion of that you brought up selling yourself or brag documents or something like that.

[00:52:12] I think it is important that people have visibility and visibility around the work that they’re doing. And this is just a very, like a basic fact about impact. Because if you want to have impact, you need to be connected to people who understand what are the biggest challenges, and you need to be coordinated.

[00:52:35] And you also need to make sure that people understand what you are capable of, such that they can put you in a position of having more impact. But if you think of it as I am trying to brag more about me. Versus I am trying to communicate and coordinate and create visibility for work that I think that is important.

[00:53:01] You will have very different outcomes.

Ryan:

[00:53:03] Yeah, it’s, it’s interesting ‘cause it’s, it’s subtle. I feel like you could have two people with different incentive. One goes into it saying, I’m gonna create this update. So I get visibility and the other person comes in to say, I’m gonna create this update. So the right people know the right things and they get to the same path at the end of the day.

Bobby:

[00:53:22] But it’s subtle, it’s worded slightly differently and people can tell. A lot of it is the degree to which you know, how much you make it about you versus how much you make it about other people and the work and the team. And everybody knows, you know, that the person sending the update likely had a significant hand in the work.

[00:53:44] And a very important thing to do as part of those updates is to make sure that you give, um. Visibility to other people and to thank the team and not make it so much about you. Uh, because also that is a way to work well with people, um, to have people feel like you are a, you know, humble leader and somebody that they want to work with.

[00:54:09] And that is an important part of leadership is making sure that you create recognition for other people’s contributions, um, and don’t make it all about you.

Ryan:

[00:54:17] It is an ideal world that people have impact and they get recognized exactly as much as their impact. One thing that I can imagine happening though is, you know, there’s that idiom that the squeaky wheel gets the grease.

[00:54:33] Basically, if you had a loud person that is really vying for their promo and, you know, making all aggressively trying to make the posts and, you know, constantly bothering their manager, Hey, I wanna get promoted. That oftentimes, assuming they have impact too, if they don’t have impact, then it’s not gonna, nothing’s gonna happen.

[00:54:55] But assuming if they’re also a high performer and they’re doing that compared to the high performer that’s, you know, reasonable, quiet and solid, not selfish, that actually that loud person unfortunately, I think in most organizations will get rewarded first or faster. What do you think about that?

Bobby:

[00:55:17] I think it does depend on the organization and it depends on the technical culture.

[00:55:20] Um, you know, one of the things that we try really hard to do in our, our culture is to not reward that. But I think there is a balance to be struck because my message is not, don’t be ambitious, but rather think about your ambition in terms of the impact that you want to have as opposed to the status you want to achieve.

[00:55:41] And if you have the impact and create visibility around the impact. The rest will follow. And yes, there are edge cases and there are probably some situations where, um, people lobbying for themselves will kind of grudgingly get themselves a little more consideration just because it’s top of mind. But the best kinds of conversations that I like to have with people are not conversations where people come and ask, how do I get promoted?

[00:56:08] It is, how do I grow my career and have more impact? Right? Like, am I working on the most important thing? Like what could I do to grow? What could I do to have more impact? Right? And I think that those are important conversations to have with your, um, leadership to, uh, make sure that you’re focused on the right things.

[00:56:24] ‘cause the worst and saddest thing is when somebody is just working so hard at something that is just not that important and not gonna have the type of impact that they ultimately want to do. And they might do a great job at it, but it’s just. Not the right thing. And so I do think that some coordination of like, this is the type of impact that I want to have and not everybody wants to have that kind of impact.

[00:56:44] And making it known that you wanna have that impact and you’re looking for swings at the bat and you’re looking for opportunities to do more, I think that that is helpful. But trying to pin people down of like, what are the boxes that I can check? And you know, I did this like, are you good to promote me now is just honestly extremely annoying from my perspective.

[00:57:03] Uh, and I just think zooming out at a level of life, you don’t want the people in leadership to find you to be annoying.

00:57:14 — Distinguished promo rejection
Ryan:

[00:57:14] So in your case, you were focusing on impact. You had these role models of these des that you wanted to be like, and I’m kind of curious what eventually did the growth look like and how did your impact grow?

Bobby:

[00:57:28] I was really focused on continuing to work on like what was the hardest and gnarliest challenge in the browser and moving on from team to team. That was really the model that I had in my head. And I did have in my head this idea that I eventually, you know, wanted to have the level of impact that Boris had.

[00:57:45] And I assumed that that would eventually mean, um, becoming a distinguished engineer. And then at some point, um, the CTO at the time Eric Rescorla sat me down because at this point, you know, Boris and David and this guy Robert o’ Callahan had been distinguished engineers kind of since the beginning, you know, since maybe like 2010 or something.

[00:58:05] And we hadn’t made any new ones since. And the CTO sat me down and he said, look, I wanna let you know that for the first time in, you know, almost a decade, we’re going to make some new distinguished engineers. And I thought, you should know that you’re not gonna be one of them. And this was, I think, a little bit surprising to me because I do think that, you know, I thought, and that, I think anybody at the time would say that at that time, like probably, maybe not quite Boris level, but that.

[00:58:34] In terms of knowledge of all of the Firefox code. That was something that I had more than almost to anyone else. But what he explained to me was that that was a more traditional model of distinguished engineer inside of Mozilla, but that he was looking for something different now and that he was looking for something that was more oriented around industry impact, and that was very much how he saw the world.

Ryan:

[00:59:04] The definition of impact seems to have shifted while you were thinking about your de journey and did you ever debate the definition of impact, or what was your thinking when you saw that the criteria was updated?

Bobby:

[00:59:20] Honestly, it was just kind of inspiring for me. I think there was, you know, some people were concerned that I would be upset, but I think it was more.

[00:59:25] Like, you know, you work out and you think that you’re really strong and you gotta go do some Pilates move or something. You’re like, oh my gosh, like this muscle that I have, I didn’t even know that I have. But it is extremely weak. Um, and the truth is, is that there are lots of different ways to define de and it’s what matters for an organization, right?

[00:59:41] The thing that mattered early on in Mozilla and what was the make or break for Firefox success was just the management of this incredibly complex and sprawling code base by very few people. And the thing that was needed most was a kind of prolific contributor and enabler of that. And that was the archetype of distinguished engineer at Mozilla.

[01:00:03] There are other companies where distinguished engineer means something else, right? I know that some companies generally it means you built a billion dollar business, but that is not what Mozilla is about. And what Mozilla is about is changing the world. And so the criteria for DE are really focused around that.

[01:00:22] And this was, I think, an inspiring thing for me. And I still think that I, you know, didn’t ultimately, you know, I still probably have not had the level of industry impact of some of our other distinguished engineers. Um, and so probably in the end when I got to de it was maybe a combination or a hybrid of the old and the new definitions.

[01:00:43] Um, but understanding that model of thinking about the world and that model of impact, I think was very profound for me and really oriented how, um, I directed my efforts.

01:00:56 — Examples of distinguished engs
Ryan:

[01:00:56] I’d love to hear some examples of what a de level of impact looks like. Can you talk about some of the people who have done really impressive engineering work?

Bobby:

[01:01:06] Sure. Yeah. So, um, at the time there were, you know, when we had this conversation, there were three new, uh, distinguished engineers that were. Promoted. So the first one, uh, was Martin Thompson, and Martin still is at Mozilla today. And Martin is an international standards extraordinaire in terms of the development of the technical standards that power the internet.

[01:01:32] And so his name is, you know, in the author line of protocols like HTTP two and Quick and, um, web Push. And he was heavily involved in the creation of Web RTC and Geolocation. He authored other protocols like oblivious htp, like, I don’t know, I am honestly not super familiar, but it wouldn’t surprise me if there’s really nobody else who has had that level of prolific impact on all of the core technical standards of the internet.

[01:02:07] And this isn’t just about, you know, doing some editorial work on. Making sure that all of the drafts are formatted correctly. This is about core design challenges of making these protocols better in a way that advances Mozilla’s objectives. And so similar to the situation around TLS, there were generally problems around the privacy and security and performance of the legacy HTB protocols.

[01:02:37] And by designing new ones that made it faster, while at the same time making it more private and having less metadata leaked and having fewer security issues meant that there was a business incentive for the entire industry to move onto these protocols because they were faster. And by designing ‘em that way, he managed to really increase the privacy and security of the internet.

[01:02:59] So that was one archetype. The second was Luke Wagner. Luke was. Many pe Luke was probably, if there was anyone in the world, the most single handedly responsible for the development of web assembly. So historically, people wanted to run code in browsers that was not written in JavaScript. Maybe you wanted to run AutoCAD, and they didn’t want to rewrite the entire code base in js.

[01:03:33] And the original way of doing that was through plugins, where there was this basically native binary blob that got shunted into the browser window and it was awful. Had lots of terrible security properties and bad user experience. And so we tried to move away from that. And the first idea was actually from, there was an engineer who worked on it as a side project at Lone Kai who made this tool at Mozilla called Inscription.

[01:03:57] The idea of INS scripting was we just take the c plus plus and then we compile it to some very naive, uh, JavaScript and then run the JavaScript, which technically worked, but it was extremely slow. And Luke was one of the lead engineers of the SpiderMonkey JavaScript engine and Firefox at the time. And he wanted to make this something that was actually viable.

[01:04:17] So the first thing they did was there was some back and forth of, well, how do we optimize the JavaScript engine for what, uh, m scripting is emitting? And that was obviously not a sustainable approach. But then they had this idea of ASM JS and the idea was that s scripting would output a subset of js, which would be detected by the JavaScript engine, and the JS engine would then verify that it was from this restricted subset, which was sort of a proto byte code format, and then run it in a more natively unoptimized way.

[01:04:52] But. And so this was what got the flywheel going, of people actually being able to say, Hey, we can deploy these amazing native experiences that are compiled and that they’re running in the browser. Because the ultimate goal was that we wanted basically everything on the desktop to be running in the browser or most things on the desktop to be running in the browser.

[01:05:10] And there were some stuff that just couldn’t. And that flywheel then created enough industry momentum to say, why don’t we actually create a new by code format, which was web assembly, where you could have code that was native, but that was also sandboxed and portable and running inside the browser. And this was at a time when Google was pushing a very different technology that was more akin to plugins.

[01:05:38] They had this thing called Native client or Knackle, and then they had this thing called Pinnacle. And there were a lot of very complicated industry dynamics of getting all of the browsers to get on board with this web assembly train. So Luke managed the technical pieces and the political pieces to eventually forge a browser consensus on web assembly, which has been a very transformative technology in terms of what browsers can do and even what can be done outside of browsers because web assembly was built with such great technical properties is now being used all over the place on the backend.

[01:06:07] Um, things like serverless. So, uh, this is a bunch of the work that the Byt Code Alliance is involved in. So that is another archetype of impact of the creation of web assembly. The third distinguished engineer at the time was Tim Berry, who was our codec lead. And so one major problem that Mozilla and honestly the web had back in the early days was that all of the video playback happened through proprietary plugins like Adobe Flesh.

[01:06:39] And you would think that the obvious answer, which is the obvious answer, is to. Build native video playback into the browser. But the problem was that the formats that are used to compress video are heavily patent encumbered. And there are lots of reasons for this, but it’s just the way the world works.

[01:07:00] Where in this particular space, everybody is fighting over patents. And this meant that an open source browser, like Mozilla Firefox, couldn’t ship native support for the H 2 64, uh, Kodak, which was really what was powering most of the video on the internet at the time. It was the most efficient Kodak, and that was what YouTube was using.

[01:07:24] And this was a pretty significant problem for us. And so Mozilla worked over a number of years to develop truly open and free and non-patent encumbered and royalty free codex. And. The team led by Tim first developed an audio codec called Opus, and then they worked to develop a video codec called dala.

[01:07:50] And Dala was then incorporated into AAV one, which became an industry standard, uh, video format that is now developed by the Alliance for Open Media, which is a consortium across many companies like Mozilla and Google and Apple and Netflix. And so this is basically what powers video today and a lot of that vision around what would it mean to actually develop truly patent encumbered video Codex came from tip.

[01:08:20] So those, I think, are three archetypes of the types of world changing impact that you can have as an engineering IC at a place like Mozilla.

Ryan:

[01:08:31] Yeah, the, the achievement of these engineers is absurd. I mean, you mentioned lab assembly. I mean, I think of a business like Figma as possible because of a lot of that work.

[01:08:45] Um, and that’s a tens of billions of dollars industry, or I mean, uh, uh, company just by its public market cap. And so it, the, the value that’s being created by these distinguished genders is absurd. What’s interesting to me is, I guess ‘cause it’s a more open source company, the value capture is very different.

[01:09:10] I’m curious, is that something that, I dunno, people in at Mozilla are ever not feeling great about? ‘cause they’ve created so much value, but the capture is happening by these capitalist, uh, other companies.

Bobby:

[01:09:25] Yeah, I think from Mozilla’s perspective, we don’t have shareholders, right? We’re not trying to make gobs and gobs of money.

[01:09:33] The. Mozilla mission. And what we are here to do at the end of the day is to create a better internet and one that works for people, and that’s open, accessible for all, right? And sure it is very convenient for big tech companies to have a royalty free codec for video streaming so they don’t have to pay anybody, but they totally could pay, right?

[01:09:55] What Mozilla’s angle here is to make these formats and make these changes in a way that really empowers everybody. And obviously that empower, that creates economic value for everybody. And some people capture that more than others. I think from Mozilla’s perspective, we want to be able to continue to exist, and that does mean that we have to think about revenue.

[01:10:16] And at the moment, you know, a lot of Mozilla’s revenue comes from one of the dominant advertising players on the internet, which is Google. And so we would like to change that, but it’s hard and it’s particularly hard because it’s not necessarily where our heart is, right? Our heart is around having impact on the internet.

[01:10:33] And making that better. And so it is a tension that I think does, does exist between, within Mozilla of, you know, how much to focus on one and how much to focus on the other. But I think that Mozilla at its best, you know, we have some necessary business stuff that we have to manage, but the end goal of what Mozilla is about is having this impact that benefits everyone.

01:10:54 — Advice for aspiring distinguished engs
Ryan:

[01:10:54] So then after these examples of, uh, distinguished engineers, I’m curious what advice you would give to someone who wants to become a distinguished engineer.

Bobby:

[01:11:04] In terms of one thing that I think that basically everybody can work on at whatever level they are is riding. This is a particular hobby horse for me because I think that this was an area where Mozilla and myself included, did not have a lot of developed capability.

[01:11:25] And I think it is one of the most powerful things we have this Internal memo, which is actually, you know, public on the internet, um, directed at Mozilla, uh, engineers called Writing Things Down. And one of the things that this memo does is it makes the case that writing is both about the artifact that you produce, which is useful for a coordination and wide review and getting feedback, but also useful in the process itself.

[01:11:51] And that is because the process of writing is the process of thinking and refining your ideas and articulating them. And this is just an infinite game that you can always get better at. And I think it is one of the most powerful ways to create clarity of thinking for yourself, because clarity of thinking is, in my view, one of the most important things.

[01:12:12] And you only can really get that by forcing yourself to write down your ideas. And so I suppose one, you know, pertinent or timely piece of advice is if you care about this, do not use an LLM to produce text. For you. Um, because first of all, if you’re putting your name on this thing, at least today, the lms, like it’s pretty easy to tell when somebody does that.

[01:12:38] But more importantly, you are losing the opportunity to do the thinking yourself. And that thinking that happens when you write is one of the most important types of thinking for growth.

Ryan:

[01:12:50] Do you have tips on how to write well?

Bobby:

[01:12:53] Yes. Um, I would say one of the most important things is that it doesn’t need to be any longer than what you have to say.

[01:13:06] I think I always prefer shorter documents, and I think there’s some notion where people run out of things to say, and at that point you either need to refine your ideas more or you’re just done. And it’s never useful to anybody to add fluff. And dealing with documents that are fluffy and overly overwrought is one of my least favorite things.

[01:13:37] So I think that’s one piece related to that. I think that it’s important to focus on substance rather than rhetoric, which is sort of related to fluff. But I think that some people say, oh, well I’m not uh, a native English speaker and therefore I’m never gonna be able to write as beautifully as others.

[01:13:59] And I think that’s the wrong way to think about it. Like there is some basic baseline that you need to work on in terms of articulation of the ideas, but it is not about using the most flowery words. It is about clarity of thought and clarity of thought. Once you have, it is relatively easy to express in written form if you practice.

01:14:40 — AI browser wars
Ryan:

[01:14:18] Yeah, I think every single person I’ve ever asked this question to has always said. Be concise. It’s shocking to me how, uh, unanimous that advice is. Okay, so going back to the browser wars, I think we all know how things have played out, and I see that there’s this new era of browser wars that’s things are heating up.

[01:14:40] Again, there’s a lot of competition for an AI browser or bringing AI into existing browsers. And I’m kind of curious for your take on what the future of the browser wars is gonna look like as the CTO of Firefox.

Bobby:

[01:14:54] So I think one thing that’s really worth clearing up is that you hear that there’s, you know, you every month you hear about a new browser from this AA company or that, and what I think is really important to understand is that these are not browsers.

[01:15:11] As I think of browsers, these are different front ends, different window dressing and monetization keys on top of Chrome. Because much of what powers a browser is the browser engine. And browser engines are also extremely complicated and difficult to build. And there have been fewer and fewer browser engines as time goes on.

[01:15:36] And today, Firefox is the only independent browser that has no dependency on a browser engine from somebody else. So you’ve got Safari, which is pretty vertically integrated with WebKit. Nobody else really uses WebKit directly. Um, then you’ve got Firefox where we build Firefox with Gecko underneath it.

[01:15:56] And then you’ve got Chrome on top of Chromium and all these other browsers like Opera and Perplexity and even Edge, uh, they all use Chromium under the hood because what they’re seeking to do is not necessarily to evolve the web platform and the web experience. They are trying to control the touchpoint with the consumer in this world that is coming with AI because on desktop.

[01:16:22] The way consumers experience the internet is through their browser and everybody is jockeying over what this experience is going to look like and people want to control that experience. So I’m very much of the opinion that AI is coming to consumer technology, like water running downhill, and that this is not something that is going to be stopped or reversed because there is so much disruptive potential of the technology.

[01:16:52] But where that water goes and how it ends up, it can end up over here in somebody’s reservoir, or it can end up in the ocean, or it can end up as a river. There are lots of opportunities now to steer how it plays out, and there is also a lot of desire for people to capture it for themselves. And Chrome, as an example, is making a very aggressive play to control the AI stock by leveraging its dominance in Chrome.

[01:17:21] They’re doing this at multiple levels. They’re obviously doing it as part of the Chrome browser where there’s 5,000 different integrations with Gemini as part of Chrome now, but they’re also doing it as part of the web platform. They are advancing some proprietary APIs that we do not support to allow websites to have local to access to an LLM inside of the browser.

[01:17:47] And this is attractive to web authors because it allows you to offload your compute and you don’t have to pay for the inference and you can just ask the browser to do the inference. But the thing that is different about this from other web standards is that there is no way to specify an LLM or to have it have deterministic behavior that is interoperable.

[01:18:07] And so the API calls that you have into this LLM are fundamentally unspecified, but as the owner of the world’s dominant web browser. They have a lot of market power to get websites to tune their usage of the LLM to what Gemini expects. And there is obviously a co-evolution of AI experiences and the models underneath them.

[01:18:38] And creating a world where more and more AI experiences are built on top of Gemini is part of Google’s strategy to achieve and dominate control of the space. And we at Mozilla are not building our own foundation model. We don’t have any particular horse in the race. But what we are trying to do is to make sure that the space remains open and the web, that the way that the web has been open and that users have choice of how they integrate with these things and which ones they use.

[01:19:06] And also that the web remains important in relevance because there is a big risk that the web becomes a backend detail that’s used by rag from your chat GPT query, or that’s used by operator on the backend where it is. No longer the focal point of the user’s experience, but if this were to happen, there would be much that would be lost because the web is a very unique system in the sense that it provides users, agency, and control that they would not necessarily achieve elsewhere.

[01:19:35] Right. It is not a direct experience that is produced and delivered in a way that can’t be modified. It is re interpretable content that the browser can modify and render as the user chooses. Right? And there are lots of ways that this matters in practice. You know, things like ad blockers are a great example of how the re interpretable nature of the web allows users to control their experiences in important ways, and that the web is a safe environment where it’s safe to open a link even from an untrusted source.

[01:20:11] And that all of this is not created and controlled by any one company, but that it is built as an interoperable system where anybody who produces code that implements the right protocols can show up and be part of the system. And this leads to a multi-stakeholder environment where no single entity controls the evolution of the web platform.

[01:20:32] And that is not how most platforms happen, right? It’s not how the platforms happen before the web. And it’s not how, you know, the native mobile platforms happen after the web. It is in some sense a very historical accident that we got something that is this well aligned with the vision that Mozilla has for how the internet should work.

[01:20:50] And it’s very important to us to make sure that the changes that happen with AI do not sacrifice these properties.

Ryan:

[01:20:58] You mentioned all the components of the browser and there’s the web engine and you know, a lot of those AI browsers and um, like, and also other ones like opera, et. They’re actually built on chromium at the end.

[01:21:12] I’m curious, what, what do you think would happen if Firefox was built on chromium? Like what is the advantage of Firefox building its own, uh, web engine? So,

Bobby:

[01:21:24] it’s a lot of work and we like doing hard things, but the strategic advantage from the perspective of Mozilla’s mission is that it gives Mozilla a seat at the table when web standards and the future of the web is decided.

[01:21:38] And it used to be the case that standards bodies were wide groups of many different vendors. You know, you had opera back in there with its own engine. You had Internet Explorer, you had Safari, you had Mozilla. And as time has gone on, engines have dropped off the map because if you look at it from a bottom line perspective, there’s basically no justification for doing it.

[01:21:59] It is a giant cost center, um, from business perspective, but from a mission perspective, the benefits of. Being part of the conversations that shape the web are profound, and that is why Mozilla is the last independent player that is doing it. Because we are not driven by that bottom line, we’re driven by the impact.

[01:22:19] And so imagine if there was a world where there was no Firefox at the standards table, you would have Apple running web kit and you would have Google in charge of everything else. And Apple and Google very, um, capable and innovative companies do not get along particularly well and are very entrenched in their own interests and in a bilateral environment.

[01:22:46] As you can even see in the mobile space, there is a sense of entrenchment that can prevent progress. And one unique thing that Mozilla brings to the table, even though we have relatively small, small market share compared to these other browsers, is that we bring a fresh perspective and the ability to.

[01:23:06] Tilt the conversation back towards what is best for the user and what is best for the web. One example that I’m particularly proud of is not necessarily one of web standards discussions per se. These happen all the time in working groups all over the, you know, uh, editor of the HT HTML specification is a Mozilla employee who works with everybody and continuing to refine, um, HTML.

[01:23:33] But the example that I would go to is actually one about performance. So it’s long been the case that competition is what drives the advancement of browsers getting faster, and it is just this amazing achievement that browsers continually get faster, right? It’s like the semiconductor supply chain. It’s something that people don’t even think about.

[01:23:56] And just like every year the stuff underneath that is powering all the experiences getting faster and faster. And the thing, if you look at the history, the thing that makes browsers get faster is competition from other browsers. And the way this has historically been measured is the different browsers would produce a benchmark that they would design in a way that was, you know, particularly well suited for their engine.

[01:24:20] And then they would optimize it. And then other browsers would say, well, yes, that’s your private cook benchmark. And there was an initiative a couple years ago around this benchmark called speedometer three to try and produce a shared benchmark that we could all agree on that would be representative, not of just what worked well in any particular browser, but would be representative of the web and the experiences that we wanted to get faster.

[01:24:45] And this is a type of engagement where if you just have the bilateral relationship between Google and Apple would predictably go nowhere because there is just too, there are too many opportunities. For somebody to tilt it in their own interests in a way that the other side says, aha, I see what you’re doing there.

[01:25:05] But I think that Mozilla’s involvement was really critical in keeping everybody focused on the stated mission of the operation, which was not to make any particular browser look good, but to provide us a shared incentive to make browser engines faster together in order to make the web faster. And in Firefox.

[01:25:28] The impact has been pretty incredible, uh, of what the, of what has been driven by this benchmark over the last couple years. I think that really across all of the browsers, at least Firefox and Chrome, both Firefox and Chrome have improved their score on the benchmark by. A factor of two. So we’ve gotten twice as fast and the, we have actually measured in Firefox the impact that this has translated to on real world performance, on the same machines in terms of page load, um, and time to first paint and all these things.

[01:26:13] And it’s on the order of 30%. So I think it is reasonable to say that having this benchmark has made the web 30% faster. And that is something that benefits everyone and I don’t think it’s something that would’ve happened without Mozilla in the room.

01:26:32 — Biggest technical regret
Ryan:

[01:26:27] Coming to the end of the interview, I just wanna ask you a few questions kind of reflecting over your career.

[01:26:32] ‘cause I feel like you have a lot of experience when you look back on your career and you know, you made a lot of contributions. You were an IC through and through for almost all of your time at Mozilla. I’m curious, is there any technical decision that in hindsight, you wish you’d change?

Bobby:

[01:26:49] One thing that comes to mind is a situation.

[01:26:53] I think the outcome, the technical outcome was good, but I think in some sense the process wasn’t worth it. And this was around web render, which was the graphics backend in Servo when I was working on quantum CSS to take the Servo CSS engine and put it in Firefox. I was very excited about the momentum of uplifting other parts of the rendering pipeline of Servo into Firefox.

[01:27:22] And I advocated very heavily that the graphics team should replace its rendering and ization pipeline with the one from Servo. And this was not based on technical expertise on my part around it. It was very much a vibes thing of this is where it’s going. And that vibes thing was infectious. And I was not necessarily strictly in a decision making point at this time, but there were.

[01:27:51] I think that point of view really caught on, um, with management. And I remember there was, uh, the, the basic issue was that the team, many engineers on the team had very strong doubts about this. They thought that it was not ready, that it was too much, um, that it was a very risky project. And they tried to express some of these concerns.

[01:28:11] And there was a engineering leader at the time who heard them and responded with c plus plus is not the future. And that vibes based enthusiasm for a risky technical direction over the concerns of the people who knew it the best, ended up being very toxic. And a number of our most senior and most impactful graphics engineers ended up leaving.

[01:28:40] Now the rest of the team ended up rallying and web render did turn out to be a major and difficult and expensive and many year project. The actual technical. Awesome. It is a fantastic, uh, engine and it is really performant and safe and does all these great things and I’m really proud of the team for what they built.

[01:29:00] But I think that pushing it on the team when the team wasn’t ready and wasn’t aligned on it, had collateral damage that I regret.

01:29:11 — Book that impacted his career most
Ryan:

[01:29:11] Is there a top book that made an impact on your career?

Bobby:

[01:29:14] I would consider myself to be an avid reader, but the truth is, um, I don’t read a lot of books. Uh, I do read some, but honestly, you know, the, the books that I can think of that probably have had the most profound impact on my thinking are not books that I’ve actually read.

[01:29:32] Uh, and that’s just a personal style of mine. Uh, I tend to be very wide in terms of what I consume and reading a whole book on a topic is a depth first approach, and I certainly wouldn’t want anybody to take This is encouragement not to read books. But, uh, and I think that there’s a lot of value that can be gained from that and it’s something that many people do and do very successfully, but it’s not the only way.

[01:30:00] I think, you know, there was this book that I just read a book review of called Good, good Strategy, bad Strategy, and I just read three pages and that has just stuck with me as a description of like, what is wrong of many strategy doc? What is wrong with many strategy documents that I read? Um, just a very clear and crisp articulation of the muddled that gets created and what the right thing looks like.

[01:30:24] And that’s something I never actually read the book. I just read a three page summary. Um, other, I think ideas that have had a profound impact on me from books this book turned the ship around, which I also haven’t read, which is about empowering teams On the subject we just discussed, um, innovator’s Dilemma, Clayton Christensen.

[01:30:41] I think it’s very powerful analysis of how the industry works. I definitely do like to consume content from a lot of. Different areas. I really encourage people to look wide, not just within tech. Within tech. You know, I, I do really appreciate Ben Thompson’s writing I think is really good, um, for understanding the tech industry.

[01:31:05] But I like to also spend a lot of time consuming, uh, writing from other intellectual disciplines. One example is I’ve found that the whole geopolitics, national security, um, space is an area where there’s actually a lot of thoughtful writing that I had never been exposed to. And there are people who basically spend their lives really thinking about what happens on a battlefield and what goes well and what doesn’t.

[01:31:37] And a lot of those ideas actually translate very similarly, or, you know, it certainly rhymes with situations. Um, you know, been battles between big tech and how do you manage and motivate teams. And so I would definitely encourage people to take a wide view of the thought that is out there because there are many things that can be learned, uh, from things that are outside of just tech and business.

01:32:09 — Advice for his younger self
Ryan:

[01:32:09] Last question for you is, if you could give yourself some advice when you had just entered the industry, is there anything you’d say, knowing everything you know now

Bobby:

[01:32:17] at the end of the day, to be humble is the most important. I think that I had a particular attitude, not strictly about myself, but about engineering and the role of engineers and how important engineers were.

[01:32:32] And there was definitely this attitude of, that was the center of the universe. And as I’ve gone on, I’ve started to realize that there are many other important things that go. You know that I, you don’t necessarily understand when you’re first starting out at an organization of why there are certain processes and why there are certain functions and what do we need a legal team for and all these kinds of things.

[01:32:58] And as I’ve progressed and found myself more in a leadership role, I have really managed to develop an appreciation and empathy for all of the different players within the organization and within the industry. And realizing that everybody has a point of view and a place that they’re coming from and that working to understand where people are coming from is the way to make progress.

Ryan:

[01:33:29] Alright, well thank you Bobby for your time. I really appreciate it. With that being said, is there any last words you wanna say for the audience?

Bobby:

[01:33:36] Yeah, I think the most important message I wanna send is that the web very much matters. And the web is something that underpins so much of what we do. And I think for a lot of people it is invisible in something that they take for granted, right?

[01:33:54] It is like water flowing through the taps or the semiconductor supply chain of this amazing resource that continues to get better over time and continues to deliver us more value that we take for granted. But it doesn’t have to be that way, and it easily could not. And we could easily backslide into a situation of unilateral control by big tech over the experiences that people have.

[01:34:16] And I think that simply losing focus on something because we’ve had it so good for so long, would be a tragedy. And I encourage people to think about what they gain from the existence of an open and free web and to participate in trying, doing your best to keep it open. And you know, from a selfish perspective and from the perspective of the web.

[01:34:41] A great thing that you can do if you are building websites and experiences is making sure that they work in all browsers and that you don’t do the lazy path and build something that only works in Google Chrome, because that is the first step to ending us back in a situation where we were 25 years ago.