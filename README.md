# THÉ School · Báo cáo tuyển sinh 0–3 tuổi

Báo cáo trực quan thị trường mầm non Đà Nẵng, khảo sát ngày **04/11/2026**.

## Xem báo cáo

Mở **`index.html`**. Các phần chính:

- Tóm tắt: kênh cũ (fanpage THÉ) và kênh mới 0–3 tuổi, mỗi kênh đăng gì, bao nhiêu, chạy tiền thế nào, kỳ vọng gì.
- 04 · Phễu hay chạy thẳng, cách chia 200k/ngày, số liệu theo giá tin nhắn thực tế (50–100k/tin nhắn) và bảng "thấy gì sửa gì".
- 05 · Kênh mới 0–3 tuổi: 4 dạng video, lịch tuần, 30 chủ đề, 6 kịch bản.
- 06 · Kênh cũ (fanpage THÉ): dạng bài, lịch tuần, cài quảng cáo, tin nhắn chào, lịch 30 ngày, mẫu ảnh và shot list.
- So sánh 5 trường và 17 card quảng cáo đối thủ. (Mục 07 ảnh bằng chứng & nguồn đã bỏ; ảnh gốc vẫn ở `bang_chung/`.)

Mở bằng Chrome/Edge, hoặc xem trên Vercel.

## Deploy Vercel

Trang tĩnh, không cần build. `vercel.json` đặt framework = Other, không chạy lệnh build/cài đặt. Import repo trên Vercel rồi bấm Deploy; mỗi lần push lên `main` Vercel tự cập nhật.

## Cập nhật báo cáo

Yêu cầu Python và Pillow:

```sh
python -m pip install -r Bao_cao_tuyen_sinh_2026-11-04/requirements.txt
python Bao_cao_tuyen_sinh_2026-11-04/build_html.py
```

Mã dựng nằm trong `Bao_cao_tuyen_sinh_2026-11-04/`:

| File | Nội dung |
| --- | --- |
| `report_template.html` | Bố cục, biểu đồ và tương tác |
| `visual_refresh.css` | Thẻ màu và phân cấp chữ |
| `ai_content.json` | Chủ đề, kịch bản và nguồn kiến thức |
| `ads_production.html`, `ads_production.css` | Mẫu ảnh và phương án quay |
| `bang_chung/`, `thiet_ke_tham_khao/`, `assets/` | Ảnh nguồn và logo |

Lệnh dựng tạo lại `index.html` ở gốc repo từ các file trên. Sửa nội dung trong `report_template.html` rồi chạy lại lệnh dựng, không sửa trực tiếp `index.html`.
