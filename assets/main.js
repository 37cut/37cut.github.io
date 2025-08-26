class Element {
    constructor(text, func) {
        this.text = text
        this.func = func
    }

    createInstance() {
        const div = document.createElement('div')
        const p = document.createElement('p')

        div.setAttribute('class', '_button')

        div.onclick = this.func

        p.appendChild(document.createTextNode(this.text))
        div.appendChild(p)
        footer.appendChild(div)
    }
}

const scroll_height = document.documentElement.scrollHeight
const inner_height = window.innerHeight

const footer = document.createElement('div')
footer.setAttribute('id', 'footer')

const Home = new Element('Home.', function() { window.location = '../../' })
Home.createInstance()

if (scroll_height > innerHeight) {
    const Top = new Element('Back to Top.', function() {
        window.scrollTo({
            top: 0, left: 0,
            behavior: 'smooth'}) })
    Top.createInstance()
}

document.body.appendChild(footer)
