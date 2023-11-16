label roaemmaend:
    show prefin2b
    mc "[en], are you okay?"
    e "Those bitches!"
    e "They want to steal you from me!"
    e "They want to steal my precious!"
    e "I won't let them get away with it!"
    e "I've been in love with you for so fucking long..."
    e "I've been hiding it all these years ..."
    e "Today I am free to tell them..."
    e "I could experience such intense intimacy with the man I love..."
    e "I will never go back."
    e "I will do everything I can."
    e "Mom was the first to put her hands on you."
    e "I'm sure this degenerate woman already had dirty plans for you, back then."
    e "I'm sure that even when you were younger, she was already dreaming of fucking you, that freak!"
    e "She always had the upper hand on you, I know it."
    e "She knows it."
    e "She may have the experience, but my will is unwavering."
    e "[sn] ..."
    e "She had your attention when I was trying to get yours..."
    e "I don't know if I blame her yet."
    e "In the end, she brought you joy and comfort."
    e "She brought you happiness, I thank her, but it should have been me."
    e "I wish I dared to do what she did."
    e "[vn] ..."
    e "I don't have anything against her, except for how she behaved to you a while ago, I feel like those days are over, so everything seems to be fine."
    e "She's really friendly to me, and is always eager to teach me."
    e "I just hope her experience doesn't catch your heart."
    e "I'll be giving it everything..."
    window hide
    show prefin2c with fade
    pause
    window auto
    e "[mc] ..."
    e "I love you."
    e "I love you like crazy."
    e "I love you, I love you, I love you!"
    e "I intend to do everything to get married to you!"
    e "No matter what you may already think or not I'll make sure you can't live without your love."
    e "Oh, [mc] ..."
    e "I can feel you getting hard..."
    e "This is not the time for that, I have to prepare for tonight."
    e "I'm gonna show all these bitches who's the one that deserves to marry you."
    e "Oh, [mc] ..."
    e "I want to fuck you like crazy, right now."
    e "Wait for me in the living room, my love."
    e "I'll show them who the real girlfriend is."
    $ eendvisit = True
    if eendvisit == True and bendvisit == True and vendvisit == True and sendvisit == True:
        scene black with dissolve
        pause
        "" "It's time."
        "" "You're heading to the livingroom."
        jump endp2
    jump togirlsroom
    return

label roasarenaend:
    show prefin1
    s "The night sky is beautiful..."
    mc "Just like you"
    s "..."
    s "Haha! Haha!"
    s "What movie did you hear that line in?"
    s "You are so crazy!"
    s "..."
    s "Thank you, [mc]."
    s "You know, sometimes I wonder what my fate will be."
    s "Am I destined to be happy?"
    s "Am I destined to have you in my life?"
    s "The more I think about it, the more I tell myself that fate is just the consequence of your actions."
    s "The moon, so gorgeous, doesn't need to worry about her choices or her fate."
    s "She is simply observing this world and watching over us, reminding us every time we see her that time is passing."
    s "Deep down, I feel that the two of us are meant to be together until the very end."
    s "I feel it deep in my soul, yet I still have this slight concern in the back of my mind that says what if we are wrong?"
    s "What if, it's not about being wrong, but rather about doing the right things to keep it real."
    s "I'm going to make it real."
    s "I'm going to get it just right. But it is true that it will be difficult if the other three are in love with you."
    s "[vn], I know how she used to treat you, yet by now, I've seen how much your relationship has changed."
    s "She is still provocative, but nothing malicious."
    s "You've managed to make her crave you..."
    s "You could say it's a kind of payback. Haha!"
    s "I also feel like she lusts after me almost as much as you do when she stares at me..."
    s "She's really hot, I'm not surprised that she has quite an effect on you!"
    s "[en] ..."
    s "She's been talking to you badly for years ..."
    s "I always thought it was odd ..."
    s "Now that I think about it, now that she has declared her feelings for you, I can understand it better ..."
    s "All this time she was just jealous of our proximity..."
    s "On the other hand, if she fell in love with you, it's because she was able to see the person you were, maybe even before me before we started talking."
    s "It would be painful for me to take you away from her... She's still my little sister I want her to be happy."
    s "And finally, mom..."
    s "She was the first one to be close to you despite the age gap."
    s "You have always been very close, much more intimate than a student and a teacher should have been."
    s "I always found it strange the way she looked at you, she had a protective look on her face most of the time, but from time to time such a lustful and perverse gaze ..."
    s "I knew it for a long time, the craving she had for you..."
    s "I just figured I was wrong, or at least I chose to ignore it."
    s "Now she talks about it openly, on the other hand I think she seems to have broken free from her moral chains."
    s "She seems to be feeling better about what she wants, so maybe that's a good thing."
    s "I don't think she realizes the power she has over you, I know what she represents to you, I know that you obey her blindly."
    s "However, I am scared that she will lock you up in a cage."
    s "You deserve all the love in the world, but you also deserve to be free."
    window hide
    show prefin1b with fade
    play sex skiss
    pause
    window auto
    s "Oh, [mc]!"
    s "I love you so much!"
    s "I could never live without you around!"
    s "I will fight for you."
    s "Oh, [mc]!"
    s "We have to stop kissing!"
    s "I'm getting wet..."
    s "I want you to penetrate me now!"
    s "I want to feel that unique connection, that energy that flows between us as we make love..."
    s "[mc]!"
    s "If we don't stop in a second, I feel like I'm going to lose control and throw myself at you and fuck you like a demoness!"
    s "Go, go, I have to get ready."
    s "I'm going to show those three soul thieves that they're nothing compared to our bond."
    s "I love you so much [mc] ..."
    stop sex
    $ sendvisit = True
    if eendvisit == True and bendvisit == True and vendvisit == True and sendvisit == True:
        scene black with dissolve
        pause
        "" "It's time."
        "" "You're heading to the livingroom."
        jump endp2
    jump tobalcony
    return

label roaberryend:
    show prefin3
    mc "Um, [bn]?"
    b "They want to take you from me!"
    b "I won't let that happen."
    b "I am the only one with authority to take care of you!"
    b "I will take care of you until the very end of your life and mine!"
    b "I am the only person who can ensure you are safe and happy!"
    b "And you are the only one who can make me feel happy."
    b "The beast is hooked on you. It won't hook on to anybody else."
    b "Are you proud of yourself?"
    b "You got my daughters to fall in love with you!"
    b "As a mother, I want my girls to have the opportunity to find the person they are happiest with."
    b "But now I'm getting it at my expense."
    b "It seems that the one person who could make my daughters happy is also the same person who makes me happy."
    b "Should I trade my daughters' happiness for my own?"
    b "Wouldn't it be highly immoral to take that away from them for the sake of mine?"
    b "Do I want to be moral?"
    b "Couldn't I just make an immoral decision, and then that's it?"
    b "From the very beginning, since we first met, we rapidly spent so much time together outside of class."
    b "I loved it so much when you told me about your days, even if they weren't very joyful days, I loved it so much when you were sharing them with me."
    b "That you shared your emotions and feelings with me."
    b "That I could comfort you."
    b "I loved seeing that smile on your face, when you were having a bad day and you would lean your head on my lap, I could see how secure you felt with me."
    b "I had extremely dirty thoughts even at that time, but I repressed them."
    b "You happened to learn them, didn't make any judgments, didn't moralize me, and didn't tell me that I had to change."
    b "Anyone would consider that I shouldn't be the way I am."
    b "But I think I'd rather have it that way, that I can instead go straight into who I really am and be accepted as such. Moral or not."
    b "[sn], ..."
    b "I was pleased when you guys became close, I was also given the opportunity to spend more time with her thanks to that."
    b "She had already done her coming out to us at that time, I knew that she was officially a lesbian, but when I saw her with you, I had doubts."
    b "She was always overlapping you. There are many male-female friendships, but not as ambiguous as this one."
    b "I realize now that you are the only person who can make her truly happy."
    b "[en], I believe I have not been there for her."
    b "I think I didn't realize enough about her father's absence's impact on her."
    b "I think now that she must have been significantly impacted by the fact that I have given you so much attention, even more than her."
    b "She always looked so angry, I rarely noticed her smile."
    b "I think the only time I've ever seen her smile genuinely was when we were all together and she was looking at you."
    b "Boy, I realize how enamored she is."
    b "And [vn], ..."
    b "I really don't like her. She has been treating you like crap."
    b "On the other hand, somehow, I want you to fuck her, violently."
    b "I feel like this is our vengeance."
    b "Ironically, I don't want any other woman to lay a hand on you, but I want you to bang her to the tears."
    b "I don't want to take away their joy, but I don't want to give you up."
    b "I will never abandon you. Whatever it takes."
    b "I will always be there for you, no matter what."
    b "I don't know what decision I have to make, but I will show them that we are inseparable, that no matter what happens, you will live with me."
    window hide
    show prefin3b with fade
    pause
    window auto
    b "Oh, [mc], you are MINE."
    b "You're already so stiff ..."
    b "I love to see how horny you are when you look at me ..."
    b "Your body is all mine, and your cock is mine."
    b "You belong to me now and forever."
    b "And I will make you the happiest person in the world by providing you all the affection a human cannot give."
    b "You will be loved unconditionally. No one else can give you that but me."
    b "[mc] ..."
    b "I'm already so wet..."
    b "I want to fuck you wildly, right now."
    b "Leave the room, I don't have time for this I have to prepare."
    b "I feel so desired and loved ..."
    b "We'll show them, we will show them all! Our bond is like no other!"
    $ bendvisit = True
    if eendvisit == True and bendvisit == True and vendvisit == True and sendvisit == True:
        scene black with dissolve
        pause
        "" "It's time."
        "" "You're heading to the livingroom."
        jump endp2
    jump toberryroom
    return

label roamvalerieend:
    show fvisitval
    mc "So, stretching?"
    v "I told you, this is going to be extremely intense."
    mc "I'm not sure you're right about that."
    mc "They didn't seem aroused at all but rather lost or angry."
    v "We'll see."
    mc "By the way, do you really intend to compete with them?"
    v "Of course I do!"
    v "You know, I've been having a lot of fun lately in this house."
    v "With you, and the girls, I feel really fulfilled."
    v "If I had treated you better, we might have been even better friends."
    v "But I think that with time the situation could get even better."
    mc "But what exactly do you want?"
    v "What I want..."
    v "Right now, I want to have friends with whom I could do lots of activities."
    v "Especially when those friends are really hot! Haha!"
    v "This [sn], with those huge, muscular and firm thighs..."
    v "I would love to eat her pussy so much and show her that I am a better lover than you."
    v "I'm sure you eat her every day, I'm jealous!"
    v "And then there's the little [en], I love that one!"
    v "I want to teach her everything, especially all the sexual techniques!"
    v "Her body has so much potential, and the lecherous look in her eyes when she sees you doesn't betray her willingness to go as far as possible in learning about sex."
    v "The second she looks at you, you can already feel how much she wants you to fuck her immediately."
    v "And finally, [bn] ..."
    v "She gives off such a dominant energy, she makes me both scared and wet as fuck."
    v "I want to become her thing as much as I am with you."
    v "They are all true goddesses..."
    v "And finally you."
    v "If I expected that the man who made me cum the most in the world was this fragile little man who was afraid of everything only a few years ago..."
    v "Don't think I'm going to let them take you away from me."
    v "I have nothing against sharing you, but if there is only one who must take you then it will be me."
    window hide
    show fvisitval2 with fade
    pause
    window auto
    v "I don't think anyone else can fuck me as good as you can."
    mc "!!"
    v "You know, not all women, but the majority, can develop stronger feelings for a man who makes them orgasm."
    v "Imagine, if one day, you make me fall deeply in love with you! Haha!"
    v "Just imagine..."
    v "Well, go see the other girls, I have to get ready for this moment."
    $ vendvisit = True
    if eendvisit == True and bendvisit == True and vendvisit == True and sendvisit == True:
        scene black with dissolve
        pause
        "" "It's time."
        "" "You're heading to the livingroom."
        jump endp2
    jump tovalerieroom
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
