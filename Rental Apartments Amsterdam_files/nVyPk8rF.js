(function(){var bhi={"DistancePerMove":0,"MouseMoves":0,"SessionTime":0};var bsi={"IsChrome":false,"WindowChrome":false,"WebDriver":false,"PermissionStatus":"","NotificationPermission":"","Touch":false};var cpt={};bsi.WebDriver=document.getElementById("webdriver-result");function put(url,body){var xhr=new XMLHttpRequest();xhr.open("PUT",url);xhr.setRequestHeader("Content-Type","application/json");xhr.send(body);}
function submitbhi(){put("/js/3XyWgyFTdrOY53wOY4LIRon7ClDBbtH4g4Pkri5tzIftAB7muHS0V66mhwLiPgbU/bhi/submit",JSON.stringify(bhi));}
function submitbsi(){put("/js/3XyWgyFTdrOY53wOY4LIRon7ClDBbtH4g4Pkri5tzIftAB7muHS0V66mhwLiPgbU/bsi/submit",JSON.stringify(bsi));}
function submitcpt(){put("/js/3XyWgyFTdrOY53wOY4LIRon7ClDBbtH4g4Pkri5tzIftAB7muHS0V66mhwLiPgbU/submit",JSON.stringify(cpt));}
function addListener(el,event,func){if(el.addEventListener){el.addEventListener(event,func,false);}
else{el.attachEvent("on"+event,func);}}
bhi.StartSession=Date.now();bsi.Touch=("ontouchstart"in window)||(navigator.maxTouchPoints>0)||(navigator.msMaxTouchPoints>0);var distancePerMove;var dists=[];var prevPosition;addListener(document,"mousemove",mouseMove);function distance(x1,x2,y1,y2){return((x1-x2)**2+(y1-y2)**2)**0.5;}
function pixelsToPercentage(pixels){return pixels/screen.width*100;}
function close(){bhi.SessionTime=Date.now()-bhi.StartSession;bhi.MouseMoves=dists.length;bhi.DistancePerMove=distancePerMove;submitbhi()}
function mouseMove(event){event=event||window.event;pos={x:event.pageX-(window.pageXOffset||document.documentElement.scrollLeft),y:event.pageY-(window.pageYOffset||document.documentElement.scrollTop),}
if(typeof prevPosition=="undefined"){prevPosition=pos;return;}
dists.push(pixelsToPercentage(distance(pos.x,prevPosition.x,pos.y,prevPosition.y,),),);distancePerMove=dists.reduce((a,b)=>a+b,0)/dists.length;prevPosition=pos;}
bsi.WindowChrome=typeof window.chrome!="undefined";bsi.IsChrome=document.getElementById("chrome-result");var ua=navigator.userAgent.toLowerCase();if(ua.indexOf("safari")==-1||ua.indexOf("chrome")!=-1){navigator.permissions.query({name:"notifications"}).then(function(permissionStatus){bsi.NotificationPermission=Notification.permission;bsi.PermissionStatus=permissionStatus.state;submitbsi();});}else if(ua.indexOf("safari")!=-1){}
var oldunload=window.onunload;window.onunload=function(){(oldunload||function(){})();close();}})();