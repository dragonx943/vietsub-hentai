define whiteflash = Fade(0.0,0.1,0.5,color="#fff")
transform cumtr:
    xalign 0.5
    yalign 0.5
    linear 0.1 xzoom 1.10 yzoom 1.10
    linear 0.3 xzoom 1 yzoom 1
    linear 0.08 xzoom 1.15 yzoom 1.15
    linear 1.0 xzoom 1.00 yzoom 1.00
    linear 0.1 xzoom 1.05 yzoom 1.05
    linear 0.5 xzoom 1.0 yzoom 1.0
    xalign 0.0
    yalign 0.0
define cum = Fade(0.1,0.5,0.5,color="#fff")

image cumanim:
    "other/cum1.webp"
    0.08
    "other/cum2.webp"
    0.08
    "other/cum3.webp"
    0.08
    "b"
    pause 0.16

    "other/cum1.webp"
    0.08
    "other/cum2.webp"
    0.08
    "other/cum3.webp"
    0.08
    "b"
    pause 0.84

    "other/cum1.webp"
    0.08
    "other/cum2.webp"
    0.08
    "other/cum3.webp"
    0.08
    "b"

transform atcenter:
    yalign 0.5
    xalign 0.5
transform leftquitinv:
    xzoom 1.0
    linear 2.0 xalign 1.0 xpos 0.0 xoffset 0.0

transform leftquit:
    xzoom 1.0
    linear 1.0 xalign -1.0 xpos 0.0 xoffset 0.0

transform rightquit:
    xzoom -1.0
    linear 2.0 xalign 0.0 xpos 1.0 xoffset 0.0

transform zoomlent:
    xalign 0.5 yalign 0.7
    ease 1.0 yzoom 1.01
    ease 1.0 yzoom 1.0
    repeat

transform hautbashaut:
    pause 0.3
    ease 4.0 yalign 1.0
    pause 0.1
    ease 4.0 yalign 0.0
transform chatouiller:
    linear 0.5 xoffset -20
    linear 0.5 xoffset 20
    repeat
transform irrit:
    linear 0.1 xanchor 0.45
    linear 0.1 xanchor 0.6
    linear 0.1 xanchor 0.4
    linear 0.1 xanchor 0.55
    linear 0.1 xanchor 0.45
    linear 0.1 xanchor 0.52
    linear 0.1 xanchor 0.48
    linear 0.1 xanchor 0.5




transform angryjump:
    linear 0.05 yzoom 0.95 xzoom 1.05
    linear 0.1 yzoom 1.05 xzoom 0.95
    linear 0.1 yzoom 0.95 xzoom 1.05
    linear 0.15 yzoom 1.05 xzoom 0.95
    linear 0.1 yzoom 1.0 xzoom 1.0
transform angryjumpcentered:
    xalign 0.5
    yalign 1.0
    linear 0.05 yzoom 0.95 xzoom 1.05
    linear 0.1 yzoom 1.05 xzoom 0.95
    linear 0.1 yzoom 0.95 xzoom 1.05
    linear 0.15 yzoom 1.05 xzoom 0.95
    linear 0.1 yzoom 1.0 xzoom 1.0

transform angryjumpinv:
    linear 0.05 yzoom 0.95 xzoom -1.05
    linear 0.1 yzoom 1.05 xzoom -0.95
    linear 0.1 yzoom 0.95 xzoom -1.05
    linear 0.15 yzoom 1.05 xzoom -0.95
    linear 0.1 yzoom 1.0 xzoom -1.0


transform masturbation:
    linear 0.3 yoffset -50
    linear 0.3 yoffset 50
    repeat

transform leftinvert:
    xalign 0
    xzoom -1

transform invisible:
    alpha 0.0

transform visible:
    alpha 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
