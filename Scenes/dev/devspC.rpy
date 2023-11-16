label devsp19:
    scene expression ifnight("House/backyard/bytalk.webp")
    show mc at left
    show sarena shy o3 at right
    s "I hope it's not something bad."
    mc "I..."
    s "Yes?"
    mc "I broke up with [zon]."
    show sarena shocked
    s "F-for real?!"
    mc "Yes, I've got nothing to do with her anymore."
    show sarena happy with dissolve
    pause
    show sarena shy with dissolve
    pause
    scene 024a with fade
    pause
    s "I'm so sorry for you, [mc]!"
    s "It's okay, you've made the right choice."
    s "I'm proud of you."
    s "She doesn't deserve someone like you."
    mc "I'm good, as long as I've got you in my life."
    s "Moooowh You're so sweet..."
    s "That's accurate, you're my precious, you'll see, [sn] mommy will take care of you!"
    s "You don't need any girlfriend as long as I'm here."
    "" "*gling*"
    s "Who dares to interrupt us?!"
    scene expression ifnight("House/backyard/bytalk.webp")
    show mc shy at left
    show sarena sad o3b:
        xalign 0.35
    s "Hi."
    pause
    s "Enough."
    s "I said enough."
    s "I'm the dumbest girl ever."
    pause
    s "Yes, I am."
    s "I think we need to have a serious conversation."
    show sarena mad
    s "What do you mean you're busy right now? You took the time to give me a call just to blame me again about bullshits!"
    s "Yes, I'm MAD."
    s "Yeah, good bye."
    show sarena sad o3
    s "I'm sorry [mc]."
    show mc serious
    mc "I'm really tired of this girl! She only brings you sadness!"
    s "Yeah..."
    show mc shy
    mc "You know, you're always telling me that I don't need any girlfriend as long as I've got you."
    mc "Why don't you consider the same thing for you?"
    s "..."
    show sarena happy with dissolve
    pause
    s "I'm happy to have you in my life, [mc]."
    s "I've been a coward until now. It has to stop."
    s "Thank you, [mc], for showing me how strong I can be."
    mc "I mean, you're the one that helped me get strong!"
    s "And you do it for me as well, like two soulmates haha!"
    $ slv = 19
    jump tobackyard
    return


label devsp20:
    stop music
    "" "*gling gling*"
    mc "What's that?"
    scene bgmcroom evening
    show mc ocaleconphone surprised
    mc "What's this message?!!"
    mc "It's full of insults!!!"
    mc "Who's this person?! I don't have that number saved."
    mc "Looks like someone thinks that I've stolen her girlfriend haha!"
    mc "Must be a wrong number."
    mc "Wait..."
    mc "Fucking pony?!"
    mc "Only [sn] calls me like this, it's not a common thing!"
    mc "Could it be-"
    mc "!!!"
    mc "I have to get to [sn]!!"
    scene black with fade
    "" "You're heading to [sn]'s room."
    scene bg firstfloor talk night with dissolve
    show mc surprised ocalecon:
        xalign 0.3
    show sarena sad o6:
        xalign 0.7
    pause
    mc "[sn]!!"
    s "[mc]? I was about to head to you."
    mc "Did you break up with your girlfriend?!"
    s "How do you know?"
    mc "I've received a very unpleasant message, referring to me as a pony."
    s "Oh..."
    s "I'm sorry, before the quarantine she used to ask for my phone so often..."
    s "I guess she stole your number..."
    s "She was so toxic to me..."
    s "I had to end our story."
    s "All these years..."
    s "She was trying to persuade me that I'm lesbian."
    s "She never cared about what I felt, she just hates men."
    s "She couldn't accept that I could like a man."
    s "She... she never cared for my happiness... Like you do..."
    show mc shy
    mc "[sn]!!"
    mc "It must have been tough for you!!"
    mc "I won't let you sleep alone tonight."
    show sarena happy
    s "Oh [mc]... You're reading in my mind, I was about to ask you exactly the same thing..."
    pause
    scene 024c with fade
    window hide
    pause
    window auto
    s "Don't worry, [mc], I'm okay."
    s "I will always be okay as long as you're staying with me..."
    s "You're my soulmate, you're the one that makes me feel so good and happy..."
    mc "I feel the same thing for you, [sn]."
    s "I know, I don't have any doubts about you."
    pause
    scene black with fade
    pause 1.0
    scene 024c2 with dissolve
    play music sand_castle
    pause
    e "Hm?"
    if estep <2:
        e "These two... they're so close..."
        e "Fucking [mc]."
    elif estep == 2:
        e "Damn..."
        e "These two, they're so close..."
        e "I wonder if she has sucked his cock..."
        e "No, I'm not jealous!!!"

    elif estep == 3:
        e "[mc] is with [sn] again..."
        e "I feel so jealous, why he isn't with me right now..."
        e "They look so much like a couple... I wonder if they fucked already..."
    pause
    scene bg doubleroom with fade
    show sarena o6:
        xalign 0.65
    show mc ocalecon shy:
        xalign 0.3
    mc "Have you slept well?"
    s "Well..."
    s "At first, not that much, I felt so guilty..."
    s "But, I shouldn't feel guilty anymore."
    s "Honestly..."
    show sarena happy
    s "This morning, I feel so light!"
    s "I'm realizing that all these calls, shaming, all these negative moments are gone!!"
    s "All that is left is having fun, my projects, and my pony by my sides!!"
    s "I can't be more happy than right now!"
    mc "I'm so happy to hear that!!"
    show sarena taunt
    s "Oh, well, actually there is something that could make me happier haha!"
    mc "What is it? Can I help it?"
    s "Oh yes you can... But, I'll tell you at the right moment hehehehehehe!"

    $ slv = 20


    jump passnightnothing
    return



label devsp21:
    play music sand_castle
    s "Yeaaaaaaah!"
    s "I'm having so much fun doing videos with you!!"
    scene black with dissolve
    pause 1.0
    scene 024d with dissolve
    s "Heeeey sweeties!"
    s "Today, another video with my favorite partner!"
    s "He looks so good today!"
    s "I wanna read good things about him in the commentary section!"
    s "Because..."
    s "It's an anatomy video!"
    mc "What?!"
    s "I haven't told him haha!"
    s "As you can see, my pony is so ripped!"
    s "I'm always talking to you about muscles to train or weak points on the body."
    s "I'm gonna use his body to show precisely everything, as he's very well defined."
    s "Now, [mc], remove your shirt!"
    mc "Er- Is this okay with the term of use?"
    s "Yeaaah don't worry, it's for education purpose."
    mc "Okay-"
    window hide
    scene 024e with fade
    pause
    window auto
    mcth "For an hour, [sn] explained my entire anatomy for the video, with exception of my private parts of course."
    mcth "..."
    mcth "Her delicate fingers..."
    mcth "She wasn't only pointing at the target of her explanations..."
    mcth "She was delicately flirting with my skin..."
    mcth "I'm having chills all over my body..."
    mcth "Oh shit, my nipples are getting hard!!!"
    mcth "I hope no one notices!!"
    scene 024d with fade
    s "So, girls, you now have every explanation you need!"
    s "See you next time, for a very special video!"
    mc "A special video?"
    s "Poor [mc], he's never aware of my plans haha!"
    s "See y'a!"
    "" "[sn] cuts down the recording"
    scene balconybgsass
    show ass sarena 1
    pause
    mc "[sn]!!"
    show 024d2
    mc "The feeling of your hand on my skin... It's driving me insane!"
    s "Oh..."
    s "[mc]!"
    s "Your cock feels so hard..."
    s "Are you thinking of putting it in me?"
    s "I hope you do."
    s "I do."
    s "It's not because I'm now single."
    s "It all started when I first met you."
    s "I was trying to persuade myself I didn't want it."
    s "But, I remember, all of these wet dreams..."
    s "You were all mine..."
    mc "[sn]!!"
    mc "I want you right now!!"
    s "Oh... Well..."
    pause
    s "Nope!"
    mc "I'm so h- Wait what?"
    s "I said no!"
    mc "But-"
    s "Don't you remember?"
    s "Your body is mine now!"
    s "I can do whatever I want to you, or do nothing!"
    mc "But, you can't let me like this!!"
    s "Oh I can haha!"
    s "Actually, I've got important work to prepare."
    s "I don't want to cross that line right now."
    mc "So you wanna cross the line?"
    s "Hehehe you dirty pony, you sound like you're going to explode if I don't ride it!"
    s "Naughty boy!"
    mc "[sn], you're driving me crazy!"
    s "I know, that was my plan haha!"
    s "But, as I said, right now I have some work to do."
    s "I will need you tonight, I will call for you."
    mc "I'll be ready!!!!"
    pause
    s "Sometimes I don't know which one of us likes the other the most."
    mc "That's me for sure!"
    s "Don't provoke me!"
    mc "Haha!"
    pause
    $ slv = 21
    jump passtime



label devsp22:
    scene bgmcroom evening
    play music sand_castle
    show mc o1
    "" "You're heading to your bed."
    "" "*Message received*"
    show mc o1phone
    pause
    mc "What's that?"
    mc "[sn] wants me to join her on the balcony."
    mc "Is this for another video?"
    "" "*Message received*"
    mc "Hm?"
    show mc surprised
    mc "Only in my underpants?!"
    mc "I'm not sure this would be right for a video!"
    show mc base
    mc "Unless..."
    show mc shy
    mc "It's not for a video?"
    mc "Oh my [sn], is it time?"
    stop music
    scene black with fade
    pause
    play music causmic
    show 024tallimg with dissolve:
        xalign 0.5
        yalign 0.9
    pause
    mc "These boots and legs..."
    mc "What has she prepared?"
    show 024tallimg:
        linear 2.0 xalign 0.0
    pause
    mc "A sofa?! When did she have the time to place it there?!"
    mc "Right, she talked about something to prepare..."
    show 024tallimg:
        linear 2.0 xalign 0.5 yalign 0.5
    pause
    mc "Great lord..."
    mc "[sn]'s Dress looks so stunning..."
    show 024tallimg:
        linear 3.0 yalign 0.25
    pause
    mc "These massive tits!"
    mc "[sn]'s body has always been so perfect."
    mc "She makes me so hard for so long..."
    s "You can't say such words on camera you know?"
    show 024tallimg:
        linear 0.5 yalign 0.0 xzoom 1.5 yzoom 1.5
    mc "?!"
    play sound spony
    s "My pony is here!"
    s "You look so hot without your clothes you know..."
    mc "Th-thank, but, did you talk about a camera?"
    s "Sure, over here!"
    show 024tallimg:
        linear 0.5 xalign 1.0 yalign 0.65 xzoom 1 yzoom 1
    pause
    mc "?!"
    mc "What kind of video are you planning?"
    s "It's not what you think, naughty pony!"
    mc "But, it looks exactly like-"
    s "Shhhh!"
    show 024tallimg:
        linear 1.0 yalign 0.5 xalign 0.5 xzoom 0.333 yzoom 0.333
    pause
    s "And it's not a video, it's live!"
    mc "Live?! But, you told me to come half naked!"
    s "Yeah!"
    s "Today is a special livestream, I wanted to tell something to the world... And to you."
    s "Don't worry, as long as we can't see \"it\", it's alright."
    s "Now if you wish, take place on the couch."
    scene 024hug with fade
    mc "[sn], your legs, I can't move."
    s "Oh?"
    s "Too bad, you can't run away from me then..."
    s "I want the chat to hear what I'm about to say."
    s "I used to present myself as lesbian."
    s "This isn't totally true."
    s "This man-"
    s "This man is the one."
    s "He has always been the one."
    s "I will never lose him."
    s "He is the one that can make me happy."
    s "I am the one that can make him happy, I'm sure of that."
    s "He's always been my pony, that I want to cherish."
    s "I know how much he loves when I'm that close to him."
    s "I know he loves when I'm kinda possessive with him."
    s "I know he loves to be MINE."
    mc "It's true, I love to be yours!"
    mc "My life has changed after I met you!"
    mc "All I want is to keep you by my side forever!"
    mc "That's why I asked you out at that moment, because-"
    mc "I love you, [sn]!"
    pause
    s "I love you too, [mc]."
    s "More than you imagine."
    s "And more than you!"
    mc "Ah that's impo-"
    play sex skiss
    window hide
    scene 024fkiss with hpunch
    pause
    window auto
    s "I love you, I love you so much!!!"
    s "I lied to myself for so long!"
    s "All I want is you!!"
    s "Your tongue is mine!"
    s "Your body is mine!"
    s "Your soul is mine!!"
    s "And also..."
    s "Your cock, is mine."
    s "Now, it's time to shut down the live stream."
    stop sex
    scene black with dissolve
    scene slv3bg
    show mc shy ocalecon at left
    show sarena ofinal at center
    show black
    pause 0.1
    hide black with dissolve
    pause
    s "Hehehe they are so cute!"
    s "They all were begging me to see the next part!"
    show sarena taunt:
        linear 1.0 xalign 0.4
    s "But, I can't, because it doesn't follow the terms of use..."
    mc "[sn], I want to ask you something..."
    s "Yes?"
    mcth "[sn] seems to want us to become a couple."
    if bstep > 1:
        mcth "I promised [bn] to be her good boy, she would never accept that!!"
    if estep > 1:
        mcth "I'm having a relationship that I enjoy with [en], do I have to end it?"
    if vstep > 1:
        mcth "I have not finished getting revenge on [vn]! But, if I get in a relationship with [sn] I have to stop."
    mc "Do you want us to be, like, in a couple relationship?"
    show sarena shy
    s "What? Not at all!"
    show mc surprised
    mc "No?"
    mc "But, what you just said earlier-"
    s "I'm thinking every word, but, there is no question of that type of relationship!"
    show mc shy
    mc "I'm... A bit lost."
    show sarena sad
    s "I get it."
    s "Couple relationships like this... Always has an end."
    s "It's as if we get roles of boyfriend or girlfriend and then someone has to end it."
    s "I don't want our relationship to end, ever."
    s "We are already perfect as we are."
    show sarena happy:
        linear 0.5 xalign 0.3
    s "I will keep being your [ssn] and I will never abandon you."
    s "We will continue to live and get old together, as soulmates."
    mc "But-"
    show sarena taunt:
        linear 1.0 xalign 0.25
    s "So you're thinking about what if you find a girlfriend?"

    s "Oh you can, there are just a few conditions."
    s "If she wants to be with you, she has to accept that... I will fuck with her boyfriend every-single-day."
    s "She has to accept that she will never make you cum as good as I do."
    s "She has to accept that I'm the most important person in your life."
    mc "But, who would accept such things?"
    s "Are you saying I won't be enough for you?"
    mc "No! Haha! You're perfect!"
    s "And as I love women's bodies, if she wants we could... Play together, you know."
    mc "You mean, me, my potential girlfriend, and you?"
    s "Yeah! But, I'm warning you, I will never lose against any other women when it comes to making you cum."
    pause
    show sarena shy
    pause
    s "It makes me wonder, I also have a question for you."
    mc "Yes?"
    s "You said it multiple times but, I want to be sure."
    s "You're a virgin right?"

    if virginitylossby == "Berry":
        mcth "I can't tell her [bn] took it from me! But, at the same time, I can't lie to her..."

    if virginitylossby == "Emma":
        mcth "I can't tell her [en] took it from me! But, at the same time, I can't lie to her..."

    if virginitylossby == "Valerie":
        mcth "I can't tell her [vn] took it from me! But, at the same time, I can't lie to her..."
    if virginitylossby == "None":
        mc "Of course I am!"
        s "Then, I'll be proud to be your first."
    elif True:
        mc "No, not anymore."
        show sarena shocked:
            linear 0.5 xalign 0.4
        s "What?!! Who Did that?!"
        s "Tell me!! Who took my pony's virginity!"
        mcth "Arh shit it's too late, I have to say it now..."

        if virginitylossby == "Berry":
            mc "[bn]..."
            show sarena shocked at angryjump
            s "My mom?!!"
            show sarena sad
            s "It's true..."
            s "You've always had a very special relationship..."
            s "I guess she was quicker than me..."
            show sarena challenge
            s "All that time she was preparing her attack!"
            s "I will have to have a discussion with her!"
            s "However, virgin or not..."
        if virginitylossby == "Emma":
            mc "[en]..."
            show sarena shocked at angryjump
            s "My sister?!!"
            s "Aren't you supposed to have a cold relationship?!"
            show sarena sad
            pause
            s "So she liked you in secret."
            s "I think I knew it."
            s "It was obvious, her attention was all the time focused on you."
            s "She was faster than me."
            s "I'm gonna need a discussion with her."
            show sarena challenge
            s "However, virgin or not..."

        if virginitylossby == "Valerie":
            mc "[vn]..."
            show sarena happy
            s "Ahahaha, stop kidding, who is she seriously?"
            mc "I'm not joking."
            show sarena shocked at angryjump
            s "HER?!!"
            s "How in the world?!"
            pause
            show sarena taunt
            s "Is it like a silly plan to take your revenge on her?"
            s "I could understand, but, to the point of giving her your first time..."
            s "I wonder if you liked it..."
            s "I'm gonna need a talk with her."
            s "But, for now..."

    show sarena taunt ofinal2 with dissolve

    s "I'm about to ride your cock like a demon!"
    s "I've been craving for you for so long! I won't hold back!!"
    s "It's time for me to ride my pony!"
    pause
    scene black with fade
    stop music
    pause
    mc "..."
    pause
    mc "Uh!"
    pause
    s "Ah!"
    s "Oh gosh it's so big..."
    window hide
    show 024frid 1 with dissolve:
        xalign 0.6
        yalign 0.5
        xzoom 3
        yzoom 3
    pause
    window auto
    mc "It doesn't want to let it in!"
    mc "You're too tight!"
    s "There is no way I'm putting my hand down on it!"
    s "I just have to force a bit on it!"
    show 024frid:
        linear 2.0 xalign 0.4 yalign 0.35
    pause
    s "I..."
    show 024frid 2:
        linear 1.0 yalign 0.4
    pause
    s "Oh fuck!!"
    s "It's only halfway!!"
    s "This is such a monster cock!"
    s "I feel like my pussy is about to break!!"
    s "This isn't enough, I want it all the way in!"

    show 024frid 3:
        linear 1.0 yalign 0.45
    pause
    mc "Oh [sn]!!"
    s "I can feel it pushing on the bottom of my womb!!"
    s "This is incredible!!"
    s "[mc]'s cock is incredible!!!"
    show 024frid 1:
        linear 1.0 xzoom 1 yzoom 1
    pause
    s "Outch!"
    s "I feel like, if I want to be able to continue, I have to train!"
    s "There is no other solution, from now on, I have to ride you every day!!"
    window hide
    stop music
    scene 024bgfride
    show 024s3v1
    pause 0.2
    play sex ssoftmoans2
    play sexfx sex20
    pause
    window auto
    mc "Oh my god, [sn]!!!"
    if virginitylossby == "None":
        mcth "So that's the feeling of a real pussy!"
        mcth "this is so intense!"
        mcth "It's so tight, I don't know if it hurts or if it feels good as hell!!"
    s "It's so much harder than I thought!!"
    s "But, at the same time, so good!!"
    s "It's as if I'm letting your soul enter me!"
    s "My vagina is sucking it out from you!"
    s "I will take out your soul and make it mine!!"
    window hide
    hide 024s3v1
    show 024s3v2
    pause 0.2
    play sex shardmoans1
    play sexfx sex10
    pause
    window auto
    mc "Oh [sn]!!"
    s "[mc]!"
    s "I can do better!!"
    mc "This is already so intense!!"
    s "I wanna make you lose your mind!"
    s "I want to be the one that fuck you the best!!"
    window hide
    hide 024s3v2
    show 024s3v3
    pause 0.2
    play sex shardmoans2ample
    play sexfx sex05

    pause
    window auto
    mc "Aaarh!!"
    s "[mc]!!!"
    s "Your cock is driving me crazy!!!"
    s "I can't stop my moves!!"
    s "My hips are taking control over me!!"
    s "All I want is fucking your cock !!"
    s "However- Aaaah!!"
    s "I feel like I'm about to-"
    s "With me, [mc]!!"
    mc "Inside of you?!"
    s "Yes!!"
    s "I want to feel your soul flowing inside of me!!!"
    mc "Haaa You're too intense I can't hold it anymore!!!"
    s "Give it to meeeeee!!!!"
    window hide
    stop sexfx
    stop sex
    play sound scum1
    hide 024s3v3
    show 024s3cuma
    show 024s3cumb
    show cumsfxrep:
        xalign 0.62
        yalign 0.45
    play audio cumexplo
    pause 0.1
    play audio cumsound

    pause
    window auto
    s "Haaaahhh!!!"
    mc "Haaaaah!!!"
    s "I'm cumming! I'm cumming all around your shaft!!!"
    s "I never came like that!!!"
    s "You're all I need!!!"
    pause
    scene 024top with fade
    window hide


    pause
    window auto
    s "Eh... eh..."
    mc "Oh [sn]..."
    mc "You look like a real goddess..."
    s "Really? Then I'm expecting you to praise me everyday from now on haha!"
    s "Aaah!"
    s "I knew I'd love to feel you inside of me, but, I didn't know I could feel... That level of intensity..."
    s "Rhah my pony..."
    s "I will fuck you soo bad from now on..."
    s "No one else will make you cum as I do."
    s "Alright, let's continue."
    mc "Continue?!"
    s "Yes, I have to get used to your cock's size, I won't if I don't train intensely!"
    s "Don't worry I won't kill you, but, we gonna keep fucking until you don't have any drop of cum in these balls."
    s "And I'm not asking, you're mine now."
    mc "I'm all yours!!"
    pause
    scene black with fade
    pause
    "" "And then, [sn] kept fucking you."
    "" "After a moment you weren't even able to move a finger anymore."
    "" "She told you that it's okay, you don't have to, and then she continued."
    "" "The next morning."
    pause
    s "[mc]!"
    s "[mc]!!!"
    s "This is an emergency!!!"
    s "Oh come on wake-up!"
    play music robot_boogie
    scene slv3bg2 with dissolve
    show mc ocalecon at left
    show sarena ofinal2 shocked at center
    pause
    mc "Hello my goddess."
    s "This isn't the right time!!!"
    s "I did not shut down the live stream yesterday!!!"
    mc "Oh well that's not-"
    show mc surprised
    mc "Oh don't tell me that-"
    show sarena:
        linear 0.5 xalign 0.5
    s "I've been banned!!!"
    s "They saw EVERYTHING!!"
    mc "Oh no, all the work you've made!!"
    s "There is worse."
    mc "What?!"
    s "I have to tell you something..."
    mc "What? What?"
    show sarena shy
    s "You... You just became a pornstar... as well as me..."
    mc "Ah?!"
    show sarena shocked
    s "Someone uploaded the video on this pornsite!!"
    mc "Oh my god!!!"
    show sarena at angryjump
    s "It has made 3 million views!!"
    show mc at angryjump
    mc "How much?!"
    s "Comments are... From my followers that came here to see it again and again!"
    s "I've received hundreds of messages from my followers!"
    s "They loved it as fuck!"
    show sarena shy
    s "Also... The uploader also contacted me..."
    s "She called herself my number one fan and loved our... Livestream."
    s "She is willing to give me access to the account, under the condition that we continue to make love content..."
    s "What do you think of it?"
    show mc shy
    mc "You don't look that afraid of that idea, right?"
    s "Hm... I mean, I never dreamed to become a pornstar..."
    s "However, if it's just about the two of us..."
    s "Like, we could show them... Our love... Show the girls they're far from beating me if they want to get you."
    mc "[sn], you're crazy..."
    s "Am I?"
    show mc base
    mc "But, I love that! Haha!"
    mc "I think this could work, a porn channel but, with just the two of us."
    show sarena happy at angryjump
    s "Oh [mc] I'm so happy you're taking it this way!!"
    s "I've got a lot of girls eager to see more of us haha!"
    s "They can see, but, only me can touch ahaha!"
    mcth "Did she planned all of it? Hm... Whatever."
    s "You're making me so happy, [mc]... I love you so much!!"
    mc "I love you too [sn]!"
    "" "All events have been upgraded to Step 3!"
    pause
    call incrskill ("cockskill", 3) from _call_incrskill_87
    call incrdesire ("Sarena", 50) from _call_incrdesire_81
    scene black with fade
    pause
    $ cumbys += 5
    $ scum += 5
    show levelupf with dissolve
    play audio bmiam
    pause
    hide levelupf with dissolve
    pause

    if virginitylossby == "None":
        $ virginitylossby = "Sarena"
    $ slv = 22
    $ sstep = 3
    $ persistent.replay54 = True
    jump passnightnothing

layeredimage 024frid:
    always:
        "024bgfride"
    group step:
        attribute 1:
            "024s3_00001"
        attribute 2:
            "024s3_00003"
        attribute 3:
            "024s3_00009"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
