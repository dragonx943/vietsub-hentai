define doorlocked = False

image locked:
    "House/mcroom/doorlocked.webp"
    linear 2.0 yoffset -20.0
    linear 2.0 yoffset 0.0
    repeat
image unlocked:
    "House/mcroom/doorunlocked.webp"
    linear 2.0 yoffset -20.0
    linear 2.0 yoffset 0.0
    repeat
image lockershadow:
    "House/mcroom/lockedshadow.webp"
    linear 2.0 alpha 0.5
    linear 2.0 alpha 1.0
    repeat
screen mcroom:
    imagemap:
        ground ifnight("House/mcroom/bg mcroom.webp")
        add "lockershadow"
        if doorlocked == True:
            imagebutton:
                idle "locked"
                focus_mask True
                action Jump("lockthedoor")
        else:
            imagebutton:
                idle "unlocked"
                focus_mask True
                action Jump("lockthedoor")
        if vlv == 12 and Toolkit in inventory.items:
            imagebutton:
                idle ifnight("House/mcroom/mcroomtoolkit.webp")
                hover lumi("House/mcroom/mcroomtoolkit.webp")
                focus_mask True
                action Jump("devvp13")
        if vlv > 12 and vstep == 1:
            add ifnight("House/mcroom/mcroomgloryhole.webp")
        if vstep > 1:
            imagebutton:
                idle ifnight("House/mcroom/mcroomgloryhole.webp")
                hover lumi("House/mcroom/mcroomgloryhole.webp")
                focus_mask True
                action Jump("valgl")
        imagebutton:
            idle "House/maps/mcroomreplay.webp"
            hover lumi("House/maps/mcroomreplay.webp")
            xalign 1.0
            yoffset 420
            at floating

            action Jump("animationreplay")
        if devzoe1ok == False and daytimenumber == 3:
            if estep > 1 or vstep >1 or sstep >1 or bstep >1:
                imagebutton:
                    idle "0.2.3/zoemess.webp"
                    hover lumi("0.2.3/zoemess.webp")
                    focus_mask True
                    action Jump("devzoe1")

transform floating:
    linear 1.2 yoffset -10.0
    linear 1.2 yoffset 0.0
    repeat

label lockthedoor:
    if doorlocked == True:
        $ doorlocked = False
        "" "The door is now unlocked at Morning."
    elif True:
        $ doorlocked = True
        "" "The door is now locked at Morning."
    jump tomcroom

label morenterb:
    play music sand_castle
    show berry o4 at left:
        xzoom -1
    "" "[bn] is entering your room while you're asleep."
    play sound bhello
    b "Good mooorning my candy!!"
    show berry shy
    play sound bjesus1
    b "Oh, Jesus!"
    b "I-I'm sorry [mc], I didn't want to..."
    play sound bow2
    b "[mc]? Oh, he's still asleep..."
    pause
    if bstep == 0:
        b "This is crazy..."
        b "My little candy, my cute candy, my lovely candy, has a cock so huge and thick..."
        show berry lewd
        b "I feel so horny..."
        b "I wish I could-"
        show berry shy at angryjumpinv
        b "Come on [bn] get a grip on yourself! I should leave before I go crazy."
        show berry at leftquitinv
        call incrdesire ("Berry", 2) from _call_incrdesire_97
        pause
    elif bstep == 1:
        show berry lewd
        b "My sweet little candy looks sooo hard!"
        b "Is it the morning erection or is he having a wet dream?"
        b "Hm..."
        show berry base
        b "Let's wake him up in a pleasant way."
        scene black with dissolve
        pause
        mc "Hm... it feels so good..."
        scene morningview with dissolve
        show bmastmorning
        $ renpy.music.set_volume(0.3, delay=0, channel='music')
        play sex bkisstongue
        play sexfx frottements2
        window hide
        pause
        window auto
        mc "[bn]!!"
        b "Good morning, my sweet boy..."
        b "Do you like my new method of waking you up?"
        mc "OOh!! Ooh!!"
        b "I want you to know that in this house, I'll take care of you like you never imagined."
        b "Now come for me! Give it to me!"
        hide bmastmorning
        $ persistent.replay10 = True
        show morningview at cumtr
        show bmastmorningcumA at cumtr
        show bmastmorningcumB at cumtr
        show cumanim
        stop sex
        stop sexfx
        $ cumbyb += 1
        window hide
        play audio cumsoundext
        pause 0.1
        play audio bcumgoodboy
        pause
        window auto
        b "Your [bsn] will always be there to care for you every morning!"
        scene black with fade
        call incrskill ("cockskill", 1) from _call_incrskill_102
        call incrdesire ("Berry", cockskill) from _call_incrdesire_98
        pause

    elif bstep == 2:
        show berry lewd
        b "This morning wood-"
        b "My [mc] is so full of energy for me!"
        b "I can't resist the temptation!"
        b "It's time for my breakfast!"
        scene black with dissolve
        pause 1.0
        mc "I feel so good..."
        mc "I don't see anything."
        mc "Aah! This feeling!!"
        mc "This is [bn]'s throat. I'm sure of this!"

        window hide
        stop music
        scene black
        play sex bdtyandere05loop
        $ persistent.replay35 = True
        show 02morning
        pause
        window auto
        mc "Oh my god!!"
        mc "[bn]'s deepthroats always making me lose my mind!!"
        mc "This type of wake-up is the best!"
        mc "Feeling her wet pussy on my face-"
        mc "Feeling that she loves to blow me-"
        mc "Aaaaah!"

        window hide
        hide 02morning
        stop sexfx
        stop sex
        play audio bcuminmouth
        play audio ecuminmouth
        play audio cumexplo
        play audio cumsound
        show 02bjmorning_00006
        show 02morningcum
        show cumanim
        pause
        window auto
        $ cumbyb += 1
        mc "Oh my lord..."
        scene bg mcroom with fade
        show berry o4 at right
        show mc o0 shy humidface at left
        pause 1.0
        b "Good morning, my candy!"
        mc "[bn]!"
        b "You prepared me a hot breakfast, so I took it, haha!"
        mc "You can do it again whenever you want!!"
        b "So cute! you're already falling for me haha!"
        call incrskill ("cockskill", 2) from _call_incrskill_103
        call incrdesire ("Berry", cockskill) from _call_incrdesire_99
        pause
    elif bstep >2:
        scene black with fade
        pause
        stop music
        play sex bmoanshard
        play sexfx sex10
        pause
        mc "Oh lord-"
        mc "I feel like in the heavens!"
        call bsexmorninga027 (0.0833) from _call_bsexmorninga027_2
        $ persistent.replay66 = True
        b "Good morning, my Candy!"
        mc "Oh my lord!!"
        mc "G-good morning [bn]!"
        b "You were having a morning wood just for me!"
        b "Your body is ready for me even before you wake up!"
        b "You look so cute while you sleep, you know?"
        b "I couldn't help but fuck you while you were probably dreaming of me!"
        b "Do you like it?"
        b "When [bn]'s tits bounce in front of your face."
        b "When her big hips are pounding yours."
        b "When she uses you for her pleasure!"
        call bsexmorninga027 (0.0416) from _call_bsexmorninga027_3
        b "Say it!"
        mc "Yes, YES!"
        mc "I love so much being yours! you can do what you want to me!!"
        call bsexmorninga027cum from _call_bsexmorninga027cum_1
        b "Yeaaaaaah!"
        b "I'm cumming so hard!!!!"
        b "Cum inside Berry mommy, you're such a gooood boy!"
        pause
        $ bcum += 1
        $ cumbyb += 1
        call incrskill ("cockskill", 3) from _call_incrskill_104
        call incrdesire ("Berry", cockskill) from _call_incrdesire_100
        pause
    jump passtime

label morentere:
    play music sand_castle
    show emma o3 at left:
        xzoom -1
    "" "[en] is entering your room while you're asleep."
    play sound eloser3
    e "Hey loser, I just came to annoy you."
    show emma angryshy
    play sound eomg3
    e "Oh, my god! Are you jerking off again?!"
    pause
    show emma base
    e "Oh, he's asleep."
    pause
    if estep == 0:
        show emma shy
        pause
        e "Why does such a loser have such a big cock?!"
        e "I wish [zon]'s boyfriend, and mine could exchange their cocks..."
        show emma ahegao
        e "Just imagine getting pounded by this monster!!"
        show emma shy
        e "!!!"
        e "Oof, I lost it for a second. I'm lucky he didn't see me like this."
        show emma at leftquitinv
        call incrdesire ("Emma", 2) from _call_incrdesire_101
    elif estep == 1:
        show emma angryshy
        e "Why is he always showing me his big dick like this!!"
        pause
        show emma shy
        e "Maybe I could..."
        e "After everything he has done to me, I can!"
        scene ean anim bg
        show e12
        play sexfx frottements
        play sex emoans1
        $ persistent.replay4 = True
        window hide
        pause
        window auto
        e "It looks so big!!!"
        e "It looks so hard!!"
        e "I was already horny, but seeing this makes me crazy!!"
        e "I hope he won't wake up!"
        e "This freaking loser thinks he can play with my pussy whenever he wants!"
        e "He is so skilled with his fingers... Imagine with this huge cock..."
        e "What did I just say?!"
        e "What am I doing?"
        stop sexfx
        stop sex
        scene mcroommorning with fade
        show mcroomerect with dissolve
        show emma o3 angryshy at left
        e "This motherfucker thinks I'd want his cock, bullshit!"
        e "Stupid loser."
        show emma at leftquitinv
        call incrdesire ("Berry", 5) from _call_incrdesire_102
    elif estep ==2:
        show emma embarrassed
        e "And again, he's branding his dick to my eyes..."
        e "I bet he does it on purpose..."
        pause
        show emma angryshy at angryjump
        e "What do you think I'm gonna do?!"
        e "I'm not this kind of-"
        show emma embarrassed
        pause
        e "He's still sleeping?"
        e "..."
        e "Oh lord, I'm so horny! I hope I won't wake him up with this!!"
        show black with dissolve
        scene black

        window hide
        stop music
        scene bgemorning:
            xalign 0.5
            yalign 0.5
        play sex emoans4
        show emorning
        $ persistent.replay43 = True
        pause
        window auto
        e "Yes! Yes!"
        e "I can feel it!"
        e "It's so hot and hard!!!"
        e "It's almost as if I can feel it inside me!!"
        e "Oh my gosh, it would be insane to ride [mc]!!"
        e "Oh my god! If I were his girlfriend, I would ride him all day long!!!"
        e "I want his cock right now!!!"
        e "I want-"
        window hide
        hide emorning
        stop sexfx
        stop sex
        play audio ecum3
        show emorningcum
        show cumanim
        window auto

        e "Gnnnnnnh!!! I'm cumming!!!"
        e "I wanna get fucked sooo baaaaaad by [mc]!!!"
        pause
        show black with dissolve
        scene mcroommorning
        show mcroomerect
        show emma o3 shy
        show black
        pause 0.1
        hide black with dissolve
        e "I swear I never said that!!!"
        pause
        show emma surprised
        e "Looks like he's still asleep."
        show emma smirk
        e "Great."
        hide emma with dissolve
        $ ecum+=1
        call incrskill ("cockskill", 2) from _call_incrskill_105
        call incrdesire ("Emma", cockskill) from _call_incrdesire_103
    elif estep >2:
        show emma tsun
        e "[mc]..."
        e "I bet he is dreaming about me right now..."
        e "I love him so much..."
        e "I have to wake him up like a king!"
        scene black with dissolve
        pause
        stop music
        play sex emoans3
        pause
        mc "Oh fuck!!"
        mc "I feel so good. What's happening?"
        call esexmorning from _call_esexmorning_1
        $ persistent.replay61 = True
        if mcstatus == "Promised to Emma":
            e "Good morning, my future husband!"
            e "I'm so sorry. I thought it was my role to wake you up like this."
        elif mcstatus == "Single":
            e "Good morning, [mc]!"
            e "I'm so sorry, but I told you I'll do anything to make you fall in love with me!"
        elif True:
            e "Good morning, honey!"
            e "I'm so sorry, but you know I can't resist my boyfriend's cock when I see it!"
        mc "Don't be sorry, [en], it's the perfect way to go!"
        e "Oh [mc]... Oh!"
        e "Oh no, it's coming again!!"
        e "Your cock is driving me insane!"
        e "I'm about to lose control!!!"
        call esexmorningb from _call_esexmorningb_1
        e "I'm so sorry [mc]!!"
        e "I'm not looking cute anymore!!"
        e "My mind is blank!"
        e "All I want is to get fucked by this cock of yours for the rest of my life!!"
        e "I'm about to die!!"
        call esexmorningcum from _call_esexmorningcum_1
        e "It's so goooooood!!!"
        e "You keep filling me out with your cum!"
        scene deve8 with fade
        e "It's pouring out!"
        e "So hot and sticky..."
        e "I love you so much, [mc]!"
        stop sex
        stop sexfx
        $ ecum +=1
        $ cumbye+=1
        call incrskill ("cockskill", 3) from _call_incrskill_106
        call incrdesire ("Emma", cockskill) from _call_incrdesire_104


    pause
    jump passtime

label morenters:
    play music sand_castle
    show sarena o4 challenge at left:
        xzoom -1
    "" "[sn] is entering your room while you're asleep."
    play sound shey1
    s "Surprise, your [ssn] is there!!!"
    show sarena shocked
    s "Oh darn! I'm sorry I didn't think you were..."
    pause
    show sarena taunt
    s "Hooh?"
    if sstep == 0:
        play sound spony
        s "My pony is asleep! Is it the famous hard cock in the morning?"
        s "I failed my morning's surprise..."
        pause
        show sarena shy
        play sound sthink
        show sarena:
            ease 1.0 xoffset 350
        pause
        play sound souaw1
        s "His thing looks so big!"
        show sarena:
            linear 1.0 xoffset 400
        s "I can even feel the heat coming from it!"
        pause
        s "I'm too curious. I shouldn't stare at it like this."
        show sarena at leftquitinv
        call incrdesire ("Sarena", 1) from _call_incrdesire_105
    elif sstep == 1:
        $ persistent.replay127 = True
        s "Looks like my pony is calling for his [ssn]'s help in his dreams..."
        scene black with fade
        pause
        call showscene ("sarenanewhjmorning presex") from _call_showscene_96
        mc "My balls feels so warmed-up..."
        mc "Oh... that feels so good..."
        call morning013 (v=1.0/12) from _call_morning013_2
        mc "OOOh!!!"
        s "Oh? That's how you thank your lovely [ssn] for helping you?"
        mc "What's all of a sudden?!"
        s "You were so hard when I entered. I just wanted to play with it a little bit."
        call morning013 (v=1.0/24) from _call_morning013_3
        s "Come on, give it to me!"
        mc "Oh my goood!"
        call morning013cum from _call_morning013cum_1
        $ persistent.replay127 = True
        $ cumbys += 1
        window hide
        pause
        window auto
        s "That's it!!! I wanna taste that thing of yours again!!"

        call showscene ("sarenanewhjmorning aftercumb") from _call_showscene_97
        s "This sticky thing tastes delicious. I wonder how you do that."
        pause
        s "So? How do you find my \"Sarena Special morning wake up\"?"
        mc "Very enjoyable!"
        s "You get used to that so fast!"
        s "You must be a real pervert, haha!"
        s "Come on, time to dress up!"
        call incrskill ("cockskill", 1) from _call_incrskill_107
        call incrdesire ("Sarena", cockskill) from _call_incrdesire_106
    elif sstep == 2:
        $ persistent.replay15 = True
        s "My favorite meal on a plate..."
        scene white
        show 018bjmorning
        stop music
        play sex sbjsoft
        show eyeshalfclosed
        show black
        pause
        mc "Oh, I feel so good..."
        hide black with dissolve
        pause
        mc "hm..."
        window hide
        hide eyeshalfclosed with dissolve
        pause
        window auto
        mc "[sn]!!"
        s "Mh!!"
        mcth "She saw my morning wood, and then she served herself!"
        mc "Oh [sn], it's too good to resist!"
        hide 018bjmorning
        show 018bjmorning2
        play sex sbjhard
        pause
        mc "Oh no, don't go faster!!"
        mc "I'm gonna-"
        window hide
        show 018bjmorningcuma
        show 018bjmorningcumb
        show cumanim
        stop sexfx
        stop sex
        play audio sbjcum
        play audio cumexplo
        play audio cumsoundext
        pause
        window auto
        mc "It was amazing..."
        s "*glouh* *glouh*"
        pause
        scene bg mcroom
        show mc o0 surprised at left
        show sarena o4 at right
        s "Good morning, my pony!"
        s "You're full of energy, like every morning!"
        mc "[sn]..."
        s "Honestly, I think it became my favorite breakfast, haha!"
        $ cumbys += 1
        call incrskill ("cockskill", 2) from _call_incrskill_108
        call incrdesire ("Sarena", cockskill) from _call_incrdesire_107
    elif sstep >2:
        show sarena taunt
        s "My pony's cock is calling for mommy..."
        s "How could I refuse!"
        scene black with fade
        pause
        stop music
        play sex ssoftmoans2
        play sexfx frottements
        pause
        $ persistent.replay53 = True
        call morning024 (1.0/12) from _call_morning024_2

        mc "Urh!"
        mc "[sn]?"
        s "Good morning, my pony!"
        s "I'm taking care of your morning wood. I hope you don't mind!"
        call morning024 (1.0/24) from _call_morning024_3
        mc "Oh [sn], you take care of it so good!"
        s "Come one, baby, it's time for my morning milk!"
        s "Your balls are full from the night, I hate when your milk is wasted!"
        mc "Aaahug!"
        call morning024cum from _call_morning024cum_1
        s "That's my good boy!!"
        s "Fill me up!"
        pause
        play sound acum2
        call showscene ("024morningcum2") from _call_showscene_98
        pause
        s "Nice breakfast in bed..."
        $ cumbys += 1
        $ scum += 1
        call incrskill ("cockskill", 3) from _call_incrskill_109
        call incrdesire ("Sarena", cockskill) from _call_incrdesire_108

    pause
    jump passtime

label morenterv:
    play music sand_castle
    show valerie o3 at left:
        xzoom -1
    "" "[vn] is entering your room while you're asleep."
    play sound vbrat
    v "Hey brat, just came to ruin your morning."
    show valerie angry
    play sound vholyfuck2
    v "Rhoooh come on, why are you always with your dick out?!"
    pause
    if vstep == 0:
        show valerie happy
        play sound vhoh
        v "Oh, he looks like he is in a deep sleep."
        v "Should I do something? Mouahaha!"
        pause
        show valerie surprised:
            ease 1.0 xoffset 400.0
        v "Seriously."
        pause
        show valerie pleasure
        v "This looks like the best cock I've ever seen!"
        v "It's such a shame it's on this brat!"
        v "I can't fuck anymore with this quarantine, and I have to live with a cock like this, on a useless brat!"
        v "I should leave before I get crazy."
        show valerie at leftquitinv
        call incrdesire ("Valerie", 2) from _call_incrdesire_109
    elif vstep == 1:
        v "He's still asleep."
        scene morningview with dissolve
        show 016lickmorning with dissolve
        play sex vmoanslick
        pause

        v "This cock is so perfect."
        v "I want to choke on it so bad..."
        v "He should never hear me saying such things."
        v "Why does this bastard have such a cock?"
        v "I want it so bad!"
        v "Oh no, I should stop before he wakes up and hear that."
        scene black with dissolve
        call incrdesire ("Valerie", 5) from _call_incrdesire_110
    elif vstep == 2:
        show valerie shy
        v "He's still asleep."
        show valerie think
        v "Hm..."
        show valerie happy
        v "He's still asleep..."
        v "I think it's time to piss him off."
        v "He doesn't respect me anymore, it's time for me to teach him."
        scene black with dissolve

        window hide
        stop music
        scene bgv2morn:
            xalign 0.5
            yalign 0.5
        play sex vbj
        $ persistent.replay46 = True
        play sexfx frottements2
        show v2morning
        pause
        window auto
        v "Holy shit!"
        v "This boy has a real monster..."
        v "It's so hard!!"
        mc "Hm... Hm?"
        mc "Is it the morning? Hello-"
        mc "[vn]?!"
        v "Ah? I failed not to wake you up, haha!"
        mc "What are you doing?"
        v "You think now you can do whatever you want to me."
        v "I'm showing you I can also do as I wish."
        v "I want to taste it again!"
        mc "It's here!!"
        window hide
        hide v2morning
        stop sexfx
        stop sex
        play audio vcuminmouth
        play audio cumexplo
        play audio cumsound
        show v2morningcum
        show cumanim
        pause
        window auto
        $ cumbyv += 1
        v "Hm..."
        v "Amazing..."
        scene bg mcroom
        show mc o0 surprised at left
        show valerie happy cumface o3 at right
        v "Are you mad at me? Haha!"
        v "See? I can also do as I please."
        v "What are you going to do? Punish me? Haha!"
        hide valerie with dissolve
        pause
        show mc base
        mc "Shit, She still woke me up so good..."
        show mc serious
        mc "But I don't like that satisfaction on her face."
        mc "Yeah, I have to teach this chick."
        call incrskill ("cockskill", 2) from _call_incrskill_110
        call incrdesire ("Valerie", cockskill) from _call_incrdesire_111
    elif vstep > 2:
        $ persistent.replay70 = True
        call valmorsex from _call_valmorsex
    pause
    jump passtime

label dream:
    scene black with fade
    "" "Dream feature is a tool outside of the story."
    "" "It's a way for the creator of the game to train sex animating skills and show it."
    "" "Pure sex will take a bit of time to arrive, so see it as a preview."
    menu:
        "Which dream do you want to see?"
        "Berry riding you in the backyard." if True:
            jump berrydream1
        "Cancel." if True:
            jump tomcroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
