label jacuzzi:
    if Swimwear not in inventory.items:
        scene jacuzzibg
        show mc
        mc "Hm... I should order swimwear on the internet..."
        jump tobackyard
    elif True:
        scene jacuzzibg
        show mc
        mc "Aaaaaah, a jacuzzi at home, do I need anything more than this?"
        show mc oswimwear with dissolve
        pause 1.0
        mc "Aaaah..."
        mc "It would be cool if I could relax with a few girls..."
        menu:
            "Which duo should arrive?"
            "[sn]/[bn]" if bstep > 0 and sstep > 0:
                if bstep == 4:
                    "" "Affection between [bn] and [sn] = [bbounds]/24"
                    if bbounds > 23:
                        jump jacc4bersar

                show mc at left
                show sarena o3 at center with dissolve
                s "Heeeey!"
                s "Look at this handsome booooy!"
                mc "Hey [sn]!"
                s "Did you want to use the jacuzzi?"
                mc "Yeah, wanna join?"
                s "Of course!"
                show sarena taunt
                s "Oh no! There is no place for two people!"
                mc "What do you mean? there is obviously enough space..."
                s "No, there isn't! It means I will have to relax, sitting on you again..."
                mc "Oh..."
                show mc lol
                mc "How did I not see it!! It's a one-person jacuzzi!"
                mc "You'll have to sit on me..."
                show berry o3 ordering at right
                b "Hum hum!"
                show sarena happy
                s "Mom! I love your bikini!"
                b "Thank you, but I've heard about you sitting on [mc], I think it's indecent."
                s "Ah?"
                b "[mc] is precious, I prefer no woman to approach him."
                show sarena taunt
                s "No woman but you, right?"
                b "Of course I don't count! I'm sure I won't hurt him, so I'm allowed!"
                show sarena happy
                s "And, you think I will hurt him?"
                show berry shy
                b "No it's not-"
                show sarena challenge
                s "You are just jealous!!!!"
                show berry at angryjump
                b "What are you talking about!"
                s "Let him decide."
                b "Decide?"
                s "The Queen of jacuzzi can decide who sits where."
                b "I won't lose my precious candy!"
                mc "The queen of Jacuzzi?"
                s "Look here!"
                scene jacuzzibgtits with dissolve
                play music causmic
                window hide
                show tits s bikini with dissolve
                pause
                window auto
                s "I know [mc] love my tiddies..."
                s "Remember... the feeling of your face in them..."
                b "[sn]!! Aren't you ashamed to use your body to win a contest?!"
                s "Well, I'm gonna win."
                window hide
                show tits berry bikini with dissolve
                pause
                window auto
                b "You think you'll win? He prefers his [bsn]'s chest, obviously."
                b "Look at my big... juicy... tits... just for you..."
                s "Mooom! That's not fair!"
                window hide
                scene jacuzzibgasses with dissolve
                show ass sarena bikini with dissolve
                pause
                window auto
                s "Guess who's got a muscular butt!!"
                s "The butt that used to make you hard so many times by sitting on you..."
                b "HARD?!"
                b "No!!"
                window hide
                show ass berry bikini with dissolve
                pause
                window auto
                b "I'm not that muscular, but I'm thick enough!"
                s "Oh haha, and now, who's doing indecent things?"
                scene jacuzzibg
                show mc oswimwear shy at left
                show sarena o3 at center
                show berry o3:
                    xalign 0.7
                mcth "Oh my gosh... They really know I can't resist both of them..."
                menu:
                    "Who is the Queen of Jacuzzi?"
                    "[bn]" if True:
                        show berry happy
                        b "Of course I am! I'm the first woman in his life!"
                        s "Rhooo, I was sure I could win... But no shame in losing against my Mom."
                        b "So, I can choose who goes where..."
                        scene black with dissolve
                        window hide
                        pause 1.0
                        scene jacuzziberry with dissolve
                        play sound bgoodboy
                        pause
                        window auto
                        b "Perfection!"
                        mcth "Urh! She's crushing my head so hard!"
                        s "[mc]?! Are you alright?"
                        b "Of course he is!"
                        s "But you're squishing his head!"
                        mc "I-it's okay..."
                        mcth "I'm dying, but I'll die happy!!"
                        s "Moh..."
                        pause
                        "" "You stayed in the jacuzzi for an hour."
                        "" "[sn] was jealous of how close [bn] was with you."
                        "" "[bn] discreetly caressed your bulge with her feet underwater, while saying \"Good boy...\" repetitively."
                        "" "They both had a good relaxing time together, and their affection increased."
                        call incrdesire ("Berry", 2) from _call_incrdesire_52

                        if bstep >1:
                            scene jacuzzibg
                            show mc oswimwear shy at left
                            show berry o3 serious at center
                            b "[sn] is finally gone."
                            mc "Why do you look so... Upset? What's wrong?"
                            b "You stared at her breast while I gave you affection."
                            b "I am NOT happy!"
                            b "I know how you love big tits."
                            b "No one has them bigger than mine!"
                            b "I want you to ask for forgiveness."
                            mc "Er... I demand your pardon, [bn], Er... your tits are my favorites."
                            show berry at angryjump
                            b "Not enough!"
                            mc "What can I do?!"
                            show berry base
                            b "You'll have to show me your passion."
                            pause
                            window hide
                            scene 026a with fade
                            play sex bmoans1
                            play sexfx frottements
                            pause
                            window auto
                            b "I definitely have to teach you!"
                            b "Looking at another woman's breast... While I'm cuddling you?"
                            b "You're really naughty sometimes..."
                            b "Oh yeah..."
                            b "Keep sucking my nipple."
                            b "More!"
                            b "Mooore!"
                            b "Did you know? A woman can orgasm with her nipples."
                            b "In fact, any erogenous spot can give an orgasm!"
                            b "With the right person, the passion."
                            b "You have to get used to your partner's body, and she has to be aware of that."
                            b "It's still pretty rare, but I know that you can-"
                            b "-Oh yeah, you know exactly how I like you to suck on them!!"
                            b "This is what I'm talking about!!"
                            window hide
                            show 026acum
                            show cumsfx:
                                xalign 0.65
                                yalign 0.5
                            stop sex
                            stop sexfx
                            play audio bcum1
                            pause
                            window auto
                            b "Oh yeaaaaah!!"
                            b "My sweety knows my body so well!!"
                            call incrskill ("tongueskill", 2) from _call_incrskill_60
                            call incrdesire ("Berry", tongueskill) from _call_incrdesire_53
                            $ bcum+=1
                            pause
                            scene black with dissolve
                    "[sn]" if True:
                        show sarena happy
                        s "My pony!!! Nobody can surpass our bonds!"
                        show berry ordering
                        b "[mc]! How did you not choose me! I'll have to punish you later."
                        s "Punish? Isn't that a bit exaggerated? haha!"
                        s "So as I won, I can choose who goes where..."
                        scene black with dissolve
                        window hide
                        pause 1.0
                        scene jacuzzisarena with dissolve
                        play sound smoh1
                        pause
                        window auto
                        s "Ah.. that's so good..."
                        b "[sn]!!!"
                        s "Yes?"
                        b "Pay attention!! Your nipples are out!!"
                        s "Oh really? That's so shameful... But I feel great. I prefer not to move right now..."
                        b "How indecent!"
                        b "[mc] shouldn't have to go through this..."
                        s "You're just mad because he's comforted by someone else's tits?"
                        b "[sn]!"
                        s "Don't worry, I would never hurt your candy, you can trust me."
                        b "Mmh..."
                        pause
                        "" "You stayed in the jacuzzi for an hour."
                        "" "[bn] was jealous but calmed herself down as she knows how close both of you are."
                        "" "She still got mad to see your face in free tits but wasn't mad at [sn] at all."
                        "" "[sn] felt so relaxed and good. Your face in her tits, warm bubbles on her skin... and your hard erection against her crotch."
                        "" "She obviously noticed it and discreetly moved her hips on it underwater."
                        "" "After a bit of time, there was no tension from [bn] and you all three just talked and had fun."
                        "" "They both had a good relaxing time together and their affection increased."
                        call incrdesire ("Sarena", 2) from _call_incrdesire_54
                        if sstep > 1:
                            scene jacuzzibg
                            show mc oswimwear shy at left
                            show sarena o3 at center
                            s "[bn] is finally gone."
                            mc "Finally?"
                            s "You turned me on so much!"
                            s "Now, time to take your responsibilities!"
                            s "I can't hold back any more!!"
                            window hide
                            stop music
                            scene 021jaccbg
                            play sex shardmoans1
                            play sexfx frottements2
                            $ persistent.replay42 = True
                            show 021jacc
                            show 021jaccbulles
                            pause
                            window auto
                            mc "!!"
                            s "Oooh, Your mouth feels so good!"
                            s "I hope I'm not hurting you!!"
                            mc "It's good!"
                            s "Oooh!"
                            s "It's almost as if I'm fucking your face!"
                            s "Oooh I'm so lucky to have you!!"
                            s "I'm about to cum so hard I can feel it!"

                            window hide
                            hide 021jacc
                            hide 021jaccbulles
                            stop sexfx
                            play sex scum1
                            show 021jacccum
                            show 021jaccbulles
                            show cumanim
                            $ cumbys +=1
                            pause
                            window auto
                            s "Haaaaaa!"
                            s "I'm cumming all over your face, [mc]!"
                            s "I'm so addicted to you!!"
                            call incrskill ("tongueskill", 2) from _call_incrskill_61
                            call incrdesire ("Sarena", tongueskill) from _call_incrdesire_55
                            pause
                            scene black with dissolve
                if bbounds + 5 < bboundsmax:
                    $ bbounds += 5
                jump passtime
                return
            "[en]/[vn]" if estep > 0 and vstep > 0:
                if bstep == 4:
                    "" "Affection between [vn] and [en] = [vbounde]/24"
                    if vbounde > 23:
                        jump jacc4emmval
                show mc at left
                show emma o2 at center with dissolve
                if estep < 3:
                    e "Don't tell me you wanted to use the jacuzzi. I was about to use it."
                    mc "Oh well, no problems, we can use it together!"
                elif True:
                    e "Hey [mc], are you there for the jacuzzi?"
                    mc "Sure, wanna go together?"
                show valerie o4 at right with dissolve
                v "Hey youngsters, how is it going?"
                if estep < 3:
                    e "[mc] trying to steal my place at the jacuzzi!"
                elif True:
                    e "[mc] and I, are about to use the jacuzzi, but I'm sure there is enough space for three."
                v "Come on, girl, we won't let a man get what WE deserve!"
                e "Yeah, you're right!"
                mcth "Hm... I've got an idea."
                mc "Wow, you both look really great!"
                e "Yeah, thanks."
                v "Obviously."
                mc "Or maybe [vn] has better tits? or [en] has a better butt?"
                show emma angryshy
                show valerie angryshy
                e "HEY!"
                v "Calm down, girl!"
                show valerie happy
                v "I'm sure your tits aren't that bad..."
                e "What?!"
                show emma smirk
                e "haha, and I'm sure your ass isn't bad either!"
                v "Wanna challenge me, girl?"
                e "I won't lose against you!"
                v "[mc], choose who is the Queen of Jacuzzi."
                mc "Er..."
                e "Tsah! I can convince him whenever I want."
                scene jacuzzibgtits with dissolve
                play music causmic
                window hide
                show tits emmabikini
                pause
                window auto
                e "I just have to stand up like this and he'll immediately vote for me."
                v "You indeed are a good-looking girl, but..."
                window hide
                show tits valbikini with dissolve
                pause
                window auto
                v "You will reach my level in a few years, but for now... I know bodies that men like..."
                e "You look very confident! However, none can beat [en]'s butt!"
                scene jacuzzibgasses with dissolve
                window hide
                show ass emma 5 with dissolve
                pause
                window auto
                e "I'm not the most popular girl for nothing!"
                v "Oh! I was also the most popular one at school!"
                e "Oh really!"
                v "Sure! Look at this!"
                window hide
                show ass valerie bikini with dissolve
                pause
                window auto
                e "Ouah!"
                v "Yes, haha!"
                v "So, little boy, decide who's the Queen of Jacuzzi?"
                scene jacuzzibg
                show mc oswimwear shy at left
                show emma smirk o2 at center
                show valerie happy o4:
                    xalign 0.7
                mcth "They both look so hot..."
                menu:
                    "Who is the Queen of Jacuzzi?"
                    "[vn]" if True:
                        v "I knew it. I'm the hottest woman in the country."
                        show emma angry
                        e "Grr, that's not fair!"
                        show valerie shy
                        v "Actually, you're the prettiest girl I've ever seen, you'll be even better than myself in a few years."
                        show emma shy
                        e "Oh... that's very kind, thank you!"
                        show mc lol
                        mc "Hum, so... I think it's time for my reward."
                        show valerie base
                        v "Your reward?"
                        mc "Yes, for making you win!"
                        mc "Don't worry I won't ask for something greedy."
                        mc "Just let me choose who goes where in the jacuzzi."
                        v "Yeah, if you want."
                        scene black with dissolve
                        window hide
                        pause 1.0
                        scene jacuzzivalerie with dissolve
                        play sound vmoansp1
                        pause
                        window auto
                        e "Er... [vn], are you okay?"
                        v "Yes.. Yes.. I'm alright..."
                        "[vn]'s thoughts" "This motherfucker! He chose me to sit on his cock!!"
                        e "[mc] really is a pervert for asking you something like thi-"
                        v "That's good, thank you for worrying for me."
                        pause
                        "" "You stayed in the jacuzzi for an hour."
                        "" "Without realizing it, [vn]'s butt started to slowly rub against your erection."
                        "" "She was so embarrassed but did not try to move on from it."
                        "" "[en] gave you a few mad looks but didn't say anything."
                        "" "You were just feeling good, it felt so satisfying to see [vn] that embarrassed..."
                        "" "After a few minutes, [vn] and [en] started to talk about their life and [vn] tried to give [en] a few of her experiences."
                        "" "They both had a good relaxing time together and their affection increased."
                        call incrdesire ("Valerie", 2) from _call_incrdesire_56
                        if vstep > 1:
                            $ persistent.replay77 = True
                            call valjaccbj from _call_valjaccbj
                    "[en]" if True:
                        show emma shy
                        e "Oh my gosh, he really chose me?!"
                        v "Ah? Why are you surprised?"
                        show emma base
                        e "I don't know, I thought he'd choose you just to get me mad."
                        v "You deserved it, you're a Queen!"
                        show emma shy
                        e "Oh thank you [vn]..."
                        show mc lol
                        mc "Hum, so... I think it's time for my reward."
                        show valerie base
                        e "Your reward?"
                        mc "Yes, for making you win!"
                        mc "Don't worry, I won't ask for something greedy."
                        mc "Just let me choose who goes where in the jacuzzi."
                        e "Er, yes, I guess that doesn't matter."
                        scene black with dissolve
                        window hide
                        pause 1.0
                        scene jacuzziemma with dissolve
                        play sound emoansingle
                        pause
                        window auto
                        v "Oooh I didn't know [mc] and you were..."
                        e "No! We're not at all!"
                        call incrdesire ("Emma", 2) from _call_incrdesire_57
                        if estep == 1:
                            e "You bastard! I didn't expect you'd..."
                            mc "Calm down [en] just relax, don't you feel good?"
                            e "I... I feel good, but it's not because of you. It's just the jacuzzi, right?"
                            mc "Yes, right."
                        elif estep == 2:
                            show jacuzziemma at angryjump
                            mc "!!!"
                            mc "[en] What are you doing?!"
                            mcth "She just removed my swimsuit and hers!!"
                            e "W-what are you talking about-"
                            mcth "She said that while slowly rubbing her pussy against my cock..."
                            mcth "... In front of [vn]..."
                            mcth "Oh [en] you're so naughty!"
                        elif estep >2:
                            mc "Are you good, [en]?"
                            e "You already know how crazy I feel when we're that close!"
                            e "But in front of [vn]..."
                        pause
                        "" "You stayed in the jacuzzi for an hour."
                        "" "[en] felt your erection slip between her thighs, but didn't react."
                        "" "She even moves slowly on it, trying to hide her moans."
                        "" "After a few minutes, [vn] and [en] started to talk about their life and [vn] tried to give [en] a few of her experiences."
                        "" "They both had a good relaxing time together, and their affection increased."
                        if estep > 1:
                            scene black with dissolve
                            "" "However, After [vn] left..."
                            window hide
                            play sex emoans3
                            play sexfx sex05
                            show 019thf
                            pause
                            window auto
                            mc "[en]! You're such a naughty girl..."
                            mc "Arousing me in front of [vn]..."
                            e "I wasn't trying to-"
                            mc "Oh you were!"
                            e "Just leave me alone!"
                            mc "What are you talking about?"
                            mc "Your pussy's lips are devouring my cock, and your hands don't want to let ME go!"
                            e "Haa [mc]!!"
                            mcth "[en] is squeezing my cock too hard. It's almost as if I were fucking her!"
                            mc "I'm cumming!"
                            e "Me as well!!"
                            window hide
                            hide 019thf
                            stop sexfx
                            play sex ecum2
                            play audio cumexplo
                            play audio cumsoundext
                            show 019thfcumb
                            show 019thfcuma
                            show cumanim
                            pause
                            window auto
                            $ persistent.replay32 = True
                            e "I'm cumming on [mc]'s diiick!!!"
                            $ ecum +=1
                            $ cumbye +=1
                            stop sex
                            call incrskill ("cockskill", 2) from _call_incrskill_62
                            call incrdesire ("Emma", cockskill) from _call_incrdesire_58
                            scene black with dissolve
                            pause



                if vbounde + 5 < vboundemax:
                    $ vbounde += 5
                jump passtime
                return
            "Cancel" if True:
                jump tobackyard
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
