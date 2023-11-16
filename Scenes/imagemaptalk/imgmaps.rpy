
define floor = 1
init python:
    def genericmap():
        
        
        
        
        renpy.music.set_volume(1.0, delay=0, channel='music')
        renpy.hide_screen("minimap1")
        renpy.hide_screen("minimap2")
        renpy.show_screen("Day")
        renpy.show_screen("minimapbutton")
        renpy.show_screen("playerstatsbutton")
        renpy.show_screen("girlsstatsbutton")
        
        
        
        renpy.music.stop("sexfx")
        renpy.hide_screen("notifglobal")
        _window_auto = True
    def hideui():
        renpy.hide_screen("uimap")
        renpy.hide_screen("minimap1")
        renpy.hide_screen("minimap2")


screen uimap:
    zorder 2

    null
    use Day
    use minimapbutton
    use playerstatsbutton
    use girlsstatsbutton
    if bstep > 2 or sstep > 2 or estep > 2 or vstep > 2:
        use endingbutton

screen playerstatsbutton:
    zorder 1
    imagebutton:
        auto "mcstats_%s.webp" pos (500,13)

        action Jump("playerstatsop")
label playerstatsop:
    call screen playerstats
    return

label girlsstatsop:
    $ actubounds()
    call screen girlsstats2
    return

screen girlsstatsbutton:
    zorder 1
    imagebutton:
        auto "girlsstats_%s.webp" pos (800,13)

        action [fixlv(),Jump("girlsstatsop")]
screen endingbutton:
    zorder 1
    imagebutton:
        idle "ending button" pos (1100,13)
        hover lumi("ui/ending button.webp")
        action [Jump("endingpanel")]
label endingpanel:
    call screen endingscreen

screen minimap1:
    zorder 2
    modal True

    imagemap:
        ground ifnight("House/maps/map plan rdc.webp")
        imagebutton:
            yalign 1.0
            offset (640,-195)
            idle ifnight( "House/maps/map living.webp")
            hover lumi("House/maps/map living.webp")

            action Jump("toliving")
        imagebutton:
            yalign 0.0
            offset (1251,0)
            idle ifnight( "House/maps/map kitchen.webp")
            hover lumi("House/maps/map kitchen.webp")

            action Jump("tokitchen")

        imagebutton:
            xalign 1.0 yalign 1.0
            offset (0,0)
            idle ifnight( "House/maps/map backyard.webp")
            hover lumi("House/maps/map backyard.webp")

            action Jump("tobackyard")
        imagebutton:
            yalign 0.0
            offset (861,0)
            idle ifnight( "House/maps/map diningroom.webp")
            hover lumi("House/maps/map diningroom.webp")

            action Jump("todiningroom")
        imagebutton:
            yalign 1.0
            offset (481,-6)
            idle ifnight( "House/maps/map floor2.webp")
            hover lumi("House/maps/map floor2.webp")

            action [Show("minimap2", dissolve), Hide("minimap1")]
        imagebutton:
            xalign 0.0 yalign 1.0
            offset (0,0)
            idle ifnight( "House/maps/map frontyard.webp")
            hover lumi("House/maps/map frontyard.webp")

            action Jump("tofrontyard")
        imagebutton:
            yalign 0.0
            offset (196,0)
            idle ifnight( "House/maps/map mcroom.webp")
            hover lumi("House/maps/map mcroom.webp")

            action Jump("tomcroom")
        imagebutton:
            xalign 0.0 yalign 0.0
            offset (0,0)
            idle ifnight( "House/maps/map valerieroom.webp")
            hover lumi("House/maps/map valerieroom.webp")

            action Jump("tovalerieroom")
        imagebutton:
            yalign 0.0
            offset (673,0)
            idle ifnight( "House/maps/map bathroom.webp")
            hover lumi("House/maps/map bathroom.webp")

            action Jump("tobathroom")
        imagebutton:
            xalign 0.98
            yalign 0.02

            idle "House/maps/close minimap1.webp"
            hover lumi( "House/maps/close minimap1.webp")

            action Jump(lastmapcall)



        add "bminiature" at location1(bpos)
        add "eminiature" at location1(epos)
        add "sminiature" at location1(spos)
        add "vminiature" at location1(vpos)
        if Gymclothes.receive == True:
            add "colis icon" yalign 0.6
        if Tsounade.receive == True:
            add "colis icon" yalign 0.6
        if Swimwear.receive == True:
            add "colis icon" yalign 0.6
        if Toolkit.receive == True:
            add "colis icon" yalign 0.6
        if blv == 16:
            add "colis icon" yalign 0.6

        add "mcroomreplay" pos (370,350) xzoom 0.6 yzoom 0.6
        if daytimenumber == 2:
            add "House/maps/dinnertime2.webp" pos (907, 182)
        if daytimenumber == 0:
            if bstep > 0 or sstep > 0 or estep > 0 or vstep > 0:
                add "House/maps/cookwith2.webp" pos (1280, 12)
        if daytimenumber == 3:
            add "House/maps/partytime2.webp" pos (650,600)
        if daytimenumber == 1:
            if bstep > 0 or sstep > 0 or estep > 0 or vstep > 0:
                add "House/maps/bg backyard jaccwith2.webp" pos (1485, 807)
            if bstep == 4:
                add "House/maps/iminiature.webp" pos (494, 632) align (0.5,0.5)
        if daytimenumber == 3:
            if bstep > 0 or sstep > 0 or estep > 0 or vstep > 0:
                add "House/maps/livingwatchtv2.webp" pos (1072, 880)
        if eventmcroom("mcroom") == True:
            add "indic2" at indicmcroom
        if eventmcroom("bathroom") == True:
            add "indic2" at indicbathroom
        if eventmcroom("valerieroom") == True:
            add "indic2" at indicvalerieroom
        if eventmcroom("kitchen") == True:
            add "indic2" at indickitchen
        if eventmcroom("backyard") == True:
            add "indic2" at indicbackyard
        if eventmcroom("livingroom") == True:
            add "indic2" at indiclivingroom
        if eventmcroom("diningroom") == True:
            add "indic2" at indicdiningroom






init python:
    def eventmcroom(eventname):
        ret = False
        if eventname == "mcroom":
            if devzoe1ok == False and daytimenumber == 3:
                if estep > 1 or vstep >1 or sstep >1 or bstep >1:
                    ret = True
            if vlv ==11 and daytimenumber ==2:
                ret = True
            if vlv==12 and Toolkit in inventory.items:
                ret = True
        if eventname == "bathroom":
            if vlv == 7 and daytimenumber == 2:
                ret = True
        if eventname == "valerieroom":
            if elv==16 and daytimenumber==2:
                ret = True
            if daytimenumber==3 and (vlv==2 or vlv==4 or vlv==9 or vlv==13 or vlv==14 or vlv==17 or vlv==18):
                ret = True
            if daytimenumber==2 and vlv==10:
                ret = True
            if qpreptalkv == False and vlv == 0 and daytimenumber ==3:
                ret = True
        
        if eventname == "kitchen":
            if  daytimenumber == 0 and blv == 6:
                ret = True
            if (slv == 8 and sdesire >= desireforstep2) or slv==11:
                ret = True
        if eventname == "backyard":
            
            if daytimenumber == 2 and blv == 9:
                ret = True
            if daytimenumber == 3 and (slv == 3):
                ret = True
            if slv == 18 and sdesire >= desireforstep3 and daytimenumber == 3:
                ret = True
            if daytimenumber ==1 and (elv==6):
                ret = True
            if daytimenumber == 0 and (vlv == 6 or vlv==20):
                ret = True
        
        if eventname == "livingroom":
            if firstparty == False and blv > 0 and vlv > 0 and elv > 0 and slv > 0 and daytimenumber == 3:
                ret = True
            if daytimenumber == 3 and blv==12:
                ret = True
            if slv ==14:
                ret = True
        if eventname == "diningroom":
            if daytimenumber == 0 and (elv==3 or elv==5):
                ret = True
        
        
        
        
        if eventname == "berryroom":
            if  daytimenumber == 1 and (blv==0 or (blv==2 and bdesire>=desireforstep1) or blv==3 or (blv==5 and Tsounade in inventory.items) or (blv==8 and bdesire>=desireforstep2) or blv==11 or blv==17):
                ret = True
            if qpreptalkb == False and blv == 0 and daytimenumber == 1:
                ret = True
        if eventname == "pcroom":
            if  blv == 10 or slv==13 or vlv==3 or (vlv==12 and Toolkit.command == False and Toolkit.receive == False and Toolkit not in inventory.items):
                ret = True
            if (daytimenumber == 2 and elv==2 and edesire>=desireforstep1) or (elv==4) :
                ret = True
            if (daytimenumber == 2 and elv==8 and edesire>=desireforstep2):
                ret = True
            if qpreptalke == False and elv == 0 and daytimenumber == 2:
                ret = True
            if (blv==5 and Tsounade.command == False and Tsounade.receive == False and Tsounade not in inventory.items):
                ret = True
            if elv ==4:
                ret = True
        
        if eventname == "girlsroom":
            if (slv == 9 and daytimenumber == 3) or elv==7 or elv==9 or(elv==10 and daytimenumber==0):
                ret = True
            if (elv == 15 and edesire >= desireforstep3 and daytimenumber == 0) or (elv==18 and daytimenumber==1):
                ret = True
        
        if eventname == "hallway":
            if daytimenumber == 3 and blv == 7:
                ret = True
        if eventname == "balcony":
            if daytimenumber == 0 and (slv==0 or (slv==2 and sdesire>=desireforstep1) or slv==4 or slv==6 or slv==7 or slv==10 or slv==20):
                ret = True
            if qpreptalks == False and slv == 0 and daytimenumber == 0:
                ret = True
        return ret




transform indicmcroom:
    xanchor 0.5
    yanchor 0.5
    pos (500, 201)
transform indicbathroom:
    xanchor 0.5
    yanchor 0.5
    pos (770, 201)
transform indicvalerieroom:
    xanchor 0.5
    yanchor 0.5
    pos (63, 335)

transform indickitchen:
    xanchor 0.5
    yanchor 0.5
    pos (1517, 222)
transform indicbackyard:
    xanchor 0.5
    yanchor 0.5
    pos (1825, 818)
transform indiclivingroom:
    xanchor 0.5
    yanchor 0.5
    pos (1125, 700)
transform indicdiningroom:
    xanchor 0.5
    yanchor 0.5
    pos (1000, 201)


label toliving:

    $ floor = 1
    $ lastmapcall = "toliving"
    if spos == "livingroom" and slv == 14:
        jump devsp15
    if blv == 12 and bpos == "livingroom":
        jump devbp13
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screennotifglobal
    call screen living with dissolve
    return
label tovalerieroom:
    $ floor = 1
    $ lastmapcall = "tovalerieroom"
    if vlv == 2 and vpos == "valerieroom" and vdesire >= desireforstep1:
        jump devvp3
    if vlv == 9 and vpos == "valerieroom" and vdesire >= desireforstep2:
        jump devvp10
    if vlv == 13 and vpos == "valerieroom":
        jump devvp14
    if vlv == 14 and vpos == "valerieroom":
        jump devvp15
    if elv == 16 and epos == "valerieroom":
        jump devep17
    if vlv == 17 and vpos == "valerieroom" and vdesire >= desireforstep3:
        jump devvp18
    if vlv == 18 and vpos == "valerieroom":
        jump devvp19
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen valerieroom with dissolve
    return
label tomcroom:
    $ floor = 1
    $ lastmapcall = "tomcroom"
    if vlv == 11 and vpos == "mcroom":
        jump devvp12
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen mcroom with dissolve
    return
label todiningroom:
    $ floor = 1
    $ lastmapcall = "todiningroom"
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen diningroom with dissolve
    return


label tokitchen:
    $ floor = 1
    $ lastmapcall = "tokitchen"
    if bpos == "kitchen" and blv == 6:
        jump devbp7
    if spos == "kitchen":
        if slv == 8 and sdesire >= desireforstep2:
            jump devsp9
        elif slv == 11:
            jump devsp12
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen kitchen with dissolve
    return

label tobathroom:
    $ floor = 1
    $ lastmapcall = "tobathroom"
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen bathroom with dissolve
    return

label tobackyard:
    $ floor = 1
    $ lastmapcall = "tobackyard"
    if blv == 9 and bpos == "backyard":
        jump devbp10
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen backyard with dissolve
    return
label tofrontyard:
    $ floor = 1
    $ lastmapcall = "tofrontyard"
    scene black
    if daytimenumber == 1 and bstep == 4:
        jump isabelleentrance
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen frontyard with dissolve
    return
label topcroom:
    $ floor = 2
    $ lastmapcall = "topcroom"
    if spos == "pcroom" and slv == 13:
        jump devsp14
    if epos == "pcroom" and elv == 8 and edesire >= desireforstep2:
        jump devep9
    if blv == 10:
        jump devbp11
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    if epos == "pcroom" and daytimenumber == 2 and firstlookonemma == False:
        jump emmapresence
    elif True:
        call screen pcroom with dissolve
    return

screen minimapbutton:
    zorder 1
    if floor == 1:
        imagebutton:
            pos (1750,13)
            idle "House/maps/Open map1.webp"
            hover lumi("House/maps/Open map1.webp")

            action Show("minimap1")
    else:
        imagebutton:
            pos (1750,13)
            idle "House/maps/Open map1.webp"
            hover lumi("House/maps/Open map1.webp")

            action Show("minimap2")




label openminimap2:
    call screen minimap2
    return

screen minimap2:
    zorder 2
    modal True

    imagemap:
        ground ifnight("House/maps/map plan 1.webp")
        imagebutton:
            yalign 1.0
            offset (1500,-40)
            idle ifnight("House/maps/map balcony.webp")
            hover lumi( "House/maps/map balcony.webp")

            action Jump("tobalcony")
        imagebutton:
            offset (218,543)
            idle ifnight("House/maps/map balcony2.webp")
            hover lumi( "House/maps/map balcony2.webp")

            action Jump("tobalcony2")
        imagebutton:
            yalign 1.0
            offset (1077,-20)
            idle ifnight("House/maps/map hallway.webp")
            hover lumi( "House/maps/map hallway.webp")

            action Jump("tohallway")
        imagebutton:
            yalign 0.0
            offset (1186,0)
            idle ifnight("House/maps/map girlsroom.webp")
            hover lumi( "House/maps/map girlsroom.webp")

            action Jump("togirlsroom")
        imagebutton:
            offset (995,150)
            idle ifnight("House/maps/map pcroom.webp")
            hover lumi( "House/maps/map pcroom.webp")

            action Jump("topcroom")
        imagebutton:
            yalign 0.0
            offset (342,0)
            idle ifnight("House/maps/map berryroom.webp")
            hover lumi( "House/maps/map berryroom.webp")

            action Jump("toberryroom")
        imagebutton:
            yalign 1.0
            offset (660,-20)
            idle ifnight("House/maps/map floor1.webp")
            hover lumi( "House/maps/map floor1.webp")

            action [Show("minimap1", dissolve),Hide("minimap2")]


        imagebutton:
            xalign 0.98
            yalign 0.02
            idle "House/maps/close minimap1.webp"
            hover lumi( "House/maps/close minimap1.webp")

            action Jump(lastmapcall)
        add "bminiature" at location2(bpos)
        add "eminiature" at location2(epos)
        add "sminiature" at location2(spos)
        add "vminiature" at location2(vpos)
        if eventmcroom("berryroom") == True:
            add "indic2" at indicberryroom
        if eventmcroom("pcroom") == True:
            add "indic2" at indicpcroom
        if eventmcroom("balcony") == True:
            add "indic2" at indicbalcony
        if eventmcroom("hallway") == True:
            add "indic2" at indichallway
        if eventmcroom("balcony2") == True:
            add "indic2" at indicbalcony2
        if eventmcroom("girlsroom") == True:
            add "indic2" at indicgirlsroom

transform indicberryroom:
    xanchor 0.5
    yanchor 0.5
    pos (904, 371)
transform indicpcroom:
    xanchor 0.5
    yanchor 0.5
    pos (1081, 185)
transform indicbalcony:
    xanchor 0.5
    yanchor 0.5
    pos (1606, 599)
transform indichallway:
    xanchor 0.5
    yanchor 0.5
    pos (1309, 962)
transform indicbalcony2:
    xanchor 0.5
    yanchor 0.5
    pos (273, 631)
transform indicgirlsroom:
    xanchor 0.5
    yanchor 0.5
    pos (1481, 185)

label tohallway:
    $ floor = 2
    $ lastmapcall = "tohallway"
    if bpos == "hallway" and blv == 7:
        jump devbp8
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen hallway with dissolve
    return


label togirlsroom:
    $ floor = 2
    $ lastmapcall = "togirlsroom"
    if elv == 7:
        jump devep8
    if elv == 9:
        jump devep10
    if elv == 10 and epos == "girlsroom":
        jump devep11
    if elv == 15 and epos == "girlsroom" and edesire >= desireforstep3:
        jump devep16
    if elv == 18 and epos == "girlsroom":
        jump devep19
    if spos == "girlsroom" and slv == 9:
        jump devsp10
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen girlsroom with dissolve
    return

label toberryroom:
    $ floor = 2
    $ lastmapcall = "toberryroom"
    if blv == 2 and bpos == "berryroom" and bdesire >= desireforstep1:
        jump devbp3
    if blv == 3 and bpos == "berryroom":
        jump devbp4
    if blv == 8 and bpos == "berryroom" and bdesire >= desireforstep2:
        jump devbp9
    if blv == 17 and bpos == "berryroom":
        jump devbp18
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen berryroom with dissolve
    return

label tobalcony:
    $ floor = 2
    $ lastmapcall = "tobalcony"
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen balcony with dissolve
    return

label tobalcony2:
    $ floor = 2
    $ lastmapcall = "tobalcony2"
    scene black
    hide screen minimap1
    hide screen minimap2
    show screen uimap
    stop sexfx
    stop sex
    hide screen notifglobal
    call screen balcony2 with dissolve
    return


transform location1(p):
    xanchor 0.5
    yanchor 0.5
    pos getpos1(p)
transform location2(p):
    xanchor 0.5
    yanchor 0.5
    pos getpos2(p)

init python:

    def getpos1(p):
        po = (-500,-500)
        if p == "livingroom":
            po = (1251, 821)
        if p == "mcroom":
            po = (480, 303)
        if p == "diningroom":
            po = (1029, 316)
        if p == "kitchen":
            po = (1364, 333)
        if p == "backyard":
            po = (1770, 492)
        if p == "valerieroom":
            po = (109, 171)
        if p == "bathroom":
            po = (768, 149)
        if p == "front":
            po = (216, 734)
        return po

    def getpos2(p):
        po = (-500,-500)
        if p == "berryroom":
            po = (675, 304)
        if p == "balcony2":
            po = (403, 627)
        if p == "pcroom":
            po = (1074, 287)
        if p == "girlsroom":
            po = (1418, 199)
        if p == "balcony":
            po = (1623, 792)
        if p == "hallway":
            po = (1234, 686)
        return po

init python:
    def ifnight(b):
        if daytimenumber < 3:
            return b
        else:
            return im.MatrixColor(b, im.matrix.tint(0.60, 0.65, 0.80)*im.matrix.brightness(-0.05))
    def night(b):
        return im.MatrixColor(b, im.matrix.tint(0.60, 0.65, 0.80)*im.matrix.brightness(-0.05))
    def lumi(b):
        return im.MatrixColor(b, im.matrix.tint(0.8, 0.8, 0.8)*im.matrix.brightness(+0.25))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
