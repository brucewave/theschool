# Hướng dẫn cho người / AI làm việc trong repo này

Repo chứa **nhiều báo cáo của nhiều thương hiệu**. Mỗi báo cáo là **một trang riêng, gửi link riêng**
cho đúng một bên. Người nhận link **không được biết** các trang khác tồn tại.
Trả lời và viết nội dung bằng tiếng Việt, dễ hiểu, không dùng thuật ngữ.

Trang chạy trên Vercel: https://theschool-gamma.vercel.app — push lên `main` là Vercel tự cập nhật
(không có bước build; `vercel.json` bật `cleanUrls` nên `abc.html` mở bằng `/abc`).

## Các trang đang có

| Link | File | Thương hiệu · nội dung | Sửa thế nào |
| --- | --- | --- | --- |
| `/` | `index.html` | THÉ School · báo cáo tuyển sinh 0–3 tuổi | **Không sửa thẳng** — sửa `Bao_cao_tuyen_sinh_2026-11-04/report_template.html` rồi chạy `build_html.py` (xem README) |
| `/mthouse` | `mthouse.html` + `mthouse-anh/` | MT House · tính năng Tool báo cáo nội bộ | Trang tĩnh, sửa thẳng |

## Thêm một trang mới (làm đủ cả 7 bước)

1. **Đặt tên** `<slug>` không dấu, gạch nối, ví dụ `mthouse-quang-cao`. Trang là `<slug>.html` ở gốc repo,
   mọi ảnh / tệp đi kèm để trong thư mục `<slug>-anh/`. Đường dẫn trong trang viết **tương đối**:
   `<slug>-anh/ten-anh.jpg` (không bắt đầu bằng `/`, không trỏ sang thư mục của trang khác).
2. **Trang tự đủ**: một tệp HTML, CSS và JS viết ngay trong tệp. Thư viện ngoài (nếu cần) chỉ nạp từ CDN
   có ghi rõ phiên bản. Dùng tốt trên điện thoại 375px, không phải kéo ngang.
3. **Trong `<head>`** thêm 2 thẻ (đây là tên và màu hiện trên thanh tab của admin):
   ```html
   <meta name="tab-label" content="Tên ngắn hiện trên tab">
   <meta name="tab-color" content="#mã-màu-thương-hiệu">
   ```
4. **Ngay sau `<body>`** thêm đúng một dòng:
   ```html
   <script src="/rtabs.js" defer></script>
   ```
   Nếu trang có thanh / nút cố định ở mép trên, chừa chỗ cho thanh tab **chỉ khi admin xem**:
   `html.rt-admin .page { padding-top: 70px }` (trên điện thoại ≤ 760px thanh tab nằm ở đáy, chừa `padding-bottom`).
5. **Thêm `"/<slug>"` vào `rtabs.json`** (mảng `pages`).
6. **Mở chặn trong `.gitignore`** (tệp này chặn mọi thứ trừ những gì được liệt kê) — thêm 2 dòng:
   ```
   !/<slug>.html
   !/<slug>-anh/
   ```
   Rồi thêm một dòng vào bảng "Các trang đang có" ở trên.
7. **Thử trước khi push**: mở `/<slug>` → không có thanh tab, không có chữ nào của thương hiệu khác.
   Admin mở `/<slug>?admin=<mã>` → có thanh tab đủ các trang (mã do chủ repo giữ, **không bao giờ** ghi vào repo).

## Quy tắc bắt buộc

- **Không nhắc tới thương hiệu / trang khác** ở bất cứ đâu trong trang: chữ, `<title>`, meta, link, chú thích
  trong mã, tên ảnh, tên thư mục. Chỉ `rtabs.js` / `rtabs.json` biết có nhiều trang.
- **Không sửa trang của thương hiệu khác**, không sửa `rtabs.js` khi không cần.
- Không đưa lên repo: mật khẩu, khoá API, số tài khoản, lương, số điện thoại / địa chỉ khách hàng.
  Repo này **công khai**.
- Commit nhỏ, ghi rõ trang nào, rồi push `main`.

## Cách trình bày (chủ repo thích)

Ít chữ, nhiều ảnh, biểu đồ, bảng, biểu tượng. **Việc quan trọng / đang triển khai / cần chốt ghi ngay đầu trang.**
Câu ngắn, số liệu thành thẻ số hoặc biểu đồ, danh sách dài thành bảng. Bấm ảnh xem to được.
Mẫu bố cục tham khảo: `mthouse.html` (khung "Đang triển khai", khung "Quan trọng", thẻ số, biểu đồ, chi tiết
từng mục có ảnh, bảng đề xuất cuối trang).
