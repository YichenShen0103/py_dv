$(function () {
  $(window).scroll(function () {
    var scrollt = document.documentElement.scrollTop + document.body.scrollTop; //获取滚动后的高度
    if (scrollt > 200) {
      $("#gotop").fadeIn(400); //淡出
    } else {
      $("#gotop").stop().fadeOut(400);
    }
  });
  $("#gotop").click(function () {
    $("html,body").animate({ scrollTop: "0px" }, 200);
  });
});

var images = document.getElementsByTagName("img");

window.addEventListener("scroll", (e) => {
  ergodic();
});
function ergodic() {
  for (let i of images) {
    if (i.offsetTop <= window.innerHeight + window.scrollY) {
      let trueSrc = i.getAttribute("data-src");
      i.setAttribute("src", trueSrc);
    }
  }
}
ergodic();
