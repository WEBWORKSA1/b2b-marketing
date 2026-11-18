/* Renders auto-refreshed news + videos from data/*.json */
(function () {
  'use strict';
  var root = document.body.getAttribute('data-root') || '';
  var esc = function (s) { return String(s || '').replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var ago = function (d) { var t = Date.parse(d); if (!t) return ''; var h = Math.round((Date.now() - t) / 36e5); return h < 1 ? 'just now' : h < 48 ? h + 'h ago' : Math.round(h / 24) + 'd ago'; };
  var safeUrl = function (u) { return /^https?:\/\//i.test(u || '') ? u : '#'; };
  function stamp(d) { document.querySelectorAll('.js-updated').forEach(function (el) { el.textContent = d.updated ? 'Last updated: ' + new Date(d.updated).toLocaleString() : 'The feed refreshes automatically every few hours.'; }); }

  var newsBox = document.querySelector('.js-news');
  if (newsBox) fetch(root + 'data/news.json', { cache: 'no-cache' }).then(function (r) { return r.json(); }).then(function (d) {
    stamp(d); var items = d.items || [], lim = +newsBox.getAttribute('data-limit') || 12, src = 'all', q = '';
    var draw = function () {
      var list = items.filter(function (n) { return (src === 'all' || n.source === src) && (!q || (n.title + ' ' + n.summary).toLowerCase().indexOf(q) > -1); }).slice(0, lim);
      newsBox.innerHTML = list.length ? list.map(function (n) {
        return '<a class="card news-card" href="' + esc(safeUrl(n.link)) + '" target="_blank" rel="noopener nofollow"><span class="src">' + esc(n.source) + '</span><h3>' + esc(n.title) + '</h3><p>' + esc(n.summary) + '</p><span class="meta">' + ago(n.date) + ' · Read at source ↗</span></a>';
      }).join('') : '<p class="muted">Fresh headlines are being gathered. Please check back shortly.</p>';
    };
    var bar = document.querySelector('.js-news-sources');
    if (bar) {
      var names = []; items.forEach(function (n) { if (names.indexOf(n.source) < 0) names.push(n.source); });
      bar.innerHTML = '<button class="pill active" data-s="all">All sources</button>' + names.map(function (n) { return '<button class="pill" data-s="' + esc(n) + '">' + esc(n) + '</button>'; }).join('');
      bar.addEventListener('click', function (e) { var b = e.target.closest('.pill'); if (!b) return; bar.querySelectorAll('.pill').forEach(function (p) { p.classList.remove('active'); }); b.classList.add('active'); src = b.getAttribute('data-s'); draw(); });
    }
    var s = document.querySelector('.js-news-search'); if (s) s.addEventListener('input', function () { q = s.value.toLowerCase(); draw(); });
    draw();
  }).catch(function () { newsBox.innerHTML = '<p class="muted">News is temporarily unavailable.</p>'; });

  var vidBox = document.querySelector('.js-videos');
  if (vidBox) fetch(root + 'data/videos.json', { cache: 'no-cache' }).then(function (r) { return r.json(); }).then(function (d) {
    stamp(d); var lim = +vidBox.getAttribute('data-limit') || 6, items = (d.items || []).filter(function (v) { return /^[\w-]{11}$/.test(v.id); }).slice(0, lim);
    vidBox.innerHTML = items.length ? items.map(function (v) {
      return '<div class="card"><button class="video js-yt" data-id="' + v.id + '" aria-label="Play: ' + esc(v.title) + '"><img loading="lazy" src="https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg" alt=""></button><h3>' + esc(v.title) + '</h3><span class="meta">' + esc(v.channel) + ' · ' + ago(v.date) + '</span></div>';
    }).join('') : '<p class="muted">New videos are being gathered. Please check back shortly.</p>';
  }).catch(function () { vidBox.innerHTML = '<p class="muted">Videos are temporarily unavailable.</p>'; });

  document.addEventListener('click', function (e) {
    var b = e.target.closest('.js-yt'); if (!b) return;
    b.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + b.getAttribute('data-id') + '?autoplay=1&rel=0" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
  });
})();
