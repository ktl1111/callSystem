 const today = new Date();
    const currentHours = ("0" + today.getHours()).slice(-2);
    const currentMinutes = ("0" + today.getMinutes()).slice(-2);
    const time =currentHours +":"+ currentMinutes;
    p = document.getElementById("time")
    p.innerHTML = time

 //reload page
// setInterval(function(){
//    window.location.reload();
// },9000);


//
//     setInterval(function(){
//    window.location.reload();
// },3000);

window.screen.height; //screen height
window.screen.width; //screen width

//For example, 1024x768:
alert(window.screen.width+"x"+window.screen.height);