from pathlib import Path
import re

root = Path('.')
index = root / 'index.html'
html = index.read_text(encoding='utf-8')

if 'content="10.8-final-polish"' in html:
    print('V10.8 already applied.')
    raise SystemExit(0)

old_meta = '<meta name="description" content="A private birthday gift sent from Quy Nhơn to Gothenburg."><meta name="app-version" content="10.7-emotional-finale">'
new_meta = '''<meta name="description" content="Một món quà nhỏ đi từ Quy Nhơn đến Gothenburg, dành riêng cho em.">
<meta name="robots" content="noindex,nofollow,noarchive,nosnippet">
<meta name="app-version" content="10.8-final-polish">
<link rel="canonical" href="https://enzoreacher.github.io/under-the-same-sky/">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<meta property="og:locale" content="vi_VN">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Under the same sky">
<meta property="og:title" content="Under the same sky — A little place for us">
<meta property="og:description" content="Một món quà nhỏ đi từ Quy Nhơn đến Gothenburg, dành riêng cho em.">
<meta property="og:url" content="https://enzoreacher.github.io/under-the-same-sky/">
<meta property="og:image" content="https://enzoreacher.github.io/under-the-same-sky/assets/our-shadow.jpg">
<meta property="og:image:width" content="1516">
<meta property="og:image:height" content="1469">
<meta property="og:image:alt" content="Under the same sky — Quy Nhơn đến Gothenburg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Under the same sky — A little place for us">
<meta name="twitter:description" content="Một món quà nhỏ đi từ Quy Nhơn đến Gothenburg, dành riêng cho em.">
<meta name="twitter:image" content="https://enzoreacher.github.io/under-the-same-sky/assets/our-shadow.jpg">'''
if old_meta not in html:
    raise RuntimeError('Không tìm thấy meta V10.7 để cập nhật.')
html = html.replace(old_meta, new_meta, 1)
html = html.replace('data-build="10.7-emotional-finale"', 'data-build="10.8-final-polish"', 1)

left_roses = '''background-image:
    radial-gradient(circle at 72% 14%,#8d173d 0 5%,#d64c77 6% 10%,#f3a0b8 11% 14%,transparent 15%),
    radial-gradient(circle at 55% 47%,#8d173d 0 4%,#d64c77 5% 9%,#f3a0b8 10% 13%,transparent 14%),
    radial-gradient(circle at 40% 70%,#8d173d 0 3.5%,#d64c77 4.5% 8%,#f3a0b8 9% 12%,transparent 13%),
    linear-gradient(68deg,transparent 47%,rgba(68,91,55,.78) 48% 49.5%,transparent 50.5%);'''
right_roses = '''background-image:
    radial-gradient(circle at 28% 14%,#8d173d 0 5%,#d64c77 6% 10%,#f3a0b8 11% 14%,transparent 15%),
    radial-gradient(circle at 45% 47%,#8d173d 0 4%,#d64c77 5% 9%,#f3a0b8 10% 13%,transparent 14%),
    radial-gradient(circle at 60% 70%,#8d173d 0 3.5%,#d64c77 4.5% 8%,#f3a0b8 9% 12%,transparent 13%),
    linear-gradient(-68deg,transparent 47%,rgba(68,91,55,.78) 48% 49.5%,transparent 50.5%);'''
html = html.replace('background-image:url("assets/real-rose-left.webp");', left_roses, 1)
html = html.replace('background-image:url("assets/real-rose-right.webp");', right_roses, 1)

html = html.replace('<body class="locked welcome-active">', '<body class="locked welcome-active">\n<a class="skip-link" href="#mainContent">Đi thẳng tới nội dung chính</a>', 1)
html = html.replace('<main>', '<main id="mainContent" tabindex="-1">', 1)
html = html.replace('id="voiceStatus">', 'id="voiceStatus" role="status" aria-live="polite" aria-atomic="true">', 1)
html = re.sub(r'<button(?![^>]*\btype=)', '<button type="button"', html)
html = html.replace('<button type="button" type="submit"', '<button type="submit"')

extra_css = '''
/* V10.8 — Final polish */
.skip-link{position:fixed;left:18px;top:12px;z-index:9999;padding:11px 15px;border-radius:999px;color:#fff;background:#8f173f;box-shadow:0 10px 26px rgba(74,16,38,.26);transform:translateY(-160%);transition:transform .2s ease}
.skip-link:focus{transform:translateY(0)}
button{min-height:44px;-webkit-tap-highlight-color:transparent}
button:disabled{cursor:not-allowed;opacity:.55}
img{max-width:100%}
@media(max-width:820px){.rose-photo{opacity:.22;filter:none}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.rose-photo{animation:none!important}}
'''
html = html.replace('</style>', extra_css + '\n</style>', 1)

old_listener = '''document.addEventListener("keydown",event=>{
  if(event.key==="Escape" && modal.classList.contains("show")) closeMessageModal();
});'''
new_listener = '''document.addEventListener("keydown",event=>{
  if(!modal.classList.contains("show")) return;
  if(event.key==="Escape"){
    event.preventDefault();
    closeMessageModal();
    return;
  }
  if(event.key==="Tab"){
    const focusable=[...modal.querySelectorAll('button:not([disabled]),a[href],input:not([disabled]),[tabindex]:not([tabindex="-1"])')]
      .filter(element=>!element.hidden && element.getClientRects().length);
    if(!focusable.length) return;
    const first=focusable[0];
    const last=focusable[focusable.length-1];
    if(event.shiftKey && document.activeElement===first){event.preventDefault();last.focus();}
    else if(!event.shiftKey && document.activeElement===last){event.preventDefault();first.focus();}
  }
});'''
if old_listener not in html:
    raise RuntimeError('Không tìm thấy modal listener để nâng accessibility.')
html = html.replace(old_listener, new_listener, 1)

required = ['10.8-final-polish', 'og:title', 'class="skip-link"', 'id="mainContent"', 'role="status" aria-live="polite"']
for token in required:
    if token not in html:
        raise RuntimeError(f'Thiếu token sau khi build: {token}')
if 'assets/real-rose-left.webp' in html or 'assets/real-rose-right.webp' in html:
    raise RuntimeError('Vẫn còn đường dẫn hoa hồng bị thiếu.')

index.write_text(html, encoding='utf-8')

favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#e86583"/><stop offset="1" stop-color="#9f143c"/></linearGradient></defs>
<rect width="64" height="64" rx="18" fill="#fff5f8"/>
<path d="M32 52S10 39.5 10 23.5C10 14.5 21 10 27 18c2.5-4 7.5-7 13-5.5 8 2.2 12 11 8.5 18.5C44 41 32 52 32 52Z" fill="url(#g)"/>
<path d="M23 26c2-5 8-7 12-2" fill="none" stroke="#ffdce7" stroke-width="3" stroke-linecap="round" opacity=".9"/>
</svg>'''
(root / 'assets' / 'favicon.svg').write_text(favicon, encoding='utf-8')
(root / 'robots.txt').write_text('User-agent: *\nDisallow: /\n', encoding='utf-8')
(root / '.nojekyll').write_text('', encoding='utf-8')

readme = '''# Under the same sky — V10.8 Final Polish

Một món quà sinh nhật riêng đi từ Quy Nhơn đến Gothenburg.

## V10.8

- Sửa hai tài nguyên hoa hồng bị thiếu bằng CSS nhẹ.
- Thêm favicon riêng.
- Thêm preview chia sẻ bằng ảnh bóng hai đứa hiện có.
- Thêm Open Graph, Twitter Card, canonical URL và mô tả chia sẻ.
- Thêm `robots.txt` và `noindex` để hạn chế công cụ tìm kiếm lập chỉ mục.
- Thêm skip link, trạng thái voice có `aria-live`, vùng bấm tối thiểu 44px và focus trap cho modal.
- Giữ nguyên gallery, game, lá thư và đoạn kết của V10.7.

## Audio bổ sung sau

Đặt hai file vào `assets/`:

- `our-song.mp3`
- `message-for-duyen.mp3`

## Deploy

GitHub Pages: branch `main`, folder `/(root)`.

`https://enzoreacher.github.io/under-the-same-sky/`
'''
(root / 'README.md').write_text(readme, encoding='utf-8')
print('V10.8 patch applied successfully.')
