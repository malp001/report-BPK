import json

with open('assets_b64.json', 'r') as f:
    assets = json.load(f)

badge_b64 = assets['police_badge.png']
mascot_b64 = assets['police_mascot.png']
footer_banner_b64 = assets['footer_banner_bg.png']
p1_b64 = assets['photo_sample1.jpg']
p2_b64 = assets['photo_sample2.jpg']

with open('html2canvas.min.js', 'r', encoding='utf-8') as f:
    html2canvas_code = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>ระบบออกแบบและรายงานผลการปฏิบัติงาน - ตำรวจภูธร</title>
  <!-- Google Fonts: Sarabun & Prompt + Fallbacks -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700;800&family=Sarabun:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --police-navy: #051a3b;
      --police-navy-dark: #031024;
      --police-blue: #092758;
      --police-royal: #0d3b80;
      --police-accent: #2563eb;
      --police-sky: #0284c7;
      --police-cyan: #38bdf8;
      --police-red: #d91424;
      --police-pill: #0c3166;
      --bg-page: #0b1528;
      --text-dark: #0f172a;
      --text-muted: #64748b;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      font-family: 'Sarabun', 'TH Sarabun New', 'Leelawadee UI', Tahoma, -apple-system, sans-serif;
      background: radial-gradient(circle at 50% 12%, #14284b 0%, #0c1830 55%, #070e1c 100%);
      background-attachment: fixed;
      color: #0f172a;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      position: relative;
    }}

    body::before {{
      content: "";
      position: fixed;
      inset: 0;
      background-image: radial-gradient(rgba(56, 189, 248, 0.08) 1.2px, transparent 1.2px);
      background-size: 28px 28px;
      pointer-events: none;
      z-index: 0;
    }}

    /* Top Nav Bar */
    .top-navbar {{
      background: linear-gradient(90deg, #051838 0%, #082554 50%, #0b3472 100%);
      color: white;
      padding: 12px 24px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #38bdf8;
      box-shadow: 0 4px 18px rgba(0,0,0,0.35);
      position: sticky;
      top: 0;
      z-index: 100;
    }}
      padding: 12px 24px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      position: sticky;
      top: 0;
      z-index: 100;
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 1.15rem;
      font-weight: 700;
      font-family: 'Prompt', sans-serif;
    }}

    .nav-actions {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 600;
      font-family: 'Prompt', sans-serif;
      cursor: pointer;
      border: none;
      transition: all 0.2s ease;
      text-decoration: none;
      white-space: nowrap;
      user-select: none;
    }}

    .btn-primary {{
      background: #2563eb;
      color: white;
    }}
    .btn-primary:hover {{
      background: #1d4ed8;
      transform: translateY(-1px);
    }}

    .btn-success {{
      background: #059669;
      color: white;
    }}
    .btn-success:hover {{
      background: #047857;
      transform: translateY(-1px);
    }}

    .btn-secondary {{
      background: rgba(255,255,255,0.15);
      color: white;
      border: 1px solid rgba(255,255,255,0.25);
    }}
    .btn-secondary:hover {{
      background: rgba(255,255,255,0.25);
    }}

    .btn-warning {{
      background: #f59e0b;
      color: #1e293b;
    }}
    .btn-warning:hover {{
      background: #d97706;
      color: white;
    }}

    .btn-line {{
      background: #06c755;
      color: white;
    }}
    .btn-line:hover {{
      background: #05a847;
      transform: translateY(-1px);
    }}

    /* Main Container Layout */
    .app-layout {{
      display: flex;
      flex: 1;
      padding: 20px;
      gap: 24px;
      max-width: 1600px;
      margin: 0 auto;
      width: 100%;
    }}

    /* Left Sidebar: Controls & Inputs */
    .sidebar-panel {{
      width: 440px;
      flex-shrink: 0;
      background: white;
      border-radius: 16px;
      padding: 20px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.06);
      max-height: calc(100vh - 90px);
      overflow-y: auto;
    }}

    .panel-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 2px solid #f1f5f9;
    }}

    .panel-title {{
      font-family: 'Prompt', sans-serif;
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--police-navy);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* Preset Box */
    .preset-box {{
      background: #f1f5f9;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 12px;
      margin-bottom: 14px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .preset-label {{
      font-size: 0.82rem;
      font-weight: 700;
      color: #1e293b;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .preset-select {{
      width: 100%;
      padding: 8px 10px;
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      font-size: 0.86rem;
      font-family: inherit;
      background: white;
      color: #0f172a;
      cursor: pointer;
      font-weight: 600;
    }}
    .preset-select:focus {{
      outline: none;
      border-color: #2563eb;
    }}

    .accordion-section {{
      margin-bottom: 12px;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      overflow: hidden;
    }}

    .accordion-header {{
      background: #f8fafc;
      padding: 12px 16px;
      font-weight: 600;
      font-size: 0.92rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
      color: #1e293b;
    }}
    .accordion-header:hover {{
      background: #f1f5f9;
    }}

    .accordion-content {{
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      background: white;
    }}

    .form-group {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .form-label {{
      font-size: 0.82rem;
      font-weight: 600;
      color: #475569;
    }}

    .form-control {{
      padding: 8px 12px;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      font-size: 0.88rem;
      font-family: inherit;
      color: #1e293b;
      transition: border-color 0.2s;
    }}
    .form-control:focus {{
      outline: none;
      border-color: #2563eb;
      box-shadow: 0 0 0 2px rgba(37,99,235,0.15);
    }}

    textarea.form-control {{
      min-height: 70px;
      resize: vertical;
      line-height: 1.4;
    }}

    .form-row {{
      display: flex;
      gap: 10px;
    }}
    .form-row > * {{
      flex: 1;
    }}

    /* Preview Canvas Area */
    .preview-panel {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      gap: 12px;
      width: 100%;
      min-width: 0;
    }}

    .preview-tip {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1e40af;
      padding: 10px 16px;
      border-radius: 12px;
      font-size: 0.85rem;
      display: flex;
      align-items: center;
      gap: 8px;
      max-width: 720px;
      width: 100%;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}

    /* Scale container: guarantees zero horizontal overflow on mobile */
    .poster-scale-wrapper {{
      width: 100%;
      max-width: 720px;
      overflow: hidden;
      position: relative;
      margin: 0 auto;
      box-sizing: border-box;
      background: transparent;
    }}

    .poster-scale-container {{
      width: 720px;
      position: relative;
      left: 50%;
      margin-left: -360px;
      transform-origin: top center;
      transition: transform 0.1s ease-out;
    }}

    .officer-item strong, .bold-line strong, .bold-line {{
      font-weight: 700 !important;
      color: #0c3166;
    }}

    /* Fullscreen Preview Modal */
    .preview-modal {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(10, 20, 35, 0.94);
      backdrop-filter: blur(5px);
      z-index: 99999;
      display: flex;
      flex-direction: column;
      padding: 10px;
      box-sizing: border-box;
    }}
    .preview-modal-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 14px;
      background: #0f172a;
      border-radius: 8px;
      margin-bottom: 8px;
      border: 1px solid #334155;
    }}
    .preview-modal-content {{
      flex: 1;
      overflow: auto;
      -webkit-overflow-scrolling: touch;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      padding: 10px 0;
    }}

    /* ========================================================
       THE EXACT REPORT INFOGRAPHIC POSTER
       ======================================================== */
    .poster-wrapper {{
      width: 720px;
      background: #ffffff;
      box-shadow: 0 16px 50px rgba(0,0,0,0.45);
      border-radius: 6px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      position: relative;
      font-family: 'Sarabun', 'TH Sarabun New', Tahoma, sans-serif;
      border: 1px solid rgba(255,255,255,0.2);

      /* Dynamic Typography Scaling */
      --fs-global: 1;
      --fs-charge-scale: 1;
      --fs-officers-scale: 1;
      --fs-station-scale: 1;
    }}

    /* Official Watermark Background */
    .poster-watermark {{
      position: absolute;
      top: 48%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 370px;
      height: 370px;
      opacity: 0.038;
      pointer-events: none;
      z-index: 1;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .poster-watermark img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      filter: grayscale(15%);
    }}

    /* 1. Header Banner - FIXED: Generous space, clean cyan bottom border, zero clipping / no "ขอบตก" */
    /* 1. Header Section - Royal Navy & Gold Harmonized Theme */
    .poster-header {{
      background: linear-gradient(135deg, #031024 0%, #06193b 35%, #0a295c 70%, #082046 100%);
      color: white;
      padding: 20px 24px 26px 24px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 4px 16px rgba(3, 16, 36, 0.4);
    }}

    /* Subtle geometric mesh background pattern */
    .header-bg-pattern {{
      position: absolute;
      inset: 0;
      background-image: 
        radial-gradient(circle at 85% 25%, rgba(56, 189, 248, 0.08) 0%, transparent 45%),
        linear-gradient(45deg, rgba(255,255,255,0.02) 25%, transparent 25%),
        linear-gradient(-45deg, rgba(255,255,255,0.02) 25%, transparent 25%);
      background-size: 100% 100%, 24px 24px, 24px 24px;
      pointer-events: none;
      z-index: 1;
    }}

    /* Radiant Golden Halo behind the Emblem */
    .header-badge-glow {{
      position: absolute;
      left: -10px;
      top: 50%;
      transform: translateY(-50%);
      width: 190px;
      height: 190px;
      background: radial-gradient(circle, rgba(245, 158, 11, 0.28) 0%, rgba(56, 189, 248, 0.12) 40%, transparent 72%);
      pointer-events: none;
      z-index: 1;
    }}

    /* Dual Gold & Cyan Swoosh Ribbon at Header Bottom (Harmonized with bottom banner) */
    .header-gold-ribbon-bar {{
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 14px;
      pointer-events: none;
      z-index: 5;
    }}

    .header-content {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
      width: 100%;
      z-index: 2;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .badge-container {{
      position: relative;
      cursor: pointer;
      flex-shrink: 0;
      z-index: 2;
    }}

    /* Clean cut badge with transparent background & radiant gold drop shadow */
    .police-badge-img {{
      width: 104px;
      height: 114px;
      object-fit: contain;
      filter: drop-shadow(0 6px 12px rgba(0,0,0,0.55)) drop-shadow(0 0 10px rgba(245, 158, 11, 0.4));
      display: block;
      transition: transform 0.2s ease;
    }}
    .badge-container:hover .police-badge-img {{
      transform: scale(1.03);
    }}

    .badge-edit-hint {{
      position: absolute;
      inset: 0;
      background: rgba(0,0,0,0.65);
      border-radius: 50%;
      display: none;
      align-items: center;
      justify-content: center;
      font-size: 0.72rem;
      color: white;
      text-align: center;
      padding: 4px;
      font-weight: 600;
    }}
    .badge-container:hover .badge-edit-hint {{
      display: flex;
    }}

    .station-title-box {{
      display: flex;
      flex-direction: column;
      gap: 3px;
    }}

    .station-main-name {{
      font-family: 'Prompt', sans-serif;
      font-size: calc(2.25rem * var(--fs-global) * var(--fs-station-scale));
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.8px;
      line-height: 1.15;
      text-shadow: 0 2px 6px rgba(0,0,0,0.65), 0 0 20px rgba(56, 189, 248, 0.3);
    }}

    .station-en-name {{
      font-family: 'Prompt', sans-serif;
      font-size: calc(0.82rem * var(--fs-global) * var(--fs-station-scale));
      font-weight: 700;
      letter-spacing: 1.5px;
      color: #bae6fd;
      margin: 1px 0 4px 0;
      text-shadow: 0 1px 3px rgba(0,0,0,0.5);
    }}

    .station-slogan-ribbon {{
      background: linear-gradient(90deg, #b91c1c 0%, #dc2626 50%, #ef4444 100%);
      color: white;
      font-family: 'Prompt', sans-serif;
      font-size: 0.92rem;
      font-weight: 700;
      padding: 4px 20px;
      border-radius: 20px;
      border: 1.5px solid #fbbf24;
      display: inline-block;
      width: fit-content;
      box-shadow: 0 3px 8px rgba(185, 28, 28, 0.45), 0 0 10px rgba(251, 191, 36, 0.3);
    }}

    .header-right {{
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 9px;
      flex-shrink: 0;
    }}

    .report-type-pill {{
      background: linear-gradient(135deg, #051936 0%, #092758 100%);
      border: 1.5px solid #f59e0b;
      border-radius: 22px;
      padding: 7px 20px;
      text-align: center;
      box-shadow: 0 4px 12px rgba(0,0,0,0.35), 0 0 10px rgba(245, 158, 11, 0.25);
    }}

    .report-title-main {{
      font-family: 'Prompt', sans-serif;
      font-size: 0.98rem;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.2;
      letter-spacing: 0.3px;
    }}

    .report-title-sub {{
      font-size: 0.88rem;
      font-weight: 700;
      color: #fde047;
      margin-top: 1px;
    }}

    .date-card {{
      background: #ffffff;
      color: #0f172a;
      border-radius: 12px;
      padding: 6px 14px;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
      border: 1.5px solid #bfdbfe;
      border-left: 5px solid #f59e0b;
    }}

    .date-icon {{
      font-size: 1.55rem;
      color: #0284c7;
    }}

    .date-info {{
      display: flex;
      flex-direction: column;
      line-height: 1.25;
    }}

    .date-text {{
      font-family: 'Prompt', sans-serif;
      font-size: 0.82rem;
      font-weight: 700;
      color: #0c2d5e;
    }}

    .time-text {{
      font-size: 0.78rem;
      font-weight: 600;
      color: #334155;
    }}

    /* 2. Body Section: Two Columns */
    .poster-body {{
      display: flex;
      padding: 16px 18px 8px 18px;
      gap: 16px;
      background: linear-gradient(180deg, #ffffff 0%, #fcfdfe 100%);
      border-bottom: 1px solid #e2e8f0;
      position: relative;
      z-index: 2;
    }}

    /* Left Column: Officers & Command */
    .body-col-left {{
      width: 43%;
      display: flex;
      flex-direction: column;
      gap: 12px;
      border-right: 1.5px dashed #cbd5e1;
      padding-right: 12px;
    }}

    .cmd-greeting {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }}

    .cmd-icon {{
      width: 24px;
      height: 24px;
      fill: #0c3166;
      flex-shrink: 0;
      margin-top: 2px;
    }}

    .cmd-greeting-text {{
      font-family: 'Prompt', sans-serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: #0c3166;
      line-height: 1.25;
    }}

    .under-command-label {{
      font-size: 0.86rem;
      font-weight: 700;
      color: #0c3166;
      margin-top: 2px;
    }}

    .commander-list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .commander-card {{
      background: linear-gradient(90deg, #061e44 0%, #0a2d64 100%);
      color: white;
      border-radius: 24px;
      padding: 6px 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 3px 8px rgba(6,30,68,0.28);
      border: 1px solid rgba(255, 255, 255, 0.12);
    }}

    .commander-avatar {{
      width: 28px;
      height: 28px;
      background: #ffffff;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #061e44;
      font-size: 0.92rem;
      flex-shrink: 0;
      box-shadow: 0 2px 4px rgba(0,0,0,0.15);
    }}

    .commander-info {{
      display: flex;
      flex-direction: column;
      line-height: 1.25;
      min-width: 0;
    }}

    .commander-name {{
      font-family: 'Prompt', sans-serif;
      font-size: calc(0.96rem * var(--fs-global) * var(--fs-officers-scale));
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.1px;
      white-space: nowrap;
    }}

    .commander-pos {{
      font-size: calc(0.80rem * var(--fs-global) * var(--fs-officers-scale));
      font-weight: 600;
      color: #bae6fd;
      margin-top: 1px;
      white-space: nowrap;
    }}

    /* Section Headers Unified Dark Navy Badges (ตามรูปที่ 2: #08244f) */
    .section-lead-pill,
    .section-joint-pill,
    .case-card-header {{
      background: linear-gradient(90deg, #061e44 0%, #0a2d64 100%);
      color: white;
      font-family: 'Prompt', sans-serif;
      font-size: calc(0.92rem * var(--fs-global));
      font-weight: 700;
      padding: 4px 16px;
      border-radius: 18px;
      width: fit-content;
      margin-bottom: 5px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 2px 6px rgba(6, 30, 68, 0.25);
      border: 1px solid rgba(255, 255, 255, 0.12);
    }}

    .officers-card-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 7px 10px;
    }}

    .officers-block {{
      font-size: calc(0.84rem * var(--fs-global) * var(--fs-officers-scale));
      line-height: 1.5;
      color: #1e293b;
    }}

    .officer-item {{
      margin-bottom: 2px;
      font-size: inherit;
    }}
    .officer-item strong {{
      font-weight: 700;
      color: #0f172a;
    }}

    .officers-subgroup-title {{
      font-weight: 700;
      color: #0c3166;
      font-size: calc(0.84rem * var(--fs-global) * var(--fs-officers-scale));
      margin-top: 4px;
      margin-bottom: 2px;
    }}

    /* Right Column: Case Details */
    .body-col-right {{
      width: 57%;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .case-card {{
      display: flex;
      flex-direction: column;
      gap: 5px;
      background: #ffffff;
      border: 1px solid #eef2f6;
      border-radius: 8px;
      padding: 8px 10px;
      box-shadow: 0 1px 4px rgba(12, 49, 102, 0.03);
    }}

    .case-card-body {{
      padding-left: 6px;
      font-size: calc(0.84rem * var(--fs-global));
      line-height: 1.5;
      color: #1e293b;
    }}

    .suspect-headline {{
      font-family: 'Prompt', sans-serif;
      font-size: calc(0.84rem * var(--fs-global));
      font-weight: 700;
      color: #0c3166;
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 2px;
    }}

    .suspect-name {{
      font-size: calc(0.84rem * var(--fs-global));
      font-weight: 700;
      color: #000000;
    }}

    .charge-quote {{
      font-family: 'Prompt', sans-serif;
      font-weight: 700;
      font-size: calc(0.84rem * var(--fs-global) * var(--fs-charge-scale));
      color: #0f172a;
      line-height: 1.4;
      margin-bottom: 3px;
    }}

    .warrant-badge {{
      font-size: calc(0.84rem * var(--fs-global) * var(--fs-charge-scale));
      color: #0c3166;
      font-weight: 600;
      display: flex;
      align-items: flex-start;
      gap: 4px;
    }}

    /* Evidence Box (Optional) */
    .evidence-box {{
      display: none;
      flex-direction: column;
      gap: 4px;
    }}
    .evidence-box.active {{
      display: flex;
    }}

    /* 3. Photos Section */
    .poster-photos {{
      padding: 10px 18px 12px 18px;
      background: #ffffff;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    /* Photo Grid & Frame */
    .photos-grid {{
      display: grid;
      gap: 12px;
    }}
    .photos-grid.layout-2 {{
      grid-template-columns: 1fr 1fr;
    }}
    .photos-grid.layout-1 {{
      grid-template-columns: 1fr;
    }}

    .photo-frame {{
      position: relative;
      border: 1.5px solid #94a3b8;
      border-radius: 6px;
      overflow: hidden;
      aspect-ratio: 4 / 3.3;
      min-height: 220px;
      background: #f8fafc;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .photo-frame.active-slot {{
      border-color: #0284c7;
      box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.25);
    }}
    .photo-frame:hover {{
      border-color: #0284c7;
    }}

    /* Empty Photo Placeholder Box */
    .photo-placeholder {{
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
      border: 2px dashed #94a3b8;
      border-radius: 6px;
      padding: 16px;
      text-align: center;
      box-sizing: border-box;
      transition: all 0.2s ease;
      cursor: pointer;
    }}
    .photo-frame:hover .photo-placeholder, .photo-frame.drag-over .photo-placeholder {{
      border-color: #0284c7;
      background: #f0f9ff;
    }}
    .placeholder-icon {{
      font-size: 2.4rem;
      margin-bottom: 6px;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.06));
    }}
    .placeholder-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: #0c3166;
      margin-bottom: 2px;
    }}
    .placeholder-sub {{
      font-size: 0.72rem;
      color: #64748b;
      margin-bottom: 10px;
    }}
    .placeholder-btn {{
      font-size: 0.75rem;
      font-weight: 600;
      color: #0284c7;
      background: #ffffff;
      border: 1px solid #7dd3fc;
      padding: 4px 12px;
      border-radius: 14px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
      transition: background 0.15s, color 0.15s;
    }}
    .photo-frame:hover .placeholder-btn {{
      background: #0284c7;
      color: #ffffff;
    }}

    .photo-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: none;
      transition: filter 0.2s;
    }}

    .photo-frame.has-photo:hover .photo-overlay-edit {{
      display: flex;
    }}

    .photo-overlay-edit {{
      position: absolute;
      inset: 0;
      background: rgba(15, 23, 42, 0.65);
      color: white;
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      font-weight: 600;
      gap: 8px;
      text-align: center;
      padding: 10px;
      z-index: 5;
    }}

    .photo-watermark {{
      position: absolute;
      bottom: 8px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(15, 23, 42, 0.88);
      border: 1px solid rgba(255,255,255,0.7);
      padding: 4px 12px;
      border-radius: 4px;
      text-align: center;
      color: white;
      width: 85%;
      box-shadow: 0 2px 6px rgba(0,0,0,0.5);
      pointer-events: none;
    }}

    .watermark-th {{
      font-family: 'Prompt', sans-serif;
      font-size: 0.76rem;
      font-weight: 700;
      line-height: 1.15;
    }}

    .watermark-en {{
      font-size: 0.62rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: #93c5fd;
    }}

    /* 4. Official Stepped Gold & Navy Closing Banner */
    .poster-closing-banner {{
      position: relative;
      width: 100%;
      height: 64px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 2;
      background: transparent;
    }}

    .closing-banner-bg {{
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      pointer-events: none;
      z-index: 1;
    }}

    .closing-banner-text {{
      position: relative;
      z-index: 2;
      font-family: 'Prompt', sans-serif;
      font-size: calc(1.25rem * var(--fs-global));
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 0.8px;
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.45);
      padding-bottom: 2px;
      text-align: center;
    }}

    .poster-closing {{
      text-align: center;
      font-family: 'Prompt', sans-serif;
      font-size: 1.25rem;
      font-weight: 800;
      color: #0c1e38;
      padding: 14px 0 14px 0;
      letter-spacing: 0.6px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      z-index: 2;
    }}

    /* 5. Footer Banner */
    .poster-footer {{
      background: linear-gradient(90deg, #00194a 0%, #002875 52%, #0c3870 100%);
      color: white;
      padding: 10px 22px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
      border-top: 3px solid #38bdf8;
      box-shadow: 0 -2px 10px rgba(0, 25, 74, 0.2);
      z-index: 2;
    }}

    .footer-slogan {{
      font-family: 'Prompt', sans-serif;
      font-size: 1.08rem;
      font-weight: 700;
      font-style: italic;
      color: #ffffff;
      letter-spacing: 1px;
      text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }}

    .footer-divider-slash {{
      display: flex;
      align-items: center;
      gap: 5px;
      height: 36px;
    }}
    .slash-line {{
      display: inline-block;
      height: 32px;
      background: #38bdf8;
      transform: skewX(-25deg);
      border-radius: 2px;
      box-shadow: 0 0 8px rgba(56, 189, 248, 0.7);
    }}
    .slash-line.s1 {{
      width: 4px;
    }}
    .slash-line.s2 {{
      width: 2.5px;
      opacity: 0.65;
    }}

    .footer-station-info {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-align: right;
    }}

    .footer-mascot-img {{
      width: 44px;
      height: 44px;
      object-fit: contain;
      filter: drop-shadow(0 2px 5px rgba(0,0,0,0.45));
    }}

    .footer-text-block {{
      display: flex;
      flex-direction: column;
      text-align: left;
    }}

    .footer-station-name {{
      font-family: 'Prompt', sans-serif;
      font-size: 0.96rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.2;
      text-shadow: 0 1px 3px rgba(0,0,0,0.4);
    }}

    .footer-province-name {{
      font-family: 'Sarabun', sans-serif;
      font-size: 0.78rem;
      font-weight: 600;
      color: #7dd3fc;
      line-height: 1.2;
    }}

    /* Contenteditable Highlighting */
    [contenteditable="true"] {{
      outline: none;
      transition: background 0.15s, box-shadow 0.15s;
      border-radius: 2px;
      padding: 0 1px;
    }}
    [contenteditable="true"]:hover {{
      background: rgba(37, 99, 235, 0.08);
      outline: 1px dashed rgba(37, 99, 235, 0.4);
    }}
    [contenteditable="true"]:focus {{
      background: rgba(37, 99, 235, 0.15);
      outline: 2px solid #2563eb;
    }}

    /* Responsive Mobile Layout */
    @media screen and (max-width: 1024px) {{
      .app-layout {{
        flex-direction: column !important;
        padding: 10px !important;
        gap: 16px !important;
      }}

      .sidebar-panel {{
        width: 100% !important;
        max-height: none !important;
        order: 1 !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06) !important;
        padding: 16px !important;
      }}

      .preview-panel {{
        width: 100% !important;
        order: 2 !important;
        margin-top: 10px;
        padding-top: 16px;
        border-top: 2px dashed #cbd5e1;
      }}

      .top-navbar {{
        padding: 10px 14px;
      }}
      .nav-brand {{
        font-size: 1rem;
        width: 100%;
        margin-bottom: 8px;
        justify-content: center;
      }}
      .nav-actions {{
        width: 100%;
        justify-content: center;
        gap: 6px;
      }}
      .btn {{
        padding: 6px 12px;
        font-size: 0.8rem;
      }}
    }}

    /* Print styles */
    @media print {{
      body {{
        background: transparent;
      }}
      .top-navbar, .sidebar-panel, .preview-tip, .mobile-jump-btn-box, .preview-header-bar {{
        display: none !important;
      }}
      .app-layout {{
        padding: 0;
        margin: 0;
        display: block;
      }}
      .preview-panel {{
        width: 100%;
        padding: 0;
        margin: 0;
        border: none;
      }}
      .poster-scale-wrapper, .poster-scale-container {{
        width: 100% !important;
        max-width: 100% !important;
        height: auto !important;
        overflow: visible !important;
      }}
      .poster-wrapper {{
        box-shadow: none;
        width: 100% !important;
        max-width: 100% !important;
        transform: none !important;
      }}
    }}

    .hidden-file-input {{
      display: none;
    }}

    /* Toast notification */
    #toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #1e293b;
      color: white;
      padding: 12px 20px;
      border-radius: 8px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.25);
      font-family: 'Prompt', sans-serif;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 10px;
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.3s ease;
      z-index: 1000;
      pointer-events: none;
    }}
    #toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}
  </style>
</head>
<body>

  <!-- Top Navigation Toolbar -->
  <header class="top-navbar">
    <div class="nav-brand">
      <span>🚓</span> ระบบสร้างรายงานผลการปฏิบัติงาน (ตำรวจภูธร)
    </div>
    <div class="nav-actions">
      <button class="btn btn-line" onclick="copyLineText()" title="คัดลอกข้อความสรุปพร้อมส่งใน LINE">
        📋 คัดลอกส่ง LINE
      </button>
      <button class="btn btn-secondary" onclick="saveDraftJSON()" title="บันทึกข้อมูลร่างเก็บไว้">
        💾 เซฟแบบร่าง
      </button>
      <button class="btn btn-secondary" onclick="document.getElementById('jsonFileInput').click()" title="โหลดข้อมูลร่างเดิม">
        📂 โหลดแบบร่าง
      </button>
      <input type="file" id="jsonFileInput" class="hidden-file-input" accept=".json" onchange="loadDraftJSON(event)">
      <button class="btn btn-warning" onclick="resetToSample()">
        🔄 รีเซ็ต
      </button>
      <button class="btn btn-primary" onclick="printReport()">
        🖨️ พิมพ์/PDF
      </button>
      <button class="btn btn-success" id="exportBtn" onclick="exportToImage()">
        📸 บันทึกรูป (PNG)
      </button>
    </div>
  </header>

  <!-- App Main Layout -->
  <main class="app-layout">
    
    <!-- 1. FORM INPUTS (Comes FIRST on mobile) -->
    <aside class="sidebar-panel" id="sidebarPanel">
      <div class="panel-header">
        <div class="panel-title">
          <span>⚙️</span> กรอกข้อมูลรายงาน
        </div>
        <a href="#previewSection" class="btn btn-primary" style="font-size: 0.78rem; padding: 4px 10px;">
          ดูภาพตัวอย่างด้านล่าง ▼
        </a>
      </div>

      <!-- Quick Case Preset -->
      <div class="preset-box">
        <span class="preset-label">⚡ เลือกประเภทคดีด่วน (เปลี่ยนข้อหา/หัวข้ออัตโนมัติ):</span>
        <select class="preset-select" id="casePresetSelect" onchange="applyPreset(this.value)">
          <option value="warrant">🎯 คดีจับกุมตามหมายจับ (ลักทรัพย์กลางคืน - ตัวอย่าง)</option>
          <option value="drugs">💊 คดียาเสพติดให้โทษ (ยาบ้า / ไอซ์ พร้อมของกลาง)</option>
          <option value="weapons">🔫 คดี พ.ร.บ.อาวุธปืน และเครื่องกระสุนปืน</option>
          <option value="theft">🛵 คดีลักทรัพย์ / ชิงทรัพย์ / วิ่งราวทรัพย์</option>
          <option value="gambling">🎲 คดีการพนัน / บาคาร่าออนไลน์</option>
          <option value="patrol">🚨 งานป้องกันปราบปราม / ตั้งจุดสกัดกวดขัน</option>
        </select>
      </div>

      <!-- 1. ข้อมูลสถานีและหัวข้อ -->
      <div class="accordion-section">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>🏢 1. ข้อมูลสถานีและวันที่</span>
          <span>▼</span>
        </div>
        <div class="accordion-content">
          <div class="form-group">
            <label class="form-label">ชื่อสถานี (ภาษาไทย) *เปลี่ยนแล้วจะอัปเดตทุกจุดอัตโนมัติ</label>
            <input type="text" id="input_station_th" class="form-control" value="สภ.บางปะกง" oninput="handleStationThChange(this.value)">
          </div>
          <div class="form-group">
            <label class="form-label">ชื่อสถานี (ภาษาอังกฤษ)</label>
            <input type="text" id="input_station_en" class="form-control" value="BANGPAKONG POLICE STATION" oninput="handleStationEnChange(this.value)">
          </div>
          <div class="form-group">
            <label class="form-label">สโลแกนใต้ชื่อสถานี</label>
            <input type="text" id="input_slogan_top" class="form-control" value="“ดูแลทุกข์ สุขของประชาชน”" oninput="syncField('slogan_top', this.value)">
          </div>
          <div class="form-row">
            <div class="form-group">
              <label class="form-label">หัวข้อรายงาน</label>
              <input type="text" id="input_report_title" class="form-control" value="รายงานผลการปฏิบัติ" oninput="syncField('report_title', this.value)">
            </div>
            <div class="form-group">
              <label class="form-label">ประเภทรอบ</label>
              <input type="text" id="input_report_sub" class="form-control" value="ประจำวัน" oninput="syncField('report_sub', this.value)">
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label class="form-label">วันที่ปฏิบัติงาน</label>
              <input type="text" id="input_report_date" class="form-control" value="วันที่ 9 พฤศจิกายน 2569" oninput="syncField('report_date', this.value)">
            </div>
            <div class="form-group">
              <label class="form-label">เวลาประมาณ</label>
              <input type="text" id="input_report_time" class="form-control" value="เวลาประมาณ 11.00 น." oninput="syncField('report_time', this.value)">
            </div>
          </div>
          <div class="form-group">
            <label class="form-label">เปลี่ยนตราสัญลักษณ์ สภ.</label>
            <input type="file" accept="image/*" class="form-control" onchange="handleBadgeUpload(event)">
          </div>
        </div>
      </div>

      <!-- 2. ผู้บังคับบัญชา & ทีมงาน -->
      <div class="accordion-section">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>👮 2. ผู้บังคับบัญชา และกำลังชุดจับกุม</span>
          <span>▼</span>
        </div>
        <div class="accordion-content">
          <div class="form-group">
            <label class="form-label">เรียน</label>
            <input type="text" id="input_cmd_to" class="form-control" value="เรียน ผู้บังคับบัญชา" oninput="syncField('cmd_to', this.value)">
          </div>
          <div class="form-group">
            <label class="form-label">ผู้บังคับบัญชา 1 (ชื่อ-ยศ)</label>
            <input type="text" id="input_cmd1_name" class="form-control" value="พ.ต.อ.บัณฑิต ธรรมอนันต์" oninput="syncField('cmd1_name', this.value)">
            <label class="form-label" style="margin-top:4px;">ตำแหน่ง</label>
            <input type="text" id="input_cmd1_pos" class="form-control" value="ผกก.สภ.บางปะกง" oninput="syncField('cmd1_pos', this.value)">
          </div>
          <div class="form-group">
            <label class="form-label">ผู้บังคับบัญชา 2 (ชื่อ-ยศ)</label>
            <input type="text" id="input_cmd2_name" class="form-control" value="พ.ต.ท.อำนาจ ยิ้มเนียม" oninput="syncField('cmd2_name', this.value)">
            <label class="form-label" style="margin-top:4px;">ตำแหน่ง</label>
            <input type="text" id="input_cmd2_pos" class="form-control" value="รอง ผกก.ป.สภ.บางปะกง" oninput="syncField('cmd2_pos', this.value)">
          </div>
          <!-- 3 ตัวเลือกหัวหน้าชุดปฏิบัติการ (นำโดย) -->
          <div class="form-group" style="background:#f0f9ff; padding:10px 12px; border-radius:8px; border:1.5px solid #7dd3fc; margin-bottom:10px;">
            <label class="form-label" style="font-weight:700; color:#0369a1; margin-bottom:4px; display:flex; align-items:center; gap:6px;">
              <span>👮</span> เลือกหัวหน้าชุดปฏิบัติการ (นำโดย):
            </label>
            <select id="select_lead_commander" class="form-control" style="font-weight:600; background:#ffffff; border:1px solid #38bdf8;" onchange="selectLeadCommander(this.value)">
              <option value="1">1. พ.ต.ต.อัครเดช แก้วร่องคำ (ตำแหน่ง สวป.สภ.บางปะกง)</option>
              <option value="2">2. พ.ต.ท.ชวกร บุษมงคล (ตำแหน่ง สว.(สอบสวน) สภ.บางปะกง)</option>
              <option value="3">3. พ.ต.ท.นิสิต ศรีโคตร (ตำแหน่ง สวป.(ชส) สภ.บางปะกง)</option>
            </select>
            <div style="display:flex; gap:4px; margin-top:6px; flex-wrap:wrap;">
              <button type="button" class="btn btn-sm" onclick="selectLeadCommander('1'); document.getElementById('select_lead_commander').value='1';" style="font-size:0.72rem; padding:3px 8px; background:#ffffff; color:#0369a1; border:1px solid #bae6fd; border-radius:4px; font-weight:600; cursor:pointer;">
                1. พ.ต.ต.อัครเดช (สวป.)
              </button>
              <button type="button" class="btn btn-sm" onclick="selectLeadCommander('2'); document.getElementById('select_lead_commander').value='2';" style="font-size:0.72rem; padding:3px 8px; background:#ffffff; color:#0369a1; border:1px solid #bae6fd; border-radius:4px; font-weight:600; cursor:pointer;">
                2. พ.ต.ท.ชวกร (สว.สอบสวน)
              </button>
              <button type="button" class="btn btn-sm" onclick="selectLeadCommander('3'); document.getElementById('select_lead_commander').value='3';" style="font-size:0.72rem; padding:3px 8px; background:#ffffff; color:#0369a1; border:1px solid #bae6fd; border-radius:4px; font-weight:600; cursor:pointer;">
                3. พ.ต.ท.นิสิต (สวป.ชส)
              </button>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">รายละเอียด "นำโดย" (พิมพ์แก้ไข/เพิ่มผู้ช่วยได้):</label>
            <textarea id="input_lead_officers" class="form-control" style="min-height:90px;" oninput="syncField('lead_officers', this.value)">• พ.ต.ต.อัครเดช แก้วร่องคำ
  สวป.สภ.บางปะกง
• ร.ต.อ.วิโรจน์ เทศทอง
  รอง สวป. สภ.บางปะกง
พร้อมกำลังสายตรวจ สภ.บางปะกง</textarea>
            <div style="font-size:0.72rem; color:#64748b; margin-top:3px;">
              *ข้อความ <strong>"พร้อมกำลังสายตรวจ สภ.บางปะกง"</strong> หรือ "พร้อมกำลัง..." ระบบจะแสดงเป็น <strong>ตัวหนา</strong> ให้อัตโนมัติ
            </div>
          </div>

          <!-- 7 นาย กำลังพลสายตรวจ (พร้อมด้วย) -->
          <div class="form-group" style="background:#f8fafc; padding:10px 12px; border-radius:8px; border:1px solid #cbd5e1;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <label class="form-label" style="font-weight:700; color:#0c3166; margin:0; display:flex; align-items:center; gap:4px;">
                <span>👥</span> พร้อมด้วย (เลือกกำลังพล 7 นาย):
              </label>
              <div style="display:flex; gap:4px;">
                <button type="button" class="btn btn-sm" onclick="toggleAllJoint(true)" style="font-size:0.68rem; padding:2px 8px; background:#e0f2fe; color:#0369a1; border:1px solid #bae6fd; border-radius:4px; font-weight:600; cursor:pointer;">
                  ✓ เลือกครบ 7 นาย
                </button>
                <button type="button" class="btn btn-sm" onclick="toggleAllJoint(false)" style="font-size:0.68rem; padding:2px 8px; background:#f1f5f9; color:#475569; border:1px solid #cbd5e1; border-radius:4px; cursor:pointer;">
                  ✕ ล้าง
                </button>
              </div>
            </div>

            <!-- Checkbox List -->
            <div id="joint_officers_checklist" style="display:grid; grid-template-columns:1fr; gap:5px; font-size:0.8rem; padding:6px 0;">
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" id="chk_joint_0" checked onchange="updateJointFromChecklist()"> 1. ส.ต.อ. อนุวัฒน์ บุตรทาสี</label>
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" id="chk_joint_1" checked onchange="updateJointFromChecklist()"> 2. ส.ต.ท. สิทธิโชค วิวัฒนพงศ์พันธ์</label>
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" id="chk_joint_2" checked onchange="updateJointFromChecklist()"> 3. ส.ต.ท. ทรงพล บุญไสย์</label>
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" id="chk_joint_3" checked onchange="updateJointFromChecklist()"> 4. ส.ต.ท. กฤษดา บูรณะกิติ</label>
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" id="chk_joint_4" checked onchange="updateJointFromChecklist()"> 5. ส.ต.ต. พัสกร อยู่ยืน</label>
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" id="chk_joint_5" checked onchange="updateJointFromChecklist()"> 6. ส.ต.ต. จิตติ แสงสว่าง</label>
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" id="chk_joint_6" checked onchange="updateJointFromChecklist()"> 7. ส.ต.ต. อนุชา พงษ์ราช</label>
            </div>

            <label class="form-label" style="margin-top:6px; font-size:0.75rem; color:#64748b;">
              ข้อความ "พร้อมด้วย" ที่จะแสดงบนรายงาน:
            </label>
            <textarea id="input_joint_officers" class="form-control" style="min-height:120px;" oninput="syncField('joint_officers', this.value)">• ส.ต.อ. อนุวัฒน์ บุตรทาสี
• ส.ต.ท. สิทธิโชค วิวัฒนพงศ์พันธ์
• ส.ต.ท. ทรงพล บุญไสย์
• ส.ต.ท. กฤษดา บูรณะกิติ
• ส.ต.ต. พัสกร อยู่ยืน
• ส.ต.ต. จิตติ แสงสว่าง
• ส.ต.ต. อนุชา พงษ์ราช</textarea>
          </div>
        </div>
      </div>

      <!-- 3. ข้อมูลผู้ต้องหาและผลการปฏิบัติ -->
      <div class="accordion-section">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>📋 3. ข้อมูลผู้ต้องหา และคดี</span>
          <span>▼</span>
        </div>
        <div class="accordion-content">
          <div class="form-group">
            <label class="form-label">หัวข้อการจับกุม</label>
            <input type="text" id="input_suspect_action" class="form-control" value="ร่วมกันทำการจับกุมตัว" oninput="syncField('suspect_action', this.value)">
          </div>
          <div class="form-group">
            <label class="form-label">ชื่อผู้ต้องหา</label>
            <input type="text" id="input_suspect_name" class="form-control" value="นางสาวนิตติญา หรือ เจน ชาเสน" oninput="syncField('suspect_name', this.value)">
          </div>
          <div class="form-row">
            <div class="form-group">
              <label class="form-label">อายุ</label>
              <input type="text" id="input_suspect_age" class="form-control" value="อายุ 40 ปี" oninput="syncField('suspect_age', this.value)">
            </div>
            <div class="form-group">
              <label class="form-label">เลขประจำตัวประชาชน</label>
              <input type="text" id="input_suspect_id" class="form-control" value="เลขบัตรประจำตัวประชาชน 1-490300033-36-7" oninput="syncField('suspect_id', this.value)">
            </div>
          </div>
          <div class="form-group">
            <label class="form-label">ที่อยู่ผู้ต้องหา</label>
            <input type="text" id="input_suspect_addr" class="form-control" value="บ้านเลขที่ 113 ม.2 ต.เหล่าหมี อ.ดอนตาล จ.มุกดาหาร (ผู้ต้องหา)" oninput="syncField('suspect_addr', this.value)">
          </div>
          <div class="form-group">
            <label class="form-label">กระทำความผิดฐาน (ข้อหา)</label>
            <textarea id="input_case_charge" class="form-control" oninput="syncField('case_charge', this.value)">“ร่วมกันลักทรัพย์ในเวลากลางคืน โดยใช้ยานพาหนะ เพื่อสะดวกแก่การกระทำความผิดเพื่อการพาทรัพย์นั้นไป หรือเพื่อให้พ้นจากการจับกุม”</textarea>
          </div>
          <div class="form-group">
            <label class="form-label">หมายจับ / รายละเอียดศาล / รายละเอียดเพิ่มเติม</label>
            <input type="text" id="input_case_warrant" class="form-control" value="◆ (หมายจับศาลจังหวัดฉะเชิงเทรา ที่ 408/2569 ลง 5 พฤศจิกายน 2569)" oninput="syncField('case_warrant', this.value)">
          </div>

          <!-- ลำดับการแสดง (ของกลาง vs ข้อหา) -->
          <div class="form-group" style="margin-top: 10px; padding: 10px; background: #f8fafc; border-radius: 8px; border: 1px solid #e2e8f0;">
            <label class="form-label" style="font-weight: 700; color: #0f172a; margin-bottom: 6px;">
              🔀 ลำดับการแสดง (ของกลาง vs กระทำความผิดฐาน):
            </label>
            <div style="display: flex; gap: 8px;">
              <button type="button" class="btn btn-sm" id="btnOrderEvFirst" onclick="setEvidenceOrder(true)" style="flex:1; font-size:0.75rem; padding:6px 8px; background:#f1f5f9; color:#334155; border:1px solid #cbd5e1; border-radius:6px; font-weight:600; cursor:pointer;">
                📦 เอาของกลางขึ้นก่อน
              </button>
              <button type="button" class="btn btn-sm" id="btnOrderChargeFirst" onclick="setEvidenceOrder(false)" style="flex:1; font-size:0.75rem; padding:6px 8px; background:#0284c7; color:#fff; border:1px solid #0284c7; border-radius:6px; font-weight:600; cursor:pointer;">
                ⚖️ ข้อหาขึ้นก่อน
              </button>
            </div>
            <div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">
              *สำหรับคดียาเสพติด/อาวุธปืน กด <strong>"📦 เอาของกลางขึ้นก่อน"</strong> เพื่อให้รายงานแสดงของกลางแล้วตามด้วยข้อหากระทำความผิดฐาน
            </div>
          </div>

          <!-- Optional Evidence -->
          <div class="form-group" style="background:#f8fafc; padding:10px; border-radius:8px; border:1px solid #cbd5e1;">
            <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
              <input type="checkbox" id="chk_has_evidence" onchange="toggleEvidenceBox(this.checked)">
              <span class="form-label" style="margin:0; font-weight:700; color:#0c3166;">📦 แสดงช่อง "ของกลางที่ตรวจยึด"</span>
            </label>
            <div id="evidence_input_group" style="display:none; margin-top:8px;">
              <textarea id="input_evidence_items" class="form-control" oninput="syncField('evidence_items', this.value)">• ยาเสพติดให้โทษประเภท 1 (ยาบ้า) จำนวน 200 เม็ด
• รถจักรยานยนต์ ยี่ห้อฮอนด้า เวฟ สีดำ หมายเลขทะเบียน 1กข-9999
• โทรศัพท์มือถือ ยี่ห้อไอโฟน จำนวน 1 เครื่อง</textarea>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">สถานที่จับกุม</label>
            <textarea id="input_case_location" class="form-control" oninput="syncField('case_location', this.value)">• บริเวณภายในบริษัท จั้มเวย์ จำกัด เลขที่ 1 ม.1 ต.หอมศีล อ.บางปะกง จ.ฉะเชิงเทรา</textarea>
          </div>
          <div class="form-group">
            <label class="form-label">การดำเนินการ</label>
            <textarea id="input_case_action" class="form-control" oninput="syncField('case_action', this.value)">• นำส่ง พงส.สภ.บางปะกง จว.ฉะเชิงเทรา ดำเนินคดีต่อไป</textarea>
          </div>
        </div>
      </div>

      <!-- 4. รูปภาพประกอบ -->
      <div class="accordion-section">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>📷 4. จัดการรูปภาพปฏิบัติงาน</span>
          <span>▼</span>
        </div>
        <div class="accordion-content">
          <div class="form-group">
            <label class="form-label">เลือกรูปแบบการจัดวางรูปภาพ:</label>
            <select class="form-control" id="photoLayoutSelect" onchange="changePhotoLayout(this.value)">
              <option value="layout-2">2 รูปภาพ (ซ้าย-ขวา แบบมาตรฐาน 50:50)</option>
              <option value="layout-1">1 รูปภาพ (แสดงรูปขนาดใหญ่ภาพเดียว)</option>
            </select>
          </div>
          <!-- รูปถ่ายที่ 1 -->
          <div class="form-group" style="background:#f8fafc; padding:8px 10px; border-radius:8px; border:1px solid #cbd5e1;">
            <label class="form-label" style="font-weight:700; color:#0c3166;">รูปถ่ายที่ 1 (ซ้าย):</label>
            <div style="display:flex; gap:6px; margin-top:4px;">
              <button type="button" class="btn btn-sm btn-primary" onclick="triggerPhotoUpload('photo1')" style="flex:1; font-size:0.75rem; padding:5px 8px;">
                📁 เลือกรูปที่ 1
              </button>
              <button type="button" class="btn btn-sm btn-danger" onclick="removePhoto('photo1')" style="font-size:0.75rem; padding:5px 8px; background:#ef4444; color:white; border:none; border-radius:4px;">
                🗑️ ลบรูปที่ 1
              </button>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">ข้อความป้ายคาดรูป (ภาษาไทย)</label>
            <input type="text" id="input_wm_th" class="form-control" value="งานสายตรวจ สภ.บางปะกง" oninput="syncField('wm_th', this.value)">
            <label class="form-label" style="margin-top:4px;">ข้อความป้ายคาดรูป (ภาษาอังกฤษ)</label>
            <input type="text" id="input_wm_en" class="form-control" value="BANGPAKONG POLICE PATROL" oninput="syncField('wm_en', this.value)">
          </div>

          <!-- รูปถ่ายที่ 2 -->
          <div class="form-group" id="photo2_group" style="background:#f8fafc; padding:8px 10px; border-radius:8px; border:1px solid #cbd5e1;">
            <label class="form-label" style="font-weight:700; color:#0c3166;">รูปถ่ายที่ 2 (ขวา):</label>
            <div style="display:flex; gap:6px; margin-top:4px;">
              <button type="button" class="btn btn-sm btn-primary" onclick="triggerPhotoUpload('photo2')" style="flex:1; font-size:0.75rem; padding:5px 8px;">
                📁 เลือกรูปที่ 2
              </button>
              <button type="button" class="btn btn-sm btn-danger" onclick="removePhoto('photo2')" style="font-size:0.75rem; padding:5px 8px; background:#ef4444; color:white; border:none; border-radius:4px;">
                🗑️ ลบรูปที่ 2
              </button>
            </div>
          </div>
          <div class="form-group">
            <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
              <input type="checkbox" id="chk_censor" onchange="toggleCensor(this.checked)">
              <span class="form-label" style="margin:0;">เบลอเซ็นเซอร์ใบหน้าผู้ต้องหา (PDPA)</span>
            </label>
          </div>
          <div style="font-size:0.75rem; color:#475569; background:#f1f5f9; padding:8px; border-radius:6px; line-height:1.4;">
            💡 <strong>วิธีใส่รูปสะดวก:</strong> สามารถคลิกที่กรอบรูปเพื่ออัปโหลด, <strong>ลากไฟล์รูปมาวาง (Drag & Drop)</strong> ลงในกรอบ หรือคลิกที่กรอบแล้วกด <strong>Ctrl + V</strong> เพื่อวางรูปจากคลิปบอร์ดได้ทันที!
          </div>
        </div>
      </div>

      <!-- 5. ส่วนท้ายรายงาน -->
      <div class="accordion-section">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>🔻 5. ส่วนท้ายและสโลแกน</span>
          <span>▼</span>
        </div>
        <div class="accordion-content">
          <div class="form-group">
            <label class="form-label">คำลงท้าย (แสดงบนแถบทอง-กรมท่า):</label>
            <input type="text" id="input_closing_text" class="form-control" value="จึงเรียนมาเพื่อโปรดทราบ" oninput="syncField('closing_text', this.value)">
          </div>
          <div class="form-group" style="background:#f8fafc; padding:8px 10px; border-radius:6px; border:1px solid #e2e8f0;">
            <label style="display:flex; align-items:center; gap:8px; cursor:pointer; font-size:0.8rem; color:#334155; font-weight:600;">
              <input type="checkbox" id="chk_show_subfooter" onchange="toggleSubFooter(this.checked)">
              <span>➕ แสดงแถบสโลแกนและชื่อสถานีด้านล่างเพิ่มเติม</span>
            </label>
          </div>
          <div id="subfooter_inputs" style="display:none; flex-direction:column; gap:8px;">
            <div class="form-group">
              <label class="form-label">สโลแกนแถบล่าง</label>
              <input type="text" id="input_footer_slogan" class="form-control" value="“ ปลอดภัย  ใกล้ชิด  ประชาชน ”" oninput="syncField('footer_slogan', this.value)">
            </div>
            <div class="form-group">
              <label class="form-label">หน่วยงานส่วนล่าง</label>
              <input type="text" id="input_footer_station" class="form-control" value="สภ.บางปะกง" oninput="syncField('footer_station', this.value)">
              <label class="form-label" style="margin-top:4px;">จังหวัด / ภ.จว.</label>
              <input type="text" id="input_footer_prov" class="form-control" value="ตำรวจภูธรจังหวัดฉะเชิงเทรา" oninput="syncField('footer_prov', this.value)">
            </div>
          </div>
        </div>
      </div>

      <!-- 6. ปรับขนาดตัวหนังสือละเอียด -->
      <div class="accordion-section">
        <div class="accordion-header" onclick="toggleAccordion(this)">
          <span>🔤 6. ปรับขนาดตัวหนังสือละเอียด</span>
          <span>▼</span>
        </div>
        <div class="accordion-content">
          <!-- ขนาดภาพรวม -->
          <div class="form-group">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <label class="form-label" style="font-weight:700; color:#38bdf8; margin:0;">ขนาดตัวหนังสือทั้งหมด (ภาพรวม):</label>
              <span id="sliderGlobalVal" style="font-weight:700; color:#38bdf8; font-size:0.8rem;">100%</span>
            </div>
            <input type="range" id="sliderGlobalFont" min="80" max="135" value="100" step="5" style="width:100%; cursor:pointer;" oninput="onGlobalSliderChange(this.value)">
          </div>

          <!-- ขนาดข้อหา/กระทำความผิดฐาน -->
          <div class="form-group">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <label class="form-label" style="margin:0;">ขนาดข้อหา / กระทำความผิดฐาน:</label>
              <span id="sliderChargeVal" style="font-weight:700; color:#38bdf8; font-size:0.8rem;">100%</span>
            </div>
            <input type="range" id="sliderChargeFont" min="80" max="145" value="100" step="5" style="width:100%; cursor:pointer;" oninput="onSectionSliderChange('charge', this.value)">
            <div style="font-size:0.7rem; color:#64748b; margin-top:2px;">*ใช้เพิ่มขนาดข้อหาให้เด่นชัด หรือลดขนาดเมื่อข้อหายาว</div>
          </div>

          <!-- ขนาดรายชื่อชุดจับกุม -->
          <div class="form-group">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <label class="form-label" style="margin:0;">ขนาดรายชื่อชุดจับกุม (นำโดย / พร้อมด้วย):</label>
              <span id="sliderOfficersVal" style="font-weight:700; color:#38bdf8; font-size:0.8rem;">100%</span>
            </div>
            <input type="range" id="sliderOfficersFont" min="80" max="140" value="100" step="5" style="width:100%; cursor:pointer;" oninput="onSectionSliderChange('officers', this.value)">
          </div>

          <!-- ขนาดชื่อสถานีตำรวจ -->
          <div class="form-group">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <label class="form-label" style="margin:0;">ขนาดชื่อสถานีตำรวจ (หัวกระดาษ):</label>
              <span id="sliderStationVal" style="font-weight:700; color:#38bdf8; font-size:0.8rem;">100%</span>
            </div>
            <input type="range" id="sliderStationFont" min="80" max="130" value="100" step="5" style="width:100%; cursor:pointer;" oninput="onSectionSliderChange('station', this.value)">
          </div>

          <button type="button" class="btn btn-sm" onclick="resetAllFontSizes()" style="background:#334155; color:#f1f5f9; border:1px solid #475569; width:100%; justify-content:center; padding:6px; margin-top:4px; font-weight:600; cursor:pointer;">
            ↺ รีเซ็ตขนาดตัวหนังสือทั้งหมดเป็นค่ามาตรฐาน
          </button>
        </div>
      </div>

      <!-- JUMP TO BOTTOM BUTTON (For Mobile Users) -->
      <div style="margin-top: 14px;">
        <a href="#previewSection" class="btn btn-primary" style="width: 100%; justify-content: center; padding: 12px; font-size: 0.95rem; border-radius: 10px;">
          👇 กรอกข้อมูลเสร็จแล้ว เลื่อนลงไปดูภาพตัวอย่างด้านล่าง
        </a>
      </div>
    </aside>

    <!-- 2. LIVE PREVIEW PANEL (Positioned at BOTTOM on mobile screens) -->
    <section class="preview-panel" id="previewSection">
      
      <div class="preview-header-bar" style="display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 720px;">
        <span style="font-weight: 700; color: #092147; font-size: 1.05rem; display: flex; align-items: center; gap: 6px;">
          🖼️ ภาพตัวอย่างรายงานผลการปฏิบัติ
        </span>
        <div style="display: flex; gap: 6px; flex-wrap: wrap;">
          <button type="button" class="btn btn-primary" onclick="openPreviewModal()" style="font-size: 0.78rem; padding: 5px 12px; background: #0284c7; color: #ffffff; border: 1px solid #0369a1; font-weight: 700;">
            🔍 ซูมดูภาพขนาดเต็ม
          </button>
          <a href="#sidebarPanel" class="btn btn-secondary" style="font-size: 0.78rem; padding: 5px 12px; background: #e2e8f0; color: #1e293b; border: 1px solid #cbd5e1;">
            👆 กลับไปแก้ไขฟอร์ม
          </a>
          <button class="btn btn-success" style="font-size: 0.8rem; padding: 5px 12px;" onclick="exportToImage()">
            📸 บันทึกรูปภาพ (PNG)
          </button>
        </div>
      </div>

      <div class="preview-tip">
        💡 <strong>คำแนะนำ:</strong> สามารถคลิกแก้ไขข้อความบนภาพได้โดยตรง หรือกดปุ่ม <strong>"บันทึกรูปภาพ (PNG)"</strong> เพื่อบันทึกภาพคมชัดสูง
      </div>

      <!-- Quick Font Size Controller Bar -->
      <div class="font-control-toolbar" style="width: 100%; max-width: 720px; background: rgba(15, 23, 42, 0.85); border: 1.5px solid rgba(56, 189, 248, 0.35); border-radius: 8px; padding: 7px 12px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.25); margin-bottom: 8px;">
        <div style="display:flex; align-items:center; gap:8px;">
          <span style="font-weight: 700; color: #38bdf8; font-size: 0.84rem; display: flex; align-items: center; gap: 4px;">
            <span>🔤</span> ปรับขนาดตัวหนังสือ:
          </span>
          <div style="display:flex; align-items:center; gap:4px;">
            <button type="button" class="btn btn-sm" onclick="adjustGlobalFontSize(-0.05)" style="background:#1e293b; color:#fff; border:1px solid #475569; padding:2px 10px; font-weight:800; border-radius:5px; font-size:0.85rem; cursor:pointer;" title="ลดขนาดตัวหนังสือ">
              A-
            </button>
            <span id="fontScaleDisplay" style="font-weight:800; color:#38bdf8; font-size:0.85rem; min-width:48px; text-align:center; background:#0b1329; padding:2px 8px; border-radius:5px; border:1px solid #334155;">
              100%
            </span>
            <button type="button" class="btn btn-sm" onclick="adjustGlobalFontSize(0.05)" style="background:#1e293b; color:#fff; border:1px solid #475569; padding:2px 10px; font-weight:800; border-radius:5px; font-size:0.85rem; cursor:pointer;" title="เพิ่มขนาดตัวหนังสือ">
              A+
            </button>
            <button type="button" class="btn btn-sm" onclick="setGlobalFontSize(1.0)" style="background:#334155; color:#cbd5e1; border:1px solid #475569; padding:2px 8px; font-size:0.75rem; border-radius:5px; cursor:pointer;">
              ปกติ
            </button>
          </div>
        </div>
        <div style="display:flex; gap:4px; align-items:center;">
          <button type="button" class="btn btn-sm btn-fscale" id="btnFs90" onclick="setGlobalFontSize(0.9)" style="font-size:0.72rem; padding:3px 7px; background:#1e293b; color:#94a3b8; border:1px solid #334155; border-radius:4px; cursor:pointer;">เล็ก 90%</button>
          <button type="button" class="btn btn-sm btn-fscale active" id="btnFs100" onclick="setGlobalFontSize(1.0)" style="font-size:0.72rem; padding:3px 7px; background:#0284c7; color:#fff; border:1px solid #0284c7; border-radius:4px; cursor:pointer; font-weight:700;">ปกติ 100%</button>
          <button type="button" class="btn btn-sm btn-fscale" id="btnFs110" onclick="setGlobalFontSize(1.1)" style="font-size:0.72rem; padding:3px 7px; background:#1e293b; color:#94a3b8; border:1px solid #334155; border-radius:4px; cursor:pointer;">ใหญ่ 110%</button>
          <button type="button" class="btn btn-sm btn-fscale" id="btnFs120" onclick="setGlobalFontSize(1.2)" style="font-size:0.72rem; padding:3px 7px; background:#1e293b; color:#94a3b8; border:1px solid #334155; border-radius:4px; cursor:pointer;">ใหญ่มาก 120%</button>
        </div>
      </div>

      <!-- RESPONSIVE AUTO-SCALING WRAPPER (Guarantees zero mobile horizontal scroll) -->
      <div class="poster-scale-wrapper">
        <div class="poster-scale-container" id="posterScaleContainer">
          
          <!-- THE POSTER CONTAINER (Target for html2canvas & Print) -->
          <div class="poster-wrapper" id="reportPoster">
            
            <!-- Official Watermark Background -->
            <div class="poster-watermark">
              <img id="watermarkBadgeImg" src="{badge_b64}" alt="Police Watermark">
            </div>
            
            <!-- HEADER - Harmonized Royal Navy & Gold Theme -->
            <div class="poster-header">
              <!-- Decorative subtle background pattern -->
              <div class="header-bg-pattern"></div>
              <!-- Radiant Golden Halo behind the Emblem -->
              <div class="header-badge-glow"></div>
              
              <div class="header-content">
                <div class="header-left">
                  <div class="badge-container" title="คลิกเพื่อเปลี่ยนตราโลโก้" onclick="document.getElementById('badgeFileInput').click()">
                    <img id="badgeImg" src="{badge_b64}" alt="ตราตำรวจภูธรจังหวัดฉะเชิงเทรา" class="police-badge-img">
                    <div class="badge-edit-hint">เปลี่ยนโลโก้</div>
                  </div>
                  <input type="file" id="badgeFileInput" class="hidden-file-input" accept="image/*" onchange="handleBadgeUpload(event)">
                  
                  <div class="station-title-box">
                    <div class="station-main-name" id="view_station_th" contenteditable="true" oninput="syncInput('station_th', this.innerText)">สภ.บางปะกง</div>
                    <div class="station-en-name" id="view_station_en" contenteditable="true" oninput="syncInput('station_en', this.innerText)">BANGPAKONG POLICE STATION</div>
                    <div class="station-slogan-ribbon" id="view_slogan_top" contenteditable="true" oninput="syncInput('slogan_top', this.innerText)">“ดูแลทุกข์ สุขของประชาชน”</div>
                  </div>
                </div>

                <div class="header-right">
                  <div class="report-type-pill">
                    <div class="report-title-main" id="view_report_title" contenteditable="true" oninput="syncInput('report_title', this.innerText)">รายงานผลการปฏิบัติ</div>
                    <div class="report-title-sub" id="view_report_sub" contenteditable="true" oninput="syncInput('report_sub', this.innerText)">ประจำวัน</div>
                  </div>
                  <div class="date-card">
                    <div class="date-icon">📅</div>
                    <div class="date-info">
                      <div class="date-text" id="view_report_date" contenteditable="true" oninput="syncInput('report_date', this.innerText)">วันที่ 9 พฤศจิกายน 2569</div>
                      <div class="time-text" id="view_report_time" contenteditable="true" oninput="syncInput('report_time', this.innerText)">เวลาประมาณ 11.00 น.</div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Dual Gold & Cyan Swoosh Ribbon at Header Bottom (Harmonized with bottom banner) -->
              <div class="header-gold-ribbon-bar">
                <svg viewBox="0 0 720 14" preserveAspectRatio="none" style="width:100%; height:100%; display:block;" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="hdrGoldRibbon" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" stop-color="#b45309"/>
                      <stop offset="18%" stop-color="#f59e0b"/>
                      <stop offset="48%" stop-color="#fef08a"/>
                      <stop offset="72%" stop-color="#f59e0b"/>
                      <stop offset="100%" stop-color="#d97706"/>
                    </linearGradient>
                    <linearGradient id="hdrCyanLine" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" stop-color="#0284c7"/>
                      <stop offset="50%" stop-color="#38bdf8"/>
                      <stop offset="100%" stop-color="#0284c7"/>
                    </linearGradient>
                  </defs>
                  <path d="M0,2 Q180,-1 360,3 T720,1 L720,4 L0,4 Z" fill="url(#hdrCyanLine)" opacity="0.9"/>
                  <path d="M0,4 Q160,0 340,5 T720,2 L720,14 L0,14 Z" fill="url(#hdrGoldRibbon)"/>
                  <path d="M0,4 Q160,0 340,5 T720,2" fill="none" stroke="#fffbeb" stroke-width="1.2" opacity="0.9"/>
                </svg>
              </div>
            </div>

            <!-- BODY: 2 COLUMNS -->
            <div class="poster-body">
              
              <!-- LEFT COLUMN -->
              <div class="body-col-left">
                <div class="cmd-greeting">
                  <svg class="cmd-icon" viewBox="0 0 24 24"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm-2 14l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
                  <div>
                    <div class="cmd-greeting-text" id="view_cmd_to" contenteditable="true" oninput="syncInput('cmd_to', this.innerText)">เรียน ผู้บังคับบัญชา</div>
                    <div class="cmd-greeting-text" id="view_cmd_stn" contenteditable="true">สภ.บางปะกง</div>
                  </div>
                </div>

                <div class="under-command-label">ภายใต้การอำนวยการของ</div>

                <div class="commander-list">
                  <!-- Commander 1 -->
                  <div class="commander-card">
                    <div class="commander-avatar">👤</div>
                    <div class="commander-info">
                      <div class="commander-name" id="view_cmd1_name" contenteditable="true" oninput="syncInput('cmd1_name', this.innerText)">พ.ต.อ.บัณฑิต ธรรมอนันต์</div>
                      <div class="commander-pos" id="view_cmd1_pos" contenteditable="true" oninput="syncInput('cmd1_pos', this.innerText)">ผกก.สภ.บางปะกง</div>
                    </div>
                  </div>
                  <!-- Commander 2 -->
                  <div class="commander-card">
                    <div class="commander-avatar">👤</div>
                    <div class="commander-info">
                      <div class="commander-name" id="view_cmd2_name" contenteditable="true" oninput="syncInput('cmd2_name', this.innerText)">พ.ต.ท.อำนาจ ยิ้มเนียม</div>
                      <div class="commander-pos" id="view_cmd2_pos" contenteditable="true" oninput="syncInput('cmd2_pos', this.innerText)">รอง ผกก.ป.สภ.บางปะกง</div>
                    </div>
                  </div>
                </div>

                <!-- นำโดย -->
                <div style="margin-top: 4px;">
                  <div class="section-lead-pill">นำโดย</div>
                  <div class="officers-card-box">
                    <div class="officers-block" id="view_lead_officers" contenteditable="true" oninput="syncInputTextarea('lead_officers', this.innerHTML)">
                      <div class="officer-item"><strong>• พ.ต.ต.อัครเดช แก้วร่องคำ</strong></div>
                      <div class="officer-item" style="padding-left:12px; color:#475569;">สวป.สภ.บางปะกง</div>
                      <div class="officer-item"><strong>• ร.ต.อ.วิโรจน์ เทศทอง</strong></div>
                      <div class="officer-item" style="padding-left:12px; color:#475569;">รอง สวป. สภ.บางปะกง</div>
                      <div class="officer-item bold-line" style="margin-top:3px; font-weight:700; color:#0c3166;"><strong>พร้อมกำลังสายตรวจ สภ.บางปะกง</strong></div>
                    </div>
                  </div>
                </div>

                <!-- พร้อมด้วย -->
                <div style="margin-top: 6px;">
                  <div class="section-joint-pill">พร้อมด้วย</div>
                  <div class="officers-card-box">
                    <div class="officers-block" id="view_joint_officers" contenteditable="true" oninput="syncInputTextarea('joint_officers', this.innerHTML)">
                      <div class="officer-item">• ส.ต.อ. อนุวัฒน์ บุตรทาสี</div>
                      <div class="officer-item">• ส.ต.ท. สิทธิโชค วิวัฒนพงศ์พันธ์</div>
                      <div class="officer-item">• ส.ต.ท. ทรงพล บุญไสย์</div>
                      <div class="officer-item">• ส.ต.ท. กฤษดา บูรณะกิติ</div>
                      <div class="officer-item">• ส.ต.ต. พัสกร อยู่ยืน</div>
                      <div class="officer-item">• ส.ต.ต. จิตติ แสงสว่าง</div>
                      <div class="officer-item">• ส.ต.ต. อนุชา พงษ์ราช</div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- RIGHT COLUMN -->
              <div class="body-col-right">
                
                <!-- Section 1: ผลการปฏิบัติ -->
                <div class="case-card">
                  <div class="case-card-header">
                    <span>🛡️</span> ผลการปฏิบัติ
                  </div>
                  <div class="case-card-body">
                    <div class="suspect-headline">
                      <span>👥</span> <span id="view_suspect_action" contenteditable="true" oninput="syncInput('suspect_action', this.innerText)">ร่วมกันทำการจับกุมตัว</span>
                    </div>
                    <div style="padding-left: 14px;">
                      <div class="suspect-name" id="view_suspect_name" contenteditable="true" oninput="syncInput('suspect_name', this.innerText)">• นางสาวนิตติญา หรือ เจน ชาเสน</div>
                      <div id="view_suspect_age" contenteditable="true" oninput="syncInput('suspect_age', this.innerText)">อายุ 40 ปี</div>
                      <div id="view_suspect_id" contenteditable="true" oninput="syncInput('suspect_id', this.innerText)">เลขบัตรประจำตัวประชาชน 1-490300033-36-7</div>
                      <div id="view_suspect_addr" contenteditable="true" oninput="syncInput('suspect_addr', this.innerText)">บ้านเลขที่ 113 ม.2 ต.เหล่าหมี อ.ดอนตาล จ.มุกดาหาร <strong>(ผู้ต้องหา)</strong></div>
                    </div>
                  </div>
                </div>

                <!-- Section 2: กระทำความผิดฐาน -->
                <div class="case-card" id="view_charge_container">
                  <div class="case-card-header">
                    <span>⚖️</span> กระทำความผิดฐาน
                  </div>
                  <div class="case-card-body">
                    <div class="charge-quote" id="view_case_charge" contenteditable="true" oninput="syncInput('case_charge', this.innerText)">
                      “ร่วมกันลักทรัพย์ในเวลากลางคืน โดยใช้ยานพาหนะ เพื่อสะดวกแก่การกระทำความผิดเพื่อการพาทรัพย์นั้นไป หรือเพื่อให้พ้นจากการจับกุม”
                    </div>
                    <div class="warrant-badge" id="view_case_warrant" contenteditable="true" oninput="syncInput('case_warrant', this.innerText)">
                      ◆ (หมายจับศาลจังหวัดฉะเชิงเทรา ที่ 408/2569 ลง 5 พฤศจิกายน 2569)
                    </div>
                  </div>
                </div>

                <!-- Optional Section: ของกลางที่ตรวจยึด -->
                <div class="case-card evidence-box" id="view_evidence_container">
                  <div class="case-card-header">
                    <span>📦</span> ของกลางที่ตรวจยึด
                  </div>
                  <div class="case-card-body" id="view_evidence_items" contenteditable="true" oninput="syncInputTextarea('evidence_items', this.innerHTML)">
                    <div>• ยาเสพติดให้โทษประเภท 1 (ยาบ้า) จำนวน 200 เม็ด</div>
                    <div>• รถจักรยานยนต์ ยี่ห้อฮอนด้า เวฟ สีดำ หมายเลขทะเบียน 1กข-9999</div>
                    <div>• โทรศัพท์มือถือ ยี่ห้อไอโฟน จำนวน 1 เครื่อง</div>
                  </div>
                </div>

                <!-- Section 3: สถานที่จับกุม -->
                <div class="case-card">
                  <div class="case-card-header">
                    <span>📍</span> สถานที่จับกุม
                  </div>
                  <div class="case-card-body">
                    <div id="view_case_location" contenteditable="true" oninput="syncInput('case_location', this.innerText)">
                      • บริเวณภายในบริษัท จั้มเวย์ จำกัด เลขที่ 1 ม.1 ต.หอมศีล อ.บางปะกง จ.ฉะเชิงเทรา
                    </div>
                  </div>
                </div>

                <!-- Section 4: การดำเนินการ -->
                <div class="case-card">
                  <div class="case-card-header">
                    <span>📑</span> การดำเนินการ
                  </div>
                  <div class="case-card-body">
                    <div id="view_case_action" style="font-weight:600;" contenteditable="true" oninput="syncInput('case_action', this.innerText)">
                      • นำส่ง พงส.สภ.บางปะกง จว.ฉะเชิงเทรา ดำเนินคดีต่อไป
                    </div>
                  </div>
                </div>

              </div>

            </div>

            <!-- PHOTOS GRID (Clean empty placeholder boxes by default) -->
            <div class="poster-photos">
              <div class="photos-grid layout-2" id="photosGrid">
                
                <!-- Photo 1 -->
                <div class="photo-frame active-slot" id="photo1Frame" onclick="triggerPhotoUpload('photo1')" ondblclick="triggerPhotoUpload('photo1')" title="คลิกเพื่อเลือกรูปภาพที่ 1">
                  <!-- Empty placeholder by default -->
                  <div class="photo-placeholder" id="photo1Placeholder">
                    <div class="placeholder-icon">📷</div>
                    <div class="placeholder-title">คลิกเพื่อเพิ่มรูปภาพที่ 1</div>
                    <div class="placeholder-sub">(หรือลากรูปมาวาง / กด Ctrl + V)</div>
                    <div class="placeholder-btn">＋ เลือกไฟล์รูปภาพ</div>
                  </div>
                  <!-- The image element (hidden initially until image uploaded) -->
                  <img id="photo1Img" src="" class="photo-img" alt="รูปปฏิบัติงาน 1">
                  <!-- Hover Action overlay when image is present -->
                  <div class="photo-overlay-edit" id="photo1Overlay">
                    <div style="display:flex; gap:6px;">
                      <button type="button" class="btn btn-sm" onclick="event.stopPropagation(); triggerPhotoUpload('photo1')" style="background:#0284c7; color:white; font-size:0.75rem; padding:5px 10px; border-radius:4px; border:none; cursor:pointer; font-weight:600;">
                        🔄 เปลี่ยนรูป
                      </button>
                      <button type="button" class="btn btn-sm" onclick="removePhoto('photo1', event)" style="background:#ef4444; color:white; font-size:0.75rem; padding:5px 10px; border-radius:4px; border:none; cursor:pointer; font-weight:600;">
                        🗑️ ลบรูป
                      </button>
                    </div>
                  </div>
                  <!-- Watermark bar (only shown when image is present) -->
                  <div class="photo-watermark" id="photo1Watermark" style="display:none;">
                    <div class="watermark-th" id="view_wm_th" contenteditable="true" onclick="event.stopPropagation()" oninput="syncInput('wm_th', this.innerText)">งานสายตรวจ สภ.บางปะกง</div>
                    <div class="watermark-en" id="view_wm_en" contenteditable="true" onclick="event.stopPropagation()" oninput="syncInput('wm_en', this.innerText)">BANGPAKONG POLICE PATROL</div>
                  </div>
                </div>
                <input type="file" id="photo1Input" class="hidden-file-input" accept="image/*" onchange="handlePhotoUpload(event, 'photo1')">

                <!-- Photo 2 -->
                <div class="photo-frame" id="photo2Frame" onclick="triggerPhotoUpload('photo2')" ondblclick="triggerPhotoUpload('photo2')" title="คลิกเพื่อเลือกรูปภาพที่ 2">
                  <div class="photo-placeholder" id="photo2Placeholder">
                    <div class="placeholder-icon">📷</div>
                    <div class="placeholder-title">คลิกเพื่อเพิ่มรูปภาพที่ 2</div>
                    <div class="placeholder-sub">(หรือลากรูปมาวาง / กด Ctrl + V)</div>
                    <div class="placeholder-btn">＋ เลือกไฟล์รูปภาพ</div>
                  </div>
                  <img id="photo2Img" src="" class="photo-img" alt="รูปปฏิบัติงาน 2">
                  <div class="photo-overlay-edit" id="photo2Overlay">
                    <div style="display:flex; gap:6px;">
                      <button type="button" class="btn btn-sm" onclick="event.stopPropagation(); triggerPhotoUpload('photo2')" style="background:#0284c7; color:white; font-size:0.75rem; padding:5px 10px; border-radius:4px; border:none; cursor:pointer; font-weight:600;">
                        🔄 เปลี่ยนรูป
                      </button>
                      <button type="button" class="btn btn-sm" onclick="removePhoto('photo2', event)" style="background:#ef4444; color:white; font-size:0.75rem; padding:5px 10px; border-radius:4px; border:none; cursor:pointer; font-weight:600;">
                        🗑️ ลบรูป
                      </button>
                    </div>
                  </div>
                </div>
                <input type="file" id="photo2Input" class="hidden-file-input" accept="image/*" onchange="handlePhotoUpload(event, 'photo2')">

              </div>

            </div>

            <!-- Official Gold & Royal Navy Closing Banner -->
            <div class="poster-closing-banner">
              <img src="{footer_banner_b64}" class="closing-banner-bg" alt="แถบปิดท้ายราชการ">
              <div class="closing-banner-text" id="view_closing_text" contenteditable="true" oninput="syncInput('closing_text', this.innerText)">
                จึงเรียนมาเพื่อโปรดทราบ
              </div>
            </div>

            <!-- Optional Secondary Footer (Default hidden) -->
            <div class="poster-footer" id="optionalFooter" style="display: none;">
              <div class="footer-slogan" id="view_footer_slogan" contenteditable="true" oninput="syncInput('footer_slogan', this.innerText)">
                “ ปลอดภัย ใกล้ชิด ประชาชน ”
              </div>
              <div class="footer-divider-slash">
                <span class="slash-line s1"></span>
                <span class="slash-line s2"></span>
              </div>
              <div class="footer-station-info">
                <img src="{mascot_b64}" class="footer-mascot-img" alt="ตราสัญลักษณ์ตำรวจ">
                <div class="footer-text-block">
                  <div class="footer-station-name" id="view_footer_station" contenteditable="true" oninput="syncInput('footer_station', this.innerText)">สภ.บางปะกง</div>
                  <div class="footer-province-name" id="view_footer_prov" contenteditable="true" oninput="syncInput('footer_prov', this.innerText)">ตำรวจภูธรจังหวัดฉะเชิงเทรา</div>
                </div>
              </div>
            </div>

          </div>

        </div>
      </div>

    </section>

  </main>

  <div id="toast">บันทึกข้อมูลเรียบร้อย</div>

  <!-- Inlined html2canvas -->
  <script>
  {html2canvas_code}
  </script>

  <!-- Interactive Logic with Bug Fixes -->
  <script>
    let activeSlot = 'photo1';

    const defaultData = {{
      station_th: "สภ.บางปะกง",
      station_en: "BANGPAKONG POLICE STATION",
      slogan_top: "“ดูแลทุกข์ สุขของประชาชน”",
      report_title: "รายงานผลการปฏิบัติ",
      report_sub: "ประจำวัน",
      report_date: "วันที่ 9 พฤศจิกายน 2569",
      report_time: "เวลาประมาณ 11.00 น.",
      cmd_to: "เรียน ผู้บังคับบัญชา",
      cmd1_name: "พ.ต.อ.บัณฑิต ธรรมอนันต์",
      cmd1_pos: "ผกก.สภ.บางปะกง",
      cmd2_name: "พ.ต.ท.ชินพัฒน์ พุทธเมตตา",
      cmd2_pos: "รอง ผกก.สส.สภ.บางปะกง",
      suspect_action: "ร่วมกันทำการจับกุมตัว",
      suspect_name: "• นางสาวนิตติญา หรือ เจน ชาเสน",
      suspect_age: "อายุ 40 ปี",
      suspect_id: "เลขบัตรประจำตัวประชาชน 1-490300033-36-7",
      suspect_addr: "บ้านเลขที่ 113 ม.2 ต.เหล่าหมี อ.ดอนตาล จ.มุกดาหาร (ผู้ต้องหา)",
      case_charge: "“ร่วมกันลักทรัพย์ในเวลากลางคืน โดยใช้ยานพาหนะ เพื่อสะดวกแก่การกระทำความผิดเพื่อการพาทรัพย์นั้นไป หรือเพื่อให้พ้นจากการจับกุม”",
      case_warrant: "◆ (หมายจับศาลจังหวัดฉะเชิงเทรา ที่ 408/2569 ลง 5 พฤศจิกายน 2569)",
      case_location: "• บริเวณภายในบริษัท จั้มเวย์ จำกัด เลขที่ 1 ม.1 ต.หอมศีล อ.บางปะกง จ.ฉะเชิงเทรา",
      case_action: "• นำส่ง พงส.สภ.บางปะกง จว.ฉะเชิงเทรา ดำเนินคดีต่อไป",
      evidence_items: "• ยาเสพติดให้โทษประเภท 1 (ยาบ้า) จำนวน 200 เม็ด\\n• รถจักรยานยนต์ ยี่ห้อฮอนด้า เวฟ สีดำ หมายเลขทะเบียน 1กข-9999\\n• โทรศัพท์มือถือ ยี่ห้อไอโฟน จำนวน 1 เครื่อง",
      wm_th: "งานสืบสวน สภ.บางปะกง",
      wm_en: "BANGPAKONG INVESTIGATION",
      closing_text: "จึงเรียนมาเพื่อโปรดทราบ",
      footer_slogan: "“ ปลอดภัย  ใกล้ชิด  ประชาชน ”",
      footer_station: "สภ.บางปะกง",
      footer_prov: "ตำรวจภูธรจังหวัดฉะเชิงเทรา"
    }};

    // Case Preset Presets
    const casePresets = {{
      warrant: {{
        suspect_action: "ร่วมกันทำการจับกุมตัว",
        suspect_name: "• นางสาวนิตติญา หรือ เจน ชาเสน",
        suspect_age: "อายุ 40 ปี",
        case_charge: "“ร่วมกันลักทรัพย์ในเวลากลางคืน โดยใช้ยานพาหนะ เพื่อสะดวกแก่การกระทำความผิดเพื่อการพาทรัพย์นั้นไป หรือเพื่อให้พ้นจากการจับกุม”",
        case_warrant: "◆ (หมายจับศาลจังหวัดฉะเชิงเทรา ที่ 408/2569 ลง 5 พฤศจิกายน 2569)",
        has_evidence: false
      }},
      drugs: {{
        suspect_action: "ร่วมกันทำการจับกุมตัว",
        suspect_name: "• นายสมชาย (สงวนนามสกุล)",
        suspect_age: "อายุ 32 ปี",
        case_charge: "“จำหน่ายโดยมีไว้ในครอบครองเพื่อจำหน่ายซึ่งยาเสพติดให้โทษประเภท 1 (ยาบ้า) โดยไม่ได้รับอนุญาต อันเป็นการกระทำเพื่อการค้า”",
        case_warrant: "",
        has_evidence: true,
        evidence_items: "• ยาเสพติดให้โทษประเภท 1 (ยาบ้า) จำนวน 200 เม็ด\\n• รถจักรยานยนต์ ยี่ห้อฮอนด้า เวฟ สีน้ำเงิน-ดำ หมายเลขทะเบียน 1กข-9999\\n• โทรศัพท์มือถือ ยี่ห้อไอโฟน จำนวน 1 เครื่อง",
        order_evidence_first: true
      }},
      weapons: {{
        suspect_action: "ร่วมกันทำการจับกุมตัว",
        suspect_name: "• นายอนุชา (สงวนนามสกุล)",
        suspect_age: "อายุ 28 ปี",
        case_charge: "“มีอาวุธปืนและเครื่องกระสุนปืนไว้ในครอบครองโดยไม่ได้รับอนุญาต และพาอาวุธปืนติดตัวไปในเมือง หมู่บ้าน หรือทางสาธารณะโดยไม่มีเหตุอันควร”",
        case_warrant: "◆ จับกุมพร้อมอาวุธปืนพกสั้นไทยประดิษฐ์ ขนาด .38 จำนวน 1 กระบอก",
        has_evidence: true,
        evidence_items: "• อาวุธปืนพกสั้นไทยประดิษฐ์ ขนาด .38 จำนวน 1 กระบอก\\n• เครื่องกระสุนปืน ขนาด .38 จำนวน 6 นัด\\n• ซองพกหนังสีดำ จำนวน 1 ซอง"
      }},
      theft: {{
        suspect_action: "ร่วมกันทำการจับกุมตัว",
        suspect_name: "• นายธีรเดช (สงวนนามสกุล)",
        suspect_age: "อายุ 25 ปี",
        case_charge: "“ลักทรัพย์ในเคหสถานในเวลากลางคืน โดยทำอันตรายสิ่งกีดกั้นสำหรับคุ้มครองบุคคลหรือทรัพย์ หรือรับของโจร”",
        case_warrant: "◆ ตามหมายจับศาลจังหวัดฉะเชิงเทรา",
        has_evidence: false
      }},
      gambling: {{
        suspect_action: "ร่วมกันทำการจับกุมตัวผู้ต้องหา รวม 4 คน",
        suspect_name: "• นายเอกชัย (สงวนนามสกุล) กับพวก รวม 4 คน",
        suspect_age: "อายุระหว่าง 28 - 45 ปี",
        case_charge: "“ร่วมกันลักลอบเล่นการพนัน (ไฮโล) พนันเอาทรัพย์สินกันโดยไม่ได้รับอนุญาต”",
        case_warrant: "◆ พร้อมของกลาง ลูกเต๋า จานรอง ฝาครอบ และเงินสด",
        has_evidence: true,
        evidence_items: "• ลูกเต๋าบอกแต้ม จำนวน 3 ลูก\\n• จานรองพร้อมฝาครอบ จำนวน 1 ชุด\\n• แผ่นแปลนบอกแต้ม จำนวน 1 แผ่น\\n• เงินสดของกลาง จำนวน 2,500 บาท"
      }},
      patrol: {{
        suspect_action: "รายงานผลการตั้งจุดตรวจ/จุดสกัด ป้องกันปราบปรามอาชญากรรม",
        suspect_name: "• ผลการตรวจค้นบุคคลและยานพาหนะกลุ่มเสี่ยง",
        suspect_age: "ผลการปฏิบัติเรียบร้อย",
        case_charge: "“การตั้งจุดตรวจความปลอดภัย กวดขันวินัยจราจร ตรวจค้นอาวุธและยาเสพติด เพื่อป้องกันเหตุอาชญากรรมในพื้นที่รับผิดชอบ”",
        case_warrant: "◆ เหตุการณ์ทั่วไปปกติ ไม่พบการกระทำความผิดรุนแรง",
        has_evidence: false
      }}
    }};

    // Auto Sync Station Name to ALL references
    function handleStationThChange(val) {{
      syncField('station_th', val);
      const cmdStn = document.getElementById('view_cmd_stn');
      if (cmdStn) cmdStn.innerText = val;
      const wmTh = document.getElementById('view_wm_th');
      if (wmTh && wmTh.innerText.includes('สภ.')) wmTh.innerText = 'งานสืบสวน ' + val;
      const fStn = document.getElementById('view_footer_station');
      if (fStn) fStn.innerText = val;
      const inputFStn = document.getElementById('input_footer_station');
      if (inputFStn) inputFStn.value = val;
    }}

    function handleStationEnChange(val) {{
      syncField('station_en', val);
      const cleanEn = val.replace(/POLICE\\s*STATION/gi, '').trim();
      const wmEn = document.getElementById('view_wm_en');
      if (wmEn && cleanEn) wmEn.innerText = cleanEn + ' INVESTIGATION';
    }}

    function applyPreset(key) {{
      const p = casePresets[key];
      if (!p) return;
      document.getElementById('input_suspect_action').value = p.suspect_action;
      document.getElementById('input_suspect_name').value = p.suspect_name;
      document.getElementById('input_suspect_age').value = p.suspect_age;
      document.getElementById('input_case_charge').value = p.case_charge;
      document.getElementById('input_case_warrant').value = p.case_warrant;

      syncField('suspect_action', p.suspect_action);
      syncField('suspect_name', p.suspect_name);
      syncField('suspect_age', p.suspect_age);
      syncField('case_charge', p.case_charge);
      syncField('case_warrant', p.case_warrant);

      const chkEv = document.getElementById('chk_has_evidence');
      chkEv.checked = p.has_evidence;
      toggleEvidenceBox(p.has_evidence);
      if (p.has_evidence && p.evidence_items) {{
        document.getElementById('input_evidence_items').value = p.evidence_items;
        syncField('evidence_items', p.evidence_items);
      }}
      if (p.order_evidence_first) {{
        setEvidenceOrder(true);
      }} else {{
        setEvidenceOrder(false);
      }}
      showToast('เปลี่ยนประเภทคดีเรียบร้อย');
    }}

    // Toggle Evidence Box
    function toggleEvidenceBox(show) {{
      const grp = document.getElementById('evidence_input_group');
      const box = document.getElementById('view_evidence_container');
      if (show) {{
        grp.style.display = 'block';
        box.classList.add('active');
      }} else {{
        grp.style.display = 'none';
        box.classList.remove('active');
      }}
      adjustPosterScale();
    }}

    // Toggle Optional Sub-Footer
    function toggleSubFooter(show) {{
      const footer = document.getElementById('optionalFooter');
      const inputs = document.getElementById('subfooter_inputs');
      if (footer) footer.style.display = show ? 'flex' : 'none';
      if (inputs) inputs.style.display = show ? 'flex' : 'none';
      adjustPosterScale();
    }}

    // Dynamic Font Sizing Logic
    let currentGlobalScale = 1.0;
    let sectionScales = {{
      charge: 1.0,
      officers: 1.0,
      station: 1.0
    }};

    function setGlobalFontSize(scale) {{
      currentGlobalScale = Math.min(1.35, Math.max(0.8, Math.round(scale * 100) / 100));
      applyFontSizes();
      showToast('ปรับขนาดตัวหนังสือ: ' + Math.round(currentGlobalScale * 100) + '%');
    }}

    function adjustGlobalFontSize(delta) {{
      setGlobalFontSize(currentGlobalScale + delta);
    }}

    function onGlobalSliderChange(val) {{
      setGlobalFontSize(parseFloat(val) / 100);
    }}

    function onSectionSliderChange(section, val) {{
      const scale = parseFloat(val) / 100;
      sectionScales[section] = scale;
      const valEl = document.getElementById('slider' + capitalize(section) + 'Val');
      if (valEl) valEl.innerText = val + '%';
      applyFontSizes();
    }}

    function capitalize(s) {{
      return s.charAt(0).toUpperCase() + s.slice(1);
    }}

    function applyFontSizes() {{
      const poster = document.getElementById('reportPoster');
      if (!poster) return;

      poster.style.setProperty('--fs-global', currentGlobalScale);
      poster.style.setProperty('--fs-charge-scale', sectionScales.charge);
      poster.style.setProperty('--fs-officers-scale', sectionScales.officers);
      poster.style.setProperty('--fs-station-scale', sectionScales.station);

      // Update UI displays
      const percent = Math.round(currentGlobalScale * 100);
      const display = document.getElementById('fontScaleDisplay');
      if (display) display.innerText = percent + '%';
      const sliderGlobal = document.getElementById('sliderGlobalFont');
      if (sliderGlobal) sliderGlobal.value = percent;
      const sliderGlobalVal = document.getElementById('sliderGlobalVal');
      if (sliderGlobalVal) sliderGlobalVal.innerText = percent + '%';

      // Update preset buttons state
      ['90', '100', '110', '120'].forEach(p => {{
        const btn = document.getElementById('btnFs' + p);
        if (btn) {{
          if (parseInt(p) === percent) {{
            btn.style.background = '#0284c7';
            btn.style.color = '#ffffff';
            btn.style.borderColor = '#0284c7';
            btn.style.fontWeight = '700';
          }} else {{
            btn.style.background = '#1e293b';
            btn.style.color = '#94a3b8';
            btn.style.borderColor = '#334155';
            btn.style.fontWeight = '400';
          }}
        }}
      }});

      adjustPosterScale();
    }}

    function resetAllFontSizes() {{
      currentGlobalScale = 1.0;
      sectionScales = {{ charge: 1.0, officers: 1.0, station: 1.0 }};
      ['charge', 'officers', 'station'].forEach(s => {{
        const slider = document.getElementById('slider' + capitalize(s) + 'Font');
        if (slider) slider.value = 100;
        const valEl = document.getElementById('slider' + capitalize(s) + 'Val');
        if (valEl) valEl.innerText = '100%';
      }});
      applyFontSizes();
      showToast('รีเซ็ตขนาดตัวหนังสือเรียบร้อย');
    }}

    // Change Photo Layout (1 or 2 photos)
    function changePhotoLayout(layout) {{
      const grid = document.getElementById('photosGrid');
      const p2 = document.getElementById('photo2Frame');
      const p2Grp = document.getElementById('photo2_group');
      grid.className = 'photos-grid ' + layout;
      if (layout === 'layout-1') {{
        p2.style.display = 'none';
        if (p2Grp) p2Grp.style.display = 'none';
        selectPhotoSlot('photo1');
      }} else {{
        p2.style.display = 'flex';
        if (p2Grp) p2Grp.style.display = 'block';
      }}
      adjustPosterScale();
    }}

    // Active Photo Slot Tracking for Click & Ctrl+V Paste
    function selectPhotoSlot(slot) {{
      activeSlot = slot;
      document.getElementById('photo1Frame').classList.toggle('active-slot', slot === 'photo1');
      document.getElementById('photo2Frame').classList.toggle('active-slot', slot === 'photo2');
      document.getElementById(slot + 'Input').click();
    }}

    // Paste from Clipboard (Ctrl+V) directly into active photo slot
    window.addEventListener('paste', function(e) {{
      const items = (e.clipboardData || e.originalEvent.clipboardData).items;
      for (let i = 0; i < items.length; i++) {{
        if (items[i].type.indexOf('image') !== -1) {{
          const blob = items[i].getAsFile();
          const reader = new FileReader();
          reader.onload = function(evt) {{
            setPhotoSrc(activeSlot, evt.target.result);
            showToast('วางรูปภาพ (Ctrl+V) ลงใน' + (activeSlot === 'photo2' ? 'รูปที่ 2' : 'รูปที่ 1') + ' สำเร็จ');
            adjustPosterScale();
          }};
          reader.readAsDataURL(blob);
          break;
        }}
      }}
    }});

    // Drag and Drop Support for Photos
    function initDragAndDrop() {{
      ['photo1Frame', 'photo2Frame'].forEach(id => {{
        const frame = document.getElementById(id);
        if (!frame) return;
        frame.addEventListener('dragover', (e) => {{
          e.preventDefault();
          frame.style.borderColor = '#2563eb';
          frame.style.background = '#eff6ff';
        }});
        frame.addEventListener('dragleave', (e) => {{
          e.preventDefault();
          frame.style.borderColor = '#94a3b8';
          frame.style.background = '#f1f5f9';
        }});
        frame.addEventListener('drop', (e) => {{
          e.preventDefault();
          frame.style.borderColor = '#94a3b8';
          frame.style.background = '#f1f5f9';
          if (e.dataTransfer.files && e.dataTransfer.files[0]) {{
            const file = e.dataTransfer.files[0];
            const target = id === 'photo2Frame' ? 'photo2' : 'photo1';
            const reader = new FileReader();
            reader.onload = function(evt) {{
              setPhotoSrc(target, evt.target.result);
              showToast('อัปโหลดรูปภาพสำเร็จ');
              adjustPosterScale();
            }};
            reader.readAsDataURL(file);
          }}
        }});
      }});
    }}

    // Function to reorder Evidence Box vs Charge Card
    function setEvidenceOrder(evidenceFirst) {{
      const rightCol = document.querySelector('.body-col-right');
      const evBox = document.getElementById('view_evidence_container');
      const chgBox = document.getElementById('view_charge_container');
      const btnEv = document.getElementById('btnOrderEvFirst');
      const btnChg = document.getElementById('btnOrderChargeFirst');
      if (!rightCol || !evBox || !chgBox) return;

      if (evidenceFirst) {{
        rightCol.insertBefore(evBox, chgBox);
        if (btnEv) {{ btnEv.style.background = '#0284c7'; btnEv.style.color = '#fff'; }}
        if (btnChg) {{ btnChg.style.background = '#f1f5f9'; btnChg.style.color = '#334155'; }}
      }} else {{
        rightCol.insertBefore(chgBox, evBox);
        if (btnChg) {{ btnChg.style.background = '#0284c7'; btnChg.style.color = '#fff'; }}
        if (btnEv) {{ btnEv.style.background = '#f1f5f9'; btnEv.style.color = '#334155'; }}
      }}
      adjustPosterScale();
    }}

    // Full-Screen Preview Modal Functions
    function openPreviewModal() {{
      const modal = document.getElementById('previewModal');
      const container = document.getElementById('modalPosterContainer');
      const poster = document.getElementById('reportPoster');
      if (!modal || !container || !poster) return;
      
      container.innerHTML = '';
      const clone = poster.cloneNode(true);
      clone.id = 'reportPosterClone';
      clone.style.boxShadow = '0 12px 36px rgba(0,0,0,0.5)';
      clone.style.margin = '0 auto';
      container.appendChild(clone);
      modal.style.display = 'flex';
      document.body.style.overflow = 'hidden';
    }}

    function closePreviewModal() {{
      const modal = document.getElementById('previewModal');
      if (modal) modal.style.display = 'none';
      document.body.style.overflow = 'auto';
    }}

    // Responsive Auto Scale: guarantees zero mobile horizontal scroll and 100% full poster visibility without collapsing
    function adjustPosterScale() {{
      const wrapper = document.querySelector('.poster-scale-wrapper');
      const container = document.getElementById('posterScaleContainer');
      const poster = document.getElementById('reportPoster');
      if (!wrapper || !container || !poster) return;

      // Reset container height so child poster measures natural content height
      container.style.height = 'auto';

      const naturalHeight = poster.scrollHeight || poster.offsetHeight;
      const parentWidth = wrapper.parentElement ? wrapper.parentElement.clientWidth : wrapper.clientWidth;
      const availableWidth = Math.min(parentWidth, window.innerWidth);

      if (availableWidth < 730 && availableWidth > 0) {{
        const scale = Math.min(1, Math.max(0.25, (availableWidth - 16) / 720));
        container.style.transform = `scale(${{scale}})`;
        container.style.transformOrigin = 'top center';
        const scaledHeight = Math.ceil(naturalHeight * scale) + 24;
        wrapper.style.height = `${{scaledHeight}}px`;
      }} else {{
        container.style.transform = 'none';
        container.style.height = 'auto';
        wrapper.style.height = 'auto';
      }}
    }}

    window.addEventListener('resize', adjustPosterScale);
    window.addEventListener('DOMContentLoaded', () => {{
      initDragAndDrop();
      setTimeout(adjustPosterScale, 150);
    }});

    // Sync from Form to Live Poster
    function syncField(key, val) {{
      const viewEl = document.getElementById('view_' + key);
      if (viewEl) {{
        if (key === 'lead_officers' || key === 'joint_officers') {{
          const formatted = val.split('\\n').map(line => {{
            const trim = line.trim();
            if (!trim) return '';
            if (trim.startsWith('เจ้าพนักงาน') || trim.startsWith('ชุดจับกุม')) {{
              return `<div class="officers-subgroup-title">${{line}}</div>`;
            }}
            if (trim.startsWith('•')) {{
              return `<div class="officer-item"><strong>${{line}}</strong></div>`;
            }}
            // Force BOLD for พร้อมกำลัง, สายตรวจ, หรือเริ่มต้นด้วย พร้อม
            if (trim.includes('พร้อมกำลัง') || trim.includes('สายตรวจ') || trim.startsWith('พร้อม')) {{
              return `<div class="officer-item bold-line" style="margin-top:3px; font-weight:700; color:#0c3166;"><strong>${{line}}</strong></div>`;
            }}
            if (line.startsWith(' ') || line.startsWith('\\t')) {{
              return `<div class="officer-item" style="padding-left:12px; color:#475569;">${{trim}}</div>`;
            }}
            return `<div class="officer-item">${{line}}</div>`;
          }}).join('');
          viewEl.innerHTML = formatted;
        }} else if (key === 'evidence_items') {{
          const formatted = val.split('\\n').map(line => {{
            const trim = line.trim();
            if (!trim) return '';
            return `<div>${{trim.startsWith('•') ? trim : '• ' + trim}}</div>`;
          }}).join('');
          viewEl.innerHTML = formatted;
        }} else if (key === 'case_warrant') {{
          viewEl.innerText = val;
          if (!val || !val.trim()) {{
            viewEl.style.display = 'none';
          }} else {{
            viewEl.style.display = 'block';
          }}
        }} else {{
          viewEl.innerText = val;
        }}
        adjustPosterScale();
      }}
    }}

    // Sync from Live Poster (contenteditable) to Form Input
    function syncInput(key, val) {{
      const inputEl = document.getElementById('input_' + key);
      if (inputEl) {{
        inputEl.value = val.trim();
      }}
    }}

    function syncInputTextarea(key, html) {{
      const inputEl = document.getElementById('input_' + key);
      if (inputEl) {{
        const temp = document.createElement('div');
        temp.innerHTML = html.replace(/<br\\s*\\/?>/gi, '\\n').replace(/<\\/div>/gi, '\\n');
        inputEl.value = temp.innerText.trim();
      }}
    }}

    // Accordion Toggle
    function toggleAccordion(header) {{
      const content = header.nextElementSibling;
      const arrow = header.querySelector('span:last-child');
      if (content.style.display === 'none') {{
        content.style.display = 'flex';
        arrow.innerText = '▼';
      }} else {{
        content.style.display = 'none';
        arrow.innerText = '▶';
      }}
    }}

    // 3 Lead Commander Presets
    const leadCommanderPresets = {{
      1: {{
        name: "พ.ต.ต.อัครเดช แก้วร่องคำ",
        pos: "สวป.สภ.บางปะกง",
        text: `• พ.ต.ต.อัครเดช แก้วร่องคำ
  สวป.สภ.บางปะกง
• ร.ต.อ.วิโรจน์ เทศทอง
  รอง สวป. สภ.บางปะกง
พร้อมกำลังสายตรวจ สภ.บางปะกง`
      }},
      2: {{
        name: "พ.ต.ท.ชวกร บุษมงคล",
        pos: "สว.(สอบสวน) สภ.บางปะกง",
        text: `• พ.ต.ท.ชวกร บุษมงคล
  สว.(สอบสวน) สภ.บางปะกง
• ร.ต.อ.วิโรจน์ เทศทอง
  รอง สวป. สภ.บางปะกง
พร้อมกำลังสายตรวจ สภ.บางปะกง`
      }},
      3: {{
        name: "พ.ต.ท.นิสิต ศรีโคตร",
        pos: "สวป.(ชส) สภ.บางปะกง",
        text: `• พ.ต.ท.นิสิต ศรีโคตร
  สวป.(ชส) สภ.บางปะกง
• ร.ต.อ.วิโรจน์ เทศทอง
  รอง สวป. สภ.บางปะกง
พร้อมกำลังสายตรวจ สภ.บางปะกง`
      }}
    }};

    function selectLeadCommander(key) {{
      const p = leadCommanderPresets[key];
      if (!p) return;
      const input = document.getElementById('input_lead_officers');
      if (input) {{
        input.value = p.text;
        syncField('lead_officers', p.text);
      }}
      const sel = document.getElementById('select_lead_commander');
      if (sel) sel.value = key;
      showToast('เลือกหัวหน้าชุด: ' + p.name);
    }}

    // 7 Default Joint Patrol Officers
    const defaultJointOfficers = [
      "ส.ต.อ. อนุวัฒน์ บุตรทาสี",
      "ส.ต.ท. สิทธิโชค วิวัฒนพงศ์พันธ์",
      "ส.ต.ท. ทรงพล บุญไสย์",
      "ส.ต.ท. กฤษดา บูรณะกิติ",
      "ส.ต.ต. พัสกร อยู่ยืน",
      "ส.ต.ต. จิตติ แสงสว่าง",
      "ส.ต.ต. อนุชา พงษ์ราช"
    ];

    function updateJointFromChecklist() {{
      const selected = [];
      defaultJointOfficers.forEach((name, i) => {{
        const chk = document.getElementById('chk_joint_' + i);
        if (chk && chk.checked) {{
          selected.push('• ' + name);
        }}
      }});
      const text = selected.join('\\n');
      document.getElementById('input_joint_officers').value = text;
      syncField('joint_officers', text);
    }}

    function toggleAllJoint(checkAll) {{
      defaultJointOfficers.forEach((name, i) => {{
        const chk = document.getElementById('chk_joint_' + i);
        if (chk) chk.checked = checkAll;
      }});
      updateJointFromChecklist();
    }}

    // Trigger Photo Upload
    function triggerPhotoUpload(target) {{
      selectPhotoSlot(target);
      const input = document.getElementById(target + 'Input');
      if (input) input.click();
    }}

    // Set Photo Src and Toggle Placeholder vs Image
    function setPhotoSrc(target, src) {{
      const img = document.getElementById(target + 'Img');
      const placeholder = document.getElementById(target + 'Placeholder');
      const frame = document.getElementById(target + 'Frame');
      const wm = (target === 'photo1') ? document.getElementById('photo1Watermark') : null;
      if (!img || !placeholder) return;

      if (src && src.trim()) {{
        img.src = src;
        img.style.display = 'block';
        placeholder.style.display = 'none';
        if (wm) wm.style.display = 'block';
        if (frame) frame.classList.add('has-photo');
      }} else {{
        img.src = '';
        img.style.display = 'none';
        placeholder.style.display = 'flex';
        if (wm) wm.style.display = 'none';
        if (frame) frame.classList.remove('has-photo');
      }}
    }}

    // Remove / Clear Photo back to placeholder
    function removePhoto(target, event) {{
      if (event) event.stopPropagation();
      setPhotoSrc(target, '');
      const input = document.getElementById(target + 'Input');
      if (input) input.value = '';
      showToast('ลบรูปภาพเรียบร้อย');
      adjustPosterScale();
    }}

    // Photo Upload Handler
    function handlePhotoUpload(event, target) {{
      const file = event.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {{
        setPhotoSrc(target, e.target.result);
        showToast('อัปโหลดรูปภาพสำเร็จ');
        adjustPosterScale();
      }};
      reader.readAsDataURL(file);
    }}

    // Badge Upload Handler
    function handleBadgeUpload(event) {{
      const file = event.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {{
        document.getElementById('badgeImg').src = e.target.result;
        const wm = document.getElementById('watermarkBadgeImg');
        if (wm) wm.src = e.target.result;
        showToast('เปลี่ยนตราโลโก้เรียบร้อย');
      }};
      reader.readAsDataURL(file);
    }}

    // Toggle Censor Face
    function toggleCensor(isCensored) {{
      const p1 = document.getElementById('photo1Img');
      const p2 = document.getElementById('photo2Img');
      if (isCensored) {{
        p1.style.filter = "contrast(1.05)";
        p2.style.filter = "contrast(1.05)";
        showToast('เปิดโหมดเซ็นเซอร์ผู้ต้องหา');
      }} else {{
        p1.style.filter = "none";
        p2.style.filter = "none";
      }}
    }}

    // Print & PDF
    function printReport() {{
      window.print();
    }}

    // Export to High-Res PNG Image
    function exportToImage() {{
      const poster = document.getElementById('reportPoster');
      const container = document.getElementById('posterScaleContainer');
      const btn = document.getElementById('exportBtn');
      const origText = btn.innerHTML;
      btn.innerHTML = '⏳ กำลังสร้างภาพ...';
      btn.disabled = true;

      // Temporarily remove transform for accurate rendering
      const wrapper = document.querySelector('.poster-scale-wrapper');
      const prevTransform = container.style.transform;
      const prevHeight = container.style.height;
      const prevWrapperHeight = wrapper ? wrapper.style.height : '';
      container.style.transform = 'none';
      container.style.height = 'auto';
      if (wrapper) wrapper.style.height = 'auto';

      html2canvas(poster, {{
        scale: 2,
        useCORS: true,
        allowTaint: true,
        backgroundColor: '#ffffff'
      }}).then(canvas => {{
        container.style.transform = prevTransform;
        container.style.height = prevHeight;
        if (wrapper) wrapper.style.height = prevWrapperHeight;

        const link = document.createElement('a');
        const stn = document.getElementById('view_station_th').innerText.trim() || 'ตำรวจ';
        const dateStr = document.getElementById('view_report_date').innerText.trim().replace(/[\\s\\/]/g, '_');
        link.download = `รายงานผลการปฏิบัติ_${{stn}}_${{dateStr}}.png`;
        link.href = canvas.toDataURL('image/png');
        link.click();

        btn.innerHTML = origText;
        btn.disabled = false;
        showToast('ดาวน์โหลดรูปภาพรายงานสำเร็จ (PNG คมชัดสูง)');
      }}).catch(err => {{
        container.style.transform = prevTransform;
        container.style.height = prevHeight;
        console.error(err);
        alert('เกิดข้อผิดพลาดในการสร้างภาพ: ' + err.message);
        btn.innerHTML = origText;
        btn.disabled = false;
      }});
    }}

    // Copy formatted text for LINE group
    function copyLineText() {{
      const stn = document.getElementById('input_station_th').value || document.getElementById('view_station_th').innerText;
      const date = document.getElementById('input_report_date').value || document.getElementById('view_report_date').innerText;
      const time = document.getElementById('input_report_time').value || document.getElementById('view_report_time').innerText;
      const cmd1 = (document.getElementById('input_cmd1_name').value || document.getElementById('view_cmd1_name').innerText) + ' ' + (document.getElementById('input_cmd1_pos').value || document.getElementById('view_cmd1_pos').innerText);
      const cmd2 = (document.getElementById('input_cmd2_name').value || document.getElementById('view_cmd2_name').innerText) + ' ' + (document.getElementById('input_cmd2_pos').value || document.getElementById('view_cmd2_pos').innerText);
      const lead = document.getElementById('input_lead_officers').value;
      const joint = document.getElementById('input_joint_officers').value;
      const suspectAction = document.getElementById('input_suspect_action').value || document.getElementById('view_suspect_action').innerText;
      const suspectName = document.getElementById('input_suspect_name').value || document.getElementById('view_suspect_name').innerText;
      const suspectAge = document.getElementById('input_suspect_age').value || document.getElementById('view_suspect_age').innerText;
      const suspectId = document.getElementById('input_suspect_id').value || document.getElementById('view_suspect_id').innerText;
      const suspectAddr = document.getElementById('input_suspect_addr').value || document.getElementById('view_suspect_addr').innerText;
      const charge = document.getElementById('input_case_charge').value || document.getElementById('view_case_charge').innerText;
      const warrant = document.getElementById('input_case_warrant').value || document.getElementById('view_case_warrant').innerText;
      const loc = document.getElementById('input_case_location').value || document.getElementById('view_case_location').innerText;
      const action = document.getElementById('input_case_action').value || document.getElementById('view_case_action').innerText;
      const hasEv = document.getElementById('chk_has_evidence').checked;
      const evItems = document.getElementById('input_evidence_items').value;

      let lineText = `เรียน ผู้บังคับบัญชา
${{stn}} ขอรายงานผลการปฏิบัติ ประจำ${{date}} ${{time}}

【ภายใต้การอำนวยการของ】
- ${{cmd1}}
- ${{cmd2}}

【นำโดย】
${{lead}}

【พร้อมด้วย】
${{joint}}

【ผลการปฏิบัติ】
${{suspectAction}}
- ${{suspectName}} (${{suspectAge}})
${{suspectId}}
ที่อยู่: ${{suspectAddr}}

【กระทำความผิดฐาน】
${{charge}}
${{warrant}}`;

      if (hasEv && evItems.trim()) {{
        lineText += `\\n\\n【ของกลางที่ตรวจยึด】\\n${{evItems}}`;
      }}

      lineText += `\\n\\n【สถานที่จับกุม】
${{loc}}

【การดำเนินการ】
${{action}}

จึงเรียนมาเพื่อโปรดทราบ`;

      navigator.clipboard.writeText(lineText).then(() => {{
        showToast('คัดลอกข้อความสรุปสำหรับส่ง LINE เรียบร้อยแล้ว!');
      }}).catch(() => {{
        const ta = document.createElement('textarea');
        ta.value = lineText;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showToast('คัดลอกข้อความสรุปสำหรับส่ง LINE เรียบร้อยแล้ว!');
      }});
    }}

    // Save Draft as JSON
    function saveDraftJSON() {{
      const data = {{}};
      for (let key in defaultData) {{
        const el = document.getElementById('input_' + key);
        if (el) {{
          data[key] = el.value;
        }}
      }}
      data.lead_officers = document.getElementById('input_lead_officers').value;
      data.joint_officers = document.getElementById('input_joint_officers').value;
      data.evidence_items = document.getElementById('input_evidence_items').value;
      data.has_evidence = document.getElementById('chk_has_evidence').checked;
      data.photo_layout = document.getElementById('photoLayoutSelect').value;
      data.badge = document.getElementById('badgeImg').src;
      data.photo1 = document.getElementById('photo1Img').src;
      data.photo2 = document.getElementById('photo2Img').src;
      data.font_global_scale = currentGlobalScale;
      data.font_section_scales = sectionScales;

      const blob = new Blob([JSON.stringify(data, null, 2)], {{ type: 'application/json' }});
      const link = document.createElement('a');
      link.download = 'ข้อมูลรายงานผลการปฏิบัติ.json';
      link.href = URL.createObjectURL(blob);
      link.click();
      showToast('บันทึกแบบร่าง JSON เรียบร้อย');
    }}

    // Load Draft from JSON
    function loadDraftJSON(event) {{
      const file = event.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {{
        try {{
          const data = JSON.parse(e.target.result);
          for (let key in data) {{
            if (key === 'badge' && data.badge) {{
              document.getElementById('badgeImg').src = data.badge;
              const wm = document.getElementById('watermarkBadgeImg');
              if (wm) wm.src = data.badge;
            }} else if (key === 'photo1' && data.photo1) {{
              document.getElementById('photo1Img').src = data.photo1;
            }} else if (key === 'photo2' && data.photo2) {{
              document.getElementById('photo2Img').src = data.photo2;
            }} else if (key === 'has_evidence') {{
              document.getElementById('chk_has_evidence').checked = data[key];
              toggleEvidenceBox(data[key]);
            }} else if (key === 'photo_layout') {{
              document.getElementById('photoLayoutSelect').value = data[key];
              changePhotoLayout(data[key]);
            }} else if (key === 'font_global_scale') {{
              currentGlobalScale = parseFloat(data[key]) || 1.0;
            }} else if (key === 'font_section_scales') {{
              sectionScales = Object.assign(sectionScales, data[key]);
            }} else {{
              const inputEl = document.getElementById('input_' + key);
              if (inputEl) inputEl.value = data[key];
              syncField(key, data[key]);
            }}
          }}
          applyFontSizes();
          showToast('โหลดข้อมูลแบบร่างเรียบร้อย');
          adjustPosterScale();
        }} catch(err) {{
          alert('ไฟล์ JSON ไม่ถูกต้อง');
        }}
      }};
      reader.readAsText(file);
    }}

    // Reset to Sample
    function resetToSample() {{
      if (confirm('คุณต้องการรีเซ็ตข้อมูลทั้งหมดกลับเป็นค่าตัวอย่างเริ่มต้นใช่หรือไม่?')) {{
        location.reload();
      }}
    }}

    // Toast helper
    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => {{
        t.classList.remove('show');
      }}, 3000);
    }}
  </script>
  <!-- FULL SCREEN PREVIEW MODAL -->
  <div id="previewModal" class="preview-modal" style="display:none;" onclick="closePreviewModal()">
    <div class="preview-modal-bar" onclick="event.stopPropagation()">
      <span style="font-weight:700; color:white; font-size:0.95rem; display:flex; align-items:center; gap:6px;">
        🔍 ภาพตัวอย่างขนาดเต็ม (เลื่อนดูและซูมได้)
      </span>
      <div style="display:flex; gap:8px;">
        <button class="btn btn-sm btn-success" onclick="exportToImage()" style="padding:5px 14px; font-weight:bold; font-size:0.8rem;">
          📸 บันทึกรูป (PNG)
        </button>
        <button class="btn btn-sm btn-danger" onclick="closePreviewModal()" style="padding:5px 14px; font-weight:bold; font-size:0.8rem; background:#ef4444; color:white; border:none; border-radius:6px; cursor:pointer;">
          ✕ ปิด
        </button>
      </div>
    </div>
    <div class="preview-modal-content" onclick="event.stopPropagation()">
      <div id="modalPosterContainer"></div>
    </div>
  </div>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html with header clipping fix successfully!")
