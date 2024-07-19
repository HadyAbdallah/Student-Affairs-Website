function validation(){
    var name=document.getElementById("name").value;
    var id=document.getElementById("id").value;
    var gpa=document.getElementById("gpa").value;
    var phone=document.getElementById("ph").value;
    var email=document.getElementById("email").value;
    var Dep=document.getElementById("Dep").value;
    var lvl=document.getElementById("lvl").value;
    var date=document.getElementById("date").value;
    var gender1=document.getElementById("M");
    var gender2=document.getElementById("F");
    var status1=document.getElementById("A");
    var status2=document.getElementById("UA");


    
    if(name==""){
        alert("Error: name can't be NULL");
        document.getElementById("name").focus();
        return false;
    }

    if(id==""){
        alert("Error: ID can't be NULL");
        document.getElementById("id").focus();
        return false;
    }

    if(gpa==""){
        alert("Error: GPA can't be NULL");
        document.getElementById("gpa").focus();
        return false;
    }
    if(phone==""){
        alert("Error: Mobile Number can't be NULL");
        document.getElementById("ph").focus();
        return false;
    }
    if(email==""){
        alert("Error: Email can't be NULL");
        document.getElementById("email").focus();
        return false;
    }
    if(Dep=="Choose a Department")
    {
        alert("Error: Plese choose a Department");
        document.getElementById("Dep").focus();
        return false;
    }
    if(lvl=="Choose a Level")
    {
        alert("Error: Plese choose a Level");
        document.getElementById("lvl").focus();
        return false;
    }
    if(date==0)
    {
        alert("Error: Plese select a Date of birth");
        document.getElementById("date").focus();
        return false;
    }
    if(gender1.checked==true){
        
    }
    else if(gender2.checked==true){
        
    }
    else{
        alert('Error: Plese select a gender');
        return false;
    }
    if(status1.checked==true){
        
    }
    else if(status2.checked==true){
        
    }
    else{
        alert('Error: Plese select a status');
        return false;
    }
}
