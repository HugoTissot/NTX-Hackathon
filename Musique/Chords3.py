#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from synthesizer import Player, Synthesizer, Waveform
from pychord import Chord

# Minor bank



def main():
    player = Player()
    player.open_stream()

#UN DEUX TROIS

    print("play E9/C chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/C")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E9/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E9/A chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/A")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.5)

# QUATRE CINQ SIX

    print("play E9/C chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/C")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E9/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E9/A chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/A")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.5)

#SEPT HUIT NEUF

    print("play E7/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E7/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E7/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E7/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E7/A chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E7/A")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.5)

#DIX ONZE DOUZE

    print("play B9/C chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("B9/C")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play B9/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("B9/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play B7/A chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("B7/A")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.5)

    #UN DEUX TROIS

    print("play E9/C chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/C")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E9/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E9/A chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/A")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.5)

# QUATRE CINQ SIX

    print("play E9/C chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/C")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E9/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E9/A chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E9/A")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.5)

#SEPT HUIT NEUF

    print("play E7/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E7/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E7/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E7/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play E7/A chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("E7/A")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.5)

#DIX ONZE DOUZE

    print("play B9/C chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("B9/C")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play B9/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("B9/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.07)

    print("play B9/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("B9/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3), 0.2))
    time.sleep(0.5)







    



  

if __name__ == '__main__':
    main()