label cookbase:
    play music sand_castle
    "" "You can cook with two girls, but they must be Step 1 minimum."
    menu:
        "Currently available:"
        "[en]([estep]) and [bn]([bstep])." if estep > 0 and bstep > 0:
            jump cookeb
        "[vn]([vstep]) and [sn]([sstep])." if vstep > 0 and sstep > 0:
            jump cookvs
        "Cancel." if True:
            jump toliving

label cookeb:
    scene black
    pause

    scene cookbg with dissolve
    show mc at left
    show berry at right
    mc "Hey [bn]! Are you up to something?"
    b "I want to prepare something cool for lunch, do you like Burgers?"
    mc "Oh my gosh I love that!"
    show berry:
        linear 0.5 xalign 0.6
    show emma surprised at right with dissolve
    e "Did I hear \"Burgers\"?!"
    b "Hey [en]! Yes, I want to prepare burgers!"
    e "Can I watch?? "
    b "Or you can help me!"
    e "Oooh yes!!"
    show mc lol
    mc "Er, I'm not sure letting [en] prepare food is..."
    show berry ordering
    b "[mc]! You should encourage her instead!"
    show berry base
    show mc shy
    mc "Yes [bn], I'm sorry."
    show emma smirk
    play sound etsah
    e "Hehehe look at this submissive boy!"
    show berry angry
    show mc base
    b "[en]!"
    show emma base
    e "Yes yes, I'm sorry [mc]..."
    show berry happy
    b "I've got an idea, why not make a contest?"
    b "We both prepare burgers and [mc] will judge!"
    show emma shy
    e "Haaah?"
    show mc lol
    mc "Sounds good, so I can show Emma how bad her cooking skills are hehe!"
    show emma angryshy
    e "What did you just saaaaaay?!!!"
    e "I'm gonna show you!!"
    show emma at angryjump
    e "I ACCEPT THE CHALLENGE!"
    window hide
    show kitemmaberry with fade
    pause
    window auto
    "" "[bn] explained to [en] how to make a good burger."
    "" "The seasoning, how to balance the taste, how to manage the texture..."
    "" "[en] is very attentive and even proposes new ideas, she seems to be very interested in cooking."
    "" "After a bit of time, they finished their burgers."
    scene beburgers with fade
    b "That was intense but very pleasant!"
    e "Yes Mom, thank you for teaching me, it was so interesting!"
    b "Hehe I'm glad we got this Mother-Daughter moment!"
    b "Now, time to vote, [mc]!"
    mc "*Scruntch scruntch scrunch*"
    mcth "[en]'s burger is delicious, with different cheeses and a potato pancake that merges perfectly."
    mcth "[bn]'s burger, on the other hand, has a double steak but delicious as well, she added more bacon and a sweet and spicy sauce."

    menu:
        "Who made the best Burger?"
        "[en]" if True:
            if bstep == 4:
                "" "Affection between [bn] and [en] = [bbounde]/24"
                if bbounde > 23:
                    jump cookemmwin
            call incrdesire ("Emma", 2) from _call_incrdesire_126
            scene cookbg with dissolve
            show mc at left
            show berry:
                xalign 0.6
            show emma smirk at right
            e "HAAA, [mc] finally admits that [en] is the best!!"
            b "Rhooo I was so sure you'd prefer mine!"
            b "But it's okay, I'm proud of my daughter."
            b "I'm going back to my stuff."
            hide berry with dissolve
            pause
            e "I'm the best mouahaha!"
            show mc lol
            mc "You're a future good wife indeed."
            if estep < 2:
                show emma angry at angryjump
                e "Shut uuup just because I'm a woman, I should cook?!"
                mc "Well, I'm not sure I could call you a woman yet..."
                show emma angryshy
                e "DIE."
                hide emma with dissolve
            if estep >1:
                show emma shy
                e "Y-you think?"
                mc "Sure! You will make your future husband very happy!"
                e "I hope so..."
                mc "Now it's time for your reward."
                e "My reward?"
                show 019kitchen_00001 with hpunch
                pause
                e "What are you doing?!"
                mc "No panties as usual..."
                e "Oh no! I forgot to put it on!"
                mc "You're not wearing panties these days, is it because you hope for me to exploit it?"
                e "What are you thinking about such a thing?!"
                window hide
                play sex emoans3
                play sexfx frottements
                show 019cookcun
                pause
                window auto
                e "You're crazy!!!"
                e "I swear I just forgot it, it's not because I would want-"
                e "Oh my god!!!"
                e "Why are you so good?!"
                mc "Why are you so delicious?"
                e "Don't say that!!"
                e "Oooh [mc]!!"
                window hide
                hide 019cookcun
                stop sexfx
                stop sex
                play audio ecum2
                $ persistent.replay30 = True
                show 019cookcuncum at cumtr
                show cumanim
                $ ecum += 1
                pause
                window auto
                e "Yeaaaaaaaah!"
                e "[mc] make me cum so hard every time!!"
                scene cookbg with fade
                show mc humidface at left
                show emma tsun at right
                pause
                e "Hehehe!"
                mc "You really enjoy it when I do that to you!"
                if estep ==2:
                    show emma angryshy
                    e "I don't know what you're talking about! I have to go!"
                elif True:
                    show emma tsun
                    e "Yeah, hehehe!"
                hide emma with dissolve
                call incrskill ("tongueskill", 2) from _call_incrskill_125
                call incrdesire ("Emma", tongueskill) from _call_incrdesire_127
                pause 2.0
                jump passtime
        "[bn]" if True:






            if bstep == 4:
                "" "Affection between [bn] and [en] = [bbounde]/24"
                if bbounde > 23:
                    jump cookberwin
            call incrdesire ("Berry", 2) from _call_incrdesire_128
            scene cookbg with dissolve
            show mc at left
            show berry:
                xalign 0.6
            show emma angry at right
            e "You loser! Mine was better, but you chose Mom's because you submitted to her!"
            b "Don't say that honey, I'm experienced, and I know his tastes very well..."
            e "... nyeah... I'll do better next time, you'll see!"
            show emma shy
            e "Anyway, th-thank you Mom, I had a great time with you."
            b "Me as well!"
            hide emma with dissolve
            pause
            b "I'm happy to spend some time with [en], my daughter, but I feel like I haven't been here for her enough when she was younger."
            b "I think I could get closer through cooking, she really seems to appreciate that!"
            show berry tease
            if bstep ==1:
                b "I could reward you, but I have to return to work hehe, see you later!"
                hide berry with dissolve
            elif bstep >1:
                pause
                show berry ordering
                b "Remove your clothes."
                show mc surprised
                mc "What's all of a sudden?!"
                b "You heard what I said."
                b "I'm hungry now. I didn't eat."
                b "What I wanna eat is in your balls."
                stop music
                pause
                $ persistent.replay63 = True
                call berrybjcookanim026 from _call_berrybjcookanim026_2
                mc "Oh my god [bn]!!!"
                mc "You're doing it so intensely!!!"
                mcth "That's crazy!!!"
                mcth "I love to receive blowjobs from [bn]."
                mcth "She can take it so deeply, it's amazing!!"
                mcth "However..."
                mcth "She looks like she enjoys it even more than myself!!"
                mcth "I'm the one supposed to get pleasure from a blowjob!"
                mcth "Look at her lust!!"
                mcth "She's devouring it!!!"
                call berrybjcookanim026 (0.0833) from _call_berrybjcookanim026_3
                mc "Aaaah [bn]!!!"
                mc "You can't grab my balls like this!!!"
                mc "The double pleasure by her throat and hand-"
                mc "Beware, I'm-"
                call berrybjcookanimcum026 from _call_berrybjcookanimcum026_1
                mc "Oh my gooooooood!!!"
                mc "Uh!!"
                mc "Aaah!"
                mcth "My balls are completely emptying into her throat!!"
                mcth "[bn] is the real deal..."
                mcth "I can't resist this woman..."
                $ cumbyb+=1
                call incrskill ("cockskill", 2) from _call_incrskill_126
                call incrdesire ("Berry", cockskill) from _call_incrdesire_129

    pause
    scene black with dissolve
    if bbounde + 5 < bboundemax:
        $ bbounde += 5
    jump passtime
    return

label cookvs:
    scene black
    pause
    if bstep == 4:
        "" "Affection between [vn] and [sn] = [vbounds]/24"
        if vbounds > 23:
            jump cookvalsar
    scene cookbg with dissolve
    show mc at left
    show sarena at right
    mc "Hey [sn]! Are you up to something?"
    s "I wanna prepare something cool for lunch, do you like Maki?"
    mc "Oh my gosh, I love that!"
    show sarena:
        linear 0.5 xalign 0.6
    show valerie surprised at right with dissolve
    v "Did I hear \"Maki\"?!"
    s "[vn]?"
    v "I'm a BIG FAN of that kind of food!"
    s "..."
    s "Do you want to join me?"
    show valerie at angryjump
    v "YES! I didn't dare to ask you!"
    s "Have you made some in the past?"
    show valerie happy
    v "I did, the best you can taste!"
    show sarena challenge
    s "The best? sounds interesting, I think I'm pretty good too!"
    v "Oh really? How about a friendly challenge?"
    s "I never refuse any challenge!"
    s "[mc], you'll be the judge!"
    v "Him?"
    s "Yes, but please be impartial, I don't want to win just because we're close, I'll show her who's the boss here!"
    v "Oh, don't underestimate me, young girl, let's go!"
    window hide
    show kitvalsar with fade
    pause
    window auto
    "" "[sn] and [vn] were not in a dirty competitive mood."
    "" "Instead, they were collaborative, giving each other some tricks from their own experience."
    scene vssushis with fade
    s "Fiou, we made it!"
    v "That was hard, but it looks so damn good!"
    v "[sn] is more talented than I expected!"
    s "And I did not suspect you of having some knowledge in that!"
    s "Now, time to vote, [mc]!"
    mc "*Scruntch scruntch scrunch*"
    mcth "[sn] has prepared I think it's called Philadelphia makis, with the soft and salty salmon surrounding the rice. She prepared it really well!"
    mcth "Valerie made a few makis, I think it's called california rolls with crispy onions, delicious."
    menu:
        "Who did the best maki?"
        "[sn]" if True:
            scene cookbg with dissolve
            call incrdesire ("Sarena", 2) from _call_incrdesire_130
            show mc at left
            show sarena:
                xalign 0.6
            show valerie happy at right
            s "I woooon! I'm da best!"
            v "Well played [sn], I'm not surprised, you are talented!"
            s "[vn] is more fair play than I expected, you were also not that bad!"
            v "I have to study more to beat you next time!"
            hide valerie with dissolve
            pause
            if sstep <2:
                show sarena shy
                s "Er, [mc]? I hope you're not mad that I had fun with [vn], if you want I can stop-"
                mc "That's all good. Yes, I know, and you know what she did, but I think if we can move on, it's good."
                mcth "I'll take my revenge by myself considering how things go with [vn], but I prefer [sn] to have a good time if she can."
            elif sstep > 1:
                show sarena taunt
                s "So, what did you prepare for me?"
                show mc surprised
                mc "Ah?! I didn't cook I thought it was for me only!"
                s "Ooh I'm so mad!"
                show sarena:
                    linear 2.0 xalign 0.35
                s "You're lucky to have a meal always ready for me then!"
                mc "Shhh-! [vn] Is not far away, she'll hear you!"
                s "Is my pony refusing me his cock?"
                s "Rejection refused!"
                window hide
                stop music
                scene 021cookbg:
                    yalign 0.5
                    xalign 0.5
                play sex sbjhard
                $ persistent.replay40 = True
                play sexfx frottements2
                show 021cook
                window auto
                mc "Oh my god [sn]!"
                mc "You're crazy this is too intense!!"
                s "What did you think?!"
                s "I want my daily cum and I'm taking it whenever I want!"
                mc "Oh!"
                s "Repeat!"
                mc "You can take my cum whenever you want, [sn]!"
                s "Great!"
                s "Now give it to me!"
                s "Give me your semen!"
                mc "Ahhh!!"
                $ cumbys +=1
                window hide
                hide 021cook
                stop sex
                stop sexfx
                play audio sbjcum
                play audio cumexplo
                play audio cumsound
                show 021cookcuma
                show 021cookcumb
                show cumanim
                pause
                window auto
                s "Hm... so tasty..."
                s "I could never forget this feeling of making you cum..."
                call incrskill ("cockskill", 2) from _call_incrskill_127
                call incrdesire ("Sarena", cockskill) from _call_incrdesire_131
        "[vn]" if True:
            scene cookbg with dissolve
            call incrdesire ("Valerie", 2) from _call_incrdesire_132
            show mc at left
            show sarena:
                xalign 0.6
            show valerie happy at right
            v "Hoooh, so he really was impartial and voted for me, how unexpected!"
            v "But honestly, [sn] could've won, she is very talented!"
            s "Thank you [vn]!"
            s "Don't worry I'll train and beat you next time!"
            hide sarena with dissolve
            pause
            if vstep <2:
                mc "I didn't expect you to be so talented."
                v "Hooo? I've got much more talents, but not for you, sadly hehe!"
            elif vstep > 1:
                jump valcuncook
                return

    pause
    scene black with dissolve
    if vbounds + 5 < vboundsmax:
        $ vbounds += 5
    jump passtime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
