function init() {
    const img = document.createElement('img');
    const imb = document.getElementById('imb');
    const hover = document.getElementById('hover');
    
    const mobile = /Mobile|Android|iPhone/i.test(navigator.userAgent);
    
    img.src = 'https://cutt37.is-a.dev/web_assets/loli';
    img.id = 'fixed-image';

    img.style.position = 'fixed';
    img.style.pointerEvents = 'none';

    img.style.right = '8px';
    img.style.bottom = '8px';

    img.style.height = '72vh';
    img.style.opacity = '0';
    img.style.transition = 'opacity 0.5s';

    if (!mobile) {
        document.body.style.maxWidth = '1024px';
        document.body.style.marginInline = 'auto';
        document.body.style.paddingInline = '8px';
        
        hover.addEventListener('mouseover', function() {
            img.style.opacity = '0.6';
            img.style.right = window.getComputedStyle(document.body).marginRight;

            hover.style.fontWeight = 'bold';
        })

        hover.addEventListener('mouseout', function() {
            img.style.opacity = '0';
            img.style.right = window.getComputedStyle(document.body).marginRight;

            hover.style.fontWeight = 'normal';
        })

    }
    
    else {
        // mui_support();
        img.style.height = '60vh';
        
        hover.addEventListener('touchstart', function() {
            img.style.opacity = '0.6';
            hover.style.fontWeight = 'bold';
        })

        hover.addEventListener('touchend', function() {
            img.style.opacity = '0';
            hover.style.fontWeight = 'normal';
        })

    }

    document.body.appendChild(img);
    document.body.style.display = 'block';
    document.body.style.height = '95vh';
}

window.addEventListener('DOMContentLoaded', init)
