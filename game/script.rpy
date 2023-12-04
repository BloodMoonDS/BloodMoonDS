# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
define sounds = ["audio/Voices/voice_hugo.ogg","audio/Voices/voice_alice.ogg","audio/Voices/voice_kenia.ogg","audio/Voices/voice_camacho.ogg"]

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[0]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v
    def type_sound_Alice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[1]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
           


        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
        
    def type_sound_kenia(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[2]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
           


        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def type_sound_camacho(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[3]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
           


        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

# El juego comienza aquí.

# define hugo = Character("hugo",color="#00FBFE",callback=type_sound)
# define alice = Character("alice",color="#f600fe",callback=type_sound_Alice)
# define kenia = Character("kenia",color="#ff7e7e",callback=type_sound_kenia)
# define camacho = Character("camacho",color="#73ff00",callback=type_sound_camacho)
define Bloodiey = Character("Bloodiey",color="#0011ff",callback=type_sound)
label start:
    scene bg classroom

    show bloodiey happy
    Bloodiey "..."
    menu:
        "Coquetear":
            jump coquetear
        "Hablar":
            jump hablar
    label coquetear:
        "hola estas muy lindo jeje~"
        show bloodiey blush
        Bloodiey "Que?"
        Bloodiey "Ehhhhh..."
        Bloodiey "Oye creo que todavia es muy temprando y no deberiamos hacer eso uhhh..."
        menu:
            "Coquetear":
                jump coquetear2
            "Hablar":
                jump hablar2
        label coquetear2:
            "Que ganas de darte bien el el orto"
            show bloodiey blush shame
            Bloodiey "EHHHHHHHH!?"
            Bloodiey "Espera Ehhhhhhh no... puedo"
            Bloodiey "Tengo que hacer Mi plataforma y..."
            "Shhhhhhhhhh"
            "Solo es una noche es lunes todavia tienes toda la semana"
            "podemos pasar la noche juntos 7u7"
            Bloodiey "eeeeh..."
            jump game_end
        label hablar2:
        jump game_end

    label hablar:
        Bloodiey "Hola jeje"
    label game_end:

    return
