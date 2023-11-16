define availableanims = []

init python:
    def firstplay (name):
        global availableanims
        if name not in availableanims:
            availableanims.append (name)
    def nextpage ():
        global replaypage
        global pagename
        if replaypage == 4:
            replaypage = 0
        else:
            replaypage += 1
        pagename = pagenaming[replaypage]
    def prevpage ():
        global pagename
        global replaypage
        if replaypage == 0:
            replaypage = 4
        else:
            replaypage -= 1
        pagename = pagenaming[replaypage]

define repunlocked = False
label animationreplay:
    scene black
    if repunlocked == False:
        "" "These animations are unlocked once you see them."
    if ispremiumversion == True:
        if repunlocked == False:
            show spoileralert
            "" "You're using the premium version. You can choose to unlock all animations."
            "" "These may spoil you the content you may not have seen."
            scene black
            menu:
                "Do you want to unlock everything?"
                "Yes, unlock everything!" if True:
                    $ repunlocked = True
                "No, I want to unlock them myself." if True:
                    $ repunlocked = False
    if repunlocked == True:
        $ cheatdev = True
    $ replaypage = 0

    call screen animationpanel2
    return
define pagenaming = ["Sarena","Emma","Berry","Valerie", "Other and multiple"]

define replaypage = 0
define cheatdev = False
define pagename = "Sarena"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
