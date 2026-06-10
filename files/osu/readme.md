## Setup

```yaml
OS: Fedora x86_64 44

Mouse: G102 < 1600dpi, x1.0 >
Keyboard: Keychron K2 HE < K1, K2: Q, A >

Offset: -22ms
Sound-Server: Pulseaudio
```

## Fetch maps
```py
import requests
import os, pathlib

file = pathlib.Path('list.txt')
target = os.makedirs('src/', exist_ok = True)

with file.open('r', encoding='utf-8') as f:
    for ln in f:
        line = ln.strip()

        if line:
            resp = requests.get(f'https://osudl.org/s/{line}')
            print(f'GET: {line}')

            if resp.status_code != 404:
                with open(f'src/{line}.osz', 'wb') as out:
                    out.write(resp.content)

```

Create a file called list.txt, and write all your mapset ids inside this file.
