screen balcony2:
    imagemap:
        ground ifnight("House/balcony2/balcony2.webp")
        if spos == "balcony2":
            imagebutton:
                idle "House/balcony2/mapbalconys.webp"
                hover lumi("House/balcony2/mapbalconys.webp")
                focus_mask True
                action Jump("balc2s")
        if vpos == "balcony2":
            imagebutton:
                idle "House/balcony2/mapbalconyv.webp"
                hover lumi("House/balcony2/mapbalconyv.webp")
                focus_mask True
                action Jump("balc2v")
        if bpos == "balcony2":
            imagebutton:
                idle ifnight("House/balcony2/mapbalconyb.webp")
                hover lumi("House/balcony2/mapbalconyb.webp")
                focus_mask True
                action Jump("balc2b")
label balc2s:
    scene balcony2
    show mapbalconys
    menu:
        "What do you do?"
        "Talk to [sn]" if True:
            jump balc2stalk
        "Compliment her muscles" if True:
            jump sarbalc2step0
        "Approach her." if sstep > 0:
            jump sbalc2approach
        "{color=#c1803a}Tickle the back of the knee.{/color}" if sstep > 1:
            $ persistent.replay14 = True
            jump sbalc269
        "{color=#c13a3a}Suggest another type of exercise.{/color}" if sstep >2:
            $ persistent.replay92 = True
            jump evsarsexbalc2
        "Step back." if True:
            jump tobalcony2
label balc2v:
    scene balcony2
    show mapbalconyv
    menu:
        "What do you do?"
        "Talk to [vn]([vstep])" if True:
            jump balc2vtalk
        "{color=#c1a63a}Slap her butt!{/color}" if vstep > 0:
            window hide
            show 016valass
            pause
            window auto
            v "Uh uh!"
            mcth "She didn't see me yet, the perfect opportunity!"
            show 016valassspank with hpunch
            play sound spank
            hide 016valassspank with dissolve
            play sound vmoansp1
            pause 1.0
            scene balcony2talk
            show mc lol at left
            show valerie o2 mad at right
            v "You son of a bitch!!"
            mc "Bouahahaha!"
            v "Get out!"
            call incrskill ("handskill", 1) from _call_incrskill_30
            call incrdesire ("Valerie", handskill) from _call_incrdesire_21
            jump passtime
        "{color=#c1803a}Eat her ass by surprise{/color}" if vstep > 1:

            scene v2f at angryjump
            play sex vmoans1
            pause
            v "Mother fucker!"
            v "What are you doing, disgusting shit?! I'm all sweaty!"
            mc "Doesn't matter."
            mc "You were bouncing my meat before my eyes."
            mc "I'm just eating what is mine."
            v "What are you talking about, I'll never be yours!"
            mc "Oh, I'm not sure you want me to stop."
            call incrskill ("handskill", 3) from _call_incrskill_31
            call incrdesire ("Valerie", handskill) from _call_incrdesire_22
            $ vcum +=1
            v "Oh sh-"
            v "I hate the fact that you can so easily make me-"
            stop sex
            show v2f at cumtr
            show cumanim
            play audio vcum1
            v "CUUUUUUM!!"
            v "Aaaaarh, it's so good!!"
            v "My pussy is all yours. You can eat me whenever you waaaaant!!"
            call incrskill ("tongueskill", 2) from _call_incrskill_32
            call incrdesire ("Valerie", tongueskill) from _call_incrdesire_23
            pause
            jump passtime
        "{color=#c13a3a}Legs workout suggestion.{/color}" if vstep > 2:
            $ persistent.replay74 = True
            jump valsexbalc2
        "Step back." if True:
            jump tobalcony2
label balc2b:
    scene expression ifnight("House/balcony2/balcony2.webp")
    show mapbalconyb
    menu:
        "What do you do?"
        "Talk to [bn]" if True:
            jump balc2btalk
        "Look at her posture." if bstep > 0:
            $ persistent.replay7 = True
            pause
            b "Is something wrong with my posture?"
            mc "Er, no, I think that's good!"
            b "Hm I don't think so, you should show me how to do it!"
            mc "It was good, I promise."
            b "Show me!"
            mc "Okay."
            scene black with dissolve
            "" "You're taking the position to show her how to make the moves."
            "" "When you don't pay attention, [bn] kneels below your hips and grabs your cock out of your pants."
            scene tjbg
            show btjbalc_0000
            b "Oh?"
            b "Look, I think I fell like this by mistake!"
            b "What are the odds that your cock ends up hard between my tits?"
            mc "[bn]!"
            b "Now, what are you waiting for? Show me the moves!"
            b "Nobody is watching. Show me!"
            hide btjbalc_0000
            show 015btjbalc
            play sexfx frottements2
            play sex btjmoan
            window hide
            pause
            window auto
            b "Are you sure you should move that fast?"
            mc "Not at all! But I can't stop!!"
            b "Hehehe You look so cute when you can't stop fucking my tits!"
            stop sex
            stop sexfx
            hide 015btjbalc
            show tjbg at cumtr
            show btjbalccumA at cumtr
            show btjbalccumB at cumtr
            show cumanim
            pause 0.1
            play audio bcumgoodboy
            $ cumbyb += 1
            play audio cumsoundext
            pause
            b "At least you showed me how much you love your [bsn]'s tits!"
            scene black with dissolve
            call incrskill ("cockskill", 1) from _call_incrskill_33
            call incrdesire ("Berry", cockskill) from _call_incrdesire_24
            pause
            jump passtime
        "Look at her crotch." if bstep > 1:
            $ persistent.replay37 = True
            b "Where are you looking at, naughty boy?"
            b "Are you looking at the meal I prepared for you?"
            mc "Meal?"
            b "Don't fake ignorance and eat me!"

            window hide
            stop music
            scene black
            play sex bmoans2
            play sexfx frottements
            show 02balc
            pause
            window auto
            b "Oooh yeah!!"
            b "I love it when my candy licks me like this!"
            b "Come on, baby make me cum!"
            b "Haaah!"
            window hide
            hide 02balc
            stop sexfx
            play sex bcumyeah
            show 02balccum at cumtr
            show cumanim
            pause
            window auto


            b "My legs will breaaaaak!"
            $ bcum +=1
            pause
            scene black with dissolve
            call incrskill ("tongueskill", 2) from _call_incrskill_34
            call incrdesire ("Berry", tongueskill) from _call_incrdesire_25
            pause
            jump passtime
        "{color=#c13a3a}Pretend to criticize her posture.{/color}" if bstep >2:
            $ persistent.replay93 = True
            jump bersexbalcony2
        "Step back." if True:
            jump tobalcony2
label sbalc2approach:
    scene 013n with dissolve
    window hide
    pause
    window auto
    mcth "What an incredible view..."
    s "Gnuh!"
    mcth "I wonder if I should..."
    menu:
        "What do you do?"
        "Tickle the back of her knees" if True:
            show 013n at chatouiller
            pause
            s "AAahh!! wh-what are you doing?!"
            s "Hehehehe!!"
            s "STOP IT!"
            mc "Why? it's too funny!"
            play sound sowh
            s "Time to face the consequences!!!"
            show 013o with vpunch
            window hide
            pause
            window auto
            mc "Mmmmh!!!"
            mcth "I can't breathe!"
            s "This is what you deserve for messing with the great Sarena!"
            mc "Mmmb, mbbb"
            s "Han!!"
            s "[mc] What are you doing?! Get out!!"
            mcth "I can't!!!"
            mcth "Her legs are squeezing my head so hard! I feel like it's going to explode!"
            s "Haannaaann!"
            s "[mc]!!!"
            mcth "I can feel the temperature rising so fast!!"
            s "[mc] I can't-"
            scene black with fade
            pause 1.0
            scene balcony2talk with dissolve
            show sarena shocked o2 at right
            show mc surprised at left
            mc "Bwaaaah! I thought I'd die!"
            s "I'm so sorry [mc]!"
            mc "Never mind, that's okay."
            s "It won't happen again!"
            call incrskill ("tongueskill", 1) from _call_incrskill_35
            call incrdesire ("Sarena", tongueskill) from _call_incrdesire_26
            jump passtime
        "Step back." if True:
            jump tobalcony2

label sbalc269:
    show 013n with dissolve


    s "Grrr! A little bit more."
    mcth "Hm... this is too tempting..."
    show 013n:
        linear 0.5 xoffset 50
        linear 0.5 xoffset -50
        repeat
    pause
    s "Bwawawawa [mc], What are you doing?!"
    s "If you continue, I will fall!!"
    window hide
    scene 018sarfall1
    play sound emoansingle
    show 018sarfall3 with vpunch
    pause
    window auto
    mc "Mh!"
    s "Aah!"
    s "I told you [mc]!"
    s "Onh!"
    s "Your face feels good!"
    show 018sarfall2
    hide 018sarfall3 with dissolve
    s "I wanna ride your face just a little bit..."
    s "Onh!"
    s "I'm so naughty... taking advantage of you when you're immobilized..."
    s "So naughty... It makes me so horny!!"
    s "Oh! You're so hard! Are you turned on by me riding your face?"
    mc "Hmhm!!"
    s "What are you saying? Do you challenge me to who will make the other cum the fastest?"
    s "I accept the challenge! I will not lose!"
    window hide
    scene black
    show 01869
    stop music
    play sex sbj69
    pause
    window auto
    mcth "Oh my gosh!!!"
    mcth "[sn] is sucking my dick like crazy!"
    mcth "But for the challenge, I must make her cum first!"
    pause
    mcth "Oh no, it's impossible she goes too hard!!"
    window hide
    hide 01869
    show 01869cuma
    pause 4*sp01869
    show 01869cumb
    show cumanim
    stop sexfx
    stop sex
    play sound sbj69cum
    play audio cumexplo
    play audio cumsoundext
    pause
    window auto
    s "Hmmmmmmm!"
    mcth "She came at the same time as me!!"
    pause
    scene balcony2talk with fade
    show mc humidface shy at left
    show sarena taunt o2 at right
    s "Well played [mc]. This is a 1-1, but don't worry, I'll win next time!"
    $ cumbys += 1
    $ scum += 1
    call incrskill ("cockskill", 2) from _call_incrskill_36
    call incrdesire ("Sarena", cockskill) from _call_incrdesire_27
    pause
    jump passtime
    return

label balc2stalk:
    scene balcony2talk
    show mc at left
    show sarena o2 at right
    if sstep == 0:
        mc "Oh wow! You look so strong!"
        play sound slol1
        s "Fiouh! you have no idea how hard it is!"
        mc "What is it exactly?"
        s "It's called calisthenics, and this figure is the front lever."
        s "I've got to hold my body horizontally while holding my arms straight!"
        s "It's a bit harder for girls, but thanks to my big boobies My center of gravity is higher haha!"
        mc "Oh.. I'm not sure I understood everything but it seems cool!"
        s "It is! Okay now, next set!"
    elif sstep ==1:
        mc "Ouaw, You look so good!"
        s "I'm working hard haha!"
        show sarena taunt
        s "And it seems to work perfectly considering... what we did recently!"
        s "You lusty pony!"
        mc "Well... I can't deny anything haha!"
    elif sstep ==2:
        mc "Ouaw You look so hot!"
        show sarena taunt
        s "Does it make you hard?"
        mc "Well, it could!"
        s "Don't worry, I will work hard so you can get hard all the time when I'm around eh eh eh"
    elif sstep > 2:
        mc "DAMN, you look like a goddess!"
        s "Heheh thanks my love, I'm working hard every day!"
        show sarena taunt
        s "So I can be strong enough to crush you between my legs."
        mc "*glouph*"
    jump tobalcony2
    return

label balc2btalk:
    scene expression ifnight("House/balcony2/balcony2talk.webp")
    show mc at left
    show berry o2 at right
    if bstep == 0:
        mc "Oh my gosh!!!"
        mc "Your sports gear is so..."
        play sound blol1
        b "Hehehe you like it?"
        mc "S-sure!"
        play sound blol2
        b "So why do you look so... disturbed?"
        mcth "This design looks like it was made to put something between her tits..."
        mc "It's just... unusual looking."
        b "Yeah haha I just bought it after you came, it looks funny, I'm happy you like it!"
        b "But I hope you're not thinking about something naughty, considering how you look at my chest!"
        mc "N-no, of course, I was just looking at the design..."
        b "Of course haha!"
    elif bstep == 1:
        mc "I can see you're working really hard!"
        show berry happy
        b "Yes, I'm glad you see it!"
        b "I'm getting older and older and want to keep in shape!"
        show berry base
        b "It's also essential for SEX!"
        show mc shy
        mc "Yeah, I imagine."
        b "Of course! Sex needs endurance but also strength! Especially for me when I'm savagely r-"
        show berry shy
        b "Hum, anyway, let me finish my exercises!"
    elif bstep == 2:
        show mc shy
        mc "Whoa..."
        show berry tease
        b "Are you amazed?"
        b "I'm training to ride your face!"
        mc "*Gloups*"
        show berry happy
        b "Hehehe I love your cute reaction!"
    elif bstep > 2:
        show mc shy
        mc "Whoa..."
        show berry tease
        b "Are you amazed?"
        b "I'm training to ride your cock properly."
        mc "*Gloups*"
        show berry happy
        b "Oh yeah... I'm gonna fuck it better and better..."
    jump tobalcony2
    return

label balc2vtalk:
    scene balcony2talk
    show mc at left
    show valerie o2 at right
    if vstep == 0:
        mc "Hey, [vsn]."
        v "Not you again... what do you want from me this time?"
        mc "Nothing special, I was just passing by."
        play sound vhoh
        v "Really?"
        v "I bet you just wanted to spy at your \"[vsn]\"'s booty, don't you?"
        mc "You're overestimating yourself."
        play sound vbrat
        v "Just fuck you."
        mcth "Always a pleasure to talk with [vn]. Look at this little opening on her clothing near her hips."
        mcth "It almost looks like an invitation to put in your hand..."
    elif vstep == 1:
        v "What do you want?"
        mc "Nothing, I was just admiring your butt."
        show valerie happy
        v "Of course you were! I'm hot as hell."
        v "I bet you were turned on, imagining you could fuck it hehehe!"
        show mc lol
        mc "Fuck you? Haha you're dreaming!"
        mc "I was just thinking of slapping it, as you deserve."
        show valerie base
        v "Tsss!"
        mcth "Notice how she didn't say to not do it!"
    elif vstep == 2:
        v "You again?"
        mc "Just checking if my meat is doing great."
        show valerie angryshy
        v "Who do you think you are to call me like that?!"
        show mc lol
        mc "I am the one that can make you cum."
        v "You moth-"
        show valerie base
        v "Tsss! Get away from me."
    elif vstep > 2:
        show valerie happy
        v "Oh no! Don't tell me you're gonna fuck me by surprise..."
        mc "It's not a surprise if you expect that!"
        v "Oh! Nevermind."
    jump tobalcony2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
