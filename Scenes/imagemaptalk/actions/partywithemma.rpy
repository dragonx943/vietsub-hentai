label partywithemma:
    mc "Hey [en]! Wanna dance with me?"
    if estep == 0:
        e "YOU?!!"
        mc "Yes, why not?"
        e "So you really believe I'll let a loser like you approach me?!"
        mc "Oh come on! Stop being like this, why not just enjoy while we are just between us?"
        e "I!!"
        pause
        e "If you tell anybody about that, I'll cut your balls off."
        mcth "God damn, she is so mean to me! I really hope I can change that."
    elif estep == 1:
        show emma shy
        e "You-you want to dance with me?"
        mc "Yes, why not?"
        e "O-okay, but don't you dare touch me!"
        mc "I didn't intend to touch you, just dancing."
        e "I'm watching you."
    scene dancingbg with dissolve
    play music Wutif
    show edance
    pause
    mc "See, that's cool!"
    if estep == 0:
        e "..."
        mc "?"
        e "Just a little bit."
    elif estep == 1:
        e "Okay, it is..."
        mc "What did you just say?"
        e "Nothing."
    mcth "God daaaaaamn [en] looks so hot!!"
    mcth "How am I supposed to stay calm?!"
    show black with fade
    stop music
    "" "Many hours later..."
    "" "Everyone, but you two, left to sleep."
    scene dancingbg with dissolve
    play music chillsexy
    show mc drunk o5 with dissolve:
        xalign 0.35
    show emma o5 drunk with dissolve:
        xalign 0.65
    e "Rhoo, it seems everyone is already in bed..."
    if estep < 3:
        e "Well then, I won't stay alone with you."
        mc "I should escort you to your room."
        e "What? Why?"
        mc "Well I'm not sure you'll end up alive if you take the stairs considering your state."
        e "..."
        e "Do as you wish, I don't care."
        scene black with fade
        pause
        scene eparty0 with fade
        "" "In the stairs..."
        play sound hh
        show eparty1b
        if estep == 0:
            show eparty1bpantsu
        window hide
        pause
        window auto
        mcth "AAAAAH!"
        play sound hh
        if estep > 0:
            mcth "She isn't wearing any panties from the beginning!"
            mcth "How funny, it's as if she knew this scene gonna happen again and did it on purpose..."
            mcth "Is it possible?"
            mcth "Oh gosh..."
        mcth "This view is insane!!"
        play sound hh
        mcth "This big juicy booty..."
        play sound hh
        mcth "Imagine she falls on me haha!"
        e "Kiaaa! I missed the step!!!"
        hide eparty1 pantsu
        hide eparty1b
        if estep == 0:
            show eparty2 with vpunch
        if estep > 0:
            show eparty2nopantiesfall with vpunch
        "" "Emma missed the step and is falling on you!"
        mcth "OH MY!!"
        stop music
        play sound doublegrab
        if estep == 0:
            show eparty3 with hpunch
        if estep > 0:
            show eparty2nopanties with hpunch
        "" "By reflex you grab her butt."
        e "Kiaa!!"
        mcth "Great lord!!!"
        mcth "Her skin is so soft!!"
        mcth "If I compare with [zon], it's even more agreeable, but also a bit more firm!"
        mc "Are you alright, [en]?"
        e "R-remove your hands, you pervert!!"
        mcth "Then why doesn't she remove her butt from my hands?"
        pause
        if estep == 0:
            mcth "[en]'s crotch right in front of my face looks so impressive!"
            mcth "She told me her boyfriend is complaining she goes too crazy when he touches her."
            mcth "I wonder if..."
            hide eparty3
            show eparty4
            show edanceassfinger
            play sex emoans1
            play sexfx frottements
            e "Haaaan!!!! mpfh!"
            e "Hmm!!! hmm!!!"
            mcth "That's crazy how it became so hot so quickly!"
            e "NNNiuh!"
            mcth "She seems to like it, will she go crazy?"
            stop sex
            stop sexfx
            e "ENOUGH!"
            scene expression ifnight ("House/1stfloor/bg firstfloor talk.webp")
            show emma o5 angryshy at right
            show mc shy o5 at left
            show emma with vpunch
            e "Are you crazy or what?!!"
            mc "I'm sorry [en] I didn't want you to get hurt, so I grabbed you and..."
            e "Shut-up!!"
            e "I don't want to think about that. Nothing happened. Good night."
            scene bgemaassparty
            show ass emma o5
            "" "She turns back to you to enter her room."
            pause
            mcth "Woaw..."
            mcth "Look at these drips, she looks so wet! Just because of my finger caressing her crotch?"
            mcth "She seems way too horny!"
            mcth "Kind of fun tho'."
            scene black with dissolve
            mcth "Time to sleep."
            call incrskill ("handskill", 1) from _call_incrskill_67
            call incrdesire ("Emma", handskill) from _call_incrdesire_64
        elif estep == 1:
            mcth "[en]'s pussy is in front of my face once again."
            mcth "I'm 99%% sure she decided not to wear panties because she knew she gonna fall on me again."
            e "[mc]?"
            mcth "This girl... She's way too horny!"
            hide eparty2nopanties
            hide eparty2nopantiesfall
            hide eparty3
            show edanceassfingernopanties
            play sexfx frottements
            play sex emoans2
            window hide
            pause
            window auto
            e "[mc]!!!"
            e "St-"
            e "Houn~g!"
            mc "Is that what you wanted?"
            e "Wh-what are you talking about?"
            mc "Come on, why are you still lying?"
            e "I- don't-"
            mc "Be a good girl and I'll give you what you want!"
            e "You bastard!"
            e "I~... I missed~... this~..."
            mcth "Oh my gosh it's so funny to play with [en]'s pussy! She completely loses her defenses!"
            mcth "Let's make her cum!"
            hide edanceassfingernopanties
            play sex ecum1
            show edanceassfingernopantiescum at cumtr
            $ ecum += 1
            show cumanim
            pause
            e "Haaahuhah!"
            e "This feels so gooooood!!"
            call incrskill ("handskill", 2) from _call_incrskill_68
            call incrdesire ("Emma", handskill) from _call_incrdesire_65
            stop sexfx
            stop sex

        elif estep == 2:
            show elv2party with dissolve
            play sex emoans3
            play sexfx frottements2
            pause
            e "Niaaah!"
            mc "Hm... Delicious..."
            e "[mc], you m-"
            mc "You're so tasty, as usual, [en]."
            e "Oh fuck..."
            e "Hoooo [mc], you're so good at it!!"
            e "You know how to lick my pussy like an expert!!"
            show elv2party at cumtr
            show cumanim
            play sound ecum3
            stop sex
            stop sexfx
            pause
            scene expression ifnight ("House/1stfloor/bg firstfloor talk.webp") with fade
            show emma o5 drunk tsun at right
            show mc o5 humidface at left
            e "Thanks [mc]... That was good."
            mc "My pleasure."
            mc "Be honest, you expected that from the start, right?"
            e "I don't know what you're talking about."
            hide emma with dissolve
            call incrskill ("tongueskill", 2) from _call_incrskill_69
            call incrdesire ("Emma", tongueskill) from _call_incrdesire_66
            pause
            jump passnightnothing


    elif estep >2:
        mc "So... What should we do?"
        show emma smirk
        e "You gonna sit there while I'm riding you."
        show mc surprised
        mc "?!"
        e "Exactly!"
        show emma ahegao
        e "I'm so hungry for your cock I can't wait anymore!!"
        e "For once, I'm taking the lead!!"
        e "Just give it to me! Right now!"
        pause
        $ persistent.replay60 = True
        call esexparty (0.08) from _call_esexparty_2
        e "Oh my gosh!!"
        e "I feel like I'd never get used to [mc]'s size!"
        e "Your cock is MINE!"
        mc "[en], are you okay?"
        e "OH YEAH I AM!"
        call esexparty (0.04) from _call_esexparty_3
        e "YEAH, YEAH!"
        e "Lemme fuck that huge cock of yours!!"
        e "It's [en]'s property!!"
        mcth "[en] looks completely possessed!!"
        mcth "Her beast has woken up so fast, is it because of alcohol?"
        mc "[en], you can't move like that, it's impossible to resist any more!"
        e "Don't tell me things, it makes me even crazier!!"
        e "This is exactly what I want!!"
        mc "OH [en]!!"
        call esexpartycum from _call_esexpartycum_1
        e "I'm cummiiiiing!!!"
        e "I'm about to pass out!"
        e "[mc] is definitively the best..."
        stop sex
        stop sexfx
        $ ecum +=1
        $ cumbye +=1
        call incrskill ("cockskill", 3) from _call_incrskill_70
        call incrdesire ("Emma", cockskill) from _call_incrdesire_67
        pause

    jump passnightnothing
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
