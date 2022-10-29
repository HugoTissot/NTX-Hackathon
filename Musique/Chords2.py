#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from synthesizer import Player, Synthesizer, Waveform
from pychord import Chord


def main():
    player = Player()
    player.open_stream()

    print("play DM7/G chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = Chord("Dm7/G")
    player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=4), 1.0))
    time.sleep(2)



    print("play GCD chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = ["G4", "C4", "D4"]
    player.play_wave(synthesizer.generate_chord(chord, 1.0))
    time.sleep(2)

    print("play CFG chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = ["C4", "F4", "G4"]
    player.play_wave(synthesizer.generate_chord(chord, 1.0))
    time.sleep(0.4)

    print("play DGA chord")
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    chord = ["D4", "G4", "A4"]
    player.play_wave(synthesizer.generate_chord(chord, 1.0))
    time.sleep(0.4)

if __name__ == '__main__':
    main()