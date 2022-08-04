function myFunction() {
  var x = document.getElementById("myInput");
  var y = document.getElementById("hide1");
  var z = document.getElementById("hide2");

  if (x.type === "password") {
    x.type = "text";
    y.style.display = "block";
    z.style.display = "none";
  } else {
    x.type = "password";
    y.style.display = "none";
    z.style.display = "block";
  }
}
function comfirmfunction() {
  var sec = document.getElementById("secmyInput");
  var comfirmhide1 = document.getElementById("comfirmhide1");
  var comfirmhide2 = document.getElementById("comfirmhide2");

  if (sec.type === "password") {
    sec.type = "text";
    comfirmhide1.style.display = "block";
    comfirmhide2.style.display = "none";
  } else {
    sec.type = "password";
    comfirmhide1.style.display = "none";
    comfirmhide2.style.display = "block";
  }
}
