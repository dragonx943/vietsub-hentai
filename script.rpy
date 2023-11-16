
label after_load:
    call gainstats from _call_gainstats_1
    return

label gainstats:
    if premiummoney > 0:
        $ money += premiummoney
        $ earn1 = premiummoney
        $ write ("You earned [earn1]$ as a patron on patreon!")
    if premiumhandskill > 0:
        $ handskill += premiumhandskill
        $ earn2 = premiumhandskill
        $ write ("You earned [earn2] hand's skill as a patron on patreon!")
    if premiumtongueskill > 0:
        $ tongueskill += premiumtongueskill
        $ earn3 = premiumtongueskill
        $ write ("You earned [earn3] tongue's skill as a patron on patreon!")
    if premiumtongueskill > 0:
        $ cockskill += premiumcockskill
        $ earn3 = premiumcockskill
        $ write ("You earned [earn3] cock's skill as a patron on patreon!")

    $ premiummoney = 0
    $ premiumhandskill = 0
    $ premiumtongueskill = 0
    $ premiumcockskill = 0
    $ addvar()



    return

define ispremiumversion = True
define ispatreonversion = False
label start:

    $ availableanims = ["init"]
    call gainstats from _call_gainstats
    if ifbrowser == True:
        $ renpy.music.set_volume(0.0, delay=0, channel='music')



    scene black with fade
    if ispremiumversion == True:
        $ persistent.firstplayprologue = True
    if persistent.firstplayprologue == True:
        "The Game detects you've already seen the prologue."
        menu:
            "Do you want to skip this prologue?"
            "Continue with the prologue." if True:
                jump introduction
            "Skip prologue (not recommended if you never saw it)" if True:
                jump skipprologue
    elif True:
        jump introduction
    return

label patreonskip:
    menu:
        "Patreon special: Do you want to skip to the new content?"
        "Yes" if True:
            $ slv = 22
            $ sstep = 3
            $ tongueskill = 50
            $ handskill = 50
            $ cockskill = 50
            $ elv = 20
            $ estep = 3
            $ epos = "girlsroom"
            $ bstep = 3
            $ blv = 19
            $ vstep = 3
            $ vlv = 22
            $ qpreptalkb = True
            $ qpreptalke = True
            $ qpreptalkv = True
            $ qpreptalks = True
            $ firstparty = True
            $ inventory.get_item(Swimwear)
            $ mcstatus = "Single"
            $ zoestate = "Ex GF"
            $ esn = "Housemate"
            $ devzoe1ok = True
            $ devzoe2ok = True
            $ devzoe3ok = True
            $ firstlookonemma = True
            $ skipprologue = True
            $ bboundv = 24
            $ bbounde = 24
            $ bbounds = 24
            $ vbounde = 24
            $ vbounds = 24
            $ sbounde = 24
            $ edesire = 300
            $ sdesire = 300
            $ bdesire = 300
            $ vdesire = 300


            call unlockreplays from _call_unlockreplays


            menu:
                "Who took your virginity?"
                "Emma" if True:


                    $ virginitylossby = "Emma"
                "Sarena" if True:
                    $ virginitylossby = "Sarena"
                "Berry" if True:
                    $ virginitylossby = "Berry"
                "Valerie" if True:
                    $ virginitylossby = "Valerie"
            menu:
                "Did you tell [en] you love her?"
                "Yes, I love [en] and want her to be my girl-friend!" if True:
                    $ ispromisedtoemma = True
                "No, I'm not in-love with [en] I'm not ready to be her boyfriend." if True:
                    $ ispromisedtoemma = False
            menu:
                "Do you want to jump to before, or after the ending events?"
                "Before the ending" if True:
                    pause
                "After the ending" if True:
                    $ bstep = 4
                    $ estep = 4
                    $ vstep = 4
                    $ sstep = 4
        "No" if True:









            "You are not skipping content."
    return

define skipprologue = False

define persistent.firstplayprologue = False
label skipprologue:

    if ispatreonversion == True:
        call patreonskip from _call_patreonskip

    scene black with fade
    call incrskill ("tongueskill", 1) from _call_incrskill_129
    call incrskill ("tongueskill", 1) from _call_incrskill_130
    $ firstplay("zoecuni")
    $ firstplay("01emmamoveass")
    $ firstplay("01berrybj")
    show mc
    $ player_name = renpy.input("Enter your name (Default: Ero)")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Ero"
    "" "Your character is named [mc]!"
    "" "You skip the prologue. You now have to give a surname to the 4 girls."
    hide mc
    show sarena
    $ ssn = renpy.input("How should I call her? Example: \"You're my ____.\" Default: Best friend")
    $ ssn = ssn.strip()
    if ssn == "":
        $ ssn = "Best friend"
    $ ssn ="{color=#f95252}" + ssn +"{/color}"
    "" "[sn] is now called your \"[ssn]\"!"
    hide sarena
    show berry
    $ bsn = renpy.input("How should I call her? Example: \"You're my ____.\" Default: Lovely teacher")
    $ bsn = bsn.strip()
    if bsn == "":
        $ bsn = "Lovely teacher"
    $ bsn ="{color=#ff7ed3}" + bsn +"{/color}"
    "" "[bn] is now called your \"[bsn]\"!"
    hide berry
    show emma
    if skipprologue == True:
        if ispromisedtoemma == False:
            $ esn = renpy.input("How should I call her? Example: \"You're my ____.\" Default: Housemate")
            $ esn = esn.strip()
            if esn == "":
                $ esn = "Housemate"
        elif True:
            $ esn = renpy.input("How should I call her? Example: \"You're my ____.\" Default: Girlfriend")
            $ esn = esn.strip()
            if esn == "":
                $ esn = "Girlfriend"
    elif True:
        $ esn = renpy.input("How should I call her? Example: \"You're my ____.\" Default: Girlfriend's best friend")
        $ esn = esn.strip()
        if esn == "":
            $ esn = "Girlfriend's best friend"
    $ esn ="{color=#4083ff}" + esn +"{/color}"
    "" "[en] is now called your \"[esn]\"!"
    hide emma
    show valerie
    $ vsn = renpy.input("How should I call her? Example: \"You're my ____.\" Default: Dad's friend")
    $ vsn = vsn.strip()
    if vsn == "":
        $ vsn = "Dad's friend"
    $ vsn ="{color=#ea48c2}" + vsn +"{/color}"
    "" "[vn] is now called your \"[vsn]\"!"
    jump tomcroom
    return
label unlockreplays:
    $ persistent.replay1 = True
    $ persistent.replay2 = True
    $ persistent.replay3 = True
    $ persistent.replay4 = True
    $ persistent.replay5 = True
    $ persistent.replay6 = True
    $ persistent.replay7 = True
    $ persistent.replay8 = True
    $ persistent.replay9 = True
    $ persistent.replay10 = True
    $ persistent.replay11 = True
    $ persistent.replay12 = True
    $ persistent.replay13 = True
    $ persistent.replay14 = True
    $ persistent.replay15 = True
    $ persistent.replay16 = True
    $ persistent.replay17 = True
    $ persistent.replay18 = True
    $ persistent.replay19 = True
    $ persistent.replay20 = True
    $ persistent.replay21 = True
    $ persistent.replay22 = True
    $ persistent.replay23 = True
    $ persistent.replay24 = True
    $ persistent.replay25 = True
    $ persistent.replay26 = True
    $ persistent.replay27 = True
    $ persistent.replay28 = True
    $ persistent.replay29 = True
    $ persistent.replay30 = True
    $ persistent.replay31 = True
    $ persistent.replay32 = True
    $ persistent.replay33 = True
    $ persistent.replay34 = True
    $ persistent.replay35 = True
    $ persistent.replay36 = True
    $ persistent.replay37 = True
    $ persistent.replay38 = True
    $ persistent.replay39 = True
    $ persistent.replay40 = True
    $ persistent.replay41 = True
    $ persistent.replay42 = True
    $ persistent.replay43 = True
    $ persistent.replay44 = True
    $ persistent.replay45 = True
    $ persistent.replay46 = True
    $ persistent.replay47 = True
    $ persistent.replay48 = True
    $ persistent.replay49 = True
    $ persistent.replay50 = True
    $ persistent.replay51 = True
    $ persistent.replay52 = True
    $ persistent.replay53 = True
    $ persistent.replay54 = True
    $ persistent.replay55 = True
    $ persistent.replay56 = True
    $ persistent.replay57 = True
    $ persistent.replay58 = True
    $ persistent.replay59 = True
    $ persistent.replay60 = True
    $ persistent.replay61 = True
    $ persistent.replay62 = True
    $ persistent.replay63 = True
    $ persistent.replay64 = True
    $ persistent.replay65 = True
    $ persistent.replay66 = True
    $ persistent.replay67 = True
    $ persistent.replay68 = True
    $ persistent.replay69 = True
    $ persistent.replay70 = True
    $ persistent.replay71 = True
    $ persistent.replay72 = True
    $ persistent.replay73 = True
    $ persistent.replay74 = True
    $ persistent.replay75 = True
    $ persistent.replay76 = True
    $ persistent.replay77 = True
    $ persistent.replay78 = True
    $ persistent.replay79 = True
    $ persistent.replay80 = True
    $ persistent.replay81 = True
    $ persistent.replay82 = True
    $ persistent.replay83 = True
    $ persistent.replay84 = True
    $ persistent.replay85 = True
    $ persistent.replay86 = True
    $ persistent.replay87 = True
    $ persistent.replay88 = True
    $ persistent.replay89 = True
    $ persistent.replay90 = True
    $ persistent.replay91 = True
    $ persistent.replay92 = True
    $ persistent.replay93 = True
    $ persistent.replay94 = True
    $ persistent.replay95 = True
    $ persistent.replay96 = True
    $ persistent.replay97 = True
    $ persistent.replay98 = True
    $ persistent.replay99 = True
    $ persistent.replay100 = True

    $ persistent.replay101 = True
    $ persistent.replay102 = True
    $ persistent.replay103 = True
    $ persistent.replay104 = True
    $ persistent.replay105 = True
    $ persistent.replay106 = True

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
