label dinnertime:

    scene diningroomtalk
    show mc with dissolve:
        xalign -0.1
    show berry with dissolve:
        xalign 0.25
    show sarena with dissolve:
        xalign 0.5
    show emma with dissolve:
        xalign 0.75
    show valerie happy with dissolve:
        xalign 1.0
    b "It's important to eat together to strengthen our bonds!"
    s "Saaaaah I'm hungryyyyy! I need proteins!!"
    e "I had to break my stream..."
    v "I hope I won't bother anyone if I join."
    scene black with dissolve
    pause
    scene dinnertime with dissolve
    window hide
    pause
    window auto

    if bboundv < 24 or bstep < 4:
        "" "[vn] and [bn] didn't share any words or looks, completely ignoring each other."
    elif bboundv > 23 and bstep >3 or bstep < 4:
        "" "[vn] and [bn] discussed wine."

    if sbounde < 24 or bstep < 4:
        "" "[sn] and [en] argued about who got more food unfairly."
    elif sbounde > 23 and bstep >3 or bstep < 4:
        "" "[sn] and [en] discussed their follower's evolution."

    if bbounde < 24 or bstep < 4:
        "" "[bn] asked [en] if she wanted more, but [en] ignored her."
    elif bbounde > 23 and bstep >3 or bstep < 4:
        "" "[bn] and [en] discussed their feelings, trying to connect more to eachothers."

    if sbounde < 24 or bstep < 4:
        "" "[en] put her attention on [vn], and tried to get to know her a bit more."
    elif sbounde > 23 and bstep >3 or bstep < 4:
        "" "[en] and [vn] discussed sex topics, how to make a man crazy for a woman."

    if bbounds < 24 or bstep < 4:
        "" "[sn] talked a bit with [bn] about how they manage their work."
    elif bbounds > 23 and bstep >3 or bstep < 4:
        "" "[sn] and [bn] discussed the limits not to pass when dominating you."

    if vbounds < 24 or bstep < 4:
        "" "[vn] complimented [sn] about her look, but [sn] just thanked her politely."
    elif vbounds > 23 and bstep >3 or bstep < 4:
        "" "[vn] and [sn] discussed their experience with girls."
    if bstep >3:
        "" "Everybody now has a great time with everyone!"
    if bboundv + 2 < bboundvmax:
        $ bboundv += 2
    if bbounde + 2 < bboundemax:
        $ bbounde += 2
    if bbounds + 2 < bboundsmax:
        $ bbounds += 2
    if vbounde + 2 < vboundemax:
        $ vbounde += 2
    if vbounds + 2 < vboundsmax:
        $ vbounds += 2
    if sbounde + 2 < sboundemax:
        $ sbounde += 2
    jump passtime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
