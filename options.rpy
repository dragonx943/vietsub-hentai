







define config.framerate = 30

define config.image_cache_size_mb = 100







define config.name = _("Confined with goddesses")






define gui.show_name = True




define config.version = "1.0premium"





define gui.about = _p("""
""")






define build.name = "Confined_with_goddesses"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True













define config.main_menu_music = "Audio/Musics/main.ogg"
define config.default_music_volume = 0.5


init python:
    renpy.music.register_channel("sex", "voice", True)
    renpy.music.register_channel("sexfx", "voice", True)
    renpy.music.register_channel("audiocum", "voice", False)








define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "Confinedwithgoddesses"






define config.window_icon = "gui/icon.ico"






init python:
    config.debug_sound = True



















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)



    build.archive("audio","all")
    build.archive("scripts","all")
    build.archive("archive1","all")
    build.archive("archive2","all")
    build.archive("archive3","all")
    build.archive("archive4","all")
    build.archive("archive5","all")
    build.archive("archivez","all")

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')


    build.classify('game/images/0.1/**.webp', 'archive1')
    build.classify('game/images/0.1.3/**.webp', 'archive1')
    build.classify('game/images/0.1.4/**.webp', 'archive1')
    build.classify('game/images/0.1.5/**.webp', 'archive1')

    build.classify('game/images/0.1.6/**.webp', 'archive2')
    build.classify('game/images/0.1.7/**.webp', 'archive2')
    build.classify('game/images/0.1.8/**.webp', 'archive2')
    build.classify('game/images/0.1.9/**.webp', 'archive2')

    build.classify('game/images/0.2/**.webp', 'archive3')
    build.classify('game/images/0.2.1/**.webp', 'archive3')
    build.classify('game/images/0.2.2/**.webp', 'archive3')
    build.classify('game/images/0.2.3/**.webp', 'archive3')


    build.classify('game/images/0.2.4/**.webp', 'archive4')
    build.classify('game/images/0.2.5/**.webp', 'archive4')
    build.classify('game/images/0.2.6/**.webp', 'archive4')
    build.classify('game/images/0.2.7/**.webp', 'archive4')
    build.classify('game/images/0.2.8/**.webp', 'archive4')

    build.classify('game/images/Characters/**.webp', 'archivez')
    build.classify('game/images/dreams/**.webp', 'archivez')
    build.classify('game/images/House/**.webp', 'archivez')
    build.classify('game/images/Characters/**.webp', 'archivez')
    build.classify('game/images/icons/**.webp', 'archivez')
    build.classify('game/images/other/**.webp', 'archivez')
    build.classify('game/images/ui/**.webp', 'archivez')
    build.classify('game/images/*.webp', 'archivez')

    build.classify('game/images/**.webp', 'archive5')




    build.classify('game/**.mp3', 'audio')
    build.classify('game/**.ogg', 'audio')
    build.classify('**.rpyc','scripts')
    build.classify('**.rpyc','scripts')
    build.classify('**.rpy','scripts')




    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
