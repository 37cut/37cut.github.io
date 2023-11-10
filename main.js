function amountToIndex(e) {
	// Array(index) starts from 0.
	return e.length - 1;
}

// Selectors
function selectAll(e) {
	return document.querySelectorAll(e);
}

function selectById(e) {
	return document.getElementById(e);
}

// t: type, e: elements, l: limit, s: step.
// bg&fg: background&foreground(font color).
// zae: Zero and even, o: odd.
function colorScheme(t, e, l, s, bg, fg) {
	if (t=='zae') {
		for (let i = 0; i <= l; i += s) {
			e[i].style.backgroundColor = bg;
			e[i].style.color = fg;
			// console.log("Zero+Even:",i);
		}		
	} else if (t=='o') {
		for (let i = 1; i <= l; i += s) {
			e[i].style.backgroundColor = bg;
			e[i].style.color = fg;
			// console.log("Odd:",i);
		}
	} else {
		return 0;
	}
}

// Select elements.
const section = selectAll('#section');
const footer = document.getElementById("Footer");

// Index.
const sectionIndex = amountToIndex(section);

// DEBUG
// console.log(importantTagIndex)
// console.log(sectionIndex)

// Colorscheme
if (sectionIndex != 0) {
	colorScheme('zae', section, sectionIndex, 2, 'powderblue', 'steelblue');
	colorScheme('o', section, sectionIndex, 2, 'darkseagreen', 'teal');
} else {
	colorScheme('zae', section, sectionIndex, 1, 'powderblue', 'steelblue');
}

console.log(document.documentElement.scrollHeight)
console.log(document.documentElement.clientHeight)
console.log(footer)

const actualHeight = document.documentElement.scrollHeight;
const visualHeight = document.documentElement.clientHeight;

if (actualHeight > visualHeight) {
	footer.innerHTML=`<a id="bottom-to-top">To top.</a>`;

	// Bottom to top
	const buttonBTT = selectById('bottom-to-top');
	
	buttonBTT.onclick = function() {
		window.scrollTo({top: 0, behavior: 'smooth'})
	}
} else {
	footer.remove();
}
