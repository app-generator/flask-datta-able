// 'use strict';
var flg = '0';
document.addEventListener('DOMContentLoaded', function () {
  // feather icon start
  feather.replace();
  // feather icon end

  // remove pre-loader start
  setTimeout(function () {
    document.querySelector('.loader-bg').remove();
  }, 400);

  // remove pre-loader end
  if (document.querySelector('body').hasAttribute('data-pc-layout')) {
    if (document.querySelector('body').getAttribute('data-pc-layout') == 'horizontal') {
      var docW = window.innerWidth;
      if (docW <= 1024) {
        add_scroller();
      }
    }
  } else {
    add_scroller();
  }

  var hamburger = document.querySelector('.hamburger:not(.is-active)');
  if (hamburger) {
    hamburger.addEventListener('click', function () {
      if (document.querySelector('.hamburger').classList.contains('is-active')) {
        document.querySelector('.hamburger').classList.remove('is-active');
      } else {
        document.querySelector('.hamburger').classList.add('is-active');
      }
    });
  }
  // Menu overlay layout start
  var temp_overlay_menu = document.querySelector('#overlay-menu');
  if (temp_overlay_menu) {
    temp_overlay_menu.addEventListener('click', function () {
      menu_click();
      if (document.querySelector('.pc-sidebar').classList.contains('pc-over-menu-active')) {
        remove_overlay_menu();
      } else {
        document.querySelector('.pc-sidebar').classList.add('pc-over-menu-active');
        document.querySelector('.pc-sidebar').insertAdjacentHTML('beforeend', '<div class="pc-menu-overlay"></div>');
        document.querySelector('.pc-menu-overlay').addEventListener('click', function () {
          remove_overlay_menu();
          document.querySelector('.hamburger').classList.remove('is-active');
        });
      }
    });
  }
  // Menu overlay layout end

  // Menu collapse click start
  var mobile_collapse_over = document.querySelector('#mobile-collapse');
  if (mobile_collapse_over) {
    mobile_collapse_over.addEventListener('click', function () {
      var temp_sidebar = document.querySelector('.pc-sidebar');
      if (temp_sidebar) {
        if (document.querySelector('.pc-sidebar').classList.contains('mob-sidebar-active')) {
          rm_menu();
        } else {
          document.querySelector('.pc-sidebar').classList.add('mob-sidebar-active');
          document.querySelector('.pc-sidebar').insertAdjacentHTML('beforeend', '<div class="pc-menu-overlay"></div>');
          document.querySelector('.pc-menu-overlay').addEventListener('click', function () {
            rm_menu();
          });
        }
      }
    });
  }
  // Menu collapse click end

  // Menu collapse click start
  var mobile_collapse = document.querySelector('.pc-horizontal #mobile-collapse');
  if (mobile_collapse) {
    mobile_collapse.addEventListener('click', function () {
      if (document.querySelector('.topbar').classList.contains('mob-sidebar-active')) {
        rm_menu();
      } else {
        document.querySelector('.topbar').classList.add('mob-sidebar-active');
        document.querySelector('.topbar').insertAdjacentHTML('beforeend', '<div class="pc-menu-overlay"></div>');
        document.querySelector('.pc-menu-overlay').addEventListener('click', function () {
          rm_menu();
        });
      }
    });
  }
  // Menu collapse click end
  // Horizontal menu click js start
  var topbar_link_list = document.querySelector('.pc-horizontal .topbar .pc-navbar>li>a');
  if (topbar_link_list) {
    topbar_link_list.addEventListener('click', function (e) {
      var targetElement = e.target;
      setTimeout(function () {
        targetElement.parentNodes.children[1].removeAttribute('style');
      }, 1000);
    });
  }
  // Horizontal menu click js end

  // header dropdown scrollbar start
  if (document.querySelector('.header-notification-scroll')) {
    new SimpleBar(document.querySelector('.header-notification-scroll'));
  }

  if (document.querySelector('.profile-notification-scroll')) {
    new SimpleBar(document.querySelector('.profile-notification-scroll'));
  }
  // header dropdown scrollbar end

  // component scrollbar start
  if (document.querySelector('.component-list-card .card-body')) {
    new SimpleBar(document.querySelector('.component-list-card .card-body'));
  }
  // component- dropdown scrollbar end

  var sidebar_hide = document.querySelector('#sidebar-hide');
  if (sidebar_hide) {
    sidebar_hide.addEventListener('click', function () {
      if (document.querySelector('.pc-sidebar').classList.contains('pc-sidebar-hide')) {
        document.querySelector('.pc-sidebar').classList.remove('pc-sidebar-hide');
      } else {
        document.querySelector('.pc-sidebar').classList.add('pc-sidebar-hide');
      }
    });
  }

  if (document.querySelector('.trig-drp-search')) {
    const search_drp = document.querySelector('.trig-drp-search');
    search_drp.addEventListener('shown.bs.dropdown', (event) => {
      document.querySelector('.drp-search input').focus();
    });
  }

});

// Menu click start
function add_scroller() {
  menu_click();
  // Menu scrollbar start
  if (document.querySelector('.navbar-content')) {
    new SimpleBar(document.querySelector('.navbar-content'));
  }
  // Menu scrollbar end
}

// Menu click start
function menu_click() {
  var vw = window.innerWidth;
  var elem = document.querySelectorAll('.pc-navbar li');
  for (var j = 0; j < elem.length; j++) {
    elem[j].removeEventListener('click', function () { });
  }

  var elem = document.querySelectorAll('.pc-navbar li:not(.pc-trigger) .pc-submenu');
  for (var j = 0; j < elem.length; j++) {
    elem[j].style.display = 'none';
  }

  var pc_link_click = document.querySelectorAll('.pc-navbar > li:not(.pc-caption).pc-hasmenu');
  for (var i = 0; i < pc_link_click.length; i++) {
    pc_link_click[i].addEventListener('click', function (event) {
      event.stopPropagation();
      var targetElement = event.target;
      if (targetElement.tagName == 'SPAN') {
        targetElement = targetElement.parentNode;
      }
      if (targetElement.parentNode.classList.contains('pc-trigger')) {
        targetElement.parentNode.classList.remove('pc-trigger');
        slideUp(targetElement.parentNode.children[1], 200);
        window.setTimeout(() => {
          targetElement.parentNode.children[1].removeAttribute('style');
          targetElement.parentNode.children[1].style.display = 'none';
        }, 200);
      } else {
        var tc = document.querySelectorAll('li.pc-trigger');
        for (var t = 0; t < tc.length; t++) {
          var c = tc[t];
          c.classList.remove('pc-trigger');
          slideUp(c.children[1], 200);
          window.setTimeout(() => {
            c.children[1].removeAttribute('style');
            c.children[1].style.display = 'none';
          }, 200);
        }
        targetElement.parentNode.classList.add('pc-trigger');
        var tmp = targetElement.children[1];
        if (tmp) {
          slideDown(targetElement.parentNode.children[1], 200);
        }
      }
    });
  }

  var pc_sub_link_click = document.querySelectorAll('.pc-navbar > li:not(.pc-caption) li.pc-hasmenu');
  for (var i = 0; i < pc_sub_link_click.length; i++) {
    pc_sub_link_click[i].addEventListener('click', function (event) {
      var targetElement = event.target;
      if (targetElement.tagName == 'SPAN') {
        targetElement = targetElement.parentNode;
      }
      event.stopPropagation();
      if (targetElement.parentNode.classList.contains('pc-trigger')) {
        targetElement.parentNode.classList.remove('pc-trigger');
        slideUp(targetElement.parentNode.children[1], 200);
      } else {
        var tc = targetElement.parentNode.parentNode.children;
        for (var t = 0; t < tc.length; t++) {
          var c = tc[t];
          c.classList.remove('pc-trigger');
          if (c.tagName == 'LI') {
            c = c.children[0];
          }
          if (c.parentNode.classList.contains('pc-hasmenu')) {
            slideUp(c.parentNode.children[1], 200);
          }
        }
        targetElement.parentNode.classList.add('pc-trigger');
        var tmp = targetElement.parentNode.children[1];
        if (tmp) {
          tmp.removeAttribute('style');
          slideDown(tmp, 200);
        }
      }
    });
  }
}

// hide menu in mobile menu
function rm_menu() {
  var temp_list = document.querySelector('.pc-sidebar');
  if (temp_list) {
    document.querySelector('.pc-sidebar').classList.remove('mob-sidebar-active');
  }
  if (document.querySelector('.topbar')) {
    document.querySelector('.topbar').classList.remove('mob-sidebar-active');
  }

  document.querySelector('.pc-sidebar .pc-menu-overlay').remove();
  if (document.querySelector('.topbar .pc-menu-overlay')) {
    document.querySelector('.topbar .pc-menu-overlay').remove();
  }
}

// remove overlay
function remove_overlay_menu() {
  document.querySelector('.pc-sidebar').classList.remove('pc-over-menu-active');
  if (document.querySelector('.topbar')) {
    document.querySelector('.topbar').classList.remove('mob-sidebar-active');
  }
  document.querySelector('.pc-sidebar .pc-menu-overlay').remove();
  document.querySelector('.topbar .pc-menu-overlay').remove();
}

window.addEventListener('load', function () {
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
  var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
  var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl);
  });
  var toastElList = [].slice.call(document.querySelectorAll('.toast'));
  var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl);
  });
});

// active menu item list start
var elem = document.querySelectorAll('.pc-sidebar .pc-navbar a');
for (var l = 0; l < elem.length; l++) {
  var pageUrl = window.location.href.split(/[?#]/)[0];
  if (elem[l].href == pageUrl && elem[l].getAttribute('href') != '') {
    elem[l].parentNode.classList.add('active');

    elem[l].parentNode.parentNode.parentNode.classList.add('pc-trigger');
    elem[l].parentNode.parentNode.parentNode.classList.add('active');
    elem[l].parentNode.parentNode.style.display = 'block';

    elem[l].parentNode.parentNode.parentNode.parentNode.parentNode.classList.add('pc-trigger');
    elem[l].parentNode.parentNode.parentNode.parentNode.style.display = 'block';
  }
}

// like event
var tc = document.querySelectorAll('.prod-likes .form-check-input');
for (var t = 0; t < tc.length; t++) {
  var prod_like = tc[t];
  prod_like.addEventListener('change', function (event) {
    if (event.currentTarget.checked) {
      prod_like = event.target;
      prod_like.parentNode.insertAdjacentHTML(
        'beforeend',
        '<div class="pc-like"><div class="like-wrapper"><span><span class="pc-group"><span class="pc-dots"></span><span class="pc-dots"></span><span class="pc-dots"></span><span class="pc-dots"></span></span></span></div></div>'
      );
      prod_like.parentNode.querySelector('.pc-like').classList.add('pc-like-animate');
      setTimeout(function () {
        try {
          prod_like.parentNode.querySelector('.pc-like').remove();
        } catch (error) { }
      }, 3000);
    } else {
      prod_like = event.target;
      try {
        prod_like.parentNode.querySelector('.pc-like').remove();
      } catch (error) { }
    }
  });
}

// authentication logo
var tc = document.querySelectorAll('.auth-main.v2 .img-brand');
for (var t = 0; t < tc.length; t++) {
  tc[t].setAttribute('src', '../assets/images/logo-white.svg');
}

// =======================================================
// =======================================================

var rtl_flag = false;
var dark_flag = false;

// ----------    new setup start   ------------
function layout_change_default() {
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    dark_layout = 'dark';
  } else {
    dark_layout = 'light';
  }
  layout_change(dark_layout);
  var btn_control = document.querySelector('.theme-layout .btn[data-value="default"]');
  if (btn_control) {
    btn_control.classList.add('active');
  }
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (event) => {
    dark_layout = event.matches ? 'dark' : 'light';
    layout_change(dark_layout);
  });
}

// dark switch mode
function dark_mode() {
  if (document.getElementById('dark-mode').checked) {
    layout_change("dark");
  } else {
    layout_change("light");
  }
}

// preset color
document.addEventListener('DOMContentLoaded', function () {
  var if_exist = document.querySelectorAll('.preset-color');
  if (if_exist) {
    var preset_color = document.querySelectorAll('.preset-color > a');
    for (var h = 0; h < preset_color.length; h++) {
      var c = preset_color[h];
      c.addEventListener('click', function (event) {
        var targetElement = event.target;
        if (targetElement.tagName == 'SPAN') {
          targetElement = targetElement.parentNode;
        }
        var temp = targetElement.getAttribute('data-value');
        preset_change(temp);
      });
    }
  }

  var if_exist = document.querySelectorAll('.header-color');
  if (if_exist) {
    var preset_color = document.querySelectorAll('.header-color > a');
    for (var h = 0; h < preset_color.length; h++) {
      var c = preset_color[h];
      c.addEventListener('click', function (event) {
        var targetElement = event.target;
        if (targetElement.tagName == 'SPAN') {
          targetElement = targetElement.parentNode;
        }
        var temp = targetElement.getAttribute('data-value');
        header_change(temp);
      });
    }
  }

  var if_exist = document.querySelectorAll('.navbar-color');
  if (if_exist) {
    var preset_color = document.querySelectorAll('.navbar-color > a');
    for (var h = 0; h < preset_color.length; h++) {
      var c = preset_color[h];
      c.addEventListener('click', function (event) {
        var targetElement = event.target;
        if (targetElement.tagName == 'SPAN') {
          targetElement = targetElement.parentNode;
        }
        var temp = targetElement.getAttribute('data-value');
        navbar_change(temp);
      });
    }
  }

  var if_exist = document.querySelectorAll('.logo-color');
  if (if_exist) {
    var preset_color = document.querySelectorAll('.logo-color > a');
    for (var h = 0; h < preset_color.length; h++) {
      var c = preset_color[h];
      c.addEventListener('click', function (event) {
        var targetElement = event.target;
        if (targetElement.tagName == 'SPAN') {
          targetElement = targetElement.parentNode;
        }
        var temp = targetElement.getAttribute('data-value');
        logo_change(temp);
      });
    }
  }

  var if_exist = document.querySelectorAll('.caption-color');
  if (if_exist) {
    var preset_color = document.querySelectorAll('.caption-color > a');
    for (var h = 0; h < preset_color.length; h++) {
      var c = preset_color[h];
      c.addEventListener('click', function (event) {
        var targetElement = event.target;
        if (targetElement.tagName == 'SPAN') {
          targetElement = targetElement.parentNode;
        }
        var temp = targetElement.getAttribute('data-value');
        caption_change(temp);
      });
    }
  }

  var if_exist = document.querySelectorAll('.navbar-img');
  if (if_exist) {
    var preset_color = document.querySelectorAll('.navbar-img > a');
    for (var h = 0; h < preset_color.length; h++) {
      var c = preset_color[h];
      c.addEventListener('click', function (event) {
        var targetElement = event.target;
        if (targetElement.tagName == 'SPAN') {
          targetElement = targetElement.parentNode;
        }
        var temp = targetElement.getAttribute('data-value');
        nav_image_change(temp);
      });
    }
  }

  var if_exist = document.querySelectorAll('.drp-menu-icon');
  if (if_exist) {
    var preset_color = document.querySelectorAll('.drp-menu-icon > a');
    for (var h = 0; h < preset_color.length; h++) {
      var c = preset_color[h];
      c.addEventListener('click', function (event) {
        var targetElement = event.target;
        if (targetElement.tagName == 'SPAN') {
          targetElement = targetElement.parentNode;
        }
        var temp = targetElement.getAttribute('data-value');
        drp_menu_icon_change(temp);
      });
    }
  }

  var if_exist = document.querySelectorAll('.drp-menu-link-icon');
  if (if_exist) {
    var preset_color = document.querySelectorAll('.drp-menu-link-icon > a');
    for (var h = 0; h < preset_color.length; h++) {
      var c = preset_color[h];
      c.addEventListener('click', function (event) {
        var targetElement = event.target;
        if (targetElement.tagName == 'SPAN') {
          targetElement = targetElement.parentNode;
        }
        var temp = targetElement.getAttribute('data-value');
        drp_menu_link_icon_change(temp);
      });
    }
  }

  if (document.querySelector('.pct-body')) {
    new SimpleBar(document.querySelector('.pct-body'));
  }

  var layout_reset = document.querySelector('#layoutreset');
  if (layout_reset) {
    layout_reset.addEventListener('click', function (e) {
      location.reload();
    });
  }
});

function layout_theme_sidebar_change(value) {
  if (value == 'true') {
    document.getElementsByTagName('body')[0].setAttribute('data-pc-sidebar_theme', 'true');
    if (document.querySelector('.pc-sidebar .m-header .logo-lg')) {
      document.querySelector('.pc-sidebar .m-header .logo-lg').setAttribute('src', '../assets/images/logo-dark.svg');
    }
    var control = document.querySelector('.sidebar-theme .btn.active');
    if (control) {
      document.querySelector('.sidebar-theme .btn.active').classList.remove('active');
      document.querySelector(".sidebar-theme .btn[data-value='true']").classList.add('active');
    }
  } else {
    document.getElementsByTagName('body')[0].setAttribute('data-pc-sidebar_theme', 'false');
    if (document.querySelector('.pc-sidebar .m-header .logo-lg')) {
      document.querySelector('.pc-sidebar .m-header .logo-lg').setAttribute('src', '../assets/images/logo-white.svg');
    }
    var control = document.querySelector('.sidebar-theme .btn.active');
    if (control) {
      document.querySelector('.sidebar-theme .btn.active').classList.remove('active');
      document.querySelector(".sidebar-theme .btn[data-value='false']").classList.add('active');
    }
  }
}
function layout_caption_change(value) {
  if (value == 'true') {
    document.getElementsByTagName('body')[0].setAttribute('data-pc-sidebar-caption', 'true');
    var control = document.querySelector('.theme-nav-caption .btn.active');
    if (control) {
      document.querySelector('.theme-nav-caption .btn.active').classList.remove('active');
      document.querySelector(".theme-nav-caption .btn[data-value='true']").classList.add('active');
    }
  } else {
    document.getElementsByTagName('body')[0].setAttribute('data-pc-sidebar-caption', 'false');
    var control = document.querySelector('.theme-nav-caption .btn.active');
    if (control) {
      document.querySelector('.theme-nav-caption .btn.active').classList.remove('active');
      document.querySelector(".theme-nav-caption .btn[data-value='false']").classList.add('active');
    }
  }
}
function preset_change(value) {
  document.getElementsByTagName('body')[0].setAttribute('data-pc-preset', value);
  var control = document.querySelector('.pct-offcanvas');
  if (control) {
    document.querySelector('.preset-color > a.active').classList.remove('active');
    document.querySelector(".preset-color > a[data-value='" + value + "']").classList.add('active');
  }
}
function header_change(value) {
  document.getElementsByTagName('body')[0].setAttribute('data-pc-header', value);
  var control = document.querySelector('.pct-offcanvas');
  if (control) {
    document.querySelector('.header-color > a.active').classList.remove('active');
    document.querySelector(".header-color > a[data-value='" + value + "']").classList.add('active');
  }
}
function navbar_change(value) {
  document.getElementsByTagName('body')[0].setAttribute('data-pc-navbar', value);
  var control = document.querySelector('.pct-offcanvas');
  if (control) {
    document.querySelector('.navbar-color > a.active').classList.remove('active');
    document.querySelector(".navbar-color > a[data-value='" + value + "']").classList.add('active');
  }
}
function logo_change(value) {
  document.getElementsByTagName('body')[0].setAttribute('data-pc-logo', value);
  var control = document.querySelector('.pct-offcanvas');
  if (control) {
    document.querySelector('.logo-color > a.active').classList.remove('active');
    document.querySelector(".logo-color > a[data-value='" + value + "']").classList.add('active');
  }
}
function caption_change(value) {
  document.getElementsByTagName('body')[0].setAttribute('data-pc-caption', value);
  var control = document.querySelector('.pct-offcanvas');
  if (control) {
    document.querySelector('.caption-color > a.active').classList.remove('active');
    document.querySelector(".caption-color > a[data-value='" + value + "']").classList.add('active');
  }
}
function drp_menu_icon_change(value) {
  document.getElementsByTagName('body')[0].setAttribute('data-pc-drp-menu-icon', value);
  var control = document.querySelector('.pct-offcanvas');
  if (control) {
    document.querySelector('.drp-menu-icon > a.active').classList.remove('active');
    document.querySelector(".drp-menu-icon > a[data-value='" + value + "']").classList.add('active');
  }
}
function drp_menu_link_icon_change(value) {
  document.getElementsByTagName('body')[0].setAttribute('data-pc-drp-menu-link-icon', value);
  var control = document.querySelector('.pct-offcanvas');
  if (control) {
    document.querySelector('.drp-menu-link-icon > a.active').classList.remove('active');
    document.querySelector(".drp-menu-link-icon > a[data-value='" + value + "']").classList.add('active');
  }
}
function nav_image_change(value) {
  document.getElementsByTagName('body')[0].setAttribute('data-pc-navimg', value);
  var control = document.querySelector('.pct-offcanvas');
  if (control) {
    document.querySelector('.navbar-img > a.active').classList.remove('active');
    document.querySelector(".navbar-img > a[data-value='" + value + "']").classList.add('active');
  }
}
function layout_rtl_change(value) {
  var control = document.querySelector('#layoutmodertl');
  if (value == 'true') {
    rtl_flag = true;
    document.getElementsByTagName('body')[0].setAttribute('data-pc-direction', 'rtl');
    document.getElementsByTagName('html')[0].setAttribute('dir', 'rtl');
    document.getElementsByTagName('html')[0].setAttribute('lang', 'ar');
    var control = document.querySelector('.theme-direction .btn.active');
    if (control) {
      document.querySelector('.theme-direction .btn.active').classList.remove('active');
      document.querySelector(".theme-direction .btn[data-value='true']").classList.add('active');
    }
  } else {
    rtl_flag = false;
    document.getElementsByTagName('body')[0].setAttribute('data-pc-direction', 'ltr');
    document.getElementsByTagName('html')[0].removeAttribute('dir');
    document.getElementsByTagName('html')[0].removeAttribute('lang');
    var control = document.querySelector('.theme-direction .btn.active');
    if (control) {
      document.querySelector('.theme-direction .btn.active').classList.remove('active');
      document.querySelector(".theme-direction .btn[data-value='false']").classList.add('active');
    }
  }
}
function layout_change(layout) {
  var control = document.querySelector('.pct-offcanvas');
  document.getElementsByTagName('body')[0].setAttribute('data-pc-theme', layout);

  var btn_control = document.querySelector('.theme-layout .btn[data-value="default"]');
  if (btn_control) {
    btn_control.classList.remove('active');
  }
  if (layout == 'dark') {
    dark_flag = true;
    if (document.querySelector('.footer-top .footer-logo')) {
      document.querySelector('.footer-top .footer-logo').setAttribute('src', '../assets/images/logo-white.svg');
    }
    if (document.querySelector('[data-pc-layout="horizontal"] .pc-sidebar .m-header .logo-lg')) {
      document.querySelector('[data-pc-layout="horizontal"] .pc-sidebar .m-header .logo-lg').setAttribute('src', '../assets/images/logo-white.svg');
    }
    if (document.querySelector('.auth-wrapper a>img')) {
      document.querySelector('.auth-wrapper a>img').setAttribute('src', '../assets/images/logo-white.svg');
    }
    var control = document.querySelector('.theme-layout .btn.active');
    if (control) {
      document.querySelector('.theme-layout .btn.active').classList.remove('active');
      document.querySelector(".theme-layout .btn[data-value='false']").classList.add('active');
    }
  } else {
    dark_flag = false;
    if (document.querySelector('.footer-top .footer-logo')) {
      document.querySelector('.footer-top .footer-logo').setAttribute('src', '../assets/images/logo-dark.svg');
    }
    if (document.querySelector('.auth-wrapper a>img')) {
      document.querySelector('.auth-wrapper a>img').setAttribute('src', '../assets/images/logo-dark.svg');
    }
    if (document.querySelector('[data-pc-layout="horizontal"] .pc-sidebar .m-header .logo-lg')) {
      document.querySelector('[data-pc-layout="horizontal"] .pc-sidebar .m-header .logo-lg').setAttribute('src', '../assets/images/logo-dark.svg');
    }
    var control = document.querySelector('.theme-layout .btn.active');
    if (control) {
      document.querySelector('.theme-layout .btn.active').classList.remove('active');
      document.querySelector(".theme-layout .btn[data-value='true']").classList.add('active');
    }
  }
}
function change_box_container(value) {
  if (document.querySelector('.pc-content')) {
    if (value == 'true') {
      document.querySelector('.pc-content').classList.add('container');
      document.querySelector('.footer-wrapper').classList.add('container');
      document.querySelector('.footer-wrapper').classList.remove('container-fluid');

      var control = document.querySelector('.theme-container .btn.active');
      if (control) {
        document.querySelector('.theme-container .btn.active').classList.remove('active');
        document.querySelector(".theme-container .btn[data-value='true']").classList.add('active');
      }
    } else {
      document.querySelector('.pc-content').classList.remove('container');
      document.querySelector('.footer-wrapper').classList.remove('container');
      document.querySelector('.footer-wrapper').classList.add('container-fluid');
      var control = document.querySelector('.theme-container .btn.active');
      if (control) {
        document.querySelector('.theme-container .btn.active').classList.remove('active');
        document.querySelector(".theme-container .btn[data-value='false']").classList.add('active');
      }
    }
  }
}

// ----------    new setup end   ------------

// =======================================================
// =======================================================

function removeClassByPrefix(node, prefix) {
  for (let i = 0; i < node.classList.length; i++) {
    let value = node.classList[i];
    if (value.startsWith(prefix)) {
      node.classList.remove(value);
    }
  }
}

let slideUp = (target, duration = 0) => {
  target.style.transitionProperty = 'height, margin, padding';
  target.style.transitionDuration = duration + 'ms';
  target.style.boxSizing = 'border-box';
  target.style.height = target.offsetHeight + 'px';
  target.offsetHeight;
  target.style.overflow = 'hidden';
  target.style.height = 0;
  target.style.paddingTop = 0;
  target.style.paddingBottom = 0;
  target.style.marginTop = 0;
  target.style.marginBottom = 0;
};

let slideDown = (target, duration = 0) => {
  target.style.removeProperty('display');
  let display = window.getComputedStyle(target).display;

  if (display === 'none') display = 'block';

  target.style.display = display;
  let height = target.offsetHeight;
  target.style.overflow = 'hidden';
  target.style.height = 0;
  target.style.paddingTop = 0;
  target.style.paddingBottom = 0;
  target.style.marginTop = 0;
  target.style.marginBottom = 0;
  target.offsetHeight;
  target.style.boxSizing = 'border-box';
  target.style.transitionProperty = 'height, margin, padding';
  target.style.transitionDuration = duration + 'ms';
  target.style.height = height + 'px';
  target.style.removeProperty('padding-top');
  target.style.removeProperty('padding-bottom');
  target.style.removeProperty('margin-top');
  target.style.removeProperty('margin-bottom');
  window.setTimeout(() => {
    target.style.removeProperty('height');
    target.style.removeProperty('overflow');
    target.style.removeProperty('transition-duration');
    target.style.removeProperty('transition-property');
  }, duration);
};

var slideToggle = (target, duration = 0) => {
  if (window.getComputedStyle(target).display === 'none') {
    return slideDown(target, duration);
  } else {
    return slideUp(target, duration);
  }
};

// =======================================================
// =======================================================
