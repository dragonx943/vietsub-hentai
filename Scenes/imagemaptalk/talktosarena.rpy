

label talks:
    scene bg talk balcon 1
    play sound shey1
    show sarena at right
    show mc at left
    if sstep == 0:
        s "Heeey!"
    elif sstep ==1 or sstep ==2:
        s "Hey my little pony!"
        s "You look so good today!"
    elif sstep > 2:
        s "Hey my love!"
        s "My pony looks so hot today!"
    menu:

        "{color=#ff9a40}\"Hey, how about we do our first video together?\"{/color}" if slv == 2 and sdesire >= desireforstep1:
            jump tryfirstvideo
        "{color=#ff9a40}\"I'm ready for your next video!\"{/color}" if slv == 4:
            jump devsp5
        "{color=#ff9a40}\"I guess it's time for another self-defense video!\"{/color}" if slv == 7:
            jump devsp8
        "{color=#ff9a40}\"I guess it's time for another video!\"{/color}" if slv == 10:
            jump devsp11

        "{color=#ff9a40}\"I guess it's time for another video!\"{/color}" if slv == 20:
            jump devsp21
        "Spank her butt!!" if sstep > 0:
            jump sspank

        "How about a chest workout video?" if sstep > 1:
            jump stiddi

        "{color=#c13a3a}How about making a new video, my love?{/color}" if sstep >2:
            $ persistent.replay90 = True
            jump evsarsexbalc
        "Quit" if True:

            jump tobalcony
label stiddi:
    s "Sure!"
    s "I love to work and spend time with you, [mc]!"
    scene black with dissolve
    pause
    "" "An hour later, after you finished work..."
    window hide
    play sex ssoftmoans2
    scene 021b with dissolve
    pause
    window auto
    s "That's good."
    s "Suck your [ssn]'s nipple!"
    s "This is your reward for your good work."
    s "I see how you're staring at my boobs all the time!"
    s "You are craving for this!"
    s "Or am I?"
    s "Oh [mc], it's like you're born to make me feel so good..."
    pause
    stop sex
    scene black with dissolve
    call incrskill ("tongueskill", 2) from _call_incrskill_111
    call incrdesire ("Sarena", tongueskill) from _call_incrdesire_112
    pause
    jump passtime

label sspank:
    scene balconybgsass
    show ass sarena 1
    mcth "Look at this round... Big... Juicy butt..."
    mcth "What's happening?!"
    mcth "I feel like a Demon is taking over my body!"
    mcth "I can't stop it!"
    play sound spank
    show ass sarena with hpunch
    pause
    s "YOU LITTLE-"
    scene bg talk balcon 1
    show sarena challenge at right
    show mc surprised at left
    mc "It's not me [sn]!"
    s "Haaaah? I bet you'll tell me some demon spirit took possession of your hand?!"
    mc "Exactly!!"
    show mc base
    show sarena taunt
    s "Haha you'll get what's coming to you!"
    s "I'll take my revenge, don't worry haha!"
    call incrskill ("handskill", 1) from _call_incrskill_112
    call incrdesire ("Sarena", handskill) from _call_incrdesire_113
    pause
    jump passtime
label tryfirstvideo:
    if Gymclothes in inventory.items:
        s "Aaah, you've got your gear! Now, we can do it!"
        jump devsp3
    elif True:
        s "If you want to join me, you'd need gym clothes!"
        mc "Where can I find that?"
        s "Well, I guess you can order one on the internet and make it delivered to home."
        "" "Go to the computer and order gym clothes."
        jump tobalcony

label sprepwork:
    $ qpreptalks = True
    mc "Hey [sn], what are you doing?"
    s "I'm setting up my camera for my future fans. Hahaha!"
    mc "Ah? What do you mean?"
    s "I'm bored of the typical life of studies and employment."
    s "I think this confinement presents a great opportunity to start a new activity and profit from it!"
    s "I wanna create content that teaches girls how to defend themselves. Plus more generic things like sports and well-being."
    mc "Ooooh, I see! You want to teach people how to become more like you, right? Haha"
    s "Yes! A Sarena Army to dominate all men. Mouahaha!"
    s "I may need you to participate, at some point, to take roles in my videos, like an aggressor or a partner."
    mc "I'd be glad to help you, [sn]!"
    s "Welcome, partner! We're going to make great stuff together!"
    if qpreptalkv == True and qpreptalkb == True and qpreptalke == True and qpreptalks == True:
        $ qpreptalk = True
        pause 1.0
    jump tobalcony
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
