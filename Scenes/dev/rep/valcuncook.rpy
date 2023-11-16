



label valcuncook:


    v "Wow, truly remaining objective. I almost respect it."
    mc "And I'm almost full, but not quite. Where's my dessert, [vn]?"
    v "What do you mean?"
    mc "Wait... Something... I smell..."
    v "[mc], what are you doing?"
    mc "FOUND IT!"



    window hide
    scene v2g at angryjump
    play sex vmoans1
    pause
    window auto

    v "Hey!! What are you doing!?"
    mc "Getting my dessert, bitch!"
    v "But we're in the middle of the- mmm, the-"
    mc "The what?"
    v "Oh, just shut up and keep going!"
    mc "I'll make you pay for speaking to me that way."
    v "Do whatever you want!!"
    v "Ffffffuck! As long as you make me feel this way, I'm all yours!"
    v "Holy shit, I'm so fucking wet! Nobody's ever eaten my pussy like this!"
    v "Hmmmm I'm getting so close!"
    v "I'm gonna-! I'm gonna-!"


    window hide
    stop sex
    play audio vcum1
    show v2g at cumtr
    show cumanim
    pause
    window auto

    v "Ohhhhhhh FUCK!!"
    v "That feels so gooooood!"
    $ vcum +=1
    scene cookbg with dissolve
    show mc lol at left
    show valerie angryshy:
        xalign 0.6

    mc "Delicious. I could have that after every meal."
    "[vn] instinctively goes to say something snarky but changes her mind."
    show valerie mad
    "" "Her face then begins to turn red and she quickly leaves."
    hide valerie with dissolve
    mcth "Am I going crazy, or was that kinda cute?"
    mcth "Shit. I might actually like seeing her like that."


    $ vcum +=1
    call incrskill ("tongueskill", 2) from _call_incrskill_8
    call incrdesire ("Valerie", tongueskill) from _call_incrdesire_10
    jump passtime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
