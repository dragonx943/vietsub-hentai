screen girlsstats2:
    zorder 2
    modal True

    imagemap:
        ground "ui/girlsstats ui.webp"
        imagebutton:
            xalign 1.0
            yalign 0.0
            idle "closeui2"
            hover "closeui2hover"
            focus_mask True
            action Jump(lastmapcall)
    frame:
        xmargin 25
        background None
        has hbox:
            spacing 57

        vbox:

            xsize 420
            frame:

                background None
                ysize 200
                xsize 420
                has vbox
                null height 10
                text "[s]" size 50 bold True xalign 0.7 outlines [ (5, "#1b1b1b", 3, 2) ]
                null height 10
                hbox xalign 0.0:
                    add "House/maps/sminiature.webp"
                    vbox:
                        text "Your [ssn]" xalign 0.1 size 25 yalign 0.0 bold True italic True outlines [ (1, "#1b1b1b", 0.5, 0.5) ]
                        textbutton "Change surname" text_style "changenamestyle" text_hover_color "#bb5d56" action Jump("renames")

            null height 20
            frame:

                background None
                ysize 150
                xsize 420
                has vbox
                text "Progression step: {b}[sstep]{/b}" xalign 0.5 size 30 yalign 0.0 color "#ac1a1a"
                text "Desire: {b}[sdesire]/[desiremax]{/b}" xalign 0.5 size 25 yalign 0.0 color "#ac1a96"
                text ssteps[sstep] size 25 color "#000" xalign 0.5
            null height 30
            frame:

                background None
                ysize 150
                xsize 420
                has vbox xalign 0.5
                text "Affection" color "#000" size 30 xalign 0.5 italic True
                text "With [bn]: [bbounds]/24" color "#000" size 25 xalign 0.5
                text "With [en]: [sbounde]/24" color "#000" size 25 xalign 0.5
                text "With [vn]: [vbounds]/24" color "#000" size 25 xalign 0.5
            null height 10
            frame:

                background None
                ysize 70
                xsize 420
                has vbox xalign 0.5
                text "You made her cum [scum] times." size 25 color "#000" xalign 0.5
                text "She made you cum [cumbys] times." size 25 color "#000" xalign 0.5

            null height 30
            if ispremiumversion == True:
                frame:

                    background None
                    ysize 500
                    xsize 420
                    has vbox xalign 0.5
                    text "Next task:" bold True size 30 color "#000" xalign 0.5 italic True
                    $ desc = slvhint[slv]
                    if slv == 2 and sdesire < desireforstep1:
                        $ desc = "Required desire "+str(sdesire)+"/"+str(desireforstep1)
                    if slv == 8 and sdesire < desireforstep2:
                        $ desc = "Required desire "+str(sdesire)+"/"+str(desireforstep2)
                    if slv == 18 and sdesire < desireforstep3:
                        $ desc = "Required desire "+str(sdesire)+"/"+str(desireforstep3)
                    text "[desc]" size 25 color "#000" xalign 0.5

        vbox:

            xsize 420
            frame:

                background None
                ysize 200
                xsize 420
                has vbox
                null height 10
                text "[b]" size 50 bold True xalign 0.5 outlines [ (5, "#1b1b1b", 3, 2) ]
                null height 10
                hbox xalign 0.0:
                    add "House/maps/bminiature.webp"
                    vbox:
                        text "Your [bsn]" xalign 0.1 size 25 yalign 0.0 bold True italic True outlines [ (1, "#1b1b1b", 0.5, 0.5) ]
                        textbutton "Change surname" text_style "changenamestyle" text_hover_color "#bb5d56" action Jump("renameb")

            null height 20
            frame:

                background None
                ysize 150
                xsize 420
                has vbox
                text "Progression step: {b}[bstep]{/b}" xalign 0.5 size 30 yalign 0.0 color "#ac1a1a"
                text "Desire: {b}[bdesire]/[desiremax]{/b}" xalign 0.5 size 25 yalign 0.0 color "#ac1a96"
                text bsteps[bstep] size 25 color "#000" xalign 0.5
            null height 30
            frame:

                background None
                ysize 150
                xsize 420
                has vbox xalign 0.5
                text "Affection" color "#000" size 30 xalign 0.5 italic True
                text "With [sn]: [bbounds]/24" color "#000" size 30 xalign 0.5
                text "With [en]: [bbounde]/24" color "#000" size 30 xalign 0.5
                text "With [vn]: [bboundv]/24" color "#000" size 30 xalign 0.5
            null height 10
            frame:

                background None
                ysize 70
                xsize 420
                has vbox xalign 0.5
                text "You made her cum [bcum] times." size 25 color "#000" xalign 0.5
                text "She made you cum [cumbyb] times." size 25 color "#000" xalign 0.5

            null height 30
            if ispremiumversion == True:
                frame:

                    background None
                    ysize 500
                    xsize 420
                    has vbox xalign 0.5
                    text "Next task:" bold True size 30 color "#000" xalign 0.5 italic True
                    $ desc = blvhint[blv]
                    if blv == 2 and bdesire < desireforstep1:
                        $ desc = "Required desire "+str(bdesire)+"/"+str(desireforstep1)
                    if blv == 8 and bdesire < desireforstep2:
                        $ desc = "Required desire "+str(bdesire)+"/"+str(desireforstep2)
                    if blv == 15 and bdesire < desireforstep3:
                        $ desc = "Required desire "+str(bdesire)+"/"+str(desireforstep3)
                    text "[desc]" size 25 color "#000" xalign 0.5

        vbox:

            xsize 420
            frame:

                background None
                ysize 200
                xsize 420
                has vbox
                null height 10
                text "[e]" size 50 bold True xalign 0.7 outlines [ (5, "#1b1b1b", 3, 2) ]
                null height 10
                hbox xalign 0.0:
                    add "House/maps/eminiature.webp"
                    vbox:
                        text "Your [esn]" xalign 0.1 size 25 yalign 0.0 bold True italic True outlines [ (1, "#1b1b1b", 0.5, 0.5) ]
                        textbutton "Change surname" text_style "changenamestyle" text_hover_color "#bb5d56" action Jump("renamee")

            null height 20
            frame:

                background None
                ysize 150
                xsize 420
                has vbox
                text "Progression step: {b}[estep]{/b}" xalign 0.5 size 30 yalign 0.0 color "#ac1a1a"
                text "Desire: {b}[edesire]/[desiremax]{/b}" xalign 0.5 size 25 yalign 0.0 color "#ac1a96"
                text esteps[estep] size 25 color "#000" xalign 0.5
            null height 30
            frame:

                background None
                ysize 150
                xsize 420
                has vbox xalign 0.5
                text "Affection" color "#000" size 30 xalign 0.5 italic True
                text "With [bn]: [bbounde]/24" color "#000" size 30 xalign 0.5
                text "With [sn]: [sbounde]/24" color "#000" size 30 xalign 0.5
                text "With [vn]: [vbounde]/24" color "#000" size 30 xalign 0.5
            null height 10
            frame:

                background None
                ysize 70
                xsize 420
                has vbox xalign 0.5
                text "You made her cum [ecum] times." size 25 color "#000" xalign 0.5
                text "She made you cum [cumbye] times." size 25 color "#000" xalign 0.5

            null height 30
            if ispremiumversion == True:
                frame:

                    background None
                    ysize 500
                    xsize 420
                    has vbox xalign 0.5
                    text "Next task:" bold True size 30 color "#000" xalign 0.5 italic True
                    $ desc = elvhint[elv]
                    if elv == 2 and edesire < desireforstep1:
                        $ desc = "Required desire "+str(edesire)+"/"+str(desireforstep1)
                    if elv == 8 and edesire < desireforstep2:
                        $ desc = "Required desire "+str(edesire)+"/"+str(desireforstep2)
                    if elv == 15 and edesire < desireforstep3:
                        $ desc = "Required desire "+str(edesire)+"/"+str(desireforstep3)
                    text "[desc]" size 25 color "#000" xalign 0.5

        vbox:

            xsize 420
            frame:

                background None
                ysize 200
                xsize 420
                has vbox
                null height 10
                text "[v]" size 50 bold True xalign 0.7 outlines [ (5, "#1b1b1b", 3, 2) ]
                null height 10
                hbox xalign 0.0:
                    add "House/maps/vminiature.webp"
                    vbox:
                        text "Your [vsn]" xalign 0.1 size 25 yalign 0.0 bold True italic True outlines [ (1, "#1b1b1b", 0.5, 0.5) ]
                        textbutton "Change surname" text_style "changenamestyle" text_hover_color "#bb5d56" action Jump("renamev")

            null height 20
            frame:

                background None
                ysize 150
                xsize 420
                has vbox
                text "Progression step: {b}[vstep]{/b}" xalign 0.5 size 30 yalign 0.0 color "#ac1a1a"
                text "Desire: {b}[vdesire]/[desiremax]{/b}" xalign 0.5 size 25 yalign 0.0 color "#ac1a96"
                text vsteps[vstep] size 25 color "#000" xalign 0.5
            null height 30
            frame:

                background None
                ysize 150
                xsize 420
                has vbox xalign 0.5
                text "Affection" color "#000" size 30 xalign 0.5 italic True
                text "With [bn]: [bboundv]/24" color "#000" size 30 xalign 0.5
                text "With [sn]: [vbounds]/24" color "#000" size 30 xalign 0.5
                text "With [en]: [vbounde]/24" color "#000" size 30 xalign 0.5
            null height 10
            frame:

                background None
                ysize 70
                xsize 420
                has vbox xalign 0.5
                text "You made her cum [vcum] times." size 25 color "#000" xalign 0.5
                text "She made you cum [cumbyv] times." size 25 color "#000" xalign 0.5

            null height 30
            if ispremiumversion == True:
                frame:

                    background None
                    ysize 500
                    xsize 420
                    has vbox xalign 0.5
                    text "Next task:" bold True size 30 color "#000" xalign 0.5 italic True
                    $ desc = vlvhint[vlv]
                    if vlv == 2 and vdesire < desireforstep1:
                        $ desc = "Required desire "+str(vdesire)+"/"+str(desireforstep1)
                    if vlv == 9 and vdesire < desireforstep2:
                        $ desc = "Required desire "+str(vdesire)+"/"+str(desireforstep2)
                    if vlv == 17 and vdesire < desireforstep3:
                        $ desc = "Required desire "+str(vdesire)+"/"+str(desireforstep3)
                    text "[desc]" size 25 color "#000" xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
