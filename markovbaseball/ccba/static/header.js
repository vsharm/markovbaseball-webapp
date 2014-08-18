function headerbutton(teamsHeader){
  console.log(teamsHeader);
  var teamNode = document.querySelector('.team');
  var menu = document.querySelector(".menu_item");
  var menuMain = document.querySelector(".menu");
  var menu_link = document.querySelector(".menu_link");
  var hover = document.querySelector("nav li:hover ul");
  if(teamsHeader){
    teamNode.style.color = "#fff";
    teamNode.style.backgroundColor = "#d9534f";
    menu.style.fontSize = "20px";
    menu.style.paddingTop="10px";
    menu.style.paddingBottom="10px";
    hover.style.display = "block";
    hover.style.position = "absolute";
    hover.style.width="100px";
    hover.style.float="left";
    menu_link.style.color = "black";
    menu_link.style.textDecoration="none"; 
  }
  else{
    teamNode.style.color = "#aaa";
    teamNode.style.backgroundColor = "";
    menu.style.fontSize = "";
    menu.style.paddingTop="";
    menu.style.paddingBottom="";
    menuMain.style.display = "";
    menuMain.style.position = "";
    menuMain.style.width="";
    menuMain.style.float="";
  }
}

  //google anylitics
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-53909133-1', 'auto');
  ga('send', 'pageview');
