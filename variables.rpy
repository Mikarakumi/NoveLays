# Relationships
default affection_igorina = 0
default Varpach_RS = 0

# Minigaems
# default text_to_type = "Функция называется непрерывной в некоторой точке, если сколь угодно малому изменению значений аргумента соответствует сколь угодно малое изменение значений функции при условии достаточной близости рассматриваемых значений аргумента к данной точке"


# Определение персонажей игры.
define I = Character('Игорина', color="#f7ff02ff")
define V = Character("Варпач", color="#ff9e2f96")
define S = Character("Серега", color="#c61400ff")
define R = Character("Руслан", color="#00e1ffff")
define K = Character("Ковалева", color="#ffb011ff")

define Unknown = Character("???", color="#ffffff")

# Characters
        # Варпач
image Varpach Base:
    "Characters/Varpach_Base.png"
    yalign 1.1
image Varpach Stand:
    "Characters/Varpach_Stand.png"
    zoom 1.35
image Varpach VM:
    "images/Characters/Varpach_Watermelon.png"
    yalign 1.5
        # Игорина
image Igorina Base:
    "Characters/Igorina_Base.png"
    zoom 0.9
    yalign 3.5
image Igorina Shy:
    "Characters/Igorina_Shy.png"
    zoom 0.9
    yalign 3.5
        # Серега
image Serega Base:
    "Characters/Serega_Base.png"
    zoom 1.3
    yalign 2.0
image Serega Strong = "Characters/Serega_Strong.png"

# CHR Icons (not working ATM)
image define varpach basic = "Characters/Varpach.png"

# Backgrounds

image bg RuslanRoom = "Backgrounds/RuslanRoom.jpg"
image bg RuslanBathroom = "Backgrounds/RuslanBathroom.png"
image bg MetroEnter = "Backgrounds/MetroStart0.png"
image bg MetroExit = "Backgrounds/MetroExit.jpg"
image bg CollegeEnter = "Backgrounds/CollegeEnter.jpg"
image bg Corridor = "Backgrounds/Corridor.jpg"
image bg AltCorridor = "Backgrounds/AltCOrridor.jpg"
image bg Floor b = im.Blur("Backgrounds/Floor.png", 2)
image bg EyeRuslanRoom = im.Blur("Backgrounds/EyeRuslanRoom.jpg", 3)
image bg MathClass = "Backgrounds/MathClass.png"
image bg EmptyMathClass = "Backgrounds/EmptyMathClass.png"
image bg OutOfMetro = "images/Backgrounds/out_of_metro0.png"
image bg NotebookMinigame = "images/Backgrounds/notebook_writing.png"
image bg TruckDeath = "images/Backgrounds/truck0.png"
image bg ExitCollege = "images/Backgrounds/ExitCollege0.png"

# Audio

define audio.clock = "Clock.mp3"
define audio.stopclock = "StopClock.mp3"
define audio.facewashing = "FaceWashing.mp3"
define audio.metroride = "MetroRide.mp3"
define audio.walk = "Walk.mp3"
define audio.zipper = "Zipper.mp3"
define audio.IgorinaRun = "audio/Игорина. Бег. Появление.mp3"
define audio.dressup = "audio/Одевает пиджак.mp3"
define audio.birds = "audio/Пение птиц на улице.mp3"
define audio.bump = "audio/Столкновение с Игориной.mp3"
define audio.run = "audio/Убегают от Сереги.mp3"
define audio.hit = "audio/Удары Сереги.mp3"
define audio.collegesounds = "audio/CollegeSounds.mp3"
define audio.penclick = "audio/shekchok-ruchki.mp3"
define audio.wokenup = "audio/wokenup.mp3"
define audio.deathcounteractivated = "audio/death-counter-activation-tsbg.mp3"
define audio.deathcounterlanded = "audio/death-counter-tsbg-the-strongest-hero-ult.mp3"
define audio.wakeupmusic = "audio/Antent_In_Your_Arms.mp3"
define audio.meetIgorina = "audio/Beskonechnoe_leto_-_Zvuki_drochki_(Zvyki.com).mp3"
define audio.sweetIgorina = "audio/Beskonechnoe_leto_-_A_Promise_From_Distant_Days_(Zvyki.com).mp3"
define audio.serega = "audio/MGR_R_-_Rules_of_Nature_Instrumental_-_Extension_(Zvyki.com).mp3"
define audio.hrust = "audio/hrust.mp3"
define audio.dtp = "audio/zvuk-avariya-avto.mp3"
define audio.point = "audio/vzmax_ruki.mp3"
define audio.tug = "audio/bed-sheet-movement_fytz-wvu.mp3"
define audio.motorcycle = "audio/motoc-mimo.mp3"
define audio.VarpachFM = "audio/Kavkaz_Starly_Kavkaz_Instagram_Version_Reverblaster_Kavkaz_TikTok.mp3"
