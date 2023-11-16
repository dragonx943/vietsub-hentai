label byvobserve:
    scene observebgbackyard with fade
    show byobservev with dissolve
    window hide
    pause
    window auto
    mcth "Great lord, she looks so horny!"
    mcth "My [vsn] has such a goddamn hot body..."
    mcth "I should step back before she notices me.."
    jump tobackyard
    return

label byvfingerjob:
    scene observebgbackyard with fade
    show byobservev with dissolve
    mcth "Look at her..."
    mcth "She's so horny, she can't stop to touch herself."
    mcth "I think it's time to play with her again."
    scene black
    window hide
    show 016fj
    stop music
    play sexfx frottements2
    play sex vmoans1
    pause
    window auto
    if vstep <3:
        v "You mother fucker, you're doing that again!"
    v "Oh! Oh!"
    v "Oh no! I can't stop him!"
    if vstep <3:
        v "Why does it feel so good?!"
    v "This bastard will make me-"
    v "Cuuuuuum!"
    window hide
    hide 016fj
    show 016fjcum
    show cumanim
    stop sexfx
    stop sex
    play sex vcum1
    pause
    $ vcum +=1
    call incrskill ("handskill", 1) from _call_incrskill_38
    call incrdesire ("Valerie", handskill) from _call_incrdesire_29
    window auto
    v "[mc], you're so good!"
    mc "Always satisfying to hear that."
    stop sex
    scene bytalk with dissolve
    show mc at left
    if vstep <3:
        show valerie o4 angryshy at right
    elif True:
        show valerie o4 happy at right
    pause
    if vstep <3:
        v "You did it again!"
    show mc lol
    mc "And I made you cum again."
    show valerie mad
    pause
    if vstep <3:
        v "I hate you."
    elif True:
        v "I love you!"
    jump passtime
    return


label byvcuni:
    window hide
    scene v2k at angryjump
    play sex vmoans1
    pause
    window auto
    v "[mc]!!"
    if vstep <3:
        mc "What again?"
        v "Why all of a sudden?!"
    mc "You prepared my meal, now I'm eating it."
    if vstep <3:
        v "Why are you always like that?!"
        mc "That's the price if you want me to forgive you."
        v "I don't want you to-"
    v "Aaah!"
    if vstep <3:
        v "Okay, just a little!"
    v "Oh my-"
    window hide
    stop sex
    play audio vcum1
    scene v2kcum at cumtr
    show cumanim

    pause
    window auto
    v "So good so goooood!!"
    v "Please forgive my sins [mc]. You can do anything to meeeee!"
    scene bytalk with fade
    show mc lol at left
    if vstep <3:
        show valerie o4 angryshy at right
        mc "I'll remember that."
        v "You'll remember nothing! I didn't mean it!"
    elif True:
        show valerie happy at right
        v "So good... as always."
    $ tongueskill +=1
    call incrskill ("tongueskill", 2) from _call_incrskill_39
    call incrdesire ("Valerie", tongueskill) from _call_incrdesire_30
    jump passtime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
