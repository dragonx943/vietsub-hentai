
define daytimes = ["Morning", "Afternoon", "Evening", "Night", "Late night"]
define daytimenumber = 0
define currdaytime = "Morning"
define positionsb = ["kitchen","berryroom","backyard","balcony2","berryroom"]
define positionse = ["diningroom","backyard","pcroom","kitchen","girlsroom"]
define positionss = ["balcony","balcony2","livingroom","backyard","girlsroom"]
define positionsv = ["backyard","kitchen","balcony2","valerieroom","valerieroom"]

init python:

    def nextdaytime():
        global daytimenumber
        global currdaytime
        global bpos
        global spos
        global epos
        global vpos
        if isendmode == False:
            daytimenumber += 1
            if daytimenumber < 5 :
                currdaytime = daytimes[daytimenumber]
            else :
                daytimenumber = 0
                currdaytime = daytimes[daytimenumber]
            
            bpos = positionsb[daytimenumber]
            if blv == 6:
                bpos = "kitchen"
            if blv == 7 and daytimenumber == 3:
                bpos = "hallway"
            if blv == 12 and daytimenumber == 3:
                bpos = "livingroom"
            spos = positionss[daytimenumber]
            if (slv == 8 and sdesire >= desireforstep2) or slv == 11:
                spos = "kitchen"
            if slv == 9 and daytimenumber == 3:
                spos = "girlsroom"
            if slv == 13:
                spos = "pcroom"
            if slv == 14:
                spos = "livingroom"
            
            epos = positionse[daytimenumber]
            if elv == 7:
                epos = "girlsroom"
            if elv == 9:
                epos = "girlsroom"
            if elv == 10 and daytimenumber == 0:
                epos = "girlsroom"
            if elv == 15 and daytimenumber == 0 and edesire >= desireforstep3:
                epos = "girlsroom"
            if elv == 18 and daytimenumber == 1 and edesire >= desireforstep3:
                epos = "girlsroom"
            if elv == 16 and daytimenumber == 2:
                epos = "valerieroom"
            
            vpos = positionsv[daytimenumber]
            if vlv == 11 and daytimenumber == 2:
                vpos = "mcroom"
        else:
            daytimenumber = 4
            spos = "balcony"
            epos = "girlsroom"
            bpos = "berryroom"
            vpos = "valerieroom"

label passtime:
    if renpy.ios or renpy.android:
        $ renpy.save_persistent()
    if isendmode == True:
        scene black
        "" "You can't pass the time right now."
        $ renpy.jump(lastmapcall)
        call pt from _call_pt_2
    elif True:
        call pt from _call_pt
    return

label launchendroam:
    $ isendmode = True
    $ nextdaytime()
    play music Harpe
    $ renpy.jump(lastmapcall)
    return
label launchend:
    $ isendmode = False
    $ estep = 4
    $ bstep = 4
    $ vstep = 4
    $ sstep = 4
    $ day += 1
    $ nextdaytime()
    $ cumbyv += 5
    $ cumbyb += 5
    $ cumbys += 5
    $ cumbye += 5
    $ bcum += 10
    $ scum += 10
    $ vcum += 10
    $ ecum += 10
    if ispromisedtoemma == True:
        $ emmastatus = "In couple with you."
        $ mcstatus = "In couple with Emma."
    elif True:
        $ emmastatus = "Heart taken by [mc]."
        $ mcstatus = "\"Single\" but not free."
    $ berrystatus = "[mc]'s mistress and owner."
    $ sarenastatus = "[mc]'s soulmate."
    $ valeriestatus = "[mc]'s slut."

    $ lastmapcall = "tomcroom"
    scene black
    "" "This will now be my everyday life from now on! (Under construction)"
    call screen endingscreen
    return
label passnightnothing:
    $ daytimenumber = 4
    call pt from _call_pt_1
    return

label pt:
    $ nextdaytime()
    if daytimenumber == 4:
        jump night
    elif daytimenumber == 0:
        $ day += 1
        play music sunny_day
        if Gymclothes.command == True:
            $ Gymclothes.command = False
            $ Gymclothes.receive = True
        if Tsounade.command == True:
            $ Tsounade.command = False
            $ Tsounade.receive = True
        if Swimwear.command == True:
            $ Swimwear.command = False
            $ Swimwear.receive = True
        if Toolkit.command == True:
            $ Toolkit.command = False
            $ Toolkit.receive = True
        jump tomcroom
    elif True:
        play music jigsaw
        $ renpy.jump(lastmapcall)


label night:


    if estep == 4 and ispromisedtoemma == True:
        $ money += levelregistered
        "" "You've earned [levelregistered]$ by your blog's visits and supporters!"
        jump nightemmagf


    if elv == 13 and devzoe1ok == True:
        jump devzoe2
    if slv == 16 and devzoe1ok == True:
        jump devzoe2
    if blv == 13 and devzoe1ok == True:
        jump devzoe2
    if vlv == 15 and devzoe1ok == True:
        jump devzoe2
    if slv == 21:
        jump devsp22

    if slv == 15:
        "" "After a long day, you go back to your room."
        jump devsp16
    if blv == 18:
        jump devbp19
    scene mcroomsleep with fade
    "" "After a long day, you go back to your room and fall asleep."
    if vlv == 19:
        jump devvp20
    if vlv == 21:
        jump devvp22
    if devzoe2ok == True and devzoe3ok == False:
        jump devzoe3
    if blogstarted == True:
        $ money += levelregistered
        "" "You've earned [levelregistered]$ by your blog's visits and supporters!"
    if slv == 19:
        jump devsp20

    if slv == 5:
        jump devsp6
    if vlv == 8:
        jump devvp9
    if slv == 12:
        jump devsp13
    if elv == 11:
        jump devep12
    if elv == 12:
        jump devep13
    if elv == 17:
        jump devep18
    if elv == 19:
        jump devep20

    "" "A long night full of lewd dreams..."
    show mcroommorning with fade
    show mcroomerect with dissolve


    "" "The next morning, you're waking up, all hard, with your cock passing through your trunks' opening."
    if vlv == 5:
        jump devvp6
    if blv == 15 and bdesire >= desireforstep3:
        scene black with dissolve
        jump devbp16
    if doorlocked == False:
        $ reste = day % 4
        if reste == 0:
            jump morenterb
        elif reste == 1:
            jump morentere
        elif reste == 2:
            jump morenters
        elif True:
            jump morenterv
    elif True:
        "" "As your door is locked, none entered your room in the morning."
        jump passtime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
