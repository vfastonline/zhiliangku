webpackJsonp([19],{Dnxr:function(t,i){var n=window.jquery;t.exports={initAnimationItems:function(){n(".animated").each(function(){var t,i;n(this).attr("data-origin-class",n(this).attr("class")),t=n(this).data("ani-duration"),i=n(this).data("ani-delay"),n(this).css({visibility:"hidden","animation-duration":t,"-webkit-animation-duration":t,"animation-delay":i,"-webkit-animation-delay":i})})},playAnimation:function(t){this.clearAnimation();var i=t.slides[t.activeIndex].querySelectorAll(".animated");n(i).each(function(){var t;n(this).css({visibility:"visible"}),t=n(this).data("ani-name"),n(this).addClass(t)})},clearAnimation:function(){n(".animated").each(function(){n(this).css({visibility:"hidden"}),n(this).attr("class",n(this).data("origin-class"))})}}},Ko4C:function(t,i,n){t.exports=n.p+"static/media/background.5c3cc7b.mp3"},OMN4:function(t,i){t.exports=axios},QAku:function(t,i){},XlGV:function(t,i){},aH0l:function(t,i,n){"use strict";Object.defineProperty(i,"__esModule",{value:!0});var e=n("lRwf"),a=n.n(e),s={data:function(){return{show:!1,num:100,show_num:!1}},components:{},created:function(){var t=this;this.$get("/wechat/thumbsuptotal?name=wangjinlong").then(function(i){t.num=i.data.total})},mounted:function(){var t=this,i=window.jQuery;i(document).ready(function(){var n=!0,e=document.querySelector(".the_button"),a=document.querySelector(".notice");e.addEventListener("touchstart",function(t){n&&i(t.target).addClass("the_button_active")}),e.addEventListener("touchend",function(s){n&&(i(a).addClass("notice_actve"),i.get("http://www.zhiliangku.com/wechat/thumbsup?name=wangjinlong",function(s){s.err||(i(e).removeClass("the_button_active"),t.show=!t.show,setTimeout(function(){t.num++,t.show=!1,t.show_num=!0},800),setInterval(function(){i(a).removeClass("notice_actve")},1300),n=!1)}))})})}},c={render:function(){var t=this,i=t.$createElement,n=t._self._c||i;return n("div",{staticClass:"project_container"},[t._m(0),t._v(" "),n("div",{staticClass:"swiper-container"},[n("div",{staticClass:"swiper-wrapper"},[n("div",{staticClass:"swiper-slide slide-1"}),t._v(" "),n("div",{staticClass:"swiper-slide slide-2"}),t._v(" "),n("div",{staticClass:"swiper-slide slide-3"}),t._v(" "),n("div",{staticClass:"swiper-slide slide-4"}),t._v(" "),n("div",{staticClass:"swiper-slide slide-5"}),t._v(" "),n("div",{staticClass:"swiper-slide slide-6"}),t._v(" "),n("div",{staticClass:"swiper-slide slide-7"},[n("div",{staticClass:"notice"},[t._v("送你个么么哒~~q^_^p~~")]),t._v(" "),n("div",{staticClass:"the_button"},[n("span",[t._v("为他打call")]),t._v(" "),n("span",{staticClass:"count db a"},[n("span",{staticClass:"animated",class:{shake:t.show_num}},[t._v(t._s(t.num))]),t._v(" "),n("transition",{attrs:{"enter-active-class":"animated fadeInUp"}},[t.show?n("span",{staticClass:"added a"},[t._v("+1")]):t._e()])],1)])])])]),t._v(" "),t._m(1),t._v(" "),t._m(2),t._v(" "),t._m(3)])},staticRenderFns:[function(){var t=this.$createElement,i=this._self._c||t;return i("div",{staticClass:"loading-overlay"},[i("img",{attrs:{src:n("eRaf")}})])},function(){var t=this.$createElement,i=this._self._c||t;return i("button",{staticClass:"up-arrow"},[i("i",{staticClass:"icon-angle-double-up"})])},function(){var t=this.$createElement,i=this._self._c||t;return i("button",{staticClass:"btn-music"},[i("i",{staticClass:"icon-note"})])},function(){var t=this.$createElement,i=this._self._c||t;return i("audio",{attrs:{loop:""}},[i("source",{attrs:{src:n("Ko4C"),type:"audio/mpeg"}})])}]};var o=n("Z0/y")(s,c,!1,function(t){n("XlGV"),n("ksw8")},null,null).exports;n("nUgu"),n("iCGY"),n("rar4");a.a.config.productionTip=!1,new a.a({el:"#app",components:{App:o},template:"<App/>"})},eRaf:function(t,i){t.exports="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0nODhweCcgaGVpZ2h0PSc4OHB4JyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIiBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCIgY2xhc3M9InVpbC1iYWxscyI+PHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjEwMCIgaGVpZ2h0PSIxMDAiIGZpbGw9Im5vbmUiIGNsYXNzPSJiayI+PC9yZWN0PjxnIHRyYW5zZm9ybT0icm90YXRlKDAgNTAgNTApIj4NCiAgPGNpcmNsZSByPSI1IiBjeD0iMzAiIGN5PSI1MCI+DQogICAgPGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJ0cmFuc2xhdGUiIGJlZ2luPSIwcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGR1cj0iMXMiIHZhbHVlcz0iMCAwOzEzLjgxOTY2MDExMjUwMTA1MSAtMTkuMDIxMTMwMzI1OTAzMDciIGtleVRpbWVzPSIwOzEiLz4NCiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJmaWxsIiBkdXI9IjFzIiBiZWdpbj0iMHMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiAga2V5VGltZXM9IjA7MSIgdmFsdWVzPSIjNTFjYWNjOyM5ZGY4NzEiLz4NCiAgPC9jaXJjbGU+DQo8L2c+PGcgdHJhbnNmb3JtPSJyb3RhdGUoNzIgNTAgNTApIj4NCiAgPGNpcmNsZSByPSI1IiBjeD0iMzAiIGN5PSI1MCI+DQogICAgPGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJ0cmFuc2xhdGUiIGJlZ2luPSIwcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGR1cj0iMXMiIHZhbHVlcz0iMCAwOzEzLjgxOTY2MDExMjUwMTA1MSAtMTkuMDIxMTMwMzI1OTAzMDciIGtleVRpbWVzPSIwOzEiLz4NCiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJmaWxsIiBkdXI9IjFzIiBiZWdpbj0iMHMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiAga2V5VGltZXM9IjA7MSIgdmFsdWVzPSIjOWRmODcxOyNlMGZmNzciLz4NCiAgPC9jaXJjbGU+DQo8L2c+PGcgdHJhbnNmb3JtPSJyb3RhdGUoMTQ0IDUwIDUwKSI+DQogIDxjaXJjbGUgcj0iNSIgY3g9IjMwIiBjeT0iNTAiPg0KICAgIDxhbmltYXRlVHJhbnNmb3JtIGF0dHJpYnV0ZU5hbWU9InRyYW5zZm9ybSIgdHlwZT0idHJhbnNsYXRlIiBiZWdpbj0iMHMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBkdXI9IjFzIiB2YWx1ZXM9IjAgMDsxMy44MTk2NjAxMTI1MDEwNTEgLTE5LjAyMTEzMDMyNTkwMzA3IiBrZXlUaW1lcz0iMDsxIi8+DQogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iZmlsbCIgZHVyPSIxcyIgYmVnaW49IjBzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIgIGtleVRpbWVzPSIwOzEiIHZhbHVlcz0iI2UwZmY3NzsjZGU5ZGQ2Ii8+DQogIDwvY2lyY2xlPg0KPC9nPjxnIHRyYW5zZm9ybT0icm90YXRlKDIxNiA1MCA1MCkiPg0KICA8Y2lyY2xlIHI9IjUiIGN4PSIzMCIgY3k9IjUwIj4NCiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InRyYW5zbGF0ZSIgYmVnaW49IjBzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIgZHVyPSIxcyIgdmFsdWVzPSIwIDA7MTMuODE5NjYwMTEyNTAxMDUxIC0xOS4wMjExMzAzMjU5MDMwNyIga2V5VGltZXM9IjA7MSIvPg0KICAgIDxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9ImZpbGwiIGR1cj0iMXMiIGJlZ2luPSIwcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiICBrZXlUaW1lcz0iMDsxIiB2YWx1ZXM9IiNkZTlkZDY7I2ZmNzA4ZSIvPg0KICA8L2NpcmNsZT4NCjwvZz48ZyB0cmFuc2Zvcm09InJvdGF0ZSgyODggNTAgNTApIj4NCiAgPGNpcmNsZSByPSI1IiBjeD0iMzAiIGN5PSI1MCI+DQogICAgPGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJ0cmFuc2xhdGUiIGJlZ2luPSIwcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGR1cj0iMXMiIHZhbHVlcz0iMCAwOzEzLjgxOTY2MDExMjUwMTA1MSAtMTkuMDIxMTMwMzI1OTAzMDciIGtleVRpbWVzPSIwOzEiLz4NCiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJmaWxsIiBkdXI9IjFzIiBiZWdpbj0iMHMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiAga2V5VGltZXM9IjA7MSIgdmFsdWVzPSIjZmY3MDhlOyM1MWNhY2MiLz4NCiAgPC9jaXJjbGU+DQo8L2c+PC9zdmc+"},hLRv:function(t,i,n){"use strict";var e=n("lRwf"),a=n.n(e);i.a=new a.a},i1om:function(t,i){t.exports={httpUrl:""}},iCGY:function(t,i){},jzHt:function(t,i){},ksw8:function(t,i){},lRwf:function(t,i){t.exports=Vue},nUgu:function(t,i,n){"use strict";var e=n("i1om"),a=n.n(e),s=n("hLRv"),c=n("rVsN"),o=n.n(c),r=n("lRwf"),l=n.n(r),d=n("OMN4"),u=n.n(d);u.a.defaults.withCredentials=!0,u.a.defaults.baseURL=a.a.httpUrl;var I=function(t,i){var n=function(n){for(var e=i.$notify({type:"error",message:t.data.msg,offset:100,duration:3e3,position:"bottom-right"}),a=document.getElementsByClassName(e.$el.className),s=0;s<a.length;s++)a[s].style.zIndex=2e4;n&&n()};switch(t.data.err){case 1:n();break;case 2:n(),s.a.$emit("specify_display",{show_key:"log_up",title_key:"登录"});break;case 3:case 4:case 5:case 6:case 7:case 8:n()}return t};l.a.prototype.$post=function(t,i){var n=this;return u.a.post(t,i).then(function(t){return I(t,n),new o.a(function(i,n){i(t)})})},l.a.prototype.$get=function(t,i){var n=this;return u.a.get(t,i).then(function(t){return I(t,n),new o.a(function(i,n){i(t)})})};var m=n("ut5U"),g=n.n(m),h=(n("jzHt"),n("QAku"),n("wYhN")),p=n.n(h);l.a.prototype.$notify=p.a,l.a.prototype.$myConst=a.a,l.a.prototype.$fn=g.a},rar4:function(t,i,n){!function(){"use strict";var t=n("Dnxr"),i=window.jQuery,e=window.Swiper;i(document).ready(function(){var n=i("audio").get(0),a=i(".btn-music"),s=i(".up-arrow");a.click(function(){n.paused?(n.play(),i(this).removeClass("paused")):(n.pause(),i(this).addClass("paused"))}),new e(".swiper-container",{mousewheelControl:!0,effect:"coverflow",speed:400,direction:"vertical",fade:{crossFade:!1},coverflow:{rotate:100,stretch:0,depth:300,modifier:1,slideShadows:!1},flip:{limitRotation:!0,slideShadows:!1},onInit:function(i){t.initAnimationItems(),t.playAnimation(i)},onTransitionStart:function(t){t.activeIndex===t.slides.length-1?s.hide():s.show()},onTransitionEnd:function(i){t.playAnimation(i)},onTouchStart:function(t,i){!a.hasClass("paused")&&n.paused&&n.play()}});var c=function(){!a.hasClass("paused")&&n.paused&&n.play()};document.addEventListener("touchstart",c),setTimeout(c,500),i(".loading-overlay").slideUp()})}()},ut5U:function(t,i){var n;t.exports=n={go:function(t){window.location.href="http://"+window.location.host+t},changeShow:function(t,i){t[i]=!t[i]},addObjString:function(t,i,n){i[n]=t+i[n]},addString:function(t,i,e){if(i instanceof Array){for(var a=0;a<i.length;a++)if(e){if(e instanceof Array)for(var s=0;s<e.length;s++)n.addObjString(t,i[a],e[s]);"string"==typeof e&&(i[a][e]=t+i[a][e])}else i.splice(a,1,t+i[a]);return i}if("string"==typeof i)return t+i;i[e]=t+i[e]},initMainData:function(t,i,n){for(var e=1;e<i.length;e++)void 0!==t.arr&&null!==t.arr||(t.arr[e]=n[e]);return t},initStyle:function(t,i,n){if(t[i]&&t[i]instanceof Object)for(var e=0;e<n.length;e++)t[i][n[e]]&&(t[n[e]]=t[i][n[e]])},exchangeKey:function(t,i,n,e){return t[n]=t[i],e&&delete t[i],t},exchangeObjectKey:function(t,i,e,a){for(var s=0;s<i.length;s++)n.exchangeKey(t,i[s],e[s],a);return t},exchangeArrayObjectKey:function(t,i,e,a){for(var s=0;s<t.length;s++)n.exchangeObjectKey(t[s],i,e,a);return t},getSearch:function(){var t;if(window.location.search&&(t=window.location.search.substr(1)),t)return t},getSearchKey:function(t){var i=n.getSearch();if(i)for(var e=i.split("&"),a=0;a<e.length;a++)if(e[a]){var s=e[a].split("=");if(s[0]===t)return s[1]}},getCookie:function(t){for(var i=document.cookie.split(";"),n=0;n<i.length;n++){var e=i[n].split("=");if(e[0]===t||e[0]===" "+t)return e[1]}},getCookies:function(t){var i=[];t.each(function(t){i.push(n.getCookie(t))})},getTargetVue:function(t,i){for(var n=0;n<t.length;n++)if(t[n].name===i)return t[n]},objToSearch:function(t){var i="";for(var n in t)i=i+n+"="+t[n]+"&";return i},funcUrlDel:function(t){var i=window.location,n=i.origin+i.pathname+"?",e=i.search.substr(1);if(e.indexOf(t)>-1){for(var a={},s=e.split("&"),c=0;c<s.length;c++)s[c]=s[c].split("="),a[s[c][0]]=s[c][1];return delete a[t],n+window.JSON.stringify(a).replace(/[\"\{\}]/g,"").replace(/\:/g,"=").replace(/\,/g,"&")}},showNotice:function(t,i,n){t.$notify({type:n||"info",message:i,offset:100,duration:3e3,position:"bottom-right"})},funcUrl:function(t,i,n){var e,a=window.location,s=void 0===n?a.origin+a.pathname+"?":"",c=a.search.substr(1);if(void 0===t)return c;if(void 0===i){var o=c.match(new RegExp("(^|&)"+t+"=([^&]*)(&|$)"));return null!=o?decodeURI(o[2]):null}if(""===c)e=s+t+"="+i,e=t+"="+i,window.location.search="?"+e;else{for(var r={},l=c.split("&"),d=0;d<l.length;d++)l[d]=l[d].split("="),r[l[d][0]]=l[d][1];r[t]=i,e=s+window.JSON.stringify(r).replace(/[\"\{\}]/g,"").replace(/\:/g,"=").replace(/\,/g,"&"),window.location.search="?"+window.JSON.stringify(r).replace(/[\"\{\}]/g,"").replace(/\:/g,"=").replace(/\,/g,"&")}return e}}}},["aH0l"]);