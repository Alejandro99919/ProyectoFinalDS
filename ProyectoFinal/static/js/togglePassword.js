const password = document.getElementById('password');
const toggle = document.getElementById('iconoTogglePassword');


toggle.addEventListener('click', () =>{
    if(password.type === 'password'){
        password.type = 'text';
    }else{
        password.type = 'password';
    }
})