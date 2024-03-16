// Light / Dark Theme Toggle

// FIXME:
// 1. Fix changing color working with cookies. There is an error while I set cookies and
// change themes. Add try catch to getting cookie code.

function WriteCookie(themeSetting) {
  var now = new Date();
  now.setMonth( now.getMonth() + 6 );

  document.cookie="theme=" + themeSetting;
  document.cookie = "expires=" + now.toUTCString() + ";"
};

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
};

// Set Color Theme Accroding to Save Data in Cookies
function setColorTheme() {
  theme = getCookie("theme");
  themeBody = theme;
  themeBg = "bg-" + theme;
  themeText = "text-" + theme;

  document.body.classList.toggle(themeBody);
  document.getElementById("footer").classList.toggle(themeBg);
  document.getElementById("navbar-menu").classList.toggle(themeBg);
  document.getElementById("navbar-site-name").classList.toggle(themeText);
  document.getElementById("menu-register").classList.toggle(themeText);
  document.getElementById("menu-login").classList.toggle(themeText);
}

const checkbox = document.getElementById("checkbox")
checkbox.addEventListener("change", () => {
  document.body.classList.toggle("dark");
  document.body.classList.toggle("light");
  document.getElementById("footer").classList.toggle("bg-white");
  document.getElementById("footer").classList.toggle("bg-dark");
  document.getElementById("navbar-menu").classList.toggle("bg-white");
  document.getElementById("navbar-menu").classList.toggle("bg-dark");
  document.getElementById("navbar-site-name").classList.toggle("text-light");
  document.getElementById("navbar-site-name").classList.toggle("text-dark");
  document.getElementById("menu-register").classList.toggle("text-light");
  document.getElementById("menu-register").classList.toggle("text-dark");
  document.getElementById("menu-login").classList.toggle("text-light");
  document.getElementById("menu-login").classList.toggle("text-dark");

  let themeSetting = document.body.classList.value;
  WriteCookie(themeSetting);
});

setColorTheme();

// END - Light / Dark Theme Toggle.