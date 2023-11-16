label introduction:







    scene black
    play music "Audio/Musics/papapalapa.ogg"


    $ player_name = renpy.input("Hãy nhập tên của bạn? (Mặc định: Ero)")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Ero"
    "" "Đã đặt tên nhân vật của bạn thành [mc]!"

    scene bg intro1 with fade
    show val01 at center
    show val01:
        xoffset 100.0
    show dad01 at right
    show mc_skinny at left
    show val01 at angryjump
    play sound vholyfuck2
    v "Ôi chúa ơi!"
    v "CÁI THẰNG BẤT TÀI!"
    show val01 at angryjump
    v "Thằng khốn kiếp !!!"
    v "Mày lại trộm tiền của tao phải không?!!"
    mcth "Đây là Valerie. Cô ta là bạn của bố tôi. Từ \"bạn\" mà tôi nói ở đây nghĩa là bạn ***** ấy."
    mcth "{i}Từ lần đầu tiên tôi gặp cô ta, thoạt nhìn thì tôi thấy cô ta rất xinh đẹp, nhưng...{/i}"
    mcth "{i}Tôi rất ghét cô ta, cô ta rất đáng khinh.{/i}"
    mcth "{i}Cô ta đã để tiền ở trên mặt bàn và giờ thì cô ta đang vu oan cho tôi vì đã ăn trộm chúng. Tôi chả biết số tiền đó đang ở đâu và cũng chả thèm quan tâm.{/i}"
    mc "Cháu x-x-xin lỗi cô Valerie, c-cháu không lấy gì cả!"
    show val01 at angryjump
    v "Thằng khốn kiếp!"
    show val01:
        linear 0.1 yoffset -100.0 xoffset -50.0
        linear 0.05 xoffset -100.0 yoffset 0.0
        "introvalclaque" with hpunch
        xoffset 0.0

    pause 0.15
    hide mc_skinny
    play sound hit
    window hide
    pause
    window auto
    show val01 at center
    show mc_skinny at left
    v "Mày đáng bị ăn vả vì tội đã nói dối tao!!!"
    show dad01:
        linear 0.1 xoffset -50
    dad "Thôi nào em, đừng đánh con trai anh như vậy!"
    pause
    show dad01:
        linear 0.1 xoffset -200
    dad "[vn], anh muốn nói điều này..."
    dad "Nếu em làm tổn thương thằng bé, chúng ta sẽ gặp rắc rối đó!"
    dad "Thôi nào con, hãy thừa nhận và xin lỗi cô ấy vì đã trộm nó đi."
    mc "G-gì cơ?! Con sẽ không bao giờ xin lỗi nếu con không làm-"
    show dad01:
        linear 0.1 yoffset 100.0 xoffset -150.0
        linear 0.05 xoffset -300.0 yoffset 0.0
        "introdadpunch" with hpunch
        xoffset 0.0 yoffset 0.0

    pause 0.15
    hide mc_skinny
    play sound hit
    "" "PAF!!"
    mc "Urgh!"
    dad "Thấy không, phải làm như thế này thì mới không để lại dấu vết."
    show dad01 at right
    show mc_skinny at left
    v "Tao mong là mày đã nhận được 1 bài học, thằng trộm đần độn!"
    dad "Chắc chắn là vậy rồi. Thôi đừng phí thời gian với nó nữa, anh có món đồ chơi to muốn cho em xem, em yêu!"
    show val01 good at center
    play sound vhah
    v "Oooh, thú vị đấy!"
    v "Và MÀY, đừng có làm phiền bọn tao đấy."
    play sound vbrat
    v "Thằng nhãi ranh!"
    scene black with fade
    "" "Và thế là họ đang cùng quay về phòng..."
    mc "Ghuh..."
    mc "...cô ta tưởng tôi muốn nhìn trộm cô ta chắc..."

    show mcphoto with dissolve
    mc "Đây là tôi của nhiều tháng trước."
    mc "Tên của tôi là [player_name]. Ở thời điểm đó, tôi vẫn đang sống cùng bố tôi. Và [vn] thì luôn vây lấy bố tôi."
    mc "Tôi ghét họ. Tôi ghét họ VL! Tôi không thể chờ đến ngày tôi rời đi và sẽ không bao giờ gặp lại họ nữa."
    mc "Nhưng cho đến lúc đó..."

    scene black with fade
    mc "...tôi vẫn phải hoàn thành việc học của mình."

    scene bg classroomdebut with fade
    mc "Tôi không biết mình sẽ làm gì sau vụ đó. Tôi sẽ sẵn sàng làm mọi thứ chỉ để thoát khỏi đó."
    mc "Tôi sẽ phải chăm chỉ hơn và cố gắng kiên nhẫn."
    mc "Chỉ còn 1 năm nữa thôi. Một năm chịu đựng cái gia đình bị chúa bỏ rơi này. Thêm 1 năm nữa để chịu đựng..."
    play sound hit
    show classroomdebut 4 with vpunch
    "" "Paf!"
    show classroomdebut 1
    play sound zlol
    zon "Cậu đang mơ về điều gì vậy, anh chàng đào hoa?"
    "Học Sinh Khác" "Tớ cá là cậu ấy đang mơ về giáo viên! Mơ làm thú cưng của cô ấy !!!"
    "Học Sinh Khác" "Thú cưng của cô giáo:)"
    show classroomdebut zo
    mc "{i}Đây là [zon]. Cô ấy đã chọc phá tôi nhiều năm nay rồi.{/i}"
    mc "{i}Tôi đã quen cmn rồi nên không thèm để ý nữa."
    mc "{i}Mấy khứa khác hay gọi tôi là thú cưng của cô giáo, bởi vì..."

    scene intro 9 with whiteflash
    mc "{i}[bn]... Cô ấy nhìn quyến rũ vãi nồi!"
    mc "{i}Giữa chúng tôi có một mối quan hệ rất đặc biệt. Cô ấy giúp tôi làm bài, nhưng không chỉ vậy..."
    mc "{i}Chúng tôi cũng nói với nhau mấy chuyện cá nhân. Chủ yếu là toàn nói về cuộc sống thường nhật, rất ít khi nói chuyện về bài giảng hay gì đó tương tự."
    mc "{i}Tôi thậm chí còn ăn trưa với cô ấy! Những học sinh khác không thể chịu nổi khi thấy tôi, nhưng tôi đếch quan tâm. Berry thú vị hơn họ rất nhiều!"
    mc "{i}Tất cả bọn họ đều chế nhạo tôi, có lẽ là vì ghen tị chăng!?{/i}"
    scene bg classroomdebut
    show classroomdebut 3
    play sound snani1
    sn "And what's your problem with him, fat ass?!"
    show classroomdebut 1
    zon "[sn]? You're the teacher's daughter. Aren't you mad he's dreaming about your mom?!"
    show classroomdebut sa
    mc "[sn] is Berry's daughter"
    show classroomdebut 3
    play sound slol1
    sn "I bet you're just jealous that our teacher is more popular with boys than you are!"
    show classroomdebut 1
    zon "Oh wow. What do you want, you red gorilla? Wanna taste my fists?"
    show classroomdebut 3
    sn "Oh YEAH, definitely! So I could grab that fist and use it to fuck your asshole!"
    show classroomdebut 1
    play sound zuh
    zon "Ew! What kind of weird threat is that?!"
    show classroomdebut 2
    play sound esoupir
    en "Stop it [sn], last time you did this, we had so many problems with that girl's relatives."
    en "Don't disgrace our family again."
    show classroomdebut 5
    zon "Wait, she really did that to someone?!!!"
    en "..."
    show classroomdebut 6
    "" "The girl is sweating intensely and instantly calms down."
    show classroomdebut em
    mc "{i}The girl on my right is [en]. She is [sn]'s little sister. She is our teacher's other daughter.{/i}"
    mc "How is it possible for them to be in the same class, you ask?"
    mc "[bn] told me that [en] skipped a year in high school, [sn] on the other hand, retook a year."
    mc "It would seem as if [en] inherited most the intellect, but at the same time [sn] doesn't look stupid..."
    show classroomdebut 2
    play sound esoupir
    en "Why did God give me such a violent sister..."
    show classroomdebut 3
    play sound slol1
    sn "What's your problem, sis? I'm just defending our mom's precious student, haha!"
    show classroomdebut 2
    play sound eloser3
    en "Stop defending such a loser. A loser is a loser because he acts like a loser."
    show classroomdebut 3
    play sound smoh1
    sn "Rhooo. You really are a heartless witch!"
    hide classroomdebut
    mcth "[en], I dislike this girl. I've only spoken with her a few times. She calls me \"The Loser\" all the time."
    mcth "But at least she doesn't harass me like [zon] does. She just avoids me."
    mcth "[sn], on the other hand, is really cool. She is intense with what she does but also goes all in when mad."
    mcth "She has no friends at school, just like me. But she doesn't care and enjoys doing her own thing in her bubble."
    mcth "Unlike me, nobody is trying to trigger her. They know she could make them pay sooo bad."
    mcth "I wish I had her intimidation skills."
    mcth "I like her, but I don't think she'd like a friend like me; we're so different..."
    mcth "I just can't wait to start a new life after the end of my studies..."

    scene intro berry watch with dissolve
    play sound bow1
    bn "Owh...?"
    bn "[zon]. That girl is such a nuisance..."
    bn "I have to do something."
    scene black with fade
    stop music fadeout 1.0
    "" "This is the end of the lesson."

    scene bg intro3 with fade
    play music "Audio/Musics/chill sexy.ogg"
    play sound bhello
    show berry shy o0 at right
    show mc_skinny at left
    bn "[mc]!"
    mc "Hey [bn]! How are you?"
    show berry base at center with move
    bn "Hm, awwh. You're not supposed to call me by my first name, you know. I'm still your teacher."
    bn "But it's okay <3."
    window hide
    pause
    window auto
    play sound bruok
    show berry shy:
        easeout 0.1 xoffset -50.0
    bn "Are you okay? I mean, your classmates aren't very nice to you."
    mc "Oh, I'm used to it. Plus, you're there for me: I don't need any of them."
    play sound blol1
    show mc_skinny at invisible
    show berry at invisible
    show intro hug with hpunch
    bn "... MMMMOOOOOH!!! You're the sweetest student I've ever had!!! <3 <3 <3"
    play sound bcandy
    bn "I could {b}eat{/b} you like sweet candy!"
    bn "You're so much more to me than a {b}simple{/b} student... I am so hopeful that everything will go well for you..."
    "" "[bn] continues to hug you for a few seconds. In her fantastic-Deep-Cleavage."
    mcth "Miss [bn] is so lovely and attentive with me. It feels so good in these moments with her..."
    mcth "...I can also feel how large her tits are beneath her shirt. I feel like I'm resting against clouds from heaven. Jesus Christ, they're soft!"
    hide intro hug
    show mc_skinny at visible
    show berry happy at visible
    bn "You can go now. Don't worry. I just wanted to make sure you were okay <3."
    mc "Thank you, [bn]!"
    hide mc_skinny
    "" "You head back to the hallway."
    pause
    stop music
    show berry serious with dissolve
    bn "..."
    show berry angry at angryjump
    play sound bhah
    bn "That [zon] bitch! How dare she treat my {i}candy{/i} like that!!!"
    show berry serious
    bn "..."
    show berry angry with dissolve:
        xzoom -1
        linear 0.2 xpos 0.5 xoffset 100
    pause 0.2
    show berry at angryjumpinv
    bn "Hey, you little shit. COME HERE!"

    scene bg intro4 with fade
    play music "Audio/Musics/robot_boogie.ogg"
    "" "In the hallway."
    show mc_skinny at left
    show emma base0 o0 at right
    en "You look so pathetic."
    pause
    play sound eloser3
    en "You're a loser."
    pause
    en "I bet you've never even had any girlfriend."
    mc "Well, if you're the kind of girl I could have, I'd rather be alone."
    show emma angry0 with vpunch
    en "WHAT?!"
    show emma at angryjump
    en "I'm the most popular girl in this lowlife university! I'm amazing!!"
    en "Just stay the way you are. You'll die alone, and no one will ever notice you."
    play sound etsah
    en "Tsah!"
    show emma:
        xzoom -1
        linear 1.0 xpos 1.5
    mc "FINALLY. The day is over. Time to go back home and repeat that same damn scenario over and over again..."
    show mc_skinny:
        xzoom -1.0
    play sound hit
    hide mc_skinny
    show intro s1 with vpunch
    "" "PEUH!"
    hide intro s1
    show mc_skinny aie at left
    show sarena o0 at center
    mc "EEEH?! What are you doing, [sn]?"
    show sarena taunt
    sn "Loser."
    show mc_skinny aie:
        xzoom -1.0
    mc "Yeah, I know."
    hide mc_skinny aie
    show sarena at invisible
    show intro s1 with vpunch
    play sound hit
    "" "PEUH!"
    show sarena challenge at visible
    show mc_skinny aie at left
    hide intro s1
    sn "WRONG!"
    sn "I feel like you've heard that so many times that you've started accepting it."
    mc "Yeah, I mean-"
    show sarena at angryjump
    sn "SILENCE!"
    mc "..."
    show sarena base
    sn "From now on, you will hang out with me."
    mc "Ah? I'm unsure I want YOU to teach me how to make friends."
    show sarena with vpunch
    sn " Silence!"
    mc "..."
    show sarena base
    sn "I won't accept a refusal."
    sn "It's not about making friends; it's about you having a stronger mind and gaining confidence."
    sn "Even if you don't want friends, you look bad. I will teach you how to have more self-esteem!"
    sn "So starting tomorrow, we're gonna start working out."
    mc "Working out?! I don't think I need muscles to feel better..."
    sn "YES YOU DO! Sports aren't about getting a \"great\" body. It's just a bonus. The main point is to get stronger mentally!"
    mc "I'm not sure I follow you..."
    show sarena taunt
    play sound slol1
    sn " You will understand when we begin the torture... Mouahaha!"
    mc "..."
    mc "Why-y-y do you want to help me?"
    show sarena base
    sn "Hmm...Because I kind of like you, I... guess."
    sn "Also, you make my mom worry a lot."
    mc "..."
    mc "*Sigh* Well..If it will help [bn] not to worry about me, I accept!"
    play sound shm
    sn "Jeez. You really do have a weird relationship with my mom..."
    sn "Okay, see you tomorrow!"

    scene black
    stop music fadeout 1.0
    mc "From that day, I started hanging out with [sn]. Not going to lie. It was pretty weird at the beginning. For both of us."
    mc "[zon] mysteriously stopped bullying me at the same moment. I guess she realized she was a pain in the ass? Who knows."
    jump introduction2



    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
