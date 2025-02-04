const scroll_height = document.documentElement.scrollHeight
const inner_height = window.innerHeight

const footer = document.createElement('div')
const return_home = document.createElement('div')
const return_homeContent = document.createElement('p')

footer.setAttribute('id', 'Footer')

return_home.setAttribute('class', '_button')
return_homeContent.appendChild(document.createTextNode('Return home.'))
return_home.appendChild(return_homeContent)
return_home.onclick = function() {window.location='../../'}

if (scroll_height > innerHeight) {
    const backto_top = document.createElement('div')
    const backto_topContent = document.createElement('p')

    backto_top.setAttribute('class', '_button')
    backto_topContent.appendChild(document.createTextNode('Back to top.'))
    backto_top.appendChild(backto_topContent)
    footer.appendChild(backto_top)

    backto_top.onclick = function() {
        window.scrollTo({
            top: 0, left: 0,
            behavior: 'smooth'})}
}

footer.appendChild(return_home)
document.body.appendChild(footer)
