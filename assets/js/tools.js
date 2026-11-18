/* B2B.Marketing calculators — all client-side */
(function () {
  'use strict';
  var form = document.querySelector('.js-calc'), out = document.querySelector('.js-out');
  if (!form || !out) return;
  var tool = form.getAttribute('data-tool');
  var n = function (id) { var v = parseFloat((form.elements[id] || {}).value); return isFinite(v) ? v : 0; };
  var s = function (id) { return (form.elements[id] || {}).value || ''; };
  var money = function (v) { return isFinite(v) ? '$' + Math.round(v).toLocaleString() : '—'; };
  var num = function (v, d) { return isFinite(v) ? (+v.toFixed(d == null ? 1 : d)).toLocaleString() : '—'; };
  var esc = function (x) { return String(x).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var kpi = function (arr) { return '<div class="kpi">' + arr.map(function (k) { return '<div><b>' + k[1] + '</b><span>' + k[0] + '</span></div>'; }).join('') + '</div>'; };
  var verdict = function (cls, t) { return '<p class="verdict v-' + cls + '">' + t + '</p>'; };

  var T = {
    'cac-payback-calculator': function () {
      var cac = n('spend') / Math.max(n('customers'), 1), gp = n('arpa') * n('margin') / 100, pb = gp > 0 ? cac / gp : Infinity;
      return kpi([['Customer acquisition cost', money(cac)], ['Monthly gross profit / customer', money(gp)], ['CAC payback', num(pb) + ' months']]) +
        (pb <= 12 ? verdict('good', 'Healthy: you recover acquisition cost within a year.') : pb <= 24 ? verdict('mid', 'Moderate: workable with strong retention, but watch cash flow.') : verdict('bad', 'Long payback: improve conversion, pricing or channel mix.'));
    },
    'ltv-cac-calculator': function () {
      var c = n('churn') / 100, ltv = c > 0 ? n('arpa') * n('margin') / 100 / c : Infinity, r = ltv / Math.max(n('cac'), 1);
      return kpi([['Customer lifetime value', money(ltv)], ['Average lifetime', c > 0 ? num(1 / c) + ' months' : '∞'], ['LTV : CAC', num(r) + ' : 1']]) +
        (r >= 3 && r <= 6 ? verdict('good', 'Healthy ratio, efficient growth.') : r > 6 ? verdict('mid', 'Very high: you may be under-investing in growth.') : r >= 1.5 ? verdict('mid', 'Below 3:1, so tighten acquisition costs or improve retention.') : verdict('bad', 'Unprofitable acquisition. Fix churn or CAC before scaling.'));
    },
    'marketing-roi-calculator': function () {
      var gp = n('revenue') * n('margin') / 100, roi = (gp - n('cost')) / Math.max(n('cost'), 1) * 100;
      return kpi([['Gross profit generated', money(gp)], ['Net return', money(gp - n('cost'))], ['Marketing ROI', num(roi, 0) + '%']]) +
        (roi > 100 ? verdict('good', 'Strong return. Consider scaling this program.') : roi > 0 ? verdict('mid', 'Positive but thin. Optimise before scaling.') : verdict('bad', 'Negative return on a gross-profit basis.'));
    },
    'pipeline-reverse-planner': function () {
      var deals = n('target') / Math.max(n('deal'), 1), opps = deals / Math.max(n('win') / 100, .0001), sqls = opps / Math.max(n('sqlopp') / 100, .0001), mqls = sqls / Math.max(n('mqlsql') / 100, .0001), leads = mqls / Math.max(n('leadmql') / 100, .0001);
      var rows = [['Leads', leads], ['MQLs', mqls], ['SQLs', sqls], ['Opportunities', opps], ['Closed-won deals', deals]], mx = leads || 1;
      return kpi([['Pipeline needed', money(opps * n('deal'))], ['Leads per month', num(leads / 12, 0)], ['Opportunities per month', num(opps / 12, 1)]]) +
        '<table><thead><tr><th>Stage</th><th>Annual</th><th>Monthly</th><th></th></tr></thead><tbody>' + rows.map(function (r) { return '<tr><td>' + r[0] + '</td><td>' + num(Math.ceil(r[1]), 0) + '</td><td>' + num(r[1] / 12, 1) + '</td><td style="width:35%"><div class="bar" style="width:' + Math.max(2, r[1] / mx * 100) + '%"></div></td></tr>'; }).join('') + '</tbody></table>';
    },
    'lead-scoring-builder': function () {
      var fit = { cx: 20, dir: 15, mgr: 8, ic: 3, student: -15 }[s('title')] + { 'in': 15, near: 7, out: -10 }[s('size')] + { work: 5, personal: -10, comp: -100 }[s('email')];
      var eng = (s('pricing') === 'yes' ? 10 : 0) + (s('demo') === 'yes' ? 40 : 0) + (s('webinar') === 'yes' ? 10 : 0) + Math.min(15, n('clicks') * 3);
      if (n('days') > 30) eng = Math.round(eng / 2);
      var total = fit + eng, th = n('threshold'), grade = fit >= 25 ? (eng >= 30 ? 'A1' : 'A2') : fit >= 10 ? (eng >= 30 ? 'B1' : 'B2') : 'C';
      return kpi([['Fit score', fit], ['Engagement score', eng], ['Total / grade', total + ' · ' + grade]]) +
        (total >= th ? verdict('good', 'MQL: route to sales now.') : total >= th * .6 ? verdict('mid', 'Nurture: close to threshold, so keep engaging.') : verdict('bad', 'Not ready: keep in long-term nurture or disqualify.'));
    },
    'marketing-budget-allocator': function () {
      var splits = { early: [['People & agencies', 45], ['Programs: demand capture', 15], ['Programs: demand creation & brand', 15], ['Technology & data', 10], ['Test reserve', 15]], growth: [['People & agencies', 35], ['Programs: demand capture', 22], ['Programs: demand creation & brand', 23], ['Technology & data', 10], ['Test reserve', 10]], mature: [['People & agencies', 33], ['Programs: demand capture', 17], ['Programs: demand creation & brand', 28], ['Technology & data', 12], ['Test reserve', 10]] }[s('stage')];
      var b = n('budget');
      return kpi([['Annual budget', money(b)], ['Monthly', money(b / 12)], ['Quarterly', money(b / 4)]]) + '<table><thead><tr><th>Line</th><th>%</th><th>Annual</th><th></th></tr></thead><tbody>' + splits.map(function (r) { return '<tr><td>' + r[0] + '</td><td>' + r[1] + '%</td><td>' + money(b * r[1] / 100) + '</td><td style="width:30%"><div class="bar" style="width:' + r[1] * 2 + '%"></div></td></tr>'; }).join('') + '</tbody></table>';
    },
    'utm-builder': function () {
      var clean = function (v) { return v.trim().toLowerCase().replace(/\s+/g, '-'); }, base = s('url').trim();
      try { var u = new URL(base); } catch (e) { return verdict('bad', 'Enter a full URL starting with https://'); }
      [['utm_source', 'source'], ['utm_medium', 'medium'], ['utm_campaign', 'campaign'], ['utm_content', 'content'], ['utm_term', 'term']].forEach(function (p) { var v = clean(s(p[1])); if (v) u.searchParams.set(p[0], v); });
      var miss = ['source', 'medium', 'campaign'].filter(function (k) { return !s(k).trim(); });
      return '<label>Your tagged URL<div class="copyline"><input id="utm-out" readonly value="' + esc(u.toString()) + '"><button type="button" class="btn btn-primary js-copy-utm">Copy</button></div></label>' +
        (miss.length ? verdict('mid', 'Missing required: ' + miss.join(', ')) : verdict('good', 'All required parameters set, values normalised to lowercase.'));
    },
    'abm-account-tiering': function () {
      var sc = (n('fit') * .5 + n('intent') * .3 + n('engage') * .2) * 10, acv = n('acv'), tier = sc >= 75 && acv >= 50000 ? 'Tier 1 · 1:1' : sc >= 55 ? 'Tier 2 · 1:few' : 'Tier 3 · 1:many';
      var play = { 'Tier 1 · 1:1': 'Custom research, executive outreach, bespoke content and events.', 'Tier 2 · 1:few': 'Cluster by industry or use case; tailored ads, content and SDR sequences.', 'Tier 3 · 1:many': 'Programmatic ads and automated nurture with light personalisation.' }[tier];
      return kpi([['Account score', num(sc, 0) + '/100'], ['Potential ACV', money(acv)], ['Recommended tier', tier]]) + verdict(sc >= 75 ? 'good' : sc >= 55 ? 'mid' : 'bad', play);
    },
    'email-subject-line-checker': function () {
      var t = s('subject'), L = t.length, sc = 100, notes = [];
      var spam = ['free', 'guarantee', 'act now', 'urgent', 'winner', '100%', 'risk-free', 'click here', 'buy now', 'limited time', 'cash', '$$$', 'no cost', 'amazing'];
      var hits = spam.filter(function (w) { return t.toLowerCase().indexOf(w) > -1; });
      if (L < 20) { sc -= 15; notes.push('Quite short. Add specificity.'); } else if (L > 60) { sc -= 20; notes.push('Over 60 characters may be cut off on mobile.'); } else notes.push('Good length (' + L + ' characters).');
      if (hits.length) { sc -= hits.length * 12; notes.push('Spam-trigger words: ' + hits.join(', ')); }
      if (/[A-Z]{4,}/.test(t)) { sc -= 12; notes.push('Avoid ALL-CAPS words.'); }
      if (/[!?]{2,}|!/.test(t)) { sc -= 8; notes.push('Exclamation marks can look promotional.'); }
      if (/\{\{.+\}\}|\[.+\]/.test(t)) { sc += 5; notes.push('Personalisation token found ✓'); }
      if (/\d/.test(t)) { sc += 3; notes.push('Numbers add specificity ✓'); }
      if (/\?$/.test(t.trim())) notes.push('Question format can lift curiosity ✓');
      sc = Math.max(0, Math.min(100, sc));
      return kpi([['Score', sc + '/100'], ['Characters', L], ['Words', t.trim() ? t.trim().split(/\s+/).length : 0]]) + '<ul>' + notes.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>';
    },
    'webinar-roi-calculator': function () {
      var att = n('reg') * n('attend') / 100, opps = att * n('opp') / 100, pipe = opps * n('deal'), rev = pipe * n('win') / 100, roi = (rev - n('cost')) / Math.max(n('cost'), 1) * 100;
      return kpi([['Attendees', num(att, 0)], ['Opportunities', num(opps, 1)], ['Pipeline created', money(pipe)], ['Expected revenue', money(rev)], ['Cost per opportunity', money(n('cost') / Math.max(opps, .0001))], ['ROI', num(roi, 0) + '%']]) +
        (roi > 100 ? verdict('good', 'Strong expected return.') : roi > 0 ? verdict('mid', 'Positive, but improve attendance or follow-up conversion.') : verdict('bad', 'Expected loss. Rethink targeting, topic or follow-up.'));
    }
  };
  function run() { try { out.innerHTML = T[tool] ? T[tool]() : ''; } catch (e) { out.innerHTML = '<p class="muted">Check your inputs.</p>'; } }
  form.addEventListener('input', run); form.addEventListener('submit', function (e) { e.preventDefault(); run(); });
  out.addEventListener('click', function (e) { if (e.target.classList.contains('js-copy-utm')) { navigator.clipboard.writeText(document.getElementById('utm-out').value); e.target.textContent = 'Copied ✓'; } });
  run();
})();
