screen backyard:
    imagemap:
        if daytimenumber > 2:
            ground night("House/backyard/bgbackyard.webp")
        else:
            ground "House/backyard/bgbackyard.webp"
        if bpos == "backyard":
            imagebutton:
                idle "House/backyard/backyardb.webp"
                hover lumi("House/backyard/backyardb.webp")
                focus_mask True
                action Jump("byactionb")
        if vpos == "backyard":
            imagebutton:
                idle "House/backyard/backyardv.webp"
                hover lumi("House/backyard/backyardv.webp")
                focus_mask True
                action Jump("byactionv")
        if epos == "backyard":
            imagebutton:
                idle "House/backyard/backyarde.webp"
                hover lumi("House/backyard/backyarde.webp")
                focus_mask True
                action Jump("byactione")
        if spos == "backyard":
            imagebutton:
                idle night("House/backyard/backyards.webp")
                hover lumi("House/backyard/backyards.webp")
                focus_mask True
                action Jump("byactions")
        if daytimenumber == 1:
            if bstep > 0 or sstep > 0 or estep > 0 or vstep > 0:
                imagebutton:
                    idle "House/backyard/bg backyard jaccwith.webp"
                    hover lumi("House/backyard/bg backyard jaccwith.webp")
                    focus_mask True
                    action Jump("jacuzzi")
        add "nuages"
        add "sunvary"
image nuages:
    ifnight("House/backyard/nuages.webp")
    xalign 0.0 yalign 0.0
    linear 15.0 xalign 1.0 yalign 1.0
    repeat

image sunvary:
    ifnight("House/backyard/sunvary.webp")
    linear 2.0 alpha 0.2
    linear 1.0 alpha 1.0
    easein 1.0 alpha 0.5
    linear 2.0 alpha 1.0
    repeat

label jacc:

    "" "This feature is ready to be used on the next udpate."
    jump tobackyard


label byactions:
    scene expression ifnight("House/backyard/bgbackyard.webp")
    show expression ifnight("House/backyard/backyards.webp")
    menu:
        "What to do?"
        "{color=#ff9a40}I have something to tell you...{/color}" if slv == 18 and sdesire >= desireforstep3:
            jump devsp19
        "Talk to [sn] ([sstep])" if True:
            jump bytalks
        "Observe her" if True:
            jump bysobserve
        "{color=#c1a63a}Try to Surprise her!{/color}" if sstep > 0:
            jump sarstep1by
        "{color=#c1803a}Put her bottom aside and look at her pussy.{/color}" if sstep > 1:
            $ persistent.replay18 = True
            jump byscuni
        "{color=#c13a3a}Be ready to get fucked!{/color}" if sstep > 2:
            $ persistent.replay52 = True
            call showscene ("024bypre") from _call_showscene_95
            s "Hehehe!"
            pause
            s "He thinks I don't see him staring at my butt... How cute!"
            s "He really is a naughty boy..."
            s "Looking at a woman with such a lust..."
            s "I have to punish him right now!"
            pause
            scene black with dissolve
            pause
            call ssexby10 (1.0/12) from _call_ssexby10_2
            s "Hoooh!"
            mc "Oh [sn]!"
            s "You were thinking of that, naughty pony!"
            mc "Oh yeah! You're looking so hot and sexy!"
            call ssexby10 (1.0/24) from _call_ssexby10_3
            s "I will make you cum!"
            mc "Oh [sn] make me cum!"
            mc "Your booty is the sexiest I've ever seen!"
            call ssexbycum10 from _call_ssexbycum10_1
            call incrskill ("cockskill", 3) from _call_incrskill_24
            call incrdesire ("Sarena", cockskill) from _call_incrdesire_14
            $ cumbys+=1
            s "Yeaaaaah"
            pause
            jump passtime
        "Step back." if True:
            jump tobackyard
label byactionb:
    scene bgbackyard
    show backyardb
    menu:
        "What to do?"
        "Talk to [bn] ([bstep])" if True:
            jump bytalkb
        "{color=#c1a63a}Compliment her.{/color}" if bstep > 0:
            jump bybnipplesuck
        "Observe her" if True:
            jump bybobserve
        "{color=#c1803a}Be a good boy and let her play with your mouth.{/color}" if bstep > 1:
            $ persistent.replay36 = True
            jump bybcuni
        "{color=#c13a3a}Kiss her and make love.{/color}" if bstep >2:
            $ persistent.replay89 = True
            jump evbersexby
        "Step back." if True:
            jump tobackyard
label byactione:
    scene bgbackyard
    show backyarde
    menu:
        "What to do?"
        "Talk to [en] ([estep])" if True:
            jump bytalke
        "Observe her" if True:
            jump byeobserve
        "{color=#c1a63a}Spank! [en]{/color}" if estep > 0:
            jump byespank
        "{color=#c1803a}Licking [en]'s pussy by surprise!{/color}" if estep > 1:
            jump byelick
        "{color=#c13a3a}Listen to her.{/color}" if elv == 6:
            jump devep7
        "{color=#c13a3a}Try to fuck her while she's Live{/color}" if estep >2:
            $ persistent.replay95 = True
            jump emmsexby
        "Step back." if True:
            jump tobackyard
label byactionv:
    scene bgbackyard
    show backyardv
    menu:
        "What to do?"
        "Talk to [vn] ([vstep])" if True:
            jump bytalkv
        "Observe her" if True:
            jump byvobserve
        "{color=#ff9a40}Finger job.{/color}" if vlv == 6:
            $ persistent.replay57 = True
            jump devvp7
        "{color=#c1a63a}Finger job.{/color}" if vstep > 0:
            $ persistent.replay57 = True
            jump byvfingerjob
        "{color=#c1803a}Lick her pussy by surprise.{/color}" if vstep >1:
            jump byvcuni
        "{color=#c13a3a}Fuck by surprise.{/color}" if vstep >2:
            $ persistent.replay73 = True
            jump valsexby
        "{color=#ff9a40}Compliment her. (Quest){/color}" if vlv == 20:
            jump devvp21
        "Step back." if True:
            jump tobackyard


label bytalks:
    scene expression ifnight("House/backyard/bytalk.webp")
    show mc at left
    show sarena o3 at right
    menu:
        "What do you say?"
        "{color=#ff9a40}Ask her about the video's feedback.{/color}" if slv == 3:
            mc "So, is the feedback good?"
            jump devsp4
        "Hey [sn]! How're you doin'?" if True:
            if sstep == 0:
                s "Hey! I'm just chilling on my phone, relaxing time you know."
                pause
                mc "I like your bikini."
                s "Hoho, you're cute, thank you!"
                mc "But... Isn't it... like, a little small?"
                s "Yeah, I got it years ago but got busier since then..."
                mc "I see..."
                s "Do you think I should buy a new one?"
                mc "Oh no, this one looks im-pe-cable!"
                s "Oh really? Don't tell me you like seeing your [ssn] wearing undersized clothes..."
                mc "Who, me? Never! I swear to god!"
                s "You little liar! You'll see when I get my revenge haha!"
            elif sstep == 1:
                s "Looking at a few new comments!"
                s "That's so funny how many of them are shipping us!"
                s "And you? What are you doing?"
                mc "Nothing special, just chilling."
                s "Just chilling? Are you sure you weren't looking at your [ssn]'s butt?! haha! "
                mc "No! Or, well, maybe a little bit..."
                s "I knew it, little pervert!!"
                s "But it's okay if it's you."
                mc "Hehe!"
                mcth "[sn] is not disturbed by the idea of me desiring her body."
            elif sstep == 2:
                show sarena sad
                s "Arguing with my girlfriend by messages."
                mc "Again..."
                s "Yeah..."
                show sarena happy
                s "But your visit makes me feel happy, so that will compensate!"
                s "I wasn't holding this pose for nothing!"
                mc "You said?"
                s "Nothing hehehe!"
            elif sstep >2:
                show sarena taunt
                s "Daaaaamn Look at this hot male body!"
                mc "Oh eh eh, thanks!"
                s "Just looking at you makes me so horny!"
                s "Grrr!"


    jump tobackyard
    return


label bytalkb:
    scene bytalk
    show mc at left
    show berry o3 at right
    if bstep == 0:
        b "Hey sweety, did you come to see [bsn]? So cute!"
        mc "Oh wouah..."
        b " Wh-what? Why are you staring at my chest?"
        mc "Eh, nothing, I thought I saw a bug, never mind."
        b "A bug? What kind of excuse is that? Do you think you can trick me with that? haha!"
        mc "I'm sorry [bn], it's just that..."
        b "You are in love with your [bsn]'s bikini, aren't you?"
        mcth "It's really revealing!! But I guess we aren't in a public place, so she doesn't care?"
        mc "She looks so pretty..."
        b "She looks so pretty?"
        mc "Whoops! I think I said that out loud..."
        b "Oh really? Then why don't you want to tell that to me?"
        mc "I..."
        b "Say it."
        mc "You... You are so pretty, [bn]."
        b "Haaah! That's a good boy!"
        b "Continue to be that sweet with your [bsn] and one day you'll get rewarded hehehe!"
    elif bstep == 1:
        b "Hey, my sugar, how are you today?"
        mc "Doing great."
        show berry tease
        b "Doing great looking at my chest?"
        show mc surprised
        mc "N-no, I wasn't!"
        b "You don't have to hide anymore, they're for you when we're alone, remember?"
        mc "Y-yeah!"
        mcth "I'm sooo luckkyyyyyy!"
    elif bstep == 2:
        b "You look hungry, don't you?"
        mc "Hm, not really, why?"
        b "I'm just checking if my sweety needs anything."
        show mc shy
        mc "Oh, so adorable!"
    elif bstep >2:
        b "My lovely candy looks so handsome, as always!"
        mc "Thank you, [bn]!"
        show berry lewd
        b "Handsome.. and... delicious."
        b "Why did you make me so horny?!"
        show mc shy
        mc "I- I didn't do anything!"
        b "I'm gonna fuck you the double amount next time!"
        mc "Oh, yes, haha!"

    jump tobackyard
    return

label bytalke:
    scene bytalk
    show mc at left
    show emma o2 at right
    if estep == 0:
        mc "Hey [en]! How are you?"
        e "Why are you talking to me? I'm BUSY!"
        mc "Busy? but you're just on your phone!"
        e "I'm always busy when it comes to talking with you."
        mc "... I just wanted to tell you that you're pretty but I won't then."
        e "As if I care to know you're craving for my body!"
        mc "Hey I never said that!"
        e "I can smell your pre-cum from there, don't lie!"
        mc "Oh so you seem to be an expert on these things?"
        e "..."
        e "Just leave me alone!"
    if estep == 1:
        mc "How is my good girl going?"
        show emma angry
        e "Stop calling me like this!"
        mc "The same way I want you to stop calling me a loser."
        e "But you're a loser, looooooser!"
        mc "A loser that made you cu-"
        show emma angryshy
        e "Don't even dare to finish this sentence!"
        e "Just leave me alone!"
    if estep == 2:
        mc "How is my good girl going?"
        e "Just chilling with my followers hehehe!"
        e "They loooooved the photos you took! Some told me how lucky I am."
        show emma smirk
        e "But they don't realize you're the lucky one to get me as a model haha!"
    if estep > 2:
        show emma happy
        e "Hehehe!"
        e "[mc] is looking at my butt again!"
        mc "I mean, you're so hot!"
        e "This is for [mc] and only for him!"
        mcth "Oh gosh, she's so cute..."
    jump tobackyard
    return

label bytalkv:
    scene bytalk
    show mc at left
    show valerie o4 at right
    if vstep == 0:
        v "It seems the little boy is peeping on his [vsn]..."
        v "Imagine how girls would react if I tell them..."
        mc "Haha, you really thought I wanted to look at you?"
        mcth "Oh shit!! I have to lie to her, but still, this bikini looks so small!"
        mcth "[vn] is a fucking bitch but... Her body looks so tasty..."
        v "Now stop wasting my time. I have to finish something."
        mc "I didn't intend to stay with you."
        jump tobackyard
    elif vstep == 1:
        show valerie mad
        v "Do you intend to touch me again?"
        show mc lol
        mc "I mean, do you expect me to do so?"
        v "Me?! NOT AT ALL."
        v "Leave me alone."
        jump tobackyard
    elif vstep == 2:
        show valerie happy
        v "Imagining you're fucking me? Huh?"
        mc "Why would I?"
        v "C'mon don't lie, you're dreaming of pounding that pussy!"
        jump tobackyard
    elif vstep >2:
        show valerie happy
        v "I'm so horny!!!"
        mc "Looks like it."
        v "When are you fucking me???!"
        mc "Why would I?"
        v "[mc]!! Don't be so naughty and help a woman in need..."
        jump tobackyard
    jump tobackyard
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
