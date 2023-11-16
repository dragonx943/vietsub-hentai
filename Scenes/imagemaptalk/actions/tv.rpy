label tvbase:

    play music papapalapa
    "" "You can watch the TV with two girls, but they must be Step 1 minimum."
    menu:
        "Currently available:"
        "[bn] and [vn]." if bstep > 0 and vstep > 0:
            jump tvbandv
        "[en] and [sn]." if estep > 0 and sstep > 0:
            jump tvsande
        "Cancel." if True:
            jump toliving


label tvbandv:
    scene black
    pause
    scene tvbg with dissolve
    show mc at left
    show berry at right
    mc "Hey [bn]! I was about to watch TV. Wanna watch it together?"
    b "Oooh, So cute! I will be glad to spend time with my candy!"
    pause
    show berry:
        linear 0.5 xalign 0.6
    show valerie at right with dissolve
    pause
    v "Oh hey, hm, excuse me, I just wanted to watch a movie, can I?"
    show berry serious
    b "Miss Valerie..."
    v "Hm, Miss Berry?"
    show berry ordering
    b "I was about to watch TV with MY candy, it's too late for YOU."
    show valerie mad
    v "Really?!"
    mc "Why don't we all watch TV together?"
    b "Hm... why not, what kind of movie did you want to watch?"
    menu:
        "What kind of movie do you want to see?"
        "Horror." if True:
            if vstep == 4:
                "" "Berry + Valerie affection: [bboundv]/24"
                if bboundv > 23:
                    jump berftv
            show berry happy
            b "Oh yes!! That's what I wanted to see!!"
            show valerie surprised
            v "Oh no!!"
            b "Good choice, my candy. As your reward, you could sit against me so you won't be frightened."
            show mc lol
            mc "Actually, I'm not afraid of-"
            show berry ordering
            b "AGAINST. ME."
            show mc shy
            mc "Yes!"
            show berry happy
            b "Great!"
            show valerie shy
            v "Ouah, you're so... Authoritarian, you impress me, Miss Berry."
            b "Thank you, Miss Valerie!"
            scene black with dissolve
            "" "You put on your nighty outfit and then start the movie."
            pause
            scene black with fade
            scene tvberry with dissolve
            play music causmic
            pause
            mc "[bn]!!"
            b "Shhhh, the movie is about to start."
            mc "I'm not sure I'm in the best position right now."
            b "I think you are."
            b "Don't worry, I'll protect you."
            mcth "After all, am I in a position that bad?"
            v "Oh gosh... I could almost be jealous..."
            window hide
            pause
            window auto
            "" "During the movie, You were unable to move, [bn] was completely overwhelming you."
            "" "She wasn't afraid at all, she even spent the movie laughing and sometimes admiring the villains."
            "" "[vn], on the other hand, had a goosebump during the whole film."
            "" "They started to tease each other, and this moment made them get closer to each other."
            scene black with dissolve
            scene expression night("0.1.7/tvbg.webp")
            show mc shy ocalecon at left
            show berry o4:
                xalign 0.6
            show valerie o3 happy at right
            b "What a funny show!"
            v "Well, I'm not sure if funny was the word..."
            v "But, I had a great time with you guys!"
            b "I- I kind of had a great time too."
            mcth "[bn] Still struggles to like [vn], and I won't blame her, but she makes efforts."
            v "Anyway guys, gonna sleep, see you tomorrow!"
            b "Good night."
            mc "Nigh'"
            hide valerie with dissolve
            pause
            mc "Thank you [bn], for trying to get along with [vn]."
            show berry base
            if bstep < 2:
                b "I despise her for what she did to you. You know that."
                b "But I understand what you're trying to do, I agree that if there is a way for us to get along, we could avoid many troubles for everyone."
                b "I won't forgive her, though."
                mc "Yeah, me either."
                call incrdesire ("Berry", 2) from _call_incrdesire_3
            elif bstep > 1:
                b "Where do you think you're going?"
                mc "Me? I don't know, I though-"
                b "You looked so scared during this movie!"
                mc "Well, not that much, in fact-"
                b "That's because I was here to protect you!"
                b "Don't worry, you're safe with me!"
                b "Let me help you to relax now."
                scene black with dissolve
                pause 1.0

                window hide
                stop music
                scene black
                play sex bdtyandere05loop
                $ persistent.replay34 = True
                show 02bjtv
                pause
                window auto
                mc "Aaaah, [bn]!"
                b "*glock* *glock*"
                mc "Your throat, I can't!"
                mc "How am I supposed to resist?!"
                mc "Oh [bn], you're caring for me so well!"
                mc "You can make me cum so easily, I- haaaaaaaaaah!"

                window hide
                hide 02bjtv
                stop sexfx
                stop sex
                play audio bcuminmouth
                play audio ecuminmouth
                play audio cumexplo
                play audio cumsound
                show 02bjtvcum at cumtr
                show cumanim
                pause
                window auto
                $ cumbyb += 1
                mc "Oh my lord..."
                b "*glouh* *glouh*"
                b "Mmmmmh..."
                mcth "[bn]'s throat makes me cum so fast, and she knows that..."
                mcth "She loves that..."
                mcth "I feel so empty of energy... and relaxed."
                call incrskill ("cockskill", 2) from _call_incrskill_5
                call incrdesire ("Berry", cockskill) from _call_incrdesire_4
                pause
        "Erotic" if True:

            if vstep == 4:
                "" "Berry + Valerie affection: [bboundv]/24"
                if bboundv > 23:
                    jump valftv
            show valerie happy
            v "Yeeeeah! That's what I wanted!"
            show berry shy
            b "Rhooo!"
            show berry base
            b "I guess that's fair, I hope next time it will be a horror movie!"
            v "As the winner, I want [mc] to be next to me!"
            show mc surprised
            mc "Me?!"
            show berry serious
            b "Why? Grr!"
            v "Don't worry, Miss Berry, I won't break him, I'm just used to having someone next to me, that's all."
            show mc base
            mc "Er... okay..."
            scene black with dissolve
            "" "You put on your nighty outfit and then start the movie."
            pause
            scene black with fade
            scene valtv with dissolve
            play music causmic
            pause
            "[mc]'s whispers" "[vn]?!! What are you doing?!"
            v "Quiet! Or [bn] will notice!"
            v "I told you I used to watch this kind of movie with someone next to me!"
            v "Don't react and just watch."
            window hide
            pause
            window auto
            "" "During the movie, [vn] continued to play with your crotch slowly."
            "" "She enjoyed the movie, and your fingers are completely wet."
            "" "[bn] wasn't that in it, seems like the main character did not suit her tastes."
            scene black with dissolve
            scene expression night("0.1.7/tvbg.webp")
            show mc shy ocalecon at left
            show berry o4:
                xalign 0.6
            show valerie o3 happy at right
            v "What a good show!"
            b "Yeah, I'm just sad that this girl was always waiting for the man to make the first move."
            b "I enjoyed that moment with you two, though!"
            v "Me too! I hope we can do that again!"
            b "Going back to my room to sleep, good night!"
            v "Good night Miss Berry!"
            b "Good night [mc]!"
            hide berry with dissolve
            pause
            show mc shy
            mc "Are you crazy?!"
            v "You kind of look cute when you're embarrassed hehe!"
            v "Don't panic. She did not notice."
            v "Thank you, though, I had a good time."

            if vstep == 1:
                call incrdesire ("Valerie", 1) from _call_incrdesire_5
                v "Good night [mc]."
                show mc base
                mc "nigh'"
            elif vstep >1:
                $ persistent.replay75 = True
                call valtvpj from _call_valtvpj


    scene black with dissolve
    if bboundv + 5 < bboundvmax:
        $ bboundv += 5
    jump passtime
    return

label tvsande:
    scene black
    pause
    scene tvbg with dissolve
    show mc at left
    show sarena at right
    mc "Hey [sn]! I was about to watch TV, wanna watch it together?"
    s "Suuuure!"
    pause
    show sarena:
        linear 0.5 xalign 0.6
    show emma at right with dissolve
    pause
    e "Hey!"
    e "Could you step aside? I wanna watch TV before sleeping."
    show sarena happy
    s "Oh so good! [mc] and I was about to do that! Wanna join?"
    e "It depends, what do you want to look at?"
    menu:
        "What do you want to look at?"
        "Horror" if True:
            if estep == 4:
                "" "Emma + Sarena affection: [sbounde]/24"
                if sbounde > 23:
                    jump emmtvf
            show emma smirk
            e "Oooh that's what I wanted! Okay so I'm with you guys."
            show sarena shocked
            s "Oh nooo I wanted an erotic movie..."
            show sarena base
            s "I can't help it, I'm on it as well, let's have fun together!"
            scene black with dissolve
            "" "You put on your nighty outfit and then start the movie."
            pause
            scene black with fade
            scene emmatv with dissolve
            play music causmic
            pause
            mc "[en]?!! What are you doing?!"
            e "Shut up!!"
            e "Just be a man and- Kiiiaaaaa this is so frightening!"
            mcth "[en] looks so cute, looking for my protection!"
            mcth "I can feel her whole body on my arm, her hands, her cheek, her breast, even her... spot..."
            window hide
            pause
            window auto
            "" "During the movie, [en] never let go of your arm. She felt safe with you."
            "" "She still released a few moans when your hand reacted to the screamers."
            "" "[sn] wasn't intimidated, she said she could handle the murderer with her fists whenever she wanted."
            scene black with dissolve
            scene expression night("0.1.7/tvbg.webp")
            show mc ocalecon at left
            show emma shy o3:
                xalign 0.6
            show sarena o4 at right
            e "This show was sooo terrifying!"
            s "I guess you were happy to have [mc] by your side haha!"
            show emma angryshy at angryjump
            e "[mc]?! Not at all!!!"
            show sarena taunt
            s "Hehe so cute reaction!"
            s "Anyways, going back to sleep, have a goodnight!"
            mc "Good night [sn]!"
            show emma base
            e "See you tomorrow."
            hide sarena with dissolve
            if estep <2:

                pause
                show emma embarrassed
                e "Just because I grabbed your arm doesn't means..."
                show mc lol
                mc "I know, I know."
                e "Great, now I'm going to sleep. Good night."
                mc "Good night [en], I had a great time with you."
                e "Yes, me too."

                call incrdesire ("Emma", 2) from _call_incrdesire_6
                hide emma with dissolve
            elif estep == 2:
                mc "Wait a minute."
                show emma shy
                e "Yes?"
                mc "You knew what you were doing by holding my arm between your thighs, right?"
                show emma tsun
                e "I don't know what you're talking about, [mc]."
                mc "Oh I think you are!"
                mc "If you want it, then just ask for it!"
                e "If I want what?"
            elif estep >2:
                e "Oh [mc], your hand made me so horny!"
                e "Please..."
            show mc lol
            pause
            play sex emoans3
            play sexfx frottements
            window hide
            scene 023m with dissolve
            pause
            window auto
            e "[mc]!"
            mc "You're so wet, [en]."
            e "I knooow!!"
            e "You're doing this to me sooo good!!"
            mc "So say it, you were waiting for this during the movie."
            e "No!"
            mc "A good girl doesn't lie."
            e "Haaa!"
            e "I was waiting for you to touch me all day long!!"
            mc "Good."
            mcth "Oh my god, I love to make her moan so much!!"
            mc "Now, your reward."
            window hide
            show 023m2
            show cumanim
            stop sex
            stop sexfx
            play audio ecum3

            $ ecum+=1

            pause
            window auto
            e "You're the only one that knows my body so well!!!"
            e "I'm all yourssssss!!"
            scene expression night("0.1.7/tvbg.webp") with fade
            show mc lol ocalecon at left
            show emma shy o3:
                xalign 0.6
            pause
            if estep == 2:
                e "You know that I didn't mean it!"
            if estep >2:
                e "You know my body so well..."
            mc "I know, I know."
            e "Great. Now, good night."
            mc "Have nice dreams thinking of me haha!"
            call incrskill ("handskill", 3) from _call_incrskill_6
            call incrdesire ("Emma", handskill) from _call_incrdesire_7
            if estep == 2:
                show emma angryshy
                e "shut up!"
            hide emma with dissolve
            pause
        "Erotic" if True:


            if sstep == 4:
                "" "Emma + Sarena affection: [sbounde]/24"
                if sbounde > 23:
                    jump sartvf
            show sarena taunt
            s "Yeeeeah, That's my boy!"
            show emma shy
            e "Erotic?! [mc], you're a perveeeeert!"
            s "What's going on, [en]? Are you too young for these kinds of things?"
            show emma angryshy
            e "Hell no! I'm a grown woman! I'm taking part in your TV night!"
            s "That was so easy hehehe!"
            scene black with dissolve
            "" "You put on your nighty outfit and then start the movie."
            pause
            scene black with fade
            scene sarenatv with dissolve
            play music causmic
            pause
            mc "[sn]?!! What are you doing?!"
            s "What do you mean? I always sit on you, that's how it is."
            mc "Yes, but, I mean, considering our clothes..."
            s "That's not a problem to me, stop complaining, the movie is about to start!"
            mcth "How am I supposed to stay calm?! We are about to watch an erotic show with [sn] on my cock!"
            e "Seriously, you two..."
            e "Your relationship is bizarre..."
            s "Our relationship is unique! He's good with that, don't worry."
            e "..."
            window hide
            pause
            window auto
            "" "During the movie, [sn] was slowly rubbing her crotch against yours."
            "" "She enjoyed the show and felt very comfortable in her seat."
            "" "[en] also enjoyed, she stayed silent during hot scenes."
            if sstep < 2:
                scene black with dissolve
                scene expression night("0.1.7/tvbg.webp")
                show mc shy ocalecon at left
                show emma shy o3 at right
                show sarena o4:
                    xalign 0.6
                s "This show was so good! I really am happy for their happy ending!"
                e "Yeah, but it doesn't work like this in real life."
                s "Rhoo don't be so pessimistic!"
                e "Goin' back to sleep, good night."
                mc "Nigh'"
                s "See you tomorrow!"
                e "I had a good time with you guys."
                hide emma with dissolve
                pause
                s "Considering what I felt on my bottom, I guess you also enjoyed the show."
                mc "Stop teasing me! This was because of you! You know, I can't control it, when you're on me!"
                s "Oh, I know."
                pause
                show sarena base
                s "Have fun jerking off, I'm tired, have nice dreams!"
                mc "Have a good night [sn]!"
                s "I loved to spend this moment with you two!"
                call incrdesire ("Sarena", 2) from _call_incrdesire_8
                hide sarena with dissolve
            elif sstep > 1:
                "" "After the movie ends, [sn] was wet like hell."
                "[sn]'s whispers" "[mc]... I'm too horny. I need you to make me cum right now!"
                "[mc]'s whispers" "But [en] is right there!"
                s "Hum, [en]?"
                e "?"
                s "I have to talk with [mc]. Is it okay if you could..."
                e "Oh sure, I'm tired, so it doesn't matter!"
                e "Thank you for this moment, have sweet dreams!"
                window hide
                scene black with dissolve
                pause
                show 018tv
                stop music
                play sex shardmoans1
                play sexfx frottements2
                pause
                window auto
                s "Yeeeeees!!"
                s "You know how to touch me so well!!"
                s "Enh! Play with my nipple!"
                s "My G spot is all yours!!"
                s "Make me cum, [mc]!"
                s "Make me-"
                window hide
                stop sexfx
                stop sex
                hide 018tv
                $ persistent.replay25 = True
                show 018tvcum at cumtr
                show cumanim
                play audio scum1
                pause
                window auto
                s "Yeeaaaaaaaaah!!"
                $ scum +=1
                call incrskill ("handskill", 2) from _call_incrskill_7
                call incrdesire ("Sarena", handskill) from _call_incrdesire_9
                s "How can you make me cum soo haaaard!"

    pause
    scene black with dissolve
    if sbounde + 5 < sboundemax:
        $ sbounde += 5
    jump passtime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
