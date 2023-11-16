label partywithvalerie:
    mc "Wanna dance with me?"
    show valerie surprised
    if vstep <3:
        v "Whaaaaat?!"
        v "What's happening in your mind? Are you sane?"
        mc "What again? I just wanna dance with you to build a better relationship for the good of the house."
        pause
        show valerie happy
        v "So... You... want to dance with your \"[vsn]\"? Like if I'd accept that HAHA!"
        show mc serious
        mc "Oh my god, I really wonder what my dad likes in you!!"
        v "Hoh? I'll show you!"
    elif vstep >2:
        v "Oooh! I see, you're not hiding you like me anymore..."
        v "Alright then, with pleasure!"
    scene dancingbg with dissolve
    play music Wutif
    show vdance
    "" "She grabs your hands and makes you dance with her."
    v "You see? He loves that hot body of mine!"
    v "I could even make you fall in love with me if I wanted to."
    if vstep <3:
        v "I don't, of course."
        mc "In your dreams haha!"
        mcth "Well, I could never fall in love with her, but her body is so hot..."
    show black with fade
    stop music
    "" "Many hours later..."
    "" "Everyone, but you two, left to sleep."
    play music chillsexy
    scene dancingbg with dissolve
    show mc drunk o5 with dissolve:
        xalign 0.35
    show valerie o5 drunk with dissolve:
        xalign 0.65
    v "Hoh? Seems that everyone left."
    mc "Wants me to escort you to your room?"
    if vstep >2:
        $ persistent.replay69 = True
        jump valsexparty

    v "Like I'd need your help haha!"
    v "I just need my drink."
    v "Speaking of it, where is it?"
    mc "Hm, I think I saw you putting it behind the couch."
    v "Oh right, then I take it and leave."
    scene partyv1 with fade
    pause
    mcth "Great lord..."
    v "Argh! I'm stuck!"
    v "I think I drank too much I can't help to get up!"
    pause
    v "Oh come on, brat! Help me!!"
    mc "So you're stuck?"
    v "Yes!!!"
    mc "And you call me a brat?"
    v "... Don't think about what I'm thinking!!"
    scene valfesseebg
    show valfesseeculotte
    mc "That view is incredible!"
    v "Shut up and help me!!"
    v "Come on, do it for your sweet [vsn]..."
    mc "Haha sweet? I think you aren't sweet. You deserve a punishment."
    v "WHAT?! What are you talking about??"
    menu:
        "What do you do to [vn]?"
        "Spank her!" if True:
            jump vspankparty
        "Show her pussy and play with it." if vstep > 0:
            hide valfesseeculotte
            show valfessee culotte2 with hpunch
            pause
            v "Wh-what do you intend to do?!"
            v "Put it back!"
            mc "You always get stuck in this position. It's almost like you do it on purpose."
            v "Wh-what are you saying?"
            window hide
            scene black
            show 016doublefinger
            play sexfx frottements2
            play sex vmoansdrunk
            pause
            window auto
            v "You bastard!!"
            v "How can you do-"
            v "Oh, That feels so good!"
            mc "Do you like when I'm touching you?"
            v "Oh yeah, I love it so much, you're so good!"
            v "But I will never tell you I love that, or you'll get full of yourself!"
            v "Don't tell your Dad I told you that!"
            mc "I'll keep my mouth closed."
            mc "For now, the most important is-"
            $ persistent.replay58 = True
            window hide
            hide 016doublefinger
            show 016doublefingercum at cumtr
            show cumanim
            stop sexfx
            stop sex
            play audio vcum1
            $ vcum +=1
            pause
            window auto
            v "So gooood!"
            v "You're so much better than your Dad!"
            mc "Oh am I?"
            v "SECRET!"
            mc "Yes, yes!"
            scene black with fade
            "" "You bring her back into her bed."
            call incrskill ("handskill", 3) from _call_incrskill_46
            call incrdesire ("Valerie", handskill) from _call_incrdesire_34
            jump passtime
            return
        "Move to the other side and fuckthroat her." if vstep > 1:
            mc "I'm guessing you expect me to eat your pussy."
            v "No!! But, if that's what you want, I can't move, so I wouldn't be able to stop you..."
            mc "That's not fun if I do what you expect from me."
            v "Hm?"
            scene black with fade
            mc "It's time to give you what you deserve."

            window hide
            stop music
            scene bgv2p:
                xalign 0.5
                yalign 0.5
            play sex vdt2s
            show v2party
            pause
            window auto
            mc "Oh shit!!"
            pause
            mc "My [vsn]'s throat is so tight!"
            mc "I've got to force into it, but it feels so good!"
            v "Hm!!!"
            mc "Oh, I know you like it. You love so much when I use you like this."
            mc "You love being a dirty slut, don't you?"
            v "Mh!!"
            mc "You love to be my cumrag!"
            mc "You love when you get punished for your behavior!"
            mc "I'm cumming!"

            $ persistent.replay47 = True
            window hide
            hide v2party
            stop sexfx
            stop sex
            play audio vcuminthroat
            play audio cumexplo
            play audio cumsound
            show v2partycum
            show cumanim
            pause
            window auto
            mc "Oh shit..."
            mc "I can feel your throat trying to swallow every drop of my cum..."
            $ cumbyv +=1
            call incrskill ("cockskill", 2) from _call_incrskill_47
            call incrdesire ("Valerie", cockskill) from _call_incrdesire_35
            pause
            scene black with fade
            jump passtime
            return



label vspankparty:
    play sound spank
    show valfesseebg with hpunch
    show valfessee fessee:
        alpha 0.0
        linear 1.0 alpha 0.5

    "" "PUUH!!"
    play sound vmoansp1
    v "Haaan!!!"
    mc "Ha? Was it a scream or a moan?"
    v "Shut up!"
    play sound spank
    show valfessee with hpunch
    show valfessee fessee:
        linear 1.0 alpha 1.0
    "" "PUUH!!"
    play sound vmoansp2
    v "Haaan!!!"
    mc "Yeah that was definitely a moan!"
    if vstep == 0:
        scene dancingbg
        show mc drunk o5 with dissolve:
            xalign 0.35
        show valerie o5 angryshy drunk with dissolve:
            xalign 0.65
        v "YOU LITTLE SHIT OF BRAT!!"
        v "How dare you!!!"
        mc "Well, at least you succeeded in getting up! I think you're underestimating yourself."
        v "YOU little..."
        v "Rha fuck, you're lucky I'm drunk..."
        v "I'm going back, don't follow me."
        hide valerie with dissolve
        mc "Mouahaha, It was so satisfying!!!"
        mc "..."
        mc "I think I wish to punish her a little harder in the future!!"
        call incrskill ("handskill", 1) from _call_incrskill_48
        call incrdesire ("Valerie", handskill) from _call_incrdesire_36
    jump passtime
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
