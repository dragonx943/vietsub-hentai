screen kitchen:

    imagemap:
        ground ifnight("House/kitchen/bg kitchen.webp")

        if bpos == "kitchen":
            imagebutton:
                idle "House/kitchen/kitchen berry.webp"
                hover lumi("House/kitchen/kitchen berry.webp")
                focus_mask True
                action Jump("kitb")
        if vpos == "kitchen":
            imagebutton:
                idle "House/kitchen/kitchenval.webp"
                hover lumi("House/kitchen/kitchenval.webp")
                focus_mask True
                action Jump("kitv")
        if epos == "kitchen":
            imagebutton:
                idle ifnight("House/kitchen/kitchene.webp")
                hover lumi("House/kitchen/kitchene.webp")
                focus_mask True
                action Jump("kite")
        if daytimenumber == 0:
            if bstep > 0 or sstep > 0 or estep > 0 or vstep > 0:
                imagebutton:
                    idle "House/kitchen/cookwith.webp"
                    hover lumi("House/kitchen/cookwith.webp")
                    focus_mask True
                    action Jump("cookbase")
label cookwith:
    "" "This feature is ready to be used on the next update."
    jump tokitchen

label kitb:
    scene bg kitchen
    show kitchen berry
    menu:
        "What do you do?"
        "Talk to [bn]([bstep])" if True:
            jump kitbtalk
        "Cuddles" if True:
            jump berkitstep0
        "{color=#c13a3a}Fantasize about her.{/color}" if bstep >2:
            $ persistent.replay94 = True
            jump bersexkitchen
        "Step back." if True:
            jump tokitchen
label kitv:
    scene bg kitchen
    show kitchenval
    menu:
        "What do you do?"
        "SPANK!" if True:
            jump valkitspank
        "Talk to [vn] ([vstep])" if True:
            jump kitvtalk
        "{color=#c1a63a}Touch her pussy by surprise.{/color}" if vstep > 0:
            show 016kitchenfj with vpunch
            play sex vmoans2
            window hide
            pause
            window auto
            mc "Surpriiiise!"
            v "You're doing that again!"
            v "Houuh!"
            mc "You're already so wet. You are horny!"
            v "Yes I am!"
            if vstep <2:
                v "But stop playing with me like that. I'm not your pet!"
                mc "Ah? Interesting."
            elif True:
                v "Oh yeah, I'm your little pet! Play with my pussy as much as you want!"
            scene black with dissolve
            stop sex
            "" "You stop."
            scene bg kitchen
            show mc lol at left
            show valerie surprised o3 at right
            v "Why did you stop?"
            if vstep <2:
                mc "Because, as you said, you're not my pet, so I stopped."
            v "You can't turn me on like that and then stops, it's so frustrating!!"
            mc "Are you saying you WANT [mc] to make you cum that bad?"
            if vstep <2:
                show valerie mad
                pause
                v "Me? Never."
            elif True:
                v "Yeeeeees!!!"
            mcth "She is totally frustrated, she wants more."
            mcth "Giving her pleasure is also a way to give her frustration, very interesting!"
            call incrskill ("handskill", 3) from _call_incrskill_122
            call incrdesire ("Valerie", handskill) from _call_incrdesire_120
            jump passtime
        "{color=#c1803a}Lick her pussy by surprise.{/color}" if vstep > 1:
            $ persistent.replay80 = True
            jump valcunkitchen
        "{color=#c13a3a}Fuck her pussy by surprise.{/color}" if vstep > 2:
            $ persistent.replay71 = True
            jump valsexkitchen
        "Step back." if True:
            jump tokitchen
label kite:
    scene expression ifnight("House/kitchen/bg kitchen.webp")
    show expression ifnight("House/kitchen/kitchene.webp")
    menu:
        "What do you do?"
        "Talk to [en]" if True:
            jump kitetalk
        "{color=#c13a3a}Stick your bulge on her crotch{/color}" if estep >2:
            $ persistent.replay96 = True
            jump emmsexkitchen
        "Step back." if True:
            jump tokitchen

label kitbtalk:
    scene bg kitchen
    show mc at left
    show berry at right
    mc "Good morning [bsn]!"
    play sound bhello
    b "Good morning, my sweet candy!! You're so cute!"
    if bstep == 0:
        mc "How's it going?"
        b "Just preparing for work, and you?"
        mc "Checking anyone needs me for anything."
        b "Oh well, I should find something for you once I get ready!"
        mc "Great!"
        mc "Oh, you look gorgeous this morning, as always!"
        b "Hehehe, you know how to make me blush!"
        mcth "Complimenting her is easy, but it's already a pleasure to see her blushing like this!"
        call incrdesire ("Berry", 1) from _call_incrdesire_121
    elif bstep == 1:
        mc "Have you slept well?"
        b "Yes hehe!"
        b "I had a fascinating dream..."
        mc "Oooh, interesting, can you tell me?"
        show berry tease
        b "No."
        show mc surprised
        mc "Nooo? Why? I wanna know!"
        b "I can't tell, or I might have to kill you."
        show mc base
        mc "I see."
        mc "Just a hint?"
        show berry base
        b "Mh... I wish it could become a reality."
        b "Stop asking me for more details before I reveal too much!"
        call incrdesire ("Berry", 3) from _call_incrdesire_122
    elif bstep == 2:
        mc "How's your day?"
        b "Actually, not that good."
        show mc surprised
        b "Ah? What happened?"
        b "I need something to have a good day."
        mc "And what is it?"
        b "My good boy!"
        window hide
        show 02kiss with dissolve
        play sex bkisstongue
        pause
        window auto
        b "I love your lips so much..."
        b "Now I can start a nice day."
        call incrskill ("tongueskill", 2) from _call_incrskill_123
        call incrdesire ("Berry", tongueskill) from _call_incrdesire_123
    elif bstep >2:
        mc "How's your day?"
        b "Not good enough."
        mc "Wh-chat happened?"
        show berry lewd
        b "I did not fucked my good boy enough for today."
        show mc shy
        mc "Oh, er, we can work on it."
        b "Be sure I'm gonna use every opportunity for that!"
        call incrdesire ("Berry", 3) from _call_incrdesire_124
    pause
    jump passtime
    return

label kitvtalk:
    scene bg kitchen
    show mc at left
    show valerie o3 at right
    if vstep ==0:
        mc "Hey [vsn]"
        play sound vbrat
        v "Stop calling me like this, you brat."
        mcth "Her nipples look hard as hell!"
        mc "What are you doing?"
        v "Just drinking my coffee before starting to work."
        mc "So what are you doing tod-"
        v "Shut up, I don't want to talk with you."
        mc "..."
    elif vstep == 1 or vstep ==2:
        mc "Hey [vn]!"
        v "What do you want?"
        mc "Nothing special, what are you doing?"
        v "Are you blind? Just drinking my coffee before working."
        mc "Oh, you mean before drinking my cum on a live stream?"
        show valerie angryshy
        v "SHHHH!"
        v "Don't say it aloud, or I'll kill you!!"
        mc "I was just teasing, hahaha!"
        show valerie mad
        pause
    elif vstep >2:
        mc "Hey [vn]!"
        v "When are you fucking me?!"
        mc "?!"
        v "Don't you see that I'm all the time waiting for-"
        v "Rhhh- Nevermind."
        mc "..."
    jump tokitchen
    return

label kitetalk:
    scene expression ifnight("House/kitchen/bg kitchen.webp")
    show mc at left
    show emma o3 food at right
    if estep == 0:
        mc "What are you doing?"
        play sound eloser2
        e "Aah! You frightened me, you loser!"
        mc "Are you... eating in secret?"
        e "N-not at all! I don't even know why you say that!"
        mc "Well, the cream around your mouth, maybe."
        mc "That's funny, it looks good on you, it looks like..."
        e "..."
        show emma at angryjump
        e "GET OUT OF MY SIGHT!!!"
        mcth "How funny! Makes me wonder how she looks, a shitty personality with cum on her face..."
    if estep == 1:
        e "What do you want..."
        mc "Nothing special."
        pause
        mc "That's funny how this cream on your mouth looks like..."
        e "?"
        mc "Well, never mind."
        e "Weirdo."
    if estep == 2 or estep == 3 or estep == 4:
        show emma shy
        mc "Are you eating in secret again?"
        e "N-no!!"
        mc "..."
        e "Maybe a little bit, but pleaaase don't tell Mom!"
        mc "You know, that's funny how the cream looks like-"
        if estep ==2:
            mc "Er-"
            mc "Never mind."
            show emma base
            e "..."
            e "Alright, I understand."
            mc "?!"
            show emma angryshy
            e "I suck your dick, but this time is the very last!!"
            mcth "I didn't even ask for this!"
            e "You disgusting pervert that just uses me!"
            show mc o1b
            mc "And you're a good girl knowing how to please a man."
            show emma shy
            pause
            show mc o1c
            mc "Here it is, just for you."
        if estep >2:
            show emma tsun
            e "Like your cum..."
            e "Oh, [mc]... I think you've got something better to eat..."
            pause
        window hide
        $ persistent.replay27 = True
        play sex ebj
        show 019kitchenbj
        pause
        window auto
        mcth "Incredible!!"
        mcth "She looks like she adores it!"
        mc "You're doing so great [en]!"
        e "Hm!!!"
        mcth "She loves to hear that!"
        mc "Oh [en] if you continue like this-"
        mc "I'm about to cum!"
        pause
        mc "I warned you!!"
        window hide
        hide 019kitchenbj
        stop sex
        play audio ecuminmouth
        play audio cumexplo
        play audio cumsound
        show elv2bjkitchen-0008
        show 019kitchencum
        show cumanim
        pause
        $ cumbye +=1
        call incrskill ("cockskill", 2) from _call_incrskill_124
        call incrdesire ("Emma", cockskill) from _call_incrdesire_125
        window auto
        mc "Oh [en]... you're so talented..."
        scene expression ifnight("House/kitchen/bg kitchen.webp") with fade
        show mc at left
        show emma tsun o3 food at right
        pause
        mc "You're so gifted [en]!"
        e "Thank you, hehehe!"
        show mc lol
        if estep ==2:
            mc "But you still can't manage to take it deeper."
            show emma angryshy at angryjump
            e "WHAT?!"
            e "Next time I'll show you!!!"
            mc "Next time? You already want to do it again?"
            e "N-no! There is no next time!"
            e "I have to go!"
        jump passtime

    jump tokitchen
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
