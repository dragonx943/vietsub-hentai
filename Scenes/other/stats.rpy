define sdesire = 0
define edesire = 0
define bdesire = 0
define vdesire = 0

define desireforstep1 = 5
define desireforstep2 = 70
define desireforstep3 = 300

define desiremax = 300
label incrdesire(namae, valeur):
    $ writetemp = valeur
    if namae == "Sarena":
        $ sdesire += valeur
        if sdesire > desiremax:
            $ sdesire = desiremax
        elif True:
            $ write ("Sarena's desire increased by [writetemp]")
    elif namae == "Emma":
        $ edesire += valeur
        if edesire > desiremax:
            $ edesire = desiremax
        elif True:
            $ write ("Emma's desire increased by [writetemp]")
    elif namae == "Berry":
        $ bdesire += valeur
        if bdesire > desiremax:
            $ bdesire = desiremax
        elif True:
            $ write ("Berry's desire increased by [writetemp]")
    elif namae == "Valerie":
        $ vdesire += valeur
        if vdesire > desiremax:
            $ vdesire = desiremax
        elif True:
            $ write ("Valerie's desire increased by [writetemp]")
    return

label incrskill(skill, valeur):
    $ rang = 0
    if valeur == 1:
        $ rang = skillrankincr1
    elif valeur == 2:
        $ rang = skillrankincr2
    elif valeur == 3:
        $ rang = skillrankincr3

    if skill == "cockskill":
        $ cockskill += rang
        if cockskill > maxskill:
            $ cockskill = maxskill
    elif skill == "handskill":
        $ handskill += rang
        if handskill > maxskill:
            $ handskill = maxskill
    elif skill == "tongueskill":
        $ tongueskill += rang
        if tongueskill > maxskill:
            $ tongueskill = maxskill
    return

define skillrankincr1 = 1
define skillrankincr2 = 3
define skillrankincr3 = 5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
