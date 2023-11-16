screen girlsroom:
    imagemap:
        if isendmode == False:
            ground ifnight("House/girlsroom/bg girlsroom.webp")
            add ifnight("House/girlsroom/girlsroom1.webp")
        else:
            ground "bg girlsroom night"
            imagebutton:
                idle "bg girlsroom emmaend"
                hover lumi("0.3.1/bg girlsroom emmaend.webp")
                pos (996,406)
                action Jump("roaemmaend")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
