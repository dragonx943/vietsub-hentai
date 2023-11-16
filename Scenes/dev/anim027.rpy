label bfsexa027(a=1.0/12):
    $ animspeed = a
    window hide
    scene bfsexbg
    show bfsexa
    if (a == 1.0/12):
        play sexfx sex10
        play sex bmoanshard
    elif True:
        play sexfx sex05
        play sex bmoans2
    pause
    window auto
    return
label bfsexa027cum(a=0.0416):
    $ animspeed = a
    window hide
    stop sex
    stop sexfx
    show bfsexacum
    show cumsfxrep:
        xalign 0.5
        yalign 0.5
    play audio bcum1
    call cummale from _call_cummale_15
    pause
    window auto
    return
label bfsexa027cum2(a=0.0416):
    $ animspeed = a
    window hide
    stop sex
    stop sexfx
    hide bfsexa
    show bfsexacum2
    show cumsfxrep:
        xalign 0.52
        yalign 0.55




    call cumfemaleflash from _call_cumfemaleflash_7
    play audio bcum1
    pause
    window auto
    return
label bfsexweda027cum(a=0.0416):
    $ animspeed = a
    window hide
    stop sex
    stop sexfx
    show bfsexwedacum
    show cumsfxrep:
        xalign 0.5
        yalign 0.5




    call cumfemaleflash from _call_cumfemaleflash_8
    play audio bcum1
    pause
    window auto
    return

image bfsexa:
    "bfsexa_00001"
    pause animspeed
    "bfsexa_00002"
    pause animspeed
    "bfsexa_00003"
    pause animspeed
    "bfsexa_00004"
    pause animspeed
    "bfsexa_00005"
    pause animspeed
    "bfsexa_00006"
    pause animspeed
    "bfsexa_00007"
    pause animspeed
    "bfsexa_00008"
    pause animspeed
    "bfsexa_00009"
    pause animspeed
    "bfsexa_00010"
    pause animspeed
    "bfsexa_00011"
    pause animspeed
    "bfsexa_00012"
    pause animspeed
    repeat
image bfsexacum:
    "bfsexanimcum_00001"
    pause animspeed
    "bfsexanimcum_00002"
    pause animspeed
    repeat
image bfsexacum2:
    "bdev3m1"
    pause animspeed
    "bdev3m2"
    pause animspeed
    repeat


image bfsexwedacum:
    "bdev3r2a"
    pause animspeed
    "bdev3r2b"
    pause animspeed
    repeat


label bsexmorninga027(a=0.0416):
    $ animspeed = a
    window hide
    scene bsexmorningbg
    show bsexmorninga
    if (a == 0.0416):
        pause 0.25
        play sexfx sex05
        play sex bmoans2
    elif True:
        pause 0.5
        play sexfx sex10
        play sex bmoanshard
    pause
    window auto
    return
label bsexmorninga027cum(a=0.0416):
    $ animspeed = a
    window hide
    stop sex
    stop sexfx
    hide bsexmorninga
    show bsexmorningacum
    show cumsfxrep:
        xalign 0.40
        yalign 0.30
    play audio bcum1
    call cummale from _call_cummale_8
    pause
    window auto
    return

image bsexmorninga:
    "bsexmorninga_00001"
    pause animspeed
    "bsexmorninga_00002"
    pause animspeed
    "bsexmorninga_00003"
    pause animspeed
    "bsexmorninga_00004"
    pause animspeed
    "bsexmorninga_00005"
    pause animspeed
    "bsexmorninga_00006"
    pause animspeed
    "bsexmorninga_00007"
    pause animspeed
    "bsexmorninga_00008"
    pause animspeed
    "bsexmorninga_00009"
    pause animspeed
    "bsexmorninga_00010"
    pause animspeed
    "bsexmorninga_00011"
    pause animspeed
    "bsexmorninga_00012"
    pause animspeed
    repeat
image bsexmorningacum:
    "bsexmorningcum1"
    pause animspeed
    "bsexmorningcum2"
    pause animspeed
    repeat





label bsexpartya027(a=1):

    if a == 1:
        $ a = 0.0625
    elif a == 2:
        $ a = 0.0416

    $ animspeed = a
    window hide
    scene bsexpartybg2
    show bsexpartya
    if (a == 0.0625):
        pause 0.3
        play sexfx sex05
        play sex bmoans1
    elif True:

        play sexfx sex033
        play sex bmoans3
    pause
    window auto
    return
label bsexpartya027cum(a=0.0416):
    $ animspeed = a
    window hide
    stop sex
    stop sexfx
    hide bsexpartya
    show bsexpartyacum
    play audio bcum1
    call cumdouble from _call_cumdouble
    pause
    window auto
    return

image bsexpartya:
    "bsexpartya_00001"
    pause animspeed
    "bsexpartya_00002"
    pause animspeed
    "bsexpartya_00003"
    pause animspeed
    "bsexpartya_00004"
    pause animspeed
    "bsexpartya_00005"
    pause animspeed
    "bsexpartya_00006"
    pause animspeed
    "bsexpartya_00007"
    pause animspeed
    "bsexpartya_00008"
    pause animspeed
    repeat
image bsexpartyacum:
    "bdev3g1"
    pause animspeed
    "bdev3g2"
    pause animspeed
    repeat




image bworksexa:
    "bworksexa_00001"
    pause animspeed
    "bworksexa_00002"
    pause animspeed
    "bworksexa_00003"
    pause animspeed
    "bworksexa_00004"
    pause animspeed
    "bworksexa_00005"
    pause animspeed
    "bworksexa_00006"
    pause animspeed
    "bworksexa_00007"
    pause animspeed
    "bworksexa_00008"
    pause animspeed
    repeat

label bworksexa027(a=1.0/8):
    $ animspeed = a
    window hide

    if animspeed == 1.0/8:
        play sex bmoans1
        play sexfx sex10
    elif animspeed == 1.0/16:
        play sex bmoans3
        play sexfx sex05
    show bworksexa
    pause
    window auto
    return

label bworksexacum027:
    window hide
    scene bdev3e1
    stop sexfx
    stop sex
    play audiocum bcum1
    call cumfemaleflash from _call_cumfemaleflash_15
    pause
    window auto
    return
label bworksexbcum027:
    window hide
    scene bfsexanimcum
    stop sexfx
    stop sex
    stop audiocum
    play audiocum bcum1
    call cummale from _call_cummale_46
    pause
    window auto
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
