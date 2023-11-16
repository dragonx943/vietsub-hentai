label evbersexby:
    scene black with dissolve
    pause
    stop music
    call bersex1by029 from _call_bersex1by029_1
    b "Hm!!"
    "" "You're making love to [bn] without even a warning."
    "" "She sounded surprised at first, since she usually is the initiator."
    "" "She feels so desired, so loved!"
    call bersex2by029 from _call_bersex2by029_1
    b "Oh sweety!!"
    b "I love you so much!!"
    b "Don't try to hold it!"
    b "I wanna feel your love flowing inside of me!"
    call bersexbycum029 from _call_bersexbycum029_1
    b "Oh yeaaaaah!!!"
    b "You're so fucking mine!!"
    b "MIIIINE!!"
    show bersexbycumafter with fade
    play audio bgoodboy
    b "Good boy..."
    b "So much cum, as usual..."
    call incrskill ("cockskill", 3) from _call_incrskill_50
    call incrdesire ("Berry", cockskill) from _call_incrdesire_38
    $ cumbyb+=1
    $ bcum+=1
    jump passtime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
