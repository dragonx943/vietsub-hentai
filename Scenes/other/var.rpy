
define ispromisedtoemma = False
define isendmode = False
define day = 0

define lastmapcall = "toliving"

define emmasurname = "Housemate"
define sarenasurname = "Best friend"
define berrysurname = "Lovely teacher"
define valeriesurname = "Dad's friend"


define blv = 0
define elv = 0
define slv = 0
define vlv = 0

define vendvisit = False
define bendvisit = False
define eendvisit = False
define sendvisit = False


define berrystatus = "married"
define emmastatus = "in couple"
define valeriestatus = "single, but dad's fuck-friend"
define sarenastatus = "in couple"
define mcstatus = "in couple"

define bstep = 0
define bsteps = ["She sees you as a cute boy she wants to take care of.",
"She loves to give you \"affection\" in secret.",
"She got really attached to you and doesn't want to let you go away from her.",
"She owes you, and loves you more than what you can imagine.",
"She's happier than ever!"]

define estep = 0
define esteps = ["She considers you as a loser.","She lets you play with her pussy but doesn't assume it.", "She appreciates your consideration.", "She is completely in love with you.",
"She's happier than ever!"]

define sstep = 0
define ssteps = ["She feels a deep and true friendship for you.","She enjoys giving you pleasure, and also like the taste\nof your cum.", "She realizes that you are the most important in her life.","She is totally in love with you and is all yours.",
"She's happier than ever!"]

define vstep = 0
define vsteps = ["She considers you're a useless brat",
"She wants more of your cum, and pretend to deny she enjoys it.",
"She enjoys getting punished by you.",
"She enjoys being your slut.",
"She's happier than ever!"]










define bboundv = 0
define bbounde = 0
define bbounds = 0
define vbounde = 0
define vbounds = 0
define sbounde = 0

define bboundvmax = 26
define bboundemax = 26
define bboundsmax = 26
define vboundemax = 26
define vboundsmax = 26
define sboundemax = 26

init python:

    def actubounds():
        global bboundv
        global bbounde
        global bbounds
        global vbounde
        global vbounds
        global sbounde
        if bboundv >24:
            bboundv = 24
        if bbounde >24:
            bbounde = 24
        if bbounds >24:
            bbounds = 24
        if vbounde >24:
            vbounde = 24
        if vbounds >24:
            vbounds = 24
        if sbounde >24:
            sbounde = 24
    def incrcum(n,v):
        global scum
        global ecum
        global bcum
        global vcum
        global cumbys
        global cumbye
        global cumbyb
        global cumbyv
        
        
        
        if n == "scum":
            scum += v
        
        elif n == "ecum":
            ecum += v
        
        elif n == "bcum":
            bcum += v
        
        elif n == "vcum":
            vcum += v
        
        elif n == "cumbys":
            cumbys += v
        
        elif n == "cumbye":
            cumbye += v
        
        elif n == "cumbyb":
            cumbyb += v
        
        elif n == "cumbyv":
            cumbyv += v
        if scum + bcum + ecum + vcum > 49 and persistent.ach_pussypro == False:
            persistent.ach_pussypro = True
        
        if cumbys + cumbye + cumbyb + cumbyv > 49 and persistent.ach_milkingmachine == False:
            persistent.ach_milkingmachine = True
    def incrstat(n,number):
        global cockskill
        global tongueskill
        global handskill
        global tempfortext
        tempfortext = number
        if n == "cockskill":
            cockskill+=number
            write ("Cock skill increased by [tempfortext]!")
            if cockskill >100:
                cockskill = 100
        elif n == "tongueskill":
            tongueskill+=number
            write ("Tongue skill increased by [tempfortext]!")
            if tongueskill >100:
                tongueskill = 100
        elif n == "handskill":
            handskill+=number
            write ("Hand skill increased by [tempfortext]!")
            if handskill >100:
                handskill = 100

define tempfortext = ""

screen skillup(n):
    timer 4.0 action [ToggleScreen("skillup")]
    if n == "handskill":
        add "incrhand" at textpop
    if n == "cockskill":
        add "incrcock" at textpop
    if n == "tongueskill":
        add "incrtongue" at textpop

transform textpop:
    align (0.5,0.5)
    alpha 1.0
    xzoom 0.9 yzoom 0.9
    linear 0.1 xzoom 1.1 yzoom 1.1 yoffset -25
    linear 2.0 yoffset -100 xzoom 1.0 yzoom 1.0 alpha 0.5
    linear 1.0 alpha 0.0

define virginitylossby = "None"
define firstbjby = "None"
define firsttjby = "None"
define firstcunto = "None"

define cumbys = 0
define cumbyb = 0
define cumbyv = 0
define cumbye = 0
define scum = 0
define vcum = 0
define bcum = 0
define ecum = 0

define bpos = "kitchen"
define vpos = "backyard"
define epos = "diningroom"
define spos = "balcony"































label showimg(imgname):
    window hide

    $ renpy.show(imgname)
    $ renpy.with_statement(fade)
    pause
    window auto
    return

transform bottall:
    yalign 1.0 xalign 0.0
label showimgtall1(imgname):
    window hide
    $ renpy.show(imgname, at_list=[bottall])
    $ renpy.with_statement(fade)
    pause

    window auto
    return

label showscene(imgname):
    window hide

    show layer master

    $ renpy.scene()
    $ renpy.show(imgname)
    $ renpy.with_statement(fade)
    pause
    window auto
    return
label showimgfury(imgname):
    window hide
    show expression DynamicImage(imgname) at angryjumpcentered

    pause
    window auto
    return




define notyet = "{color=#a81919}You'll have to wait for the next game's update to continue her development. Don't forget to checkout all of her new daily activities!{/color}"

define blvhint = ["Talk to each girl when they work. Berry works in her room.",
    "Ask her about what she misses in her couple during a party.",
    "Take a visit to Berry while she is working in her room.",
    "Spy again on Berry while she is working in her room!", "",
    "Buy her a new cosplay outfit at the PC. Give it to her when she works in her room.",
    "Find her in the kitchen",
    "Join her at 10 P.M in the hallway.",
    "Berry needs you when she's in her room!",
    "Berry is looking at her feedback in the backyard.",
    "Try to contact Isabelle on the Internet.",
    "Tell Berry she can talk with her idol! In her room.",
    "Spend the night with Berry in the living room at 10 P.M.",
    "Go to sleep after getting a call from Zoe.",
    "Break up with Zoe. Just pass the day.",
    "Let her wake you up.",
    "She is expecting a package delivery.",
    "You can hear some noises from her room when she's working.",
    "The beast will come for you. Pass the day.",
    "You have finished Berry's individual storyline. Congratulations!",
    notyet]

define slvhint = ["Talk to each girl when they work. Sarena works on the balcony.",
    "Ask her about what she misses in her couple during a party.",
    "Propose Sarena to make videos when she's on the balcony.",
    "Ask her about the video's feedback in the backyard.",
    "Time to make another video with Sarena! At the balcony.",
    "Pass the day.",
    "Meet Sarena at the balcony.",
    "It's time to do another video! At the balcony.",
    "Sarena is in the kitchen? What is she doing?",
    "Sarena is having a discussion with her girlfriend in her room in the evening.",
    "It's maybe time to make a new video! At the balcony.",
    "Sarena is in the kitchen? What is she doing?",
    "Am I fantasizing about Sarena? Anyway, time to go to sleep.",
    "Find her on the map.",
    "You can hear Sarena from the living room.",
    "Sarena is preparing something. When will it happen? Pass the day.",
    "Go to sleep after getting a call from Zoe.",
    "Break up with Zoe. Just pass the day.",
    "Annonce your break-up to Sarena in the backyard.",
    "Wait for something to happen. Just pass the day.",
    "Make another video with her! At the balcony.",
    "Wait for her to call for you. Just pass the day.",
    "You have finished Sarena's individual storyline. Congratulations!",
    notyet]

define elvhint = ["Talk to each girl when they work. Emma works in the pc room",
    "Ask her about what she misses in her couple during a party.",
    "Meet Emma when she is streaming.",
    "Meet Emma at the dining room",
    "Learn how to take photos on the internet.",
    "Propose her to try your new skills in the dinning-room",
    "Find her in the backyard.",
    "Join Emma in her room.",
    "Go to the PC when Emma is streaming.",
    "Emma is in her room. What is she doing?",
    "Emma is giving a call to her BF in the morning in her room.",
    "Wait for her to do something. Just pass the day.",
    "Wait for her to do something. Just pass the day.",
    "Go to sleep after getting a call from Zoe.",
    "Break up with Zoe. Just pass the day.",
    "Emma is in her room in the morning!",
    "Emma is in Valerie's room around 6 PM",
    "Wait for her to do something when you wake up. Just pass the day.",
    "Emma is in her room around 2 PM!",
    "Wait for her to do something when you go to sleep. Just pass the day.",
    "You have finished Emma's individual storyline. Congratulations!",
    notyet]
define vlvhint = ["Talk to each girl when they work. Valerie works in her room.",
    "Ask her about what she misses in her couple during a party.",
    "Spy on her to see what she does in her room.",
    "Go on the internet to get her fake sperm.",
    "Give her the \"fake\" sperm.",
    "Wait for her to take action. Just pass the day.",
    "Touch her while she relaxes in the backyard as revenge!",
    "Shower when she passes at 6 PM",
    "Wait for her to take action. Just pass the day.",
    "Spy on her once again.",
    "Steal her dildo right before she starts to work. In her room at 6 P.M",
    "Some noise is coming from your room at 6 P.M.",
    "You have an idea, but you need a toolkit (on the internet), then go to your room.",
    "Show her your work when she's in her room.",
    "It's show time. In her room.",
    "Go to sleep after getting a call from Zoe.",
    "Break up with Zoe. Just pass the day.",
    "Valerie is doing something in her room at 10 P.M.",
    "Valerie is doing something in her room at 10 P.M.",
    "Wait for a call. pass the day.",
    "Talk to Valerie in the backyard",
    "Wait for her. Just pass the day.",
    "You have finished Valerie's individual storyline. Congratulations!",
    notyet]



define introepeek = True
define firstlookonemma = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
