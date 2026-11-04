# THÉ School · Báo cáo tuyển sinh 0–3 tuổi

Báo cáo trực quan thị trường mầm non Đà Nẵng, khảo sát ngày **04/11/2026**.

## Xem báo cáo

Mở **`index.html`** bằng Chrome hoặc Edge. File đã nhúng logo, biểu đồ và ảnh; dùng được offline, không cần cài đặt hay chạy server.

- So sánh THÉ với 5 trường; ảnh social và 17 card quảng cáo đầy đủ.
- Mô hình media 200–300k/ngày, có thể điều chỉnh trực tiếp.
- Kế hoạch 30 video AI, bộ lọc chủ đề và 6 kịch bản mẫu.
- 3 ảnh thiết kế tham khảo, 2 phương án sản xuất video và shot list 10 nhóm cảnh.

Bấm các mục mở rộng để xem bảng, brief và nguồn chi tiết. Số quảng cáo và follower không phản ánh hiệu quả tuyển sinh; các dự báo chuyển đổi là **giả định**, không phải kết quả đã chạy của THÉ. Ảnh tham khảo người dùng cung cấp được phân biệt với bằng chứng Ads Library.

## Cập nhật báo cáo

Yêu cầu Python và Pillow:

```sh
python -m pip install -r requirements.txt
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

Lệnh dựng cập nhật `index.html` ở gốc repo, đồng thời tạo bản HTML và ZIP trong thư mục báo cáo. File HTML ở gốc là bản để đọc và chia sẻ.
