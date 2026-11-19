<html>
<head>
<title>Profile Editor</title>
<style>
<!--
body { font-family: Verdana; line-spacing: 0 }
td.nb { font: 10pt Verdana }
-->
</style>
<script language="JavaScript">
<!--
function setcookie(name, value, store) {
if (store >= 1) {
var expire = new Date ();
if (store == 1) {
expire.setTime (expire.getTime() + (365*24*60*60*1000));
}
if (store == 2) {
expire.setTime (expire.getTime() + (1*24*60*60*1000));
}
} else {
var expire = null;
}
document.cookie = name + "=" + escape(value) + ((expire == null) ? "" : "; expires=" + expire.toGMTString()) + "; path=/";
}
function cookie_icons_offset() {
var now = new Date ();
var browser_time = now.getTime();
setcookie("lastvisit", browser_time, 1);
var server_now = "1102268391";
if (server_now != "") {
var offset = browser_time - (1000*server_now);
setcookie("offset", offset, 1);
}
}
// -->
</script>
<style type="text/css">
<!--
p.topborder { border-bottom: thin #999999 solid; padding-bottom: 4pt }
p { font: 8pt Verdana; }
table.topsection { }
td.topsect1 { vertical-align: bottom; text-align: left; font: 12pt Verdana; font-weight: 600; }
td.topsect2 { vertical-align: top; text-align: right; font: 8pt Verdana; }
td.nb { font: 8pt Verdana; }
td.b { font: 8pt Verdana; font-weight: 600;}
-->
</style>
</head>
<body bgcolor="#ffffff" text="#000000" link="#0000ff" vlink="#000099" alink="#ff0000" onLoad="document.lif.username.focus()">
<basefont size="1"><font face="Verdana" size="1">
<a name=MT></a>
<p class="topborder">
<table class="topsection" width=100% border=0 cellpadding=0 cellspacing=0>
<tr>
<td class="topsect1">Profile Editor</td>
<td class="topsect2">
<a href="http://www.catchbtk.com/cgi-bin/discus/discus.cgi?pg=logout">Log Out</a> |
<a href="http://www.catchbtk.com/cgi-bin/discus/discus.cgi?pg=topics">Topics</a> |
<a href="http://www.catchbtk.com/cgi-bin/discus/search.cgi">Search</a>
<br>
<a href="http://www.catchbtk.com/cgi-bin/discus/board-contact.cgi">Moderators</a> |
<a href="http://www.catchbtk.com/cgi-bin/discus/board-profile.cgi">Edit Profile</a>
</td>
</tr>
</table>
</p>
<font face="Verdana" size="1">
<form action="http://www.catchbtk.com/cgi-bin/discus/board-profile.cgi" method="post" name="lif">
<input type="hidden" name="forcedest" value="">
<input type="hidden" name="action" value="login">
<input type="hidden" name="script" value="board-profile">
<input type="hidden" name="query_string" value="">
<p></p>
<p>Enter your username and password below to edit your profile.</p>
<table border=1 width=600 cellpadding=5 cellspacing=0 bordercolor="#cccccc" bordercolordark="#f7f7f7" bordercolorlight="#cccccc">
<tr>
<td height=20 width=600 bgcolor="#999999" colspan=2><font color="#f7f7f7" face="Verdana" size="1"><b>Log In</b></font></td>
</tr>
<tr>
<td width=100 valign=center align=right bgcolor="#cccccc"><font color="#000000" face="Verdana" size="1"><b>Username:</b></font></td>
<td width=475 valign=center bgcolor="#cccccc"><input type=text name="username" size=15 value=""></td>
</tr>
<tr>
<td width=100 valign=center align=right bgcolor="#cccccc"><font color="#000000" face="Verdana" size="1"><b>Password:</b></font></td>
<td width=475 valign=center bgcolor="#cccccc"><input type=password name="password" size=15 value=""></td>
</tr>
<tr>
<td width=100 valign=center align=right bgcolor="#cccccc">&nbsp;</td>
<td width=475 valign=center bgcolor="#cccccc">
<input type="submit" value="Log In">
</td>
</tr>
</table>
</form>
<p></p>
<table border=0 cellpadding=4 border=0 cellspacing=0 width=100%>
<tr bgcolor="#999999">
<td valign=top align=left width=80%><font size=1 face="Verdana" color="#f7f7f7"><b>
<a href="http://www.catchbtk.com/cgi-bin/discus/discus.cgi?pg=topics"><font color="#f7f7f7">Topics</font></a>
| <a href="http://www.catchbtk.com/cgi-bin/discus/search.cgi?method=last&number=1&units=1440&tree=ON&where=all"><font color="#f7f7f7">Last Day</font></a>
| <a href="http://www.catchbtk.com/cgi-bin/discus/search.cgi?method=last&number=7&units=1440&tree=ON&where=all"><font color="#f7f7f7">Last Week</font></a>
| <a href="http://www.catchbtk.com/cgi-bin/discus/board-viewtree.cgi"><font color="#f7f7f7">Tree View</font></a>
| <a href="http://www.catchbtk.com/cgi-bin/discus/search.cgi"><font color="#f7f7f7">Search</font></a>
| <a href="http://www.catchbtk.com/cgi-bin/discus/discus.cgi?pg=help"><font color="#f7f7f7">Help/Instructions</font></a>
| <a href="http://www.catchbtk.com/cgi-bin/discus/discus.cgi?pg=credits"><font color="#f7f7f7">Program Credits</font></a>
</td>
<td valign=top align=right width=20%><font size=1 face="Verdana" color="#f7f7f7"><b>
<a href="http://www.catchbtk.com/cgi-bin/discus/discus.cgi?pg=admin" target=_top><font color="#f7f7f7">Administration</font></a>
</b></font>
</td></tr></table>
</body></html>
<!--HTTP Cookie:  -->
<!--Setting Cookies:
  -->
