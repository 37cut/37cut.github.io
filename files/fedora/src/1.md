# dnf

### dnf usage
sudo dnf install/remove/... { package-names: __required__ } - abbr: sudo dnf in/rm<br>
sudo dnf update/upgrade/... { package-names: __optional__ } - abbr: sudo dnf up,<br>

### /etc/dnf/dnf.conf
max\_parallel\_downloads=1<br>
install\_weak\_deps=False<br>
exclude=flameshot


### /etc/yum.repos.d
this directory stores different repositories

