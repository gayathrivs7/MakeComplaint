function login(){

var username = document.getElementById("user").value;
var password = document.getElementById("pas").value;

if (username == 'user'&& password == 'enter')
{
    window.open("location.href='http://127.0.0.1:5000/register'")
}
else{
    alert("Invalid credentials")

}

}