import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import os

doc = docx.Document()

# Set standard A4 margins (1 inch / 2.54 cm)
sections = doc.sections
for section in sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

# Set Normal Style font to TH Sarabun PSK or TH Sarabun New
style = doc.styles['Normal']
font = style.font
font.name = 'TH Sarabun PSK'
font.size = Pt(16)
font.color.rgb = RGBColor(0, 0, 0)

# 1. Header: บันทึกข้อความ (Bold 29 pt)
p_header = doc.add_paragraph()
p_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_header.paragraph_format.space_before = Pt(0)
p_header.paragraph_format.space_after = Pt(12)
run_header = p_header.add_run("บันทึกข้อความ")
run_header.bold = True
run_header.font.size = Pt(29)

# 2. ส่วนราชการ (Bold 20 pt label, 16 pt value)
p_agency = doc.add_paragraph()
p_agency.paragraph_format.space_before = Pt(0)
p_agency.paragraph_format.space_after = Pt(4)
run_lbl1 = p_agency.add_run("ส่วนราชการ  ")
run_lbl1.bold = True
run_lbl1.font.size = Pt(20)
run_val1 = p_agency.add_run("สถานีตำรวจภูธรบางปะกง  อำเภอบางปะกง  จังหวัดฉะเชิงเทรา")
run_val1.font.size = Pt(16)

# 3. ที่ และ วันที่
p_ref = doc.add_paragraph()
p_ref.paragraph_format.space_before = Pt(0)
p_ref.paragraph_format.space_after = Pt(4)
run_lbl2 = p_ref.add_run("ที่  ")
run_lbl2.bold = True
run_lbl2.font.size = Pt(20)
run_val2 = p_ref.add_run("ตช ๐๐๑๗.(ฉช).๔/               ")
run_val2.font.size = Pt(16)
run_lbl3 = p_ref.add_run("วันที่  ")
run_lbl3.bold = True
run_lbl3.font.size = Pt(20)
run_val3 = p_ref.add_run("๙  พฤศจิกายน  ๒๕๖๙")
run_val3.font.size = Pt(16)

# 4. เรื่อง
p_subj = doc.add_paragraph()
p_subj.paragraph_format.space_before = Pt(0)
p_subj.paragraph_format.space_after = Pt(12)
run_lbl4 = p_subj.add_run("เรื่อง  ")
run_lbl4.bold = True
run_lbl4.font.size = Pt(20)
run_val4 = p_subj.add_run("รายงานผลการปฏิบัติหน้าที่ จับกุมผู้ต้องหาตามหมายจับ")
run_val4.font.size = Pt(16)

# 5. เรียน
p_to = doc.add_paragraph()
p_to.paragraph_format.space_before = Pt(0)
p_to.paragraph_format.space_after = Pt(12)
run_lbl5 = p_to.add_run("เรียน  ")
run_lbl5.bold = True
run_lbl5.font.size = Pt(16)
run_val5 = p_to.add_run("ผกก.สภ.บางปะกง")
run_val5.font.size = Pt(16)

# 6. เนื้อหาข้อความ ย่อหน้า 1: การอำนวยการและชุดจับกุม
p_body1 = doc.add_paragraph()
p_body1.paragraph_format.first_line_indent = Inches(0.8)
p_body1.paragraph_format.space_before = Pt(0)
p_body1.paragraph_format.space_after = Pt(6)
p_body1.paragraph_format.line_spacing = 1.15
r1 = p_body1.add_run(
    "ด้วยเมื่อวันที่ ๙ พฤศจิกายน ๒๕๖๙ เวลาประมาณ ๑๑.๐๐ น. ภายใต้การอำนวยการของ พ.ต.อ.บัณฑิต ธรรมอนันต์ ผกก.สภ.บางปะกง, "
    "พ.ต.ท.ชินพัฒน์ พุทธเมตตา รอง ผกก.สส.สภ.บางปะกง นำโดย พ.ต.ท.พรศักดิ์ คชชะ สว.สส.สภ.บางปะกง, ร.ต.อ.ธรรมนูญ บรรเทิงจิตต์ "
    "รอง สว.(สส.) สภ.บางปะกง พร้อมด้วยกำลังชุดสืบสวน สภ.บางปะกง ร่วมกับ เจ้าพนักงานตำรวจ กก.สืบสวน ๓ บก.สส.ภ.๒ "
    "นำโดย พ.ต.ต.ภูทัย นรสิงห์, ร.ต.อ.คมกฤษ สั้นหลาม, ร.ต.ต.ณัฐ สอนตระกูล, ด.ต.อภิชัย โกจินทึก, ด.ต.ธฤต เดชธรรมฤทธิ์, "
    "ด.ต.อรพร เปรมอำพล และ ส.ต.ท.ณัฐวุธ อินทรเรืองศรี ได้ร่วมกันทำการจับกุมตัวผู้ต้องหา ดังนี้"
)

# 7. รายละเอียดผู้ต้องหา
p_suspect = doc.add_paragraph()
p_suspect.paragraph_format.left_indent = Inches(1.2)
p_suspect.paragraph_format.space_before = Pt(0)
p_suspect.paragraph_format.space_after = Pt(4)
r_s = p_suspect.add_run("๑. นางสาวนิตติญา หรือ เจน ชาเสน  อายุ ๔๐ ปี  สัญชาติไทย\n")
r_s.bold = True
p_suspect.add_run(
    "    เลขประจำตัวประชาชน : ๑-๔๙๐๓๐๐๐๓๓-๓๖-๗\n"
    "    ที่อยู่ตามทะเบียนบ้าน : บ้านเลขที่ ๑๑๓ หมู่ที่ ๒ ตำบลเหล่าหมี อำเภอดอนตาล จังหวัดมุกดาหาร (ผู้ต้องหา)"
)

# 8. ข้อกล่าวหา
p_charge = doc.add_paragraph()
p_charge.paragraph_format.left_indent = Inches(1.2)
p_charge.paragraph_format.space_before = Pt(0)
p_charge.paragraph_format.space_after = Pt(4)
r_c_lbl = p_charge.add_run("โดยกล่าวหาว่ากระทำความผิดฐาน : ")
r_c_lbl.bold = True
r_c_val = p_charge.add_run(
    "“ร่วมกันลักทรัพย์ในเวลากลางคืน โดยใช้ยานพาหนะ เพื่อสะดวกแก่การกระทำความผิดเพื่อการพาทรัพย์นั้นไป "
    "หรือเพื่อให้พ้นจากการจับกุม” ตามหมายจับศาลจังหวัดฉะเชิงเทรา ที่ ๔๐๘/๒๕๖๙ ลงวันที่ ๕ พฤศจิกายน ๒๕๖๙"
)

# 9. สถานที่จับกุม
p_loc = doc.add_paragraph()
p_loc.paragraph_format.left_indent = Inches(1.2)
p_loc.paragraph_format.space_before = Pt(0)
p_loc.paragraph_format.space_after = Pt(6)
r_l_lbl = p_loc.add_run("สถานที่จับกุม : ")
r_l_lbl.bold = True
r_l_val = p_loc.add_run("บริเวณภายในบริษัท จั้มเวย์ จำกัด เลขที่ ๑ หมู่ที่ ๑ ตำบลหอมศีล อำเภอบางปะกง จังหวัดฉะเชิงเทรา")

# 10. พฤติการณ์และการดำเนินการ
p_action = doc.add_paragraph()
p_action.paragraph_format.first_line_indent = Inches(0.8)
p_action.paragraph_format.space_before = Pt(0)
p_action.paragraph_format.space_after = Pt(6)
p_action.paragraph_format.line_spacing = 1.15
p_action.add_run(
    "ก่อนการจับกุม เจ้าหน้าที่ตำรวจชุดจับกุมได้รับแจ้งจากสายลับว่า ผู้ต้องหาตามหมายจับดังกล่าวได้ปรากฏตัวอยู่ที่บริเวณสถานที่เกิดเหตุ "
    "จึงได้เดินทางไปตรวจสอบและพบตัวผู้ต้องหาตรงตามรูปพรรณในหมายจับ จึงได้แสดงตัวและแสดงหมายจับให้ดู อ่านจนเข้าใจดีแล้ว "
    "ผู้ต้องหายอมรับว่าเป็นบุคคลตามหมายจับจริงและยังไม่เคยถูกจับกุมตามหมายจับนี้มาก่อน เจ้าหน้าที่จึงได้ควบคุมตัวนำส่ง "
    "พนักงานสอบสวน สภ.บางปะกง เพื่อดำเนินคดีตามกฎหมายต่อไป"
)

# 11. จึงเรียนมาเพื่อโปรดทราบ
p_close = doc.add_paragraph()
p_close.paragraph_format.first_line_indent = Inches(0.8)
p_close.paragraph_format.space_before = Pt(6)
p_close.paragraph_format.space_after = Pt(24)
p_close.add_run("จึงเรียนมาเพื่อโปรดทราบ")

# 12. ลายมือชื่อ
p_sign = doc.add_paragraph()
p_sign.alignment = WD_ALIGN_PARAGRAPH.RIGHT
p_sign.paragraph_format.right_indent = Inches(0.8)
p_sign.paragraph_format.space_after = Pt(0)
p_sign.add_run(
    "(ลงชื่อ)........................................................\n"
    "( พ.ต.ท.พรศักดิ์  คชชะ )\n"
    "สว.สส.สภ.บางปะกง"
)

# 13. ตารางรูปถ่ายประกอบ
doc.add_page_break()
p_pic_head = doc.add_paragraph()
p_pic_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_pic_head.paragraph_format.space_after = Pt(12)
r_ph = p_pic_head.add_run("ภาพถ่ายประกอบรายงานผลการปฏิบัติงาน สภ.บางปะกง")
r_ph.bold = True
r_ph.font.size = Pt(18)

# Table for 2 photos
table = doc.add_table(rows=1, cols=2)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
for cell in table.rows[0].cells:
    cell.width = Inches(3.2)

if os.path.exists('photo_sample1.jpg'):
    cell_left = table.rows[0].cells[0]
    p_img1 = cell_left.paragraphs[0]
    p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img1.add_run().add_picture('photo_sample1.jpg', width=Inches(3.0))
    p_cap1 = cell_left.add_paragraph("ภาพขณะเจ้าหน้าที่ทำการตรวจสอบและควบคุมตัว")
    p_cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap1.runs[0].font.size = Pt(12)

if os.path.exists('photo_sample2.jpg'):
    cell_right = table.rows[0].cells[1]
    p_img2 = cell_right.paragraphs[0]
    p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img2.add_run().add_picture('photo_sample2.jpg', width=Inches(3.0))
    p_cap2 = cell_right.add_paragraph("ภาพขณะแสดงหมายจับและแจ้งข้อกล่าวหาให้ทราบ")
    p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap2.runs[0].font.size = Pt(12)

docx_path = "บันทึกข้อความ_รายงานผลการปฏิบัติ_สภ_บางปะกง.docx"
doc.save(docx_path)
print(f"Word document saved successfully to {docx_path}")

