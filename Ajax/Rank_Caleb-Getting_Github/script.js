
async function getUser() {
    user = document.getElementById('user').value
    data = await getCoderData( user )
    console.log( data )
    var contents = (`<h1>${data.name} has ${data.followers} followers.</h1>`+
    `<img src="${data.avatar_url}">`);
    user = document.querySelector( '#results' ).innerHTML = contents
}

async function getCoderData( user ) {
    var response = await fetch("https://api.github.com/users/" + user);
    var coderData = await response.json();
    return coderData;
}