if (document.documentElement.scrollHeight > window.innerHeight) {
	const Footer = document.createElement('div')
	const FooterContent = document.createElement('p')

	FooterContent.appendChild(document.createTextNode('To top.'))
	Footer.appendChild(FooterContent)
	
	Footer.setAttribute('id', 'Footer')
	Footer.style.textAlign='center'
	Footer.style.backgroundColor='#2f2f2f'
	
	document.body.appendChild(Footer)

	Footer.onclick = function() {
		window.scrollTo({
			top: 0,
			left: 0,
			behavior: 'smooth'
		})
	}
}
