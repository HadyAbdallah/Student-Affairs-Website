function checkLevelName(){
    var search=document.getElementById("search").value;
    var value=document.getElementById("select").value;
    var value2=document.getElementById("right").innerText;
    if(search=="")
    {
        alert('Error, Please Enter student name to search for..')
        document.getElementById("search").focus();
        return false;
    }
    if(value!=value2)
    {
        alert('Error, The student should be in Third level..');
        return false;
    } 
}
function checkSearch(){
    var search=document.getElementById("search").value;
    var value=document.getElementById("select").value;
    if(search=="")
    {
        alert('Error, Please Enter student name to search for..')
        document.getElementById("search").focus();
        return false;
    }
    if(value=="Student Level")
    {
        alert("Error: Plese choose a Level");
        return false;
    }
    

}
    
    





























// function Search(){
//     var search=document.getElementById("search").value;
//     if(search=="")
//     {
//         alert('Error: Plese enter ID for student you want to updet')
//         document.getElementById("search").focus();
//         return false;
//     }
