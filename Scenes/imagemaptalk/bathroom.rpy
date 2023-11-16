screen bathroom:

    imagemap:
        ground ifnight("House/bathroom/bg bathroom.webp")
        if daytimenumber > 2:
            imagebutton:
                idle night("House/bathroom/takeshower.webp")
                hover lumi("House/bathroom/takeshower.webp")
                focus_mask True
                action Jump("takeshower")
        else:
            imagebutton:
                idle "House/bathroom/takeshower.webp"
                hover lumi("House/bathroom/takeshower.webp")
                focus_mask True
                action Jump("takeshower")



screen bathroom3:

    imagemap:
        ground ifnight("House/bathroom/bg bathroom.webp") xpos 200
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
