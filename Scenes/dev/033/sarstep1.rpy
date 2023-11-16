label sarstep1by:
    scene observebgbackyard2 with fade
    show byobserves with dissolve
    mcth "Hahaha, she looks very focused, I shall surprise her!"
    mcth "I approach slowly..."
    mcth "Be careful..."
    call showscene ("sars1by1") from _call_showscene_39
    mcth "SURP-"
    mcth "Wait, what?"
    mcth "Am I really getting my foot caught in my other leg?!"
    mcth "Oh no! I'm tripping!"
    mcth "I'm about to fall on [sn]!"
    mcth "I-"
    play audio doublegrab
    scene sars1by2 with hpunch
    play audio bmoansp
    s "Nyah!!!"
    mc "F~arena!!!"
    s "[mc], is that you?!"
    mc "I'm F~orry, I F~ripped!"
    s "[mc], stop talking while you still have it in your mouth!"
    s "Otherwise I-"
    pause
    scene expression ifnight("House/backyard/bytalk.webp")
    show mc surprised humidface at left
    show sarena shy o3 at right
    pause
    show sarena taunt
    s "So you stumbled, headfirst between my legs, right?!"
    s "What kind of an excuse is that?"
    mc "Yes, it is! I swear!"
    mc "I just wanted to surprise you and then I tripped and fell!"
    s "When you put it that way, it sounds like a porn scenario, haha!"
    mc "But it's true!"
    s "Okay, I believe you."
    mc "Is that right?"
    show sarena happy
    s "Of course, I have full faith in you!"
    mcth "Oh, [sn] is really amazing..."
    call incrskill ("tongueskill", 1) from _call_incrskill_128
    call incrdesire ("Sarena", tongueskill) from _call_incrdesire_133
    pause
    jump passtime
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
