
init python:

    def allocate_screen(txt):
        global notifplaces
        notifplaces = []
        notifplaces.append (txt)
        renpy.hide_screen("notifglobal")
        renpy.show_screen("notifglobal")

    def write(txt):
        global notifplaces
        notifplaces = []
        notifplaces.append (txt)
        renpy.hide_screen("notifglobal")
        renpy.show_screen("notifglobal")

    def removenotif(txt):
        notifplaces.remove(txt)

define notifplaces = []

screen notifglobal:
    zorder 10
    vbox:
        spacing 10.0
        ypos 100
        xpos 10
        at shownotif
        for i in notifplaces:
            use notifelement(i)
            timer 4.5 action Function(removenotif, i)


screen notifelement(txt):
    zorder 10
    frame:
        style "my_style"
        text txt size 40



style my_style:
    background Frame("ui/awakeningtextbox.webp", 10, 10)
    xpadding 20
    ypadding 20

define writetemp = ""

transform shownotif:
    xalign 0.0 alpha 0.0
    linear 0.5 alpha 1.0
    pause 3.0
    linear 1.0 alpha 0.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
