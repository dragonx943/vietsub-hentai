screen playerstats:
    zorder 2
    modal True

    imagemap:
        ground "ui/playerstatsbg.webp"
        imagebutton:
            idle "ui/closeui.webp"
            hover "ui/closeui h.webp"
            focus_mask True
            action Jump(lastmapcall)


        text "[mc]" size 40 xalign 0.5 justify True bold True italic True ypos 65
        textbutton "(Change)" xalign 0.9 ypos 65 text_style "changenamestyle" text_hover_color "#bb5d56" action Jump("renamemc")

        vbox:
            pos (920, 190)
            xmaximum 400
            spacing 20
            text "{i}First times{/i}" size 40 bold True color "#113052"
            text "{i}Virginity lost with{/i}: [virginitylossby]" size 30 color "#113052"
            text "{i}First blowjob by{/i}: [firstbjby]" size 30 color "#113052"
            text "{i}First titsjob by{/i}: [firsttjby]" size 30 color "#113052"
            text "{i}First cunnilingus to{/i}: [firstcunto]" size 30 color "#113052"
            text "{i}Status: [mcstatus]{/i}" size 30 color "#113052"
        vbox:
            pos (1350, 190)
            xmaximum 500
            spacing 20
            text "[mc]'s feeling for girls" size 40 bold True

            if sstep == 0:
                text "[sn]: She's my best friend!" size 25 color "#113052"
            elif sstep == 1:
                text "[sn]: My body is now her new playground! This is disturbing, but I kind of love that!" size 25 color "#113052"
            elif sstep == 2:
                text "[sn]: She can do what she wants to me and I love that!" size 25 color "#113052"
            elif sstep == 3:
                text "[sn]: We love eachother and this will never change!" size 25 color "#113052"
            elif sstep == 4:
                text "[sn]: My bestfriend that fuck me whenever she wants!" size 25 color "#113052"

            if estep == 0:
                text "[en]: Infernal, but cute." size 25 color "#113052"
            if estep == 1:
                text "[en]: She is horny as fuck! it's also her weak point." size 25 color "#113052"
            if estep == 2:
                text "[en]: She loves to be a good girl." size 25 color "#113052"
            if estep == 3:
                if mcstatus == "Promised to Emma":
                    text "[en]: I love her, I promised her to become my official girlfriend." size 25 color "#113052"
                else:
                    text "[en]: I don't love her as much as she does, but I was transparent with her." size 25 color "#113052"
            if estep == 4:
                if ispromisedtoemma == True:
                    text "[en]: My lovely girlfriend." size 25 color "#113052"
                else:
                    text "[en]: I know she'd do anything for me" size 25 color "#113052"

            if vstep == 0:
                text "[vn]: I hate her! Why does she look so hot? I refuse to admit I like her body!" size 25 color "#113052"
            if vstep == 1:
                text "[vn]: I still hate her, however I could use the fact that she is horny to get my revenge!" size 25 color "#113052"
            if vstep == 2:
                text "[vn]: I love to see how she enjoys me more and more." size 25 color "#113052"
            if vstep == 3:
                text "[vn]: She's now my personal cumslut!." size 25 color "#113052"
            if vstep == 4:
                text "[vn]: We all can fuck her like a free slut!" size 25 color "#113052"

            if bstep == 0:
                text "[bn]: She's so sweet, I love how she takes care of me." size 25 color "#113052"
            if bstep == 1:
                text "[bn]: We are sharing affection in secret... She's making me feel so good." size 25 color "#113052"
            if bstep == 2:
                text "[bn]: I'm kind of \"scaroused\" by [bn]... But I have faith in her, I want to be there for her." size 25 color "#113052"
            if bstep == 3:
                text "[bn]: I chose to let [bn] take care of me for the rest of my life." size 25 color "#113052"
            if bstep == 4:
                text "[bn]: I would always obey her, in exchange for her unconditionnal love!" size 25 color "#113052"

        text "Hand\nskill\n\n{b}[handskill]{/}/[maxskill]" pos (510, 180) size 30 color "#113052" justify True
        text "Tongue\nskill\n\n{b}[tongueskill]{/}/[maxskill]" pos (625, 180) size 30 color "#113052" justify True
        text "Cock\nskill\n\n{b}[cockskill]{/}/[maxskill]" pos (750, 180) size 30 color "#113052" justify True

        text "{b}[money]${/b}" pos (1850, 920) size 80 xalign 1.0 color "#c68109"

        frame:

            background None
            ysize 220
            xsize 370
            pos (490, 410)
            text "Skills increase the amount of desire earned by the girls at some events.\nKeep looking for those evolving events!" size 28 xalign 0.5 color "#113052"


        hbox pos (520, 700) box_wrap True:
            xmaximum 1500

            spacing 30
            for i in inventory.items:
                vbox:
                    text i.name size 22 bold True color "#113052"
                    add i.imageref xzoom 0.4 yzoom 0.4 xalign 0.5

label renamemc:
    scene black
    show mc
    $ player_name = renpy.input("Write your new Name. Currently: [mc]")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Ero"

    "" "You are now called \"[mc]\"!"
    $ renpy.jump(lastmapcall)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
