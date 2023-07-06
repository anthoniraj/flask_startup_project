function displayAddUser() {
    var url = "/user_add"
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("content").innerHTML = this.responseText; 
       
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}

function processUpdateUser(id) {
    url = "/user_update?id="+id
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("content").innerHTML = this.responseText;   
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}
function processDeleteUser(id) {
    if (confirm("Are you sure want to delete this user?") == true) {        
        var url = "/user_delete?id="+id
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {  
                document.getElementById("content").innerHTML = this.responseText;   
                new simpleDatatables.DataTable("#userTable");
                alert("User deleted successfully!");               
            }
        };
        xhttp.open("GET", url, true);
        xhttp.send();
    }
}
function processGetAllUsers() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("content").innerHTML = this.responseText;
            new simpleDatatables.DataTable("#userTable");                    
        }
    };
    xhttp.open("GET", "/get_all_users", true);
    xhttp.send();
}