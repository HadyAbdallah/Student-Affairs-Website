function ceackSerch(){
    var search=document.getElementById("search").value;
    if(search=="")
    {
        alert('Error: Plese enter ID for student you want to updet')
        document.getElementById("search").focus();
        return false;
    }
    re=/[0-9]/
    if(!re.test(search))
    {
        alert('Error: Plese enter ID for student you want to updet')
        document.getElementById("search").focus();
        return false;
    }
}
function confirmDelete()
{
    alert('Are you sure you want to remove student data')
}
function ceackSerchstatus(){
    var search=document.getElementById("search").value;
    if(search=="")
    {
        alert('Error: Plese enter name for student you want to see his status')
        document.getElementById("search").focus();
        return false;
    }
}