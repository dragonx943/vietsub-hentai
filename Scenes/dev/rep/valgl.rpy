label valgl:
    scene prevhole with fade
    "" "You are placing your cock through the wall's glory hole."
    if daytimenumber == 3:
        scene black

        show prevhole

        mcth "Alright, let's see what happens."
        mcth "I wonder what she'll think when she sees it."
        mcth "Feels kinda awkward, just waiting."
        mcth "I hope she comes soon, my dick is getting cold."
        scene black with dissolve
        mcth "Wait! It's getting warmer..."
        if vstep == 2:
            $ persistent.replay78 = True
            jump valgloryhole2
        elif vstep > 2:
            $ persistent.replay72 = True
            jump valgloryhole3
    elif True:
        "" "Nothing happens, no one is in that room at this time."
        jump tomcroom
        return

label valgloryhole2:

    call valoralgl028 (1.0/10) from _call_valoralgl028_2


    v "Mmmmm!"
    mcth "Fuck yea! Good job, [vn]!"
    mcth "Could never actually let her hear me say that."
    v "GLPH! GLPH!"
    mcth "Jesus, I never thought we would get here."
    mcth "I just put it in, and she's there to service my cock."
    mcth "That's so fucking hot!"

    call valoralgl028 (1.0/20.0) from _call_valoralgl028_3


    v "MMMPH!"
    mcth "Fuuuuck! She's going so fast!"
    mcth "She's getting a lot better at this."
    mcth "Her mouth is adjusting to my cock perfectly."
    mcth "Holy shit, I'm getting close!"


    call valoralglcum028 from _call_valoralglcum028_1


    mc "AGH! That feels so good!!"
    v "NNNG!"
    scene black with fade
    pause
    scene expression ifnight ("House/valerie room/valerieroom 1.webp") with dissolve
    show valerie cumface at right
    show mc at left

    v "Hey..."
    mc "That was good... for the viewers."
    show valerie happy
    v "Oh! Yea! For the viewers. Yea..."
    mc "I'm just saying I hope they liked it."
    show valerie shy
    v "Right, yea. I'm sure they did..."
    "[vn] starts blushing."
    mc "Alright, see ya."
    show valerie base
    v "See ya."
    mcth "That was weird, her screen wasn't on. Maybe I'm confused."


    $ cumbyv +=1
    call incrskill ("cockskill", 2) from _call_incrskill_100
    call incrdesire ("Valerie", cockskill) from _call_incrdesire_95
    jump passtime
    return

label valgloryhole3:
    stop music
    call valsexgl028 (1.0/10) from _call_valsexgl028_2
    v "Fuck yeah!!!"
    v "This cock is all mine!!"
    v "So big!!"
    mcth "[vn] goes so roughly!"
    v "This cock is driving me crazy!!"
    call valsexgl028 (1.0/20) from _call_valsexgl028_3
    v "Oh, I'm his slut!"
    v "I'm his cum slut!!"
    mcth "What is she saying? I can't hear!"
    v "I'm his bitch for the rest of my life!!"
    call valsexglcum028 (1.0/24) from _call_valsexglcum028_1
    v "Oh my gooood!!"
    pause
    scene black with dissolve
    v "Oh shit, I forgot to record that, again..."

    $ cumbyv +=1
    $ vcum+=1
    call incrskill ("cockskill", 3) from _call_incrskill_101
    call incrdesire ("Valerie", cockskill) from _call_incrdesire_96
    jump passtime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
