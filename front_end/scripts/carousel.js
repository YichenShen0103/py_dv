let left = document.querySelector(".button-left");
let right = document.querySelector(".button-right");
let min = document.querySelectorAll(".min");
let images = document.querySelector(".images");
let index = 0;
let time;

function position() {
  images.style.left = index * -100 + "%";
  min[index].style.opacity = 1;
  for (let i = 0; i < min.length; i++) {
    if (i !== index) {
      min[i].style.opacity = 0.3;
    }
  }
}

function add() {
  if (index >= min.length - 1) {
    index = 0;
  } else {
    index++;
  }
}

function desc() {
  if (index < 1) {
    index = min.length - 1;
  } else {
    index--;
  }
}

function timer() {
  time = setInterval(() => {
    index++;
    desc();
    add();
    position();
  }, 3000);
}

left.addEventListener("click", () => {
  desc();
  position();
  clearInterval(time);
  timer();
});

right.addEventListener("click", () => {
  add();
  position();
  clearInterval(time);
  timer();
});

for (let i = 0; i < min.length; i++) {
  min[i].addEventListener("click", () => {
    index = i;
    position();
    clearInterval(time);
    timer();
  });
}

timer();
