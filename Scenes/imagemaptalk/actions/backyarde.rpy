label byeobserve:
    scene observebgbackyard with fade
    show byobservee with dissolve
    window hide
    pause
    window auto
    mcth "Great lord, that BUTT!!"
    mcth "My [esn]'s ass is begging for something or what?"
    mcth "Oh gosh, she makes me feel so horny..."
    jump tobackyard
    return

label byespank:
    scene observebgbackyard with fade
    show byobservee with dissolve
    window hide
    pause
    window auto
    mcth "And again, [en] is showing us her magnificent butt."
    mcth "It's time to shine!"
    play sound spank
    window hide
    show byobservee with hpunch
    pause
    window auto
    scene bytalk
    show mc at left
    show emma o2 angryshy at right
    if estep <3:
        e "You little bastard!!"
        mc "Hehe it's not my fault! your butt was calling for it!"
        e "Calling for it, my ass!"
        mc "Yes exactly!"
        e "DON'T TALK TO ME!"
    elif True:
        e "[mc]!!!"
    call incrskill ("handskill", 1) from _call_incrskill_95
    call incrdesire ("Emma", handskill) from _call_incrdesire_91
    jump passtime
    return

label byelick:
    stop music
    call emmcunby100 (v=1.0/8) from _call_emmcunby100_2
    pause
    e "Oh, my viewers I'm sorry!"
    e "My stomach hurts!"
    e "Yeah maybe I ate something wrong..."
    call emmcunby100 (v=1.0/16) from _call_emmcunby100_3
    e "Oh lord it hurts, so, so bad!"
    e "Oh no!"
    e "I'm gonna-"
    call emmcunby100cum from _call_emmcunby100cum_1
    $ ecum+=1
    $ persistent.replay128 = True
    call incrskill ("tongueskill", 1) from _call_incrskill_96
    call incrdesire ("Emma", tongueskill) from _call_incrdesire_92
    stop sexfx
    play sex ecum1
    pause
    e "It's alright, I'm good now..."
    jump passtime
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
