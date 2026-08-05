from pathlib import Path

INDEX = Path("index.html")
README = Path("README.md")
PUBLIC_URL = "https://under-samma-himmel.hoangnt2000.chatgpt.site/"
PUBLIC_IMAGE = f"{PUBLIC_URL}assets/our-shadow.jpg"
VERSION = "10.9-birthday-polish"

html = INDEX.read_text(encoding="utf-8")

if f'content="{VERSION}"' in html and f'data-build="{VERSION}"' in html:
    print("V10.9 already applied.")
    raise SystemExit(0)


def must_replace(old: str, new: str, label: str) -> None:
    global html
    if old not in html:
        raise SystemExit(f"Missing expected content: {label}")
    html = html.replace(old, new, 1)


def soft_replace(old: str, new: str, label: str) -> None:
    global html
    if old in html:
        html = html.replace(old, new, 1)
        print(f"Updated: {label}")
    else:
        print(f"Skipped absent optional text: {label}")


# Build metadata and public sharing URLs.
html = html.replace(
    '<meta name="app-version" content="10.8.2-hero-sakura-rain">',
    f'<meta name="app-version" content="{VERSION}">',
    1,
)
html = html.replace(
    'data-build="10.8.2-hero-sakura-rain"',
    f'data-build="{VERSION}"',
    1,
)
for old, new in (
    ('<link rel="canonical" href="https://enzoreacher.github.io/under-the-same-sky/">', f'<link rel="canonical" href="{PUBLIC_URL}">'),
    ('<meta property="og:url" content="https://enzoreacher.github.io/under-the-same-sky/">', f'<meta property="og:url" content="{PUBLIC_URL}">'),
    ('<meta property="og:image" content="https://enzoreacher.github.io/under-the-same-sky/assets/our-shadow.jpg">', f'<meta property="og:image" content="{PUBLIC_IMAGE}">'),
    ('<meta name="twitter:image" content="https://enzoreacher.github.io/under-the-same-sky/assets/our-shadow.jpg">', f'<meta name="twitter:image" content="{PUBLIC_IMAGE}">'),
):
    if old in html:
        html = html.replace(old, new, 1)

# Birthday-day presentation in the hero.
css_anchor = '''.hero-line{font-family:"Playfair Display",serif;font-style:italic;color:var(--rose);margin:12px 0 0}
.hero-sub{max-width:580px;margin:28px 0;color:var(--muted);font-size:clamp(1rem,1.5vw,1.18rem);line-height:1.75}'''
css_replacement = '''.hero-line{font-family:"Playfair Display",serif;font-style:italic;color:var(--rose);margin:12px 0 0}
.hero-sub{max-width:580px;margin:28px 0;color:var(--muted);font-size:clamp(1rem,1.5vw,1.18rem);line-height:1.75}
.birthday-now-message{
  max-width:560px;
  margin:24px 0 0;
  padding:18px 22px;
  border:1px solid rgba(198,29,59,.16);
  border-radius:22px;
  color:#7c1835;
  background:rgba(255,255,255,.76);
  box-shadow:0 18px 45px rgba(123,30,58,.10);
  font-family:"Playfair Display",serif;
  font-size:clamp(1.12rem,2.4vw,1.45rem);
  line-height:1.55;
  backdrop-filter:blur(12px);
}
.birthday-now-message strong{display:block;color:var(--rose);font-size:1.12em}
.birthday-now-message[hidden]{display:none!important}'''
must_replace(css_anchor, css_replacement, "hero birthday CSS anchor")

hero_copy_old = '''    <p class="hero-line">Năm nay anh không thể đứng cạnh em, nên anh gom những điều muốn nói vào đây.</p>
    <p class="hero-sub">Không phải món quà lớn. Chỉ là một nơi nhỏ anh làm riêng cho em, để khoảng cách hôm nay bớt xa đi một chút.</p>
    <div class="countdown">
      <div><strong id="dd">00</strong><small>days</small></div><div><strong id="hh">00</strong><small>hours</small></div>
      <div><strong id="mm">00</strong><small>mins</small></div><div><strong id="ss">00</strong><small>secs</small></div>
    </div>'''
hero_copy_new = '''    <p class="hero-line" id="heroBirthdayLine">Năm nay anh không thể đứng cạnh em, nên anh gom những điều muốn nói vào đây.</p>
    <p class="hero-sub" id="heroBirthdaySub">Không phải món quà lớn. Chỉ là một nơi nhỏ anh làm riêng cho em, để khoảng cách hôm nay bớt xa đi một chút.</p>
    <div class="countdown" id="birthdayCountdown">
      <div><strong id="dd">00</strong><small>days</small></div><div><strong id="hh">00</strong><small>hours</small></div>
      <div><strong id="mm">00</strong><small>mins</small></div><div><strong id="ss">00</strong><small>secs</small></div>
    </div>
    <p class="birthday-now-message" id="birthdayNowMessage" role="status" aria-live="polite" hidden>
      <strong>Hôm nay là ngày của em.</strong>
      Chúc mừng sinh nhật, em bé. Mong tuổi mới dịu dàng với em và mang đến thật nhiều điều khiến em mỉm cười.
    </p>'''
must_replace(hero_copy_old, hero_copy_new, "hero countdown markup")

countdown_old = '''function target(){const n=new Date(),y=n.getFullYear();let t=new Date(Date.UTC(y,7,11,22));if(t<n)t=new Date(Date.UTC(y+1,7,11,22));return t}
function tick(){let d=Math.max(0,target()-Date.now()),s=Math.floor(d/1000);$("#dd").textContent=String(Math.floor(s/86400)).padStart(2,"0");$("#hh").textContent=String(Math.floor(s%86400/3600)).padStart(2,"0");$("#mm").textContent=String(Math.floor(s%3600/60)).padStart(2,"0");$("#ss").textContent=String(s%60).padStart(2,"0")}'''
countdown_new = '''const BIRTHDAY_TIME_ZONE="Europe/Stockholm";
const birthdayDateFormatter=new Intl.DateTimeFormat("en-CA",{
  timeZone:BIRTHDAY_TIME_ZONE,
  year:"numeric",
  month:"2-digit",
  day:"2-digit"
});

function getBirthdayLocalDate(date=new Date()){
  const values={};
  birthdayDateFormatter.formatToParts(date).forEach(part=>{
    if(part.type!=="literal") values[part.type]=Number(part.value);
  });
  return {year:values.year,month:values.month,day:values.day};
}

function target(date=new Date()){
  const local=getBirthdayLocalDate(date);
  const birthdayPassed=local.month>8 || (local.month===8 && local.day>12);
  const targetYear=birthdayPassed?local.year+1:local.year;
  return new Date(Date.UTC(targetYear,7,11,22));
}

function tick(){
  const now=new Date();
  const local=getBirthdayLocalDate(now);
  const isBirthday=local.month===8 && local.day===12;
  const countdown=$("#birthdayCountdown");
  const birthdayMessage=$("#birthdayNowMessage");

  if(countdown) countdown.hidden=isBirthday;
  if(birthdayMessage) birthdayMessage.hidden=!isBirthday;
  document.body.classList.toggle("birthday-today",isBirthday);

  if(isBirthday) return;

  const d=Math.max(0,target(now)-now.getTime());
  const s=Math.floor(d/1000);
  $("#dd").textContent=String(Math.floor(s/86400)).padStart(2,"0");
  $("#hh").textContent=String(Math.floor(s%86400/3600)).padStart(2,"0");
  $("#mm").textContent=String(Math.floor(s%3600/60)).padStart(2,"0");
  $("#ss").textContent=String(s%60).padStart(2,"0");
}'''
must_replace(countdown_old, countdown_new, "birthday countdown JavaScript")

# Make the relationship language romantic but open-ended rather than promising a fixed ending.
replacements = [
    (
        "Sau này chắc trang này sẽ có thêm nhiều ảnh chung hơn.",
        "Anh mong rồi sẽ có thêm những tấm ảnh chung, nếu một ngày hai đứa có cơ hội đứng cạnh nhau.",
        "story future-photo note",
    ),
    (
        "<h3>Anh bắt đầu nghĩ xa hơn hôm nay</h3><p>Không chỉ là một món quà sinh nhật. Anh bắt đầu muốn có thêm những ngày, những chuyến đi và những tấm ảnh thật sự có cả hai đứa.</p>",
        "<h3>Anh bắt đầu trân trọng điều đang có</h3><p>Không chỉ là một món quà sinh nhật. Anh muốn giữ lại cảm giác của hiện tại — những câu chuyện, sự quan tâm và khoảng cách mà hai đứa vẫn đang cố gắng đi qua.</p>",
        "timeline future promise",
    ),
    (
        'data-msg="Anh cũng nhớ em. Ráng thêm chút nữa rồi sẽ có ngày gặp nhau."',
        'data-msg="Anh cũng nhớ em. Dù ngày mai thế nào, những điều mình đã dành cho nhau vẫn là thật."',
        "open-when missing message",
    ),
    (
        "<p class=\"secret-ending-kicker\">The beginning, not the ending</p>\n          <h4>Đây mới chỉ là phiên bản đầu tiên.</h4>",
        "<p class=\"secret-ending-kicker\">A little place to remember</p>\n          <h4>Một nơi nhỏ để giữ lại hôm nay.</h4>",
        "game ending heading",
    ),
    (
        "Trang này bắt đầu từ sinh nhật em. Nhưng anh không định để nó dừng lại ở hôm nay.\n            Anh sẽ tiếp tục thêm những câu chuyện, những tấm ảnh và những ngày của hai đứa —\n            để nơi này dần trở thành một góc riêng của hai đứa mình.",
        "Trang này bắt đầu từ sinh nhật em, để giữ lại những điều anh thật lòng muốn nói ở hiện tại.\n            Tương lai sẽ đi đâu, anh không muốn đoán thay cả hai đứa —\n            chỉ mong khi em mở lại, em vẫn cảm nhận được sự chân thành anh đã đặt vào đây.",
        "game ending copy",
    ),
    (
        "<span><small>Sau này</small>Thêm những điều của hai đứa</span>",
        "<span><small>Nếu có dịp</small>Thêm một kỷ niệm mới</span>",
        "game path step two",
    ),
    (
        "<span><small>Dần dần</small>Một nơi chỉ hai đứa hiểu</span>",
        "<span><small>Về sau</small>Một nơi để nhớ lại</span>",
        "game path step three",
    ),
    (
        "Hai đứa chưa có nhiều ảnh chung, cũng chưa đi cùng nhau được nhiều. Nhưng anh không thấy điều đó đáng buồn, vì anh vẫn muốn tin phía trước còn rất nhiều ngày để hai đứa làm đầy những chỗ đang còn trống.",
        "Hai đứa chưa có nhiều ảnh chung, cũng chưa đi cùng nhau được nhiều. Anh không muốn biến tương lai thành một lời hứa thay cho cả hai; anh chỉ biết những gì mình đã có đến hôm nay đều đáng để anh trân trọng.",
        "letter future paragraph",
    ),
    (
        "Đây mới chỉ là phiên bản đầu tiên. Anh muốn nơi này lớn lên cùng những câu chuyện, tấm ảnh và những ngày của hai đứa.",
        "Đây là phiên bản anh làm cho sinh nhật em. Nếu sau này có thêm một kỷ niệm đẹp, anh sẽ biết nơi để giữ nó lại.",
        "letter postscript",
    ),
    (
        "Đây mới chỉ là trang đầu tiên của “thế giới riêng” hai đứa mình.",
        "Anh để những trang sau còn trống, cho bất cứ điều gì tương lai mang đến.",
        "final message",
    ),
    (
        "<strong>Để dành cho ngày hai đứa gặp nhau.</strong>\n          <p>Anh chưa có tấm ảnh này để đặt vào đây. Mình sẽ chụp nó sau.</p>",
        "<strong>Một chỗ trống cho điều chưa biết.</strong>\n          <p>Anh chưa có tấm ảnh này. Nếu một ngày nó tồn tại, nơi này sẽ có chỗ để giữ lại.</p>",
        "future photo card",
    ),
    (
        "<small>Future ticket · Private</small>\n                <strong>Our first day together</strong>",
        "<small>Open ticket · Private</small>\n                <strong>For a day not decided yet</strong>",
        "future ticket heading",
    ),
    (
        "<div><small>Status</small><b>Reserved</b></div>",
        "<div><small>Status</small><b>Open</b></div>",
        "future ticket status",
    ),
    (
        "<p class=\"ticket-note\">Tấm vé này không có ngày hết hạn.</p>",
        "<p class=\"ticket-note\">Không phải lời hứa — chỉ là một chỗ nhỏ cho điều có thể đến.</p>",
        "future ticket note",
    ),
    (
        "<p class=\"epilogue-kicker\">D&H · To be continued</p>",
        "<p class=\"epilogue-kicker\">D&H · 12 August</p>",
        "epilogue kicker",
    ),
    (
        "<strong>Còn câu chuyện của hai đứa thì chưa.</strong>",
        "<strong>Còn ngày mai, cứ để ngày mai tự trả lời.</strong>",
        "epilogue ending",
    ),
    (
        "<p class=\"epilogue-copy\">Chúc mừng sinh nhật, em bé. Hẹn em ở tấm ảnh tiếp theo.</p>",
        "<p class=\"epilogue-copy\">Chúc mừng sinh nhật, em bé. Cảm ơn em vì đã có mặt trong những điều đẹp đẽ anh giữ ở đây.</p>",
        "epilogue copy",
    ),
]
for old, new, label in replacements:
    soft_replace(old, new, label)

INDEX.write_text(html, encoding="utf-8")

readme = README.read_text(encoding="utf-8")
if not readme.startswith("# Under the same sky — V10.9"):
    first_line, rest = readme.split("\n", 1)
    readme = "# Under the same sky — V10.9 Birthday Polish\n" + rest

if "## V10.9" not in readme:
    readme += f'''\n\n## V10.9\n\n- Cập nhật canonical, Open Graph và ảnh chia sẻ sang `{PUBLIC_URL}`.\n- Trong toàn bộ ngày 12/8 theo múi giờ Gothenburg, đồng hồ chuyển thành lời chúc sinh nhật riêng.\n- Sau ngày 12/8, đồng hồ tự chuyển sang sinh nhật năm kế tiếp.\n- Làm mềm các đoạn kết và lời nhắn về tương lai để giữ sự chân thành mà không áp đặt một happy ending.\n- Giữ nguyên vị trí chờ `our-song.mp3` và `message-for-duyen.mp3`.\n'''
README.write_text(readme, encoding="utf-8")

print("Applied V10.9 birthday polish.")
