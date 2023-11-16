init python:
    def getwin():
        if not renpy.variant("small"):
            return Image("gui/textboxth.png", xalign=0.5, yalign=1.0)
        else:
            return Image("gui/textboxth.png")
define player_name = "Ero"
define mc = Character("[player_name]",who_color="#81b6ff")
define mcth = Character("Suy nghĩ của [player_name]",what_prefix="{i}",what_suffix="{/i}", window_background= getwin())

define tongueskill = 0
define cockskill = 0
define handskill = 0

define maxskill = 50

define money = 20



define premiummoney = 0
define premiumhandskill = 0
define premiumtongueskill = 0
define premiumcockskill = 0



define blogstarted = False
define levelregistered = 0
init python:
    def bloglv():
        return blv + elv + vlv + slv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
