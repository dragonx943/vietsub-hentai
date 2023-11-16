screen animationpanel2:
    zorder 2
    modal True
    imagemap:
        ground "ui/animreplaypbg.webp"
        text "[pagename]" align (0.9,0.1) bold True size 40
        imagebutton:
            align (0.97, 0.5)
            idle "ui/Arrow.webp"
            hover lumi("ui/Arrow.webp")
            action Function(nextpage)
        imagebutton:
            align (0.03, 0.5)

            idle "ui/Arrow2.webp"
            hover lumi("ui/Arrow2.webp")
            action Function(prevpage)

        imagebutton:
            align (1.0,0.0)
            idle "ui/closeui.webp"
            hover "ui/closeui h.webp"
            action Jump(lastmapcall)

        hbox align (0.1, 0.2) box_wrap True spacing 10 xmaximum 1500 yanchor 0.0 xanchor 0.0:


            if replaypage == 4:
                imagebutton:
                    idle "minia/minia26.webp"
                    hover lumi("minia/minia26.webp")
                    xalign 0.5

                    action Jump ("repzoe1")


            if replaypage == 1:
                imagebutton:
                    idle "minia/minia23.webp"
                    hover lumi("minia/minia23.webp")
                    xalign 0.5

                    action Jump ("rep01emmamoveass")


            if replaypage == 2:
                imagebutton:
                    idle "minia/minia24.webp"
                    hover lumi("minia/minia24.webp")
                    xalign 0.5

                    action Jump ("rep01berrybj")



            if replaypage == 0:
                if persistent.replay3 == True or cheatdev == True:
                    imagebutton:
                        idle "minia/minia3.webp"
                        hover lumi("minia/minia3.webp")
                        xalign 0.5

                        action Jump ("repscrunches")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 0:
                if persistent.replay2 == True or cheatdev == True:
                    imagebutton:
                        idle "minia/minia2.webp"
                        hover lumi("minia/minia2.webp")
                        xalign 0.5

                        action Jump ("repsjoff")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 0:
                if persistent.replay127 == True or cheatdev == True:
                    imagebutton:
                        idle "minia/minia127.webp"
                        hover lumi("minia/minia127.webp")
                        xalign 0.5

                        action Jump ("repsjoffmorning")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 0:
                if persistent.replay1 == True or cheatdev == True:
                    imagebutton:
                        idle "minia/minia1.webp"
                        hover lumi("minia/minia1.webp")
                        xalign 0.5

                        action Jump ("repstjparty")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 1:
                if persistent.replay5 == True or cheatdev == True:
                    imagebutton:
                        idle "minia/minia5.webp"
                        hover lumi("minia/minia5.webp")
                        xalign 0.5

                        action Jump ("repedevfj")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 2:
                if persistent.replay6 == True or cheatdev == True:
                    imagebutton:
                        idle "minia/minia6.webp"
                        hover lumi("minia/minia6.webp")
                        xalign 0.5

                        action Jump ("reptjmassage")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 3:
                if persistent.replay13 == True or cheatdev == True:
                    imagebutton:
                        idle "minia/minia13.webp"
                        hover lumi("minia/minia13.webp")
                        xalign 0.5

                        action Jump ("repdreamsexval")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 3:
                if cheatdev == True or persistent.replay56 == True:
                    imagebutton:
                        idle "minia/minia56.webp"
                        hover lumi("minia/minia56.webp")
                        xalign 0.5

                        action Jump ("repvalhj")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 3:
                if cheatdev == True or persistent.replay58 == True:
                    imagebutton:
                        idle "minia/minia58.webp"
                        hover lumi("minia/minia58.webp")
                        xalign 0.5

                        action Jump ("repvaldoublefingerparty")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 3:
                if persistent.replay12 == True or cheatdev == True:
                    imagebutton:
                        idle "minia/minia12.webp"
                        hover lumi("minia/minia12.webp")
                        xalign 0.5

                        action Jump ("rep016tf")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 0:
                if cheatdev == True or persistent.replay14 == True:
                    imagebutton:
                        idle "minia/minia14.webp"
                        hover lumi("minia/minia14.webp")
                        xalign 0.5

                        action Jump ("rep01869")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 0:
                if cheatdev == True or persistent.replay15 == True:
                    imagebutton:
                        idle "minia/minia15.webp"
                        hover lumi("minia/minia15.webp")
                        xalign 0.5

                        action Jump ("rep018bjmorning")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 0:
                if cheatdev == True or persistent.replay18 == True:
                    imagebutton:
                        idle "minia/minia18.webp"
                        hover lumi("minia/minia18.webp")
                        xalign 0.5

                        action Jump ("rep018cunby")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 0:
                if cheatdev == True or persistent.replay21 == True:
                    imagebutton:
                        idle "minia/minia21.webp"
                        hover lumi("minia/minia21.webp")
                        xalign 0.5

                        action Jump ("rep018devfj")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 0:
                if cheatdev == True or persistent.replay19 == True:
                    imagebutton:
                        idle "minia/minia19.webp"
                        hover lumi("minia/minia19.webp")
                        xalign 0.5

                        action Jump ("rep018devcun")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 0:
                if cheatdev == True or persistent.replay20 == True:
                    imagebutton:
                        idle "minia/minia20.webp"
                        hover lumi("minia/minia20.webp")
                        xalign 0.5

                        action Jump ("rep018dreamsex")
                else:
                    add "minialocked" xalign 0.5








            if replaypage == 0:
                if cheatdev == True or persistent.replay17 == True:
                    imagebutton:
                        idle "minia/minia17.webp"
                        hover lumi("minia/minia17.webp")
                        xalign 0.5

                        action Jump ("rep018party")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 0:
                if cheatdev == True or persistent.replay25 == True:
                    imagebutton:
                        idle "minia/minia25.webp"
                        hover lumi("minia/minia25.webp")
                        xalign 0.5

                        action Jump ("rep018tv")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 0:
                if cheatdev == True or persistent.replay16 == True:
                    imagebutton:
                        idle "minia/minia16.webp"
                        hover lumi("minia/minia16.webp")
                        xalign 0.5

                        action Jump ("rep018bjdev")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 1:
                if cheatdev == True or persistent.replay31 == True:
                    imagebutton:
                        idle "minia/minia31.webp"
                        hover lumi("minia/minia31.webp")
                        xalign 0.5

                        action Jump ("rep019sexdream")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay128 == True:
                    imagebutton:
                        idle "minia/minia128.webp"
                        hover lumi("minia/minia128.webp")
                        xalign 0.5

                        action Jump ("repemmcunby100")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay29 == True:
                    imagebutton:
                        idle "minia/minia29.webp"
                        hover lumi("minia/minia29.webp")
                        xalign 0.5

                        action Jump ("rep019devcun")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay28 == True:
                    imagebutton:
                        idle "minia/minia28.webp"
                        hover lumi("minia/minia28.webp")
                        xalign 0.5

                        action Jump ("rep019devbj")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay30 == True:
                    imagebutton:
                        idle "minia/minia30.webp"
                        hover lumi("minia/minia30.webp")
                        xalign 0.5

                        action Jump ("rep019cookcun")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay32 == True:
                    imagebutton:
                        idle "minia/minia32.webp"
                        hover lumi("minia/minia32.webp")
                        xalign 0.5

                        action Jump ("rep019thf")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay27 == True:
                    imagebutton:
                        idle "minia/minia27.webp"
                        hover lumi("minia/minia27.webp")
                        xalign 0.5

                        action Jump ("rep019kitchenbj")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 2:
                if cheatdev == True or persistent.replay36 == True:
                    imagebutton:
                        idle "minia/minia36.webp"
                        hover lumi("minia/minia36.webp")
                        xalign 0.5

                        action Jump ("rep02by")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay37 == True:
                    imagebutton:
                        idle "minia/minia37.webp"
                        hover lumi("minia/minia37.webp")
                        xalign 0.5

                        action Jump ("rep02balc")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay129 == True:
                    imagebutton:
                        idle "minia/minia129.webp"
                        hover lumi("minia/minia129.webp")
                        xalign 0.5

                        action Jump ("repbercunparty100")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay35 == True:
                    imagebutton:
                        idle "minia/minia35.webp"
                        hover lumi("minia/minia35.webp")
                        xalign 0.5

                        action Jump ("rep02morning")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay34 == True:
                    imagebutton:
                        idle "minia/minia34.webp"
                        hover lumi("minia/minia34.webp")
                        xalign 0.5

                        action Jump ("rep02bjtv")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay38 == True:
                    imagebutton:
                        idle "minia/minia38.webp"
                        hover lumi("minia/minia38.webp")
                        xalign 0.5

                        action Jump ("rep02devbj")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay39 == True:
                    imagebutton:
                        idle "minia/minia39.webp"
                        hover lumi("minia/minia39.webp")
                        xalign 0.5

                        action Jump ("rep02devcuni")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay33 == True:
                    imagebutton:
                        idle "minia/minia33.webp"
                        hover lumi("minia/minia33.webp")
                        xalign 0.5

                        action Jump ("rep02dream")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 0:
                if cheatdev == True or persistent.replay42 == True:
                    imagebutton:
                        idle "minia/minia42.webp"
                        hover lumi("minia/minia42.webp")
                        xalign 0.5

                        action Jump ("rep021jacc")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay41 == True:
                    imagebutton:
                        idle "minia/minia41.webp"
                        hover lumi("minia/minia41.webp")
                        xalign 0.5

                        action Jump ("rep021shower")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay40 == True:
                    imagebutton:
                        idle "minia/minia40.webp"
                        hover lumi("minia/minia40.webp")
                        xalign 0.5

                        action Jump ("rep021cook")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 1:
                if cheatdev == True or persistent.replay43 == True:
                    imagebutton:
                        idle "minia/minia43.webp"
                        hover lumi("minia/minia43.webp")
                        xalign 0.5

                        action Jump ("repemorning")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 3:
                if cheatdev == True or  persistent.replay44 == True:
                    imagebutton:
                        idle "minia/minia44.webp"
                        hover lumi("minia/minia44.webp")
                        xalign 0.5

                        action Jump ("repv2j")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or  persistent.replay45 == True:
                    imagebutton:
                        idle "minia/minia45.webp"
                        hover lumi("minia/minia45.webp")
                        xalign 0.5

                        action Jump ("repv2l")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay46 == True:
                    imagebutton:
                        idle "minia/minia46.webp"
                        hover lumi("minia/minia46.webp")
                        xalign 0.5

                        action Jump ("repv2morning")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay47 == True:
                    imagebutton:
                        idle "minia/minia47.webp"
                        hover lumi("minia/minia47.webp")
                        xalign 0.5

                        action Jump ("repv2party")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 1:
                if cheatdev == True or persistent.replay48 == True:
                    imagebutton:
                        idle "minia/minia48.webp"
                        hover lumi("minia/minia48.webp")
                        xalign 0.5

                        action Jump ("rep023l")
                else:
                    add "minialocked" xalign 0.5
            if replaypage == 4:
                if cheatdev == True or persistent.replay51 == True:
                    imagebutton:
                        idle "minia/minia51.webp"
                        hover lumi("minia/minia51.webp")
                        xalign 0.5

                        action Jump ("rep023g")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay50 == True:
                    imagebutton:
                        idle "minia/minia50.webp"
                        hover lumi("minia/minia50.webp")
                        xalign 0.5

                        action Jump ("rep023i")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay49 == True:
                    imagebutton:
                        idle "minia/minia49.webp"
                        hover lumi("minia/minia49.webp")
                        xalign 0.5

                        action Jump ("rep023j")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 0:
                if cheatdev == True or persistent.replay52 == True:
                    imagebutton:
                        idle "minia/minia52.webp"
                        hover lumi("minia/minia52.webp")
                        xalign 0.5

                        action Jump ("rep024backyard")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay53 == True:
                    imagebutton:
                        idle "minia/minia53.webp"
                        hover lumi("minia/minia53.webp")
                        xalign 0.5

                        action Jump ("rep024morning")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay54 == True:
                    imagebutton:
                        idle "minia/minia54.webp"
                        hover lumi("minia/minia54.webp")
                        xalign 0.5

                        action Jump ("rep024s3")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay55 == True:
                    imagebutton:
                        idle "minia/minia55.webp"
                        hover lumi("minia/minia55.webp")
                        xalign 0.5

                        action Jump ("rep024party")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 1:
                if cheatdev == True or persistent.replay59 == True:
                    imagebutton:
                        idle "minia/minia59.webp"
                        hover lumi("minia/minia59.webp")
                        xalign 0.5

                        action Jump ("repesexdev")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay61 == True:
                    imagebutton:
                        idle "minia/minia61.webp"
                        hover lumi("minia/minia61.webp")
                        xalign 0.5

                        action Jump ("repesexmorning")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay60 == True:
                    imagebutton:
                        idle "minia/minia60.webp"
                        hover lumi("minia/minia60.webp")
                        xalign 0.5

                        action Jump ("repesexparty")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay62 == True:
                    imagebutton:
                        idle "minia/minia62.webp"
                        hover lumi("minia/minia62.webp")
                        xalign 0.5

                        action Jump ("repesexshower")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 2:
                if cheatdev == True or persistent.replay63 == True:
                    imagebutton:
                        idle "minia/minia63.webp"
                        hover lumi("minia/minia63.webp")
                        xalign 0.5

                        action Jump ("repberrybjcookanim026")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay64 == True:
                    imagebutton:
                        idle "minia/minia64.webp"
                        hover lumi("minia/minia64.webp")
                        xalign 0.5

                        action Jump ("repberryworkfacesitting026")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay129 == True:
                    imagebutton:
                        idle "minia/minia129.webp"
                        hover lumi("minia/minia129.webp")
                        xalign 0.5

                        action Jump ("repbercunparty100")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay65 == True:
                    imagebutton:
                        idle "minia/minia65.webp"
                        hover lumi("minia/minia65.webp")
                        xalign 0.5

                        action Jump ("repbfsexa027")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay66 == True:
                    imagebutton:
                        idle "minia/minia66.webp"
                        hover lumi("minia/minia66.webp")
                        xalign 0.5

                        action Jump ("repbsexmorninga027")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay67 == True:
                    imagebutton:
                        idle "minia/minia67.webp"
                        hover lumi("minia/minia67.webp")
                        xalign 0.5

                        action Jump ("repbsexpartya027")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay68 == True:
                    imagebutton:
                        idle "minia/minia68.webp"
                        hover lumi("minia/minia68.webp")
                        xalign 0.5

                        action Jump ("repbworksexa027")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 3:
                if cheatdev == True or persistent.replay81 == True:
                    imagebutton:
                        idle "minia/minia81.webp"
                        hover lumi("minia/minia81.webp")
                        xalign 0.5
                        action Jump ("repvaldevtwerk2028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay82 == True:
                    imagebutton:
                        idle "minia/minia82.webp"
                        hover lumi("minia/minia82.webp")
                        xalign 0.5
                        action Jump ("repvaldevtwerk1028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay83 == True:
                    imagebutton:
                        idle "minia/minia83.webp"
                        hover lumi("minia/minia83.webp")
                        xalign 0.5
                        action Jump ("repv3devb028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay85 == True:
                    imagebutton:
                        idle "minia/minia85.webp"
                        hover lumi("minia/minia85.webp")
                        xalign 0.5
                        action Jump ("repv3tap028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay84 == True:
                    imagebutton:
                        idle "minia/minia84.webp"
                        hover lumi("minia/minia84.webp")
                        xalign 0.5
                        action Jump ("repv3dev028")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay80 == True:
                    imagebutton:
                        idle "minia/minia80.webp"
                        hover lumi("minia/minia80.webp")
                        xalign 0.5
                        action Jump ("repvalcunkit028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay78 == True:
                    imagebutton:
                        idle "minia/minia78.webp"
                        hover lumi("minia/minia78.webp")
                        xalign 0.5
                        action Jump ("repvaloralgl028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay77 == True:
                    imagebutton:
                        idle "minia/minia77.webp"
                        hover lumi("minia/minia77.webp")
                        xalign 0.5
                        action Jump ("repvaloraljacc028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay76 == True:
                    imagebutton:
                        idle "minia/minia76.webp"
                        hover lumi("minia/minia76.webp")
                        xalign 0.5
                        action Jump ("repvaloralshower028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay75 == True:
                    imagebutton:
                        idle "minia/minia75.webp"
                        hover lumi("minia/minia75.webp")
                        xalign 0.5
                        action Jump ("repvalpjtv028")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay69 == True:
                    imagebutton:
                        idle "minia/minia69.webp"
                        hover lumi("minia/minia69.webp")
                        xalign 0.5
                        action Jump ("repvalsexparty028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay74 == True:
                    imagebutton:
                        idle "minia/minia74.webp"
                        hover lumi("minia/minia74.webp")
                        xalign 0.5
                        action Jump ("repvalsexbalc2028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay73 == True:
                    imagebutton:
                        idle "minia/minia73.webp"
                        hover lumi("minia/minia73.webp")
                        xalign 0.5
                        action Jump ("repvalsexby028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay72 == True:
                    imagebutton:
                        idle "minia/minia72.webp"
                        hover lumi("minia/minia72.webp")
                        xalign 0.5
                        action Jump ("repvalsexgl028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay79 == True:
                    imagebutton:
                        idle "minia/minia79.webp"
                        hover lumi("minia/minia79.webp")
                        xalign 0.5
                        action Jump ("repvalsexshower028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay74 == True:
                    imagebutton:
                        idle "minia/minia71.webp"
                        hover lumi("minia/minia71.webp")
                        xalign 0.5
                        action Jump ("repvalsexkitchen028")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay70 == True:
                    imagebutton:
                        idle "minia/minia70.webp"
                        hover lumi("minia/minia70.webp")
                        xalign 0.5
                        action Jump ("repvalsexmorning028")
                else:
                    add "minialocked" xalign 0.5


            if replaypage == 3:
                if cheatdev == True or persistent.replay100 == True:
                    imagebutton:
                        idle "minia/minia100.webp"
                        hover lumi("minia/minia100.webp")
                        xalign 0.5
                        action Jump ("repvaleriesexend031")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay107 == True:
                    imagebutton:
                        idle "minia/minia107.webp"
                        hover lumi("minia/minia107.webp")
                        xalign 0.5
                        action Jump ("repvaleriealtv033")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay114 == True:
                    imagebutton:
                        idle "minia/minia114.webp"
                        hover lumi("minia/minia114.webp")
                        xalign 0.5
                        action Jump ("repvalfjjacc034")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay115 == True:
                    imagebutton:
                        idle "minia/minia115.webp"
                        hover lumi("minia/minia115.webp")
                        xalign 0.5
                        action Jump ("repvaldhjjacc034")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay120 == True:
                    imagebutton:
                        idle "minia/minia120.webp"
                        hover lumi("minia/minia120.webp")
                        xalign 0.5
                        action Jump ("repvalanalcook034")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 2:
                if cheatdev == True or persistent.replay88 == True:
                    imagebutton:
                        idle "minia/minia88.webp"
                        hover lumi("minia/minia88.webp")
                        xalign 0.5
                        action Jump ("repbersexshower029")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay89 == True:
                    imagebutton:
                        idle "minia/minia89.webp"
                        hover lumi("minia/minia89.webp")
                        xalign 0.5
                        action Jump ("repbersexby029")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay93 == True:
                    imagebutton:
                        idle "minia/minia93.webp"
                        hover lumi("minia/minia93.webp")
                        xalign 0.5
                        action Jump ("repberrysexbalcony2030")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay94 == True:
                    imagebutton:
                        idle "minia/minia94.webp"
                        hover lumi("minia/minia94.webp")
                        xalign 0.5
                        action Jump ("repberrysexkitchen030")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay97 == True:
                    imagebutton:
                        idle "minia/minia97.webp"
                        hover lumi("minia/minia97.webp")
                        xalign 0.5
                        action Jump ("repberrysexend031")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay103 == True:
                    imagebutton:
                        idle "minia/minia103.webp"
                        hover lumi("minia/minia103.webp")
                        xalign 0.5
                        action Jump ("repisabelleberrysex032")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay108 == True:
                    imagebutton:
                        idle "minia/minia108.webp"
                        hover lumi("minia/minia108.webp")
                        xalign 0.5
                        action Jump ("repberrycuntv033")
                else:
                    add "minialocked" xalign 0.5



                if cheatdev == True or persistent.replay113 == True:
                    imagebutton:
                        idle "minia/minia113.webp"
                        hover lumi("minia/minia113.webp")
                        xalign 0.5
                        action Jump ("repberfootjjacc034")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay121 == True:
                    imagebutton:
                        idle "minia/minia121.webp"
                        hover lumi("minia/minia121.webp")
                        xalign 0.5
                        action Jump ("repbertjjacc034")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay125 == True:
                    imagebutton:
                        idle "minia/minia125.webp"
                        hover lumi("minia/minia125.webp")
                        xalign 0.5
                        action Jump ("repbertjcook034")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay126 == True:
                    imagebutton:
                        idle "minia/minia126.webp"
                        hover lumi("minia/minia126.webp")
                        xalign 0.5
                        action Jump ("repberanalcook034")
                else:
                    add "minialocked" xalign 0.5


            if replaypage == 1:
                if cheatdev == True or persistent.replay87 == True:
                    imagebutton:
                        idle "minia/minia87.webp"
                        hover lumi("minia/minia87.webp")
                        xalign 0.5
                        action Jump ("repemmsexpcroom029")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay96 == True:
                    imagebutton:
                        idle "minia/minia96.webp"
                        hover lumi("minia/minia96.webp")
                        xalign 0.5
                        action Jump ("repemmasexkitchen030")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay95 == True:
                    imagebutton:
                        idle "minia/minia95.webp"
                        hover lumi("minia/minia95.webp")
                        xalign 0.5
                        action Jump ("repemmasexby030")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay98 == True:
                    imagebutton:
                        idle "minia/minia98.webp"
                        hover lumi("minia/minia98.webp")
                        xalign 0.5
                        action Jump ("repemmasexend031")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay101 == True:
                    imagebutton:
                        idle "minia/minia101.webp"
                        hover lumi("minia/minia101.webp")
                        xalign 0.5
                        action Jump ("repemmabjgf032")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay102 == True:
                    imagebutton:
                        idle "minia/minia102.webp"
                        hover lumi("minia/minia102.webp")
                        xalign 0.5
                        action Jump ("repemmagfsex032")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay111 == True:
                    imagebutton:
                        idle "minia/minia111.webp"
                        hover lumi("minia/minia111.webp")
                        xalign 0.5
                        action Jump ("repsemmakisstv033")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay110 == True:
                    imagebutton:
                        idle "minia/minia110.webp"
                        hover lumi("minia/minia110.webp")
                        xalign 0.5
                        action Jump ("repemmafcuntv033")
                else:
                    add "minialocked" xalign 0.5


                if cheatdev == True or persistent.replay116 == True:
                    imagebutton:
                        idle "minia/minia116.webp"
                        hover lumi("minia/minia116.webp")
                        xalign 0.5
                        action Jump ("repemmtmassjacc034")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay117 == True:
                    imagebutton:
                        idle "minia/minia117.webp"
                        hover lumi("minia/minia117.webp")
                        xalign 0.5
                        action Jump ("repemmtfjacc034")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay123 == True:
                    imagebutton:
                        idle "minia/minia123.webp"
                        hover lumi("minia/minia123.webp")
                        xalign 0.5
                        action Jump ("repemmanalcook034")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay124 == True:
                    imagebutton:
                        idle "minia/minia124.webp"
                        hover lumi("minia/minia124.webp")
                        xalign 0.5
                        action Jump ("repemmajcook034")
                else:
                    add "minialocked" xalign 0.5



            if replaypage == 0:
                if cheatdev == True or persistent.replay86 == True:
                    imagebutton:
                        idle "minia/minia86.webp"
                        hover lumi("minia/minia86.webp")
                        xalign 0.5
                        action Jump ("repsarsexliving029")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay90 == True:
                    imagebutton:
                        idle "minia/minia90.webp"
                        hover lumi("minia/minia90.webp")
                        xalign 0.5
                        action Jump ("repsarsexbalc029")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay91 == True:
                    imagebutton:
                        idle "minia/minia91.webp"
                        hover lumi("minia/minia91.webp")
                        xalign 0.5
                        action Jump ("repsarsexshower029")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay92 == True:
                    imagebutton:
                        idle "minia/minia92.webp"
                        hover lumi("minia/minia92.webp")
                        xalign 0.5
                        action Jump ("repsarsexbalc2029")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay99 == True:
                    imagebutton:
                        idle "minia/minia99.webp"
                        hover lumi("minia/minia99.webp")
                        xalign 0.5
                        action Jump ("repsarenasexend031")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay112 == True:
                    imagebutton:
                        idle "minia/minia112.webp"
                        hover lumi("minia/minia112.webp")
                        xalign 0.5
                        action Jump ("repsarenakisstv033")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay109 == True:
                    imagebutton:
                        idle "minia/minia109.webp"
                        hover lumi("minia/minia109.webp")
                        xalign 0.5
                        action Jump ("repsarenanstv033")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay118 == True:
                    imagebutton:
                        idle "minia/minia118.webp"
                        hover lumi("minia/minia118.webp")
                        xalign 0.5
                        action Jump ("repsartmassjacc034")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay119 == True:
                    imagebutton:
                        idle "minia/minia119.webp"
                        hover lumi("minia/minia119.webp")
                        xalign 0.5
                        action Jump ("repsartjjacc034")
                else:
                    add "minialocked" xalign 0.5
                if cheatdev == True or persistent.replay122 == True:
                    imagebutton:
                        idle "minia/minia122.webp"
                        hover lumi("minia/minia122.webp")
                        xalign 0.5
                        action Jump ("repsaranalcook034")
                else:
                    add "minialocked" xalign 0.5

            if replaypage == 4:

                if cheatdev == True or persistent.replay104 == True:
                    imagebutton:
                        idle "minia/minia104.webp"
                        hover lumi("minia/minia104.webp")
                        xalign 0.5
                        action Jump ("repisabellesex032")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay105 == True:
                    imagebutton:
                        idle "minia/minia105.webp"
                        hover lumi("minia/minia105.webp")
                        xalign 0.5
                        action Jump ("repisabelletj032")
                else:
                    add "minialocked" xalign 0.5

                if cheatdev == True or persistent.replay106 == True:
                    imagebutton:
                        idle "minia/minia106.webp"
                        hover lumi("minia/minia106.webp")
                        xalign 0.5
                        action Jump ("repisabellesex2032")
                else:
                    add "minialocked" xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
