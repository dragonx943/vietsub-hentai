label partywithsarena:
    mc "Let's dance!"
    show sarena happy
    s "Oooh, you're so cute, my pony wanna dance with me hehehe!"
    s "Let's goooo!"
    scene dancingbg with dissolve
    play music Wutif
    show sdance
    pause
    s "Palapapa!"
    mcth "I don't feel like a pro dancer at all."
    mcth "Sarena is always so full of energy! It makes me happy to see her like this."
    s "You look so stiff haha! Relax! Don't forget you're with me right now. No need to feel uncomfortable!"
    mc "Y-yes, of course!"
    mcth "I feel so happy to be confined with her..."
    show black with fade
    stop music
    "" "Many hours later..."
    "" "Everyone, but you two, left to sleep."
    scene dancingbg with dissolve

    play music chillsexy
    show mc drunk o5 with dissolve:
        xalign 0.35
    show sarena o5 drunk with dissolve:
        xalign 0.65
    s "Mooowh! Everyone left!"
    pause
    show sarena base
    if sstep >2:
        show sarena taunt
        s "You know what it means..."
        show mc shy
        mc "Er, that you want to go to the backyard?"
        s "Fuck the backyard."
        show sarena o5b with dissolve
        pause
        s "I wanna fuck right now."
        mc "Oh [sn], I want it too!"
        s "*hips*"
        s "Oh shoot..."
        s "I'm not sure I can drive this time."
        s "Maybe..."
        scene 024partypre with dissolve
        pause
        s "You can show me how badly you wanna fuck your [ssn]..."
        s "Look at it... I'm so wet just thinking of your cock!"
        window hide
        stop music
        scene 024partybg
        show 024party
        play sex ssoftmoans2
        pause 0.2
        play sexfx sex05
        $ persistent.replay55 = True
        pause
        window show
        mc "Oh [sn]!!"
        mc "I can't stop fucking you!!"
        s "Oh I know!"
        s "Fuck me like a savage!"
        s "Show me how much you love me, [mc]!"
        pause
        mc "Haaa!!"
        window hide
        stop sexfx
        stop sex
        play sound scum1
        hide 024party
        show 024partycum
        show cumanim
        play audio cumexplo
        pause 0.5
        play audio cumsound

        pause
        window auto
        s "Yeeees!!!"
        s "Cum in me, my pony!"
        scene 024partycumafter with dissolve
        window hide
        pause
        window auto
        s "I'm... so full of your cum..."
        s "This is all I needed...."
        $ cumbys += 1
        $ scum += 1
        call incrskill ("cockskill", 3) from _call_incrskill_26
        call incrdesire ("Sarena", cockskill) from _call_incrdesire_16
        jump passnightnothing


    s "I have to admit that I start to feel sleepy as well..."
    mc "Can I escort you to your bed?"
    show sarena happy
    s "You're sweet!"
    s "But no, [en] is already sleeping. I don't want to wake her up."
    s "It's not cold outside, come! I wanna sleep in the backyard!"
    mc "O-okay!"
    scene expression ifnight ("House/backyard/bytalk.webp")
    show mc drunk o5 with dissolve:
        xalign 0.35
    show sarena drunk o5 with dissolve:
        xalign 0.65
        yalign 1.0
    s "Waah... The temperature feels so perfect..."
    mc "So you wanna sleep there?"
    pause
    show sarena taunt
    s "Did I ever say you look cute?"
    mc "I think I heard that one or two times haha!"
    show sarena challenge
    s "Sit on the couch."
    mc "Ah? Why?"

    show sarena at angryjump
    s "Stop discussing! Just do as I said!"
    mc "Okay!"
    scene partybgsoutside with dissolve
    show tits s o5 with dissolve
    "" "[sn] is standing in front of you, exposing her voluptuous chest to your eyes."
    pause
    mcth "My [ssn] looks so pretty..."
    pause
    s "Looks like my seat is ready."
    mc "Hah?"
    scene sparty0b:
        yalign 1.0
        xalign 0.5
    show sparty0b at angryjump
    mc "Auuugh!"
    play sound smoh2
    s "Mooh that little moan was so sweet!"
    mc "What are you doing [sn]?!"
    s "So you like my tits?"
    mc "S-sure I do!"
    s "Haaah? You didn't even hesitate? Is it because you're drunk?"
    mcth "She doesn't take it badly. I guess I can freely say it."
    scene partybgsoutside with dissolve
    show tits s o5 with dissolve
    s "You know what? Earlier, I said the temperature was perfect. I was wrong."
    s "It feels a bit hot in there..."
    show tits s o2 with dissolve
    pause
    mc "!!! [sn]!!!"
    s "And now? Do you like this view on your [ssn]?"
    mc "You look... so perfect... I have no words..."
    if sstep == 0:
        mcth "Why do I feel like it's another dream?"
        s "Now it's time to sleep."
        mc "Ah?"
        scene sparty0 at angryjump
        mc "MMmgouh!"
        play sound sdontmove
        s "Shhhhh Don't move!! Just stay there..."
        s "Keep quiet!"
        mc "Bufth!"
        s "I said silence!! Just relax and sleep on my tits!"
        pause
        play sound sifeelsogood
        s "I feel so good."
        s "I don't know if I'm too drunk, but..."
        s "I feel so peaceful when I'm close to you like this..."
        s "I feel so much like I wanna take care of you, forever..."
        s "Your [ssn] will always stay by your side, never forget it."
        s "Now just sleep, I wanna sleep like this, it's so perfect..."
        mcth "Oh my gosh she is so drunk!!"
        mcth "But being drunk makes us do things with no sense, or is it making us do things we wouldn't dare in sober life?"
        mcth "I can feel her affection so much..."
        mcth "I also wish she never quit my life."
        mcth "I feel like in the heavens when she is on me like this..."
        scene black with dissolve
        "" "You fall asleep like this."
        call incrdesire ("Sarena", 2) from _call_incrdesire_17
    elif sstep == 1:
        show tits s o0 with dissolve
        window hide
        pause
        window auto
        s "And now?"
        mc "Oh great lord..."
        mc "You're blessed by god for real..."
        s "[mc] you're so cute... I shall reward you..."
        mc "Ah?"
        s "You know that I like feeling you between my tits."
        mc "Will I get my face in it?!"
        s "No, not your face... Look at this..."
        s "You're already so ready to play..."
        scene titsjobsa bg2 with dissolve
        play sexfx frottements
        play sex ssoftmoans
        show stjparty with dissolve
        window hide
        pause
        window auto
        mc "[sn]?!!! Are you alright?! Han!!"
        s "I may be a bit drunk... but I wanted to try this in secret..."
        s "But don't tell [mc]!"
        mc "Er yes, I won't say anything to myself..."
        s "I know you love my tits, and recently I've been playing with your thing a lot..."
        s "I did a little research on the internet and found that guys love this type of thing."
        s "Do you?"
        mc "Haaan [sn] I love it so much!!!"
        s "Do you realize how your [ssn] takes good care of you? Say it!"
        mc "My [ssn] is taking so good care of me!!! Haaan!"
        s "Great."
        s "Now, give me my meal."
        mc "You mean-"
        s "Yes, Just let it go! I want to taste it again!!! It's so good!"
        mcth "That's crazy, I could almost think she develops an addiction to my cum... is it? Nah I'm just fantasizing, I guess..."
        mc "Oh gosh it's so soft but you squeeze them so hard!"
        s "You can feel safe in between my tits!"
        s "Just give it to me!!!!! Abandon yourself to your [ssn]!!!"
        hide stjparty
        $ persistent.replay1 = True
        show stjpartycum
        stop sex
        play sound ssurprised
        if firsttjby == "None":
            $ firsttjby = "Sarena"
        $ cumbys += 1
        window hide
        pause
        window auto
        s "Ooooh!!! this is what I've been waiting for!!!"
        s "Oh!!!"
        s "It feels so warm on my face!!!"
        s "Your face expression looks so good!!"
        s "Haaa, I feel so satisfieeeeed...."
        stop sexfx
        scene black with fade
        "" "[sn] swallowed every drop of cum after that."
        "" "After a quick sleep, she woke up and said she didn't remember how the party ended and went back to her room, and you to yours."
        call incrskill ("cockskill", 2) from _call_incrskill_27
        call incrdesire ("Sarena", cockskill) from _call_incrdesire_18
    elif sstep == 2:
        show tits s o0 with dissolve
        s "I'm so hungry right now."
        mc "Er, do you want a snack or-"
        s "Oh yeah, an exceptional snack..."
        s "A snack that belongs to me."
        mc "Oh!"
        s "I am thinking of sucking your cock, - Every - Day."
        s "I want to take out your soul and keep it for me!"
        s "I can't wait anymore I need your cum right now!!"
        window hide
        show 018partyslow
        stop music
        play sex sbjsoft
        pause
        window auto
        mc "Great lord!!!"
        mc "[sn] you're so-"
        mc "Oh my god!!"
        mc "When I think you're doing it perfectly, you're improving each time!"
        mc "It's impossible for me to resist!"
        window hide
        hide 018partyslow
        show 018partyspeed
        play sex sbjhard
        pause
        window auto
        mc "Oh my god!!!"
        mcth "[sn] really does become like a succubus out to devour my soul!!"
        mcth "I want to offer her my soul!!"
        mc "[sn] I'm cumming!!"
        window hide
        show 018partycuma
        pause 0.6
        show 018partycumb
        show cumanim
        stop sexfx
        stop sex
        play audio sbjcum
        play audio cumexplo
        play audio cumsoundext
        pause
        window auto
        s "Such a perfect taste as always..."
        s "This is definitely my favorite meal..."
        scene black with fade
        $ persistent.replay17 = True
        $ cumbys += 1
        call incrskill ("cockskill", 2) from _call_incrskill_28
        call incrdesire ("Sarena", cockskill) from _call_incrdesire_19
    pause
    jump passnightnothing
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
