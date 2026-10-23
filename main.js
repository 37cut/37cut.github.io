function init() {
    const img = document.createElement('img');
    const details = document.getElementsByTagName('details');
    
    const mobile = /Mobile|Android|iPhone/i.test(navigator.userAgent);
    
    img.src = 'https://cutt37.is-a.dev/src/Loli';
    img.id = 'fixed-image';

    img.style.position = 'fixed';
    img.style.pointerEvents = 'none';

    img.style.right = '8px';
    img.style.bottom = '8px';

    img.style.height = '72vh';
    img.style.opacity = '0.6';

    if (!mobile) {
        document.body.style.maxWidth = '1024px';
        document.body.style.marginInline = 'auto';
        document.body.style.paddingInline = '8px';

        img.style.right = getComputedStyle(document.body).marginRight;
    }
    
    else {
        document.documentElement.style.zoom = "75%";
        img.style.height = '85vh';
    }

    Array.from(details).forEach(details => {
        details.onclick = function () {
        img.animate(
            [
                { transform: 'translateY(0)', offset: 0 },
                { transform: 'translateY(-40px)', offset: .3 },
                { transform: 'translateY(-60px)', offset: .6 },
                { transform: 'translateY(-40px)', offset: .8 },
                { transform: 'translateY(-20px)', offset: .9 },
                { transform: 'translateY(0)', offset: 1 }
            ],

            {
                duration: 475,
                easing: 'ease-out'
            }

        )

        }
    })

    window.onresize = () => {
        img.style.right =
            getComputedStyle(document.body).marginRight;
    }

    document.body.appendChild(img);
    document.body.style.display = 'block';
    document.body.style.height = '95vh';
}

window.addEventListener('DOMContentLoaded', init)
