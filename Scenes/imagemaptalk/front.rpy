screen frontyard:

    imagemap:
        if daytimenumber > 2:
            ground night("House/frontyard/bg front.webp")
            if bstep <4:
                add "botnight"
        else:
            ground "House/frontyard/bg front.webp"
            if bstep <4:
                add "bot"
        if Gymclothes.receive == True:
            imagebutton:
                idle "House/frontyard/pack1.webp"
                hover lumi("House/frontyard/pack1.webp")
                focus_mask True
                action [Function(inventory.get_item, Gymclothes), Jump("getitem")]
        if Tsounade.receive == True:
            imagebutton:
                idle "House/frontyard/pack1.webp"
                hover lumi("House/frontyard/pack1.webp")
                focus_mask True
                action [Function(inventory.get_item, Tsounade), Jump("getitem")]
        if Swimwear.receive == True:
            imagebutton:
                idle "House/frontyard/pack1.webp"
                hover lumi("House/frontyard/pack1.webp")
                focus_mask True
                action [Function(inventory.get_item, Swimwear), Jump("getitem")]
        if Toolkit.receive == True:
            imagebutton:
                idle "House/frontyard/pack1.webp"
                hover lumi("House/frontyard/pack1.webp")
                focus_mask True
                action [Function(inventory.get_item, Toolkit), Jump("getitem")]
        if blv == 16:
            imagebutton:
                idle "0.2.7/package 2.webp"
                hover lumi("0.2.7/package 2.webp")
                focus_mask True
                action [Jump("devbp17")]

label getitem:
    scene bg front
    "" "You've received a new item in your inventory."
    jump tofrontyard
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
