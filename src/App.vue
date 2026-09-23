<template>
  <div id="app">
    <div id="nav">
      <div class="container menu">
        <router-link class="" to="/">
          <img alt="OPAS DASHBOARD" width="240" src="./assets/logo-pt-br.png" />
        </router-link>
        <button
          v-if="mobile"
          id="burger"
          @click="toggleMenu()"
          class="open-main-nav d-block d-sm-none  "
        >
          <span class="burger"></span>
          <span class="burger-text">Menu</span>
        </button>

        <div class="menu-navegacao" v-if="!showMenu">
          <router-link class="" to="/">Covid-19 e SRAG</router-link>
          <router-link class="" to="/vacinacao">Vacinação</router-link>
          <router-link class="" to="/ocupacao">Ocupação de leitos</router-link>
          <router-link class="" to="/variantes">Variantes</router-link>
          <router-link class="" to="/indigenas"
            >Covid-19 em terras indígenas</router-link
          >
        </div>
      </div>
    </div>
    <router-view />
  </div>
  
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;700&display=swap");
/* http://meyerweb.com/eric/tools/css/reset/
   v2.0-modified | 20110126
   License: none (public domain)
*/

html,
body,
div,
span,
applet,
object,
iframe,
h1,
h2,
h3,
h4,
h5,
h6,
p,
blockquote,
pre,
a,
abbr,
acronym,
address,
big,
cite,
code,
del,
dfn,
em,
img,
ins,
kbd,
q,
s,
samp,
small,
strike,
strong,
sub,
sup,
tt,
var,
b,
u,
i,
center,
dl,
dt,
dd,
ol,
ul,
li,
fieldset,
form,
label,
legend,
table,
caption,
tbody,
tfoot,
thead,
tr,
th,
td,
article,
aside,
canvas,
details,
embed,
figure,
figcaption,
footer,
header,
hgroup,
menu,
nav,
output,
ruby,
section,
summary,
time,
mark,
audio,
video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}

footer {
	display: block;
	position: absolute;
    bottom: 0;
    width: 100%;
    height: 60px;
    background-color: #f5f5f5;
}

/* make sure to set some focus styles for accessibility */
:focus {
  outline: 0;
}

/* HTML5 display-role reset for older browsers */
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
menu,
nav,
section {
  display: block;
}

body {
  line-height: 1;
}

ol,
ul {
  list-style: none;
}

blockquote,
q {
  quotes: none;
}

blockquote:before,
blockquote:after,
q:before,
q:after {
  content: "";
  content: none;
}

table {
  border-collapse: collapse;
  border-spacing: 0;
}

input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration,
input[type="search"]::-webkit-search-results-button,
input[type="search"]::-webkit-search-results-decoration {
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type="search"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
}

textarea {
  overflow: auto;
  vertical-align: top;
  resize: vertical;
}

/**
 * Correct `inline-block` display not defined in IE 6/7/8/9 and Firefox 3.
 */

audio,
canvas,
video {
  display: inline-block;
  *display: inline;
  *zoom: 1;
  max-width: 100%;
}

/**
 * Prevent modern browsers from displaying `audio` without controls.
 * Remove excess height in iOS 5 devices.
 */

audio:not([controls]) {
  display: none;
  height: 0;
}

/**
 * Address styling not present in IE 7/8/9, Firefox 3, and Safari 4.
 * Known issue: no IE 6 support.
 */

[hidden] {
  display: none;
}

/**
 * 1. Correct text resizing oddly in IE 6/7 when body `font-size` is set using
 *    `em` units.
 * 2. Prevent iOS text size adjust after orientation change, without disabling
 *    user zoom.
 */

html {
  font-size: 100%; /* 1 */
  -webkit-text-size-adjust: 100%; /* 2 */
  -ms-text-size-adjust: 100%; /* 2 */
}

/**
 * Address `outline` inconsistency between Chrome and other browsers.
 */

a:focus {
  outline: thin dotted;
}

/**
 * Improve readability when focused and also mouse hovered in all browsers.
 */

a:active,
a:hover {
  outline: 0;
}

/**
 * 1. Remove border when inside `a` element in IE 6/7/8/9 and Firefox 3.
 * 2. Improve image quality when scaled in IE 7.
 */

img {
  border: 0; /* 1 */
  -ms-interpolation-mode: bicubic; /* 2 */
}

/**
 * Address margin not present in IE 6/7/8/9, Safari 5, and Opera 11.
 */

figure {
  margin: 0;
}

/**
 * Correct margin displayed oddly in IE 6/7.
 */

form {
  margin: 0;
}

/**
 * Define consistent border, margin, and padding.
 */

fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}

/**
 * 1. Correct color not being inherited in IE 6/7/8/9.
 * 2. Correct text not wrapping in Firefox 3.
 * 3. Correct alignment displayed oddly in IE 6/7.
 */

legend {
  border: 0; /* 1 */
  padding: 0;
  white-space: normal; /* 2 */
  *margin-left: -7px; /* 3 */
}

/**
 * 1. Correct font size not being inherited in all browsers.
 * 2. Address margins set differently in IE 6/7, Firefox 3+, Safari 5,
 *    and Chrome.
 * 3. Improve appearance and consistency in all browsers.
 */

button,
input,
select,
textarea {
  font-size: 100%; /* 1 */
  margin: 0; /* 2 */
  vertical-align: baseline; /* 3 */
  *vertical-align: middle; /* 3 */
}

/**
 * Address Firefox 3+ setting `line-height` on `input` using `!important` in
 * the UA stylesheet.
 */

button,
input {
  line-height: normal;
}

/**
 * Address inconsistent `text-transform` inheritance for `button` and `select`.
 * All other form control elements do not inherit `text-transform` values.
 * Correct `button` style inheritance in Chrome, Safari 5+, and IE 6+.
 * Correct `select` style inheritance in Firefox 4+ and Opera.
 */

button,
select {
  text-transform: none;
}

/**
 * 1. Avoid the WebKit bug in Android 4.0.* where (2) destroys native `audio`
 *    and `video` controls.
 * 2. Correct inability to style clickable `input` types in iOS.
 * 3. Improve usability and consistency of cursor style between image-type
 *    `input` and others.
 * 4. Remove inner spacing in IE 7 without affecting normal text inputs.
 *    Known issue: inner spacing remains in IE 6.
 */

button,
html input[type="button"], /* 1 */
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button; /* 2 */
  cursor: pointer; /* 3 */
  *overflow: visible; /* 4 */
}

/**
 * Re-set default cursor for disabled elements.
 */

button[disabled],
html input[disabled] {
  cursor: default;
}

/**
 * 1. Address box sizing set to content-box in IE 8/9.
 * 2. Remove excess padding in IE 8/9.
 * 3. Remove excess padding in IE 7.
 *    Known issue: excess padding remains in IE 6.
 */

input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box; /* 1 */
  padding: 0; /* 2 */
  *height: 13px; /* 3 */
  *width: 13px; /* 3 */
}

/**
 * 1. Address `appearance` set to `searchfield` in Safari 5 and Chrome.
 * 2. Address `box-sizing` set to `border-box` in Safari 5 and Chrome
 *    (include `-moz` to future-proof).
 */

input[type="search"] {
  -webkit-appearance: textfield; /* 1 */
  -moz-box-sizing: content-box;
  -webkit-box-sizing: content-box; /* 2 */
  box-sizing: content-box;
}

/**
 * Remove inner padding and search cancel button in Safari 5 and Chrome
 * on OS X.
 */

input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}

/**
 * Remove inner padding and border in Firefox 3+.
 */

button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}

/**
 * 1. Remove default vertical scrollbar in IE 6/7/8/9.
 * 2. Improve readability and alignment in all browsers.
 */

textarea {
  overflow: auto; /* 1 */
  vertical-align: top; /* 2 */
}

/**
 * Remove most spacing between table cells.
 */

table {
  border-collapse: collapse;
  border-spacing: 0;
}

html,
button,
input,
select,
textarea {
  color: #222;
}

::-moz-selection {
  background: #b3d4fc;
  text-shadow: none;
}

::selection {
  background: #b3d4fc;
  text-shadow: none;
}

img {
  vertical-align: middle;
}

fieldset {
  border: 0;
  margin: 0;
  padding: 0;
}

textarea {
  resize: vertical;
}

.chromeframe {
  margin: 0.2em 0;
  background: #ccc;
  color: #000;
  padding: 0.2em 0;
}

/* RESET FIM */

body {
  font-family: "Oswald", sans-serif;
  /* min-height: 3004px; */
  scroll-behavior: smooth;
}
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* cursor: grab;
  overflow: auto; */
}

.container {
  max-width: 90%;
  margin: 0 auto;
}

#nav {
  background: #fafafa;
  margin-bottom: 60px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 10;
}

#nav .menu {
  padding: 20px 30px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 10;
}

#nav .menu-navegacao a {
  font-weight: 500;
  color: #333;
  font-size: 1rem;
  text-decoration: none;
  text-transform: uppercase;
  position: relative;
}
#nav .menu-navegacao a:hover {
  color: #ff671b;
}
#nav .menu-navegacao a:not(:last-child)::after {
  content: "";
  width: 2px;
  height: 100%;
  background: #dadada;
  position: absolute;
  margin-left: 15px;
  bottom: 0;
}

#nav .menu-navegacao a:not(:last-child) {
  margin-right: 30px;
}

#nav .menu-navegacao a.router-link-exact-active {
  color: #333;
}
.colunas .container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
}
.colunas4 .container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 20px;
}
.colunas6 .container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
  gap: 20px;
}
.graficos.brasil {
  background: #f6f6f6;
  /* padding: 2rem; */
}
.graficos.por-regiao {
  background: #fafafa;
  padding: 60px 0;
}
.graficos.por-regiao .lista-graficos {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 30px;
}
.grafico {
  position: relative;
}
.grafico h2 {
  /* position: absolute; */
  z-index: 1;
  font-size: 1.3rem;
  text-transform: uppercase;
  font-weight: 500;
}
.graficos header h2 {
  font-size: 1.6rem;
  text-align: left;
  padding: 30px 0;
  /* max-width: 40%; */
  line-height: 2.5rem;
  text-transform: uppercase;
  font-weight: 500;
}
.home {
  /* display: flex; */
  margin-top: 130px;
}
.topo {
  display: flex;
  margin-bottom: 80px;
  /* padding-bottom: 80px; */
  border-bottom: 2px solid #ccc;
}
.dados {
  min-width: 40%;
}
.tipo {
  text-align: left;
  padding: 0 0 30px 0;
}
.date-range {
  padding: 15px 0;
}
.date-range .mx-datepicker-range {
  width: 416px;
}
.tipo a {
  border: 0;
  font-size: 1.4rem;
  font-weight: 500;
  padding: 15px 25px;
  min-width: 150px;
  margin-right: 15px;
  background: #ff671b;
  color: #fff;
  position: relative;
  text-decoration: none;
  display: inline-block;
  text-align: left;
}

.tipo a.covid {
  background: #0099d9;
}
.tipo a:hover::before {
  content: "";
  border: 2px solid #fff;
  position: absolute;
  left: 2px;
  top: 2px;
  bottom: 2px;
  right: 2px;
  z-index: 12;
}
.mapa {
  width: 100%;
  position: relative;
  z-index: 2;
  max-height: 750px;
  overflow: hidden;
}
.mapa1 {
  width: 100%;
  position: relative;
  z-index: 2;
  max-height: 350px;
  overflow: hidden;
}
.dados .cards {
  text-align: left;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  grid-auto-rows: max-content;
}
.dadosv .cardsv {
  text-align: left;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 30px;
  grid-auto-rows: max-content;
}
.dadosi .cardsi {
  text-align: left;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  gap: 30px;
  grid-auto-rows: max-content;
}
.dados .cards h2 {
  font-size: 0.8rem;
  margin-bottom: 15px;
  text-transform: uppercase;
  font-weight: 400;
  /* background: #fbfbfb; */
  line-height: 1rem;
  color: #a0a0a0;
  margin-top: 10px;
  border-bottom: 2px solid;
  display: inline-block;
  align-self: start;
  padding-right: 0px;
  padding-bottom: 5px;
}
.dadosv .cardsv h2 {
  font-size: 0.8rem;
  margin-bottom: 15px;
  text-transform: uppercase;
  font-weight: 400;
  /* background: #fbfbfb; */
  line-height: 1rem;
  color: #a0a0a0;
  margin-top: 10px;
  border-bottom: 2px solid;
  display: inline-block;
  align-self: start;
  padding-right: 0px;
  padding-bottom: 5px;
}
.dadosi .cardsi h2 {
  font-size: 0.8rem;
  margin-bottom: 15px;
  text-transform: uppercase;
  font-weight: 400;
  /* background: #fbfbfb; */
  line-height: 1rem;
  color: #a0a0a0;
  margin-top: 10px;
  border-bottom: 2px solid;
  display: inline-block;
  align-self: start;
  padding-right: 0px;
  padding-bottom: 5px;
}
.dados .cards h4 {
  font-size: 3rem;
  /* font-weight: bold; */
  margin-bottom: 15px;
  margin-top: 5px;
  letter-spacing: -2px;
}
.dadosv .cardsv h4 {
  font-size: 3rem;
  /* font-weight: bold; */
  margin-bottom: 15px;
  margin-top: 5px;
  letter-spacing: -2px;
}
.dadosi .cardsi h4 {
  font-size: 3rem;
  /* font-weight: bold; */
  margin-bottom: 15px;
  margin-top: 5px;
  letter-spacing: -2px;
}
.dados .cards .card {
  padding: 2rem 1.5rem;
  /* background: #f6f6f6; */
  display: flex;
  /* align-items: center; */
  flex-direction: column;
  /* justify-content: center; */
  text-align: left;
  /* border: 1px solid #e0e0e0; */
  border-radius: 8px;
  justify-content: center;
  position: relative;
  z-index: 3;
  /* box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px; */
  box-shadow: rgba(50, 50, 93, 0.2) 0px 1px 5px -1px,
    rgba(0, 0, 0, 0.2) 0px 0px 3px -1px;
}
.dadosv .cardsv .card {
  padding: 2rem 1.5rem;
  /* background: #f6f6f6; */
  display: flex;
  /* align-items: center; */
  flex-direction: column;
  /* justify-content: center; */
  text-align: left;
  /* border: 1px solid #e0e0e0; */
  border-radius: 8px;
  justify-content: center;
  position: relative;
  z-index: 3;
  /* box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px; */
  box-shadow: rgba(50, 50, 93, 0.2) 0px 1px 5px -1px,
    rgba(0, 0, 0, 0.2) 0px 0px 3px -1px;
}
.dadosi .cardsi .card {
  padding: 2rem 1.5rem;
  /* background: #f6f6f6; */
  display: flex;
  /* align-items: center; */
  flex-direction: column;
  /* justify-content: center; */
  text-align: left;
  /* border: 1px solid #e0e0e0; */
  border-radius: 8px;
  justify-content: center;
  position: relative;
  z-index: 3;
  /* box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px; */
  box-shadow: rgba(50, 50, 93, 0.2) 0px 1px 5px -1px,
    rgba(0, 0, 0, 0.2) 0px 0px 3px -1px;
}
.dados .cards .card.covid h2 {
  border-color: #0099d9;
}
.dados .cards .card.srag h2 {
  border-color: #ff671b;
}
.dados .cards .card.covid h2 {
  border-color: #0099d9;
}
.dados .cards .card.indigena h2 {
  border-color: #0099d9;
}
.dadosv .cardsv .card.Alpha h2 {
  border-color: #E5AB53;
}
.dadosv .cardsv .card.Beta h2 {
  border-color: #3288bd;
}
.dadosv .cardsv .card.Gamma h2 {
  border-color: #9F579E;
}
.dadosv .cardsv .card.Delta h2 {
  border-color: #7A8F2D;
}
.dadosv .cardsv .card.Omicron h2 {
  border-color: #3D5486;
}
.dadosv .cardsv .card.Lambda h2 {
  border-color: #b2abd2;
}
.dadosv .cardsv .card.Mu h2 {
  border-color: #C0641F;
}

.componente-mapa {
  height: 750px;
}

.componente-mapa1 {
  height: 350px;
}

.app-content {
  padding-top: 120px;
}
.interna-titulo {
  text-align: left;
  font-size: 2.2rem;
  text-transform: uppercase;
  font-weight: bold;
  padding: 30px 0;
}

/* Burger Style: @see: https://codepen.io/CreativeJuiz/full/oMZNXy */
.open-main-nav {
  position: absolute;
  top: 15px;
  padding-top: 20px;
  right: 15px;
  z-index: 1000;
  background: none;
  border: 0;
  cursor: pointer;
}
.open-main-nav:focus {
  outline: none;
}
.burger {
  position: relative;
  display: block;
  width: 28px;
  height: 4px;
  margin: 0 auto;
  background: #e9a04e;
  transform: skew(5deg);
  transition: all 0.275s;
}

.burger:after,
.burger:before {
  content: "";
  display: block;
  height: 100%;
  background: #e9a04e;
  transition: all 0.275s;
}

.burger:after {
  transform: translateY(-12px) translateX(-2px) skew(-20deg);
}

.burger:before {
  transform: translateY(-16px) skew(-10deg);
}

/* Toggle State part */
.is-open .burger {
  transform: skew(5deg) translateY(-8px) rotate(-45deg);
}

.is-open .burger:before {
  transform: translateY(0px) skew(-10deg) rotate(75deg);
}

.is-open .burger:after {
  transform: translateY(-12px) translateX(10px) skew(-20deg);
  opacity: 0;
}

/* Wider than desktop */
@media (min-width: 1200px) {
}

/* Landscape phone to desktop */
@media (max-width: 1199px) {
}

/* Landscape phone to landscape tablet */
@media (max-width: 979px) {
}

/* Small desktop */
@media (min-width: 980px) and (max-width: 1199px) {
}

/* Portrait tablet to landscape tablet */
@media (min-width: 768px) and (max-width: 979px) {
}

/* Landscape phone to portrait tablet */
@media (max-width: 767px) {
  .home {
    margin-top: 122px;
  }
  .topo {
    display: inline;
  }
  .tipo {
    padding: 0 0 30px;
  }
  .tipo a.srag {
    right: 0;
    position: absolute;
    margin-right: 0;
    margin-top: 20px;
    z-index: 9;
  }
  .tipo a.covid {
    margin-right: 0;
    z-index: 2;
  }
  .dados .cards {
    display: block;
    padding: 15px;
  }
  .dadosi .cardsi {
    display: block;
    padding: 15px;
  }
  #nav .menu a img {
    width: 100%;
  }
  .menu-navegacao {
    position: absolute;
    top: 0;
    /* bottom: 0; */
    left: 0;
    right: 0;
    background: #fafafa;
    padding: 30px;
    box-shadow: rgb(0 0 0 / 16%) 0px 1px 4px;
  }
  #nav .menu-navegacao a:not(:last-child)::after {
    width: 0;
  }
  #nav .menu-navegacao a {
    display: block;
    text-align: left;
    margin-bottom: 15px;
  }
  .graficos.por-regiao .lista-graficos {
    display: inline;
  }
  .graficos header h2 {
    max-width: 100%;
    font-size: 1.8rem;
  }
  .colunas {
    display: inline;
    grid-template-columns: 1fr 1fr;
  }
  .colunas .container {
    display: inline-block;
  }
  .colunas4 {
    display: inline;
    grid-template-columns: 1fr 1fr 1fr 1fr;
  }
  .colunas4 .container {
    display: inline-block;
  }
  .colunas6 {
    display: inline;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
  }
  .colunas6 .container {
    display: inline-block;
  }
  .leaflet-bottom .info {
    top: 64px;
  }
  #nav .menu {
    padding: 10px 15px;
  }

  .container.menu a {
    max-width: 270px;
  }
}

/* Landscape phones and smaller */
@media (max-width: 480px) {
}
</style>
<script>
export default {
  data() {
    return {
      mobile: screen.width <= 760,
      showMenu: screen.width <= 760,
    };
  },
  mounted() {
    this.onResize();
    window.addEventListener("resize", this.onResize, { passive: true });
  },
  methods: {
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
    onResize() {
      this.mobile = screen.width <= 760;
      this.showMenu = screen.width <= 760;
    },
  },
};
</script>
