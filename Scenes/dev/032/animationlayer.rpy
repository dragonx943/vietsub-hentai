label cummale:
    hide wflash
    call impact1 from _call_impact1
    show wflash
    play sound acum1

    pause 0.85
    call impact1 from _call_impact1_1
    show wflash
    play sound acum2

    pause 1.2
    call impactsofter from _call_impactsofter
    show wflash
    play sound acum3

    pause 0.8
    call cumfemale from _call_cumfemale
    return


label cumfemaleflash:

    hide wflash
    show wflash
    play sound pulsation2
    call impact1 from _call_impact1_2
    pause 0.3
    show wflash
    call impact1 from _call_impact1_3
    play sound pulsation2
    pause 0.3
    show wflash
    call impact1 from _call_impact1_4
    play sound pulsation2
    pause 0.05
    show wflash
    call impact1 from _call_impact1_5
    play sound pulsation2
    pause 0.5
    show wflash
    call impact1 from _call_impact1_6
    play sound pulsation2
    pause 0.8
    call cumfemale from _call_cumfemale_1
    return


label cumdouble:
    hide wflash
    call impact1 from _call_impact1_7
    show wflash
    play sound acum1

    pause 0.85
    call impact1 from _call_impact1_8
    show wflash
    play sound acum2

    pause 1.2
    call impactsofter from _call_impactsofter_1
    show wflash
    play sound acum3

    pause 0.8
    call cumfemale from _call_cumfemale_2
    return
    return


label zoomingcumfemale:
    show layer master:
        xalign 0.5 yalign 0.5
        xzoom 1.140 yzoom 1.140

label impact1:
    show layer master:
        xalign 0.5 yalign 0.5
        pause 0.05
        xzoom 1.140 yzoom 1.140
        offset (50,50)
        pause 0.05
        offset (-50,-50)
        pause 0.05
        offset (-50,50)
        pause 0.05
        offset (50,-50)
        pause 0.05
        xzoom 1.07 yzoom 1.07
        offset (25,25)
        pause 0.05
        offset (-25,-25)
        pause 0.05
        offset (-25,25)
        pause 0.05
        offset (25,-25)
        pause 0.05
        xzoom 1.0 yzoom 1.0
        offset (12,12)
        pause 0.05
        offset (-12,-12)
        pause 0.05
        offset (-12,12)
        pause 0.05
        offset (12,-12)
        pause 0.05
        offset (6,6)
        pause 0.05
        offset (-6,-6)
        pause 0.05
        offset (-6,6)
        pause 0.05
        offset (6,-6)
        pause 0.05
        offset (3,3)
        pause 0.05
        offset (-3,-3)
        pause 0.05
        offset (-3,3)
        pause 0.05
        offset (3,-3)
        pause 0.05
        offset (0,0)
    return

label cumfemale:

    show layer master:
        xzoom 1.0 yzoom 1.0
        yalign 0.5 xalign 0.5
        offset (2,2)
        pause 0.05
        offset (-2,-2)
        pause 0.05
        offset (-2,2)
        pause 0.05
        offset (2,-2)
        pause 0.05
        repeat
    return

label impactsofter:
    show layer master:
        xzoom 1.07 yzoom 1.07
        offset (25,25)
        pause 0.05
        offset (-25,-25)
        pause 0.05
        offset (-25,25)
        pause 0.05
        offset (25,-25)
        pause 0.05
        xzoom 1.0 yzoom 1.0
        offset (12,12)
        pause 0.05
        offset (-12,-12)
        pause 0.05
        offset (-12,12)
        pause 0.05
        offset (12,-12)
        pause 0.05
        offset (6,6)
        pause 0.05
        offset (-6,-6)
        pause 0.05
        offset (-6,6)
        pause 0.05
        offset (6,-6)
        pause 0.05
        offset (3,3)
        pause 0.05
        offset (-3,-3)
        pause 0.05
        offset (-3,3)
        pause 0.05
        offset (3,-3)
        pause 0.05
        offset (0,0)
    return
label slowrepos:
    show layer master:
        linear 0.5 offset (-2,0)
        linear 0.5 offset (2,0)
        repeat
    return
image wflash:
    "wh"
    alpha 1.0
    linear 0.5 alpha 0.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
