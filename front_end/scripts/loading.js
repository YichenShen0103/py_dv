// Loadings
function getBrowserType() {
  var ua = navigator.userAgent;
  var isOpera = ua.indexOf("Opera") > -1;
  if (isOpera) {
    return "Opera";
  }
  var isIE =
    ua.indexOf("compatible") > -1 && ua.indexOf("MSIE") > -1 && !isOpera;
  var isIE11 = ua.indexOf("Trident") > -1 && ua.indexOf("rv:11.0") > -1;
  if (isIE11) {
    return "IE11";
  } else if (isIE) {
    var re = new RegExp("MSIE (\\d+\\.\\d+);");
    re.test(ua);
    var ver = parseFloat(RegExp["$1"]);
    if (ver == 7) {
      return "IE7";
    } else if (ver == 8) {
      return "IE8";
    } else if (ver == 9) {
      return "IE9";
    } else if (ver == 10) {
      return "IE10";
    } else {
      return "IE";
    }
  }
  var isEdge = ua.indexOf("Edge") > -1;
  if (isEdge) {
    return "Edge";
  }
  var isFirefox = ua.indexOf("Firefox") > -1;
  if (isFirefox) {
    return "Firefox";
  }
  var isSafari = ua.indexOf("Safari") > -1 && ua.indexOf("Chrome") == -1;
  if (isSafari) {
    return "Safari";
  }
  var isChrome =
    ua.indexOf("Chrome") > -1 &&
    ua.indexOf("Safari") > -1 &&
    ua.indexOf("Edge") == -1;
  if (isChrome) {
    return "Chrome";
  }
  var isUC = ua.indexOf("UCrowser") > -1;
  if (isUC) {
    return "UC";
  }
  var isQQ = ua.indexOf("QQBrowser") > -1;
  if (isQQ) {
    return "QQ";
  }
  return "未知";
}

document.addEventListener("DOMContentLoaded", function () {
  disableScroll();
  $("#resources").show();
});

$(window).on("load", function () {
  var resources = document.getElementById("resources");
  setTimeout(function () {
    resources.textContent = "检测环境中...";
    setTimeout(function () {
      $("#resources").hide();
      $("#finish").show();
      setTimeout(function () {
        if (
          getBrowserType() != "Edge" &&
          getBrowserType() != "Safari" &&
          getBrowserType() != "Chrome" &&
          getBrowserType() != "Firefox"
        ) {
          alert(
            "检测到您的浏览器内核为：" +
              getBrowserType() +
              "，这一内核未经过测试，可能存在显示问题，建议使用Chrome、Firefox、Edge或者Safari浏览器以获得最佳体验！"
          );
        }
        $(".loader-container").fadeOut("slow", function () {
          enableScroll();
        });
      }, 500);
    }, 600);
  }, 600);
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
