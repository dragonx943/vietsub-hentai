label devsp9:
    scene bg kitchen
    play music sand_castle
    show sarena o4 at right
    show valerie happy o3:
        xzoom -1
        xalign 0.0
    v "You're really hot!"
    s "Thank you! I'm working hard every day!"
    v "I can see that."
    v "I've never been with a girl with your body type, I bet it's incredible!"
    s "A girl? Aren't you heterosexual?"
    v "I prefer cocks, of course, but... Sometimes I feel like I could enjoy the company of some women."
    show sarena shocked
    s "Er... is that an invite?"
    show valerie surprised
    v "Oh no, of course not!"
    show valerie shy
    v "I was wondering... How does being with a female instead of a male feel?"
    show sarena base
    s "Hm, I'm not sure how I could answer that question."
    s "I'm lesbian, I've never been with a male, so I can't compare."
    v "Are you lesbian for real?"
    s "Of course, are you doubting it?"
    v "I mean no offense, it's just that when I look at [mc] and you... I feel like you're like a couple already."
    show sarena shy
    s "A- a- a couple?!"
    show valerie happy
    v "Yeah, He looks like a boy in love when you're talking with him, and-"
    v "I saw that you always sit on him... like... two people that are more than friends..."
    s "I guess it's just because our relationship is special!"
    v "I see... So, are you feeling better with your girlfriend or with [mc]?"
    show sarena base
    s "What a question! [mc] of course!"
    show valerie base
    v "Ah? You answered without any hesitation."
    show sarena sad
    s "Oh..."
    s "I get what you mean..."
    s "My girlfriend is always mad at me, she wasn't like this at the beginning."
    s "When we talk, it always ends up with reproaches. I missed that time when she wasn't like this."
    v "Or maybe she was like this but was hiding it?"
    s "Hm?"
    show valerie shy
    v "I'm sorry, I think I went too far in your private life."
    s "Nah, it's okay..."
    v "So... is she fulfilling your sexual desire at least?"
    s "Hm... I guess..."
    v "So, you're not sure of that?"
    s "I-"
    pause
    v "I'm sorry I should stop right there, your relationship seems complicated. It's not my business."
    v "Just remember, don't force yourself into a relationship if it's not worth it."
    s "I'll think about that."
    s "Thank you, [vn] for listening to me."
    v "My pleasure!"
    scene bg living1 with fade
    show mc
    mcth "[sn] doesn't feel happy with her girlfriend, I'm sure."
    mcth "I wish she could make the right decision to get a happier future."
    $ slv = 9
    if vbounds + 5 < vboundsmax:
        $ vbounds += 5
    jump passtime
    return

label devsp10:
    scene 018mastlit
    play music causmic
    show 018mastlitcul1
    s "Yeah..."
    s "I miss you too..."
    s "Hm..."
    pause
    s "Am I actually masturbating?"
    s "Er.. Not yet but-"
    pause
    s "I'm sorry... I thought..."
    s "It's just that we haven't done anything with us both in isolation for a while so maybe..."
    pause
    s "Don't call me that!"
    s "I'm not a... I just have natural desires!"
    s "... Stop..."
    s "Listen, I think this is a bad time to discuss, I think I should call you later."
    s "Yeah, bye."
    pause
    s "This can't keep going like this..."
    s "Why can't she be more like [mc]? At least he always respects me, and doesn't get mad when I'm a bit horny."
    pause
    s "[mc]..."
    pause

    show 018mastlitcul2 with dissolve
    hide 018mastlitcul1 with dissolve
    stop music
    play sex smoans1
    pause
    s "Oh [mc]..."
    s "Let me sit on you again..."
    s "Let me feel your... thing... hard... again..."
    s "I feel so horny..."
    s "Just do as I say, [mc], I want you to touch me right there..."
    s "Don't worry, you're safe with me..."
    s "Please.. touch me... please... your... tongue... just once... please..."
    s "What? Do you want it to be my toy? My personal toy? Doesn't it sound a bit demeaning?"
    s "If you want then... It's now my toy I can play with, whenever I want... This idea makes me so wet... I'm so wrong..."
    s "If he knows I'm thinking about such things, he won't talk to me ever again..."
    mcth "Toy?! She means she wants my cock to be her sextoy?!"
    mcth "[sn] is masturbating thinking of my cock as her toy?! I'm NOT mad AT ALL!!"
    mcth "Actually, she has always been like this, like my body was hers and played without asking for permission... But I didn't know she enjoyed it to that point."
    mcth "She always told me \"she is lesbian\" as a reason to make it like it's nothing."
    mcth "I have been enjoying it since the beginning because she always did it with respect."
    mcth "Was she lying about her sexuality? Or maybe she was lost and this excuse was for herself, not me?"
    mcth "So, she's confirmed not to be lesbian after all."
    mcth "She said she only got with her current girlfriend, I bet she thought to be lesbian because her GF insisted on it."
    mcth "[sn] finally has some desire for me... I feel so happy!!"
    mcth "I want my [ssn] to be the happiest in the world, I would do anything for this."
    mcth "She needs me, I will be there for her. If she wants my dick as a toy, I'm in."
    mcth "I know she doesn't mean ”toy” in a disrespectful way."
    mcth "It will be her toy."
    mcth "Let's enter and-"
    b "What are you doing?"
    stop sex
    scene bg firstfloor talk night
    show berry at right
    show mc shy at angryjump
    mc "Er nothing at all!"
    b "Haah?"
    show berry tease
    b "You look so suspicious..."
    show berry happy
    b "Hm, anyway, I must be wrong."
    hide berry with dissolve
    mcth "Waaaah! [bn] almost caught me peeking on [sn]..."
    pause
    show mc base
    mcth "[sn] doesn't feel happy. I have to make her happy."
    mcth "I can't tell her to dump her girlfriend, she has to make that decision on her own."
    mcth "I guess if I wasn't interrupted and entered like \"Here is your toy!\", it wouldn't have worked."
    mcth "She seems to fantasize about it, but if it becomes real, she would probably panic and freak out."
    mcth "All I can do for now is to support her as much as I can, and maybe one day..."
    mcth "Until she decides, I'll be there for her."
    if mcstatus == "in couple":
        pause
        mcth "... I just realized my girlfriend isn't better. With me. I think I will have to make a decision as well."


    $ slv = 10
    jump passtime
    return


label devsp11:
    $ persistent.replay21 = True
    $ persistent.replay19 = True
    s "Suuure!"
    s "Hmm what could we do..."
    mc "Why not in your room?"
    s "Ah?"
    mc "I don't know, maybe some people would like to do sports in their room? just a suggestion."
    s "That's an amaaaazing idea!!!"
    s "No wonder why you're my perfect assistant!"
    s "Let's goooo!"
    scene black with dissolve
    pause
    "" "You filmed [sn] showing exercises you can do in your room."
    "" "She looked so pretty... You had a half boner."
    scene 018sarsurlit with dissolve
    play music chillsexy
    s "Fiou! That was intense!"
    s "Sports in rooms was a great idea but I still hope they could access a balcony or a garden to get fresh air."
    mc "Yeah, I guess some people that live in a small house with their families can only do that in their room."
    mc "I hope everyone is fine."
    pause
    s "?"
    mc "??"
    s "What are you waiting for?"
    mc "What do you mean?"
    s "Pull out your dick!"
    mc "All of sudden?!"
    s "Of course! Why are you surprised? I always play with it when the work is done!"
    mcth "Great lord..."
    mcth "Sarena really got an addiction! Well, that's not as if it was a problem."
    mcth "However..."
    mc "No."
    s "No?! You meant YES SARENA!"
    mc "It's always you touching me. That's not fair."
    s "That's alright for me, I like that!"
    mc "This is not what I meant, I want-"
    scene 018sarfj with dissolve
    pause
    s "[mc]?!"
    mcth "You were touching yourself thinking of me, I know you wish me to touch you."
    mc "You said you enjoy touching me, but what if I would enjoy touching you the same way?"
    mc "It's the same thing, so you have no reason to refuse, right?"
    s "You-you want to touch me right there??"
    mc "Of course! I want to treat you the same way!"
    s "Are you sure of th-"
    window hide
    play audio emoansingle
    show 018sarfj2 with dissolve
    pause
    window auto
    s "D-don't look!!"
    mc "Why?"
    mc "You look at mine all the time!"
    s "It's different, your penis is so good-looking!"
    mc "[sn]... Your vulva looks so good as well!"
    s "R-really?"
    mc "It looks perfect for me."
    s "S-so... Can you touch it? Please..."
    mcth "I was initiating it, and now she asks me?"
    mcth "The [sn] I know is always full of confidence, but on this field, it's the opposite."
    mcth "I want to give her confidence like she gave it to me. I owe her so much."
    window hide
    scene black
    show 018devfj
    stop music
    play sex ssoftmoans2
    play sexfx frottements
    pause
    window auto
    s "[mc]!"
    s "I'm so surprised!"
    mc "Surprised?"
    s "I didn't expect you to be this good!"
    s "Oh my!!!"
    mc "[sn], you look so good when you're having pleasure!"
    s "Don't talk to me like that, Or-"
    mc "Or?"
    s "Grouuh!! Or..."
    s "Or..."
    s "What's happening to me?!!"
    mc "Are you okay?"
    s "I didn't feel this with my girlfriend!!"
    mc "This?"
    s "Yeah, I feel like- like- RHAAAAA!"
    mc "?!"
    call incrskill ("handskill", 1) from _call_incrskill_40
    s "GIVE ME YOUR FACE!"
    if firstcunto == "None":
        $ firstcunto = "Sarena"
    hide rep018devfj
    window hide
    show 018devcun
    stop music
    play sex shardmoans1
    play sexfx frottements2
    pause
    window auto
    s "I can't control myself!!!"
    s "RHAA I want you to lick my pussy so bad!!!"
    "" "Tongue's skill lv 15 required."
    s "I wanna cum on your cute little face!!!"
    s "I'm so sorry [mc], I- I-"
    s "Your mouth feels too good I feel like I'm gonna explode!!!!"
    s "What am I even doing?! It's so good I NEED YOU!!!"
    s "I want to fuck your face so hard!!"
    s "Just one time, just let me cu-"
    stop sexfx
    stop sex
    hide 018devcun
    show 018devcuncum at cumtr
    show cumanim
    play audio scum2
    pause
    window auto
    $ scum += 1
    s "Yiiiiiiii!!!!"
    s "Your face is too goooood! I just came!!"
    s "I just came on your sweet face!!!"
    scene black with dissolve
    pause
    scene bg doubleroom with hpunch
    show sarena o2 shocked at right
    show mc humidface shy o1b at left
    call incrskill ("tongueskill", 2) from _call_incrskill_41
    s "What have I done???!!!"
    s "Oh my god, oh my god, oh my god, what happened??!"
    mc "Sar-"
    s "Did I hurt you [mc]?! I don't understand!!"
    mc "You didn't."
    s "I feel like a monster!! [mc], if from now on you'd hate me, then I-"
    mc "What are you talking about?"
    s "Considering what I have just-"
    mc "I loved it."
    show sarena shy
    s "Loved?!"
    mc "I was a bit surprised but enjoyed it a lot!"
    s "I- I- I don't know what to say..."
    mc "I want to do that more often!"
    s "More?!"
    mc "I want to see you like this again! I didn't know this side of you existed!"
    s "I didn't either..."
    s "I'm a bit confused right now..."
    s "I'm surprised you reacted this way, I really thought you would hate me, it was like a r-"
    mc "Don't worry [sn], you know me. Deep inside of you, I'm sure you did it because you knew I'd want it."
    s "Wh-"
    s "... I need some time to think about that..."
    s "If you're good with it, then at least I don't have to worry about our relationship."
    s "But considering me... I didn't feel that even with my-"
    show sarena sad
    pause
    s "Oh..."
    mc "Are you okay?"
    s "Thanks [mc], whenever I think I might lose you, you prove me wrong! Thank you, really."
    mc "You can count on me!"
    scene black with dissolve
    pause
    $ slv = 11
    jump passtime
    return
label devsp12:
    scene bg kitchen
    play music sand_castle
    show berry:
        xalign 0.0
        xzoom -1
    show sarena shy at right
    s "So what do you think of that?"
    b "That's nothing, don't worry, my love."
    s "But doesn't it sound weird? I swear it was as if I wanted to devour his soul!"
    s "I felt like a beast with unlimited hunger! It scares me!"
    show berry ordering
    b "\"Him?\""
    show sarena sad
    s "I mean \"her\", it was with my girlfriend, eh-,eh-"
    show berry base
    b "My love... Actually, I know what happened."
    show sarena base
    s "Really??! How do I get rid of that?"
    b "You can't."
    s "Oooh!"
    b "This is something... That I've got as well..."
    b "I didn't know you could inherit that, but it seems like it."
    s "What's that?"
    b "Hm, how to explain..."
    b "It can happen with people who are very special to you."
    b "Our Sex drive is normal, but sometimes, our brain falls for a specific person and then our sex drive explodes for this person."
    b "It explodes so much that you could even lose control and become like a beast."
    show sarena shocked
    s "Oh my god! can It happen to anyone?"
    b "No, he or she - must be extraordinary for us."
    b "You must be so close to your girlfriend if it woke \"it\" up."
    show sarena sad
    s "Yeah... I think I couldn't live without \"her\"..."
    b "Just beware of one thing."
    b "If the person doesn't accept this part of you, don't continue your adventure. Don't make the same mistake as me."
    show sarena base
    s "... Are you talking about Dad?!"
    b "Yes, He never really accepted my sex drive and-"
    show sarena shocked
    s "Baaaaaark I don't want to hear that kind of thing between you and Dad!"
    b "Moh! It's natural, how do you think you came into this world!"
    s "I just became deaf. I don't hear anything!!"
    show berry happy
    b "Haha!"
    b "Just remember what I told you, she will have to accept this part of you or you won't end up happy or satisfied in the long term."
    show sarena base
    s "I get it."
    s "Actually, I think he- I mean she - would accept this part of me."
    b "Great! Then I'll be happy for my child!"
    scene black with dissolve
    pause
    $ slv = 12
    jump passtime

label devsp13:
    scene black
    stop music
    mc "Oh [sn]..."
    mc "I want you so bad..."
    window hide
    $ persistent.replay21 = True
    show 018dreamsex with dissolve
    show dream with dissolve
    $ persistent.replay20 = True
    stop music
    play sex ssoftmoans2
    play sexfx frottements
    pause
    window auto
    s "Oooh [mc] let me ride you!!"
    s "I never told you this but I have loved you since the very beginning!!"
    s "I have been dreaming of riding you for years!!"
    s "You could get your confidence back because of me!"
    s "You are happy because of me!"
    s "You owe it to me! Then for that... You will have to fuck me like this EVERY-DAY!"
    mc "Everything for you [sn]!!"
    s "Yeah! From now on, your dick will be my personal toy, I can use it whenever I want!!"
    mc "Oh [sn], I'm about to cum!"
    s "Me too!!"
    scene bg mcroom
    stop sex
    stop sexfx
    show mc ocaleconerect surprised at right
    show sarena shy o4 at right
    show mc at left with hpunch
    play music chillsexy
    mc "Aaaah!"
    s "[mc]?!"
    mc "[sn] What are you doing here?"
    s "Er, I was about to wake you up, then I heard your... moans... I thought you were masturbating without me."
    show sarena taunt
    s "As I can see, you just had a wet dream!"
    show mc base
    mc "Er yeah, kind of."
    show sarena:
        linear 2.0 xalign 0.5
    s "So..."
    s "I hope the girl in your dream wasn't as good as me for..."
    show mc shy
    mc "Stop!"
    show sarena shy
    s "Stop?"
    mc "This isn't enough!"
    s "?!"
    mc "Yeah, handjob is good but... It's... also frustrating! Not getting more!"
    s "More?!"
    mc "Yes, maybe you could use- your- mouth?"
    show sarena behind mc:
        linear 2.0 xalign 0.35
    s "You want me to suck your dick?"
    mc "I mean... Only if you want to."
    s "I can't do that! Imagine I hurt you!!"
    mc "Hurt me?!"
    s "Imagine I get crazy and-"
    hide sarena with hpunch
    mc "[sn]!"
    mc "Oh shit, was it too soon?"
    mc "Is she mad at me?"
    mc "She didn't look mad, I need to find out what she really thought of that."

    scene black with dissolve
    pause
    $ slv = 13
    jump passtime
    return

label devsp14:
    scene bg firstfloor talk
    show mc at left
    show sarena at right
    play music robot_boogie
    s "Whoops sorry [mc]!"
    mc "Hey [sn], you just got out of the computer?"
    s "Yes! I had some searches to do... for a potential project. It's alright I've finished, you can go!"
    hide sarena with dissolve
    pause
    mc "She looks delighted! I wonder why? What's that project?"
    mc "I want to try something I shouldn't..."
    scene bg pcroom with fade
    mc "let's see her search history..."
    show bg pcroom at angryjump
    pause
    mc "WHAT?!!"
    mc "Is it for real??!"
    mc "She taped on Gougeule:"
    mc "\"How to be sure if I'm lesbian?\""
    mc "I'm now pretty sure you're not."
    mc "\"Can a blowjob destroy friendship?\""
    mc "She was probably willing to do it but was afraid of repercussions."
    mc "\"How to make a man lose his mind with a blowjob?\""
    mc "Holy shit!"
    mc "\"How to suck a huge penis?\""
    mc "\"How to suck a man without hurting him?\""
    mc "\"How many times can a man ejaculate?\""
    mc "And many others like that..."
    mc "[sn] seems very interested in this!"
    mc "So wait, when she talked about her project..."
    mc "Great lord..."
    mc "I must not tell her I know!!"
    mc "[sn] is the greatest [ssn] ever!!!"

    scene black with dissolve
    pause
    $ slv = 14
    jump passtime
    return

label devsp15:
    scene bg living1
    show sarena o1a sad
    play music papapalapa
    s "Why??"
    s "So you hate [mc] just because he's a man?"
    s "Isn't that a bit sexist?"
    s "Why is it different?"
    s "..."
    s "Nooo I'm not ashamed to be friends with a man!!"
    s "I don't want to talk about [mc] anymore."
    s "Ah?"
    s "What does your neighbor girl has to do with-"
    s "Are you joking?!"
    s "Just trying to make me jealous?"
    s "Actually, you just make me sad. You always do that. Even before the quarantine."
    s "I'm starting to get tired of always arguing with you, at least, [mc] always gives me good vibes."
    s "Even if it would be to make you jealous, you just did the same th-"
    pause
    s "...My mom is calling for me. Call you later."
    show sarena sad o1 with dissolve
    pause
    show sarena at right
    show mc at left
    mc "Is she mad at you again?"
    s "Yeah... It's starting to get on my nerves."
    mc "May I ask you why you got together at first?"
    s "She wasn't like this when we first met."
    s "She was very affectionate with me, you know how much I love affection!"
    s "I was a bit disturbed when we started to touch each other, I thought she was just shy but I think it's just not her thing."
    s "I knew she hated men, I'm also starting to think she insisted on me saying I'm lesbian because she couldn't accept I could like a man."
    mc "So, you're not?"
    s "I don't know... I've never been with a man, but, I've got some compulsions that aren't very lesbian..."
    mc "Such as??"
    show sarena base
    s "You really want to know hah? It's a secret!!"
    show sarena sad
    pause
    s "She always blames me because of my sex drive... I feel like I'm not normal..."
    mc "You don't have to worry about your sex drive, every body is different, it's part of you and you should be proud of it!"
    mc "You should find someone that wants you as you are."
    pause
    show sarena happy
    s "That's funny, it's the same thing Mom told me!"
    s "You are the best relationship I have, you know?"
    s "You're not disgusted by me having a high sex drive, are you?"
    show mc shy
    mc "Oh- er- it's alright for me-"
    s "Heheh you're cute, come here!"
    show shugliving with dissolve
    s "You're so important to me, I need you in my life."
    s "I want you to be happy so bad."
    s "There is something that I have wanted to do for a while now. I think I'm gonna do it."
    mc "What do you want to do?"
    s "Hm... You'll know about that later."
    mc "O-Okay."

    scene black with dissolve
    pause
    $ slv = 15
    jump passtime
    return

label devsp16:
    scene black
    stop music
    "" "You return to your room, however it looks like someone was waiting for you..."
    window hide
    play music causmic
    show 018sarshot:
        yalign 1.0
        xalign 0.5
    pause
    window auto
    mc "Ah? Someone is in my room."
    window hide
    show 018sarshot:
        ease 4.0 yalign 0.45
    pause
    window auto
    mc "Oh my gosh!"
    mcth "This booty looks incredible!!"
    window hide
    show 018sarshot:
        ease 4.0 yalign 0.0
    pause
    window auto
    s "So you're finally here, at last."
    mc "Ouaw [sn], you look so amazing!!"
    s "I was waiting for you."
    window hide
    scene 018sarshot with dissolve:
        xalign 0.5
        yalign 0.5
        xzoom 0.3333
        yzoom 0.3333
    pause
    window auto
    s "Do you like my outfit?"
    mc "Great lord, you're so sexy!!!"
    s "Do you think that is for real, or is it just to be polite?"
    mc "I mean-"
    scene bgmcroom evening
    show mc shy o1a at left
    show sarena onighty at right
    show black
    hide black with dissolve
    pause
    s "It's true, Men can't lie when they get aroused haha!"
    mc "I'm sorry [sn]-"
    s "No, that's perfect, that's what I wanted."
    mc "What you wanted?"
    show sarena taunt
    s "Get naked."
    mc "Wh-"
    s "Get naked."
    show mc o0a
    pause
    show sarena happy
    s "Good boy."
    show sarena base
    s "Now, on the bed."
    mc "Yes!"
    scene 018prebj with dissolve
    s "You obeyed so fast! Do you enjoy it when I give you orders?"
    mc "Er- is it bad? I mean, I know you would never order me to do something I shouldn't."
    s "Nah, in fact, I like that."
    mc "Will you give me a hand job?"
    pause
    s "Do you have faith in me?"
    mc "Of course!"
    s "To what extent?"
    mc "I could give you my life!"
    s "So... If I ask you to give me your body?"
    s "What if I want you to give me free access to your body?"
    s "Even though we shouldn't?"
    mc "You're treating me so much better than [zon], I'd give you anything!"
    s "Speaking of her, you told me she never gave you a blowjob, right?"
    mc "Right."
    s "You know it but I've never done such a thing."
    s "Let's make a deal."
    s "If I can make you cum, then I'll become an owner of your penis."
    s "I want free access to it, for life, and you couldn't refuse it anymore."
    mc "...I accept the bet!"
    mcth "The first time she jerked me off, [sn] showed a such talent for her first time!"
    mcth "I bet her mouth won't be any different!"
    s "Just be prepared."
    s "You've been so gentle with me, it makes me so starving for you!!"
    window hide
    pause
    show 018bjdev with dissolve
    stop music
    play sex sbjsoft
    pause
    window auto
    mc "GREAT LORD!!!"
    mc "This feeling is incredible!!!"
    if firstbjby == "None":
        mc "It's the first time someone has done this to me, I'm so happy it's you!"
        $ firstbjby = "Sarena"
    s "!"
    mc "This is sooooo incredible!"
    mc "I can feel how soft your lips are, and how your tongue's tip plays with my glans!"
    mc "And you're sucking so HARD!!"
    mc "I feel like you're about to take out my soul!!"
    pause
    "" "[sn] reacted to this sentence and looked at your eyes very intensely!"
    mcth "Don't tell me it's exactly what she wa-"
    window hide
    hide 018bjdev
    show 018bjdevcum
    pause sp018bjdev*7
    show cumanim
    stop sexfx
    stop sex
    play audio sbjcum
    play audio cumexplo
    play audio cumsoundext
    pause
    window auto
    "" "[sn] is swallowing your cum in her mouth."
    s "That's so delicious... Even more when I get it directly from the source..."
    mc "Oh my gosh... [sn], that was incredible..."
    s "Was?"
    s "I'm not done yet."
    s "You came, so your penis is now mine."
    s "And it is now even tastier with your delicious cum... I want more!!"
    window hide
    $ persistent.replay16 = True
    show 018bjdev2a
    show 018bjdev2b
    play sex sbjhard
    pause
    window auto
    mc "Oh my god!!!"
    mc "Just- just slow down, it's too sensitive after ejaculating!!"
    mc "Oh my-"
    mc "You're making me crazy!!"
    s "Mh!"
    mcth "My [ssn] is killing me by an overdose of Blowjob, I can die happy..."
    scene black with dissolve
    stop sex
    stop sexfx
    "" "She continued to suck you until your balls were completely empty..."
    scene 018end with dissolve
    pause
    s "Are you alright? Hehehe!"
    mc "I saw death... But I'm still alive..."
    s "Perfect! I can continue then!"
    mc "Er-"
    s "I'm kidding haha! My jaw is completely congested I can't continue either."
    s "It's a hard exercise, you know! But I love this so bad!!"
    mc "I could see that... I'm happy that I helped you discover something you like."
    s "Will you keep your promise?"
    mc "Yes, my body is yours, you can do whatever you want, it's your play toy."
    s "Isn't it demeaning to talk about yourself like that?"
    mc "It isn't, if I'm sure you'll treat me well."
    s "It's funny that you use the word \"toy\"."
    mc "Why?"
    s "Oh er because it's exactly what I-"
    s "Hm, never mind."
    s "Now we should sleep."
    mc "Sleep well [sn]."
    s "Have sweet dreams [mc], and thank you, a lot, for being you..."
    "" "All events have been upgraded to Step 2!"
    scene black with dissolve
    call incrskill ("cockskill", 3) from _call_incrskill_42
    $ cumbys += 5
    show levelupf with dissolve
    play audio bmiam
    pause
    hide levelupf with dissolve
    pause
    $ slv = 16
    $ sstep = 2
    $ day +=1
    $ daytimenumber = 0
    $ bpos = positionsb[daytimenumber]
    $ spos = positionss[daytimenumber]
    $ vpos = positionsv[daytimenumber]
    $ epos = positionse[daytimenumber]
    play music sunny_day
    jump passnightnothing
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
