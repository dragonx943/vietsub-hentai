label talkv:
    scene expression ifnight ("House/valerie room/valerieroom 1.webp")
    show mc at left
    play sound vbrat
    if vstep <3:
        show valerie at right
        v "Hey, little brat."
    elif True:
        show valerie happy at right
        v "What do you want? Brat."
    menu:
        "{color=#ff9a40}Ask her what she's doing.{/color} Orange color = Quest" if qpreptalkv == False and vlv <2:
            jump vprepwork
        "{color=#ff9a40}Give her your cum.{/color}" if vlv == 4:
            jump devvp5
        "Tell her to jerk you off." if vstep > 0:
            jump vjerkoff
        "Quit" if True:
            jump tofrontyard

label vprepwork:
    $ qpreptalkv = True
    mc "Oh damn. It's rather small in here..."
    v "Did you come here just to make fun of me?"
    mc "No, not at all!"
    mcth "[bn] did a good job giving her this small room. Haha!"
    mc "I just came by to make sure you're okay."
    v "You want to know... if I'm okay? Don't mess with me, brat. I know you don't care."
    mc "I don't like you. We both know it."
    mc "We'll be living in someone else's house for a long time, perhaps. I think it would be best to try to get along at least. I don't want us to have a negative experience."
    pause
    v "Yeah. You're right."
    mc "So, what are you doing?"
    v "I'm preparing for my future activity."
    pause
    mc "Which is?"
    v "You don't need to know."
    mc "Ah?! Are you going to be a camgirl or something? Haha!"
    pause
    pause
    v "GET OUT OF MY ROOM, LOW LIFE!"
    if qpreptalkv == True and qpreptalkb == True and qpreptalke == True and qpreptalks == True:
        $ qpreptalk = True
        pause 1.0
    jump tofrontyard
    return

label vjerkoff:
    $ persistent.replay56 = True
    mc "Hey, wanna some more of my semen?"
    if vstep <3:
        v "Well, if you have another bottle, I wouldn't refuse."
        mc "I don't have any bottles. You have to collect it directly from the source."
        show valerie angryshy
        v "What the hell are you talking about?"
        show mc o1c
        pause
        show valerie surprised
        v "You want to cum on my face again?!"
        mcth "Why does it sound like she wants that?"
        mc "You do it."
        v "Me?"
        mc "Of course, if you want some, I'll let you take it. You're the one in control."
        show valerie happy
        v "I'm in control, obviously!"
        v "And I'm taking what I want!"
    elif True:
        v "Of course, and I'll take it from the source..."
    scene black
    window hide
    show 016hj
    stop music
    play sexfx frottements2
    play sex vmoanshj
    pause
    window auto
    v "The great lord created such a monster cock..."
    v "It's even more impressive when I touch it..."
    mc "Are you turned on by the brat's cock?"
    if vstep <3:
        v "In your dreams!"
    elif True:
        v "You already know how wet your cock makes me..."
    pause
    window hide
    hide 016hj
    show repvalmmastcum at cumtr
    show 016hjcum at cumtr
    show cumanim
    stop sexfx
    stop sex
    play audio vmccum
    play audio cumexplo
    play audio cumsoundext
    $ cumbyv += 1
    pause
    window auto
    v "Holy fuck"
    mc "You did a great job."
    if vstep <3:
        v "..."
        mcth "She doesn't say a thing."
        mcth "Does she realize she loves that?"
        v "N-now... I've got what I wanted. Leave me... alone..."
    scene black with dissolve
    call incrskill ("cockskill", 1) from _call_incrskill_59
    call incrdesire ("Valerie", cockskill) from _call_incrdesire_51
    pause
    jump passtime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
