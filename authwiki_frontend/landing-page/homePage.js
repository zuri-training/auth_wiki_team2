const hamburger = document.querySelector(".hamburger");
const navList = document.querySelector(".nav-list");
const navItem = document.querySelectorAll(".nav-item");

hamburger.addEventListener("click", () => {
  //Animate Links
  navList.classList.toggle("open");
  navItem.forEach((link) => {
    link.classList.toggle("fade");
  });

  //Hamburger Animation
  hamburger.classList.toggle("toggle");
});
