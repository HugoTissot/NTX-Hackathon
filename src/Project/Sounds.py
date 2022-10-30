from synthesizer import Player, Synthesizer, Waveform
from timeflux.core.node import Node
from pychord import Chord
import numpy as np
import pandas as pd
import time


player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=2.0, use_osc2=False)
# Play A4
#player.play_wave(synthesizer.generate_constant_wave(440.0, 3.0))

# Play C major
#player.play_wave(synthesizer.generate_chord(chord, 3.0))
#sound1 = ["C4", "E4", "D4"]
#sound2 = ["D3", "A4", "G4"]
#sound3 = ["A3", "E3", "D4"]
#sound4 = ["C3", "G4", "E4"]

arp1 = ['E9/C', 'E9/G', 'E9/A']
arp2 = ['E9/C', 'E7/G', 'E9/A']
arp3 = ['E7/G', 'E7/G', 'E7/A']
arp4 = ['B9/C', 'B9/G', 'B7/A']


period = 0.2

class SoundMaker(Node) :
    
    def __init__(self) :
        pass
    
    def update(self) :
        
        if not self.i.ready():
            return
        
        
        print('Input')
        print(self.i.data.mean())
        pc1 = self.i.data.mean()[0]
        pc2 = self.i.data.mean()[1]
        if pc1 > 0 and pc2 > 0 :
            chord = Chord(arp1[0])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.07)
            chord = Chord(arp1[1])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.07)
            chord = Chord(arp1[2])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.5)
            
        elif pc1 > 0 and pc2 <= 0 :
            chord = Chord(arp2[0])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.07)
            chord = Chord(arp2[1])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.07)
            chord = Chord(arp2[2])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.5)
            
        elif pc1 <= 0 and pc2 > 0 :
            chord = Chord(arp3[0])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.07)
            chord = Chord(arp3[1])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.07)
            chord = Chord(arp3[2])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.5)
            
        else :
            chord = Chord(arp4[0])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.07)
            chord = Chord(arp4[1])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.07)
            chord = Chord(arp4[2])
            player.play_wave(synthesizer.generate_chord(chord.components_with_pitch(root_pitch=3),period))
            time.sleep(0.5)


class EEG_sonification(Node) :
    
    def __init__(self) :
        pass
    
    def update(self) :
        
        if not self.i.ready():
            return
        
        
        print('Input')
        print(self.i.data.mean())
        f = float(self.i.data.mean())
        print(float(self.i.data.mean()))
        if f > 0 :
            player.play_wave(synthesizer.generate_chord(sound1,1.0))
        else :
            player.play_wave(synthesizer.generate_chord(sound2,1.0))
