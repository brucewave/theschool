# THÉ School · Báo cáo tuyển sinh 0–3 tuổi

Báo cáo trực quan thị trường mầm non Đà Nẵng, khảo sát ngày **04/11/2026**.

## Xem báo cáo

- **`index.html`**: kế hoạch hành động 30 ngày (kênh mới 0–3 tuổi, fanpage THÉ, quảng cáo 200k/ngày, số liệu dự kiến, lịch). Đây là trang chính.
- **`nghien-cuu.html`**: bản nghiên cứu đầy đủ (so sánh 5 trường, 17 card quảng cáo, 30 chủ đề video, shot list, nguồn).

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

Lệnh dựng chỉ cập nhật `nghien-cuu.html` (bản nghiên cứu). `index.html` (kế hoạch hành động) được sửa trực tiếp.
