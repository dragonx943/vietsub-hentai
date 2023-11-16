label evsarsexbalc2:
    scene black with fade
    pause 1.0
    scene balcony2talk with dissolve
    show sarena o2 at right
    show mc at left
    mc "Hey, I see you're working out on your upper body every single day."
    mc "What about your legs?"
    s "My legs? Did you just say that because my legs look small???"
    mcth "They're not, but... He he"
    s "That's not gonna happen!!!"
    s "And you're gonna give me a hand."
    s "On the ground!"
    s "Oh?"
    s "That's the cost for criticizing my legs!!!"
    call sarsexbalc2029 (1.0/12) from _call_sarsexbalc2029_1
    $ a = 1.0/12
    show sarsexbalc2:
        linear 5.0 yalign 1.0
        linear 5.0 yalign 0.0
    s "[mc]! You're a very nasty boy!"
    s "You actually knew I was going to do something like this!"
    s "Now you're not going anywhere until I finish my practice!"
    call devmenu029 from _call_devmenu029
    return

label evsarsexbalc2b:
    call sarsexbalc2029 (1.0/18) from _call_sarsexbalc2029_2
    s "Oh I'm getting crazy on your prick!"
    s "I NEED it!"
    s "I need to drain every drop of cum from your balls!"
    call devmenu029b from _call_devmenu029b
    return

label evsarsexbalc2c:
    call sarsexbalc2cum029 from _call_sarsexbalc2cum029_2
    s "I'm cumming so hard!!!"
    pause
    show sarsexbalc2-aftercum with fade
    play audio spony
    s "My pony!"
    s " You really like it when I ride you like a wild animal, do you!"
    s "I'm so loaded with your semen right now..."
    pause
    $ scum+=1
    $ cumbys+=1
    call incrskill ("cockskill", 3) from _call_incrskill_9
    call incrdesire ("Sarena", cockskill) from _call_incrdesire_11
    jump passtime

label devmenu029:
    menu:
        "Look at her face (Press H to hide it)" if True:
            call devlook1029 from _call_devlook1029
        "Look at her chest (Press H to hide it)" if True:
            call devlook2029 from _call_devlook2029
        "Look at her bottom (Press H to hide them)" if True:
            call devlook3029 from _call_devlook3029
        "Next" if True:
            jump evsarsexbalc2b
label devmenu029b:
    menu:
        "Look at her face (Press H to hide it)" if True:
            call devlook1029 (1.0/18) from _call_devlook1029_1
        "Look at her chest (Press H to hide)" if True:
            call devlook2029 (1.0/18) from _call_devlook2029_1
        "Look at her bottom (Press H to hide)" if True:
            call devlook3029 (1.0/18) from _call_devlook3029_1
        "Next" if True:
            jump evsarsexbalc2c

label devlook1029(a=1.0/12):
    $ animspeed = a
    hide window
    show sarsexbalc2:
        linear 3.0 yalign 0.0
    if a == 1.0/12:
        pause 0.4
        play sexfx sex10
        play sex ssoftmoans2
    elif a == 1.0/18:
        pause 0.2
        play sexfx sex066
        play sex shardmoans1
    pause
    window auto
    if a == 1.0/12:
        call devmenu029 from _call_devmenu029_1
    elif True:
        call devmenu029b from _call_devmenu029b_1
label devlook2029(a=1.0/12):
    $ animspeed = a
    hide window
    show sarsexbalc2:
        linear 3.0 yalign 0.5
    if a == 1.0/12:
        pause 0.4
        play sexfx sex10
        play sex ssoftmoans2
    elif a == 1.0/18:
        pause 0.2
        play sexfx sex066
        play sex shardmoans1
    pause
    window auto
    if a == 1.0/12:
        call devmenu029 from _call_devmenu029_2
    elif True:
        call devmenu029b from _call_devmenu029b_2

label devlook3029(a=1.0/12):
    $ animspeed = a
    hide window
    show sarsexbalc2:
        linear 3.0 yalign 1.0
    if a == 1.0/12:
        pause 0.4
        play sexfx sex10
        play sex ssoftmoans2
    elif a == 1.0/18:
        pause 0.2
        play sexfx sex066
        play sex shardmoans1
    pause
    window auto
    if a == 1.0/12:
        call devmenu029 from _call_devmenu029_3
    elif True:
        call devmenu029b from _call_devmenu029b_3
label devlook4029(a=1.0/12):
    $ animspeed = a
    hide window
    show sarsexbalc2:
        linear 3.0 yalign 1.0
    if a == 1.0/12:
        pause 0.4
        play sexfx sex10
        play sex ssoftmoans2
    elif a == 1.0/18:
        pause 0.2
        play sexfx sex066
        play sex shardmoans1
    pause
    window auto
    if a == 1.0/12:
        call devmenu029 from _call_devmenu029_4
    elif True:
        call devmenu029b from _call_devmenu029b_4
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
