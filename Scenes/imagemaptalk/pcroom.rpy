

screen pcroom:
    imagemap:
        ground "House/pcroom/bg pcroom.webp"
        if epos == "pcroom" and daytimenumber ==2:
            if estep < 2:
                imagebutton:
                    align (0.5, 1.0)
                    idle "House/pcroom/pce1.webp"
                    hover lumi("House/pcroom/pce1.webp")

                    action Jump("emmagpcroom")
            else:
                imagebutton:
                    align (0.5, 1.0)
                    idle "0.1.9/emma_on_pc2.webp"
                    hover lumi("0.1.9/emma_on_pc2.webp")

                    action Jump("emmagpcroom")
        else:
            imagebutton:
                align (0.5, 1.0)
                idle "House/pcroom/chaisepcroom.webp"
                hover lumi("House/pcroom/chaisepcroom.webp")

                action Jump("bosserstats")
label emmapresence:
    scene bg pcroom
    show pce1
    mcth "!!!"
    mcth "What a perfect shot..."
    mcth "Look like my [esn] is wearing thongs while working... such a naughty girl."
    mcth "I want to spank her so bad!"
    $ firstlookonemma = True
    jump topcroom

label bosserstats:
    scene 02devb5
    if blogstarted == False:
        "" "You can use the computer to earn money, or to enhance your statistics"
        "" "Your character has three main statistics that can be increased by studying it or by practicing during events."
        "" "The higher the statistics, the higher you can increase a girl's desire."
    menu:
        "What do you want to do on the computer?"
        "{color=#ff9a40}Learn how to take photos.{/color}" if elv == 4:
            jump devep5
        "{color=#ff9a40}Look for fake sperm for [vn].{/color}" if vlv == 3:
            jump devvp4
        "Find a way to start earning money." if blogstarted == False:
            jump creatblog
        "Actualize your blog. (Pass the time)" if blogstarted == True:
            $ levelregistered = bloglv()
            "" "You write your current progression on your blog."
            "" "Your daily income has been actualized to [levelregistered]$"
            jump passtime
        "Exercice your skills." if True:
            menu:
                "Search about how to please a woman with your tongue." if True:
                    "" "After a few hours of working, you've found some interesting tips on how to use your tongue with girls."
                    call incrskill ("tongueskill", 2) from _call_incrskill_71
                    $ write ("Tongue skill increased by [skillrankincr2]!")
                    pause
                    jump passtime
                "Search about how to please a woman with your hands." if True:

                    "" "After a few hours of working, you've found some interesting tips on how to use your hands with girls."
                    call incrskill ("handskill", 2) from _call_incrskill_72
                    $ write ("Hand skill increased by [skillrankincr2]!")
                    pause
                    jump passtime
                "Search about how to please a woman with your cock." if True:

                    "" "After a few hours of working, you've found some interesting tips on how to use your cock with girls."
                    call incrskill ("cockskill", 2) from _call_incrskill_73
                    $ write ("Cock skill increased by [skillrankincr2]!")
                    pause
                    jump passtime
                "Cancel" if True:
                    jump topcroom
        "Order online." if True:
            call screen shoptab with dissolve
            return
        "Read the latest feedback about girl's content." if True:

            menu:
                "Which girl do you want to see her feedback?"
                "Sarena" if True:
                    menu:
                        "Which content?"
                        "You haven't made any content with [sn] yet." if slv <4:
                            jump topcroom
                        "First video with [sn] (Throat hit)" if slv > 3:

                            "fox95" "The new assistant looks pretty hot! I wouldn't mind getting him as assistant as well..."

                            "SlaveMe" "Totally my type!"

                            "Michella" "I bet they are, in fact, in a couple!! I want a couple-work-out video!"
                            jump topcroom
                        "[sn]'s abs video." if slv > 5:

                            "fox95" "[mc] looks really built to be able to do that! Amazing video!"

                            "SlaveMe" "This looked so sexual! I want a boyfriend right now to do the same thing."

                            "Michella" "That cut in the middle of the exercise was suspect..."
                            jump topcroom
                        "[sn]'s self defense 2 (Kick balls)." if slv > 8:

                            "fox95" "Poor [mc] he is so badly treated, haha! I love both of you!"

                            "SlaveMe" "It would have been fun if she massaged his balls! They're both so hot..."

                            "Michella" "Hm... Honestly, It didn't look like she did it by accident..."
                            jump topcroom
                        "[sn]'s sports in-room video." if slv > 9:

                            "fox95" "Perfect! I needed this since I can't do sport with my family beside me..."

                            "SlaveMe" "I'm disappointed. I was hoping for something else, in her \"room\"..."

                            "Michella" "Imagine being in a room alone with [sn]. I'm sure [mc] thought of something naughty!"
                            jump topcroom
                        "[sn]'s porn video with you." if sstep > 2:

                            "fox95" "I KNEW they would end up together! My dream comes true!"

                            "SlaveMe" "I'm so happy someone uploaded their porn video. I fapped so hard on it!"

                            "Michella" "Oh gosh she looks so savage on his cock! I want to see MORE, MOOOOOOORE"
                            jump topcroom
                "Berry" if True:
                    menu:
                        "Which content?"
                        "You haven't made any content with [bn] yet." if blv <6:
                            jump topcroom
                        "Berry's cosplay as tsunade photoshoot." if blv > 5:

                            "Naruto69" "Oh my goooood! Her body type fits the character so well. She looks GORGEOUS!"

                            "Bee Gkok" "Holy shit is that tits' size even possible?! I SIMP FOR HER!"

                            "Angeloflust" "Guyz, I've waited for a milf to do cosplays like this for so long!!!!"
                            jump topcroom
                        "Berry's cosplay as Dimitrescu." if blv > 8:

                            "Naruto69" "It fits so well to her! But she is a sweet mommy I don't see her as a dom."

                            "Bee Gkok" "That crotch grab omfg! This guy is so lucky! I hope they fucked."

                            "Angeloflust" "Wait, who is this guy? He looks much younger! And look at this bulge! He probably has a massive cock!"
                            jump topcroom
                "Emma" if True:



                    menu:
                        "Which content?"
                        "You haven't made any content with [en] yet." if elv <3:
                            jump topcroom
                        "Your appearance during her live. (Chat replay)" if elv > 2:

                            "Tonia975" "You look so good together! I hope we'll see him again!"

                            "AmandineOf38" "I bet he was looking for his daily head!"

                            "Skelettor" "Did you all realize he could see EVERYTHING from behind?!"
                            jump topcroom
                        "Her first photo from you" if elv > 5:

                            "Tonia975" "Oh ouaw, I wonder what is happening to her hehehe"

                            "AmandineOf38" "WTF? She is riding some dildo! This idea was AMAZING!"

                            "Skelettor" "This is so lewd! You should open an Hornyfan I'm sure you'll earn plenty of money!"
                            jump topcroom
                        "Her second photo from you" if elv > 7:

                            "Tonia975" "She looks like a pornstar, lol! But I like it."

                            "AmandineOf38" "Oh gosh why don't we see what makes her in that state? I want to see the sex toy in her!"

                            "Skelettor" "Great! But I'd expect more for a Hornyfan... like... more nudity?"
                            jump topcroom
                        "Her second photo from you" if elv > 9:

                            "Tonia975" "Poor of her... her stomach hurt so bad!"

                            "AmandineOf38" "Are you fucking with me? She looked like she had an orgasm lol"

                            "Skelettor" "Hm... I loved to imagine someone licking her pussy in reality..."
                            jump topcroom
                "Valerie" if True:
                    menu:
                        "Which content?"
                        "You haven't made any content with [vn] yet." if vlv <3:
                            jump topcroom
                        "Your appearance during her live." if vlv > 2:

                            "Tonia975" "They live together? He is better looking than the older guy."

                            "AmandineOf38" "It smells hardcore sex tension between them."

                            "Skelettor" "Has she left her old man for him? I won't complain."
                            jump topcroom
                        "[vn] using your \"fake cum\"." if vlv > 4:

                            "Tonia975" "Good quality content, you've found an excellent asset!"

                            "AmandineOf38" "She won't get me, it's true sperm lol, I bet she pumped the younger guy!"

                            "Skelettor" "If this is real sperm, why doesn't she take it from the source instead of a toy?"
                            jump topcroom
                        "[vn] Sucking Dildo." if vlv > 9:

                            "Tonia975" "Great cock's model!"

                            "AmandineOf38" "She isn't as skilled as expected. I was hoping for a DT so bad :("

                            "Skelettor" "I think she needs someone to push the back of her head."
                            jump topcroom
                        "[vn] Glory Hole." if vlv > 13:

                            "Tonia975" "Oh my gosh, this dildo looked so realistic!"

                            "AmandineOf38" "Ah, you dumb?! It clearly was a real dick!!"

                            "Skelettor" "I agree, it's a real cock. The question is... Who was that lucky guy?"
                            jump topcroom
                        "Twerk" if vlv > 18:

                            "Tonia975" "I love how we can clearly see they want to fuck each other!"

                            "AmandineOf38" "She looks so frustrated!!! I want to see her unleashed haha!"

                            "Skelettor" "Wait, how is it possible to resist that woman?"
                            jump topcroom
                        "First sex" if vstep > 2:

                            "Tonia975" "She looked like she was falling in love with his dick!"

                            "AmandineOf38" "Lucky girl, I wish I got a boyfriend with a cock like that..."

                            "Skelettor" "That Cuckhold was legendary!"
                            jump topcroom
                "Quit" if True:


                    jump topcroom
        "Step back." if True:
            jump topcroom


label emmagpcroom:
    scene bg pcroom
    if estep <2:
        show pce1
    elif True:
        show emma_on_pc2
    menu:
        "What to do?"
        "Talk" if True:
            jump talke
        "{color=#ff9a40}Join her while she streams.{/color}" if elv == 2 and edesire >= desireforstep1:
            jump devep3
        "Look at her." if True:
            jump emmpcstep0
        "Fingerjob while she's streaming" if estep > 0:
            scene e2
            mc "Hey chat! How are you?"
            if estep <3:
                e "You again? Erh, ignore him."
            elif True:
                e "Oh, [mc] is there!"
            pause
            mc "Look at that. They all are welcoming me!"
            if estep <3:
                e "You're such annoying."
                e "Rha calm down chat. I'm not harsh with him. It's just normal talk between us."
            elif True:
                e "Yeah, they know you always do interesting things."
            if estep < 2:
                scene e1
            elif True:
                scene e1b
                mcth "Look at this..."
                if estep <3:
                    mcth "\"Normal talk between us.\""
                    mcth "It's time to take my revenge!"
            if estep < 2:
                mcth "She completely knows I can see her thong but stay as she is."
            elif True:
                mcth "I bet she isn't wearing any panties because she knew I'd come."
                mcth "Such a naughty girl..."
                mcth "It's time to give her what she deserves!"
            if estep < 2:
                show e1a:
                    xalign 0.5
                show e1a at angryjump
            elif True:
                show e1c:
                    xalign 0.5
                show e1c at angryjump

            play sound emoansingle
            e "Huuun!"
            pause
            e "Ha? No, don't worry, chat that was... nothing..."
            mcth "Gosh, she's already so wet!!"
            mcth "I'm starting to love doing that!"
            mcth "She doesn't even try to push me away!"
            e "Huuun!"
            e "Eh? No, I'm just..."
            e "Listen chat, my belly hurts. I need a minute break."
            scene bg pcroom
            show mc at left
            show emma angryshy at right
            pause
            e "What are you doing?!"
            mc "Me? Nothing."
            e "Grrrmblrrr~"
            e "You're lucky no one noticed!!"
            mc "So the first thought that comes to your mind is the chat noticing it, and not me doing this to you?"
            show emma shy
            e "Ah-heuh~"
            if estep <3:
                show emma angryshy at angryjump
                e "GET OUT!"
            elif True:
                show emma tsun
                e "Don't do that while I'm live..."
            mc "Haha!"
            call incrskill ("handskill", 1) from _call_incrskill_74
            call incrdesire ("Emma", handskill) from _call_incrdesire_68
            jump passtime
        "{color=#c1803a}Lick her pussy in secret.{/color}" if estep > 1:
            mcth "Look at her! She is not wearing any panties!!"
            mcth "Great lord she looks delicious..."
            mcth "I can't. She's streaming!"
            mcth "Can I?"
            mcth "I just have not to be seen."
            scene 019cunspc with fade
            play sexfx frottements
            play sex emoans1
            pause
            e "That's so g-"
            e "Er, don't worr-rry chat, I just-"
            e "My stomach hurts!"
            e "Yeah, yeah, I can't move right now, it-"
            e "Oh my-"
            show 019cunspc at cumtr
            show cumanim
            $ ecum +=1
            stop sexfx
            stop sex
            play audio ecum2
            pause
            e "Oh my god..."
            e "It's okay Guys... I think I feel better..."
            e "Damned stomach, yeah..."
            scene black with dissolve
            "" "After she breaks the stream."
            scene bg pcroom
            show mc lol humidface at left
            if estep <3:
                show emma angryshy at right
                e "How dare you to do that to me during the stream!!!"
            elif True:
                show emma tsun at right
                e "[mc]!!!"
            e "Imagine if someone saw you?!"
            mc "Are you saying if no one saw me, then there is no problem?"
            show emma shy
            e "It's not what I-"
            if estep <3:
                show emma angryshy at angryjump
            elif True:
                show emma tsun
            e "Get out!!"
            call incrskill ("tongueskill", 3) from _call_incrskill_75
            call incrdesire ("Emma", tongueskill) from _call_incrdesire_69
            jump passtime
        "{color=#c13a3a}Let her be aware of your presence.{/color}" if estep >2:
            $ persistent.replay87 = True
            jump evemmsexpcroom




label creatblog:

    show mc at center
    mc "All the girls are preparing their work for the confinement."
    mc "I also have to make my own money!"
    show mc surprised
    mc "I've got no idea of how to make it..."
    show mc base
    mc "What do I have?"
    mc "I'm bad at games."
    mc "I'm good at sport but only because [ssn] tells me what to do."
    show mc facetel
    mc "It seems I've got a big cock. Hearing what girls said, should I do an OnlyLust?"
    show mc pleasure
    mc "Imagine all these women worshipping me..."
    show mc base
    mc "Eh, well, I'm not sure it'll work in this direction..."
    show mc surprised
    mc "Plus, I'll feel so shy and intimidated..."
    show mc base
    mc "..."
    mc "Maybe I should ask girls?"
    mc "Girls... Girls..."
    mc "This is it, this is my particularity!"
    mc "I'm living in a house full of gorgeous ladies!"
    mc "Why not write, like, a blog?"
    mc "I would share my adventures in this house!"
    mc "And maybe put 1 or 2 ads here and here, haha!"
    mc "Of course, I have to keep girls' integrities, so I'll just use pseudonyms."
    mc "Yeah, It should work like this."
    scene black with fade
    "" "After a few hours, Your blog is ready and online!"
    "" "The problem is that you've got nothing to tell except your current situation and few descriptions of everyone."
    "" "You even found a donation widget!"
    scene bg pcroom
    show mc at center
    mc "Pfious! That should work."
    "" "*cling*"
    mc "Oh damn, already a comment!!"
    mc "\"Oh man, you're so lucky! I can't wait to read where it's going! I hope you'll fuck'em all!\""
    mc "Fuck them all? Ah, I guess he ignored that we all have companions already."
    $ blogstarted = True
    jump passtime
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
