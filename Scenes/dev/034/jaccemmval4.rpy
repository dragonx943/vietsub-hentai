label jacc4emmval:
    scene black
    "" "You change into your swimwear."
    "" "Suddenly, you hear two women giggling behind your back."

    call showscene ("034q") from _call_showscene_46

    e "Look at him!"
    if ispromisedtoemma == False:
        e "The person I love is so sexy..."
    if ispromisedtoemma == True:
        e "My boyfriend is so sexy!"
        v "That's for sure ..."
    v "Just looking at him makes me want to eat his dick!"
    e "HEY!"
    if ispromisedtoemma == True:
        e "Don't say that in my presence, he's MY boyfriend!"
        v "Yes that's right, he's our-, I mean your boyfriend, Haha!"
    call showscene ("034p") from _call_showscene_47
    mc "Hi, [en], [vn]!"
    mc " Do you want to join me?"
    e "You bet! Of course!"
    v "I book my seat on [mc]'s lap!"
    e "Hey, stop it, you have no right!"
    e "[mc]'s lap is for his princess!"
    e "[mc]'s knees are for me!"
    v "How about letting [mc] choose?"
    e "He'll choose me then!"
    e "Who do you choose, [mc]?"
    v "No, not yet!"
    v "Let's have some fun, we'll strike a sexy pose, and only then let [mc] decide."
    e "Sounds like fun, let's do it!"
    call showscene ("emmposejacc") from _call_showscene_48

    "" "[en] strikes a simple pose by the hot tub."
    "" "She's exposing her beautiful legs to your eyes, all the while flashing a cute little smile."
    e "Oh, [mc], pick me!"
    call showscene ("034w") from _call_showscene_49

    "" "[vn], meanwhile, lends a forward-leaning pose."
    "" "She's showing off her big breasts in an effort to bewitch you."
    v "I'll be the one to choose, the experienced woman!"
    e "Oh no, don't show her your breasts, those are so big ..."
    mcth "Who am I going to choose this time?"
    menu:
        "Who wins?"
        "[en]" if True:
            jump jacc4ewin
        "[vn]" if True:
            jump jacc4vwin
    return
label jacc4ewin:
    show emmposejacc
    e "Yes!!!"
    e "I'm so happy every time [mc] picks me!"
    call showscene ("emmtjmass0") from _call_showscene_50

    e "[mc]? Are you sure this is correct?"
    mc "Well, what's the problem?"

    mc "The winner was entitled to sit on my lap, it's my duty to look after her properly."
    call showscene ("emmtjmass0") from _call_showscene_51
    v "What a bastard..."
    pause
    scene black with dissolve
    pause
    e "Oh, [mc] ..."
    pause
    stop music
    call emmtmassjacc034 from _call_emmtmassjacc034_1
    $ persistent.replay116 = True
    mc "You were afraid of [vn]'s breasts, which are bigger than yours."
    e "Yes she's so voluptuous and beautiful ..."
    mc "I want you to know that, one, yours is very big too."
    mc " Two, it's not the size of the breast that's important, it's the person who wears it."
    mc "I love your breasts, [en]!"
    e "Oh yes, [mc], I feel it through your hands!"
    e "They're so warm, and manly!"
    v "Am I bothering you?"
    "" "hand skill [handskill]/[maxskill]"
    if handskill < maxskill:
        call showscene ("034v") from _call_showscene_52
        e "Thank you [mc] for such a lovely time!"
        v "[mc] you little pervert, but you took good care of her, Haha!"
        stop sex
        stop sexfx
        call incrskill ("handskill", 3) from _call_incrskill_135
    elif True:
        e "[mc], you're so good with your hands, I want to return the favor!"
        stop sex
        stop sexfx
        call showscene ("valjacctalk1") from _call_showscene_53
        v "Well, well, well ..."
        v "What if ... You take care of him with your tits?"
        v "You were telling me about it the other day."
        v "You were jealous of other women because they have bigger breasts than you ..."
        v "And there's no reason to be."
        e "I don't know if I can-"
        v "Don't worry, I'll help you ..."
        v "We'll show [mc] what a good girl you are!"
        call emmtfjacc034 (v=1.0/8) from _call_emmtfjacc034_2
        $ persistent.replay117 = True

        e "Oh my God!"
        v "Well, [mc]?"
        mc "That's really nice!"
        e "But look, but they don't even touch!"
        v "You're really complex about everything and anything!"
        v "Do you really think [mc] cares about that kind of detail?"
        v "Just be present and focus on the fun!"
        mc "Oh, [en], that's good!"
        call emmtfjacc034 (v=1.0/16) from _call_emmtfjacc034_3

        e "[vn]!"
        v "Do you want to make him come?"
        e "Yes!"
        e "I want him to cum between my breasts!"
        v "Come on, [mc]!"
        mc "Oh yes, [en], that's good!"
        mc "[en], your breasts are going to make me cum!"
        call emmtfjacccum034 from _call_emmtfjacccum034_1

        e "Oh my God!!!"
        mc "Haaaa!"
        mc "Hooo!"
        e "He's cumming all over my face!"
        v "Go ahead, [mc], empty your balls!"
        v "Look how she loves it!"
        $ cumbye += 1
        $ ecum += 1
    jump passtime
label jacc4vwin:
    call showscene ("034w") from _call_showscene_54
    $ persistent.replay114 = True
    v "You made the right choice."
    e "Oh no, I didn't!"
    v "Don't worry, it's just for the moment, it doesn't mean he doesn't love you!"
    play sex vmoans2
    call showscene ("034r") from _call_showscene_55

    v "It's good..."
    play sound etsah
    e "Tsah!"
    e "It's not fair ..."
    e "What's with your face?"
    stop music
    call valfjjacc034 (v=1.0/6) from _call_valfjjacc034_2
    e "You look like you're on the verge of orgasm sitting on [mc]'s lap, you're exaggerating!"
    v "Well actually ..."
    call valfjjacc034 (v=1.0/12) from _call_valfjjacc034_3
    v "Oh boy!"
    v "[mc]'s lap is so comfortable!"
    v "[mc] is so good!"
    e "Well, are we done here?"
    "" "hand skill [handskill]/[maxskill]"
    if handskill < maxskill:
        call showscene ("034v") from _call_showscene_56
        v "Thank you so much, [mc], for a very nice time, Haha!"
        e "Next time, I'll win!"
        call incrskill ("handskill", 3) from _call_incrskill_136
        pause
    elif True:
        v "Oh no it's coming!"
        call valfjjacccum034 from _call_valfjjacccum034_1
        v "Hooo!"
        v "I'm coming so hard!"
        call showscene ("034s") from _call_showscene_57
        e "No way!"
        e "I was sure you were up to something!"
        e "You forced him to put his hand on your pussy didn't you?!"
        e "You're mean!"
        v "I want to apologize."
        v "I've got an idea, I'm going to teach you a new skill."
        e "Oh yeah?"
        v "I'll show you."
        stop music
        call valdhjjacc034 (v=1.0/8) from _call_valdhjjacc034_2

        e "Oh my God!"
        v "This is two-handed masturbation!"
        e "Does it, does it work?"
        mc "Gee, [vn] is pretty good after all!"
        v "Gosh, [mc]'s dick is so big ..."
        v "I've never had so much trouble masturbating a penis with both hands ..."
        e " Are you able to make him come that way?"
        v "Is that a request, or a question?"
        e "A question, don't make him cum!"
        e "His cum is for me!"
        call valdhjjacc034 (v=1.0/16) from _call_valdhjjacc034_3

        mc "Oh shit!"
        e "What the hell are you doing?"
        v "Poor guy, he's on the verge of dropping everything, it would be torture not to finish him off now!"
        e "No stop!"
        e "You're so good at making him feel good, I don't want him to fall in love with you!"
        e "No!!"
        call valdhjjacccum034 from _call_valdhjjacccum034_1

        e "Haaaa!"
        mc "Oh boy!"
        v "You said his cum was only for you, well here it is, Haha!"
        e "[vn], that's not funny!"
        v "Haha!"
        $ cumbyv+=1
        $ persistent.replay115 = True
    jump passtime
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
