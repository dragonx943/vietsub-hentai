label talkb:
    scene berryroom talk
    play sound bhello
    show mc at left
    show berry at right
    b "Hi!"
    menu:
        "Stare at her breasts." if True:
            jump berroomstep0
        "{color=#ff9a40}Ask her how things are going.{/color} Orange color = Quest" if qpreptalkb == False:
            jump bpreptaff
        "{color=#ff9a40}Give her the Tsounade outfit.{/color}" if blv == 5 and Tsounade in inventory.items:
            jump devbp6
        "Wait for an interesting moment to peek. (Level 1)" if bstep == 1:
            jump peekfaceass
        "Wait for an interesting moment to peek. (Level 2)" if bstep > 1:
            jump peekfaceass
        "{color=#ff9a40}\"I contacted Isabelle, and you've got a video meeting with her.\"{/color}" if blv == 11:
            jump devbp12
        "\" Can I help you with your next photo shooting?\"" if bstep >2:
            jump bworksex
        "Quit" if True:
            jump toberryroom

label bpreptaff:
    $ qpreptalkb = True
    b "Hello!"
    mc "Hey [bn], how's it going?"
    b "My Candy wants to know if I'm okay. How cute!"
    b "Right now, I'm setting up my camera for my new activity!"
    mc "Your new... activity..?"
    b "Yes. I wanna be a cosplayer!"
    mc "Cosplayer?!"
    b "What? You think I'm too old for that type of thing?"
    mc "No-uh-I mean, I'm just surprised. I didn't know that would be your thing."
    b "I'm teasing you! Haha. It seems like only younger people are online doing cosplay. I want to stand out as a {b}milf {/b}cosplayer!"
    b "I'll show those girls. A woman of my age can also be successful!"
    mcth "Indeed. Considering her incredible body, if she does cosplay, she will set the internet on fire..."
    mc "I wish you luck, even though you don't need it. There's no way you'll go unnoticed."
    b "Hehe. You're so cute!"
    b "*Kisses your forehead*"
    if qpreptalkv == True and qpreptalkb == True and qpreptalke == True and qpreptalks == True:
        $ qpreptalk = True
        pause 1.0
    jump talkb

label peekfaceass:
    scene black with fade
    "" "After a few minutes, [bn] is wearing underwear only. It's showtime!"
    play music causmic
    show berryspy1 with fade:
        yalign 1.0
    show berryspy1:
        linear 2.0 yalign 0.95
        linear 2.0 yalign 1.0
        repeat
    mcth "I'll never get tired of seeing [bn] 's butt..."
    mcth "I wonder if she'll punish me again if she-"
    stop music
    show berryspy1:
        linear 1.0 yalign 0.0
    pause
    play music papapalapa
    b "Well, well, well... What do we have here?"
    mc "It's- it's not what you think!"
    b "Ah? I think you were peeking at me once again."
    play sound bnaughtyboy
    b "You're such a naughty boy!"
    b "Come here for your punishment!"
    if bstep < 2:
        $ persistent.replay11 = True
        scene 015assfacebgmc with dissolve
        mc "Y-yes, [bn]."
        b "Now I'm gonna punish you properly."
        show 015assrubb
        play sex bmoans1
        play sexfx frottements
        window hide
        pause
        window auto
        mc "Mmmmh!"
        b "Haawh!"
        b "You like being punished, don't you?"
        mc "Hmmh!"
        b "Yeah, I knew it!"
        b "Haaawh, your cute little face is completely crushed by my butt!!"
        b "I want to punish you even MORE!"
        b "Oh no, I will hurt you if I continue!!"
        scene black with dissolve
        stop sex
        stop sexfx
        pause 0.5
        scene berryroom talk
        show mc o1b shy humidface at left
        show berry o6 lewd2 at right
        pause
        b "I'm sorry [mc], I almost lost control!"
        mc "Th-that's okay. I deserve the punishment."
        show berry lewd
        b "Y-yes. You deserved it."
        b "But don't hesitate to warn me if I go too far."
        mc "Okay."
        call incrskill ("tongueskill", 1) from _call_incrskill_119
        call incrdesire ("Berry", tongueskill) from _call_incrdesire_117
    elif bstep ==2 or bstep ==3 or bstep ==4:
        $ persistent.replay64 = True
        b "On the floor."
        b "And I want you to keep your arm behind your back."
        b "I don't want you to move while I give you your lesson."
        mc "Yes, [bn], I'm ready for my lesson!!!!"
        pause
        stop music
        call berryworkfacesitting026 from _call_berryworkfacesitting026_2
        b "Oh yeah!!!"
        b "Today's lesson!"
        b "Gnh!"
        b "When you make [bn] upset, gnh, you'll have to let her play with you!"
        b "All you deserve is [bn] 's pussy on your face!!"
        b "You naughty boy!"
        b "I have to teach you!!"
        b "Oh my gosh, your mouth feels so good!"
        call berryworkfacesitting026 (0.05) from _call_berryworkfacesitting026_3
        b "You won't get away with that!!"
        b "You're my butt's property!"
        call berryworkfacesittingcum026 from _call_berryworkfacesittingcum026_1
        b "Aaaaaaaah!!!"
        b "I'm cumming!"
        b "I'm cumming on [mc] 's face!!!"
        b "My good boy!!!!"
        $ bcum+=1
        call incrskill ("tongueskill", 3) from _call_incrskill_120
        call incrdesire ("Berry", tongueskill) from _call_incrdesire_118
        pause

    jump passtime


    return
label bworksex:
    b "My candy is so cuuuute! Of course, you can!"
    b "However, there is a new rule!"
    mc "That is?"
    pause
    scene bdev3d with fade
    pause
    mc "Er... Are you sure this is required?"
    b "It is!"
    b "You have to be naked to take photos!"
    mc "What's the logic?"
    b "That way, I can see with my own eyes if my posing is good!"
    mc "..."
    scene black with fade
    "" "After the photoshoot..."
    pause
    mc "[bn]?!"
    mc "Wh-what are you doing?!"
    b "Don't move!!"
    stop music
    call bworksexa027 (1.0/8) from _call_bworksexa027_2
    b "You thought I'd let you go with a boner like that?"
    b "Hahaha!"
    b "That cock of yours is MINE!"
    b "Any time it gets hard, I have to fuck it, like I'm doing right now!"
    call bworksexa027 (1.0/16) from _call_bworksexa027_3
    mc "Oh [bn]!!"
    b "Come on [mc]!"
    b "Cum for me!!"
    b "I want to see your face flooded with pleasure!"
    call bworksexacum027 from _call_bworksexacum027_1
    mc "I'm cumming, [bn]!!"
    b "Yeessssss!"
    call bworksexbcum027 from _call_bworksexbcum027_1
    b "I'm cumming as well!!"
    b "I'm so in love with your facial expression when you cum!!!"
    pause
    scene bdev3f with dissolve
    b "Look, over here."
    b "You're still so full of cum, haha! It's incredible."
    pause
    $ bcum+=1
    $ cumbyb +=1
    call incrskill ("cockskill", 3) from _call_incrskill_121
    call incrdesire ("Berry", cockskill) from _call_incrdesire_119
    pause
    $ persistent.replay68 = True
    jump passtime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
