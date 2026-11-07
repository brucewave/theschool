/* Thanh chuyển giữa các báo cáo — CHỈ hiện trên máy đã mở một lần bằng ?admin=<mã>.
   Người xem thường không thấy gì: tệp này không tải danh sách trang, không vẽ gì.
   Danh sách trang ở /rtabs.json; tên + màu mỗi tab lấy từ <meta name="tab-label">, <meta name="tab-color">
   của chính trang đó, nên không trang nào phải ghi tên thương hiệu khác.
   Trang có menu cố định bên trái: <meta name="tab-shift" content="112,85"> (dời sang phải 112px khi > 980px, 85px khi 761–980px).
   ?admin=off để tắt trên máy đó. Mã không nằm trong repo, ở đây chỉ có mã băm SHA-256. */
(function () {
  var H = 'd30f1b080e3715cc6c976884f38514ec562e4c20fefb95d3ae72720dafec9126', K = 'rt_admin';

  function ls(v) {
    try {
      if (v === undefined) return localStorage.getItem(K);
      if (v === null) localStorage.removeItem(K); else localStorage.setItem(K, v);
    } catch (e) {}
  }
  function meta(src, n) {
    var m = src.match(new RegExp('<meta name="' + n + '" content="([^"]*)"'));
    return m ? m[1] : '';
  }
  function norm(p) {
    p = p.replace(/[?#].*$/, '').replace(/\.html$/, '').replace(/\/index$/, '/');
    return p.length > 1 ? p.replace(/\/$/, '') : '/';
  }
  // Chỉ đọc phần <head> của trang kia (trang có thể rất nặng).
  function head(url) {
    return fetch(url).then(function (r) {
      if (!r.ok) return '';
      if (!r.body || !r.body.getReader) return r.text();
      var rd = r.body.getReader(), dec = new TextDecoder(), txt = '';
      function step() {
        return rd.read().then(function (x) {
          if (x.done) return txt;
          txt += dec.decode(x.value, { stream: true });
          if (txt.indexOf('</head>') >= 0) { rd.cancel(); return txt; }
          return step();
        });
      }
      return step();
    }).catch(function () { return ''; });
  }
  function style(shift) {
    var s = shift.split(',').map(Number), css =
      '.rtabs{position:fixed;top:12px;left:50%;transform:translateX(-50%);z-index:60;display:flex;gap:4px;padding:4px;max-width:calc(100vw - 24px);overflow-x:auto;scrollbar-width:none;border-radius:999px;background:rgba(255,255,255,.94);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);box-shadow:0 4px 18px rgba(16,24,40,.14);border:1px solid rgba(16,24,40,.08);font:600 13px/1 "Segoe UI",Arial,sans-serif}' +
      '.rtabs::-webkit-scrollbar{display:none}' +
      '.rtabs a{display:flex;align-items:center;gap:7px;padding:9px 15px;border-radius:999px;color:#475569;text-decoration:none;white-space:nowrap}' +
      '.rtabs a:hover{background:#f1f5f9}' +
      '.rtabs a i{width:8px;height:8px;border-radius:50%;flex:none;background:var(--c)}' +
      '.rtabs a.on{color:#fff;background:var(--c)}.rtabs a.on i{background:#fff}' +
      (s[0] ? '@media(min-width:981px){.rtabs{left:calc(50% + ' + s[0] + 'px)}}' : '') +
      (s[1] ? '@media(min-width:761px) and (max-width:980px){.rtabs{left:calc(50% + ' + s[1] + 'px)}}' : '') +
      '@media(max-width:760px){.rtabs{top:auto;bottom:14px}}@media print{.rtabs{display:none}}';
    var el = document.createElement('style');
    el.textContent = css;
    document.head.appendChild(el);
  }
  function show() {
    document.documentElement.classList.add('rt-admin');
    var me = document.documentElement.outerHTML.slice(0, 6000), here = norm(location.pathname);
    fetch('/rtabs.json', { cache: 'no-cache' }).then(function (r) { return r.json(); }).then(function (cfg) {
      return Promise.all((cfg.pages || []).map(function (p) {
        return (norm(p) === here ? Promise.resolve(me) : head(p)).then(function (src) {
          return { href: p, label: meta(src, 'tab-label'), color: meta(src, 'tab-color') || '#334155', on: norm(p) === here };
        });
      }));
    }).then(function (tabs) {
      tabs = tabs.filter(function (t) { return t.label; });
      if (tabs.length < 2) return;
      style(meta(me, 'tab-shift'));
      var nav = document.createElement('nav');
      nav.className = 'rtabs';
      nav.setAttribute('aria-label', 'Chọn báo cáo');
      tabs.forEach(function (t) {
        var a = document.createElement('a');
        a.href = t.href;
        a.style.setProperty('--c', t.color);
        if (t.on) { a.className = 'on'; a.setAttribute('aria-current', 'page'); }
        a.innerHTML = '<i></i>';
        a.appendChild(document.createTextNode(t.label));
        nav.appendChild(a);
      });
      document.body.appendChild(nav);
      var on = nav.querySelector('.on');
      if (on && on.scrollIntoView) on.scrollIntoView({ inline: 'center', block: 'nearest' });
    }).catch(function () {});
  }
  function hex(b) {
    return Array.prototype.map.call(new Uint8Array(b), function (x) { return ('0' + x.toString(16)).slice(-2); }).join('');
  }
  function start() {
    var u = new URL(location.href), q = u.searchParams.get('admin');
    if (q !== null) {
      u.searchParams.delete('admin');
      history.replaceState(null, '', u.pathname + u.search + u.hash);
      if (q === 'off') { ls(null); return; }
      if (window.crypto && crypto.subtle)
        crypto.subtle.digest('SHA-256', new TextEncoder().encode(q)).then(function (b) {
          if (hex(b) === H) { ls(H); show(); }
        });
      return;
    }
    if (ls() === H) show();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
