

thumbsUp = document.getElementById("thumbsUp");
thumbsDown = document.getElementById("thumbsDown"); 

thumbsUp.onsubmit = (e)=>{
    e.preventDefault();
    thumbsUp.style.color="red";
    thumbsDown.style.color="black";

}

thumbsDown.onsubmit = (e)=>{
    e.preventDefault();
    thumbsDown.style.color="red";
    thumbsUp.style.color="black";

}

console.log(thumbsUp)
console.log(thumbsDown)