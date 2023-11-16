define firstparty = False
label party:
    if firstparty == False:
        if blv > 0 and vlv > 0 and elv > 0 and slv > 0:
            jump fparty
        elif True:
            "" "You have to talk to each girl when they work before accessing this event."
            jump toliving
    elif True:
        jump partydebut0
label partydebut0:
    scene black with fade
    "" "It's party time!"
    "" "[bn], [en], [sn], [vn] and you are having a good time together, having a few drinks."
    "" "About an hour later, everyone is a bit tipsy."
    scene dancingbg
    show mc drunk o5:
        xalign -0.1
    show sarena drunk o5:
        xalign 0.3
    show berry drunk happy o5:
        xalign 0.5
    show valerie happy drunk o5:
        xalign 1.0
    show emma smirk drunk o5:
        xalign 0.8
    pause
    jump partydebut
label partydebut:
    s "Hehe, I think it's time to dance!"
    $ firstparty = True
    s "Come to your [ssn]. She wants to dance with her pony!"
    b "No, come to your [bsn]. I want to cherish my sweet candy soo bad!"
    v "Candy? Well, I don't know if it's because I'm drunk, but this brat looks like a snack."
    e "Yeah, I'm sure this snack-I-mean-loser doesn't even know how to dance!"
    jump choosedir
label choosedir:
    menu:
        "Which girl do you want to join this time?"
        "Join [bn]" if True:
            jump pjb
        "Join [vn]" if True:
            jump pjv
        "Join [sn]" if True:
            jump pjs
        "Join [en]" if True:
            jump pje
        "No one, just go to sleep." if True:
            $ daytimenumber = 3
            jump passtime
label pjb:
    hide sarena with dissolve
    hide valerie with dissolve
    hide emma with dissolve
    show mc:
        linear 0.2 xalign 0.25
    show berry base
    menu:
        "What do you do?"
        "Dance with her." if True:
            jump partywithberry
        "{color=#ff9a40}Ask her about her husband.{/color}" if blv == 1:
            jump bpartyask
label bpartyask:
    mc "So tell me, how is it going with your husband?"
    show berry serious
    b "Oh, well, as you already know, he is always far away from home..."
    mc "Yes, but I mean... as a partner..."
    show berry base
    play sound bnaughtyboy
    b "Oh you mean as a sexual partner? You're such a naughty boooy to ask me something like this!"
    mc "Yeah, but, I mean, I'm just curious about a woman's perspective."
    show berry happy
    b "Oh, that curiosity could make you a really good man, you know!"
    show berry base
    b "I think every woman is different and expects different things. There is no right answer."
    b "You'll have to watch and learn her tastes individually."
    b "To me, I'd say..."
    show berry shy
    b "I think we're not... on the same level of libido, I guess..."
    b "He always falls asleep before I get satisfied..."
    b "I would also love it if he'd be a bit more.. docile."
    mc "docile?"
    b "Yes, you know, maybe it's a man thing, to try being the one in charge..."
    b "I would prefer a cuter behavior that would let me submerge him with all my love."
    show berry lewd
    b "That... I... could.. completely..."
    show berry base
    b "Anyway."
    show mc base
    mc "Okay, thank you for your honest answer!"
    b "And you, how is it going with your b-, your girlfriend?"
    mc "Hmm I'd say that she isn't giving me what I need, I guess."
    b "It doesn't surprise me, this f-, hum, I mean, I don't agree with you being with her, you should dump her out."
    b "But that's for you to decide. Find a girl that would take good care of you."
    mc "I'll think about that, thank you, [bsn]!"
    show berry happy
    b "Thank you for your attention on me!"
    mcth "So [bn] needs much more affection and wants to lead the relationship and the sex."
    $ blv = 2
    jump pjb

label pje:
    hide sarena with dissolve
    hide valerie with dissolve
    hide berry with dissolve
    show mc:
        linear 0.2 xalign 0.55
    menu:
        "What do you do?"
        "Dance with her." if True:
            jump partywithemma
        "{color=#ff9a40}Ask her about her boyfriend.{/color}" if elv == 1:
            jump epartyask
label epartyask:
    mc "So tell me, how is it going with your boyfriend?"
    show emma angry
    e "Why do you think I'm gonna talk about that with you?"
    mc "Oh come on, don't you like it when people are interested in you?"
    show emma base
    e "..."
    show emma angry
    e "Do you think because I'm drunk, you can trick me?!"
    mc "No, I swear!"
    show emma base
    pause
    e "Okay."
    e "Any comments?"
    mc "I won't make any comments."
    show emma smirk
    e "I fucking love when he fucks me."
    mc "..."
    pause
    show emma shy
    e "But..."
    e "Sometimes I wish he'd get a bigger thing... I don't feel... satisfied like I would like to be..."
    e "I don't know if it's because of the size or how he does it..."
    e "He told me I was frightening sometimes because to him I go too crazy when he touches me..."
    e "This bastard even called me a nympho!"
    mcth "Hm?! She's so harsh with him! It's like she is with him only for sex..."
    mcth "A nympho?!"
    mcth "I really wonder how she'd look, when being smashed."
    show emma angryshy
    e "And with this confinement, I can't even get my daily fuck!!"
    e "I feel so mad and horny!!"
    show emma base
    pause
    e "You stay silent. At least you kept your word."
    e "But I never said that, right?"
    mc "I don't know what you're talking about."
    e "Good."
    mcth "Okay so [en] is horny, she likes big dick, and her boyfriend defines her as a nympho."
    mcth "It really sounds like a sex addict, I wonder if she could get deeper feelings in addition to that?"
    mcth "Wait, is she always aggressive because she isn't sexually satisfied?"
    $ elv = 2
    jump pje
label pjs:
    hide berry with dissolve
    hide valerie with dissolve
    hide emma with dissolve
    show mc:
        linear 0.2 xalign 0.05
    menu:
        "What do you do?"
        "Dance with her." if True:
            jump partywithsarena
        "{color=#ff9a40}Ask her about her girlfriend.{/color}" if slv == 1:
            jump spartyask
label spartyask:
    mc "So, how is it going with your girlfriend?"
    s "Ah? You sound very concerned about the love aspect of my life!"
    mc "I just want to be sure everything is alright for my [ssn]."
    show sarena shy
    s "Rhooow you'll make me blush!"
    s "Well, to be honest, I'm a bit lost nowadays..."
    s "I love her, but... I don't know, I feel like something is missing..."
    mc "What could be missing?"
    show sarena taunt
    s "Are you insinuating I'm talking about a cock?"
    show mc surprised
    mc "Oh not at all!!!"
    show sarena happy
    s "Just kiddin' haha"
    show sarena sad
    s "I really wonder about that, actually."
    show mc base
    s "I never was attracted by a guy before. Girls always have been so hot!"
    s "You are the only guy I'm close to."
    s "And you see, sometimes I feel like I even prefer our friendship to my relationship with my girlfriend..."
    s "I feel guilty for that very often, but at the same time, I try not to ignore my true feelings."
    s "I don't know if I miss a cock, she always tells me she's sure that I'm lesbian."
    s "I guess we maybe lack a close relationship like the two of us!"
    mc "I think I understand what you mean."
    show sarena happy
    show mc shy
    s "Of course you understand, you're my soulmate haha!"
    mcth "Gosh she makes me blush so much!!"
    show sarena base
    s "And you, your girlfriend?"
    show mc base
    mc "We clearly are not on the same level of complicity as you and me."
    mc "But she's the only girl that asked me out so... I don't know."
    show sarena shy
    s "Don't take it badly, but... I think you deserve someone that respects you better."
    show sarena base
    s "If you wish, after the confinement, you dump her, and I'll help you to find a better girlfriend hehe!"
    mc "You're so kind, [sn]!"
    mcth "So, [sn] loves her girlfriend, but it's not enough. It seems I can possibly give her what is missing."
    mcth "Imagine she quits her girlfriend, I quit mine, and then we [sn] and I get together... Just, imagine..."
    mcth "I'm thinking too much."
    mcth "She seems lost for now, I guess she'll need time to think about all of this."
    $ slv = 2
    jump pjs




label pjv:
    hide sarena with dissolve

    hide berry with dissolve
    hide emma with dissolve
    show mc:
        linear 0.2 xalign 0.75

    menu:
        "What do you do?"
        "Dance with her." if True:
            jump partywithvalerie
        "{color=#ff9a40}Ask her about her relationship with your dad.{/color}" if vlv == 1:
            jump vpartyask

label vpartyask:
    mc "So, how is life with my dad?"
    show valerie happy
    v "You're kidding? Are you interested in that for real?"
    mcth "Well, not really, but I try to find as much information as possible."
    mc "Yeah, of course!"
    v "Oh well, I'd say it works well."
    v "He's always ready for a good fuck."
    pause
    show valerie think
    v "Or maybe..."
    pause
    v "I wish he'd be a bit more... Rough... Sometimes."
    v "Like I wish he'd be more dominating."
    mc "Thank you, [vn]."
    show valerie angry
    v "Oh gosh why did I say that so easily?!"
    v "What do you want to do with this information?!"
    mc "Nothing special, I was just curious."
    v "..."
    mcth "Actually, this is very interesting..."
    mcth "I wonder if I could use this information to take some revenge on her later."
    $ vlv = 2
    jump pjv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
