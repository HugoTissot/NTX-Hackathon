from synthesizer import Player, Synthesizer, Waveform
from timeflux.core.node import Node
import numpy as np
import pandas as pd


player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=2.0, use_osc2=False)
# Play A4
#player.play_wave(synthesizer.generate_constant_wave(440.0, 3.0))

# Play C major
#player.play_wave(synthesizer.generate_chord(chord, 3.0))
sound1 = ["C4", "E4", "G4"]
sound2 = ["C4", "F4", "G4"]

class SoundMaker(Node) :
    
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
