define nextsteptitle = "[desc]"

image closeui2:
    "ui/closeui.webp"
    zoom 0.8
image closeui2hover:
    "ui/closeui h.webp"
    zoom 0.8
screen girlsstats:
    zorder 2
    modal True
    frame:
        imagemap:
            ground "ui/girlsstats ui.webp"
            imagebutton:
                xalign 1.0
                yalign 0.0
                idle "closeui2"
                hover "closeui2hover"
                focus_mask True
                action Jump(lastmapcall)

        hbox:

            vbox:
                xpos 40
                xsize 420
                null height 20
                text "[s]" size 50 bold True xalign 0.5 outlines [ (3, "#1b1b1b", 3, 2) ]
                null height 20
                hbox xalign 0.0:
                    add "House/maps/sminiature.webp"
                    vbox:
                        text "Your [ssn]" xalign 0.1 size 25 yalign 0.0 bold True italic True outlines [ (1, "#1b1b1b", 0.5, 0.5) ]
                        textbutton "Change surname" text_style "changenamestyle" text_hover_color "#bb5d56" action Jump("renames")

                null height 50
                text "Progression step: {b}[sstep]{/b}" xalign 0.5 size 30 yalign 0.0 color "#000"
                text ssteps[sstep] size 25 color "#000" xalign 0.5
                null height 50
                text "Affection" color "#000" size 40 xalign 0.5 italic True
                text "With [bn]: [bbounds]/24" color "#000" size 30 xalign 0.5
                text "With [en]: [sbounde]/24" color "#000" size 30 xalign 0.5
                text "With [vn]: [vbounds]/24" color "#000" size 30 xalign 0.5

                null height 30
                text "You made her cum [scum] times." size 25 color "#000" xalign 0.5
                text "She made you cum [cumbys] times." size 25 color "#000" xalign 0.5

                null height 50
                if ispremiumversion == True:
                    text "Next task:" bold True size 30 color "#000" xalign 0.5 italic True
                    $ desc = slvhint[slv]
                    text "[desc]" size 25 color "#000" xalign 0.5


            null width 55
            vbox:
                xpos 40
                xsize 420
                null height 20
                text "[b]" size 50 bold True xalign 0.5 outlines [ (3, "#1b1b1b", 3, 2) ]
                null height 20
                hbox xalign 0.0:
                    add "House/maps/bminiature.webp"
                    vbox:
                        text "Your [bsn]" xalign 0.1 size 25 yalign 0.0 bold True italic True outlines [ (1, "#1b1b1b", 0.5, 0.5) ]
                        textbutton "Change surname" text_style "changenamestyle" text_hover_color "#bb5d56" action Jump("renameb")
                null height 50
                text "Progression step: {b}[bstep]{/b}" xalign 0.5 size 30 yalign 0.0 color "#000"
                text bsteps[bstep] size 25 color "#000" xalign 0.5
                null height 50
                text "Affection" color "#000" size 40 xalign 0.5 italic True
                text "With [sn]: [bbounds]/24" color "#000" size 30 xalign 0.5
                text "With [en]: [bbounde]/24" color "#000" size 30 xalign 0.5
                text "With [vn]: [bboundv]/24" color "#000" size 30 xalign 0.5
                null height 30
                text "You made her cum [bcum] times." size 25 color "#000" xalign 0.5
                text "She made you cum [cumbyb] times." size 25 color "#000" xalign 0.5
                null height 50
                if ispremiumversion == True:
                    text "Next task:" bold True size 30 color "#000" xalign 0.5 italic True
                    $ desc = blvhint[blv]
                    text "[desc]" size 25 color "#000" xalign 0.5

            null width 55

            vbox:
                xpos 40
                xsize 420
                null height 20
                text "[e]" size 50 bold True xalign 0.5 outlines [ (3, "#1b1b1b", 3, 2) ]
                null height 20
                hbox xalign 0.0:
                    add "House/maps/eminiature.webp"
                    vbox:
                        text "Your [esn]" xalign 0.1 size 25 yalign 0.0 bold True italic True outlines [ (1, "#1b1b1b", 0.5, 0.5) ]
                        textbutton "Change surname" text_style "changenamestyle" text_hover_color "#bb5d56" action Jump("renamee")
                null height 50
                text "Progression step: {b}[estep]{/b}" xalign 0.5 size 30 yalign 0.0 color "#000"
                text esteps[estep] size 25 color "#000" xalign 0.5
                null height 50
                text "Affection" color "#000" size 40 xalign 0.5 italic True
                text "With [bn]: [bbounde]/24" color "#000" size 30 xalign 0.5
                text "With [sn]: [sbounde]/24" color "#000" size 30 xalign 0.5
                text "With [vn]: [vbounde]/24" color "#000" size 30 xalign 0.5
                null height 30
                text "You made her cum [ecum] times." size 25 color "#000" xalign 0.5
                text "She made you cum [cumbye] times." size 25 color "#000" xalign 0.5
                null height 50
                if ispremiumversion == True:
                    text "Next task:" bold True size 30 color "#000" xalign 0.5 italic True
                    $ desc = elvhint[elv]
                    text "[desc]" size 25 color "#000" xalign 0.5

            null width 60

            vbox:
                xpos 40
                xsize 420
                null height 20
                text "[v]" size 50 bold True xalign 0.5 outlines [ (3, "#1b1b1b", 3, 2) ]
                null height 20
                hbox xalign 0.0:
                    add "House/maps/vminiature.webp"
                    vbox:
                        text "Your [vsn]" xalign 0.1 size 25 yalign 0.0 bold True italic True outlines [ (1, "#1b1b1b", 0.5, 0.5) ]
                        textbutton "Change surname" text_style "changenamestyle" text_hover_color "#bb5d56" action Jump("renamev")
                null height 50
                text "Progression step: {b}[vstep]{/b}" xalign 0.5 size 30 yalign 0.0 color "#000"
                text vsteps[vstep] size 25 color "#000" xalign 0.5
                null height 50
                text "Affection" color "#000" size 40 xalign 0.5 italic True
                text "With [bn]: [bboundv]/24" color "#000" size 30 xalign 0.5
                text "With [sn]: [vbounds]/24" color "#000" size 30 xalign 0.5
                text "With [en]: [vbounde]/24" color "#000" size 30 xalign 0.5
                null height 30
                text "You made her cum [vcum] times." size 25 color "#000" xalign 0.5
                text "She made you cum [cumbyv] times." size 25 color "#000" xalign 0.5
                null height 50
                if ispremiumversion == True:
                    text "Next task:" bold True size 30 color "#000" xalign 0.5 italic True
                    $ desc = vlvhint[vlv]
                    text "[desc]" size 25 color "#000" xalign 0.5


label renames:
    show sarena
    $ ssn = renpy.input("Write her new surname. Currently: [ssn]")
    $ ssn = ssn.strip()
    if ssn == "":
        $ ssn = "Best friend"
    $ ssn ="{color=#f95252}" + ssn +"{/color}"
    "" "[sn] is now called your \"[ssn]\"!"
    $ renpy.jump(lastmapcall)
    return
label renamee:
    show emma
    $ esn = renpy.input("Write her new surname. Currently: [esn]")
    $ esn = esn.strip()
    if esn == "":
        $ esn = "Girlfriend's best friend"
    $ esn ="{color=#4083ff}" + esn +"{/color}"
    "" "[en] is now called your \"[esn]\"!"
    $ renpy.jump(lastmapcall)
    return
label renameb:
    show berry
    $ bsn = renpy.input("Write her new surname. Currently: [bsn]")
    $ bsn = bsn.strip()
    if bsn == "":
        $ bsn = "Lovely teacher"
    $ bsn ="{color=#ff7ed3}" + bsn +"{/color}"
    "" "[bn] is now called your \"[bsn]\"!"
    $ renpy.jump(lastmapcall)
    return
label renamev:
    show valerie
    $ vsn = renpy.input("Write her new surname. Currently: [vsn]")
    $ vsn = vsn.strip()
    if vsn == "":
        $ vsn = "Dad's shrew"
    $ vsn ="{color=#ea48c2}" + vsn +"{/color}"
    "" "[vn] is now called your \"[vsn]\"!"
    $ renpy.jump(lastmapcall)
    return
style changenamestyle:
    size 25
    color "#fff"


init python:

    def fixlv():
        global blv
        global elv
        global slv
        global vlv
        if qpreptalkb == True and blv == 0:
            blv = 1
        if qpreptalke == True and elv == 0:
            elv = 1
        if qpreptalks == True and slv == 0:
            slv = 1
        if qpreptalkv == True and vlv == 0:
            vlv = 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
