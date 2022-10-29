window.onscroll = function () { myFunction() };

var headerTop = document.getElementById("myHeader");
var sticky = headerTop.offsetTop;

function myFunction() {
    if (window.pageYOffset > sticky) {
        headerTop.classList.add("sticky");
    } else {
        headerTop.classList.remove("sticky");
    }
}

const menuBtn = document.querySelector('.menu-btn')
const miniMenu = document.querySelector('.mini-menu')
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    if (!menuOpen) {
        menuBtn.classList.add('open');
        miniMenu.classList.add('menu-left')
        menuOpen = true;
    } else {
        menuBtn.classList.remove('open');
        miniMenu.classList.remove('menu-left')
        menuOpen = false;
    }
})

var header = document.getElementById("menu");
var btns = header.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
  var current = document.getElementsByClassName("active");
  current[0].className = current[0].className.replace(" active", "");
  this.className += " active";
  });
}
var header1 = document.getElementById("miniMenu");
var btn = header1.getElementsByClassName("btn1");
for (var i = 0; i < btn.length; i++) {
  btn[i].addEventListener("click", function() {
  var current = document.getElementsByClassName("active");
  current[0].className = current[0].className.replace(" active", "");
  this.className += " active";
  });
}

function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  }