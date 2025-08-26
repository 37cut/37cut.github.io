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

const Return = new Element('Return.', function() { window.history.back() })
const Page0 = new Element('0', function() { window.location.href = "./cutt37" })
// const Page1 = new Element('1', function() { window.location.href = "./comment" })

Return.createInstance()
Page0.createInstance()
// Page1.createInstance()

document.body.appendChild(footer)
