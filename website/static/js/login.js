function validation() {
  var username=document.getElementById("name").value;
  var pass=document.getElementById("pass").value;
  
  if(username=="" && pass==""){
    alert("Error: Enter your username and password");
    document.getElementById("name").focus();
    document.getElementById("pass").focus();
    return false;
  }
  if(username==""){
    alert("Error: Username can't be NULL");
    document.getElementById("name").focus();
    return false;
  }
  if(pass==""){
    alert("Error: password can't be NULL");
    document.getElementById("pass").focus();
    return false;
  }
  if(pass==username){
    alert("Error: password must be diffrent from username");
    document.getElementById("pass").focus();
    return false;
  }
}

function f(){
  alert("Forget password?");
}

function c(){
  alert ("Wanna create an account?");
}