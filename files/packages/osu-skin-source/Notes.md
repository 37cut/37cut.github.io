# Editor
- Audio Edit: audacity
- Graphic Edit: gimp

# Content
- Audio: Store all audio files
- Interface: As the name
- Mode: 2/4 modes in osu
- Transparent: Useless widgets to hide

___***Osu***___

# Mode::Osu::approachcircle
- Canva: 272x272
- Color: #ffffff

# Mode::Osu::hitcirle
- Canva: 256x256
- Color: #ffffff and #000000
- Feather: 3px
- Drop shadow:
	- blur radius: 6
	- grow radius: 3
	- opacity: 2(max)

# Mode::Osu::{hit,sliderstart}cirleoverlay
- Canva: 256x256
- Color: #ffffff
- Feather: 2px
- Drop shadow:
	- blur radius: 2
	- grow radius: 3
	- opacity: 2(max)

# Mode::Osu::sliderb
- Canva: 256x256
- Color: #000000
- Feather: 3px
- Drop shadow:
    - blur radius: 6
    - grow radius: 3
    - opacity: 2(max)

# Mode::Osu::reversearrow
- Canva: 256x256
- Color: #ffffff
- Feather: 3px
- Drop shadow:
	- blur radius: 2
	- grow radius: 3
	- opacity: 2(max)

# Mode::Osu::Default::default-{0,1,2,3,4,5,6,7,8,9}
- Canva: 70x104
- Font: Cute Aurora
- Font size: 116px
- Drop shadow:
	- color: #000000
	- blur radius: 1
	- grow radius: 1
	- opacity: 1

___***Interface***___

# Interface::Arrow::arrow-pause
- Canva: 192x96
- Font: Philosopher
- Font size: 96px
- Color: #eeffcc
- Drop shadow:
	- color: #eeffcc
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Song-select::songselect-{top,bottom}
- Canva: 2732x1536(top), 2732x200(bottom) 
- Color: #111111
- songselect-top::Bottom layer:
	- Note: Path tool
	- Points(top left->top right): (0,1220),(440,1356),(784,1280),(1260,1356),(2732,1356)
	- Points(bottom left<-bottom right): (0,0),(2732,1536)
- Drop shadow:
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::selection-tab
- Canva: 236x44
- Size: 194x36
- Position: Right bottom
- Color: #ffffff

# Interface::spinner-rpm
- Canva: 176x96
- Font: Constantia
- Font size: 64px
- Drop shadow:
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Play::play-unranked
- Canva: 512x128
- Color: #ffffcc
- Font size: 96px
- Drop shadow:
	- color: #ffffcc
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Play::play-skip
- Canva: 928x460
- Font: Candara
- Font size: 340px
- 'Character.xcf' Layer:
	- Drop shadow:
		- x,y: 5,5
		- blur radius: 4
		- grow radius: 0
		- opacity: 0.25
- 'Skip' Layer:
	- Color: #eeffcc
	Long shadow:
		- style: fading(fixed length)
		- length: 32
		- color: #bbcc99
		
# Interface::menu-button-background
- Canva: 1412x212
- 'Any' Color: #000033
- 'Layer' Feather: 3px

# Interface::Cursor::cursor
- Canva: 128x128
- 'Paint' Layer:
	- Color: #000000
- 'Padding' Layer:
	- Color: #ffffff 
- 'Cursor' Layer:
	- Color: #ffff80
	- Item Size: 80x80
- 'Blur' Layer:
	- Focus Blur(Gaussian Blur)
	- 3px
	- High quality
	
# Interface::Cursor::cursortrail
- Canva: 128x128
- Color: #ffffcc
- Focus Blur(Gaussian Blur):
	- 3px
	- High quality

# Interface::Cursor::cursor-smoke
- Canva: 16x16
- Feather: 3px
- Color: #eeffcc

# Interface::Pause::pause-{back,continue,replay,retry}
- Canva: 768x128
- Font: Constantia
- Font size: 80px
- Color: #eeffcc
- Drop shadow:
	- color: #eeffcc
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Ranking::ranking-graph
- Canva: 632x320
- Color: #eeffcc
- Drop shadow:
	- color: #bbcc99
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Ranking::ranking-panel
- Canva: 1920x1332
- Color: #eeffcc, #111111, #000000
- 'Panel::Character.xcf' Layer:
	- Position: Right Bottom
	- Drop shadow:
		- x,y: 5,5
		- blur radius: 4
		- grow radius: 0
		- opacity: 0.25
- 'Panel::PanelWidget::Score' Layer:
	- Font: Candara
	- Font size: 96px
	- Color: #ffffff
	- Drop shadow:
		- x,y: 10,10
		- blur radius: 8
		- grow radius: 0
		- opacity: 1

# Interface::Ranking::ranking-{accuracy,maxcombo}
- Canva: 448x128(accuracy), 320x128(accuracy)
- Font: Mingzat
- Font size: 80px
- Color: #f3ffcc
- Drop shadow:
	- x,y: 5,5
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Ranking::ranking-title
- Canva: 620x272
- Font: Candara
- Font size: 172px
- Color: #eeffcc
- Drop shadow:
	- color: #bbcc99
	- blur radius: 2
	- grow radius: 0
	- opacity: 2

# Interface::Ranking::ranking-{X,S,A,B,C,D,SH,XH}-small
- Canva: 68x80
- Font: Source Code Pro Light Italic
- Font size: 64px
- Color: #ffcc66(X,S), #ccff66, #66ccff, #cc66ff, #ff6666, #cccccc(SH,XH)
- Drop shadow:
	- color: #ff9966(X,S), #99ff66, #6699ff, #9966ff, #ff3333, #999999(SH,XH)
	- blur radius: 2
	- grow radius: 0
	- opacity: 1

# Interface::Ranking::ranking-{X,S,A,B,C,D,SH,XH}
- Canva: 768x768
- Font: ft anima
- Font size: 768px
- Color: #f3ffcc, #eeffcc(S,A), #bbcc99(B,C,D), #eeffdd, #f3ffdd
- Drop shadow(For ranking-{B,C,D}):
	- color: #999999
	- blur radius: 8
	- grow radius: 0
	- opacity: 0.5
- Drop shadow(except ranking-{B,C,D}):
	- color: same as Color
	- blur radius: 8
	- grow radius: 0
	- opacity: 0.5

# Interface::Score::score-{0,1,2,3,4,5,6,7,8,9}
- Canva: 48x80(0-9), 24x80(c,d,p,x)
- Font: Philosopher(0-9), Cute Aurora(c,d,p,x)
- Font size: 82px(0-9), 66px(c,d), 33px(p,x)
- Drop shadow:
	- color: black once, white once
	- blur radius: 1
	- grow radius: 0
	- opacity: 0.5