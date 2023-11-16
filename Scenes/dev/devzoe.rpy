define devzoe1ok = False
define devzoe2ok = False
define devzoe3ok = False

label devzoe1:
    scene bgmcroom evening
    play music sand_castle
    show mc o1phone
    mc "Hm..."
    mc "I'm having so much fun these days, I even forgot to make calls with my girlfriend..."
    mc "Is that a sign that... I should dump her?"
    mc "That's... Kind of obvious, in fact."
    mc "Honestly..."
    mc "All girls here are better to me than [zon]."
    mc "However, how should I proceed?"
    mc "I don't know, doing it not face to face is for cowards."
    mc "I should wait for the end of quarantine and finish it."
    mc "But what if the quarantine continues for a long time?"
    mc "Hm... I should call her and see."
    pause
    scene black with dissolve
    pause 1.0
    scene 023n with dissolve
    pause
    mc "Hey [zon]."
    zo "Hey boy, how have you been?"
    zo "You don't catch up with your GF as much as I expected!"
    zo "Are you not missing me?"
    mc "Well, I'm calling right now."
    mcth "I've been living with girls for some time already."
    mcth "It's clear to me, I don't want to be with her anymore."
    mcth "However, just doing it from a long distance... Isn't it disrespectful?"
    zo "Anyway, how's life with [en]? And the other girls?"
    mcth "Pretty good for me!"
    mcth "Every girl is awesome with me!"
    zo "I'm guessing you should be hard all day long with [en] living with you!"
    zo "Too bad you're already taken, hahaha!"
    mcth "Yeah, too bad..."
    pause
    zo "Why do you stay silent?"
    mc "To be honest, they all treat me better than my girlfriend."
    zo "That's because they're not your girlfriend."
    zo "Remember that you were a loser. You should feel lucky that someone like me chose you."
    mcth "..."
    mcth "How she just said that..."
    mcth "Clearly, I didn't realize what I was doing then."
    mcth "She was the first girl to ever show me interest, so I thought..."
    mcth "... I thought I shouldn't miss this opportunity."
    mcth "Now that I have developed a little bit more of my relationship with the girls, I can see that I deserve someone so much better than [zon]."
    mc "Yeah, I'm lucky."
    mcth "I'll just tell her what she wants. I'm gonna dump her anyway."
    mcth "I don't understand why she asked me out. She clearly doesn't like me."
    zo "Good boy."
    zo "Now, if you excuse me, I have to have dinner with my stepdad. I'm happy that you didn't forget about me."
    mc "Stepdad? Aren't you supposed to be at your uncle's place?"
    zo "Er yeah, my uncle, stepdad is just a surname."
    mcth "Hm..."
    mcth "His uncle-stepdad really has shitty tastes, look at this board behind [zon]... Who would use that as a decoration..."
    zo "See you!"
    scene bgmcroom evening
    play music sand_castle
    show mc o1phone
    pause
    mc "[zon] Never actually loved me, or even liked me."
    mc "I don't either."
    mc "I was just not realizing it because I had no good experience before that, so I thought it was normal."
    mc "I want to ask the girls what they think about my situation."

    $ devzoe1ok = True
    jump passtime
    return



label devzoe2:
    scene black
    pause 1.0
    play music storm
    pause
    scene bgmcroom evening
    show mc
    mc "Time to sleep!"
    mc "Damn, rain and storm are intense!"
    mc "It's... kind of relaxing in a way..."
    mc "Is that the so-called ASMR?!"
    mc "I feel like I'm gonna have a great sleep!"
    show mc ocalecon with dissolve
    pause
    if elv == 13:
        jump devzoe2emma

    if slv == 16:
        jump devzoe2sarena

    if blv == 13:
        jump devzoe2berry

    if vlv == 15:
        jump devzoe2valerie
    return

label devzoe2emma:
    e "hm, [mc]?"
    show mc at left
    show emma o3 shy at right
    mc "[en]?"
    e "[mc], can I sleep with you?"
    e "I don't like storms at all..."
    mc "You're still a little girl after all, haha!"
    e "Oh, come on! I swear I'll be a good girl. Please."
    mc "It's asked so kindly, I can't refuse."
    scene black with fade
    pause
    scene 023a with dissolve
    pause
    e "Rrrh...."
    mc "Do you feel better?"
    e "Yeah... I feel so good with you..."
    mc "Oh my!! That's so sweet!"
    mc "Do you realize what you just said to me? Haha!"
    e "Shut up! I mean it."
    e "You're still a loser, but at least a loser that makes me feel good."
    pause
    mc "I wanted to ask you, what do you think of [zon]?"
    e "Hm..."
    e "I think she's a bitch, the way she treats you."
    e "Don't get me wrong, you're still a loser but deserve love."
    e "I mean, like anyone deserves it. Not because I like you."
    mc "Thanks, [en], I appreciate it."
    e "I don't know why you accepted."
    e "You already had my sister and my mom."
    e "I know how much you like [sn], and it goes both ways."
    e "And my mom... She was giving you so much attention..."
    e "You didn't need more."
    e "I don't even know why [zon] asked you out, I was so mad when she did that."
    mc "Why were you mad?"
    e "Ah? Obviously, because once again, you-"
    e "Er-"
    e "I don't remember what I wanted to say, I'm falling asleep..."
    mcth "She was about to say something. I feel like she isn't ready. She needs time."
    mc "Have sweet dreams, [en]."
    e "You too [mc]!"
    e "Ah I feel so relaxed right now..."
    $ devzoe2ok = True
    $ elv = 14
    if devzoe3ok == True:
        $ elv = 15
    call incrdesire ("Emma", 10) from _call_incrdesire_60
    pause
    jump passnightnothing
    return

label devzoe2sarena:
    s "[mc]!!"
    show mc surprised at left
    show sarena o4 shocked at right
    mc "[sn]?! What happened?!"
    s "[mc], sleep with me!!"
    show mc shy
    mc "Wh-what?!"
    s "I'm so terrified by the thunder!!"
    mc "Oh! Sure!"
    s "I know I'm a strong woman and all, but, I don't know I feel terrified!!"
    mc "What can I do to make you feel better?"
    s "I know EXACTLY how!"
    scene black with fade
    pause
    scene 023c with dissolve
    pause
    s "Aaaah... Perfect <3"
    s "This is definitely my favorite position..."
    s "I love so much feeling your breath between my tits..."
    s "I feel so close to you..."
    s "I feel so much safer with you..."
    mc "MMmh!!"
    s "Oh I'm sorry, I'm suffocating you with my huge tits hehehe!"
    s "Oooh, you're already so hard for me..."
    mc "I'm sorry [sn], I just-"
    s "You just love when I'm on you like this!"
    s "Don't worry, I'm used to feeling you hard for me when I sit on you for many years already."
    s "I like that, because-"
    s "You've always respected me, you never tried to cross the limits."
    s "I feel like you'd never hurt me in any way and always respect my boundaries."
    s "I feel guilty sometimes because I think I'm not respecting your boundaries as much as you do."
    s "If I ever do something you want me to stop, I hope you gonna tell me, alright?"
    mc "I will do, but I trust you, you can do anything you want to me!"
    s "Hehehe you're a naughty boooooy! Don't tell me things like that or I will devour your soul, hahaha!"
    pause
    mc "Hm, I wanted to ask you, what do you think of [zon]?"
    s "[zon]?!"
    s "I HATE her."
    s "She stole you from me!"
    s "I mean, you were not my boyfriend but-"
    s "I noticed you spent a bit less time with me."
    s "I don't understand why you accepted."
    s "I am here to give you all the affection you need."
    s "Even mom is here for you, and I know how strong your relationship is."
    s "You deserve so much better, you deserve to feel what it's like to be loved."
    s "I don't see you being with her for a long time at all."
    s "I don't want your next girlfriend to impact our relationship."
    s "I want to stay that close to you forever..."
    pause
    mcth "[sn] is a real treasure."
    mc "But, can't I say the same thing for you and your girlfriend?"
    s "I-"
    pause
    s "Yes, you can say the same thing, you're right."
    $ devzoe2ok = True
    $ slv = 17
    if devzoe3ok == True:
        $ slv = 18
    call incrdesire ("Sarena", 10) from _call_incrdesire_61
    pause
    jump passnightnothing
    return

label devzoe2berry:
    b "[mc]..."
    show mc surprised at left
    show berry o4 shy at right
    mc "[bn]?"
    b "My poor dear!"
    mc "?!"
    b "You have to be so frightened by the storm!"
    mc "No, I'm not."
    b "Ooh you don't have to play the alpha with me!"
    b "You need someone to cuddle you and make you feel safe."
    b "I will always be here to take care of you."
    mcth "I'm really not affected by the storm..."
    mcth "However, it sounds like an excuse to give me affection, which I would not refuse!!"
    show mc
    mc "Er yeah, I need you [bn]!"
    show berry lewd
    b "Oooh my sweety! I knew my good boy would need me!!"
    b "Come here, I know exactly what you need to feel better..."
    scene black with fade
    pause
    scene 023d with dissolve
    pause
    b "Oh yeah, right there..."
    b "You can't live without your daily [bn]'s nipples, am I right?"
    b "You love them so much..."
    b "I love so much to see you sucking on it..."
    b "You look like a baby!"
    mc "Eh! I'm not!!"
    b "I know hahaha I was just teasing you!"
    b "You're a grown man!"
    b "But please, stay a good boy when you're with me..."
    b "I love when you're just innocent, doing anything I tell you."
    b "I love to feel that you need me..."
    b "...That you give me control over you, so I can be sure you get the best of the best..."
    b "I wanna cherish you, more than any woman would do."
    b "In exchange, just stay as you are, a good boy that follows anything I say, so I can make your life perfect."
    mc "You're the first woman that ever cared for me, I would do anything for you."
    b "Perfect."
    pause
    mc "Hm... I wanted to ask you..."
    b "Yes?"
    mc "What do you think of [zon]?"
    b "That bitc-, I mean that naughty girl?"
    b "I think..."
    b "I think we're close enough, I can be honest."
    b "I don't want to see you with her, ever again."
    b "Since when a girl like her can touch a boy like you?!!"
    b "I won't tolerate it anymore."
    b "If you need love, if you need affection-"
    b "If you need a woman to take care of your body-"
    b "I'm here now, so you don't need her anymore."
    b "She doesn't love you."
    b "I remember that time, I needed to talk with her, before she got to ask you out."
    b "I told her everything she deserved to hear."
    b "She's a bitch, she will fail her exams, she will never be loved by anyone."
    b "She will die like a little shit in the streets."
    b "I shouldn't have said that as a teacher... However, NOBODY touches my candy."
    b "Sometimes I wonder if she asked you out just to prove me wrong..."
    b "But she doesn't know you already belong to me, you've always been."
    b "Now, don't think of her anymore and just sleep."
    mc "Yes, [bn]."
    b "Good boy."
    mcth "Wait, what [bn] said just now, is it possible?"
    mcth "[zon] wanted me just to make [bn] mad?"
    mcth "Who can do such crazy sh-"
    mcth "... Yeah, that doesn't sound that wrong..."
    mcth "I can't be sure, but I don't doubt that [bn] will take care of me, and I can trust her."
    $ devzoe2ok = True
    $ blv = 14
    if devzoe3ok == True:
        $ blv = 15
    call incrdesire ("Berry", 10) from _call_incrdesire_62
    pause
    jump passnightnothing
    return

label devzoe2valerie:
    v "[mc]."
    show mc at left
    show valerie think o3 at right
    mc "Hm?"
    v "I can't sleep with this storm."
    mc "Ah."
    v "..."
    show valerie angryshy
    v "Won't you ask me if I'd like to join you?"
    mc "Nope!"
    mc "You're a grown woman, you don't need a \"boy\", do you?"
    v "Ghrrrrr!!!"
    show valerie happy
    v "Come on! I'll let you touch my body if you want."
    mc "What makes you think I wanna touch your body?"
    show valerie happy
    v "Because I'm hot!"
    v "And you can get your revenge on me."
    pause
    v "Pleaaaase I'll be adorable with you!"
    mc "Alright, alright."
    scene black with fade
    pause
    scene 023e with dissolve
    pause
    v "aaaah, that's great."
    v "I instantly feel better."
    v "A hand firmly grabbing my tits, a bulge against my ass..."
    v "Perfect."
    pause
    v "I know I've been abusive with you, in the past."
    mc "You were."
    v "I..."
    v "I apologize."
    v "You are not the useless boy I thought, or at least you changed."
    mc "You know that presenting apologies isn't enough."
    v "I know, but it's already a good start, no?"
    v "You have been playing with my body for a few moments. Doesn't it mean you accept my apologies?"
    mc "It's very little compensation."
    mc "However, you're still mean to me. So I'll need much more than what we already did."
    v "I get it."
    v "As long as I'm mean to you, you'll have to play with my body for compensation, it's understandable."
    mc "Don't lie. You like when I'm playing with your body, don't you?"
    v "Hm... Maybe. You're doing it right, so I don't mind you taking your frustrations out on me."
    v "I wish your Dad was a bit more like this. Sometimes I wish that you were mine haha!"
    mc "Are you crazy?"
    v "I'm kidding, boy!"
    v "Or do I? You will never know!"
    pause
    mc "[vn]"
    v "Hm?"
    mc "What do you think of [zon]?"
    v "Hm..."
    v "I don't know her very well, you know."
    v "All I see is that, considering how rough you're with me, she wasn't giving you what you need."
    v "From what you told last time, she gave zero effort to your couple."
    v "I think you have to find a better woman."
    v "There is [en], She's a hot girl and I bet she's craving for a good fuck."
    v "[bn], she's so intimidating to me, but at the same time I want her to step on me..."
    v "I know you like being her good boy, I kind of understand you."
    v "And [sn], holy shit, she has the body of a Goddess!"
    v "I can feel so much sexual tension between you two, I bet if you get together, you will fuck all day long!"
    v "I also wonder how skilled she is with another girl haha!"
    v "You're surrounded by so many hot girls, just find one!"
    v "Or even better, stay single and fuck tons of women!"
    mc "Why?"
    v "I can feel your lust, boy."
    v "I'm not sure a single woman could relieve it."
    v "Except for women like me! I could take any amount of lust!"
    mc "You want me to fuck you, is that what you mean?"
    v "What are you talking about, I'm taken!"
    v "Just saying that... In a fantasy world, a girl like me could fit very well with a guy like you... lewdly speaking."
    mcth "[vn]... She wants me to fuck her roughly."
    mcth "It's funny because even my biggest enemy from my childhood is sweeter with me than [zon]."
    $ devzoe2ok = True
    $ vlv = 16
    if devzoe3ok == True:
        $ vlv = 17
    call incrdesire ("Valerie", 10) from _call_incrdesire_63
    pause
    jump passnightnothing
    return



label devzoe3:
    scene black
    stop music
    pause 1.0
    mc "Where am I?"
    scene white
    show mc:
        xalign 0.3
    show dream
    show black
    pause 0.1
    hide black with dissolve
    pause
    mc "What's this white place?"
    pause
    zo "No, noooo!"
    show zoe mad behind dream with dissolve:
        xalign 0.7
    pause
    zo "[mc]?"
    zo "I can't believe I'm dreaming of him!"
    zo "God damn I was about to fuck these guys..."
    zo "Lucid dreams are the best! But, why is there [mc]?"
    mc "How weird, I'm dreaming about [zon] dreaming of me..."
    zo "I am the one who is dreaming! What the heck is this?!"
    pause
    mc "[zon]..."
    show zoe base
    zo "What?"
    mc "I'm tired of you."
    zo "What?!"
    mc "I was so stupid back then, to accept you in my life."
    mc "I didn't know what it felt like to have a girl interested in me."
    mc "I accepted without questioning myself if I really wanted it."
    mc "I never took my needs, my will, my worth into consideration."
    zo "..."
    mc "You know, I've spent a bit of time with 4 amazing girls, some more than the others."
    mc "They all showed me I've got value, and I also have the right to get someone that brings me the respect I deserve."
    zo "Just because I never touched your cock? You're such a perv'!"
    mc "I'm not talking about that, just your behavior towards me generally."
    zo "..."
    mc "You made me curious, why haven't you tried to do anything with me yet?"
    zo "Why would I?"
    zo "It's just a dream, so I don't care if I tell you."
    show zoe mad
    zo "I never liked you at all."
    zo "Honestly, I just wanted to piss [bn] off, and also [en]."
    zo "It was also kind of satisfying to see [sn] losing her mind because of this."
    zo "All of them, I hate them all."
    zo "They all have one thing in common, they liked you."
    zo "I just wanted to get the one they liked and frustrate him the most I could."
    mcth "Wait, did she say [en] liked me back then? Impossible."
    show mc serious
    mc "That was so stupid of you."
    mc "So just to get revenge on people, you locked yourself in a false relationship?"
    mc "You sacrificed sex just for that?"
    show zoe base
    zo "I never sacrificed sex."
    show mc surprised
    mc "What?"
    zo "Are you stupid? I had no reason to be loyal!"
    zo "I would have loved to fuck with that cock of yours, though, it looks so amazing..."
    zo "But I prefer to keep you in your frustration."
    show mc base
    mc "... You're right."
    zo "?!"
    mc "I am stupid."
    mc "I'm probably too naive."
    mc "It ends now."
    zo "Hah? What are you gonna do?"
    show mc serious
    mc "I'm going to fuck you right now, like the bitch you are."
    show zoe shy
    zo "Wh-what?!"
    mc "Get naked and on your knees. I'm gonna fuck your face."
    mc "I'm so mad at you. I won't be sweet."
    zo "What a weird dream... But I like this version of [mc]."
    pause
    window hide
    stop music
    scene white
    play sex vdt1s
    show 023g
    show dream
    pause
    window auto
    mc "Oh shit!"
    mc "So, as you said, you wanted it but resisted just to frustrate me?"
    mc "I'm gonna relieve my frustration then!"
    mc "Oh my god, your throat is so tight!"
    mc "I despise you."
    mc "You've wasted my time and energy."
    mc "You're just a bitch good to be fucked hard!"
    zo "Hm!!"
    mc "Shut up!"
    call incrskill ("cockskill", 2) from _call_incrskill_64
    pause
    window hide
    stop music
    scene white
    play sex zmoans
    play sexfx sex05
    show 023i
    show dream
    pause
    window auto
    zo "Oh great lord!!!"
    zo "Your cock is about to rip my pussy off!!"
    zo "This is clearly the biggest one I've ever tried!"
    zo "The feeling is so intense, it's so much more real than usual!"
    zo "Oh, I love this dream!"
    zo "Fuck me! Fuck me, [mc]!"
    zo "Make me your bitch!!"
    call incrskill ("cockskill", 3) from _call_incrskill_65
    pause
    window hide
    stop music
    scene white
    play sex zmoans
    play sexfx sex05
    show 023j
    show dream
    pause
    window auto
    mc "I don't even want to see your face!!"
    mc "You're just a whore!"
    mc "You're a piece of shit just good to be fucked by me!!"
    zo "Yeah! yeah!!"
    zo "Make me pay for what I've done!"
    zo "Fuck me deep!"
    zo "I'm your little slut!!"
    mc "I'm about to cum into my slut!!!"
    zo "Yes!!! Do it!!!"
    pause
    window hide
    hide 023j
    stop sexfx
    stop sex
    show 023jcum
    show cumanim
    play audio cumexplo
    pause 0.1
    play audio zcum1
    pause 0.5
    play audio cumsound
    pause
    window auto
    zo "Ooooh yeaaaaah!!"
    call incrskill ("cockskill", 3) from _call_incrskill_66
    zo "I'm cumming so hard!!!"
    scene 023f with whiteflash
    show cumanim
    play audio zcum1
    pause
    zo "I'm cumming!! I'm cummiiiiing!!!"
    zo "It is even possible to cum from a dream?!!"
    zo "Oh shit, I need to fuck with [mc] right fucking now!!!"
    zo "Right after the end of the quarantine, I will-"
    "" "Message received."
    scene 023h with fade
    pause
    zo "\"I don't want to see you, ever again.\""
    zo "\"You don't even deserve the respect of being told face to face.\""
    zo "\"Adios.\""
    zo "Impossible!!!"
    zo "This little shit!!!"
    zo "I didn't think he'd get the balls to do that!!!"
    zo "I planned to make him suffer so much more!!!"
    zo "I didn't even get the chance to fuck with him for real!!"
    zo "Nooooooooooooo!"
    pause
    scene black with dissolve
    pause
    scene 023k with dissolve
    pause
    mc "I made it."
    mc "I was stupid."
    mc "She doesn't even deserve it until I'm waiting to see her face to face."
    mc "I'm free of her..."
    mc "I'm free..."
    mc "I'm single..."
    mc "What am I gonna do?"
    mc "Should I try to start a relationship with one of the 4 women living with me?"
    mc "But if I chose one, the others could be hurt!"
    mc "I don't know..."
    mc "Hmm. Well, they're not single, I'm the only one."
    mc "I think I just have to continue to live, and I'll see what happens."
    $ devzoe3ok = True
    if elv == 14:
        $ elv = 15

    if slv == 17:
        $ slv = 18

    if blv == 14:
        $ blv = 15

    if vlv == 16:
        $ vlv = 17
    $ mcstatus = "Single"
    $ zoestate = "Ex GF"
    if esn == "Girlfriend's best friend":
        $ esn = "Housemate"
    $ persistent.replay49 = True
    $ persistent.replay50 = True
    $ persistent.replay51 = True
    jump passnightnothing
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
