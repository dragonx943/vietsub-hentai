screen valerieroom:

    imagemap:
        if isendmode == False:
            ground ifnight( "House/valerie room/bg valerieroom.webp")
            if vpos == "valerieroom":
                imagebutton:
                    idle ifnight("House/valerie room/valerieroom button1.webp")
                    hover lumi("House/valerie room/valerieroom button1.webp")
                    focus_mask True
                    action Jump("talkv")
            add ifnight("House/valerie room/valtrace.webp")
            if daytimenumber == 2 and vlv == 10:
                imagebutton:
                    idle ifnight("House/valerie room/vroomdildo.webp")
                    hover lumi("House/valerie room/vroomdildo.webp")
                    focus_mask True
                    action Jump("devvp11")
            add ifnight("House/valerie room/vroombed.webp")
        else:
            ground "bg valerieroom evening"
            imagebutton:
                idle "v room valend"
                hover lumi("0.3.1/v room valend.webp")
                pos (1076,166)
                action Jump("roamvalerieend")
            add ifnight("House/valerie room/valtrace.webp")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
