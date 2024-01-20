const Footer = document.createElement('div')
const FooterContent = document.createElement('p')

FooterContent.appendChild(document.createTextNode('To top.'))
Footer.appendChild(FooterContent)
Footer.setAttribute('id', 'Footer')

if (document.documentElement.scrollHeight > window.innerHeight) {
	document.body.appendChild(Footer)
	Footer.style.textAlign='center'

	Footer.onclick = function() {
		window.scrollTo({
			top: 0,
			left: 0,
			behavior: 'smooth'
		})
	}
}
