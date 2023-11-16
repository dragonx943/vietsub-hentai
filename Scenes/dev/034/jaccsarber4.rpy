
label jacc4bersar:
    scene black
    "" "You change into your swimwear."
    "" "Suddenly, you hear two women giggling behind your back."

    call showscene ("034c") from _call_showscene_58
    s "Haha! Look who's here!"
    b "He looks so cute in his tight swimsuit!"
    s "He is!"
    b "I could eat him for a snack."
    s "Calm down, Mom! I want my slice too."
    "" "In front of you are two goddesses willing to devour you down to the last bone."
    call showscene ("034b") from _call_showscene_59
    mc "Hi! [bn], [sn]!"
    s "He doesn't know what awaits him, haha!"
    b "My candy!"
    s "My pony!!"
    mc "Would you like to join me?"
    b "Yes, but first we're going to play a little game."
    s "We're going to decide which one of us is the hot tub queen!"
    b "We'll take a pause, and you choose which of us is sexiest!"
    mcth "Shit ..."
    mcth "If I have to pick just one, I have a feeling one of them will be very unhappy ..."
    b "I'm starting!"
    call showscene ("034f") from _call_showscene_60

    "" "[bn] posed like a gangster."
    "" "She's looking down at you, legs spread."
    "" "She demonstrates a certain dominance, while being a leader in charge of the situation."
    s "Now it's my turn!"
    call showscene ("034e") from _call_showscene_61

    "" "[sn] posed to demonstrate her flexibility!"
    "" "She managed to do the splits without any difficulty, due to years of training!"
    s "I'm the most flexible! And we know how important that is ..."
    call showscene ("034d") from _call_showscene_62

    b "Haha! Look how red he is!"
    s "Is it just me, or is he getting a hard-on just because we posed in front of him?"
    b "It's normal, we're very sexy women! Especially me, Haha!"
    s "But I've got more abs!"
    b "And I've got bigger breasts!"
    s "Well, [mc], it's time to choose!"
    b "The hot tub queen gets a prize."
    s "She gets to ask [mc] for a massage!"
    mc "A massage, where exactly?"
    b "It doesn't matter, the winner decides."
    s "So, who wins? Who's the sexiest? The mother or the daughter?"
    menu:
        "Who wins?"
        "[sn]" if True:

            call showimgfury ("034g") from _call_showimgfury_2
            s "[mc]!!!"
            b "Eh!"
            s "I knew you'd choose me!"
            b "[mc], let her go right now!"
            s "You no longer have a say, I'm the winner!"
            call showscene ("034h") from _call_showscene_63
            s "You may have bigger tits than me, but that's nothing compared to the love between me and him!"
            b "Let him go, he'll choke!"
            s "Come on! You're always stuffing his head between your breasts too!"
            s "But enough with the jokes, it's time for the massage..."
            s "And I want him to massage me..."
            s "Breasts, precisely!"
            call showimgfury ("berjacctalk0") from _call_showimgfury_3
            b "What?!!"
            mc "!!!"
            b "Do you want your mother to discipline you?!"
            b "That's not what we agreed!"
            s "Of course it is! The winner can choose where [mc] will massage her."
            b "Yes, but I was thinking of a more normal massage spot."
            s "It's decided!"
            scene black with dissolve
            pause
            "" "A few moments later..."
            pause
            stop music
            call sartmassjacc034 (v=1.0/6) from _call_sartmassjacc034_1
            $ persistent.replay118 = True
            s "Oh yes, [mc]!"
            s "You're so good with your hands!"
            mc " Oh, [sn]!"
            mc "Your breasts are so voluptuous, but at the same time so delicate..."
            s "Your hands are so warm, firm, but tender at the same time."
            s "I love it when you touch them lovingly like you do now!"
            b "Bullshit!!!"
            s "What's the matter, Mom?"
            s "Are you jealous?"
            b "Not in the least! I know he'd rather massage my boobs!"
            "" "Hand skill [handskill]/[maxskill]"
            if handskill < maxskill:

                call showscene ("034d") from _call_showscene_64
                pause
                call incrskill ("handskill", 3) from _call_incrskill_137
                s "Thank you, [mc], for sharing this pleasant moment..."
                s "I hope with all my heart that next time you'll choose me again!"
                s "May I have the honor of feeling your hands on my breasts one more time, Haha!"
                b "No matter what, next time I'll win!"
            elif True:

                stop sex
                call showscene ("034l") from _call_showscene_65
                s "Oh, [mc] ..."
                s "You're so talented ..."
                s "I can't take it anymore, take off your clothes!"
                b "What?!"
                s "What the hell? You said you weren't jealous!"
                call sartjjacc034 (v=1.0/12) from _call_sartjjacc034_2

                b "Grrr!"
                b "What are you doing to my candy?!"
                s "I think you can tell, can't you?"
                s "I thank him for taking such good care of me!"
                b "You could have just said thank you!"
                s "Yes, but I love feeling his cock between my breasts so much..."
                b "[sn]!"
                s "She's so hot, and so hard!"
                s "I feel it inflate slightly more with each second that passes."
                s "It's as if it's awakened a volcano inside [mc] ..."
                s "It's burning with desire, and I'm going to make it erupt!"
                b "No!!"
                call sartjjacc034 (v=1.0/24) from _call_sartjjacc034_3

                s "Yes!"
                mc "Oh no! [sn]!"
                b "[mc]! I forbid you to come!"
                mc "It's impossible, [sn] makes me feel much too good!"
                b "[mc]!!"
                s "Unleash the volcano, [mc]!"
                s "It makes me so horny to see you cum between my breasts!"
                mc "I'm cumming!!"
                call sartjjacccum034 from _call_sartjjacccum034_1

                "" "The second the first drop of semen came out of your glans, Sarena rushed to put it in her mouth."
                "" "As time went on, [sn] developed a serious addiction to your cum."
                "" "She doesn't want to waste a drop."
                b "[sn]!!"
                s "What a delight..."
                s "[mc]'s cum is probably the thing I love most in the world ..."
                s "I could eat it all day long ..."

                call showscene ("034i") from _call_showscene_66
                mc "Hmmpf!!!"
                b "You're a bad boy."
                b "Cumming between my own daughter's breasts ... And in front of me!"
                b "I forgive you, but I warn you, you're going to have to be very nice to me."
                $ cumbys += 1
                $ persistent.replay119 = True
        "[bn]" if True:

            b "I knew it!"
            s "Oh no!"
            b "You can't beat your mother, haha!"
            b "I'm the sexiest!"
            b "Regarding the massage I won ..."
            b "I request a foot massage."
            call showscene ("sarjacctalk0") from _call_showscene_67
            s "Really? Just the feet?"
            b "Well yes, is there a problem?"
            s "I'd have thought you'd ask her to a different ... Place."
            b "What are you talking about? A foot massage is a classic!"
            b "[mc] is a very good boy, who takes care of the women he loves."
            s "I can sense the trickery..."
            b "No, you're not!"
            b "Let's go."
            scene black with dissolve
            pause
            "" "A few moments later..."
            play sex vmoanstj
            call showimg ("berfootj1jacc") from _call_showimg_26
            b "It's so good, [mc] ..."
            b "You are so good at taking care of women my age ..."
            mc "Your age?!"
            mc "Come on, you talk as if you were old, but you're not at all!"
            b "Oh, [mc]..."
            s "Stop flirting around me!"
            "" "Hand skill [handskill]/[maxskill]"
            if handskill < maxskill:

                call showscene ("034d") from _call_showscene_68
                pause
                call incrskill ("handskill", 3) from _call_incrskill_138
                b "Thank you, [mc]."
                b "That was really nice..."
                b "I'll have to remember to thank you, privately ..."
                s "It's ok, she thanked you, get off her feet!"
            elif True:
                b "Oh my god this is so good!"
                b "You deserve an immediate reward!"
                s "Wait, what are you talking about? That wasn't in the agreement!"
                b "But my candy is such a good boy, he deserves a reward, right now!"
                b "Tell me, [mc], in the moment, do you like my feet more, or my breasts?"
                menu:
                    "Footjob or Titsjob?"
                    "Footjob" if True:
                        call berfootjjacc034 (v=1.0/6) from _call_berfootjjacc034_2
                        $ persistent.replay113 = True
                        $ cumbyb += 1
                        s "Oh my god!!!"
                        s "What the hell are you doing to him?!"
                        b "That's my good boy!"
                        b "Don't move... Let me do the work."
                        b "My foot thanks you for treating it so well."
                        s "Oh my god ... Does [mc] like this kind of stuff? I didn't know!"
                        b "He likes every part of my body."
                        b "I can make him orgasm any way I want."
                        call berfootjjacc034 (v=1.0/12) from _call_berfootjjacc034_3
                        b "[mc] is mine!"
                        b "My candy obeys me, like a good boy!"
                        b "Now cum for me!"
                        b "Come on, cum now!"
                        mc "Haaaa!"
                        call berfootjjacccum034 from _call_berfootjjacccum034_1
                        b "Oh yes!"
                        b "My good boy!"
                        b "You loved cumming with my foot, didn't you?"
                        mc "Yes, [bn]!"
                        b "That's good ..."
                        b "Remember that, [sn], I can make [mc] climax with absolutely every part of my body!"
                        b "I'm the one he loves the most!"
                    "Titsjob" if True:
                        stop music
                        call bertjjacc034 (v=1.0/12) from _call_bertjjacc034_2
                        s "Stop it!"
                        b "Why would I stop?"
                        b "Look at him, look at him!"
                        b "His face is contorting with pleasure, Haha!"
                        mc "It's so nice!"
                        b "Nice enough to make you cum in seconds, isn't it?"
                        s "No!"
                        s "Only my own breasts can make him come!"
                        b "What are you talking about?"
                        call bertjjacc034 (v=1.0/24) from _call_bertjjacc034_3

                        mc "Oh my god!"
                        s "Stop it!"
                        b "My boobs are the biggest, but not only!"
                        b "He's been fantasizing about my huge breasts since the very second he first saw me!"
                        b "He has masturbated countless times thinking about cumming between my breasts, I know it!"
                        mc "[bn], I can't hold out any longer!"
                        b "And I don't want you to hold any longer!"
                        b "Go ahead, empty your balls!"
                        b "I want to see your face twitch with pleasure as you cover mine with your sperm!"
                        call bertjjacccum034 from _call_bertjjacccum034_1

                        mc "Haaaa!"
                        mc "Hooo!"
                        b "Oh my God!"
                        b "What a tremendous amount of semen!"
                        b "No matter how much I know, it still surprises me!"
                        s "No! [mc] came between the breasts of another woman than me!"
                        s "That's not possible!!!"
                        b "It's obviously possible, because I'm the woman of his dreams!"
                        s "I refuse! From now on, I'm going to make him cum twice as much every day!"
                        $ persistent.replay121 = True
                        $ cumbyb += 1
    jump passtime
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
