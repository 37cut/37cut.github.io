function selectById(e) {
	return document.getElementById(e)
}

/* BTT: Bottom To Top */
const buttonBTT = selectById('bottom-to-top');

buttonBTT.onclick = function() {
	window.scrollTo({top: 0, behavior: 'smooth'})
};
