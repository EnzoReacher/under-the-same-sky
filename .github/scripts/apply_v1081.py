from pathlib import Path

index_path = Path("index.html")
readme_path = Path("README.md")
html = index_path.read_text(encoding="utf-8")

html = html.replace(
    '<meta name="app-version" content="10.8-final-polish">',
    '<meta name="app-version" content="10.8.1-epilogue-fix">',
    1,
)
html = html.replace(
    'data-build="10.8-final-polish"',
    'data-build="10.8.1-epilogue-fix"',
    1,
)

old_css = '''.gift-epilogue{
  position:absolute;
  inset:0;
  z-index:12;
  display:grid;
  place-content:center;
  justify-items:center;
  padding:42px 24px;
  overflow:hidden;'''
new_css = '''.gift-epilogue{
  position:fixed;
  inset:0;
  z-index:740;
  display:grid;
  place-content:center;
  justify-items:center;
  width:100%;
  min-height:100svh;
  min-height:100dvh;
  padding:
    max(30px,env(safe-area-inset-top))
    24px
    max(30px,env(safe-area-inset-bottom));
  overflow-x:hidden;
  overflow-y:auto;
  overscroll-behavior:contain;
  -webkit-overflow-scrolling:touch;'''
if old_css not in html:
    raise SystemExit("Expected epilogue CSS was not found")
html = html.replace(old_css, new_css, 1)

anchor = '''.cinematic-surprise.epilogue-open .cinema-content{
  opacity:0;'''
replacement = '''.cinematic-surprise.epilogue-open{
  overflow:hidden;
}
.cinematic-surprise.epilogue-open .cinema-content{
  opacity:0;'''
if anchor not in html:
    raise SystemExit("Expected epilogue-open CSS was not found")
html = html.replace(anchor, replacement, 1)

mobile_old = '''  .gift-epilogue{
    padding:30px 20px;
  }'''
mobile_new = '''  .gift-epilogue{
    place-content:safe center;
    padding:
      max(24px,env(safe-area-inset-top))
      20px
      max(24px,env(safe-area-inset-bottom));
  }'''
if mobile_old not in html:
    raise SystemExit("Expected mobile epilogue CSS was not found")
html = html.replace(mobile_old, mobile_new, 1)

open_old = '''  cinema.classList.add("show");
  cinema.setAttribute("aria-hidden","false");
  document.body.classList.add("locked");'''
open_new = '''  cinema.classList.add("show");
  cinema.setAttribute("aria-hidden","false");
  cinema.scrollTop=0;
  giftEpilogue.scrollTop=0;
  document.body.classList.add("locked");'''
if open_old not in html:
    raise SystemExit("Expected cinematic open code was not found")
html = html.replace(open_old, open_new, 1)

js_old = '''const lastLineButton=$("#lastLineButton");
const giftEpilogue=$("#giftEpilogue");
const epilogueBack=$("#epilogueBack");

lastLineButton?.addEventListener("click",()=>{
  const cinema=$("#cinematicSurprise");
  cinema.classList.add("epilogue-open");
  giftEpilogue.setAttribute("aria-hidden","false");

  if(!voice.paused){
    voice.pause();
  }

  if(!bgm.paused){
    fadeAudioTo(bgm,0,900,{pauseAtEnd:true});
    music.textContent="Bật nhạc";
  }
});

epilogueBack?.addEventListener("click",()=>{
  const cinema=$("#cinematicSurprise");
  cinema.classList.remove("epilogue-open");
  giftEpilogue.setAttribute("aria-hidden","true");
});'''
js_new = '''const lastLineButton=$("#lastLineButton");
const giftEpilogue=$("#giftEpilogue");
const epilogueBack=$("#epilogueBack");
let cinemaScrollBeforeEpilogue=0;

lastLineButton?.addEventListener("click",()=>{
  const cinema=$("#cinematicSurprise");
  cinemaScrollBeforeEpilogue=cinema.scrollTop;
  cinema.scrollTo({top:0,left:0,behavior:"auto"});
  giftEpilogue.scrollTop=0;
  cinema.classList.add("epilogue-open");
  giftEpilogue.setAttribute("aria-hidden","false");

  requestAnimationFrame(()=>{
    epilogueBack?.focus({preventScroll:true});
  });

  if(!voice.paused){
    voice.pause();
  }

  if(!bgm.paused){
    fadeAudioTo(bgm,0,900,{pauseAtEnd:true});
    music.textContent="Bật nhạc";
  }
});

epilogueBack?.addEventListener("click",()=>{
  const cinema=$("#cinematicSurprise");
  cinema.classList.remove("epilogue-open");
  giftEpilogue.setAttribute("aria-hidden","true");

  requestAnimationFrame(()=>{
    cinema.scrollTo({top:cinemaScrollBeforeEpilogue,left:0,behavior:"auto"});
    lastLineButton?.focus({preventScroll:true});
  });
});'''
if js_old not in html:
    raise SystemExit("Expected epilogue JavaScript was not found")
html = html.replace(js_old, js_new, 1)

close_old = '''  cinema.setAttribute("aria-hidden","true");
  document.body.classList.remove("locked");'''
close_new = '''  cinema.setAttribute("aria-hidden","true");
  cinema.scrollTop=0;
  giftEpilogue.scrollTop=0;
  document.body.classList.remove("locked");'''
if close_old not in html:
    raise SystemExit("Expected cinematic close code was not found")
html = html.replace(close_old, close_new, 1)

index_path.write_text(html, encoding="utf-8")

readme = readme_path.read_text(encoding="utf-8")
readme = readme.replace(
    "# Under the same sky — V10.8 Final Polish",
    "# Under the same sky — V10.8.1 Epilogue Fix",
    1,
)
if "## V10.8.1" not in readme:
    readme += '''\n\n## V10.8.1\n\n- Sửa màn “Đọc dòng cuối cùng” xuất hiện ngoài viewport khi cinematic đã cuộn xuống.\n- Epilogue bám trực tiếp theo viewport trên desktop và mobile.\n- Khi quay lại, cinematic trở về đúng vị trí tấm vé.\n'''
readme_path.write_text(readme, encoding="utf-8")
