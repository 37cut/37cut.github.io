# Mode -> mode-{osu,taiko,catch,mania}-small
- Canva: 80x80
- Feather: 2px
- Color: #eeffcc
- Taiko: Stroke path: Paint: 6px, hardness: 25%
- Catch: Objects width: 16px
- Mania: Rounded corners: 32px

# menu-button-background
- Canva: 1412x212
- 'Any' Color: #000033
- 'Layer' Feather: 3px

# Song-select -> songselect-top
- Canva: 2732x1536(top)
- songselect-top > Character layer:
	- X Position: at 784px
    - Y Position: at 1536px
    - Drop shadow:
		- x,y: 5,5
		- blur radius: 12
		- grow radius: 0
		- opacity: 0.2
- songselect-top > Top layer:
    - Color: #111111, #eeffcc
    - Gaussian Blur: 0.6(Top ^ Decorate), 0.5(Top ^ Outline)
    - Drop shadow(exclude Shape, see fx):
		- blur radius: 4
		- grow radius: 0
		- opacity: 1
    - Drop shadow(Shape, see fx):
        - color: #eeffcc
		- blur radius: 4
		- grow radius: 0
		- opacity: 1
- songselect-top > Bottom layer:
    - Color: #111111, #222222
    - Drop shadow:
		- blur radius: 6
		- grow radius: 0
		- opacity: 1

# Song-select -> songselect-bottom
- Canva: 2732x192(bottom)
- songselect-bottom:
    - Color: #111111, #eeffcc
    - Drop shadow:
	    - blur radius: 6
	    - grow radius: 0
	    - opacity: 1

# Selection -> selection-tab
- Canva: 236x44
- Size: 194x36
- Position: Right bottom
- Color: #ffffff

# Selection -> selection-{mode,mods,options,random}
- Canva: 188x180(mode), 160x180(mods,options,random)
- Font: Philosopher-44px(mode,mods), Philosopher-32px(mode,mods)  
- Color: #222222
- Drop shadow:
	- blur radius: 4
	- grow radius: 0
	- opacity: 1

# Selection -> selection-{mode,mods,options,random}-over
- Canva: 188x180(mode), 160x180(mods,options,random)
- Font: Philosopher-44px(mode,mods), Philosopher-32px(mode,mods)  
- Color: #333333
- Drop shadow:
	- blur radius: 4
	- grow radius: 0
	- opacity: 1
