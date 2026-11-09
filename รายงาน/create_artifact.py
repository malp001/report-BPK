import json

with open('assets_b64.json', 'r') as f:
    assets = json.load(f)

badge_b64 = assets['police_badge.png']
mascot_b64 = assets['police_mascot.png']
footer_banner_b64 = assets['footer_banner_bg.png']
p1_b64 = assets['photo_sample1.jpg']
p2_b64 = assets['photo_sample2.jpg']

artifact_html = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    [contenteditable="true"]:hover {{
      outline: 1px dashed #3b82f6;
      background-color: rgba(59, 130, 246, 0.08);
      border-radius: 2px;
    }}
    [contenteditable="true"]:focus {{
      outline: 2px solid #2563eb;
      background-color: rgba(59, 130, 246, 0.15);
      border-radius: 2px;
    }}
  </style>
</head>
<body class="bg-[var(--background)] text-[var(--foreground)] antialiased p-3 min-h-screen">
  <div class="max-w-3xl mx-auto space-y-4">
    
    <!-- Top Action Bar -->
    <div class="bg-[var(--card)] border border-[var(--border)] rounded-xl p-4 shadow-sm flex flex-wrap items-center justify-between gap-3">
      <div>
        <h2 class="text-base font-bold text-[var(--foreground)] flex items-center gap-2">
          <span>🚓</span> รายงานผลการปฏิบัติงาน (สภ.บางปะกง)
        </h2>
        <p class="text-xs text-[var(--muted-foreground)]">
          ตัดขอบตราสัญลักษณ์เรียบร้อยคมชัด และปรับให้แสดงผลเรียงลงมาด้านล่างบนจอมือถือ
        </p>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-xs bg-emerald-100 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300 px-2.5 py-1 rounded-full font-medium flex items-center gap-1">
          <span>✓</span> ตัดขอบตราโลโก้โปร่งใส
        </span>
        <span class="text-xs bg-blue-100 dark:bg-blue-950/60 text-blue-800 dark:text-blue-300 px-2.5 py-1 rounded-full font-medium flex items-center gap-1">
          <span>📱</span> รองรับจอมือถือ
        </span>
      </div>
    </div>

    <!-- The Report Poster Component -->
    <div class="relative bg-white text-slate-800 rounded-lg shadow-xl overflow-hidden border border-slate-200 text-sm">
      
      <!-- Watermark Emblem -->
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-80 h-80 opacity-[0.038] pointer-events-none z-0 flex items-center justify-center">
        <img src="{badge_b64}" alt="Police Watermark" class="w-full h-full object-contain grayscale-[15%]">
      </div>
      
      <!-- HEADER - Royal Navy & Gold Harmonized Theme -->
      <div class="bg-gradient-to-r from-[#031024] via-[#06193b] to-[#0a295c] text-white p-4 sm:p-5 relative overflow-hidden">
        <!-- Golden Aura behind Logo -->
        <div class="absolute -left-4 top-1/2 -translate-y-1/2 w-48 h-48 bg-radial from-amber-500/25 via-sky-400/10 to-transparent pointer-events-none z-0"></div>
        
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 relative z-10">
          <!-- Left Logo & Station Name -->
          <div class="flex items-center gap-3.5">
            <img src="{badge_b64}" alt="Police Badge" class="w-20 h-22 sm:w-24 sm:h-26 object-contain drop-shadow-[0_4px_10px_rgba(0,0,0,0.6)] drop-shadow-[0_0_8px_rgba(245,158,11,0.35)]">
            <div>
              <div class="text-xl sm:text-2xl font-black tracking-wide text-white leading-tight drop-shadow-md" contenteditable="true">
                สภ.บางปะกง
              </div>
              <div class="text-[11px] sm:text-xs font-bold tracking-widest text-sky-200 uppercase mt-0.5" contenteditable="true">
                BANGPAKONG POLICE STATION
              </div>
              <div class="mt-1.5 bg-gradient-to-r from-red-600 via-red-500 to-rose-500 text-white text-[11px] sm:text-xs font-bold px-3.5 py-0.5 rounded-full inline-block shadow-md border border-amber-400/80" contenteditable="true">
                “ดูแลทุกข์ สุขของประชาชน”
              </div>
            </div>
          </div>

          <!-- Right Pill & Date -->
          <div class="flex flex-row sm:flex-col items-center sm:items-end justify-between w-full sm:w-auto gap-2.5">
            <div class="bg-gradient-to-r from-[#051936] to-[#092758] border-1.5 border-amber-500 rounded-full px-4 py-1.5 text-center shadow-lg shadow-black/30 border border-amber-500">
              <div class="text-[11px] sm:text-xs font-extrabold text-white tracking-wide" contenteditable="true">รายงานผลการปฏิบัติ</div>
              <div class="text-[10px] sm:text-[11px] font-bold text-amber-300" contenteditable="true">ประจำวัน</div>
            </div>
            <div class="bg-white text-slate-800 rounded-xl px-2.5 py-1 sm:px-3 sm:py-1.5 border border-blue-200 border-l-4 border-l-amber-500 flex items-center gap-2 shadow-md">
              <span class="text-base sm:text-lg">📅</span>
              <div class="leading-tight">
                <div class="text-[11px] sm:text-xs font-bold text-[#0c2d5e]" contenteditable="true">วันที่ 9 พฤศจิกายน 2569</div>
                <div class="text-[10px] sm:text-[11px] text-slate-600 font-medium" contenteditable="true">เวลาประมาณ 11.00 น.</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Gold & Cyan Dual Swoosh Accent Ribbon at Bottom -->
        <div class="absolute bottom-0 left-0 right-0 h-3 pointer-events-none">
          <svg viewBox="0 0 720 12" preserveAspectRatio="none" class="w-full h-full block" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="artGoldRibbon" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#b45309"/>
                <stop offset="20%" stop-color="#f59e0b"/>
                <stop offset="50%" stop-color="#fef08a"/>
                <stop offset="80%" stop-color="#f59e0b"/>
                <stop offset="100%" stop-color="#d97706"/>
              </linearGradient>
            </defs>
            <path d="M0,2 Q180,-1 360,3 T720,1 L720,3 L0,3 Z" fill="#38bdf8" opacity="0.9"/>
            <path d="M0,3 Q160,0 340,4 T720,2 L720,12 L0,12 Z" fill="url(#artGoldRibbon)"/>
          </svg>
        </div>
      </div>

      <!-- BODY: 2 COLUMNS -->
      <div class="grid grid-cols-1 md:grid-cols-12 gap-4 p-4 sm:p-5 bg-white">
        
        <!-- LEFT COLUMN: COMMAND & TEAM -->
        <div class="md:col-span-5 space-y-3 border-b md:border-b-0 md:border-r border-slate-200 pb-3 md:pb-0 md:pr-3">
          
          <div class="flex items-start gap-2">
            <span class="text-lg">📋</span>
            <div>
              <div class="font-bold text-[#0c3166] text-xs sm:text-sm" contenteditable="true">เรียน ผู้บังคับบัญชา</div>
              <div class="font-bold text-[#0c3166] text-xs sm:text-sm" contenteditable="true">สภ.บางปะกง</div>
            </div>
          </div>

          <div>
            <div class="font-bold text-xs text-[#0c3166] mb-1.5">ภายใต้การอำนวยการของ</div>
            <div class="space-y-2">
              <div class="bg-gradient-to-r from-[#061e44] to-[#0a2d64] text-white rounded-full px-3 py-1.5 flex items-center gap-2 shadow-md border border-white/10">
                <div class="w-7 h-7 rounded-full bg-white text-[#061e44] flex items-center justify-center text-xs font-bold shrink-0 shadow-sm">👤</div>
                <div class="leading-tight min-w-0">
                  <div class="font-extrabold text-[13px] sm:text-[14px] text-white tracking-tight whitespace-nowrap" contenteditable="true">พ.ต.อ.บัณฑิต ธรรมอนันต์</div>
                  <div class="text-[11px] text-sky-200 font-semibold mt-0.5 whitespace-nowrap" contenteditable="true">ผกก.สภ.บางปะกง</div>
                </div>
              </div>
              <div class="bg-gradient-to-r from-[#061e44] to-[#0a2d64] text-white rounded-full px-3 py-1.5 flex items-center gap-2 shadow-md border border-white/10">
                <div class="w-7 h-7 rounded-full bg-white text-[#061e44] flex items-center justify-center text-xs font-bold shrink-0 shadow-sm">👤</div>
                <div class="leading-tight min-w-0">
                  <div class="font-extrabold text-[13px] sm:text-[14px] text-white tracking-tight whitespace-nowrap" contenteditable="true">พ.ต.ท.อำนาจ ยิ้มเนียม</div>
                  <div class="text-[11px] text-sky-200 font-semibold mt-0.5 whitespace-nowrap" contenteditable="true">รอง ผกก.ป.สภ.บางปะกง</div>
                </div>
              </div>
            </div>
          </div>

          <!-- นำโดย -->
          <div>
            <div class="bg-gradient-to-r from-[#061e44] to-[#0a2d64] text-white text-[12px] sm:text-[13px] font-bold px-3.5 py-1 rounded-full inline-block mb-1 shadow-sm border border-white/10">
              นำโดย
            </div>
            <div class="text-xs leading-relaxed space-y-0.5 text-slate-800" contenteditable="true">
              <div><strong>• พ.ต.ต.อัครเดช แก้วร่องคำ</strong></div>
              <div class="pl-3 text-slate-500">สวป.สภ.บางปะกง</div>
              <div><strong>• ร.ต.อ.วิโรจน์ เทศทอง</strong></div>
              <div class="pl-3 text-slate-500">รอง สวป. สภ.บางปะกง</div>
              <div class="pt-1 font-bold text-[#0c3166]"><strong>พร้อมกำลังสายตรวจ สภ.บางปะกง</strong></div>
            </div>
          </div>

          <!-- พร้อมด้วย (กำลังพลสายตรวจ 7 นาย) -->
          <div>
            <div class="bg-gradient-to-r from-[#061e44] to-[#0a2d64] text-white text-[12px] sm:text-[13px] font-bold px-3.5 py-1 rounded-full inline-block mb-1 shadow-sm border border-white/10">
              พร้อมด้วย
            </div>
            <div class="text-xs leading-relaxed text-slate-800 space-y-0.5" contenteditable="true">
              <div>• ส.ต.อ. อนุวัฒน์ บุตรทาสี</div>
              <div>• ส.ต.ท. สิทธิโชค วิวัฒนพงศ์พันธ์</div>
              <div>• ส.ต.ท. ทรงพล บุญไสย์</div>
              <div>• ส.ต.ท. กฤษดา บูรณะกิติ</div>
              <div>• ส.ต.ต. พัสกร อยู่ยืน</div>
              <div>• ส.ต.ต. จิตติ แสงสว่าง</div>
              <div>• ส.ต.ต. อนุชา พงษ์ราช</div>
            </div>
          </div>

        </div>

        <!-- RIGHT COLUMN: CASE DETAILS -->
        <div class="md:col-span-7 space-y-3">
          
          <!-- Card 1: ผลการปฏิบัติ -->
          <div class="space-y-1">
            <div class="bg-gradient-to-r from-[#061e44] to-[#0a2d64] text-white text-[12px] sm:text-[13px] font-bold px-3.5 py-1 rounded-full inline-flex items-center gap-1.5 shadow-sm border border-white/10">
              <span>🛡️</span> ผลการปฏิบัติ
            </div>
            <div class="pl-2 text-xs leading-relaxed">
              <div class="font-bold text-[#0c3166] flex items-center gap-1.5 text-xs">
                <span>👥</span> <span contenteditable="true">ร่วมกันทำการจับกุมตัว</span>
              </div>
              <div class="pl-3 space-y-0.5 mt-0.5" contenteditable="true">
                <div class="font-bold text-black">• นางสาวนิตติญา หรือ เจน ชาเสน</div>
                <div>อายุ 40 ปี</div>
                <div>เลขบัตรประจำตัวประชาชน 1-490300033-36-7</div>
                <div>บ้านเลขที่ 113 ม.2 ต.เหล่าหมี อ.ดอนตาล จ.มุกดาหาร <strong class="text-[#0c3166]">(ผู้ต้องหา)</strong></div>
              </div>
            </div>
          </div>

          <!-- Card 2: กระทำความผิดฐาน -->
          <div class="space-y-1">
            <div class="bg-gradient-to-r from-[#061e44] to-[#0a2d64] text-white text-[12px] sm:text-[13px] font-bold px-3.5 py-1 rounded-full inline-flex items-center gap-1.5 shadow-sm border border-white/10">
              <span>⚖️</span> กระทำความผิดฐาน
            </div>
            <div class="pl-2 text-xs leading-relaxed space-y-1" contenteditable="true">
              <div class="font-bold text-slate-900 leading-snug">
                “ร่วมกันลักทรัพย์ในเวลากลางคืน โดยใช้ยานพาหนะ เพื่อสะดวกแก่การกระทำความผิดเพื่อการพาทรัพย์นั้นไป หรือเพื่อให้พ้นจากการจับกุม”
              </div>
              <div class="text-[#0c3166] font-medium flex items-start gap-1">
                <span>◆</span> <span>(หมายจับศาลจังหวัดฉะเชิงเทรา ที่ 408/2569 ลง 5 พฤศจิกายน 2569)</span>
              </div>
            </div>
          </div>

          <!-- Card 3: สถานที่จับกุม -->
          <div class="space-y-1">
            <div class="bg-gradient-to-r from-[#061e44] to-[#0a2d64] text-white text-[12px] sm:text-[13px] font-bold px-3.5 py-1 rounded-full inline-flex items-center gap-1.5 shadow-sm border border-white/10">
              <span>📍</span> สถานที่จับกุม
            </div>
            <div class="pl-2 text-xs text-slate-800 leading-relaxed" contenteditable="true">
              • บริเวณภายในบริษัท จั้มเวย์ จำกัด เลขที่ 1 ม.1 ต.หอมศีล อ.บางปะกง จ.ฉะเชิงเทรา
            </div>
          </div>

          <!-- Card 4: การดำเนินการ -->
          <div class="space-y-1">
            <div class="bg-gradient-to-r from-[#061e44] to-[#0a2d64] text-white text-[12px] sm:text-[13px] font-bold px-3.5 py-1 rounded-full inline-flex items-center gap-1.5 shadow-sm border border-white/10">
              <span>📑</span> การดำเนินการ
            </div>
            <div class="pl-2 text-xs font-semibold text-slate-900 leading-relaxed" contenteditable="true">
              • นำส่ง พงส.สภ.บางปะกง จว.ฉะเชิงเทรา ดำเนินคดีต่อไป
            </div>
          </div>

        </div>

      </div>

      <!-- PHOTOS SECTION -->
      <div class="p-4 sm:p-5 pt-1 bg-white space-y-3">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <!-- Photo 1 -->
          <div class="relative rounded border border-slate-300 overflow-hidden bg-slate-100 aspect-[4/3]">
            <img src="{p1_b64}" alt="หลักฐานจับกุม 1" class="w-full h-full object-cover">
            <div class="absolute bottom-2 left-1/2 -translate-x-1/2 bg-slate-950/85 border border-white/70 px-3 py-1 rounded text-center text-white w-[88%]">
              <div class="text-[11px] font-bold leading-tight" contenteditable="true">งานสืบสวน สภ.บางปะกง</div>
              <div class="text-[9px] font-semibold text-sky-300 tracking-wider" contenteditable="true">BANGPAKONG INVESTIGATION</div>
            </div>
          </div>
          <!-- Photo 2 -->
          <div class="relative rounded border border-slate-300 overflow-hidden bg-slate-100 aspect-[4/3]">
            <img src="{p2_b64}" alt="หลักฐานจับกุม 2" class="w-full h-full object-cover">
          </div>
        </div>

      </div>

      <!-- Official Gold & Royal Navy Closing Banner -->
      <div class="relative w-full h-16 overflow-hidden flex items-center justify-center">
        <img src="{footer_banner_b64}" class="absolute inset-0 w-full h-full object-cover pointer-events-none z-10" alt="แถบปิดท้ายราชการ">
        <div class="relative z-20 font-bold text-base sm:text-lg text-white tracking-wider drop-shadow pb-0.5 text-center" contenteditable="true">
          จึงเรียนมาเพื่อโปรดทราบ
        </div>
      </div>

    </div>

  </div>
</body>
</html>'''

with open('C:/Users/Apcomzxx/.gemini/antigravity/brain/8af4d5e0-b0d9-4290-b5fb-354ad40427b0/report_preview.html', 'w', encoding='utf-8') as f:
    f.write(artifact_html)

print('Updated artifact report_preview.html successfully!')
