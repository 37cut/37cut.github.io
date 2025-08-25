const footer = document.createElement('div')
const profile = document.createElement('div')
const profileText = document.createElement('p')

footer.setAttribute('id', 'footer')
profile.setAttribute('class', '_button')

profile.onclick = function() { window.location.href = "https://osu.ppy.sh/users/17589673" }

profileText.appendChild(document.createTextNode('Return'))
profile.appendChild(profileText)
footer.appendChild(profile)

document.body.appendChild(footer)
