label takeshower:
    scene bathroom talk with fade
    show bathroom
    play music chillsexy
    show mc o0 at left
    mc "It's shower time!"
    "" "Each girl will try to take a shower at a specific time of day."
    show shower sfx zorder 1
    mc "Aaaah, it feels good..."
    mc "This house is making me so lustful..."
    show mc o0a shy
    mc "I need to relieve!"
    show mc o0b pleasure
    mc "Oh!"
    mc "Ah!"
    "" "You forgot to lock up the door. Someone is entering..."
    if daytimenumber == 0:
        jump showere
    elif daytimenumber == 1:
        jump showers
    elif daytimenumber == 2:
        jump showerv
    elif daytimenumber == 3:
        jump showerb
    jump passtime

label showerb:
    if bstep == 0:
        jump showerb0
    elif bstep ==1:
        $ persistent.replay9 = True
        show berry at right
        play sound bhello
        show mc surprised
        b "Well, well, well. What do we have here?"
        b "My cute little boy is having fun in secret?"
        mc "Arh, [bn] Yeah, it's my private time, so..."
        b "Let me give you a hand."
        mc "Oh, well, -"
        b "I'm not giving you a choice."
        scene black with fade
        window hide
        pause 0.5
        scene 015bgbhj with dissolve
        play sexfx frottements2
        play sex bdonttrytoholdback
        show 015hjshowerb with dissolve
        show buee with dissolve
        pause
        window auto
        b "Nobody will know, don't be afraid."
        b "Your [bsn] is here to make you feel good. She takes good care of you."
        b "Now, cum for me, don't try to hold back!"
        hide 015hjshowerb
        stop sex
        stop sexfx
        show 015bgbhj at cumtr
        show 015hjshowerbcumA at cumtr
        show 015hjshowerbcumB at cumtr
        show cumanim
        $ cumbyb += 1
        play audio cumsound
        play audio bcumgoodboy
        b "That's what I wanted..."
        b "You're a good obedient boy. I'm very proud of you."
        call incrskill ("cockskill", 1) from _call_incrskill_51
        call incrdesire ("Berry", cockskill) from _call_incrdesire_39
    elif bstep ==2:
        show berry tease at right
        play sound bhello
        show mc surprised
        b "Well, well, well. What do we have here?"
        b "A handsome youngster thinking of his [bsn]?"
        b "You're so hard for me right now..."
        pause
        b "You know what?"
        b "I need a shower."
        hide window
        show berry o6 with dissolve
        pause 1.0
        scene 026c with dissolve
        pause
        window auto
        b "A woman needs a good boy for her cleaning."
        mc "Oh, [bn]! Anything for you!"
        b "You're so sweet..."
        pause
        b "Here."
        b "My anus is almost cleaned."
        b "It just needs a good boy's tongue."
        b "Come, show me you're not afraid of [bn]'s body."
        mc "Oh [bn]!!!"
        window hide
        scene 026b with dissolve
        play sex bmoans1
        pause
        window auto
        b "That's what I call a goooood boy."
        b "Never afraid of a woman's body."
        b "Particularly mine."
        mc "Hmmm!!!"
        b "Hooh?"
        b "I can hear by those moans that you love it."
        b "You know that it's a very delicate spot."
        b "On rare occasions, a person can cum from there because it is a concentration of nerve endings."
        b "I think, with training, you could make me, one day-"
        b "-Oh gosh!!"
        b "I can feel how hard you're loving my anus!!"
        b "That's it!!!"
        b "Oh my-"
        window hide
        scene 026bcum
        show cumsfxrep:
            xalign 0.53
            yalign 0.40
        play audio bcum1
        stop sex
        $ bcum+=1
        call incrskill ("tongueskill", 2) from _call_incrskill_52
        call incrdesire ("Berry", tongueskill) from _call_incrdesire_40
        pause
        window auto
        b "I'm cumming from my asshole!!!"
        b "Oh, your [bsn] is so proud of you, [mc]!!"
        b "I will never let a good boy like you go away from me!!!"
        pause
    elif bstep >2:
        $ persistent.replay88 = True
        show berry tease at right
        play sound bhello
        show mc surprised
        pause
        jump evbersexshower



    jump passtime

label showerb0:
    show berry at right
    play sound bhello
    b "Hey there, it seems there's already some-"
    show berry shy
    play sound bohjesus2
    b "OOoh!!!"
    show mc o0a surprised
    mc "Oh no!!! Why are you there?"
    b "I'm sorry [mc], it wasn't locked correctly!"
    b "I'm always going to the bathroom at this time!"
    b "..."
    show berry:
        linear 1.0 xoffset -50
    pause 1.0
    play sound bow
    b "Are you jerking off?"
    mc "It looks like..."
    show berry:
        linear 2.0 xoffset -150
    pause 2.0
    b "..."
    b "Are you doing it every time you take a shower?"
    b "No, don't answer. I'm sorry!"
    show berry happy
    b "I'll wait for you to finish, have a good time with yourself!"
    show berry at rightquit
    mc "Holy shit..."
    show mc shy
    mc "The way she looked at my cock..."
    mc "I don't know if I feel excited or embarrassed..."
    call incrdesire ("Berry", 2) from _call_incrdesire_41
    jump passtime
label showers:
    if sstep == 0:
        jump showers0
    elif sstep == 1:
        jump showers1
    elif sstep == 2:
        jump showers2
    elif sstep > 2:
        $ persistent.replay91 = True
        show sarena at right
        play sound shey1
        mc "Hhey-"
        pause
        jump evsarsexshower
    jump tobathroom

label showers0:
    show sarena at right
    play sound shey1
    s "Is there someone?"
    show sarena shocked
    show mc o0a surprised
    play sound souaw2
    s "Oh waw!"
    s "I'm so sorry [mc]! I'm used to taking my shower at this time of day!"
    show mc shy
    mc "O-okay, I take note..."
    s "So I'm leav-"
    pause
    mc "?!"
    show sarena shy:
        linear 1.0 xoffset -300
    pause 2.0
    play sound sthink
    s "Are you stroking your thing?"
    mc "[sn]!!"
    show sarena taunt:
        linear 0.5 xoffset -400
    play sound slol1
    s "Rhoo what, you don't want your [ssn] to see your Godzilla? Haha!"
    s " Don't worry, I know guys are doing this thing all the time. There is no shame."
    s "Alright, I'm waiting after you finish. I hope you're not thinking about me haha!"
    mc "Of... course not.. haha..."
    show sarena at rightquit
    pause
    mc "[sn]... "
    call incrdesire ("Sarena", 2) from _call_incrdesire_42
    pause
    jump passtime
label showers1:
    show sarena at right
    play sound shey1
    s "Is there someone?"
    show sarena shocked
    show mc o0a surprised
    play sound souaw2
    s "Oh waw!"
    pause
    show sarena taunt
    s "Hooh are you playing with my new toy?"
    show mc shy
    mc "Hey! That's also my toy! A man needs some time for himself!"
    show sarena shy
    s "Oooh, that's true!"
    pause
    s "I want to give you a bit of inspiration."
    mc "Ah?"
    scene bathtitsbg with fade
    show tits s o1 with dissolve
    s "I know you like them, so..."
    show tits s o2 with dissolve
    pause
    show tits s o0 with dissolve
    mc "!!!"
    s "You can continue."
    mc "..."
    "" "You're jerking off in front of Sarena's tits."
    mc "Aaaarh!"
    show titsscum with whiteflash
    window hide
    pause 2.0
    window auto
    s "Oaaa! You came so much!"
    s "Thank you for the gift hehehe!"
    call incrskill ("cockskill", 1) from _call_incrskill_53
    call incrdesire ("Sarena", cockskill) from _call_incrdesire_43
    pause
    jump passtime
    return

label showers2:
    show sarena at right
    play sound shey1
    s "You there, [mc]?"
    show mc o0a surprised
    mc "S-Sarena?!"
    show sarena taunt
    s "As expected."
    s "Always jerking off while I'm away, right?"
    s "You naughty boy..."
    show sarena o6 with dissolve
    pause 1.0
    show sarena onaked with dissolve
    pause 1.0
    mc "What are you doing?!"
    s "You look like you're in trouble cleaning your body."
    s "I'm just giving you a hand. It's important to clean everything."
    s "Hand isn't the right word."

    window hide
    stop music
    scene i021showerbg:
        yalign 0.5
    play sex sdt2sec
    show 021shower
    show i021shower

    window auto
    mc "Oh my!!"
    mc "It's so deep!"
    s "I need to force a little bit, but I can do it!!"
    mc "Oh [sn], you're making me crazy!"
    s "I love when you say that!"
    s "I want to give you the best!"
    mc "Oh [sn], OOOH!"
    window hide
    hide 021shower
    stop sex
    $ persistent.replay41 = True
    play audio sbjcum
    play audio cumexplo
    play audio cumsound
    show 021showercuma behind i021shower
    show 021showercumb behind i021shower
    show cumanim

    window auto
    s "So hard... But so good..."
    $ cumbys += 1
    pause
    call incrskill ("cockskill", 2) from _call_incrskill_54
    call incrdesire ("Sarena", cockskill) from _call_incrdesire_44
    pause
    jump passtime
    return



label showere:
    if estep == 0:
        jump showere0
    if estep == 1:
        show emma at right
        e "Hey, who's ther-"
        show emma shy
        e "Kiaah!!"
        e "You, again?!"
        mc "Yes again, I also take showers. What's the problem?"
        show emma angry at angryjump
        e "You're jerking off all the time, disgusting pervert!"
        e "I hope you're not thinking about ME!!"
        mc "Of course not."
        show emma angryshy
        e "You liar!"
        mc "Why would I? I've got better standards. I prefer good girls!"
        show emma at angryjump
        e "Huuh?!"
        e "I don't think good girls have a body like mine!"
        mc "Oh you think?"
        e "Of course!"
        scene bathassbg
        show ass emma 1
        pause
        e "Look at that!"
        mc "I don't see anything that hot."
        e "~Grmblfe!~"
        show ass emma 3 with dissolve
        window hide
        pause
        window auto
        e "AND NOW?"
        "" "You're continuing to masturbate looking at her ass."
        e "Why are you silent? Amazed?"
        e "[mc]?"
        mc "I'm cumming!!"
        show assemmacum at cumtr
        show cumanim
        pause
        e "Kyaaaaaaa!"
        mc "I'm sorry [en] I was just jerking off, and you were in my way!"
        scene black with fade
        "" "[en] runs away from the bathroom with your cum on her butt. You won't know what she did with that."
        call incrskill ("cockskill", 1) from _call_incrskill_55
        call incrdesire ("Emma", cockskill) from _call_incrdesire_45
        pause
    elif estep == 2:
        $ persistent.replay48 = True
        show emma at right
        e "You're still under the shower? AGAIN?!"
        show mc shy
        mc "[en]! You don't even knock anymore?!"
        e "I never did. Plus, I've already seen you naked."
        e "I've been waiting for the shower, but you're taking so long!"
        show mc lol
        mc "Wanna join me then? Haha!"
        show emma angryshy
        pause
        e "DEAL!"
        show mc surprised
        mc "It was just-"
        show mc base
        mc "Alright, I'm waiting for you."
        show emma shy
        e "Wait, are you done soon?"
        mc "Yeah, I just have to clean my cock."
        show emma tsun
        e "D- d- do you want me to..."
        mc "Help? Sure!"
        e "I hope you won't-"
        mc "I won't tell anyone."
        e "O-okay."
        scene black with dissolve
        pause
        window hide
        stop music
        scene 023lbg_00001
        show 023l
        show i021shower
        pause 1.0
        play sex edt_2
        pause
        window auto
        mc "Oh, don't move!"
        mc "Oh, [en], your throat feels so good!"
        mcth "She's not moving at all."
        mcth "She wants me to feel good and use her mouth how I'd like."
        mc "You're such a nice girl... Let me feel good in your mouth like this..."
        mc "I could become addicted to you, [en]!"
        e "Hm!!!"
        mc "Oh, I'm gonna cum!!"
        pause
        mcth "She doesn't push me away."
        window hide
        hide 023l
        stop sexfx
        stop sex
        show 023lcum
        show cumanim

        play audio cumexplo
        pause 0.1
        play audio ecuminmouth2
        pause 0.5
        play audio cumsound
        pause
        window auto
        mc "Oh..."
        mc "That's so good..."
        scene black with dissolve
        pause
        mcth "[en] wasn't mad at me for cumming deep down her throat. I think she loved it."
        $ cumbye +=1
        call incrskill ("cockskill", 2) from _call_incrskill_56
        call incrdesire ("Emma", cockskill) from _call_incrdesire_46
        pause
    elif estep >2:
        $ persistent.replay62 = True
        show emma happy at right
        e "[mc]!"
        show mc shy
        mc "Oh hey, [en]!"
        if estep == 4 and ispromisedtoemma == True:
            e "Washing without your wife?!"
            mc "You're not my wife yet!"
            e "You're right... Let's fix that!"
            show emma tsun
            e "Fuck me until you fall in love, enough to make your move..."
        elif True:
            e "Washing your shaft again?"
            mc "Yeah, washing..."
            show emma tsun
            e "I knew it."
            e "You know, I was wondering..."
            e "If you want, there is a better place to rub your monster..."
            show mc lol
            mc "You naughty girl..."
            e "No, Imma good girl!"
            mc "Come here."
        call esexshower (0.08) from _call_esexshower_2
        mc "Oh fuck!"
        mc "Your pussy makes me insane!!"
        e "Isn't it your favorite place to be?"
        mc "That's right, I feel like you're made for me!!"
        e "Oh, [mc]!"
        mc "So tight, but so slippery!"
        mc "I can't stop fucking you!"
        e "[mc]! Repeat it!"
        call esexshower (0.04) from _call_esexshower_3
        mc "I- can't-stop-"
        mc "Fucking you, [en]!!"
        e "My pussy is yours, [mc]!"
        e "Just use me as you want!"
        mc "Oh [en]!"
        call esexshowercum from _call_esexshowercum_1
        e "It's pouring in me!!!!"
        e "I can feel my womb full of your warm cum!!"
        pause
        scene deve7 with fade
        e "Look at this... A real mess..."
        mc "You look amazing like that, though."
        e "Hehehe!"

        stop sex
        stop sexfx
        $ cumbye += 1
        $ ecum += 1
        call incrskill ("cockskill", 3) from _call_incrskill_57
        call incrdesire ("Emma", cockskill) from _call_incrdesire_47
        pause


    jump passtime

label showere0:
    show emma at right
    play sound esoupir
    e "Hey, who's ther-"
    show emma shy
    e "Kiaah!!"
    play sound eomg2
    e "Oh my god!"
    show mc o0a surprised
    mc "[en]?! Why are you spying on me?!"
    show emma angry at angryjump
    play sound ewhat1
    e "WHAT?!"
    e "Spying on you in your dreams! I always go to the bathroom at this time of day!"
    e "And why are you naked in the bathroom?!"
    show mc serious
    mc "What the hell is that question?! I'm taking a shower!"
    show emma angryshy
    e "And you have to stroke yourself to take a shower?!"
    show mc base
    mc "It's just my private time!!"
    pause
    show emma shy:
        linear 1.0 xoffset -75
    pause 1.0
    mc "[en]?"
    show emma angryshy
    play sound eloser2
    e "You fucking loser."
    show emma at rightquit
    mc "Ahlala, that girl..."
    mc "She acts so harsh with me, but I'm sure she'll learn to like me one day."
    call incrdesire ("Emma", 2) from _call_incrdesire_48
    pause
    jump passtime
label showerv:
    if vlv == 7:
        jump devvp8
    if vstep == 0:
        jump showerv0
    if vstep ==1:
        show valerie at right
        v "Oh! You're there, stroking yourself again."
        v "..."
        v "Are you kidding?"
        v "Hello, someone is here!"
        mc "Ah! Shut up!"
        show valerie angry
        v "You-"
        mc "I'm about to cum. Show me your tits and kneel so I can cum on your face!"
        v "Are you Kidding?"
        mc "I won't last long! Do it!"
        scene 016shower with dissolve
        pause
        v "Oh ouah!"
        mc "I knew you'd do it! You are a naughty woman!"
        v "I know, but hurry up!"
        pause
        show 016showercum at cumtr
        show 016shower at cumtr
        show cumanim
        play audio cumsoundext
        pause
        v "Holy fuck!"
        mcth "She loves so much to get facials... so fascinating."
        call incrskill ("cockskill", 1) from _call_incrskill_58
        call incrdesire ("Valerie", cockskill) from _call_incrdesire_49
        pause
        jump passtime
    if vstep == 2:
        $ persistent.replay76 = True
        jump valshower2
    if vstep >2:
        $ persistent.replay79 = True
        jump valshower3
    return














































label showerv0:
    show valerie at right
    play sound vhoh
    v "Hey, I'm here, I hope none is naked!"
    show valerie surprised
    play sound vholyfuck2
    v "Holy fuck!!"
    v "It's even bigger than what I remember!"
    show mc serious o0a
    mc "[vn]?!"
    play sound vhoh
    show valerie happy:
        linear 1.0 xoffset -100
    v "It seems the little boy is a bit horny."
    mc "And? You're not concerned about my urges."
    v "It's so sad for your girlfriend not to be there. Are you sad?"
    mc "Get out!"
    show valerie base
    play sound vbrat
    v "You may have a giant cock, it doesn't mean you're allowed to talk to me like that."
    show valerie at rightquit
    pause
    mc "She is focused on my cock's look all the time."
    mc "Hm... I should keep this information in mind for later."
    call incrdesire ("Valerie", 2) from _call_incrdesire_50
    pause
    jump passtime
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
