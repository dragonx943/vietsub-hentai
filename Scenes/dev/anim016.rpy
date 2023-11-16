init python:

    def valhj():
        renpy.show("016hj")
        renpy.music.play(audio.frottements2,"sexfx")
        renpy.music.play(audio.vmoanshj,"sex")

    def valhjcum():
        renpy.hide("016hj")
        renpy.show("repvalmmastcum")
        renpy.show("016hjcum")
        renpy.show ("cumanim")
        renpy.music.stop("sexfx")
        renpy.music.stop("sex")
        renpy.play(audio.vmccum,channel = "audio")
        renpy.play(audio.cumexplo,channel = "audio")
        renpy.play(audio.cumsoundext,channel = "audio")

    def valpartydoublefinger():
        renpy.show("016doublefinger")
        renpy.music.play(audio.frottements2,"sexfx")
        renpy.music.play(audio.vmoansdrunk,"sex")

    def valpartydoublefingercum():
        renpy.hide("016doublefinger")
        renpy.show("016doublefingercum", at_list = [cumtr])
        renpy.show ("cumanim")
        renpy.music.stop("sexfx")
        renpy.music.stop("sex")
        renpy.play(audio.vcum1,channel = "audio")

define sp016doublefinger = 0.0416

image 016doublefinger:
    "016partyfj_00000"
    pause sp016doublefinger
    "016partyfj_00001"
    pause sp016doublefinger
    "016partyfj_00002"
    pause sp016doublefinger
    "016partyfj_00003"
    pause sp016doublefinger
    "016partyfj_00004"
    pause sp016doublefinger
    "016partyfj_00005"
    pause sp016doublefinger
    "016partyfj_00006"
    pause sp016doublefinger
    "016partyfj_00007"
    pause sp016doublefinger
    repeat

image 016doublefingercum:
    "016partyfjcum_00000"
    pause 0.03
    "016partyfjcum_00001"
    pause 0.03
    "016partyfjcum_00002"
    pause 0.03
    "016partyfjcum_00001"
    pause 0.03
    repeat

define sp016hj = 0.035
image 016hj:
    "016valhj_0000"
    pause sp016hj
    "016valhj_0001"
    pause sp016hj
    "016valhj_0002"
    pause sp016hj
    "016valhj_0003"
    pause sp016hj
    "016valhj_0004"
    pause sp016hj
    "016valhj_0005"
    pause sp016hj
    "016valhj_0006"
    pause sp016hj
    "016valhj_0007"
    pause sp016hj
    "016valhj_0008"
    pause sp016hj
    repeat

define sp016hjcum = 0.06
image 016hjcum:
    "016hjcum_0000"
    pause sp016hjcum
    "016hjcum_0001"
    pause sp016hjcum
    "016hjcum_0002"
    pause sp016hjcum
    "016hjcum_0003"
    pause sp016hjcum
    "016hjcum_0004"
    pause sp016hjcum
    "016hjcum_0005"
    pause sp016hjcum
    "016hjcum_0006"
    pause sp016hjcum
    "016hjcum_0007"
    pause sp016hjcum
    "016hjcum_0008"
    pause sp016hjcum
    "016hjcum_0009"
    pause sp016hjcum
    "016hjcum_0010"
    pause sp016hjcum
    "016hjcum_0011"
    pause sp016hjcum
    "016hjcum_0012"
    pause sp016hjcum
    "016hjcum_0013"
    pause sp016hjcum
    "016hjcum_0014"
    pause sp016hjcum
    "016hjcum_0015"
    pause sp016hjcum
    "016hjcum_0016"
    pause sp016hjcum
    "016hjcum_0017"
    pause sp016hjcum
    "016hjcum_0018"
    pause sp016hjcum
    "016hjcum_0019"
    pause sp016hjcum
    "016hjcum_0020"
    pause sp016hjcum
    "016hjcum_0021"
    pause sp016hjcum
    "016hjcum_0022"




define sp016sex = 0.038


image 016sex:
    "016sex_0000"
    pause sp016sex
    "016sex_0001"
    pause sp016sex
    "016sex_0002"
    pause sp016sex
    "016sex_0003"
    pause sp016sex
    "016sex_0004"
    pause sp016sex
    "016sex_0005"
    pause sp016sex
    "016sex_0006"
    pause sp016sex
    "016sex_0007"
    pause sp016sex
    "016sex_0008"
    pause sp016sex
    "016sex_0009"
    pause sp016sex
    "016sex_0010"
    pause sp016sex
    "016sex_0011"
    pause sp016sex
    repeat


define sp016sexcum = 0.0416
image 016sexcumA:
    "016sexdreamcum_00004"
    pause sp016sexcum
    "016sexdreamcum_00005"
    pause sp016sexcum
    "016sexdreamcum_00006"
    pause sp016sexcum
    repeat

define sp016sexcumB = 0.06
image 016sexcumB:
    "016sexcumcum_0000"
    pause sp016sexcumB
    "016sexcumcum_0001"
    pause sp016sexcumB
    "016sexcumcum_0002"
    pause sp016sexcumB
    "016sexcumcum_0003"
    pause sp016sexcumB
    "016sexcumcum_0004"
    pause sp016sexcumB
    "016sexcumcum_0005"
    pause sp016sexcumB
    "016sexcumcum_0006"
    pause sp016sexcumB
    "016sexcumcum_0007"
    pause sp016sexcumB
    "016sexcumcum_0008"
    pause sp016sexcumB
    "016sexcumcum_0009"
    pause sp016sexcumB
    "016sexcumcum_0010"
    pause sp016sexcumB
    "016sexcumcum_0011"
    pause sp016sexcumB
    "016sexcumcum_0012"
    pause sp016sexcumB
    "016sexcumcum_0013"
    pause sp016sexcumB
    "016sexcumcum_0014"
    pause sp016sexcumB
    "016sexcumcum_0015"
    pause sp016sexcumB
    "016sexcumcum_0016"
    pause sp016sexcumB
    "016sexcumcum_0017"

define sp016tf = 0.04
image 016tf:
    "016tf_0000"
    pause sp016tf
    "016tf_0001"
    pause sp016tf
    "016tf_0002"
    pause sp016tf
    "016tf_0003"
    pause sp016tf
    "016tf_0004"
    pause sp016tf
    "016tf_0005"
    pause sp016tf
    "016tf_0006"
    pause sp016tf
    "016tf_0007"
    pause sp016tf
    "016tf_0008"
    pause sp016tf
    "016tf_0009"
    pause sp016tf
    "016tf_0010"
    pause sp016tf
    "016tf_0011"
    pause sp016tf
    repeat

define sp016tfcum = 0.05
image 016tfcumA:
    "016tf_0000"
    pause sp016tfcum
    "016tf_0001"
    pause sp016tfcum
    "016tf_0002"
    pause sp016tfcum
    "016tf_0003"
    pause sp016tfcum
    "016tf_0004"
    pause sp016tfcum
    "016tf_0005"
    pause sp016tfcum
    "016tf_0006"
    pause sp016tf
    "016tf_0007"
    pause sp016tfcum
    "016tf_0008"
    pause sp016tfcum
    "016tf_0009"

image 016tfcumB:
    "016tjcumb_0000"
    pause sp016tfcum
    "016tjcumb_0001"
    pause sp016tfcum
    "016tjcumb_0002"
    pause sp016tfcum
    "016tjcumb_0003"
    pause sp016tfcum
    "016tjcumb_0004"
    pause sp016tfcum
    "016tjcumb_0005"
    pause sp016tfcum
    "016tjcumb_0006"
    pause sp016tfcum
    "016tjcumb_0007"
    pause sp016tfcum
    "016tjcumb_0008"
    pause sp016tfcum
    "016tjcumb_0009"
    pause sp016tfcum
    "016tjcumb_0010"
    pause sp016tfcum
    "016tjcumb_0011"
    pause sp016tfcum
    "016tjcumb_0012"
    pause sp016tfcum
    "016tjcumb_0013"
    pause sp016tfcum
    "016tjcumb_0014"
    pause sp016tfcum
    "016tjcumb_0015"
    pause sp016tfcum
    "016tjcumb_0016"
    pause sp016tfcum
    "016tjcumb_0017"

define sp016fj = 0.0416
image 016fj:
    "by fj_00000"
    pause sp016fj
    "by fj_00001"
    pause sp016fj
    "by fj_00002"
    pause sp016fj
    "by fj_00003"
    pause sp016fj
    "by fj_00004"
    pause sp016fj
    "by fj_00005"
    pause sp016fj
    "by fj_00006"
    pause sp016fj
    "by fj_00007"
    pause sp016fj
    repeat

define sp016fjcum = 0.04
image 016fjcum:
    "by fjcum_00000"
    pause sp016fj
    "by fjcum_00001"
    pause sp016fj
    "by fjcum_00002"
    pause sp016fj
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
