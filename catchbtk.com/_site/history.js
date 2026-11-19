/* catchBTK.com reconstruction: page-history bar.
   Loaded by every page; reads window.CBTK (written by _site/data/<page>.js).
   - Shows the version slider only when the page changed over time (versions whose content differs).
   - "Keep this date when following links" carries ?asof=<timestamp> to other pages so the whole site can be browsed as of a date. */
(function () {
  'use strict';
  var P = window.CBTK;
  var me = document.currentScript;
  if (!P || !me) return;
  var cur = parseInt(me.getAttribute('data-cur'), 10) || 0;
  var V = P.versions, N = V.length;
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  function d(ts) { return MONTHS[+ts.slice(4, 6) - 1] + ' ' + (+ts.slice(6, 8)) + ', ' + ts.slice(0, 4); }
  function dt(ts) { return d(ts) + ' ' + ts.slice(8, 10) + ':' + ts.slice(10, 12) + ' UTC'; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }

  /* ---- time travel (?asof=) ---- */
  var qs = new URLSearchParams(location.search);
  var asof = qs.get('asof') || '';
  if (!/^\d{14}$/.test(asof)) asof = '';
  function pick(ts) { var k = 0; for (var i = 0; i < N; i++) { if (V[i].t <= ts) k = i; } return k; }
  if (asof) {
    var want = pick(asof);
    if (want !== cur) { location.replace((want === N - 1 ? P.page : V[want].f) + '?asof=' + asof); return; }
  }
  var base = document.baseURI.split('#')[0].split('?')[0].replace(/[^\/]*$/, '');   // site root folder URL
  var hasBase = !!document.querySelector('base');

  /* in history copies <base> points at the site root, so same-page "#anchor" links need a nudge */
  if (hasBase) {
    document.addEventListener('click', function (e) {
      var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
      if (!a) return;
      var h = a.getAttribute('href');
      if (h && h.charAt(0) === '#') { e.preventDefault(); if (h.length > 1) location.hash = h; }
    }, false);
  }
  /* carry the chosen date to other pages of the reconstruction */
  document.addEventListener('click', function (e) {
    if (!asof) return;
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a || a.getAttribute('href').charAt(0) === '#') return;
    var u; try { u = new URL(a.href); } catch (x) { return; }
    if (u.href.indexOf(base) !== 0 || !/\.html?$/i.test(u.pathname)) return;
    if (/\/(sitemap|missing)\.html$/i.test(u.pathname)) return;
    u.searchParams.set('asof', asof);
    a.href = u.href;
  }, true);

  function setOpen(v) { try { sessionStorage.setItem('cbtk-open', v ? '1' : '0'); } catch (x) { } }
  function getOpen() { try { return sessionStorage.getItem('cbtk-open') === '1'; } catch (x) { return false; } }

  /* ---- UI ---- */
  var host = document.createElement('div');
  host.id = 'cbtk-history-host';
  var sr = host.attachShadow ? host.attachShadow({ mode: 'open' }) : host;
  var v = V[cur];
  var single = N === 1;
  var css = ':host{all:initial}*{box-sizing:border-box}' +
    '.wrap{position:fixed;left:0;right:0;bottom:0;z-index:2147483647;font:13px/1.4 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:#1d1b18;pointer-events:none}' +
    '.pill{pointer-events:auto;position:absolute;right:12px;bottom:12px;background:#1f2a33;color:#fff;border:1px solid #0b1116;border-radius:999px;padding:6px 13px;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,.35);font:600 12px/1.2 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;max-width:92vw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
    '.pill:hover{background:#2d3d4a}.pill small{font-weight:400;opacity:.8;margin-left:6px}' +
    '.panel{pointer-events:auto;display:none;background:#fffdf8;border-top:3px solid #8a3b12;box-shadow:0 -4px 16px rgba(0,0,0,.3);padding:10px 16px 12px}' +
    '.open .panel{display:block}.open .pill{display:none}' +
    '.row{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:3px 0}' +
    '.ttl{font-weight:700}.mut{color:#6a655b}.right{margin-left:auto}' +
    'button{font:inherit;padding:3px 10px;border:1px solid #bdb5a3;border-radius:6px;background:#efe9db;color:#1d1b18;cursor:pointer}' +
    'button:hover{border-color:#8a3b12}button[disabled]{opacity:.4;cursor:default}' +
    'input[type=range]{flex:1 1 320px;min-width:180px;accent-color:#8a3b12}' +
    'a{color:#1f5f86}label{cursor:pointer;display:inline-flex;gap:5px;align-items:center}' +
    '.sum{font-weight:600}.add{color:#2f6b3a}.del{color:#9a2b2b}' +
    'details{margin-top:3px}summary{cursor:pointer;color:#6a655b}' +
    'ul.ch{margin:4px 0 2px 18px;padding:0;max-height:120px;overflow:auto}ul.ch li{margin:1px 0}' +
    '.note{background:#fff1b8;border:1px solid #d9c46a;border-radius:5px;padding:2px 8px}' +
    '@media print{.wrap{display:none}}';

  function summary(i) {
    var x = V[i];
    if (i === 0) return '<span class="sum">First capture of this page</span>';
    if (!x.a && !x.d) return '<span class="sum">Wording unchanged; layout, images or links changed</span>';
    return '<span class="sum">vs. previous version: <span class="add">+' + x.a + ' words</span> / <span class="del">&minus;' + x.d + ' words</span></span>';
  }
  function range(i) {
    var x = V[i];
    var span = x.t.slice(0, 8) === x.e.slice(0, 8) ? d(x.t) : d(x.t) + ' &ndash; ' + d(x.e);
    return span + (x.n > 1 ? ' <span class="mut">(' + x.n + ' captures, identical)</span>' : '');
  }
  function changes(i) {
    var x = V[i]; if (i === 0 || (!(x.sa && x.sa.length) && !(x.sd && x.sd.length))) return '';
    var h = '<details><summary>What changed since the previous version</summary><ul class="ch">';
    (x.sa || []).forEach(function (s) { h += '<li><span class="add">+</span> ' + esc(s) + '</li>'; });
    (x.sd || []).forEach(function (s) { h += '<li><span class="del">&minus;</span> ' + esc(s) + '</li>'; });
    return h + '</ul></details>';
  }
  var wb = 'https://web.archive.org/web/' + v.t + '/http://www.catchbtk.com/' + (P.page === 'index.html' ? '' : P.page);
  var html = '<div class="wrap" id="w"><div class="pill" id="pill" title="Show this page’s history">' +
    (single ? '\u{1F4C4} Archived copy &middot; ' + d(v.t) + '<small>only version</small>'
      : '\u{1F558} History &middot; version <b id="pv">' + (cur + 1) + '</b> of ' + N + ' &middot; ' + d(v.t) + (cur === N - 1 ? '<small>latest</small>' : '')) +
    '</div><div class="panel"><div class="row"><span class="ttl">' + esc(P.page) + '</span><span class="mut">' + esc(P.title || '') + '</span>' +
    '<span class="right"><button id="x" title="Hide">✕ Close</button></span></div>';
  if (single) {
    html += '<div class="row">Captured ' + range(0) + '. This page never changed in the saved snapshots, so there are no older versions to browse.</div>';
  } else {
    html += '<div class="row"><button id="prev" title="Older version">◀</button>' +
      '<input id="sl" type="range" min="0" max="' + (N - 1) + '" step="1" value="' + cur + '" aria-label="Page version">' +
      '<button id="next" title="Newer version">▶</button><button id="latest" title="Most recent version">Latest ⏭</button></div>' +
      '<div class="row"><span class="mut">' + d(V[0].t) + '</span><span class="mut right">' + d(V[N - 1].t) + '</span></div>' +
      '<div class="row"><b>Version <span id="pv2">' + (cur + 1) + '</span> of ' + N + '</b><span id="rng">' + range(cur) + '</span></div>' +
      '<div class="row" id="sm">' + summary(cur) + '</div><div id="chg">' + changes(cur) + '</div>';
  }
  html += '<div class="row"><label title="When on, links to other pages open them as they were on this date"><input type="checkbox" id="fol"' + (asof ? ' checked' : '') + '> Keep this date when I follow links</label>' +
    '<span id="asnote"></span><span class="right"><a href="sitemap.html">Site map</a> &middot; <a href="' + esc(P.archive) + '">Forum post archive</a> &middot; <a href="' + esc(wb) + '" target="_blank" rel="noopener">Original on Wayback ↗</a></span></div></div></div>';
  sr.innerHTML = '<style>' + css + '</style>' + html;
  document.body.appendChild(host);

  var $ = function (id) { return sr.getElementById ? sr.getElementById(id) : sr.querySelector('#' + id); };
  var wrap = $('w');
  function open(o) {
    wrap.className = 'wrap' + (o ? ' open' : '');
    setOpen(o);
    document.documentElement.style.scrollPaddingBottom = o ? '220px' : '';
    var pad = o ? Math.ceil($('w').querySelector('.panel').offsetHeight) + 'px' : '';
    document.body.style.paddingBottom = pad;
  }
  $('pill').addEventListener('click', function () { open(true); });
  $('x').addEventListener('click', function () { open(false); });
  var isPopup = false; try { isPopup = !!window.opener && window.innerWidth < 800; } catch (x) { }
  open((getOpen() && !isPopup) || location.hash === '#history');

  if (asof && asof < V[0].t) {
    $('asnote').innerHTML = '<span class="note">Not yet captured at ' + d(asof) + ' &ndash; showing the earliest capture.</span>';
  }

  function go(i, follow) {
    var tgt = (i === N - 1) ? P.page : V[i].f;
    if (follow) tgt += '?asof=' + V[i].t;
    setOpen(true);
    location.href = tgt;
  }
  var fol = $('fol');
  fol.addEventListener('change', function () {
    var i = single ? 0 : +$('sl').value;
    if (fol.checked) { var u = new URL(location.href); u.searchParams.set('asof', V[i].t); location.replace(u.href); }
    else { var u2 = new URL(location.href); u2.searchParams.delete('asof'); location.replace(u2.href); }
  });
  if (!single) {
    var sl = $('sl');
    function preview() {
      var i = +sl.value;
      $('pv2').textContent = i + 1; $('rng').innerHTML = range(i); $('sm').innerHTML = summary(i); $('chg').innerHTML = changes(i);
      $('prev').disabled = i === 0; $('next').disabled = i === N - 1;
    }
    sl.addEventListener('input', preview);
    sl.addEventListener('change', function () { var i = +sl.value; if (i !== cur) go(i, !!asof || fol.checked); });
    $('prev').addEventListener('click', function () { if (cur > 0) go(cur - 1, !!asof); });
    $('next').addEventListener('click', function () { if (cur < N - 1) go(cur + 1, !!asof); });
    $('latest').addEventListener('click', function () { setOpen(true); location.href = P.page; });
    $('prev').disabled = cur === 0; $('next').disabled = cur === N - 1;
    document.addEventListener('keydown', function (e) {
      if (!(e.altKey && (e.key === 'ArrowLeft' || e.key === 'ArrowRight'))) return;   // Alt+Left/Right: older / newer version
      if (e.key === 'ArrowLeft' && cur > 0) go(cur - 1, !!asof);
      if (e.key === 'ArrowRight' && cur < N - 1) go(cur + 1, !!asof);
    });
  }
})();
