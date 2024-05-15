const Footer = document.createElement('div')
const ToIndex = document.createElement('div')
const ToIndexContent = document.createElement('p')

Footer.setAttribute('id', 'Footer')
ToIndex.setAttribute('class', 'functionbuttons')
ToIndexContent.appendChild(document.createTextNode('To index.'))
ToIndex.appendChild(ToIndexContent)

if (document.documentElement.scrollHeight > window.innerHeight) {
	const ToTop = document.createElement('div')
	const ToTopContent = document.createElement('p')

	ToTop.setAttribute('class', 'functionbuttons')
	ToTopContent.appendChild(document.createTextNode('To top.'))
	ToTop.appendChild(ToTopContent)
	Footer.appendChild(ToTop)
	
	ToTop.onclick = function() {
		window.scrollTo({
			top: 0, left: 0,
			behavior: 'smooth'})}
}

ToIndex.onclick = function() {
		window.location='../../'}

Footer.appendChild(ToIndex)
document.body.appendChild(Footer)