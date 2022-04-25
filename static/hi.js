firebase.auth().onAuthStateChanged((user)=>{
    if(!user){
        location.replace("login.html")
    }else{

        document.getElementById("username").innerHTML = "you are currently logged in as: "+user.email
        if(user.displayName !=null){

            document.getElementById("displayname").innerHTML = user.displayName
            document.getElementById("headingname").innerHTML = user.displayName + ','
        }else{
            document.getElementById("displayname").innerHTML = "None"
        }
        
        if(user.photoURL !=null){

            document.getElementById("userimage").src =user.photoURL
        }else{
            document.getElementById("userimage").src = "/static/default.jpg"
        }

    }
})


function logout(){
    firebase.auth().signOut()
}