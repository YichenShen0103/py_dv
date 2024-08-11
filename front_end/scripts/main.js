// Scroll to top
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

// Lazy load
const observer = lozad();
observer.observe();

// Loadings
$(window).on("load", function () {
  disableScroll();
  setTimeout(function () {
    $(".loader-container").fadeOut("slow", function () {
      enableScroll();
    });
  }, 3000);
});

function disableScroll() {
  window.addEventListener("wheel", preventDefault, { passive: false });
  window.addEventListener("DOMMouseScroll", preventDefault, { passive: false });
  window.addEventListener("touchmove", preventDefault, { passive: false });
}

function enableScroll() {
  window.removeEventListener("wheel", preventDefault);
  window.removeEventListener("DOMMouseScroll", preventDefault);
  window.removeEventListener("touchmove", preventDefault);
}

function preventDefault(e) {
  e.preventDefault();
}
