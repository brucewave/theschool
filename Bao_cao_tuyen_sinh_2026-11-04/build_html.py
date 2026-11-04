from pathlib import Path
import json,csv,base64,zipfile
from PIL import Image

root=Path(__file__).resolve().parent
evidence=root/'bang_chung'
sources=json.loads((root/'nguon_tham_khao.json').read_text(encoding='utf-8'))
ai=json.loads((root/'ai_content.json').read_text(encoding='utf-8'))
sources.update(ai['sources'])
manifest={x['name']:x for x in json.loads((root/'manifest_bang_chung.json').read_text(encoding='utf-8'))}
keys={'THÉ':'THE','Sakura':'Sakura','Casa':'Casa','Fuji':'Fuji','Sky-Line':'Skyline'}
payload={'sources':sources,'ai':ai,'ads':[],'evidence':[],'images':{}}
def embed(name,path):
    mime='image/png' if path.suffix.lower()=='.png' else 'image/jpeg'
    payload['images'][name]='data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode('ascii')
payload['design_refs']=[
    {'id':'01','name':'design_ref_01','title':'Ảnh ghép · tuổi tuyển sinh nổi bật','file':'01_tuyen_sinh_anh_ghep.png','lesson':'Một thông điệp lớn + ảnh trẻ và cô trong nhiều tình huống.','use':'THÉ: mốc tuổi đã xác nhận + 3–4 ảnh chăm sóc thật.'},
    {'id':'02','name':'design_ref_02','title':'Ảnh lợi ích · 4 lý do để tìm hiểu','file':'02_tuyen_sinh_loi_ich.png','lesson':'Chia ô giúp phụ huynh quét nhanh từng lợi ích.','use':'THÉ: chăm sóc, nếp sinh hoạt, môi trường, trao đổi với gia đình.'},
    {'id':'03','name':'design_ref_03','title':'Ảnh giải đáp · đi học hay chờ thêm?','file':'03_giai_dap_phu_huynh.png','lesson':'Mở bằng câu hỏi phụ huynh đang cân nhắc.','use':'THÉ: mời gặp cô / xem lớp; dùng lịch và người phụ trách có thật.'}
]
for ref in payload['design_refs']:
    image_path=root/'thiet_ke_tham_khao'/ref['file']
    ref['width'],ref['height']=Image.open(image_path).size
    embed(ref['name'],image_path)
with (root/'Danh_muc_quang_cao.csv').open(encoding='utf-8-sig',newline='') as f:
    for row in csv.DictReader(f):
        aid=row['Library ID'];path=evidence/'cards'/(aid+'.jpg');im=Image.open(path)
        payload['ads'].append({'school':keys[row['Trường']],'id':aid,'date':row['Ngày bắt đầu hiển thị'],'theme':row['Chủ đề đọc được'],'type':row['Phân loại'],'url':row['URL'],'height':im.height})
        embed('card_'+aid,path)
titles={
'01_THE_website':('THÉ · Website','website'),
'02_THE_social':('THÉ · Bìa Facebook','social'),
'03_Sakura_social':('Sakura · Bìa Facebook','social'),
'04_Cocoon_website':('Cocoon · Website','website'),
'05_Cocoon_datlich':('Cocoon · Form tham quan','website'),
'06_THE_ads':('THÉ · Kết quả Ads Library','ads'),
'07_THE_ad_chitiet':('THÉ · Ads còn mốc tháng 5','ads'),
'08_Casa_social':('Casa · Bìa Facebook','social'),
'09_Cocoon_social':('Cocoon · Bìa Facebook','social'),
'10_Fuji_website':('Fuji · Lời mời trải nghiệm','website'),
'11_Skyline_website':('Sky-Line · Landing page 2025–2026','website'),
'12_Fuji_social':('Fuji · Bìa Facebook','social'),
'13_Sakura_ads':('Sakura · Kết quả Ads Library','ads'),
'16_Casa_ads':('Casa · Kết quả Ads Library','ads'),
'17_Skyline_social':('Sky-Line · Bìa Facebook','social'),
'18_Cocoon_ads':('Cocoon · Không có mẫu khớp','ads'),
'19_Fuji_ads':('Fuji · Kết quả Ads Library','ads'),
'20_THE_bai_trai_nghiem':('THÉ · Bài trải nghiệm nghề làm muối','other'),
'21_Skyline_ads':('Sky-Line · Kết quả Ads Library','ads'),
'23_Skyline_12thang':('Sky-Line · Quảng cáo nhà trẻ 12 tháng','ads'),
'24_THE_tiktok_truycap':('THÉ · TikTok yêu cầu đăng nhập','other'),
'25_Fuji_12thang':('Fuji · Quảng cáo bé 12 tháng','ads'),
'26_Sakura_ad_chitiet':('Sakura · Thông điệp tuyển sinh','ads'),
'27_Casa_ad_chitiet':('Casa · Quảng cáo vận động','ads'),
}
for name,(title,category) in titles.items():
    embed(name,evidence/(name+'.jpg'))
    payload['evidence'].append({'name':name,'title':title,'category':category,'url':manifest[name]['url']})
template=(root/'report_template.html').read_text(encoding='utf-8')
template=template.replace('__AD_PRODUCTION_CSS__',(root/'ads_production.css').read_text(encoding='utf-8'))
template=template.replace('__VISUAL_CSS__',(root/'visual_refresh.css').read_text(encoding='utf-8'))
template=template.replace('__AD_PRODUCTION_SECTION__',(root/'ads_production.html').read_text(encoding='utf-8'))
assert template.count('__REPORT_DATA__')==1
html=template.replace('__REPORT_DATA__',json.dumps(payload,ensure_ascii=False,separators=(',',':')).replace('</',r'<\/'))
logo='data:image/png;base64,'+base64.b64encode((root/'assets'/'logo-the-school.png').read_bytes()).decode('ascii')
html=html.replace('__BRAND_LOGO__',logo)
html=html.replace('THÁNG TUỔI / LỚP','TUỔI ƯU TIÊN')
for target in [root.parent/'index.html',root/'index.html']:target.write_text(html,encoding='utf-8')
with zipfile.ZipFile(root/'THE_Bao_cao_truc_quan_HTML.zip','w',zipfile.ZIP_DEFLATED) as z:z.write(root.parent/'index.html','index.html')
print(json.dumps({'html':str(root.parent/'index.html'),'bytes':len(html.encode('utf-8')),'ad_cards':len(payload['ads']),'evidence':len(payload['evidence']),'self_contained':True},ensure_ascii=True))
