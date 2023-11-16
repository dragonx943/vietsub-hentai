label sarbalc2step0:
    call showimg ("034cn") from _call_showimg_27
    "" "[sn] poses in front of you."
    s "Witness the power of my muscles!"
    s "Gnnnnh"
    mc "Incredible!"
    mc "A real Greek statue!"
    s "Haha! Thank you!"
    call incrdesire ("Sarena", 1) from _call_incrdesire_138
    pause
    jump passtime
    return


label berkitstep0:
    call showimg ("034co") from _call_showimg_28
    b "Surprise!"
    mc "!!!!"
    b "You're always looking at my cleavage..."
    b "Naughty boy!"
    b "Your punishment is to choke upon [bn]'s love! Haha!!!"
    call incrdesire ("Berry", 1) from _call_incrdesire_139
    pause
    jump passtime
    return



label berroomstep0:
    call showimgtall1 ("034cptall") from _call_showimgtall1_1
    mcth "Oh my god..."
    mcth "[bn]'s boobs are so huge ..."
    mcth "They look so soft, so comfortable ..."
    mcth "Like an altar to appease the hearts of men..."
    show 034cptall:
        linear 4.0 yalign 0.0
    b "Oh my-"
    b "You're not even bothering to hide the fact that you're staring at my breasts?"
    b "Naughty boy!"
    mc "I-"
    b "And on top of that you've got a boner!"
    mc "No, it's-"
    b "Don't worry about it. You're at an age where this kind of thing is normal, haha!"
    b "That flatters me, especially coming from you."
    call incrdesire ("Berry", 1) from _call_incrdesire_140
    pause
    jump passtime
    return


label emmdinstep0:
    call showimg ("034cq") from _call_showimg_29
    mcth "It's crazy, [en] may have the smallest boobs in the family, but they're still really big!"
    mcth "Gee, I don't want her to see that I'm watching it's simple!"
    "" "[en] stares at you ..."
    "" "She looks upset ..."
    "" "Yet she says nothing."
    call incrdesire ("Emma", 1) from _call_incrdesire_141
    pause
    jump passtime
    return


label emmpcstep0:
    call showimg ("034cr") from _call_showimg_30
    e "So, we're trying to see up the goddess's skirt [en]?"
    mc "I'm not trying anything, you're the one exposing your panties all the time!"
    e "I-"
    e "Look at him trying to make up lies!"
    e "Boo, liar!"
    call incrdesire ("Emma", 1) from _call_incrdesire_142
    pause
    jump passtime
    return


label sarbalcstep0:
    call showimg ("034cs") from _call_showimg_31
    s "Oh, [mc]!"
    s "You're so sweet!"
    s "You know how much I love to cuddle!"
    mc "I know, and I love it even more when it's with you!"
    s "You're so cute!"
    call incrdesire ("Sarena", 1) from _call_incrdesire_143
    pause
    jump passtime
    return
label valkitspank:
    play sound claque1
    show valkitspank with hpunch
    pause
    scene bg kitchen
    show mc lol at left
    if vstep <3:
        show valerie angry o3 at right
        v "What are you fucking doing, you fucker?!!!"
    elif True:
        show valerie mad o3 at right
        v "All of sudden??"
    mc "I'm sorry, there was a spider, just lending a hand."
    show valerie mad
    pause
    call incrdesire ("Valerie", 1) from _call_incrdesire_144
    pause
    jump passtime
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
