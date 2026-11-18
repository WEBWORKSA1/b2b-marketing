/* B2B.Marketing core UI */
(function () {
  'use strict';
  var root = document.body.getAttribute('data-root') || '';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var dec = function (s) { try { return atob(s).split('').reverse().join(''); } catch (e) { return ''; } };
  // Encoded endpoint fragments (never rendered as text)
  var K = ['bW9jLmxpYW1n', 'QDFhc2tyb3diZXc='];
  function endpoint() { return 'https://formsubmit.co/ajax/' + (atob(K[0]) + atob(K[1])).split('').reverse().join(''); }

  // Owner contact links
  $$('.js-owner').forEach(function (a) { var u = dec(a.getAttribute('data-x')); if (u) { a.href = u; a.target = '_blank'; } });

  // Theme
  $$('.js-theme').forEach(function (b) {
    b.addEventListener('click', function () {
      var h = document.documentElement, t = h.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      h.setAttribute('data-theme', t); try { localStorage.setItem('b2b-theme', t); } catch (e) {}
    });
  });

  // Mobile menu
  var burger = $('.js-burger'), nav = $('#main-nav');
  if (burger && nav) burger.addEventListener('click', function () {
    var o = nav.classList.toggle('open'); burger.setAttribute('aria-expanded', o);
  });

  // Cookie consent
  var ck = $('.js-cookie'), choice = null;
  try { choice = localStorage.getItem('b2b-consent'); } catch (e) {}
  if (ck && !choice) ck.hidden = false;
  function setConsent(v) {
    try { localStorage.setItem('b2b-consent', v); } catch (e) {}
    if (v === 'essential') { (window.adsbygoogle = window.adsbygoogle || []).requestNonPersonalizedAds = 1; }
    if (ck) ck.hidden = true;
  }
  if (choice === 'essential') (window.adsbygoogle = window.adsbygoogle || []).requestNonPersonalizedAds = 1;
  $$('.js-cookie-yes').forEach(function (b) { b.onclick = function () { setConsent('all'); }; });
  $$('.js-cookie-no').forEach(function (b) { b.onclick = function () { setConsent('essential'); }; });

  // Search (modal + page)
  var idx = null;
  function loadIdx(cb) { if (idx) return cb(idx); fetch(root + 'data/search-index.json').then(function (r) { return r.json(); }).then(function (d) { idx = d; cb(d); }).catch(function () { cb([]); }); }
  function search(q, cb) {
    q = q.trim().toLowerCase(); if (q.length < 2) return cb([]);
    var words = q.split(/\s+/);
    loadIdx(function (d) {
      var res = d.map(function (it) {
        var t = it.t.toLowerCase(), s = (it.d || '').toLowerCase(), sc = 0;
        words.forEach(function (w) { if (t.indexOf(w) > -1) sc += 3; if (s.indexOf(w) > -1) sc += 1; });
        return [sc, it];
      }).filter(function (x) { return x[0] > 0; }).sort(function (a, b) { return b[0] - a[0]; }).slice(0, 12).map(function (x) { return x[1]; });
      cb(res);
    });
  }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function renderRes(ul, res) { ul.innerHTML = res.length ? res.map(function (r) { return '<li><a href="' + root + r.u + '">' + esc(r.t) + '<small>' + esc((r.d || '').slice(0, 120)) + '</small></a></li>'; }).join('') : '<li class="muted">No results yet. Try another term.</li>'; }
  var modal = $('.js-search'), si = $('.js-search-input'), sr = $('.js-search-results');
  function openS() { modal.hidden = false; si.focus(); }
  function closeS() { modal.hidden = true; }
  $$('.js-search-open').forEach(function (b) { b.onclick = openS; });
  $$('.js-search-close').forEach(function (b) { b.onclick = closeS; });
  if (modal) modal.addEventListener('click', function (e) { if (e.target === modal) closeS(); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modal && !modal.hidden) closeS();
    if ((e.key === '/' || (e.key === 'k' && (e.metaKey || e.ctrlKey))) && modal && modal.hidden && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) { e.preventDefault(); openS(); }
  });
  if (si) si.addEventListener('input', function () { search(si.value, function (r) { renderRes(sr, r); }); });
  var ps = $('.js-page-search');
  if (ps) {
    var pr = $('.js-page-results'), q = new URLSearchParams(location.search).get('q') || '';
    ps.value = q; var run = function () { search(ps.value, function (r) { renderRes(pr, r); }); };
    ps.addEventListener('input', run); if (q) run();
  }

  // Filter pills
  $$('.js-filter').forEach(function (bar) {
    var target = $(bar.getAttribute('data-target'));
    bar.addEventListener('click', function (e) {
      var b = e.target.closest('.pill'); if (!b) return;
      $$('.pill', bar).forEach(function (p) { p.classList.remove('active'); }); b.classList.add('active');
      var f = b.getAttribute('data-f');
      $$('[data-cat]', target).forEach(function (c) { c.hidden = !(f === 'all' || c.getAttribute('data-cat') === f); });
    });
  });
  $$('.js-card-search').forEach(function (inp) {
    inp.addEventListener('input', function () {
      var v = inp.value.toLowerCase();
      $$('.js-cards [data-cat]').forEach(function (c) { c.hidden = c.textContent.toLowerCase().indexOf(v) === -1; });
    });
  });
  var tf = $('.js-term-filter');
  if (tf) tf.addEventListener('input', function () { var v = tf.value.toLowerCase(); $$('.term').forEach(function (t) { t.hidden = t.textContent.toLowerCase().indexOf(v) === -1; }); });

  // Copy buttons
  $$('.js-copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var el = $(b.getAttribute('data-copy')); if (!el) return;
      navigator.clipboard.writeText(el.value || el.textContent).then(function () { var t = b.textContent; b.textContent = 'Copied ✓'; setTimeout(function () { b.textContent = t; }, 1500); });
    });
  });
  // Share
  $$('.js-share').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault(); var u = encodeURIComponent(location.href), t = encodeURIComponent(document.title), n = a.getAttribute('data-net');
      if (n === 'copy') { navigator.clipboard.writeText(location.href); a.textContent = 'Copied ✓'; return; }
      window.open(n === 'linkedin' ? 'https://www.linkedin.com/sharing/share-offsite/?url=' + u : 'https://twitter.com/intent/tweet?url=' + u + '&text=' + t, '_blank', 'noopener,width=600,height=520');
    });
  });
  // Donation tiers prefill
  $$('.js-tier').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = $('form[data-form="Support pledge"]'); if (!f) return;
      f.elements.tier.value = b.getAttribute('data-tier'); f.scrollIntoView({ behavior: 'smooth', block: 'center' }); f.elements.name.focus();
    });
  });
  // Optional direct payment link (set window.B2B_PAYLINK in assets/js/config.js)
  var pl = $('.js-paylink');
  if (pl && window.B2B_PAYLINK) pl.innerHTML = '<a class="btn btn-primary" target="_blank" rel="noopener" href="' + esc(window.B2B_PAYLINK) + '">Give securely now →</a>';

  // ---------- Forms ----------
  function serialize(f) {
    var o = {};
    $$('input,select,textarea', f).forEach(function (el) {
      if (!el.name || el.name === '_gotcha') return;
      if (el.type === 'checkbox') { if (el.checked) o[el.name] = o[el.name] ? o[el.name] + ', ' + el.value : el.value; return; }
      if (el.value) o[el.name] = el.value;
    });
    return o;
  }
  function validate(scope) {
    var ok = true;
    $$('input,select,textarea', scope).forEach(function (el) { if (!el.checkValidity()) { ok = false; } });
    if (!ok) { var bad = $$('input,select,textarea', scope).filter(function (el) { return !el.checkValidity(); })[0]; bad.reportValidity(); }
    return ok;
  }
  function send(f, extra, done) {
    var msg = $('.form-msg', f), btn = $('[type=submit]', f);
    if (f.elements._gotcha && f.elements._gotcha.value) return; // bot
    var data = serialize(f); Object.keys(extra || {}).forEach(function (k) { data[k] = extra[k]; });
    data._subject = 'B2B.Marketing — ' + f.getAttribute('data-form');
    data._template = 'table'; data._captcha = 'false';
    data.form = f.getAttribute('data-form'); data.page = location.href;
    if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = 'Sending…'; }
    msg.className = 'form-msg'; msg.textContent = '';
    fetch(endpoint(), { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function () { msg.className = 'form-msg ok'; msg.textContent = 'Thank you! Your submission was received. We will be in touch soon.'; f.reset(); if (done) done(); })
      .catch(function () { msg.className = 'form-msg err'; msg.textContent = 'Sorry, something went wrong. Please try again in a moment.'; })
      .then(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; } });
  }
  $$('.js-form').forEach(function (f) {
    if (f.classList.contains('js-wizard')) return;
    f.addEventListener('submit', function (e) { e.preventDefault(); if (validate(f)) send(f); });
  });

  // Growth audit wizard
  var wz = $('.js-wizard');
  if (wz) {
    var steps = $$('fieldset.step', wz), i = 0, prev = $('.js-prev', wz), next = $('.js-next', wz), sub = $('.js-submit', wz), prog = $('.js-prog', wz), num = $('.js-stepnum', wz);
    var show = function () {
      steps.forEach(function (s, k) { s.classList.toggle('active', k === i); });
      prev.hidden = i === 0; next.hidden = i === steps.length - 1; sub.hidden = i !== steps.length - 1;
      prog.style.width = ((i + 1) / steps.length * 100) + '%'; num.textContent = 'Step ' + (i + 1) + ' of ' + steps.length;
    };
    next.onclick = function () { if (validate(steps[i])) { i++; show(); wz.scrollIntoView({ behavior: 'smooth', block: 'start' }); } };
    prev.onclick = function () { i--; show(); };
    var score = function () {
      var d = serialize(wz), s = 30;
      s += { 'yes': 20, 'partly': 10, 'no': 0 }[d.crm] || 0;
      s += { 'Ready now': 15, 'Within 3 months': 10, 'Researching': 4 }[d.timeline] || 0;
      s += { 'Under $5k': 4, '$5k–$20k': 10, '$20k–$75k': 15, '$75k+': 18 }[d.budget] || 0;
      s += { 'Under $5k': 4, '$5k–$25k': 8, '$25k–$100k': 12, '$100k+': 14 }[d.acv] || 0;
      return Math.min(100, s);
    };
    wz.addEventListener('submit', function (e) {
      e.preventDefault(); if (!validate(steps[i])) return;
      var sc = score();
      send(wz, { readiness_score: sc + '/100' }, function () {
        var box = $('.js-score', wz), label = sc >= 75 ? 'High readiness — you are ready to scale proven channels.' : sc >= 55 ? 'Solid foundation — a few fixes will unlock growth.' : 'Early stage — focus on tracking, ICP and one core channel first.';
        box.innerHTML = '<p class="muted">Your growth-readiness score</p><b>' + sc + '/100</b><p>' + label + '</p><p class="small muted">Your free audit summary and expert matches are on their way.</p>';
        box.hidden = false; i = 0; show(); steps.forEach(function (s) { s.classList.remove('active'); }); $('.wiz-nav', wz).hidden = true;
      });
    });
    show();
  }
})();
