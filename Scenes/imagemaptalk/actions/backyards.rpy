label bysobserve:
    scene observebgbackyard2 with fade
    show byobserves with dissolve
    window hide
    pause
    window auto
    mcth "Great lord, that ASS!!"
    mcth "My [ssn] has one of the sexiest butts I've ever seen! This bikini thong fits her so well!"
    mcth "Oh gosh, I feel like I'll lose my mind if I continue to look at her..."
    jump tobackyard
    return
label byscuni:
    window hide
    play sound emoansingle
    scene 018sarbypre with hpunch
    pause
    window auto
    s "Wh-what are you doing [mc]?"
    mc "[sn]... You're so beautiful!"
    s "Oh really? D-do you like the view?"
    mc "For sure!"
    s "You really are naughty for doing this to your [ssn]..."
    s "I'll make you pay the price!"
    window hide
    scene black
    show 018cunby
    stop music
    play sex ssoftmoans2
    play sexfx frottements
    pause
    window auto
    s "Oooh yeah, oh yeah!!"
    s "Lick your [ssn]'s pussy!!"
    s "Oh I love your cute face so bad!"
    s "You learned my body so quickly!"
    s "I'm gonna cum on your face, [mc]!"
    window hide
    stop sexfx
    stop sex
    hide 018cunby
    show 018cunbycum at cumtr
    show cumanim
    play audio scum1
    pause
    window auto
    s "I'm cumming so haaaaaard!!!"
    $ scum += 1
    s "I want your mouth to taste me forever!!!"
    scene black with dissolve
    pause 1.0
    scene expression ifnight("House/backyard/bytalk.webp")
    show mc humidface at left
    show sarena shy o3 at right
    s "So sorry [mc], I almost forced y-"
    mc "You know that it's alright!"
    show sarena taunt
    s "I bet you did that on purpose because you knew how I'd react!"
    mc "I don't know what you're talking about hehehe!"
    call incrskill ("tongueskill", 2) from _call_incrskill_99
    call incrdesire ("Sarena", tongueskill) from _call_incrdesire_94
    jump passtime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
