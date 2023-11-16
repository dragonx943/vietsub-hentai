screen endingscreen:
    zorder 2
    modal True
    imagemap:
        ground "ui/UIending.webp"
        imagebutton:
            xalign 1.0
            yalign 0.0
            idle "closeui2"
            hover "closeui2hover"
            focus_mask True
            action Jump(lastmapcall)
    hbox:
        align (0.5,0.5)
        xsize 700
        box_wrap True

        if bstep==3 and vstep==3 and estep==3 and sstep==3 and isendmode == False:
            text "It's time for dinner!" size 50 outlines [ (1, "#1b1b1b", 0.5, 0.5) ] xalign 0.5
        elif estep ==4:
            text "Congratulations! You've finished the story of Confined with Goddesses." bold True size 30 color "#9d2d91" xalign 0.5
            text "That content will come in future game's updates, don't miss them:" bold True size 30 color "#9d2d91" xalign 0.5
            null height 100
            text "- Filling missing Jacuzzi and Cooking events." bold True size 30 color "#9d2d91" xalign 0.0
        elif estep == 3 and isendmode == True:
            text "Find every girls and talk to them." size 50 outlines [ (1, "#1b1b1b", 0.5, 0.5) ] xalign 0.0
        else:
            text "Special event will trigger once [bn], [sn], [vn], [en] are step 3." size 50 outlines [ (1, "#1b1b1b", 0.5, 0.5) ] xalign 0.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
