

label talke:
    scene bg pcroom
    show mc at left
    if estep < 3:
        show emma at right
        play sound esoupir
        e "What do you want, loser?"
    elif estep == 3:
        show emma tsun at right
        e "Oh... Hey, [mc]..."
    elif True:
        if ispromisedtoemma == True:
            e "Hello, my lovely boyfriend!"
        elif True:
            e "Hey... [mc]..."
    menu:
        "{color=#ff9a40}What are you doing?{/color} Orange color = Quest" if qpreptalke == False:
            jump eprepwork

        "\"You look really pretty today!([estep])\"" if estep > 0:
            if estep == 1:
                show emma embarrassed
                e "As... as If I care..."
                e "Now let me work and leave the room, please."
                jump topcroom
            if estep == 2:
                show emma embarrassed
                e "R-really?"
                e "T-thank you!"
                jump topcroom
            if estep > 2:
                show emma tsun
                e "I'm so happy [mc] thinks I'm pretty!"
                e "I hope he's gonna fuck me."
                show mc shy
                mc "I can hear you, you know?"
                e "Oopsie!"
                e "Hehehe!"
                jump topcroom
        "Quit" if True:

            jump topcroom

label eprepwork:
    $ qpreptalke = True
    e "What?!"
    mc "I don't know, I wanna... get to know you more. I'm sure there's a good person under that shell."
    pause
    e "Why the hell did I end up under the same roof as you..."
    e "I'm setting up the accounts for my new activity."
    mc "What will you be doing?"
    e "I'm starting a dancing activity."
    mc "Dancing? I want to see that! What kind of dancing?"
    e "I won't show my goddess-like moves to a loser like you!"
    e "Just stop bothering me and let me work!"
    if qpreptalkv == True and qpreptalkb == True and qpreptalke == True and qpreptalks == True:
        $ qpreptalk = True
    jump topcroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
