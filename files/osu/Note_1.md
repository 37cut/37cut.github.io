# Arrow -> arrow-pause
- Canva: 192x96
- Font: Philosopher-96px
- Color: #eeffcc
- Drop shadow:
	- color: #eeffcc
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Play -> play-unranked
- Canva: 512x128
- Color: #ffffcc
- Font: Philosopher-96px
- Drop shadow:
	- color: #ffffcc
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Play -> play-skip
- Canva: 928x460
- Font: "Louis George Cafe"-340px
- Character-skip.xcf Layer:
	- Drop shadow:
		- x,y: 5,5
		- blur radius: 4
		- grow radius: 0
		- opacity: 0.25
- 'Skip' Layer:
	- Color: #eeffcc
	- Drop shadow:
		- x,y: 10,10
		- blur radius: 0
		- grow radius: 0
		- opacity: 0.5
    - Drop shadow:
		- x,y: 20,20
		- blur radius: 0
		- grow radius: 0
		- opacity: 0.25

# Cursor -> cursor
- Canva: 272x272
- Color: #fcfcfc
- Drop shadow:
    - color: #cceeff
    - blur radius: 4
    - grow radius: 0
    - opacity: 0.5

# Cursor -> cursormiddle
- Canva: 272x272
- Color: #fcfcfc, #cceeff
- Drop shadow:
    - color: #cceeff
    - blur radius: 4
    - grow radius: 0
    - opacity: 0.5

# Cursor -> cursortrail
- Canva: 16x16
- Color: #cceeff
- Drop shadow:
    - color: #cceeff
    - blur radius: 2
    - grow radius: 0
    - opacity: 0.5


# Cursor -> cursor-smoke
- Canva: 16x16
- Gaussian Blur: 0.5
- Color: #3399cc

# Pause -> pause-{back,continue,replay,retry}
- Canva: 768x128
- Font: Constantia-80px
- Color: #eeffcc
- Drop shadow:
	- color: #eeffcc
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Ranking -> ranking-graph
- Canva: 632x320
- Font: "Louis George Cafe"-24px

# Ranking -> ranking-panel
- Canva: 1920x1332
- Color: #eeffcc, #111111, #000000
- Panel -> Character-panel.xcf:
	- Position: Right Bottom
	- Drop shadow:
		- x,y: 5,5
		- blur radius: 4
		- grow radius: 0
		- opacity: 0.25
- Panel -> PanelWidget -> Score:
	- Font: Candara
	- Font size: 96px
	- Color: #ffffff
	- Drop shadow:
		- x,y: 10,10
		- blur radius: 8
		- grow radius: 0
		- opacity: 1

# Ranking -> ranking-{accuracy,maxcombo}
- Canva: 448x128(accuracy), 320x128(maxcombo)
- Font: Mingzat-80px
- Color: #ffffff
- Drop shadow:
	- x,y: 5,5
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Ranking -> ranking-title
- Canva: 620x272
- Font: Candara-172px
- Color: #eeffcc
- Drop shadow:
	- color: #bbcc99
	- blur radius: 2
	- grow radius: 0
	- opacity: 2

# Ranking -> ranking-{X,S,A,B,C,D,SH,XH}-small
- Canva: 68x80
- Font: "Source Code Pro Light Italic"-64px
- Color: #ffcc66(X,S), #ccff66, #66ccff, #cc66ff, #ff6666, #cccccc(SH,XH)
- Drop shadow:
	- color: #ff9966(X,S), #99ff66, #6699ff, #9966ff, #ff3333, #999999(SH,XH)
	- blur radius: 2
	- grow radius: 0
	- opacity: 1

# Ranking -> ranking-{X,S,A,B,C,D,SH,XH}
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
