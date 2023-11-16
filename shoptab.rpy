screen shoptab:
    zorder 2
    modal True

    imagemap:
        ground "ui/shopbg.webp"
        text "{b}[money]${/b}" xalign 0.95 yalign 0.85 size 80 color "#c68109"
        imagebutton:
            align (1.0,0.0)
            offset (-20,20)
            idle "ui/closeui.webp"
            hover "ui/closeui h.webp"

            action Jump(lastmapcall)
        text "Command right now and receive it in front of your door in the next 24h!" pos (400,150)
        hbox pos (50,250) box_wrap True:

            if Gymclothes.command == False and Gymclothes.receive == False and Gymclothes not in inventory.items:
                vbox:
                    text "[Gymclothes.name]" bold True xalign 0.5
                    imagebutton:
                        idle Gymclothes.imageref
                        hover lumi(Gymclothes.imageref)

                        action Function(inventory.buy, Gymclothes)
                    text "[Gymclothes.cost]$" xalign 0.5
            if Tsounade.command == False and Tsounade.receive == False and Tsounade not in inventory.items:
                vbox:
                    text "[Tsounade.name]" bold True xalign 0.5
                    imagebutton:
                        idle Tsounade.imageref
                        hover lumi(Tsounade.imageref)

                        action Function(inventory.buy, Tsounade)
                    text "[Tsounade.cost]$" xalign 0.5
            if Swimwear not in inventory.items and Swimwear.command == False and Swimwear.receive == False:
                vbox:
                    text "[Swimwear.name]" bold True xalign 0.5
                    imagebutton:
                        idle Swimwear.imageref
                        hover lumi(Swimwear.imageref)

                        action Function(inventory.buy, Swimwear)
                    text "[Swimwear.cost]$" xalign 0.5
            if Toolkit not in inventory.items and Toolkit.command == False and Toolkit.receive == False:
                vbox:
                    text "[Toolkit.name]" bold True xalign 0.5
                    imagebutton:
                        idle Toolkit.imageref
                        hover lumi(Toolkit.imageref)

                        action Function(inventory.buy, Toolkit)
                    text "[Toolkit.cost]$" xalign 0.5
label buyitem:
    scene black
    "" "You ordered for this item, you'll receive it tomorrow in your frontyard."
    jump topcroom
label toopoor:
    scene black
    "" "You're too poor for that!"
    call screen shoptab
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
