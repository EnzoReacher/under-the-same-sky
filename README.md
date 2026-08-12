# Under the same sky — V28 Final

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

## V28 — Final mobile & desktop audio mix

- Cập nhật đồng thời hai bản hoàn chỉnh trong `mobile/` và `desktop/`.
- Khi mở lá thư, nhạc nền hạ ngay xuống mức nhẹ.
- Khi phát lời chúc, giọng thật ở mức 84% và nhạc nền tiếp tục chạy ở mức 6,5%.
- Khi tạm dừng hoặc nghe hết lời chúc, nhạc nền tự trở lại mức bình thường.
- Trang gốc tự nhận diện thiết bị và chuyển tới đúng bản V28.

## V24 — Reliable voice playback

- Chuyển lời chúc và nhạc nền từ dữ liệu nhúng trong HTML sang file MP3 cùng tên miền để Safari và trình duyệt mobile tải ổn định hơn.
- Chuẩn hóa âm lượng lời chúc, giữ nguyên thời lượng 2 phút 11 giây.
- Giữ cơ chế hạ nhỏ nhạc nền khi lời chúc đang phát và khôi phục âm lượng sau khi dừng.


## V10.8.1

- Sửa màn “Đọc dòng cuối cùng” xuất hiện ngoài viewport khi cinematic đã cuộn xuống.
- Epilogue bám trực tiếp theo viewport trên desktop và mobile.
- Khi quay lại, cinematic trở về đúng vị trí tấm vé.


## V10.9

- Cập nhật canonical, Open Graph và ảnh chia sẻ sang `https://under-samma-himmel.hoangnt2000.chatgpt.site/`.
- Trong toàn bộ ngày 12/8 theo múi giờ Gothenburg, đồng hồ chuyển thành lời chúc sinh nhật riêng.
- Sau ngày 12/8, đồng hồ tự chuyển sang sinh nhật năm kế tiếp.
- Làm mềm các đoạn kết và lời nhắn về tương lai để giữ sự chân thành mà không áp đặt một happy ending.
- Giữ nguyên vị trí chờ `our-song.mp3` và `message-for-duyen.mp3`.
