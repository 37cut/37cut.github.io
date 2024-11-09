# Editor
- Audio Edit: audacity
- Graphic Edit: gimp

# Content
- Audio
- Interface
- Mode

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
- Font: "Cute Aurora"-116px
- Drop shadow:
	- color: #000000
	- blur radius: 1
	- grow radius: 1
	- opacity: 1

___***Interface***___

# Interface::Arrow::arrow-pause
- Canva: 192x96
- Font: Philosopher-96px
- Color: #eeffcc
- Drop shadow:
	- color: #eeffcc
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Song-select::songselect-{top,bottom}
- Canva: 2732x1536(top), 2732x200(bottom) 
- Color: #111111
- songselect-top::Character-songselect-top.xcf layer:
	- Drop shadow:
		- x,y: 5,5
		- blur radius: 4
		- grow radius: 0
		- opacity: 0.25
- Drop shadow:
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Selection::selection-tab
- Canva: 236x44
- Size: 194x36
- Position: Right bottom
- Color: #ffffff

# Interface::Selection::selection-{mode,mods,options,random}
- Canva: 188x180(mode), 160x180(mods,options,random)
- Font: Philosopher-44px(mode,mods), Philosopher-32px(mode,mods)  
- Color: #222222
- Drop shadow:
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Selection::selection-{mode,mods,options,random}-over
- Canva: 188x180(mode), 160x180(mods,options,random)
- Font: Philosopher-44px(mode,mods), Philosopher-32px(mode,mods)  
- Color: #333333
- Drop shadow:
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::spinner-rpm
- Canva: 176x96
- Font: Constantia-64px
- Drop shadow:
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Play::play-unranked
- Canva: 512x128
- Color: #ffffcc
- Font: Philosopher-96px
- Drop shadow:
	- color: #ffffcc
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Play::play-skip
- Canva: 928x460
- Font: Candara-340px
- Character-skip.xcf Layer:
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
- Font: Constantia-80px
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
- Panel::Character-panel.xcf Layer:
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
- Font: Mingzat-80px
- Color: #f3ffcc
- Drop shadow:
	- x,y: 5,5
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Interface::Ranking::ranking-title
- Canva: 620x272
- Font: Candara-172px
- Color: #eeffcc
- Drop shadow:
	- color: #bbcc99
	- blur radius: 2
	- grow radius: 0
	- opacity: 2

# Interface::Ranking::ranking-{X,S,A,B,C,D,SH,XH}-small
- Canva: 68x80
- Font: "Source Code Pro Light Italic"-64px
- Color: #ffcc66(X,S), #ccff66, #66ccff, #cc66ff, #ff6666, #cccccc(SH,XH)
- Drop shadow:
	- color: #ff9966(X,S), #99ff66, #6699ff, #9966ff, #ff3333, #999999(SH,XH)
	- blur radius: 2
	- grow radius: 0
	- opacity: 1

# Interface::Ranking::ranking-{X,S,A,B,C,D,SH,XH}
- Canva: 768x768
- Font: "ft anima"-768px
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
- Font: Philosopher-82px(0-9), "Cute Aurora"-66px(c,d), "Cute Aurora"-33px(p,x)
- Drop shadow:
	- color: black once, white once
	- blur radius: 1
	- grow radius: 0
	- opacity: 0.5