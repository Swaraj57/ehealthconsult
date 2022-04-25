document.getElementById("loginForm").addEventListener("submit",(event)=>{
    event.preventDefault()
})

document.getElementById("signupform").addEventListener("submit",(event)=>{
    event.preventDefault()
})

firebase.auth().onAuthStateChanged((user)=>{
 
    if(user !=null){
        location.replace("/main")
    }
})


let loadSite = false;

function login(){
    const email = document.getElementById("email_field").value
    const password = document.getElementById("password_field").value
    firebase.auth().signInWithEmailAndPassword(email, password)
    .catch((error)=>{
        document.getElementById("error").innerHTML = error.message
    })
}
async function signup(){
    const Fullname = document.getElementById("fullname").value
    const email = document.getElementById("email_field1").value
    const password = document.getElementById("password_field1").value
    await firebase.auth().createUserWithEmailAndPassword(email, password)
    

    // .then(()=> {
    //     const user = firebase.auth().currentUser;
    //     console.log(user.email);
    //     user.updateProfile({
    //         displayName: Fullname
    //     });
    //     console.log("Bhossa")
    // }).then(() => {
    //     //Update the Vuex Store here with firebase.auth().currentUser
    //     console.log(firebase.auth().currentUser.displayName);
    //   })
    // await firebase.auth().
    const user = await firebase.auth().currentUser;
        console.log(user.email)
        console.log(Fullname)


    await user.updateProfile({
            displayName:Fullname.toString()
            })
    console.log(user.displayName)
    await user.reload()
    // loadSite = true

    

    // .catch((error) => {
    //     document.getElementById("error").innerHTML = error.message
    // });
    
}

function forgotPass(){
    const email = document.getElementById("email_field").value
    firebase.auth().sendPasswordResetEmail(email)
    .then(() => {
        alert("Password reset link sent to your email address.")
    })
    .catch((error) => {
        document.getElementById("error").innerHTML = error.message
    });
}


function google() {
    var provider = new firebase.auth.GoogleAuthProvider();
firebase.auth().signInWithRedirect(provider);
firebase.auth()
  .getRedirectResult()
  .then((result) => {
    if (result.credential) {
      /** @type {firebase.auth.OAuthCredential} */
      var credential = result.credential;

      // This gives you a Google Access Token. You can use it to access the Google API.
      var token = credential.accessToken;
      // ...
    }
    // The signed-in user info.
    var user = result.user;
  })
  .catch((error) => {
    document.getElementById("error").innerHTML = error.message
});
}