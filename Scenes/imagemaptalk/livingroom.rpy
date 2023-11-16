screen living:

    imagemap:
        ground ifnight("House/living/bg livingroom.webp")

        if spos == "livingroom":
            imagebutton:
                idle "House/living/living b2.webp"
                hover lumi("House/living/living b2.webp")
                focus_mask True
                action Jump("lrs")
        add "lumitv"
        if daytimenumber == 3:
            if bstep > 0 or sstep > 0 or estep > 0 or vstep > 0:
                imagebutton:
                    idle "House/living/livingwatchtv.webp"
                    hover lumi("House/living/livingwatchtv.webp")
                    focus_mask True
                    action Jump("tvbase")
        if daytimenumber == 3:
            imagebutton:
                idle "House/living/partytime.webp"
                hover lumi("House/living/partytime.webp")
                focus_mask True
                action Jump("party")


label tvwith:
    "" "This feature is ready to be used on the next update."
    jump toliving

image lumitv:
    "House/living/livingtv.webp"
    linear 0.5 alpha 0.4
    linear 0.5 alpha 1.0
    linear 0.2 alpha 0.7
    linear 0.2 alpha 1.0
    repeat

label lrs:
    scene bg livingroom
    show living b2
    menu:
        "Talk to [sn]" if True:
            jump lrstalk

label lrstalk:
    if sstep > 2:
        scene bg living1
        show sarena at right
        show mc at left
        mc "Hey! How you doin'?"
        s "Just looking at my content's feedback."
        s "We've got so many comments!"
        s "I got some messages from girls asking me how I can take such a monster, haha!"
        $ persistent.replay86 = True
        jump evsarsexliving

    s "Rhooo, why are you always so mad at me?!"
    s "Stop yelling!"
    "" "[sn] is talking to her girlfriend on her computer."
    menu:
        "What do you do?"
        "Wait until the end of her call." if True:
            scene black with fade
            "" "A few minutes later..."
            scene bg living1
            show sarena sad at right
            show mc at left
            mc "Hey [sn]... Are you alright?"
            s "Yeah... I'm sorry, my girlfriend was mad at me again..."
            s "She is always mad and never stops yelling at me..."
            mc "It must be hard. Is it because of the quarantine?"
            s "It is, but... it also started even before that... it has become unbearable."
            show mc:
                linear 0.5 xalign 0.4
            mc "If you don't feel good, I'm here. It will always be a good time with your [mc]!"
            if sstep == 0:
                show sarena happy
                s "Indeed haha! Thanks! I wonder what I'd do without you hehe!"
                jump toliving
            elif sstep ==1:
                show sarena happy:
                    linear 0.5 xalign 0.65
                s "[mc]..."
                show shugliving:
                    xalign 0.5
                show shugliving at angryjump
                pause
                s "[mc]!!!"
                s "You're so important in my life!"
                s "You're always there to give my smile again..."
                s "I know you would never let me down."
                s "Never forget your [ssn] will also stay by your sides, forever!"
                mc "It makes me happy!"
                play audio spony
                s "My pony!!!"
                mc "[sn]!!!"
                s "Hehehe!"
                call incrdesire ("Sarena", 1) from _call_incrdesire_73
                jump passtime
            elif sstep ==2:
                show sarena happy:
                    linear 0.5 xalign 0.65
                s "[mc]!"
                show shugliving:
                    xalign 0.5
                show shugliving at angryjump
                pause
                s "[mc]!"
                s "You always make my day better!"
                play audio spony
                s "My pony!!!"
                mc "[sn]!!!"
                show 021a at angryjump
                pause
                s "Hm..."
                s "You taste so good..."
                s "I wanna fuck you so hard..."
                scene bg living1
                show sarena shy at right
                show mc shy at left
                s "Oh!!"
                s "I'm sorry [mc], I didn't intend to say that!"
                s "Let's please act like you never heard it!"
                mc "O-okay."
                call incrdesire ("Sarena", 2) from _call_incrdesire_74
                jump passtime
        "Step back" if True:
            jump toliving
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
