
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

const footer = document.createElement('div')
footer.setAttribute('id', 'footer')

const Profile = new Element('Return.', function() { window.location.href = "https://osu.ppy.sh/users/17589673" })
Profile.createInstance()

document.body.appendChild(footer)
