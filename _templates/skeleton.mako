## -*- coding: utf-8 -*-
<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html dir="ltr" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml" lang="en">

<head>
  <title>${title} - Ubuntu FAQ</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="description" content="${title} Ubuntu Faq" />
  % if tags is UNDEFINED:
    <meta name="keywords" content="ubuntu, ${title}" />
  % else:
    <meta name="keywords" content="ubuntu, ${tags}" />
  %endif
  <meta name="verify-reformal" content="47570c0e20eec98528284fe7" />
  <link rel="stylesheet" href="style.css" type="text/css" media="screen" />
  <script type="text/javascript" src="jquery.js"></script>

</head>
<body>

  <div id="container">
    <div id="wrapper">


      <div id="buttons">
        <a rel="nofollow" href="/">article</a>
        <a rel="nofollow" href="/">edit</a>
        <a rel="nofollow" href="/">comment</a>
        <b><a rel="nofollow" href="http://thexnews.com/contacts">Комментировать</a></b>
      </div>

      <div id="content" class="bordered">
        <h1>${title}</h1>

        ${next.body()}
      </div>

      <div id="cloud" class="bordered">

        

      </div>


    </div>
  
    <div id="navigation">
      <div id="logo"><img src="ubuntu.png" alt="ubuntu"></div>
      <div class="otstup">navigation</div>
      
      <div id="menu" class="bordered">

        <%include file="menu.mako"/>
 
      </div>
  
      <div class="otstup">search</div>
        <div id="search" class="bordered box">

<div class="yandexform" onclick="return {'bg': '#ffffff', 'language': 'ru', 'encoding': '', 'suggest': false, 'tld': 'ru', 'site_suggest': false, 'webopt': false, 'fontsize': 13, 'arrow': false, 'fg': '#000000', 'logo': 'rb', 'websearch': false, 'type': 3}"><form action="http://thexnews.com/ubuntu/Y_Search" method="get"><input type="hidden" name="searchid" value="1834280"/><input name="text"/><input type="submit" value="Найти"/></form></div><script type="text/javascript" src="http://site.yandex.net/load/form/1/form.js" charset="utf-8"></script>

        </div>

    </div>

  <div id="footer">
    <a href="http://dmi3.net">ц</a> <a href=''>Димоныч-"Wiki" ${version}</a></p>
  </div>
</div>

  <%include file="counters.mako"/>

</body>

</html>

