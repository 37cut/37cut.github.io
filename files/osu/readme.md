## Setup

```yaml
OS: Fedora x86_64 43

Mouse: g102 1600dpi x1.0 no-raw-input
Keyboard: o2c with greywood switch v3

Sound-Server: Pulseaudio
Config:
  default-sample-format = s16le
  default-sample-rate = 44100
  alternate-sample-rate = 48000
  default-sample-channels = 6
  default-channel-map = front-left,front-right,rear-left,rear-right,lfe

  # base-offset = 20ms (4 * 5)
  default-fragments = 4
  default-fragment-size-msec = 5

  # offset = about 22ms (base-offset + 2048us / 1000)
  enable-deferred-volume = yes
  deferred-volume-safety-margin-usec = 2048
  deferred-volume-extra-delay-usec = 0
```
