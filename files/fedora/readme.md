# Fedora
https://alt.fedoraproject.org

## Config
Switch your current workspace to tty4 (ctrl + alt + f4) before editing these files

### things to add
- alacritty
- alsa-plugins-pulseaudio
- chromium
- dbus-x11
- dunst
- feh
- gimp
- gvfs-archive
- htop
- i3
- ibus ___;remove it first___
- ibus-setup
- ibus-pinyin
- light
- mousepad
- mpv
- NetworkManager-tui
- pcmanfm
- picom
- tlp
- vim-enhanced
- xarchiver
- xsecurelock
- zsh
- zsh-autosuggestions
- zsh-syntax-highlighting

### things to remove
- abrt
- firefox
- gnome-abrt
- gnome-disk-utility
- nano
- nfs-utils
- pavucontrol
- plymouth
- setroubleshoot
- xorg-x11-drv-{intel,amdgpu,ati,nouveau,openchrome,qxl,vmware}
- xfce4-terminal
- {amd,nvidia}-gpu-firmware
- {amd-ucode,mt7xxx}-firmware
- {atheros,brcmfmac,libertas,nxpwireless,qcom-wwan,tiwilink}-firmware
- cirrus-audio-firmware
- lightdm ___;beware this___

### my configs
Download [here](https://cutt37.is-a.dev/files/fedora/files.cutt37)
- .zshrc                        -> $HOME
- alacritty.toml                -> $HOME/.config/alacritty
- config                        -> $HOME/.config/i3
- dunstrc                       -> $HOME/.config/dunst
- mimeapps.list                 -> /usr/share/applications
- 50-mouse-acceleration.conf    -> /usr/share/X11/xorg.conf.d
- environment                   -> /etc
- vimrc                         -> /etc
- i3status.conf                 -> /etc
- tlp.conf                      -> /etc
- picom.conf                    -> /etc/xdg
- xdm/xdm-config                -> /etc/X11/xdm
- xdm/Xresources                -> /etc/X11/xdm
- xdm/Xsetup                    -> /etc/X11/xdm

## Settings

### dnf
Edit /etc/dnf/dnf.conf
- `max_parallel_downloads=1`
- `install_weak_deps=False`
- `exclude=flameshot`

### Audio Server: pipewire -\> pulseaudio
```shell
sudo dnf rm pipewire\*
sudo dnf in pulseaudio
```

and add these code to /etc/asound.conf:
```shell
pcm.!default {
    type pulse
}

ctl.!default {
    type pulse
}
```

___This part is supplement___ <br>
Edit /usr/share/alsa/ucm2/Intel/sof-hda-dsp/HiFi-sof.conf

Find ___cset "name='${var:PostMixerAnalogPlaybackDrcSwitch ${var:\_\_drcswitch}"___ <br>
Then replace '${var:\_\_drcswitch}' to 'off'

Example /etc/pulse/daemon.conf file:<br>
```ini
default-sample-format = s16le
default-sample-rate = 44100
alternate-sample-rate = 48000
default-sample-channels = 6
default-channel-map = front-left,front-right,rear-left,rear-right,front-center,lfe
```

### Display Manager: lightdm -\> xorg-x11-xdm
```shell
sudo dnf rm lightdm
sudo dnf in xorg-x11-xdm
```

Create .xsession: `touch .xsession && echo i3 > .xsession`<br>
Make file executeable: `chmod +x .xsession`<br>
Then run this command to activate xdm:<br>
`systemctl set-default graphical.target`

and finally enable xdm.service

### 7zip -\> 7zip-standalone
Install 7zip-standalone, rather than 7zip.

### DPI Scale
See /etc/X11/Xresources<br>

### set default shell
`chsh -s /usr/bin/zsh`

### x264/265 video codec support - Intel
```shell
sudo dnf in https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf in intel-media-driver
```

### flameshot
```shell
sudo dnf in qt5-{qtbase,qttools} qt5-qtbase-gui
curl -L https://github.com/flameshot-org/flameshot/releases/download/v0.5.1/flameshot_0.5.1-fedora27-x86_64.rpm > flameshot_0.5.1-fedora27-x86_64.rpm
sudo rpm -i flameshot_0.5.1-fedora27-x86_64.rpm
```

### disable selinux
Edit /etc/selinux/config<br>
Find 'SELINUX=...' then replace 'enforcing' to 'disabled'.

`sudo grubby --update-kernel ALL --args selinux=0`

### disable \`default dirs
Edit $HOME/.config/user-dirs.dirs<br>
Remove the text inside the quotes.

### disable watchdog
Create /etc/modprobe.d/blacklist.conf<br>
Find your wdt via `lsmod`

Then add `blacklist your_module` into the file

### unused services
```shell
sudo systemctl disable avahi-daemon
sudo systemctl disable avahi-daemon.socket
```

### mask services
```shell
sudo systemctl mask sshd
sudo systemctl mask wsdd
sudo systemctl mask NetworkManager-wait-online.service
sudo systemctl mask NetworkManager-dispatcher.service
```

### Chromium Supplements
Go to ___chrome://flags___

Search ___gemini___ and disable every options include gemini keyword<br>
Search ___optimization guide on device___ and disable it

To prevent chrome download ai models into this folder -> ___$HOME/.config/chromium/OptGuideOnDeviceModel___ <br>
You could make this folder inmutable:<br>
`sudo chattr +i $HOME/.config/chromium/OptGuideOnDeviceModel/`

## Notes

### system upgrade
```shell
sudo dnf upgrade --refresh
sudo dnf system-upgrade download --releasever=XX
sudo dnf system-upgrade reboot
```

### update rescue kernel
```shell
sudo rm /boot/*rescue*
sudo kernel-install add "$(uname -r)" "/lib/modules/$(uname -r)/vmlinuz"
```

### remove old kernel
`sudo dnf remove $(dnf repoquery --installonly --latest-limit=-1)`
