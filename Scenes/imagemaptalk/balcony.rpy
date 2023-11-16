screen balcony:
    imagemap:
        if daytimenumber <3:
            ground "House/1stfloor/bg balcony.webp"
        else:
            ground "0.3.1/bg balcony evening.webp"
        if spos == "balcony" and daytimenumber == 0:
            imagebutton:
                idle "House/1stfloor/sbalcony1.webp"
                hover lumi("House/1stfloor/sbalcony1.webp")
                focus_mask True
                action Jump("balctalks")
        if spos == "balcony" and isendmode == True:
            imagebutton:
                idle "0.3.1/bgbalconyendsarena.webp"
                hover lumi("0.3.1/bgbalconyendsarena.webp")
                xalign 0.0
                yalign 0.0
                xpos 1307
                ypos 154
                action Jump("roasarenaend")

label balctalks:
    scene bg balcony
    show sbalcony1
    if slv == 6:
        jump devsp7
    menu:
        "What to do?"
        "{color=#ff9a40}Ask her what she's doing.{/color} Orange color = Quest" if qpreptalks == False and slv == 0:
            jump sprepwork
        "Hug her." if True:
            jump sarbalcstep0
        "Talk" if True:
            jump talks
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
