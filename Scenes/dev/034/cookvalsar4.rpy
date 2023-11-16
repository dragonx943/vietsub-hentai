label cookvalsar:
    call showscene ("034cg") from _call_showscene_78
    s "[vn] ..."
    v "[sn] ..."
    mc "???"
    s "I think we agree."
    v "Yes, that's a good idea."
    mc "What's going on? They haven't even talked!"
    mc "Agree on what?"
    v "It's always us, cooking for you."
    s "I want to enjoy myself too!"
    mc "You want me to cook?"
    s "Not necessarily cook ... But you can make us a nice little snack."
    v "Let's have some fun ... What if ... Only one of us got to have that snack?"
    s "In that case, you'll starve."
    s "[mc] will always choose me, in any situation."
    s "He knows very well that I'm ready to do anything for him."
    v "We'll see about that!"

    call showscene ("034ch") from _call_showscene_79
    s "Oh, [mc] ... I'm so hungry ..."
    s "I need you to feed me ..."

    call showscene ("034ci") from _call_showscene_80
    v "I haven't eaten anything in almost two weeks ... I'm so hungry ..."
    s "Liar!!!"
    v "I could eat anything ..."
    menu:
        "Who wins?"
        "[sn]" if True:
            jump cook4swin
        "[vn]" if True:
            jump cook4vwin
    return




label cook4swin:
    call showscene ("034cg") from _call_showscene_81
    s "I won!!"
    v "Indeed ..."
    v "I hope I get a little bite ..."
    s "If I understand correctly, I have to prepare food for [sn]?"
    s "Yes, but there's only one thing I want to eat."
    s "Meat. Specifically your meat!"
    v "I knew you were going to say that!!!"
    play sex skiss
    play sexfx vmoanslick
    call showscene ("034cm") from _call_showscene_82

    mc "Oh my God!!!"
    mc "This is incredible!"
    mcth "[sn] sucks my cock ... While [vn] sucks my balls ..."
    mc "Oh boy, how do I not cum in a second?"
    s "[mc]'s meat is the best on earth ..."
    s "I could enjoy it every day ..."
    s "I mean, I already enjoy it every day, haha!"
    s "All that's missing is the cream!"
    s "A hot cream prepared by Mrs [vn] ..."
    s "Cum! Otherwise I'll have to go harder!"
    mcth "Ah? if I don't cum, [sn] has another idea in mind ..."
    "" "Cock skill [cockskill]/[maxskill]"
    if cockskill < maxskill:
        mcth "But it's impossible not to cum!"
        mc "I can't take it anymore, I'm cumming!"
        stop sex
        stop sexfx
        play audio sbjcum
        scene 034cw
        call cummale from _call_cummale_40
        $ cumbys += 1
        call incrskill ("cockskill", 2) from _call_incrskill_139
        s "Hmmmm!!!"
        mcth "This is crazy ..."
        mcth "[sn] delights so much in my seed ..."
        mcth "Other women also adore my semen but it's a whole new league with [sn]."
        s " She's the real deal ..."
        v "She's the one tasting the cum I've warmed-up, grrr..."
    elif True:

        "" "By focusing you manage not to cum."
        s "Why are you trying to hold back?"
        v "It's because he wants the sperm to be for me!"
        s "You're forcing me to do it the hard way!"
        stop sex
        stop sexfx
        scene black with dissolve
        pause
        call showscene ("034cv") from _call_showscene_83
        v "[sn] ... You're so hot!"
        mc "[sn]? What are you-"
        s "In my ass."
        mc "[sn]?!"
        s "I want you to fuck me now."
        v "Oh my god, she's so direct, I love it!"
        s "My ass is tight, it'll be impossible for you to resist cumming!"
        v "What about me?!"
        s "I may have...another dish for you to enjoy..."
        stop music
        call saranalcook034 (v=1.0/12) from _call_saranalcook034_2

        s "Oh yes!"
        s "Hooo!"
        s "Oh yes! Oh yes!"
        s "[mc]'s cock is stretching my ass so far apart!"
        s "His penetration in me is so intense!"
        s "And meanwhile, [vn] is licking my pussy!"
        s "I'm so over-stimulated, I'm losing it!"
        mcth "I love it so much when [sn] goes crazy with pleasure!!!"
        call saranalcook034 (v=1.0/24) from _call_saranalcook034_3

        s "Haaaa! Haaaa!"
        s "This is too intense!"
        s "I'm going to cum through every hole!"
        s "I'm gonna-"
        call saranalcookcum034 from _call_saranalcookcum034_1

        s "This is so good!!!"
        s "I can't think of anything else besides the pleasure I'm feeling right now!"
        play sound acum2
        call showscene ("034cu") from _call_showscene_84
        s "All this cum pouring out of my ass ..."
        v "She managed to take all that?!"
        v "She's really tough ..."
        s "Thank you!!"
        $ cumbys += 1
        $ scum += 1
        $ persistent.replay122 = True
    jump passtime


label cook4vwin:
    call showscene ("034cg") from _call_showscene_85

    v "I won, Haha!"
    s "He just wanted to be nice to you."
    s "He chooses you, but his heart chooses me."
    v "Enough chatter, I'm hungry!"
    v "Give me your dick!"
    s "?!"
    v "I want to eat [mc]'s cock!"
    play sex skiss
    play sexfx vmoanslick
    call showscene ("034cj") from _call_showscene_86

    "" "The two women got active and took care of you."
    mcth "Oh my god it's so good!"
    mcth "[vn] sucks my cock ... And [sn] sucks my balls ..."
    "" "They both look at each other like they're in the middle of a challenge."
    mcth "It's crazy, they look like real rivals!"
    mcth "I feel I can play ..."
    mcth "If I orgasm it will please [vn]. If I don't orgasm, it will please [sn]."
    "" "Cock skill [cockskill]/[maxskill]"
    if cockskill < maxskill:
        mcth "No it's impossible not to cum!!!"
        mc "I'm cumming!"
        v "My delicious dish!!"
        mcth "My God ... These two women will end up sucking out my soul ..."
        stop sex
        stop sexfx
        play audio sbjcum
        scene 034ck
        call cummale from _call_cummale_41
        call incrskill ("cockskill", 2) from _call_incrskill_140
        $ cumbyv += 1
    elif True:
        stop sex
        stop sexfx
        call showscene ("valbjcookmad") from _call_showscene_87
        v "What do you mean he's not cumming?!"
        v "What are you trying to do?!"
        s " Lady isn't good enough to make [mc] come?"
        s "And what's more, she complains?"
        s "[mc], I think she deserves to be punished!"
        mc "Feeds and complains about not having enough?!"
        mc "I agree, she deserves a punishment!"
        call showscene ("034cx") from _call_showscene_88

        s "There ..."
        v "Hmmm!"
        s "Shut up!"
        s "She's all yours, [mc] ..."
        s " Fuck her ass!"
        call showscene ("034cl") from _call_showscene_89

        v "MMhh!!"
        s "That's good ..."
        s "Penetrate her very gently ..."
        s "And after a while, I want you to fuck her severely!"
        v "Yef!!!"
        call valanalcook034 (v=1.0/12) from _call_valanalcook034_2

        s "That's good, [mc], keep going ..."
        s "Her asshole's only there to serve you ..."
        mc "So tight!"
        s "She's like a cum hole!"
        s "She's taken on the role of house slut, remember."
        s "Faster!"
        call valanalcook034 (v=1.0/24) from _call_valanalcook034_3

        v "Mmmmmhhh!!!"
        v "Hooo!"
        mc "I can't take it anymore!"
        s "I want you to drop everything in her ass!"
        s "I want her to get your seed all over her body!"
        mc "I'm coming!!!"
        call valanalcookcum034 from _call_valanalcookcum034_1

        v "Ah, fuck!"
        v "There's too much cum!"
        v "It's everywhere!"
        v "I'm a naughty girl, I want to be punished like this more often!!!"
        s "It seems she loved it, Haha! She's like a toy to both of us..."
        $ cumbyv += 1
        $ vcum += 1
        $ persistent.replay120 = True
    jump passtime
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
