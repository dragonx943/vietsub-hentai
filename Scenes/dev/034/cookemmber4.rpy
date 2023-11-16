label cookberwin:
    call coolemmber1 from _call_coolemmber1
    call cookbwin from _call_cookbwin
    jump passtime
    return

label cookemmwin:
    call coolemmber1 from _call_coolemmber1_1
    call cookewin from _call_cookewin
    jump passtime
    return

label coolemmber1:
    call showscene ("034ca") from _call_showscene_69
    b "Yeees!!"
    b "Still, I congratulate you on your progress, girl."
    e "And I don't intend to stop there, I hope to become the perfect wife for [mc]!"
    b "Yup, the second perfect woman after me, Haha!"
    e "I'm not kidding!!!"
    b "You're not? You really think you can beat your mother?"
    b "I have all the experience I need to be the best woman for [mc]."
    if ispromisedtoemma == True:
        e "And yet, I'm the one he's going to marry!"
        b "Maybe, but even married I'll still be the number 1 woman in his life."
    return

label cookbwin:
    b "And I'll show you..."
    call showscene ("034cc") from _call_showscene_70
    e "Mom?!"
    e "Why are you getting undressed?!"
    "" "After getting naked, [bn] grabs your erection through your pants."
    "" "You can feel her nipple rubbing against your tip, causing you to go wild with desire."
    mc "[bn]?!"
    b "It seems that [en] doubts that I can be a better wife than her."
    b "I'll show her what an experienced woman is ..."
    b "And I'm going to show her that I can fulfill all your desires ..."
    b "Get undressed, now!"
    scene black with fade
    pause
    e "Mom?! What the-"
    stop music
    call bertjcook034 (v=1.0/12) from _call_bertjcook034_2

    $ persistent.replay125 = True
    mc "Gnh!!!"
    b "Oh yes!"
    e "Oh no!"
    b "That's it, that's my good boy..."
    b "You like [bn]'s breasts so much, don't you?"
    b "Say it!"
    e "No, don't say it!"
    e "You wouldn't dare cum between my mother's tits in front of me, would you?"
    mcth "I'm trapped..."
    b "In that case I'll speed up, and you won't be able to resist the urge to cum between my breasts!"
    call bertjcook034 (v=1.0/24) from _call_bertjcook034_3
    e "No!"
    mcth "I must resist!"
    mcth "The tits of [bn] put such intense squeeze on my shaft ..."
    mcth "They're also so soft..."
    mcth "I feel like I'm in heaven..."
    mcth "But I mustn't enjoy myself in front of [en]!"
    b "Come on, [mc], let yourself all the way out!!!"
    "" "Cock skill [cockskill]/[maxskill]"
    if cockskill < maxskill:
        mc "I'm sorry, [en], I can't hold it anymore!"
        call bertjcookcum from _call_bertjcookcum_1
        $ cumbyb += 1
        call incrdesire ("Berry", cockskill/2.0) from _call_incrdesire_134
        b "Oh yes!"
        b "Blow your balls off between your [bsn]'s tits!"
        b "That's my good boy..."
        e "No, that's not fair!"
    elif True:
        stop sex
        stop sexfx
        call showscene ("034cd1") from _call_showscene_71
        b "What do you mean?!"
        b "[mc] dares to resist me? Me?!"
        b "I will not tolerate it!"
        e "Thank you, [mc]!"
        b "I won't admit defeat so easily!"
        b "I think I'm going to have to do it the hard way!"
        b "Lie down, now!"
        pause
        call showscene ("034ce") from _call_showscene_72
        b "That's it, my good boy..."
        b "Stay still, don't move."
        b "Let [bn] take care of you."
        e "Wait, Mom?!"
        e "What do you intend to do?!"
        b "I'm going to put it in my butt, of course."
        e "What?!"
        b "He won't be able to resist this time."
        b "He's going to see his queen bouncing on his cock, he won't be able to hold back from pouring his load into me!"
        e "No!!"
        call showscene ("034cf") from _call_showscene_73
        e "Don't look, [mc]!"
        mc "Gfffuhf!"
        e "I don't want you to see that!"
        b "Not letting him see me won't stop him from cumming like crazy!"
        call beranalcook034 (v=1.0/12) from _call_beranalcook034_2
        b "Oh, fuck!!!"
        b "[mc]'s penis is so big!!!"
        e "[mc]!! Nothing is going on at all, okay?!"
        mcth "How could I think there's nothing going on?!"
        mcth "I can't see anything yet I feel a tremendous compression around my penis..."
        mcth "I feel the mighty bounce of [bn]'s ass on my pelvis!"
        mcth "It's impossible to stand against something like this!"
        call beranalcook034 (v=1.0/24) from _call_beranalcook034_3
        b "You're going to cum inside me, [mc]!"
        b "You're going to cum in my tight ass!"
        mc "I can't take it anymore!"
        e "No!!"
        b "It's so big, I can't stand it either!"
        b "Give it all you've got, all at once!"
        b "I want your testicles completely empty in the next three seconds!"
        mc "I'm cumming!"
        e "No!"
        call beranalcookcum from _call_beranalcookcum_1
        b "Oh my God!"
        b "Oh my God!"
        b "Hooo!"
        b "Haaaa!"
        play sound acum2
        call showscene ("beranalcum1") from _call_showscene_74
        b "I feel my ass full of cum..."
        b "I can't move ..."
        play sound acum3
        call showscene ("beranalcum2") from _call_showscene_75
        b "Give me a few seconds ..."
        pause
        b "I told you, [en] ..."
        pause
        b "I, [bn], am most suited to [mc]'s needs ..."
        $ cumbyb += 1
        $ bcum+=1
        call incrdesire ("Berry", cockskill) from _call_incrdesire_135
        $ persistent.replay126 = True

    jump passtime
    return



label cookewin:
    e "I highly doubt it, and I'm going to prove it to you!"
    e "Knowing [mc], it's not just cooking that will satisfy him!"
    scene black with fade
    pause
    b "Wait, what are you doing?"
    call showimgtall1 ("034cbtall") from _call_showimgtall1
    mc "Wow ..."
    e "Look at him ..."
    e "Look how he drools over my perfect body."
    e "I forged this body especially for [mc]."
    e "He loves my ass, he's been fantasizing about it for a long time already!"
    b "And he's been fantasizing about my tits for even longer!"
    show 034cbtall:
        linear 4.0 yalign 0.0
    e "We'll see about that."
    e "[mc], can you undress and get on the floor, please?"
    e "Thanks, you're a sweetheart."
    b "What do you intend to do?"
    scene black with fade
    pause
    stop music
    call emmajcook034 (v=1.0/12) from _call_emmajcook034_2
    $ persistent.replay124 = True
    mc "[en]!"
    b "[en]?! Stop that, immediately!"
    e "Never!"
    e "I'll show you how bad he loves my ass!"
    call emmajcook034 (v=1.0/24) from _call_emmajcook034_3
    b "[mc], I forbid you to cum!"
    mc "But I-"
    e "You have no right to forbid him to cum!"
    b "I said, forbidden!"
    mcth "Focus! I've got to stay focused!"
    "" "Cock skill [cockskill]/[maxskill]"
    if cockskill < maxskill:
        mc "Oh no, [en], you have way too much skill in your movements!"
        mc "I can't hold it anymore!"
        e "Go for it! Free yourself!"
        mc "I'm coming!!"
        call showscene ("emmpjcookcum") from _call_showscene_90
        call cummale from _call_cummale_42
        e "Yes!!"
        b "No!!"
        e "You see, it's me, his chosen one!"
        $ cumbye += 1
        call incrdesire ("Emma", cockskill/2.0) from _call_incrdesire_136
        pause
    elif True:

        "" "You focus on your breathing..."
        mcth "It's okay, I think I can resist!"
        scene black
        call showimgfury ("emmrefuscumcook") from _call_showimgfury_4
        e "What do you mean he's resisting me?!"
        b "That's good, [mc]. You're a good boy!"
        e "No!!"
        e "I have to show my mother that I'm best suited to marry [mc]!"
        e "I'm not finished!"
        e "There's only one solution!!!"
        call showscene ("emmpreanal") from _call_showscene_76
        b "[en]?!"
        mc "[en]? Don't tell me you're going to-"
        e "I am!"
        e "I think my ass is very tight. I shouldn't have any trouble making him come that way!"
        b "[en]?! Are you even aware of the size of [mc]'s gear?"
        e "Of course I'm aware of it!"
        e "I knew I'd be doing this sooner or later, so I've been practicing with a few toys for a while!"
        e "It's time to take it to the next level!"
        e "Oh my God, it's really hard... I really have to force it with all my weight!"
        e "Let's go!"
        call emmanalcook034 (v=1.0/12) from _call_emmanalcook034_2
        mc "Hmmm!!"
        e "Oh my God!"
        e "This is so huge!"
        e "I can't imagine what it would be like if I hadn't practiced!"
        b "Don't look, [mc]."
        b "There's nobody in front of you."
        b "There's only me, [bn], kissing you tenderly."
        e "You think you can make him forget I'm here?!"
        e "I'm willing to give 1000%% for [mc]!"
        call emmanalcook034 (v=1.0/24) from _call_emmanalcook034_3
        e "I'll make him come!"
        mc "Hmmmm!!!!"
        mcth "[en]'s hip thrusts are so powerful!"
        mcth "I can't resist this!"
        mcth "But [bn] is kissing me, how am I going to signal to her that I'm about to cum?"
        e "I know what you're thinking, [mc]."
        e "Come in my ass!"
        e "I'll do anything for you I'm ready to take anything!"
        mcth "Oh I'm cumming!"
        call emmanalcookcum from _call_emmanalcookcum_1
        e "Yes!!"
        e "I feel it! I feel it!"
        e "[mc]'s cum is filling my entire ass!"
        b "No!!"
        b "Naughty boy!!"
        play sound acum2
        call showscene ("emmanalcookcum2") from _call_showscene_77
        e "Look at that!"
        e "There's so much cum dripping out of my ass."
        e "He's really released it all!"
        mc "I'm sorry, [en] ..."
        e "No don't be, that's what I wanted, haha!"
        e "I was able to show my mother that I'm the best at making you orgasm, Haha!"
        $ persistent.replay123 = True
        $ cumbye += 1
        $ ecum += 1
        call incrdesire ("Emma", cockskill) from _call_incrdesire_137
    jump passtime
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
