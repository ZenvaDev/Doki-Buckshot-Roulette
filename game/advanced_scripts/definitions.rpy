#Definitions optimised by Zenva to make it easier to create mods by defining the stuff that team salvato and the ddlc monika after story team were to lazy to define
#Your welcome peoples 😭

#Advanced
#Only edit these if you know what you are doing
define persistent.demo = False
define persistent.steam = False
define config.developer = True #Change this flag to DISABLE dev tools (Dev tools on by default for your convenience)
#Note: You can use Shift + R in game to refresh your code without having to restart ;)

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)

#Audio section

#Music
define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)
define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Ohayou Sayori!
define audio.t2g = "bgm/2g.ogg" #Ohayou Sayori! (Wobbly 4 Second Section)
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg" #Ohayou Sayori! (Rapid Glitch Noise)
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg" #Ohayou Sayori! (Gradual Pitch Increase)
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg" #Main Theme (Off Key Notes)
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg" #Main Theme (Start From Weird Note)
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg" #Main Theme (Reverb + Strange Wet Noises [Before Yuri Cutting])
define audio.t3m = "<loop 4.618>bgm/3.ogg" #Main Theme (In game)
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame (Dreams of Love and Literature)
define audio.t4g = "<loop 1.000>bgm/4g.ogg" #Static + Error Noise
define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems...... 'Okay Everyone~!'
define audio.blankshell = "menu assets/blank_shell.ogg"

#Poem Music 
#The poem music is controlled directly in poems.rpy at the very bottom of the script
define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" #I'm the only one with pianos x3
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" #Hxppy Thoughts with Ukelele & Snapping~!
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" #Was it always cute on purpose?
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" #Fancy harps and instruments!

#SFX
define audio.t5b = "<loop 4.444>bgm/5.ogg" #Okay, Everyone!
define audio.t5c = "<loop 4.444>bgm/5.ogg" #Okay, Everyone!
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg" #Yuri/Natsuki theme (Bitcrushed Melody Piano)
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg" #Play With Me (Sped-up + Reversed)
define audio.t6s = "<loop 43.572>bgm/6s.ogg" #Play With Me (Yuri Death)
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Poem Panic!
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg" #Poem Panic! (First Melody Loop)
define audio.t7g = "<loop 31.880>bgm/7g.ogg" #Poem Panic (Act 2 Argument)
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #My feelings
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #My feelings (Harpsichord + Fast)
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #My Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg" #My Confession (Yuri)
define audio.td = "<loop 36.782>bgm/d.ogg" #Sayo-nara (Sayori's suicide)
define audio.m1 = "<loop 0>bgm/m1.ogg" #Just Monika.
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" #I Still Love You
define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg" #Ghost Menu Theme (Static + Weird Breathing)
define audio.g1 = "<loop 0>bgm/g1.ogg" #Low Sawtooth Wave (Sounds like an error)
define audio.g2 = "<loop 0>bgm/g2.ogg" #Lower Sawtooth Wave (Also sounds like an error, but worse)
define audio.hb = "<loop 0>bgm/heartbeat.ogg" #Heartbeat
define audio.closet_open = "sfx/closet-open.ogg" #Closet open sound
define audio.closet_close = "sfx/closet-close.ogg" #Closet close sound
define audio.page_turn = "sfx/pageflip.ogg" #Poem/Note pageflip
define audio.fall = "sfx/fall.ogg" #Falling sound

#Unnoriginal SFX
#Because i feel like getting certain assets or sounds for your mod can be hard for some newer people here are some free sounds and images~
#Ambient sounds
define audio.ext_day = "<loop 3.090>ambient/ext_day.ogg" #Day time sounds
define audio.ext_night = "<loop 4.103>ambient/ext_night.ogg" #Night time sounds
define audio.int_day = "<loop 3.090>ambient/int_day.ogg" #Inside a building day time sounds
define audio.int_night = "<loop 4.103>ambient/int_night.ogg" #Inside a building night time sounds
define audio.fountain = "<loop 1.801>ambient/fountain.ogg" #Fountain sound
define audio.bus = "<loop 3.247>ambient/bus.ogg" #Bus sound
define audio.wind = "<loop 2.069>ambient/wind.ogg" #Wind ambient sound
define audio.clifftop = "<loop 0.000>ambient/clifftop.ogg" #Heavy wind ambience
define audio.rain_ext = "<loop 2.094>ambient/rain_ext.ogg" #Rain outside building ambience
define audio.rain_int = "<loop 2.102>ambient/rain_int.ogg" #Rain inside building ambience
define audio.hb2 = "sfx/hb2.ogg"
define audio.tinnitus = "<loop 11.411 from 0 to 15.782>sfx/tinnitus.ogg"
define audio.clatter = "sfx/clatter.ogg"
define audio.phone = "sfx/phone.ogg"
define audio.slam = "sfx/slam.ogg"
define audio.carpass = "sfx/carpass.ogg"
define audio.dadcar = "<from 0 to 11.011 loop 1.735>sfx/dadcar.ogg"
define audio.dadcarend = "<from 11.011>sfx/dadcar.ogg"
define audio.beep = "sfx/beep.ogg"
define audio.microwave = "<loop 3.191>sfx/microwave.ogg"
define audio.camera_click = "sfx/camera_click.ogg"
define audio.siren_wail = "<loop 0>sfx/siren_wail.ogg"
define audio.siren_yelp = "<loop 0>sfx/siren_yelp.ogg"
define audio.thunder = "sfx/thunder.ogg"
define audio.doorbell = "sfx/doorbell.ogg"
define audio.thx = "sfx/thx.mp3"
define audio.caralarm = "<loop 4.530>sfx/caralarm.ogg"
define audio.gun = "sfx/gun.ogg"
define audio.kettle1 = "<from 0 to 42.342 loop 28.428>sfx/kettle.ogg"
define audio.kettle2 = "<from 42.342>sfx/kettle.ogg"
define audio.toaster = "sfx/toaster.ogg"
define audio.sofa_drop = "sfx/sofadrop.ogg"
define audio.bell = "sfx/bell.ogg"
define audio.scrape = "sfx/scrape.ogg"
define audio.stinger = "sfx/stinger.ogg"


# Backgrounds/Overlays
image black = "#000000" #Black background/Overlay
image dark = "#000000e4" #Dark background/Overlay
image darkred = "#110000c8" #Darker background/Overlay
image white = "#ffffff" #White background/Overlay
image splash = "bg/splash.png" #Team Salvato Splash screen
image end: #End screen/To avoid dealing with this dont leave ur code unfinished :p
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png" #Residential background daytime
image bg class_day = "bg/class.png" #Classroom (Not the literature club)
image bg corridor = "bg/corridor.png" #School corridor
image bg club_day = "bg/club.png" #Club room
image bg club_day2: #Jumpscare thing
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png" #Closet clubroom
image bg bedroom = "bg/bedroom.png" #MC'S Bedroom
image bg sayori_bedroom = "bg/sayori_bedroom.png" #Sayori's bedroom
image bg house = "bg/house.png" #Sayori's house
image bg kitchen = "bg/kitchen.png" #Just a kitchen
image bg notebook = "bg/notebook.png" #Poem notebook
image bg notebook-glitch = "bg/notebook-glitch.png" #Glitched notebook
image bg glitch = LiveTile("bg/glitch.jpg") #Glitch effect
image bg vill = "bg/vill.png" #pedophile
image menusplash = "menu assets/menusplash.png"

#Overlays/Moving backgrounds
image glitch_color: #Glitch animation
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

image glitch_color2: #Glitch animation colour variant
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

# Character Variables 
# These configure the shortcuts for writing dialog for each character.
# If you add new characters please for the love of god define them here
define narrator = Character(ctc="ctc", ctc_position="fixed") #Narrator (Stays blank)
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed") #MC in game name (player variable)
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed") #Sayori in game name
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed") #Monika in game name
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed") #Natsuki in game name
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed") #Yuri in game name
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed") #Nat and Yuri in game name
define _dismiss_pause = config.developer #I have no clue what this does so just leave it be


# Persistent Variables (ADVANCED)
# These values are automatically loaded/saved on game start and exit.
# These exist across all saves
# If you mess with these values and break something dont go complaining to me

default persistent.playername = "" #Player name changes only in the memory not in the code so dont mess with this
default player = persistent.playername #Defines player as the name that is chosen
default persistent.playthrough = 0 #Playthrough variable
default persistent.yuri_kill = 0 #0 by default as setting to 1 will make your game boot up as if yuri has been killed
default persistent.seen_eyes = None #Yuri cursed eyes scene
default persistent.seen_sticker = None #Doki stickers trigger
default persistent.ghost_menu = None #Changing this will make the game display the ghost menu
default persistent.seen_ghost_menu = None #Changing this will make the game act as if you have seen the ghost menu
default seen_eyes_this_chapter = False #Changing this will make the game act as if you have seen yur cursed eyes in the current chapter
default persistent.anticheat = 0 #Changing this to 1 will stop you from being able to skip as monika does in chapter 30
default persistent.clear = [False] #If save game has been cleared
default persistent.special_poems = None #If special poems (example: Yuri's piss paper poem) have been read
default persistent.clearall = None #If all save games have been cleared
default persistent.menu_bg_m = None #Changing this will play monikas menu background music instead of the base menu music
default persistent.first_load = None #Will replay the begining intro which for when you first load ddlc each time you start the game
default persistent.do_not_delete = None #Stops dokis from being deleted

# Other global variables (ADVANCED)
# It's good practice to define global variables here, just so you know what you can call later 
# Keep your code clean so monika stays happy
default in_sayori_kill = None #Changing this will make the game think sayori has killed herself
default in_yuri_kill = None #Changing this will make the game think yuri has killed herself
default anticheat = 0 #If you set this to 1 monika will punish you for skipping
define config.mouse = None #Something to do with the mouse try it yourself
default allow_skipping = True #Changing this to false will stop you from being able to skip
default basedir = config.basedir #Game base directory
default chapter = 0 #Pressing new game will load you into a further chapter pretty good for testing
default currentpos = 0 #Postion in the game playthrough
default faint_effect = None #Faint effect toggle
default s_name = "Sayori" #Sayori name
default m_name = "Monika" #Monika name
default n_name = "Natsuki" #Natsuki name
default y_name = "Yuri" #Yuri name

# Default poem appeal (These values change over time)
# Change this to rig the poem appeal 
default n_poemappeal = [0, 0, 0] #Natsuki poem appeal default value
default s_poemappeal = [0, 0, 0] #Sayori poem appeal default value
default y_poemappeal = [0, 0, 0] #Yuri poem appeal default value
default m_poemappeal = [0, 0, 0] #Monika poem appeal default value

# The last winner of the poem minigame (These values also change over time)
# Will always be sayori by default as this will change after the first poem minigame
default poemwinner = ['sayori', 'sayori', 'sayori'] #Sayori default poem winner (Change this for no reason)

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False #Sayori read poem default value
default n_readpoem = False #Natsuki read poem default value
default y_readpoem = False #Yuri read poem default value
default m_readpoem = False #Monika read poem default value

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0 #If any of the girls have read your poem

# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
# These work a bit different as only one point is added per poem per chapter
default n_appeal = 0 #Natsuki CHAPTER poem appeal default value
default s_appeal = 0 #Sayori CHAPTER poem appeal default value
default y_appeal = 0 #Yuri CHAPTER poem appeal default value
default m_appeal = 0 #Monika CHAPTER poem appeal default value

# We keep track of whether we watched Natsuki's and Yuri's second exclusive scenes
# to decide whether to play them in chapter 3.
# Editing these wont effect gameplay
default n_exclusivewatched = False #Changing this value to True will change if natsuki's exclusive scene has been watched
default y_exclusivewatched = False #Changing this value to True will change if yuri's exclusive scene has been watched

# Yuri runs away after the first exclusive scene of playthrough 2.
# Editing these wont effect gameplay
default y_gave = False #Changing this value to True will make the game assume you have watched Yuri's giving scene
default y_ranaway = False #Changing this value True make the game assume you have watched Yuri's running away scene

# We choose who to side with in chapter 1.
default ch1_choice = "sayori" #Sayori and monika are the only choice so maybe you could change this to change the course of the main game

# If we choose to help Sayori in ch3, some of the dialogue changes.
# Changing this will effect gameplay
default help_sayori = None #Choose to help sayori
default help_monika = None #Choose to help sayori

# We choose who to spend time with in chapter 4.
# Changing this will not effect gameplay
default ch4_scene = "yuri" #This will change if you choose a different character
default ch4_name = "Yuri" #This will change if you choose a different character
default sayori_confess = True #This will change if you don't want to confess to sayori for some reason

# We read Natsuki's confession poem in chapter 23.
# Changing this will not effect gameplay
default natsuki_23 = None #This will happen if you do the natsuki route so if you do the yuri route there is no point of this existing
