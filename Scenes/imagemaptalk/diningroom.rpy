screen diningroom:
    imagemap:
        if daytimenumber > 2:
            ground night("House/diningroom/bg diningroom.webp")
        else:
            ground "House/diningroom/bg diningroom.webp"
        if epos == "diningroom":
            imagebutton:
                idle "House/diningroom/dininge.webp"
                hover lumi("House/diningroom/dininge.webp")
                focus_mask True
                action Jump("dre")
        if daytimenumber == 2:
            imagebutton:
                idle "House/diningroom/dinnertime.webp"
                hover lumi("House/diningroom/dinnertime.webp")
                focus_mask True
                action Jump("dinnertime")
        if isendmode == False and bstep==3 and sstep ==3 and vstep==3 and estep ==3:
            imagebutton:
                idle ifnight("0.3.1/drroomicon.webp")
                hover lumi("0.3.1/drroomicon.webp")
                pos (399,533)
                action Jump("endp1")

label dre:
    scene bg diningroom
    show dininge
    menu:
        "What to do?"
        "Talk to her. ([estep])" if True:
            if estep == 0:
                jump dretalk0
            elif estep == 1:
                jump dretalk1
            elif estep == 2:
                scene diningroomtalk
                show mc at left
                show emma shy at right
                e "Hey [mc], how are you?"
                mc "Whut? Since when are you asking me if I'm alright?"
                show emma base
                e "Tsah! I didn't mean it, just being polite."
                jump todiningroom
            elif estep > 2:
                scene diningroomtalk
                show mc at left
                show emma happy at right
                e "Hey [mc], how are you?"
                mc "I'm always fine when I see you [en]!"
                e "Hehehe, stop being so cute, or I'll marry you!"
                jump todiningroom
        "Stare at her." if estep <3:
            jump emmdinstep0
        "Go under the table" if estep > 1:
            scene elv2liv with fade
            pause
            e "[mc]!"
            e "What are you d-"
            e "Oh gosh!"
            mc "Your pussy is so tasty, I miss it all the time!"
            e "Don't say that!"
            e "You're always doing such things as if you could make me-"
            play sound ecum3
            show elv2liv at cumtr
            show elv2livcum at cumtr
            show cumanim
            e "Make me cuuuuum all the tiiiiime!!!"
            e "You're so goood at it!!"
            pause
            $ ecum += 1
            call incrskill ("tongueskill", 2) from _call_incrskill_113
            call incrdesire ("Emma", tongueskill) from _call_incrdesire_114
            jump passtime
        "Kiss her by surprise." if estep > 2:
            play sex ekiss
            window hide
            show deve12 with hpunch
            pause
            window auto
            e "!!!"
            e "What are you d-"
            e "Mmmh!"
            "" "After a second, [en] grabs you by your neck and pushes her tongue deep into your mouth."
            "" "She's loving it, to the point of trying to eat your soul."
            stop sex
            call incrskill ("tongueskill", 3) from _call_incrskill_114
            call incrdesire ("Emma", tongueskill) from _call_incrdesire_115
            jump passtime

        "{color=#ff9a40}Why does she look mad?{/color}" if elv == 3:
            jump devep4
        "{color=#ff9a40}Propose her to take a photo for her.{/color}" if elv == 5:
            jump devep6
        "Step back." if True:
            jump todiningroom

label dretalk0:
    scene diningroomtalk
    show mc at left
    show emma at right
    mc "Hey!"
    play sound esoupir
    e "Why are you always bothering me?"
    mc "What are you doing?"
    e "Just looking at my subs' feedback."
    mc "Feedback about?"
    e "None of your business."
    mc "ok..."
    jump todiningroom

label dretalk1:
    scene diningroomtalk
    show mc at left
    show emma at right
    mc "Hey!"
    play sound esoupir
    e "Why are you always bothering me?"
    mc "What are you doing?"
    e "Just looking at my subs' feedback."
    mc "What are their feedback about our content?"
    e "\"Our\" ?! I'm the only one who shines!"
    mc "ok..."
    e "They love it, but they all are so perverts, they seem unsatisfied by my beautiful face only..."
    mc "Are you thinking about showing more?"
    e "Ha? Never! These are just a bunch of losers like you!"
    mc "Oh come on, they're giving you support. Couldn't you respect them a little bit more?"
    e "... I guess."
    e "Not leave me alone."
    jump todiningroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
