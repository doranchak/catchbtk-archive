<html>
<head>
<title>Search Board</title>
<style>
<!--
body { font-family: Verdana; line-spacing: 0 }
td.nb { font: 10pt Verdana }
td.b { font: 10pt Verdana; font-weight: bold; }
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
var server_now = "1109903717";
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
<body bgcolor="#ffffff" text="#000000" link="#0000ff" vlink="#000099" alink="#ff0000" onLoad="cookie_icons_offset()">
<basefont size="1"><font face="Verdana" size="1">
<a name=MT></a>
<p class="topborder">
<table class="topsection" width=100% border=0 cellpadding=0 cellspacing=0>
<tr>
<td class="topsect1">Search Board</td>
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
<form action="http://www.catchbtk.com/cgi-bin/discus/search.cgi" method="post" name="searchform">
<table border=0 cellspacing=0 cellpadding=1 width=100% bgcolor=#000000><tr><td>
<table border=0 cellpadding=4 cellspacing=1 width=100%>
<tr bgcolor="#f7f7f7">
<td class="b" colspan=2><input type=checkbox name="stype" value="s"> Search by keyword:</td>
</tr>
<tr bgcolor="#cccccc">
<td class="nb" width=175>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search for:</td>
<td><input type=text name="squery" size=35 onChange="if (document.searchform.squery.value.length > 0) { document.searchform.stype[0].checked = true; }" onBlur="if (document.searchform.squery.value.length > 0) { document.searchform.stype[0].checked = true; }"></td>
</tr>
<tr bgcolor="#cccccc">
<td class="nb">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Keyword options:</td>
<td><select name="sopts" size=1>
<option value="0">"Or" (Match any keyword)</option>
<option value="1">"And" (Match all keywords)</option>
</select></td>
</tr>
<tr bgcolor="#cccccc">
<td class="nb">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Match method:</td>
<td><select name="smethod" size=1>
<option value="0">Parts of words</option>
<option value="1">Whole words only</option>
</select></td>
</tr>
<tr bgcolor="#cccccc">
<td class="nb">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Match case:</td>
<td><select name="scase" size=1>
<option value="0">Case insensitive (case does not matter)</option>
<option value="1">Case sensitive (case must match)</option>
</select></td>
</tr>
<tr bgcolor="#cccccc">
<td class="nb">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Look in:</td>
<td><select name="slookin" size=1>
<option value="1">Subject lines</option>
<option value="2">Names of authors</option>
<option value="3" selected>Text of messages</option>
</select></td>
</tr>
<tr bgcolor="#f7f7f7">
<td class="b" colspan=2><input type=checkbox name="stype" value="n" onClick="if (document.searchform.stype[1].checked == false) { document.searchform.nmsm[0].checked = false; document.searchform.nmsm[1].checked = false; } else { if (document.searchform.nmsm[0].checked == 0 && document.searchform.nmsm[1].checked == 0) { document.searchform.nmsm[0].checked = true; }}"> Search by date:</td>
</tr>
<tr bgcolor="#cccccc">
<td class="nb" width=175>&nbsp;&nbsp;&nbsp;&nbsp;<input type=radio name="nmsm" value="1" onClick="document.searchform.stype[1].checked = true">Recent posts:</td>
<td class="nb">Messages posted within the last <input type="text" name="nnumber" size=3 value="3" onClick="document.searchform.nmsm[0].checked = true; document.searchform.stype[1].checked = true;" onBlur="document.searchform.nmsm[0].checked = true; document.searchform.stype[1].checked = true;">&nbsp;<select name="units" size=1 onBlur="document.searchform.nmsm[0].checked = true; document.searchform.stype[1].checked = true;">>
<option value="1">Minute(s)</option>
<option value="60">Hour(s)</option>
<option value="1440" selected>Day(s)</option>
</select></td>
</tr>
<tr bgcolor="#cccccc">
<td class="nb" width=175 valign=top>&nbsp;&nbsp;&nbsp;&nbsp;<input type=radio name="nmsm" value="2" onClick="document.searchform.stype[1].checked = true">Registered&nbsp;users:</td>
<td class="nb">Messages since I last checked for new messages:
<ul><table>
<tr><td class="nb">Username:</td>
<td><input type=text name="username" size="15" value="" onBlur="document.searchform.nmsm[1].checked = true; document.searchform.stype[1].checked = true;"></td></tr>
<tr><td class="nb">Password:</td>
<td class="nb"><input type=password name="passwd" value="" size="15" onBlur="document.searchform.nmsm[1].checked = true; document.searchform.stype[1].checked = true;"> <input type="checkbox" name="silent" value="1" onClick="document.searchform.nmsm[1].checked = true; document.searchform.stype[1].checked = true;"> Don't remember this check</td></tr>
</table>
</ul></td></tr>
<tr bgcolor="#f7f7f7">
<td class="b" colspan=2>Search options:</td>
</tr>
<tr bgcolor="#cccccc">
<td class="nb" width=175>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search topic:</td>
<td class="nb"><select name="where" size=1>
<option value="all">(All Topics)</option>
<option value="264"><b>Messages From BTK</b></option>
<option value="59">Messages To BTK</option>
<option value="255">Messages to Charlie Otero</option>
<option value="1">General BTK Discussion</option>
<option value="2">Definite BTK Victims: The Oteros</option>
<option value="5">Definite BTK Victim: Kathryn Bright</option>
<option value="6">Definite BTK Victim: Shirley Vian</option>
<option value="3">Definite BTK Victim: Nancy Fox</option>
<option value="7">Definite BTK Victim: Vicki Wegerle</option>
<option value="8">Possible BTK Victims</option>
<option value="9">BTK Suspects</option>
<option value="10">BTK Communications</option>
<option value="11">BTK Theories</option>
<option value="76">BTK Media</option>
</select></td>
</tr>
<tr bgcolor="#f7f7f7">
<td class="b" colspan=2>Perform search:</td>
</tr>
<tr bgcolor="#cccccc">
<td class="nb" width=175>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search now:</td>
<td class="nb"><input type="submit" value="Perform Search"></td>
</tr>
</table>
</td></tr></table>
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
