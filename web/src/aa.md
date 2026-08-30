# dnf

### dnf usage
sudo dnf install/remove/... { package-names: __required__ } - abbr: sudo dnf in/rm<br>
sudo dnf update/upgrade/... { package-names: __optional__ } - abbr: sudo dnf up<br>

### /etc/dnf/dnf.conf
max\_parallel\_downloads=1<br>
install\_weak\_deps=False<br>
exclude=flameshot

### /etc/yum.repos.d
this directory store files which is linked to specific mirror (or repository)



# rpm - manual install from file

### rpm usage
sudo rpm -i  # install<br>
sudo rpm -e  # erase (not recommended, use dnf rm instead)<br>
sudo rpm -U  # upgrade<br>
sudo rpm -qa # show all packages installed
