import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
import os

prs = pptx.Presentation()
# Set to A4 Portrait
prs.slide_width = Inches(8.27)
prs.slide_height = Inches(11.69)

# Blank slide layout
blank_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_layout)

# Define Theme Colors
NAVY_DARK = RGBColor(9, 36, 82)       # #092452
NAVY_PILL = RGBColor(12, 49, 102)     # #0c3166
BLUE_ACCENT = RGBColor(45, 136, 255)  # #2d88ff
BLUE_LIGHT = RGBColor(220, 237, 255)  # #dcedff
RED_SLOGAN = RGBColor(217, 20, 36)    # #d91424
TEXT_DARK = RGBColor(20, 24, 33)      # #141821
TEXT_MUTED = RGBColor(90, 95, 105)
WHITE = RGBColor(255, 255, 255)
BG_LIGHT = RGBColor(248, 250, 253)
CARD_BG = RGBColor(235, 243, 253)

# 1. Background
bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(8.27), Inches(11.69))
bg_shape.fill.solid()
bg_shape.fill.fore_color.rgb = WHITE
bg_shape.line.fill.background()

# 2. Header Top Banner (Dark Blue)
header_rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(8.27), Inches(1.5))
header_rect.fill.solid()
header_rect.fill.fore_color.rgb = NAVY_DARK
header_rect.line.fill.background()

# Header Badge Image
if os.path.exists('police_badge.png'):
    slide.shapes.add_picture('police_badge.png', Inches(0.25), Inches(0.12), width=Inches(1.25))

# Header Station Name
title_box = slide.shapes.add_textbox(Inches(1.55), Inches(0.12), Inches(4.0), Inches(0.85))
tf = title_box.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
p1 = tf.paragraphs[0]
p1.text = "สภ.บางปะกง"
p1.font.name = "TH Sarabun PSK"
p1.font.size = Pt(28)
p1.font.bold = True
p1.font.color.rgb = WHITE

p2 = tf.add_paragraph()
p2.text = "BANGPAKONG POLICE STATION"
p2.font.name = "Arial"
p2.font.size = Pt(10)
p2.font.bold = True
p2.font.color.rgb = BLUE_LIGHT

# Red Slogan Pill
slogan_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.55), Inches(1.02), Inches(3.2), Inches(0.38))
slogan_box.fill.solid()
slogan_box.fill.fore_color.rgb = RED_SLOGAN
slogan_box.line.fill.background()
tf_slogan = slogan_box.text_frame
tf_slogan.vertical_anchor = MSO_ANCHOR.MIDDLE
p_slogan = tf_slogan.paragraphs[0]
p_slogan.text = "“ดูแลทุกข์ สุขของประชาชน”"
p_slogan.font.name = "TH Sarabun PSK"
p_slogan.font.size = Pt(14)
p_slogan.font.bold = True
p_slogan.font.color.rgb = WHITE
p_slogan.alignment = PP_ALIGN.CENTER

# Right Header: Report Type Pill
rpt_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.6), Inches(0.15), Inches(2.45), Inches(0.65))
rpt_pill.fill.solid()
rpt_pill.fill.fore_color.rgb = RGBColor(6, 25, 60)
rpt_pill.line.color.rgb = BLUE_ACCENT
rpt_pill.line.width = Pt(1)
tf_rpt = rpt_pill.text_frame
tf_rpt.vertical_anchor = MSO_ANCHOR.MIDDLE
p_r1 = tf_rpt.paragraphs[0]
p_r1.text = "รายงานผลการปฏิบัติ"
p_r1.font.name = "TH Sarabun PSK"
p_r1.font.size = Pt(14)
p_r1.font.bold = True
p_r1.font.color.rgb = WHITE
p_r1.alignment = PP_ALIGN.CENTER
p_r2 = tf_rpt.add_paragraph()
p_r2.text = "ประจำวัน"
p_r2.font.name = "TH Sarabun PSK"
p_r2.font.size = Pt(13)
p_r2.font.color.rgb = BLUE_LIGHT
p_r2.alignment = PP_ALIGN.CENTER

# Date Pill (White Card)
date_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.5), Inches(0.85), Inches(2.55), Inches(0.55))
date_card.fill.solid()
date_card.fill.fore_color.rgb = WHITE
date_card.line.color.rgb = BLUE_ACCENT
date_card.line.width = Pt(1.5)
tf_date = date_card.text_frame
tf_date.vertical_anchor = MSO_ANCHOR.MIDDLE
p_d1 = tf_date.paragraphs[0]
p_d1.text = "📅 วันที่ 9 พฤศจิกายน 2569"
p_d1.font.name = "TH Sarabun PSK"
p_d1.font.size = Pt(12)
p_d1.font.bold = True
p_d1.font.color.rgb = NAVY_DARK
p_d1.alignment = PP_ALIGN.CENTER
p_d2 = tf_date.add_paragraph()
p_d2.text = "เวลาประมาณ 11.00 น."
p_d2.font.name = "TH Sarabun PSK"
p_d2.font.size = Pt(11)
p_d2.font.color.rgb = TEXT_DARK
p_d2.alignment = PP_ALIGN.CENTER

# ==================== BODY SECTION ====================
# Left Column: x=0.3 to 3.5 (width=3.2), Right Column: x=3.65 to 7.95 (width=4.3)
col1_left = Inches(0.3)
col1_width = Inches(3.2)
col2_left = Inches(3.65)
col2_width = Inches(4.35)
body_top = Inches(1.65)

# --- LEFT COLUMN: COMMAND & TEAM ---
# 1. Header: เรียน ผู้บังคับบัญชา
cmd_header = slide.shapes.add_textbox(col1_left, body_top, col1_width, Inches(0.6))
tf_ch = cmd_header.text_frame
tf_ch.margin_left = tf_ch.margin_top = tf_ch.margin_right = tf_ch.margin_bottom = 0
p = tf_ch.paragraphs[0]
p.text = "📋 เรียน ผู้บังคับบัญชา"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_DARK

p_sub = tf_ch.add_paragraph()
p_sub.text = "     สภ.บางปะกง"
p_sub.font.name = "TH Sarabun PSK"
p_sub.font.size = Pt(13)
p_sub.font.bold = True
p_sub.font.color.rgb = NAVY_DARK

# Section: ภายใต้การอำนวยการของ
lbl_under = slide.shapes.add_textbox(col1_left, body_top + Inches(0.65), col1_width, Inches(0.3))
tf_u = lbl_under.text_frame
tf_u.margin_left = tf_u.margin_top = tf_u.margin_right = tf_u.margin_bottom = 0
p = tf_u.paragraphs[0]
p.text = "ภายใต้การอำนวยการของ"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = NAVY_DARK

# Commander 1 Card
c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col1_left, body_top + Inches(0.95), col1_width, Inches(0.48))
c1.fill.solid()
c1.fill.fore_color.rgb = NAVY_DARK
c1.line.fill.background()
tf_c1 = c1.text_frame
tf_c1.margin_left = Inches(0.12)
tf_c1.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf_c1.paragraphs[0]
p.text = "👤  พ.ต.อ.บัณฑิต ธรรมอนันต์"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = WHITE
p2 = tf_c1.add_paragraph()
p2.text = "     ผกก.สภ.บางปะกง"
p2.font.name = "TH Sarabun PSK"
p2.font.size = Pt(10)
p2.font.color.rgb = BLUE_LIGHT

# Commander 2 Card
c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col1_left, body_top + Inches(1.48), col1_width, Inches(0.48))
c2.fill.solid()
c2.fill.fore_color.rgb = NAVY_DARK
c2.line.fill.background()
tf_c2 = c2.text_frame
tf_c2.margin_left = Inches(0.12)
tf_c2.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf_c2.paragraphs[0]
p.text = "👤  พ.ต.ท.ชินพัฒน์ พุทธเมตตา"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = WHITE
p2 = tf_c2.add_paragraph()
p2.text = "     รอง ผกก.สส.สภ.บางปะกง"
p2.font.name = "TH Sarabun PSK"
p2.font.size = Pt(10)
p2.font.color.rgb = BLUE_LIGHT

# Section: นำโดย (Pill)
lead_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col1_left, body_top + Inches(2.05), Inches(1.1), Inches(0.32))
lead_pill.fill.solid()
lead_pill.fill.fore_color.rgb = BLUE_ACCENT
lead_pill.line.fill.background()
p = lead_pill.text_frame.paragraphs[0]
p.text = "นำโดย"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Lead Officers Text Box
lead_box = slide.shapes.add_textbox(col1_left, body_top + Inches(2.4), col1_width, Inches(1.1))
tf_lb = lead_box.text_frame
tf_lb.word_wrap = True
tf_lb.margin_left = tf_lb.margin_top = tf_lb.margin_right = tf_lb.margin_bottom = 0
lead_lines = [
    ("• พ.ต.ท.พรศักดิ์ คชชะ", True),
    ("  สว.สส.สภ.บางปะกง", False),
    ("• ร.ต.อ.ธรรมนูญ บรรเทิงจิตต์", True),
    ("  รอง สว.(สส.) สภ.บางปะกง", False),
    ("พร้อมกำลังชุดสืบสวน สภ.บางปะกง", True)
]
for i, (txt, bold) in enumerate(lead_lines):
    p = tf_lb.paragraphs[0] if i == 0 else tf_lb.add_paragraph()
    p.text = txt
    p.font.name = "TH Sarabun PSK"
    p.font.size = Pt(10.5)
    p.font.bold = bold
    p.font.color.rgb = TEXT_DARK

# Section: พร้อมด้วย (Pill)
with_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col1_left, body_top + Inches(3.6), Inches(1.3), Inches(0.32))
with_pill.fill.solid()
with_pill.fill.fore_color.rgb = BLUE_ACCENT
with_pill.line.fill.background()
p = with_pill.text_frame.paragraphs[0]
p.text = "พร้อมด้วย"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# With Officers Text Box
with_box = slide.shapes.add_textbox(col1_left, body_top + Inches(3.95), col1_width, Inches(2.8))
tf_wb = with_box.text_frame
tf_wb.word_wrap = True
tf_wb.margin_left = tf_wb.margin_top = tf_wb.margin_right = tf_wb.margin_bottom = 0
with_lines = [
    ("เจ้าพนักงานตำรวจ กก.สืบสวน 3 บก.สส.ภ.2", True),
    ("ชุดจับกุมนำโดย", True),
    ("• พ.ต.ต.ภูทัย นรสิงห์", False),
    ("• ร.ต.อ.คมกฤษ สั้นหลาม", False),
    ("• ร.ต.ต.ณัฐ สอนตระกูล", False),
    ("• ด.ต.อภิชัย โกจินทึก", False),
    ("• ด.ต.ธฤต เดชธรรมฤทธิ์", False),
    ("• ด.ต.อรพร เปรมอำพล", False),
    ("• ส.ต.ท.ณัฐวุธ อินทรเรืองศรี", False)
]
for i, (txt, bold) in enumerate(with_lines):
    p = tf_wb.paragraphs[0] if i == 0 else tf_wb.add_paragraph()
    p.text = txt
    p.font.name = "TH Sarabun PSK"
    p.font.size = Pt(10)
    p.font.bold = bold
    p.font.color.rgb = TEXT_DARK

# --- RIGHT COLUMN: ARREST DETAILS & RESULTS ---
# Card 1: ผลการปฏิบัติ
cur_y = body_top
sec1_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col2_left, cur_y, Inches(1.8), Inches(0.35))
sec1_pill.fill.solid()
sec1_pill.fill.fore_color.rgb = NAVY_PILL
sec1_pill.line.fill.background()
p = sec1_pill.text_frame.paragraphs[0]
p.text = "🛡️  ผลการปฏิบัติ"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = WHITE

# Suspect details box
cur_y += Inches(0.4)
suspect_box = slide.shapes.add_textbox(col2_left, cur_y, col2_width, Inches(1.4))
tf_s = suspect_box.text_frame
tf_s.word_wrap = True
tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
s_lines = [
    ("👥 ร่วมกันทำการจับกุมตัว", True, NAVY_DARK, 12),
    ("• นางสาวนิตติญา หรือ เจน ชาเสน", True, TEXT_DARK, 12),
    ("   อายุ 40 ปี", False, TEXT_DARK, 11),
    ("   เลขบัตรประจำตัวประชาชน 1-490300033-36-7", False, TEXT_DARK, 11),
    ("   บ้านเลขที่ 113 ม.2 ต.เหล่าหมี", False, TEXT_DARK, 11),
    ("   อ.ดอนตาล จ.มุกดาหาร (ผู้ต้องหา)", True, NAVY_DARK, 11)
]
for i, (txt, bold, colr, sz) in enumerate(s_lines):
    p = tf_s.paragraphs[0] if i == 0 else tf_s.add_paragraph()
    p.text = txt
    p.font.name = "TH Sarabun PSK"
    p.font.size = Pt(sz)
    p.font.bold = bold
    p.font.color.rgb = colr

# Card 2: กระทำความผิดฐาน
cur_y += Inches(1.45)
sec2_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col2_left, cur_y, Inches(2.2), Inches(0.35))
sec2_pill.fill.solid()
sec2_pill.fill.fore_color.rgb = NAVY_PILL
sec2_pill.line.fill.background()
p = sec2_pill.text_frame.paragraphs[0]
p.text = "⚖️  กระทำความผิดฐาน"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = WHITE

cur_y += Inches(0.4)
charge_box = slide.shapes.add_textbox(col2_left, cur_y, col2_width, Inches(1.4))
tf_c = charge_box.text_frame
tf_c.word_wrap = True
tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
c_lines = [
    ("“ร่วมกันลักทรัพย์ในเวลากลางคืน โดยใช้ยานพาหนะ เพื่อสะดวกแก่การกระทำความผิดเพื่อการพาทรัพย์นั้นไป หรือเพื่อให้พ้นจากการจับกุม”", True, TEXT_DARK, 11),
    ("◆ (หมายจับศาลจังหวัดฉะเชิงเทรา ที่ 408/2569 ลง 5 พฤศจิกายน 2569)", False, NAVY_DARK, 10.5)
]
for i, (txt, bold, colr, sz) in enumerate(c_lines):
    p = tf_c.paragraphs[0] if i == 0 else tf_c.add_paragraph()
    p.text = txt
    p.font.name = "TH Sarabun PSK"
    p.font.size = Pt(sz)
    p.font.bold = bold
    p.font.color.rgb = colr

# Card 3: สถานที่จับกุม
cur_y += Inches(1.35)
sec3_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col2_left, cur_y, Inches(1.8), Inches(0.35))
sec3_pill.fill.solid()
sec3_pill.fill.fore_color.rgb = NAVY_PILL
sec3_pill.line.fill.background()
p = sec3_pill.text_frame.paragraphs[0]
p.text = "📍  สถานที่จับกุม"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = WHITE

cur_y += Inches(0.4)
loc_box = slide.shapes.add_textbox(col2_left, cur_y, col2_width, Inches(0.7))
tf_l = loc_box.text_frame
tf_l.word_wrap = True
tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0
p = tf_l.paragraphs[0]
p.text = "• บริเวณภายในบริษัท จั้มเวย์ จำกัด เลขที่ 1 ม.1 ต.หอมศีล อ.บางปะกง จ.ฉะเชิงเทรา"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(11)
p.font.bold = False
p.font.color.rgb = TEXT_DARK

# Card 4: การดำเนินการ
cur_y += Inches(0.7)
sec4_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col2_left, cur_y, Inches(1.8), Inches(0.35))
sec4_pill.fill.solid()
sec4_pill.fill.fore_color.rgb = NAVY_PILL
sec4_pill.line.fill.background()
p = sec4_pill.text_frame.paragraphs[0]
p.text = "📑  การดำเนินการ"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = WHITE

cur_y += Inches(0.4)
act_box = slide.shapes.add_textbox(col2_left, cur_y, col2_width, Inches(0.6))
tf_a = act_box.text_frame
tf_a.word_wrap = True
tf_a.margin_left = tf_a.margin_top = tf_a.margin_right = tf_a.margin_bottom = 0
p = tf_a.paragraphs[0]
p.text = "• นำส่ง พงส.สภ.บางปะกง จว.ฉะเชิงเทรา ดำเนินคดีต่อไป"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = TEXT_DARK

# ==================== PHOTOS SECTION ====================
photos_top = Inches(7.3)
photo_w = Inches(3.75)
photo_h = Inches(3.0)

# Photo 1 (Left)
if os.path.exists('photo_sample1.jpg'):
    slide.shapes.add_picture('photo_sample1.jpg', Inches(0.3), photos_top, width=photo_w, height=photo_h)
    # Watermark overlay on left photo
    wm = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), photos_top + Inches(2.45), Inches(2.55), Inches(0.48))
    wm.fill.solid()
    wm.fill.fore_color.rgb = RGBColor(20, 20, 20)
    wm.line.color.rgb = WHITE
    wm.line.width = Pt(1)
    tf_wm = wm.text_frame
    tf_wm.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf_wm.paragraphs[0]
    p.text = "งานสืบสวน สภ.บางปะกง"
    p.font.name = "TH Sarabun PSK"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    p2 = tf_wm.add_paragraph()
    p2.text = "BANGPAKONG INVESTIGATION"
    p2.font.name = "Arial"
    p2.font.size = Pt(7.5)
    p2.font.color.rgb = BLUE_LIGHT
    p2.alignment = PP_ALIGN.CENTER
else:
    p1_box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.3), photos_top, photo_w, photo_h)
    p1_box.fill.solid()
    p1_box.fill.fore_color.rgb = BG_LIGHT

# Photo 2 (Right)
if os.path.exists('photo_sample2.jpg'):
    slide.shapes.add_picture('photo_sample2.jpg', Inches(4.22), photos_top, width=photo_w, height=photo_h)
else:
    p2_box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.22), photos_top, photo_w, photo_h)
    p2_box.fill.solid()
    p2_box.fill.fore_color.rgb = BG_LIGHT

# "จึงเรียนมาเพื่อโปรดทราบ" Centered Text
closing_box = slide.shapes.add_textbox(Inches(1.0), Inches(10.35), Inches(6.27), Inches(0.35))
tf_cl = closing_box.text_frame
p_cl = tf_cl.paragraphs[0]
p_cl.text = "จึงเรียนมาเพื่อโปรดทราบ"
p_cl.font.name = "TH Sarabun PSK"
p_cl.font.size = Pt(16)
p_cl.font.bold = True
p_cl.font.color.rgb = NAVY_DARK
p_cl.alignment = PP_ALIGN.CENTER

# ==================== FOOTER SECTION ====================
footer_rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(10.8), Inches(8.27), Inches(0.89))
footer_rect.fill.solid()
footer_rect.fill.fore_color.rgb = NAVY_DARK
footer_rect.line.fill.background()

# Footer Slogan Left
f_slogan = slide.shapes.add_textbox(Inches(0.4), Inches(10.95), Inches(4.5), Inches(0.55))
tf_fs = f_slogan.text_frame
tf_fs.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf_fs.paragraphs[0]
p.text = "“ ปลอดภัย  ใกล้ชิด  ประชาชน ”"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = WHITE

# Footer Police Mascot & Station Info Right
f_info = slide.shapes.add_textbox(Inches(5.0), Inches(10.9), Inches(3.0), Inches(0.65))
tf_fi = f_info.text_frame
tf_fi.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf_fi.paragraphs[0]
p.text = "👮 สภ.บางปะกง"
p.font.name = "TH Sarabun PSK"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.RIGHT
p2 = tf_fi.add_paragraph()
p2.text = "ตำรวจภูธรจังหวัดฉะเชิงเทรา"
p2.font.name = "TH Sarabun PSK"
p2.font.size = Pt(11)
p2.font.color.rgb = BLUE_LIGHT
p2.alignment = PP_ALIGN.RIGHT

output_path = "รายงานผลการปฏิบัติ_สภ_บางปะกง.pptx"
prs.save(output_path)
print(f"Presentation saved successfully to {output_path}")

