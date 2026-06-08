# Sound

### Pipewire -\> Pulseaudio
```shell
sudo dnf rm pipewire\*
sudo dnf in pulseaudio
```

### /etc/asound.conf
```ini
05 pcm.!default {
06     type pulse
07 }
08
09 ctl.!default {
10     type pulse
11 }
```

### /etc/pulse/daemon.conf
```ini
...
81 default-sample-format = s16le
82 default-sample-rate = 44100
83 alternate-sample-rate = 48000
84 default-sample-channels = 6
85 default-channel-map = front-left,front-right,rear-left,rear-right,front-center,lfe
```

### /usr/share/alsa/ucm2/Intel/sof-hda-dsp/HiFi-sof.conf
```ini
...
56 If.spk {
57     Condition {
58         Type String
59         Empty "${var:spkvol}"
60     }
61     True.SectionDevice."Speaker" {
62         Macro.speaker.SofAnalogPlaybackControl "endpoint=Speaker drcswitch=off"
63     }
64 }
```
