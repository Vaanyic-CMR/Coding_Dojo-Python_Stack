function getUsers(){
    fetch('http://localhost:5000/users')
        .then(res =>  res.json())
        .then(data => {
            var users = document.getElementById('users');
            users.innerHTML = ""
            for( let i = 0; i < data.length; i++){
                let row = document.createElement('tr');

                let name = document.createElement('td');
                name.innerHTML = data[i].username;
                row.appendChild(name);
                
                let email = document.createElement('td');
                email.innerHTML = data[i].email;
                row.appendChild(email);
                users.appendChild(row);
            }
        })
}


function clear_form() {
    var username = document.getElementById('username');
    var email = document.getElementById('email');

    username.value = ''
    email.value = ''
}

var user_form = document.getElementById('user_form');
user_form.onsubmit = function(e){
    e.preventDefault();
    
    var form = new FormData( user_form );

    fetch("http://localhost:5000/create/user", { method :'POST', body : form})
        .then( response => response.json() )
        .then( data => console.log(data) )
        .then( clear_form() )
        .then( getUsers() )
}

getUsers();