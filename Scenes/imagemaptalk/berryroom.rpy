screen berryroom:
    imagemap:
        if daytimenumber <3:
            ground "bg berryroom"
        else:
            ground "bg berryroom evening"
        if bpos == "berryroom" and daytimenumber == 1:
            imagebutton:
                idle "House/berryroom/berryroom button1.webp"
                hover lumi("House/berryroom/berryroom button1.webp")
                focus_mask True
                action Jump("talkb")

        if bpos == "berryroom" and isendmode == True:
            imagebutton:
                idle "berry roomberryend"
                hover lumi("0.3.1/berry roomberryend.webp")
                pos (681,420)
                action Jump("roaberryend")
        if isendmode == False:
            add ifnight("House/berryroom/berryroom b1.webp")
            imagebutton:
                idle ifnight("House/berryroom/brb5.webp")
                hover lumi("House/berryroom/brb5.webp")
                focus_mask True
                action Jump("lookatisaphoto")
            if bstep < 4:
                imagebutton:
                    idle ifnight("House/berryroom/brb4.webp")
                    hover lumi("House/berryroom/brb4.webp")
                    focus_mask True
                    action Jump("lookberrymarriage")
            else:
                add ifnight("0.3.2/berry room familyboard.webp")



label lookatisaphoto:
    scene expression ifnight("House/berryroom/tabisa.webp")
    mcth "Hm? WHo is this woman?"
    mcth "She looks hot, I wonder why my [bsn] is displaying her..."
    if bpos == "berryroom" and daytimenumber == 1:
        scene berryroom talk
        show mc at left
        show berry at right
        b "Hey, you're looking at Isabelle's picture!"
        mcth "Isabelle? Is she one of your acquaintances?"
        b "Not at all, she is my idol!"
        b "She is an actress that is sooo gorgeous!"
        mc "An actress? Which movie can I see her in?"
        b "Eh... I... I prefer not to mention it."
        mc "So, do you want to be an actress like her?"
        b "Oh, not really, I just admire her."
        b "I've heard about where she retired and her new life..."
        b "Sometimes I feel jealous of her, haha!"
        mc "What is about her new companion?"
        b "Stop asking me questions! I feel embarrassed to talk about that."
        mc "O-okay..."
    jump toberryroom

label lookberrymarriage:
    scene expression ifnight("House/berryroom/photomarriage.webp")
    if bstep <3:
        mcth "It looks like [bn]'s photo of her marriage with her current husband."
        mcth "Waw she looks so pretty..."
        mcth "But why did she do that black trace on her husband?"
        if bpos == "berryroom" and daytimenumber == 1:
            scene berryroom talk
            show mc at left
            show berry at right
            b "Oh you're looking at my marriage's photo!"
            b "I was a long time ago... back when he used to live together..."
            mc "What do you mean?"
            show berry angry
            b "This bastard is always on a business trip!! I never see him, and when it happens, he just sleeps..."
            show berry base
            b "But it doesn't matter, now I've got my cutie that I can take care of at his place, hehehe!"
            mcth "She seems really mad at him, I guess that's normal when a husband doesn't pay attention to his wife anymore."
    elif True:
        mc "[bn] and her ex-husband..."

        if bpos == "berryroom" and daytimenumber == 1:
            scene berryroom talk
            show mc at left
            show berry at right
            show berry angry
            b "I have to change this portrait!"
            b "I don't want to see it anymore!"
    jump toberryroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
