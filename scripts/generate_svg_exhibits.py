# -*- coding: utf-8 -*-
"""
generate_svg_exhibits.py
為陳海賢《自我發展心理學》16 頁無雜訊簡報生成 16 幅高解析度、頂尖管顧風格向量 SVG 展覽圖 (Exhibits 1-16)
色彩規範：McKinsey Deep Navy (#051C2C), BCG Forest Green (#004F32), Accent Gold (#D97706), Tech Purple (#A100FF), Cyan (#06B6D4)
"""

import os

OUTPUT_DIR = r"C:\Users\davidyeh\Documents\Codex\psychology-portal\images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Helper function to write SVG
def write_svg(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"[OK] Generated {filename}")

# Exhibit 1: 封面展覽圖 - 心理系統演化與自我突破徽章
svg_01 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#051C2C" />
      <stop offset="50%" stop-color="#0F2942" />
      <stop offset="100%" stop-color="#1E3A8A" />
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>
  <rect width="800" height="450" rx="16" fill="url(#bgGrad1)" />
  <circle cx="400" cy="225" r="180" fill="none" stroke="#2563EB" stroke-width="1.5" stroke-dasharray="6,6" opacity="0.3" />
  <circle cx="400" cy="225" r="130" fill="none" stroke="#60A5FA" stroke-width="2" opacity="0.5" />
  <circle cx="400" cy="225" r="80" fill="#0A2540" stroke="url(#goldGrad)" stroke-width="3" filter="url(#shadow)" />
  
  <!-- Central Icon: System Evolution / Inner Growth -->
  <path d="M400 175 L415 210 L452 214 L424 238 L432 274 L400 255 L368 274 L376 238 L348 214 L385 210 Z" fill="url(#goldGrad)" />
  <text x="400" y="240" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="bold" fill="#051C2C" text-anchor="middle">EVOLVE</text>

  <!-- 5 Nodes around the circle -->
  <!-- Node 1: 行為 -->
  <g transform="translate(400, 70)">
    <rect x="-65" y="-22" width="130" height="44" rx="22" fill="#0B3056" stroke="#38BDF8" stroke-width="2" filter="url(#shadow)" />
    <text x="0" y="5" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">01 行為新經驗</text>
  </g>
  <!-- Node 2: 思維 -->
  <g transform="translate(560, 160)">
    <rect x="-65" y="-22" width="130" height="44" rx="22" fill="#0B3056" stroke="#38BDF8" stroke-width="2" filter="url(#shadow)" />
    <text x="0" y="5" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">02 心智成長型</text>
  </g>
  <!-- Node 3: 關係 -->
  <g transform="translate(510, 340)">
    <rect x="-65" y="-22" width="130" height="44" rx="22" fill="#0B3056" stroke="#38BDF8" stroke-width="2" filter="url(#shadow)" />
    <text x="0" y="5" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">03 關係去三角</text>
  </g>
  <!-- Node 4: 轉折 -->
  <g transform="translate(290, 340)">
    <rect x="-65" y="-22" width="130" height="44" rx="22" fill="#0B3056" stroke="#38BDF8" stroke-width="2" filter="url(#shadow)" />
    <text x="0" y="5" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">04 轉折重生期</text>
  </g>
  <!-- Node 5: 地圖 -->
  <g transform="translate(240, 160)">
    <rect x="-65" y="-22" width="130" height="44" rx="22" fill="#0B3056" stroke="#38BDF8" stroke-width="2" filter="url(#shadow)" />
    <text x="0" y="5" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">05 人生地圖使命</text>
  </g>

  <!-- Connective Arrows -->
  <path d="M465 75 Q540 100 550 135" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" />
  <path d="M570 185 Q570 260 520 315" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" />
  <path d="M445 345 L355 345" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" />
  <path d="M280 315 Q230 260 230 185" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" />
  <path d="M250 135 Q260 100 335 75" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" />
  
  <text x="400" y="420" font-family="-apple-system, sans-serif" font-size="13" fill="#94A3B8" text-anchor="middle">EXHIBIT 1 ｜ 自我發展心理學五維全景系統動力模型</text>
</svg>"""
write_svg("exhibit-01-cover.svg", svg_01)

# Exhibit 2: 版型 3 結合論法 - 全書五層架構金字塔樹
svg_02 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%">
  <rect width="900" height="480" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <!-- 頂層：最終結論 -->
  <rect x="150" y="25" width="600" height="75" rx="8" fill="#051C2C" />
  <text x="450" y="55" font-family="-apple-system, sans-serif" font-size="18" font-weight="bold" fill="#F8FAFC" text-anchor="middle">【頂層結論】自我發展的本質是「心理系統的升級」</text>
  <text x="450" y="80" font-family="-apple-system, sans-serif" font-size="13" fill="#38BDF8" text-anchor="middle">非單純意志力壓制 ｜ 而是認知、情感、關係與生命週期的全維重構</text>
  
  <!-- 中層三支柱 -->
  <!-- 支柱 1 -->
  <rect x="40" y="145" width="250" height="120" rx="8" fill="#FFFFFF" stroke="#004F32" stroke-width="2" />
  <rect x="40" y="145" width="250" height="32" rx="8" fill="#004F32" />
  <text x="165" y="167" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">支柱一：行動系統重構</text>
  <text x="55" y="200" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 象與騎象人：情感動力優先</text>
  <text x="55" y="222" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 心理免疫：看清隱含好處</text>
  <text x="55" y="244" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 小步子＋環境場：創造新經驗</text>

  <!-- 支柱 2 -->
  <rect x="325" y="145" width="250" height="120" rx="8" fill="#FFFFFF" stroke="#051C2C" stroke-width="2" />
  <rect x="325" y="145" width="250" height="32" rx="8" fill="#051C2C" />
  <text x="450" y="167" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">支柱二：心智模型躍遷</text>
  <text x="340" y="200" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 成長型思維：把犯錯當數據</text>
  <text x="340" y="222" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 破除應該思維：願望≠事實</text>
  <text x="340" y="244" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• WOOP＋控制兩分法：聚焦可控</text>

  <!-- 支柱 3 -->
  <rect x="610" y="145" width="250" height="120" rx="8" fill="#FFFFFF" stroke="#6B21A8" stroke-width="2" />
  <rect x="610" y="145" width="250" height="32" rx="8" fill="#6B21A8" />
  <text x="735" y="167" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">支柱三：關係系統演化</text>
  <text x="625" y="200" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 聽懂話外音：關係資訊維度</text>
  <text x="625" y="222" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 去三角化：退出夾心人角色</text>
  <text x="625" y="244" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 課題分離＋NVC：邊界清明</text>

  <!-- 底層進階場景 -->
  <rect x="40" y="310" width="395" height="125" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
  <rect x="40" y="310" width="395" height="28" fill="#E2E8F0" />
  <text x="237" y="329" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">進階場景 A：轉折期三階段與意義重生</text>
  <text x="55" y="360" font-family="-apple-system, sans-serif" font-size="12" fill="#334155">• 威廉·布里奇斯轉折模型：結束 ➔ 迷茫中性區 ➔ 重生啟程</text>
  <text x="55" y="382" font-family="-apple-system, sans-serif" font-size="12" fill="#334155">• 職業轉型：以「多元可能自我 (Ibarra)」平行小步實驗</text>
  <text x="55" y="404" font-family="-apple-system, sans-serif" font-size="12" fill="#334155">• 英雄之旅與救贖敘事：將苦難經驗轉化為自我進化恩賜</text>

  <rect x="465" y="310" width="395" height="125" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
  <rect x="465" y="310" width="395" height="28" fill="#E2E8F0" />
  <text x="662" y="329" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">進階場景 B：埃里克森生命地圖與終極使命</text>
  <text x="480" y="360" font-family="-apple-system, sans-serif" font-size="12" fill="#334155">• 青春期（自我同一性）➔ 確立我是誰與真實方向</text>
  <text x="480" y="382" font-family="-apple-system, sans-serif" font-size="12" fill="#334155">• 成年早期（親密與立業）➔ 敞開去愛與專長深耕</text>
  <text x="480" y="404" font-family="-apple-system, sans-serif" font-size="12" fill="#334155">• 中年期（繁殖傳承）➔ 晚年期（自我整合與人生坦然）</text>

  <!-- Connective Arrows -->
  <path d="M450 100 L450 145" stroke="#051C2C" stroke-width="2" />
  <path d="M250 100 L165 145" stroke="#004F32" stroke-width="2" />
  <path d="M650 100 L735 145" stroke="#6B21A8" stroke-width="2" />
  
  <text x="450" y="465" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 2 ｜ 結合論法：三層金字塔演繹推導五大維度共構系統</text>
</svg>"""
write_svg("exhibit-02-combined-tree.svg", svg_02)

# Exhibit 3: 大象與騎象人 + 新經驗驅動迴路 (版型 4: 連鎖論法)
svg_03 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <!-- Left Side: Rider & Elephant Concept -->
  <g transform="translate(40, 40)">
    <rect width="360" height="370" rx="10" fill="#FFFFFF" stroke="#004F32" stroke-width="2" />
    <rect width="360" height="40" rx="10" fill="#004F32" />
    <text x="180" y="26" font-family="-apple-system, sans-serif" font-size="15" font-weight="bold" fill="#FFFFFF" text-anchor="middle">海特心理模型：象與騎象人</text>
    
    <!-- Rider -->
    <rect x="30" y="65" width="300" height="90" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5" />
    <text x="50" y="92" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#004F32">【騎象人】理性與邏輯 (Rider)</text>
    <text x="50" y="115" font-family="-apple-system, sans-serif" font-size="12" fill="#374151">• 功能：指引方向、分析規劃、設想未來</text>
    <text x="50" y="135" font-family="-apple-system, sans-serif" font-size="12" fill="#DC2626">• 痛點：力量微弱、易心理耗竭、單靠意志難以持久</text>

    <!-- Elephant -->
    <rect x="30" y="175" width="300" height="110" rx="8" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5" />
    <text x="50" y="202" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#B45309">【大象】情感與潛意識 (Elephant)</text>
    <text x="50" y="225" font-family="-apple-system, sans-serif" font-size="12" fill="#374151">• 功能：提供強大前進動力、受切身體會支配</text>
    <text x="50" y="245" font-family="-apple-system, sans-serif" font-size="12" fill="#374151">• 盲點：恐懼不確定性、貪戀既有安全感、容易退縮</text>
    <text x="50" y="265" font-family="-apple-system, sans-serif" font-size="12" fill="#15803D">• 核心心法：以「愛與期待」引導，創造「新經驗的好處」</text>
    
    <rect x="30" y="305" width="300" height="80" rx="8" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1" />
    <text x="180" y="332" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#1E40AF" text-anchor="middle">改變鐵律：經驗勝過道理</text>
    <text x="180" y="355" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">「期待的好處」只在理智大腦中飄渺</text>
    <text x="180" y="372" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">「經驗的好處」才能真正讓大象自發邁步！</text>
  </g>

  <!-- Right Side: 4-Step Chain Flow -->
  <g transform="translate(430, 40)">
    <rect width="430" height="370" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
    <rect width="430" height="40" rx="10" fill="#051C2C" />
    <text x="215" y="26" font-family="-apple-system, sans-serif" font-size="15" font-weight="bold" fill="#FFFFFF" text-anchor="middle">新經驗形成的 4 步演進迴路 (Chain Flow)</text>
    
    <!-- Step 1 -->
    <rect x="25" y="60" width="380" height="65" rx="6" fill="#F8FAFC" stroke="#E2E8F0" />
    <circle cx="55" cy="92" r="16" fill="#004F32" />
    <text x="55" y="97" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1</text>
    <text x="85" y="85" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A">理性指引方向 (Direction)</text>
    <text x="85" y="105" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">騎象人看清目標，明確定義可行的具體成果，拒絕抽象空想。</text>

    <!-- Step 2 -->
    <rect x="25" y="135" width="380" height="65" rx="6" fill="#F8FAFC" stroke="#E2E8F0" />
    <circle cx="55" cy="167" r="16" fill="#004F32" />
    <text x="55" y="172" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2</text>
    <text x="85" y="160" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A">情感觸發與喚醒 (Arousal)</text>
    <text x="85" y="180" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">拒絕自責！用「微小期待」讓大象感到安全，激發前進好奇心。</text>

    <!-- Step 3 -->
    <rect x="25" y="210" width="380" height="65" rx="6" fill="#F8FAFC" stroke="#E2E8F0" />
    <circle cx="55" cy="242" r="16" fill="#004F32" />
    <text x="55" y="247" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3</text>
    <text x="85" y="235" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#0F172A">小步子與環境場 (Micro-Action)</text>
    <text x="85" y="255" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">阻力小到不可能失敗的第一步；以固定物理環境釋放行為觸發線索。</text>

    <!-- Step 4 -->
    <rect x="25" y="285" width="380" height="65" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5" />
    <circle cx="55" cy="317" r="16" fill="#15803D" />
    <text x="55" y="322" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4</text>
    <text x="85" y="310" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#166534">新經驗鞏固習慣 (Habit Loop) ★ 關鍵</text>
    <text x="85" y="330" font-family="-apple-system, sans-serif" font-size="11" fill="#15803D">大象親身體驗到多巴胺正反饋，神經迴路自發改道，舊模式自然瓦解！</text>
  </g>
  
  <text x="450" y="445" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 3 ｜ 模組一 行為改變動力學：象與騎象人協同之新經驗形成鏈</text>
</svg>"""
write_svg("exhibit-03-elephant-rider.svg", svg_03)

# Exhibit 4: 心理免疫 X 光片 (Kegan 4-Column Diagnosis)
svg_04 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 460" width="100%" height="100%">
  <rect width="920" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <!-- Header Title -->
  <rect x="30" y="20" width="860" height="42" rx="6" fill="#051C2C" />
  <text x="460" y="47" font-family="-apple-system, sans-serif" font-size="15" font-weight="bold" fill="#FFFFFF" text-anchor="middle">哈佛 Robert Kegan 心理免疫系統 X 光片 (Immunity to Change Matrix)</text>
  
  <!-- 4 Columns -->
  <!-- Col 1 -->
  <g transform="translate(30, 75)">
    <rect width="205" height="340" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="2" />
    <rect width="205" height="40" rx="8" fill="#0284C7" />
    <text x="102" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">① 渴望的改變目標</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#0369A1">【理性大腦承諾】</text>
    <text x="15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 我真正渴望達成的新行為</text>
    <text x="15" y="120" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 帶來高價值的長期願景</text>
    
    <rect x="15" y="150" width="175" height="150" rx="6" fill="#F0F9FF" />
    <text x="25" y="175" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#0369A1">【典型個案】</text>
    <text x="25" y="200" font-family="-apple-system, sans-serif" font-size="11" fill="#1E293B">「在主管會議中主動發言，爭取領導新產品研發專案」</text>
  </g>

  <!-- Col 2 -->
  <g transform="translate(248, 75)">
    <rect width="205" height="340" rx="8" fill="#FFFFFF" stroke="#EA580C" stroke-width="2" />
    <rect width="205" height="40" rx="8" fill="#EA580C" />
    <text x="102" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">② 當前的相反行為</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#C2410C">【客觀事實阻礙】</text>
    <text x="15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 我正在做、阻礙目標的事</text>
    <text x="15" y="120" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 表面看是拖延、逃避、沉默</text>
    
    <rect x="15" y="150" width="175" height="150" rx="6" fill="#FFF7ED" />
    <text x="25" y="175" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#C2410C">【典型個案】</text>
    <text x="25" y="200" font-family="-apple-system, sans-serif" font-size="11" fill="#1E293B">「會議中全程低頭記筆記、主管點名時推託給資深同事」</text>
  </g>

  <!-- Col 3 -->
  <g transform="translate(466, 75)">
    <rect width="205" height="340" rx="8" fill="#FFFFFF" stroke="#D97706" stroke-width="2" />
    <rect width="205" height="40" rx="8" fill="#D97706" />
    <text x="102" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">③ 競爭性承諾 (好處)</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#B45309">【潛意識安全保護】</text>
    <text x="15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 相反行為帶來的「隱含好處」</text>
    <text x="15" y="120" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 若做目標行為，我最怕什麼？</text>
    
    <rect x="15" y="150" width="175" height="150" rx="6" fill="#FEF3C7" />
    <text x="25" y="175" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#B45309">【典型個案】</text>
    <text x="25" y="200" font-family="-apple-system, sans-serif" font-size="11" fill="#1E293B">「承諾保護自己不成為眾人攻擊的靶子，確保不承擔出錯恥辱」</text>
  </g>

  <!-- Col 4 -->
  <g transform="translate(684, 75)">
    <rect width="205" height="340" rx="8" fill="#FFFFFF" stroke="#DC2626" stroke-width="2" />
    <rect width="205" height="40" rx="8" fill="#DC2626" />
    <text x="102" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">④ 重大心理假設 ★</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#B91C1C">【未受檢驗世界觀】</text>
    <text x="15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 支撐整套防禦系統的底層假設</text>
    <text x="15" y="120" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 設計小實驗反證其虛妄！</text>
    
    <rect x="15" y="150" width="175" height="150" rx="6" fill="#FEF2F2" />
    <text x="25" y="175" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#B91C1C">【典型個案】</text>
    <text x="25" y="200" font-family="-apple-system, sans-serif" font-size="11" fill="#1E293B">「若我主動表現卻失敗，就證明我徹底無能，將失去所有人尊重」</text>
  </g>

  <text x="460" y="442" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 4 ｜ 心理免疫四欄表：從相反行為反向推導重大假設，精準解除內在煞車</text>
</svg>"""
write_svg("exhibit-04-kegan-xray.svg", svg_04)

# Exhibit 5: 第一序列 vs 第二序列改變 (版型 6: 對立論法)
svg_05 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="450" y="38" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#051C2C" text-anchor="middle">系統控制論改變維度對比：瓦茲拉威克 (Watzlawick) 變革理論</text>
  
  <!-- Left: First Order Change -->
  <g transform="translate(40, 60)">
    <rect width="385" height="350" rx="10" fill="#FFFFFF" stroke="#94A3B8" stroke-width="2" />
    <rect width="385" height="42" rx="10" fill="#64748B" />
    <text x="192" y="27" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第一序列改變 (狀態微調・陷阱)</text>
    
    <text x="25" y="75" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#334155">【核心本質】More of the Same (更多同樣的努力)</text>
    <text x="25" y="100" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 在「既定系統與舊遊戲規則內部」微調參數</text>
    <text x="25" y="125" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 相信只要加倍努力、提高自律就能成功</text>
    
    <rect x="20" y="150" width="345" height="100" rx="6" fill="#F1F5F9" />
    <text x="35" y="175" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#DC2626">【典型致命閉環】</text>
    <text x="35" y="200" font-family="-apple-system, sans-serif" font-size="12" fill="#1E293B">失眠 ➔ 拚命逼自己睡 ➔ 精神更緊繃 ➔ 更睡不著</text>
    <text x="35" y="225" font-family="-apple-system, sans-serif" font-size="12" fill="#1E293B">「企圖解決問題的手段，本身反倒成了問題！」</text>
    
    <text x="25" y="280" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B">結果：陷入體能與心理耗竭，系統僵死在原地。</text>
  </g>

  <!-- Right: Second Order Change -->
  <g transform="translate(475, 60)">
    <rect width="385" height="350" rx="10" fill="#FFFFFF" stroke="#A100FF" stroke-width="2.5" />
    <rect width="385" height="42" rx="10" fill="#A100FF" />
    <text x="192" y="27" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第二序列改變 (規則重寫・根本突破) ★</text>
    
    <text x="25" y="75" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#6B21A8">【核心本質】Reframing &amp; Rule Rewrite (系統躍遷)</text>
    <text x="25" y="100" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 跳出既定框架，徹底改變系統運作的底層規則</text>
    <text x="25" y="125" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 重新定義問題，瓦解原有困境的成立前提</text>
    
    <rect x="20" y="150" width="345" height="100" rx="6" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1" />
    <text x="35" y="175" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#7C3AED">【顛覆性破局做法】</text>
    <text x="35" y="200" font-family="-apple-system, sans-serif" font-size="12" fill="#1E293B">失眠 ➔ 坦然接納睡不著 ➔ 起床去客廳看書 ➔ 焦慮消除</text>
    <text x="35" y="225" font-family="-apple-system, sans-serif" font-size="12" fill="#1E293B">「不以解決問題為目的，反倒讓問題自然消散！」</text>
    
    <text x="25" y="280" font-family="-apple-system, sans-serif" font-size="12" fill="#7C3AED" font-weight="bold">結果：遊戲規則改變，生命進入全新自由維度。</text>
  </g>
  
  <text x="450" y="440" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 5 ｜ 對立論法：第一序列微調 vs 第二序列規則顛覆</text>
</svg>"""
write_svg("exhibit-05-order-change.svg", svg_05)

# Exhibit 6: BCG 2x2 心智模式矩陣
svg_06 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="450" y="35" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#004F32" text-anchor="middle">BCG 2×2 心智模式矩陣：Carol Dweck 成長型思維 vs 防禦型思維</text>
  
  <!-- Y Axis -->
  <line x1="450" y1="65" x2="450" y2="405" stroke="#CBD5E1" stroke-width="2" stroke-dasharray="4,4" />
  <!-- X Axis -->
  <line x1="90" y1="235" x2="810" y2="235" stroke="#CBD5E1" stroke-width="2" stroke-dasharray="4,4" />
  
  <!-- Axis Labels -->
  <text x="450" y="60" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32" text-anchor="middle">▲ 挫折解讀：探索與回饋 (Curiosity)</text>
  <text x="450" y="425" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#64748B" text-anchor="middle">▼ 挫折解讀：威脅與攻擊 (Threat)</text>
  <text x="100" y="230" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#64748B" text-anchor="start">◄ 表現目標：證明自己 (Performance)</text>
  <text x="800" y="230" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32" text-anchor="end">學習目標：發展能力 (Learning) ►</text>
  
  <!-- Quadrant 1: Top Right (GROWTH HERO) -->
  <rect x="470" y="80" width="330" height="140" rx="8" fill="#F0FDF4" stroke="#29BA74" stroke-width="2" />
  <text x="490" y="110" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#004F32">【右上・成長探索型】★ 策略核心</text>
  <text x="490" y="135" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 視挫折為客觀數據，不評判個人本質價值</text>
  <text x="490" y="157" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 主動犯「可承受的小錯」，在反饋中複利進化</text>
  <text x="490" y="180" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#15803D">• 口頭禪：「我還沒學會，這正好讓我知道哪裡能補強」</text>

  <!-- Quadrant 2: Top Left (IMPOSTOR) -->
  <rect x="100" y="80" width="330" height="140" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
  <text x="120" y="110" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#475569">【左上・冒牌者焦慮型】</text>
  <text x="120" y="135" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 雖保持好學，但內心極度害怕被識破無能</text>
  <text x="120" y="157" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 成功歸因於運氣，失敗歸因於自身缺陷</text>
  <text x="120" y="180" font-family="-apple-system, sans-serif" font-size="12" fill="#DC2626">• 口頭禪：「大家千萬別發現我其實沒那麼厲害」</text>

  <!-- Quadrant 3: Bottom Left (FIXED DEFENSE) -->
  <rect x="100" y="250" width="330" height="140" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5" />
  <text x="120" y="280" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#B91C1C">【左下・僵固防禦型】(對立面)</text>
  <text x="120" y="305" font-family="-apple-system, sans-serif" font-size="12" fill="#7F1D1D">• 活在他人眼光中，脆弱高自尊，一觸即潰</text>
  <text x="120" y="327" font-family="-apple-system, sans-serif" font-size="12" fill="#7F1D1D">• 迴避一切可能暴露不足的新挑戰，嫉妒他人</text>
  <text x="120" y="350" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#DC2626">• 口頭禪：「反正我沒天賦，認真做只會丟臉」</text>

  <!-- Quadrant 4: Bottom Right (CONSERVATIVE) -->
  <rect x="470" y="250" width="330" height="140" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
  <text x="490" y="280" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#475569">【右下・謹慎保守型】</text>
  <text x="490" y="305" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 渴望技能精進，但對威脅防備過度</text>
  <text x="490" y="327" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 只在有100%把握的安全小圈子裡微調練習</text>
  <text x="490" y="350" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B">• 口頭禪：「慢慢來就好，千萬別冒險踏出界限」</text>
  
  <text x="450" y="448" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 6 ｜ BCG 2×2 矩陣：由僵固防禦躍遷至終身成長探索心態</text>
</svg>"""
write_svg("exhibit-06-bcg-mindset.svg", svg_06)

# Exhibit 7: 破除「應該思維」與 Ellis ABC 理情反駁
svg_07 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="450" y="35" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#051C2C" text-anchor="middle">認知解毒：Karen Horney 應該的暴政 × Albert Ellis ABC 反駁法</text>
  
  <!-- Left Side: Should Thinking Diagnosis -->
  <g transform="translate(40, 60)">
    <rect width="380" height="350" rx="10" fill="#FFFFFF" stroke="#DC2626" stroke-width="2" />
    <rect width="380" height="40" rx="10" fill="#DC2626" />
    <text x="190" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">應該思維 (暴政盲區)：混淆願望與事實</text>
    
    <rect x="20" y="55" width="340" height="85" rx="6" fill="#FEF2F2" />
    <text x="35" y="80" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#B91C1C">對世界的應該思維：</text>
    <text x="35" y="102" font-family="-apple-system, sans-serif" font-size="11" fill="#1E293B">「計畫應該完全無瑕、別人應該理解我」</text>
    <text x="35" y="122" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626">➔ 結果：現實一旦不如意，瞬間憤怒崩潰、怨懟世界</text>

    <rect x="20" y="150" width="340" height="85" rx="6" fill="#FEF2F2" />
    <text x="35" y="175" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#B91C1C">對自己的應該思維：</text>
    <text x="35" y="197" font-family="-apple-system, sans-serif" font-size="11" fill="#1E293B">「我必須隨時完美、我絕不能感到焦慮恐懼」</text>
    <text x="35" y="217" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626">➔ 結果：理想自我壓抑真實自我，引發深層情緒羞恥</text>
    
    <rect x="20" y="245" width="340" height="85" rx="6" fill="#F1F5F9" />
    <text x="35" y="270" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#475569">悲觀絕對化 (Seligman 3P 陷阱)：</text>
    <text x="35" y="292" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 永久化 (永遠好不起來) ｜ 普遍化 (整個人生完了)</text>
    <text x="35" y="312" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 人格化 (全都是因為我天生無能)</text>
  </g>

  <!-- Right Side: Ellis REBT ABC+D Model -->
  <g transform="translate(480, 60)">
    <rect width="380" height="350" rx="10" fill="#FFFFFF" stroke="#004F32" stroke-width="2" />
    <rect width="380" height="40" rx="10" fill="#004F32" />
    <text x="190" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">理性情緒反駁 (REBT)：ABC+D 破局心法</text>
    
    <!-- A Step -->
    <rect x="20" y="55" width="340" height="55" rx="6" fill="#F8FAFC" stroke="#E2E8F0" />
    <text x="35" y="77" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#051C2C">A (Activating Event) 客觀誘發事件</text>
    <text x="35" y="97" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">專案被主管退件修正（客觀事實，無情緒色彩）</text>

    <!-- B Step -->
    <rect x="20" y="118" width="340" height="55" rx="6" fill="#FEF3C7" stroke="#FDE68A" />
    <text x="35" y="140" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#B45309">B (Belief) 關鍵信念透鏡 ★ 決定因子</text>
    <text x="35" y="160" font-family="-apple-system, sans-serif" font-size="11" fill="#92400E">「這代表他看不起我，我永遠做不好」（非理性信念）</text>

    <!-- C Step -->
    <rect x="20" y="181" width="340" height="55" rx="6" fill="#FEE2E2" stroke="#FECACA" />
    <text x="35" y="203" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#DC2626">C (Consequence) 情緒與行為後果</text>
    <text x="35" y="223" font-family="-apple-system, sans-serif" font-size="11" fill="#B91C1C">極度沮喪、憤怒、冷戰消極怠工</text>

    <!-- D Step -->
    <rect x="20" y="244" width="340" height="85" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5" />
    <text x="35" y="268" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#15803D">D (Disputation) 顧問反駁介入 ★ 解脫之道</text>
    <text x="35" y="290" font-family="-apple-system, sans-serif" font-size="11" fill="#166534">「有什麼客觀證據證明他看不起我？退件只是內容格式需調整，並不代表人身否定！」</text>
    <text x="35" y="312" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#15803D">➔ 轉化為 E (Effective Belief)：接納現實，專注修正</text>
  </g>
  
  <text x="450" y="440" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 7 ｜ 認知重構：拆解應該思維，以 ABC+D 信念質疑奪回心理自主權</text>
</svg>"""
write_svg("exhibit-07-should-thinking-abc.svg", svg_07)

# Exhibit 8: WOOP + 斯多葛控制兩分法 (版型 7: 比較論法)
svg_08 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="450" y="35" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#004F32" text-anchor="middle">版型 7 比較論法：WOOP 心理對比 (左) ∩ 斯多葛控制兩分法 (右) 之落地交集</text>
  
  <!-- Left Box: WOOP -->
  <g transform="translate(30, 60)">
    <rect width="265" height="350" rx="10" fill="#FFFFFF" stroke="#004F32" stroke-width="2" />
    <rect width="265" height="40" rx="10" fill="#004F32" />
    <text x="132" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">WOOP 心理對比引擎</text>
    
    <text x="18" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32">W (Wish 願望)：</text>
    <text x="18" y="90" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">設定具體且切合內心渴望的目標</text>

    <text x="18" y="125" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32">O (Outcome 最佳結果)：</text>
    <text x="18" y="145" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">沉浸想像目標實現後的喜悅畫面</text>

    <text x="18" y="180" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#D97706">O (Obstacle 內在障礙) ★：</text>
    <text x="18" y="200" font-family="-apple-system, sans-serif" font-size="11" fill="#B45309">直面拖延、恐懼、分心等真實障礙</text>

    <text x="18" y="240" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32">P (Plan 執行意圖)：</text>
    <text x="18" y="260" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">制定 If-Then：「如果障礙X出現，我就立即執行動作Y！」</text>
    
    <text x="18" y="320" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">特色：以心理對比創造行動張力</text>
  </g>

  <!-- Center: Common Intersection -->
  <g transform="translate(315, 60)">
    <rect width="270" height="350" rx="10" fill="#FEF3C7" stroke="#D97706" stroke-width="2.5" />
    <rect width="270" height="40" rx="10" fill="#D97706" />
    <text x="135" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">③ 核心交集：高效落地閉環</text>
    
    <rect x="15" y="60" width="240" height="90" rx="6" fill="#FFFFFF" />
    <text x="25" y="85" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#B45309">【拒絕空想樂觀】</text>
    <text x="25" y="110" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">兩者皆不主張盲目樂觀，而是徹底直視現實障礙與局限。</text>

    <rect x="15" y="165" width="240" height="110" rx="6" fill="#FFFFFF" />
    <text x="25" y="190" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#B45309">【黃金操作公式】</text>
    <text x="25" y="215" font-family="-apple-system, sans-serif" font-size="11" fill="#1E293B">將控制兩分法篩選出的「100%完全可控微行動」，填入 WOOP 的 Plan (If-Then) 中！</text>

    <text x="135" y="315" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#B45309" text-anchor="middle">徹底切斷內耗，直奔行動！</text>
  </g>

  <!-- Right Box: Stoic Control -->
  <g transform="translate(605, 60)">
    <rect width="265" height="350" rx="10" fill="#FFFFFF" stroke="#051C2C" stroke-width="2" />
    <rect width="265" height="40" rx="10" fill="#051C2C" />
    <text x="132" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">斯多葛控制兩分法</text>
    
    <text x="18" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#DC2626">【完全不可控圈・果斷放手】</text>
    <text x="18" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 他人的想法、評價、情緒反彈</text>
    <text x="18" y="112" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 外在經濟大環境與突發意外</text>
    <text x="18" y="132" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 過去已發生的事實</text>

    <text x="18" y="175" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32">【完全可控圈・100%投入】</text>
    <text x="18" y="197" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 我此時此刻採取的行動與努力</text>
    <text x="18" y="217" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 我對外界刺激做出的理性詮釋</text>
    <text x="18" y="237" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 我為自己劃定的邊界與承諾</text>

    <text x="18" y="320" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">特色：以邊界收斂獲得內在寧靜</text>
  </g>
  
  <text x="450" y="440" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 8 ｜ 比較論法：WOOP 心理對比引擎與斯多葛控制兩分法之落地交集</text>
</svg>"""
write_svg("exhibit-08-woop-stoic.svg", svg_08)

# Exhibit 9: 關係系統視角與互補循環 (版型 5: 麥肯錫矩陣)
svg_09 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="450" y="35" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#051C2C" text-anchor="middle">模組三 關係的改變：系統動力學視角 vs 個體孤島視角</text>
  
  <!-- Circular Feedback Diagram in Center-Top -->
  <g transform="translate(180, 55)">
    <rect width="540" height="110" rx="8" fill="#F1F5F9" stroke="#CBD5E1" />
    <text x="270" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#051C2C" text-anchor="middle">【系統閉環反饋：追與逃的雙人舞】</text>
    
    <rect x="25" y="40" width="160" height="50" rx="6" fill="#FEE2E2" />
    <text x="105" y="62" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#B91C1C" text-anchor="middle">A 感到焦慮 ➔ 逼近質問</text>
    <text x="105" y="78" font-family="-apple-system, sans-serif" font-size="9" fill="#DC2626" text-anchor="middle">（渴望確認關係安全）</text>

    <path d="M195 65 L245 65" stroke="#051C2C" stroke-width="2" marker-end="url(#arrow)" />
    
    <rect x="255" y="40" width="160" height="50" rx="6" fill="#EFF6FF" />
    <text x="335" y="62" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#1D4ED8" text-anchor="middle">B 感到窒息 ➔ 沉默逃避</text>
    <text x="335" y="78" font-family="-apple-system, sans-serif" font-size="9" fill="#2563EB" text-anchor="middle">（渴望保護個人空間）</text>
    
    <!-- Curved back arrow -->
    <path d="M425 65 Q480 65 480 95 Q480 120 270 120 Q60 120 60 95" fill="none" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="4,4" />
    <text x="270" y="105" font-family="-apple-system, sans-serif" font-size="10" fill="#DC2626" text-anchor="middle">▲ B越逃 ➔ A越恐慌 ➔ 追得更兇（閉環升級）</text>
  </g>

  <!-- 3 Comparison Cards Below -->
  <g transform="translate(40, 185)">
    <!-- Card 1: 語言層次 -->
    <rect width="250" height="225" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5" />
    <rect width="250" height="32" rx="8" fill="#0284C7" />
    <text x="125" y="22" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. 語言的兩個層次</text>
    <text x="15" y="55" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#0369A1">【內容層 vs 關係層】</text>
    <text x="15" y="80" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 內容層：表面字句事實</text>
    <text x="15" y="105" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 關係層：話外音中的權力界定、身分認可與依賴程度</text>
    <rect x="15" y="130" width="220" height="75" rx="6" fill="#F0F9FF" />
    <text x="25" y="152" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#0369A1">高階洞察：</text>
    <text x="25" y="172" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">所有無休止的講道理爭辯，爭的都不是道理本身，而是關係中的話語權！</text>
  </g>

  <g transform="translate(325, 185)">
    <!-- Card 2: 角色期待 -->
    <rect width="250" height="225" rx="8" fill="#FFFFFF" stroke="#004F32" stroke-width="1.5" />
    <rect width="250" height="32" rx="8" fill="#004F32" />
    <text x="125" y="22" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. 角色的系統互補</text>
    <text x="15" y="55" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32">【強者與弱者相互滋養】</text>
    <text x="15" y="80" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 強制管束者的存在，依賴於被管束者的妥協順從</text>
    <text x="15" y="110" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 過度承擔的拯救者，往往親手製造了無能的依賴者</text>
    <rect x="15" y="130" width="220" height="75" rx="6" fill="#F0FDF4" />
    <text x="25" y="152" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#004F32">高階洞察：</text>
    <text x="25" y="172" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">想改變對方的軟弱，先停下自己的過度包辦；改變系統從自身舞步開始！</text>
  </g>

  <g transform="translate(610, 185)">
    <!-- Card 3: 新契約重構 -->
    <rect width="250" height="225" rx="8" fill="#FFFFFF" stroke="#6B21A8" stroke-width="1.5" />
    <rect width="250" height="32" rx="8" fill="#6B21A8" />
    <text x="125" y="22" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. 重寫新關係契約</text>
    <text x="15" y="55" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#6B21A8">【透明對等的演化】</text>
    <text x="15" y="80" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 主動表達個人邊界與底線</text>
    <text x="15" y="105" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 將潛意識隱形契約轉化為公開協商的正向約定</text>
    <rect x="15" y="130" width="220" height="75" rx="6" fill="#F5F3FF" />
    <text x="25" y="152" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#6B21A8">高階洞察：</text>
    <text x="25" y="172" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">不寄望對方主動開竅，而是以成人的成熟姿態，共同定義健康合作關係。</text>
  </g>
  
  <text x="450" y="440" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 9 ｜ 關係系統矩陣：看懂人際循環因果，以改變自身應對重構新契約</text>
</svg>"""
write_svg("exhibit-09-relational-system.svg", svg_09)

# Exhibit 10: 破解三角化與阿德勒課題分離
svg_10 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="450" y="35" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#111827" text-anchor="middle">關係解套：Murray Bowen 去三角化 (Triangulation) × 阿德勒課題分離</text>
  
  <!-- Left Side: Triangulation Diagram -->
  <g transform="translate(50, 65)">
    <rect width="360" height="345" rx="10" fill="#FFFFFF" stroke="#DC2626" stroke-width="2" />
    <rect width="360" height="38" rx="10" fill="#DC2626" />
    <text x="180" y="25" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">【家庭與組織的三角化陷阱】</text>
    
    <!-- Triangle Visual -->
    <circle cx="180" cy="95" r="24" fill="#FEF2F2" stroke="#DC2626" stroke-width="2" />
    <text x="180" y="100" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#DC2626" text-anchor="middle">第三方 C</text>
    <text x="180" y="132" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">(孩子 / 夾心中階主管)</text>

    <circle cx="85" cy="210" r="24" fill="#F1F5F9" stroke="#64748B" stroke-width="2" />
    <text x="85" y="215" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">主體 A</text>

    <circle cx="275" cy="210" r="24" fill="#F1F5F9" stroke="#64748B" stroke-width="2" />
    <text x="275" y="215" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">主體 B</text>

    <!-- Tension Line between A and B -->
    <path d="M115 210 L245 210" stroke="#DC2626" stroke-width="3" stroke-dasharray="5,5" />
    <text x="180" y="200" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#DC2626" text-anchor="middle">核心衝突焦慮 (難以直面)</text>

    <!-- Triangulation Pull Lines -->
    <path d="M100 190 L160 115" stroke="#F59E0B" stroke-width="2" />
    <text x="110" y="150" font-family="-apple-system, sans-serif" font-size="9" fill="#B45309">拉攏結盟</text>
    
    <path d="M260 190 L200 115" stroke="#F59E0B" stroke-width="2" />
    <text x="245" y="150" font-family="-apple-system, sans-serif" font-size="9" fill="#B45309">分擔砲火</text>

    <rect x="20" y="250" width="320" height="80" rx="6" fill="#FEF2F2" />
    <text x="30" y="272" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#B91C1C">三角化毒害：</text>
    <text x="30" y="292" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">• A與B的真實矛盾被掩蓋，轉化為慢性系統毒瘤</text>
    <text x="30" y="312" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">• 第三方 C 承擔無辜罪責，喪失個人主體性</text>
  </g>

  <!-- Right Side: Separation of Tasks -->
  <g transform="translate(480, 65)">
    <rect width="370" height="345" rx="10" fill="#FFFFFF" stroke="#004F32" stroke-width="2" />
    <rect width="370" height="38" rx="10" fill="#004F32" />
    <text x="185" y="25" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">【阿德勒課題分離：解套與邊界確立】</text>
    
    <rect x="25" y="55" width="320" height="80" rx="6" fill="#F0FDF4" stroke="#86EFAC" />
    <text x="35" y="78" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#15803D">黃金判定準則：</text>
    <text x="35" y="100" font-family="-apple-system, sans-serif" font-size="11" fill="#166534">「某種選擇所帶來的直接後果，最終由誰來承擔？」</text>
    <text x="35" y="120" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#004F32">➔ 由誰承擔，那就是誰的課題！</text>

    <!-- Two Pillars -->
    <rect x="25" y="150" width="150" height="110" rx="6" fill="#F8FAFC" stroke="#CBD5E1" />
    <text x="100" y="172" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#051C2C" text-anchor="middle">自己課題 (專注主控)</text>
    <text x="35" y="195" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">• 我的選擇與態度</text>
    <text x="35" y="215" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">• 我的工作成果與付出</text>
    <text x="35" y="235" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">• 絕不推卸屬於我的責任</text>

    <rect x="195" y="150" width="150" height="110" rx="6" fill="#F8FAFC" stroke="#CBD5E1" />
    <text x="270" y="172" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#DC2626" text-anchor="middle">他人課題 (尊重不干涉)</text>
    <text x="205" y="195" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">• 別人滿不滿意我</text>
    <text x="205" y="215" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">• 父母的情緒是否平靜</text>
    <text x="205" y="235" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">• 絕不僭越干涉他人課題</text>

    <rect x="25" y="275" width="320" height="55" rx="6" fill="#FEF3C7" />
    <text x="35" y="297" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#B45309">去三角化實踐：「退出夾心，歸還責任」</text>
    <text x="35" y="315" font-family="-apple-system, sans-serif" font-size="10" fill="#78350F">「這是你們兩人的課題，我相信你們有智慧直接對話解決。」</text>
  </g>
  
  <text x="450" y="440" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 10 ｜ 關係解套：識破三角化夾心陷阱，落實阿德勒課題分離劃清邊界</text>
</svg>"""
write_svg("exhibit-10-triangulation-adler.svg", svg_10)

# Exhibit 11: 非暴力溝通四步法 (NVC Flow)
svg_11 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="450" y="35" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#004F32" text-anchor="middle">馬歇爾·盧森堡非暴力溝通 (NVC)：四步重建高品質人際連結</text>
  
  <!-- 4 Step Flow Horizontal -->
  <g transform="translate(30, 65)">
    <!-- Step 1 -->
    <rect x="0" y="0" width="195" height="340" rx="8" fill="#FFFFFF" stroke="#004F32" stroke-width="2" />
    <rect x="0" y="0" width="195" height="40" rx="8" fill="#004F32" />
    <text x="97" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. 觀察 (Observation)</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32">【客觀事實】</text>
    <text x="15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 攝影機拍得到的具體畫面</text>
    <text x="15" y="120" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 不帶任何道德評判或誇飾</text>
    
    <rect x="15" y="145" width="165" height="80" rx="6" fill="#FEE2E2" />
    <text x="25" y="165" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#B91C1C">錯誤批判：</text>
    <text x="25" y="185" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">「你總是在偷懶敷衍！」</text>
    
    <rect x="15" y="235" width="165" height="85" rx="6" fill="#F0FDF4" />
    <text x="25" y="255" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#15803D">正向觀察：</text>
    <text x="25" y="275" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">「這週兩次交報告時間，比預定截止晚了兩小時」</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(245, 65)">
    <rect x="0" y="0" width="195" height="340" rx="8" fill="#FFFFFF" stroke="#004F32" stroke-width="2" />
    <rect x="0" y="0" width="195" height="40" rx="8" fill="#004F32" />
    <text x="97" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. 感受 (Feeling)</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32">【真實脆弱】</text>
    <text x="15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 表達內在當下真實情緒</text>
    <text x="15" y="120" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 區分感受 vs 偽裝指責</text>
    
    <rect x="15" y="145" width="165" height="80" rx="6" fill="#FEE2E2" />
    <text x="25" y="165" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#B91C1C">偽裝感受：</text>
    <text x="25" y="185" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">「我覺得你毫無責任心！」</text>
    
    <rect x="15" y="235" width="165" height="85" rx="6" fill="#F0FDF4" />
    <text x="25" y="255" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#15803D">真誠感受：</text>
    <text x="25" y="275" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">「當進度延誤時，我感到十分焦慮和沮喪」</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(460, 65)">
    <rect x="0" y="0" width="195" height="340" rx="8" fill="#FFFFFF" stroke="#004F32" stroke-width="2" />
    <rect x="0" y="0" width="195" height="40" rx="8" fill="#004F32" />
    <text x="97" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. 需要 (Need)</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32">【底層渴望】</text>
    <text x="15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 負面情緒源於未被滿足的需要</text>
    <text x="15" y="120" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 看見彼此共有的生命需求</text>
    
    <rect x="15" y="145" width="165" height="80" rx="6" fill="#FEE2E2" />
    <text x="25" y="165" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#B91C1C">忽視需要：</text>
    <text x="25" y="185" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">「你為什麼總是跟我作對！」</text>
    
    <rect x="15" y="235" width="165" height="85" rx="6" fill="#F0FDF4" />
    <text x="25" y="255" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#15803D">表達需要：</text>
    <text x="25" y="275" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">「因為我非常需要團隊能保持資訊同步與穩定節奏」</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(675, 65)">
    <rect x="0" y="0" width="195" height="340" rx="8" fill="#FFFFFF" stroke="#29BA74" stroke-width="2.5" />
    <rect x="0" y="0" width="195" height="40" rx="8" fill="#29BA74" />
    <text x="97" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4. 請求 (Request) ★</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32">【具體行動】</text>
    <text x="15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 提出明確、正向、可執行的請求</text>
    <text x="15" y="120" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 區分「請求」與「懲罰命令」</text>
    
    <rect x="15" y="145" width="165" height="80" rx="6" fill="#FEE2E2" />
    <text x="25" y="165" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#B91C1C">模糊命令：</text>
    <text x="25" y="185" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">「請你以後態度認真點！」</text>
    
    <rect x="15" y="235" width="165" height="85" rx="6" fill="#F0FDF4" />
    <text x="25" y="255" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#15803D">清晰請求：</text>
    <text x="25" y="275" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">「下次若預計無法準時，能否提前半小時發訊息告知？」</text>
  </g>
  
  <text x="450" y="440" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 11 ｜ 非暴力溝通四步推進法：觀察事實 ➔ 真誠感受 ➔ 洞察需要 ➔ 明確請求</text>
</svg>"""
write_svg("exhibit-11-nvc-four-steps.svg", svg_11)

# Exhibit 12: 布里奇斯轉折三階段 (Bridges Transition Model)
svg_12 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="450" y="35" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#051C2C" text-anchor="middle">William Bridges 人生轉折三部曲：外在變故是一瞬，內在轉折是漫長的心理過渡</text>
  
  <!-- U-Curve Path Visual -->
  <path d="M100 120 C 250 120, 320 260, 450 260 C 580 260, 650 120, 800 120" fill="none" stroke="#CBD5E1" stroke-width="4" stroke-dasharray="6,6" />
  <path d="M100 120 C 200 120, 250 200, 300 240" fill="none" stroke="#DC2626" stroke-width="5" />
  <path d="M300 240 C 370 280, 530 280, 600 240" fill="none" stroke="#D97706" stroke-width="5" />
  <path d="M600 240 C 650 200, 700 120, 800 120" fill="none" stroke="#16A34A" stroke-width="5" />
  
  <!-- Phase 1: Endings -->
  <g transform="translate(60, 160)">
    <rect width="230" height="230" rx="8" fill="#FFFFFF" stroke="#DC2626" stroke-width="2" />
    <rect width="230" height="32" rx="8" fill="#DC2626" />
    <text x="115" y="22" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第一階段：結束 (Endings)</text>
    <text x="15" y="55" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#B91C1C">【告別與脫離舊自我】</text>
    <text x="15" y="78" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 心理任務：承認喪失、允許哀傷</text>
    <text x="15" y="98" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 舉辦心理告別儀式，放下舊身分安全感</text>
    <rect x="15" y="125" width="200" height="85" rx="6" fill="#FEF2F2" />
    <text x="25" y="147" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#B91C1C">顧問金句：</text>
    <text x="25" y="167" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">「沒有徹底而坦誠的結束，就不可能迎來真正的開始。」</text>
  </g>

  <!-- Phase 2: Neutral Zone -->
  <g transform="translate(335, 180)">
    <rect width="230" height="230" rx="8" fill="#FFFFFF" stroke="#D97706" stroke-width="2" />
    <rect width="230" height="32" rx="8" fill="#D97706" />
    <text x="115" y="22" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第二階段：迷茫中性區 (Neutral)</text>
    <text x="15" y="55" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#B45309">【混沌中的創新孵化期】</text>
    <text x="15" y="78" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 狀態：舊模式已死，新模式未生</text>
    <text x="15" y="98" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 致命誘惑：因恐懼草率抓住錯的稻草</text>
    <rect x="15" y="125" width="200" height="85" rx="6" fill="#FEF3C7" />
    <text x="25" y="147" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#B45309">顧問金句：</text>
    <text x="25" y="167" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">「迷茫不是浪費時間，而是種子在冰雪泥土中積蓄重生的養分。」</text>
  </g>

  <!-- Phase 3: New Beginnings -->
  <g transform="translate(610, 160)">
    <rect width="230" height="230" rx="8" fill="#FFFFFF" stroke="#16A34A" stroke-width="2" />
    <rect width="230" height="32" rx="8" fill="#16A34A" />
    <text x="115" y="22" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第三階段：重生 (Beginnings)</text>
    <text x="15" y="55" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#15803D">【內在指南針校準啟程】</text>
    <text x="15" y="78" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 心理任務：重構個人價值觀優先序</text>
    <text x="15" y="98" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 採取微步行動，培育全新成熟身分</text>
    <rect x="15" y="125" width="200" height="85" rx="6" fill="#F0FDF4" />
    <text x="25" y="147" font-family="-apple-system, sans-serif" font-size="10" font-weight="bold" fill="#15803D">顧問金句：</text>
    <text x="25" y="167" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">「以開放好奇的心態擁抱新世界，自我系統完成深層升級。」</text>
  </g>
  
  <text x="450" y="440" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 12 ｜ 轉折 U 型曲線：告別結束 ➔ 耐受迷茫中性區 ➔ 迎向新生的心理過渡歷程</text>
</svg>"""
write_svg("exhibit-12-bridges-transition.svg", svg_12)

# Exhibit 13: 轉折期決策 2x2 矩陣 (多元可能自我 Herminia Ibarra)
svg_13 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="450" y="35" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#004F32" text-anchor="middle">BCG 2×2 生涯轉型決策矩陣：Herminia Ibarra「多元可能自我 (Working Identity)」</text>
  
  <!-- Y Axis -->
  <line x1="450" y1="65" x2="450" y2="405" stroke="#CBD5E1" stroke-width="2" stroke-dasharray="4,4" />
  <!-- X Axis -->
  <line x1="90" y1="235" x2="810" y2="235" stroke="#CBD5E1" stroke-width="2" stroke-dasharray="4,4" />
  
  <!-- Axis Labels -->
  <text x="450" y="60" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32" text-anchor="middle">▲ 轉型策略：平行小步試驗 (Parallel Experiment)</text>
  <text x="450" y="425" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#64748B" text-anchor="middle">▼ 轉型策略：一刀切豪賭 / 固守不變 (All-or-Nothing)</text>
  <text x="100" y="230" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#64748B" text-anchor="start">◄ 決策依據：經濟模型 (外在回報・性價比)</text>
  <text x="800" y="230" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32" text-anchor="end">決策依據：心理模型 (內在契合・自我拓展) ►</text>
  
  <!-- Quadrants -->
  <!-- Top Right: Possible Selves (Hero) -->
  <rect x="470" y="80" width="330" height="140" rx="8" fill="#F0FDF4" stroke="#29BA74" stroke-width="2" />
  <text x="490" y="110" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#004F32">【右上・多元可能自我】★ 策略高亮</text>
  <text x="490" y="135" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 保留生存基線，在業餘啟動低風險專案</text>
  <text x="490" y="157" font-family="-apple-system, sans-serif" font-size="12" fill="#1F2937">• 「邊做邊想」以行動培育新身分，安全過渡</text>
  <text x="490" y="180" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#15803D">• 典範：從工程師兼職寫作，逐步演化為專欄作家</text>

  <!-- Top Left: Side Hustle for Money -->
  <rect x="100" y="80" width="330" height="140" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
  <text x="120" y="110" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#475569">【左上・純功利副業】</text>
  <text x="120" y="135" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 雖分散財務風險，但只看短期變現</text>
  <text x="120" y="157" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 缺乏內在熱情驅動，容易淪為雙重疲憊</text>
  <text x="120" y="180" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B">• 局限：無法觸發心靈深處的自我重塑</text>

  <!-- Bottom Left: Traditional Trap -->
  <rect x="100" y="250" width="330" height="140" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5" />
  <text x="120" y="280" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#B91C1C">【左下・傳統沉沒成本困局】(對立面)</text>
  <text x="120" y="305" font-family="-apple-system, sans-serif" font-size="12" fill="#7F1D1D">• 困在薪水金絲雀籠中，天天抱怨卻不敢動</text>
  <text x="120" y="327" font-family="-apple-system, sans-serif" font-size="12" fill="#7F1D1D">• 滿腦子性價比算計，最終在職業倦怠中枯萎</text>
  <text x="120" y="350" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#DC2626">• 痛點：用安穩作為麻痺靈魂的藉口</text>

  <!-- Bottom Right: Blind Resignation -->
  <rect x="470" y="250" width="330" height="140" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
  <text x="490" y="280" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#475569">【右下・衝動盲目裸辭】</text>
  <text x="490" y="305" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 滿懷理想一刀切離職，缺乏緩衝試錯空間</text>
  <text x="490" y="327" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">• 殘酷的現實財務壓力迅速扼殺剛萌芽的新身分</text>
  <text x="490" y="350" font-family="-apple-system, sans-serif" font-size="12" fill="#DC2626">• 教訓：誤將外在辭職當作內在轉型的完成</text>
  
  <text x="450" y="448" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 13 ｜ 轉型矩陣：以多元可能自我平行實驗，取代傳統困局與盲目冒險</text>
</svg>"""
write_svg("exhibit-13-possible-selves-matrix.svg", svg_13)

# Exhibit 14: 英雄之旅與救贖敘事 (Joseph Campbell)
svg_14 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="450" y="35" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#111827" text-anchor="middle">意義重構：Joseph Campbell 單子神話英雄之旅 × Dan McAdams 救贖敘事</text>
  
  <!-- 3 Pillar Journey Map -->
  <g transform="translate(40, 60)">
    <!-- Stage 1 -->
    <rect width="255" height="350" rx="8" fill="#FFFFFF" stroke="#0066CC" stroke-width="2" />
    <rect width="255" height="38" rx="8" fill="#0066CC" />
    <text x="127" y="24" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第一幕：啟程 (Departure)</text>
    <text x="15" y="65" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#0066CC">【跨越熟悉的日常界限】</text>
    <text x="15" y="90" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 聽見冒險的召喚：覺察現狀已枯竭</text>
    <text x="15" y="115" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 克服對未知的本能恐懼與拒絕召喚</text>
    <text x="15" y="140" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 遇見智者或內在信念導師指引</text>
    <text x="15" y="165" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 跨過第一道守門人門檻，踏上未知</text>
    <rect x="15" y="210" width="225" height="110" rx="6" fill="#F0F9FF" />
    <text x="25" y="235" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#0369A1">心理意涵：</text>
    <text x="25" y="258" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">不再安於受害者角色，主動承認舊的生活方式無法支撐未來的自我。</text>
  </g>

  <!-- Stage 2 -->
  <g transform="translate(320, 60)">
    <rect width="260" height="350" rx="8" fill="#FFFFFF" stroke="#DC2626" stroke-width="2" />
    <rect width="260" height="38" rx="8" fill="#DC2626" />
    <text x="130" y="24" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第二幕：深淵啟蒙 (Initiation)</text>
    <text x="15" y="65" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#B91C1C">【至暗時刻與心靈淬煉】</text>
    <text x="15" y="90" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 經歷一連串嚴酷考驗、背叛與創傷</text>
    <text x="15" y="115" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 進入內心最深處的黑暗洞穴 (Abyss)</text>
    <text x="15" y="140" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 舊自我與虛妄自尊的象徵性死亡</text>
    <text x="15" y="165" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 浴火重生，獲得心靈超凡智慧良藥</text>
    <rect x="15" y="210" width="230" height="110" rx="6" fill="#FEF2F2" />
    <text x="25" y="235" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#B91C1C">救贖敘事 (Redemption)：</text>
    <text x="25" y="258" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">拒絕「污染敘事（好境況被徹底毀掉）」；堅定認定「正是這段深淵，賦予我前所未有的慈悲與韌性」。</text>
  </g>

  <!-- Stage 3 -->
  <g transform="translate(605, 60)">
    <rect width="255" height="350" rx="8" fill="#FFFFFF" stroke="#004F32" stroke-width="2" />
    <rect width="255" height="38" rx="8" fill="#004F32" />
    <text x="127" y="24" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">第三幕：回歸饋贈 (Return)</text>
    <text x="15" y="65" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32">【帶著智慧良藥回饋社群】</text>
    <text x="15" y="90" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 跨越歸途門檻，重返日常生活</text>
    <text x="15" y="115" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 成為兩個世界的引領者與主宰者</text>
    <text x="15" y="140" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 將苦難轉化為陪伴與啟發他人的光</text>
    <text x="15" y="165" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 自我系統圓滿升級，迎向下一次冒險</text>
    <rect x="15" y="210" width="225" height="110" rx="6" fill="#F0FDF4" />
    <text x="25" y="235" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#15803D">終極整合：</text>
    <text x="25" y="258" font-family="-apple-system, sans-serif" font-size="10" fill="#1E293B">你不是命運的受害者，你是這部英雄傳記的主動撰寫者！</text>
  </g>
  
  <text x="450" y="440" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 14 ｜ 英雄之旅三幕九階圖：以救贖敘事重寫生命故事，賦予苦難超凡意義</text>
</svg>"""
write_svg("exhibit-14-heros-journey.svg", svg_14)

# Exhibit 15: 埃里克森人生地圖 (Erik Erikson 4 Adult Stages)
svg_15 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 460" width="100%" height="100%">
  <rect width="920" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="460" y="35" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#051C2C" text-anchor="middle">模組五 人生地圖：Erik Erikson 心理社會發展四大成年階段與危機轉化</text>
  
  <!-- 4 Stage Columns -->
  <!-- Col 1 -->
  <g transform="translate(30, 60)">
    <rect width="205" height="355" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="2" />
    <rect width="205" height="40" rx="8" fill="#0284C7" />
    <text x="102" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">階段一：青春期使命</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#0369A1">【核心心理衝突】</text>
    <text x="15" y="90" font-family="-apple-system, sans-serif" font-size="11" fill="#1E293B">同一性 vs. 角色混亂</text>
    <text x="15" y="108" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">(Identity vs. Confusion)</text>

    <text x="15" y="140" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#0369A1">【核心發展任務】</text>
    <text x="15" y="162" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 回答「我是誰？我要去哪？」</text>
    <text x="15" y="182" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 探索個人信念與價值觀</text>
    <text x="15" y="202" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 擺脫對父母認同的單純依附</text>

    <rect x="15" y="240" width="175" height="95" rx="6" fill="#F0F9FF" />
    <text x="25" y="265" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#0369A1">獲得心靈美德：</text>
    <text x="25" y="290" font-family="-apple-system, sans-serif" font-size="15" font-weight="bold" fill="#0284C7">【忠誠 Fidelity】</text>
    <text x="25" y="315" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">對真實自我方向的信守</text>
  </g>

  <!-- Col 2 -->
  <g transform="translate(248, 60)">
    <rect width="205" height="355" rx="8" fill="#FFFFFF" stroke="#004F32" stroke-width="2" />
    <rect width="205" height="40" rx="8" fill="#004F32" />
    <text x="102" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">階段二：成年早期</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#004F32">【核心心理衝突】</text>
    <text x="15" y="90" font-family="-apple-system, sans-serif" font-size="11" fill="#1E293B">親密感 vs. 孤獨感</text>
    <text x="15" y="108" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">(Intimacy vs. Isolation)</text>

    <text x="15" y="140" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#004F32">【核心發展任務】</text>
    <text x="15" y="162" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 學會愛的能力：打開心扉</text>
    <text x="15" y="182" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 敢於向伴侶暴露脆弱</text>
    <text x="15" y="202" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 建立職業認同與專業專長</text>

    <rect x="15" y="240" width="175" height="95" rx="6" fill="#F0FDF4" />
    <text x="25" y="265" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#004F32">獲得心靈美德：</text>
    <text x="25" y="290" font-family="-apple-system, sans-serif" font-size="15" font-weight="bold" fill="#004F32">【愛 Love】</text>
    <text x="25" y="315" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">在深刻親密中保有自我獨立</text>
  </g>

  <!-- Col 3 -->
  <g transform="translate(466, 60)">
    <rect width="205" height="355" rx="8" fill="#FFFFFF" stroke="#D97706" stroke-width="2" />
    <rect width="205" height="40" rx="8" fill="#D97706" />
    <text x="102" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">階段三：中年期使命</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#B45309">【核心心理衝突】</text>
    <text x="15" y="90" font-family="-apple-system, sans-serif" font-size="11" fill="#1E293B">繁殖/創生感 vs. 停滯感</text>
    <text x="15" y="108" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">(Generativity vs. Stagnation)</text>

    <text x="15" y="140" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#B45309">【核心發展任務】</text>
    <text x="15" y="162" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 教養與陪伴下一代成長</text>
    <text x="15" y="182" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 傳承自身人生經驗與智慧</text>
    <text x="15" y="202" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 扮演青年世代的導師與燈塔</text>

    <rect x="15" y="240" width="175" height="95" rx="6" fill="#FEF3C7" />
    <text x="25" y="265" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#B45309">獲得心靈美德：</text>
    <text x="25" y="290" font-family="-apple-system, sans-serif" font-size="15" font-weight="bold" fill="#D97706">【關懷 Care】</text>
    <text x="25" y="315" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">超越私利，滋養他人生命</text>
  </g>

  <!-- Col 4 -->
  <g transform="translate(684, 60)">
    <rect width="205" height="355" rx="8" fill="#FFFFFF" stroke="#6B21A8" stroke-width="2" />
    <rect width="205" height="40" rx="8" fill="#6B21A8" />
    <text x="102" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">階段四：晚年期使命</text>
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#6B21A8">【核心心理衝突】</text>
    <text x="15" y="90" font-family="-apple-system, sans-serif" font-size="11" fill="#1E293B">自我整合 vs. 絕望感</text>
    <text x="15" y="108" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">(Ego Integrity vs. Despair)</text>

    <text x="15" y="140" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#6B21A8">【核心發展任務】</text>
    <text x="15" y="162" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 回首一生得失，接納圓缺</text>
    <text x="15" y="182" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 承認局限，與過往遺憾和解</text>
    <text x="15" y="202" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• 超脫死亡恐懼，安享精神圓滿</text>

    <rect x="15" y="240" width="175" height="95" rx="6" fill="#F5F3FF" />
    <text x="25" y="265" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#6B21A8">獲得心靈美德：</text>
    <text x="25" y="290" font-family="-apple-system, sans-serif" font-size="15" font-weight="bold" fill="#6B21A8">【智慧 Wisdom】</text>
    <text x="25" y="315" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">以超然平靜接納生命終局</text>
  </g>
  
  <text x="460" y="442" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 15 ｜ 埃里克森人生地圖：四大成年階段之心理衝突、發展任務與美德收穫</text>
</svg>"""
write_svg("exhibit-15-erikson-lifemap.svg", svg_15)

# Exhibit 16: 並列論法三大支柱 (總結行動藍圖)
svg_16 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  
  <text x="450" y="35" font-family="-apple-system, sans-serif" font-size="16" font-weight="bold" fill="#051C2C" text-anchor="middle">版型 2 並列論法：自我發展落地三角——行為微步化、思維彈性化、關係邊界化</text>
  
  <!-- 3 Parallel Columns -->
  <!-- Col 1 -->
  <g transform="translate(40, 60)">
    <rect width="250" height="350" rx="8" fill="#FFFFFF" stroke="#004F32" stroke-width="2" />
    <rect width="250" height="40" rx="8" fill="#004F32" />
    <text x="125" y="25" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">支柱一：行為微步化</text>
    
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#004F32">【行動系統落地】</text>
    <text x="15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 最小阻力第一步：阻力小到大象完全感受不到威脅</text>
    <text x="15" y="130" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 環境場刺激：單一空間綁定特定微習慣，觸發自發行為</text>
    <text x="15" y="165" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 心理免疫透視：停滯時填寫四欄表，看清隱含好處</text>
    <text x="15" y="200" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 第二序列改變：努力無效時跳出框架，重寫遊戲規則</text>

    <rect x="15" y="240" width="220" height="90" rx="6" fill="#F0FDF4" />
    <text x="25" y="265" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#004F32">每日行動檢核：</text>
    <text x="25" y="288" font-family="-apple-system, sans-serif" font-size="10" fill="#15803D">「今天我是否為大象創造了一個微小而愉悅的新經驗？」</text>
  </g>

  <!-- Col 2 -->
  <g transform="translate(325, 60)">
    <rect width="250" height="350" rx="8" fill="#FFFFFF" stroke="#051C2C" stroke-width="2.5" />
    <rect width="250" height="40" rx="8" fill="#051C2C" />
    <text x="125" y="25" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">支柱二：思維彈性化 ★</text>
    
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#051C2C">【心智系統重構】</text>
    <text x="15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• WOOP 閉環：願望 ➔ 結果 ➔ 內在障礙 ➔ If-Then 方案</text>
    <text x="15" y="130" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 控制兩分法：焦慮時區分可控與不可控，100%精力收斂</text>
    <text x="15" y="165" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 瓦解應該思維：以客觀現實取代暴政，進行 ABC 反駁</text>
    <text x="15" y="200" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 成長型心態：把犯錯當作學習數據，專注能力進化</text>

    <rect x="15" y="240" width="220" height="90" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1" />
    <text x="25" y="265" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#051C2C">每日思維檢核：</text>
    <text x="25" y="288" font-family="-apple-system, sans-serif" font-size="10" fill="#1E3A8A">「我正在為證明自己而焦慮，還是為發展自己而探索？」</text>
  </g>

  <!-- Col 3 -->
  <g transform="translate(610, 60)">
    <rect width="250" height="350" rx="8" fill="#FFFFFF" stroke="#6B21A8" stroke-width="2" />
    <rect width="250" height="40" rx="8" fill="#6B21A8" />
    <text x="125" y="25" font-family="-apple-system, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">支柱三：關係邊界化</text>
    
    <text x="15" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#6B21A8">【人際系統演化】</text>
    <text x="15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 阿德勒課題分離：誰承受直接後果就是誰的責任</text>
    <text x="15" y="130" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 去三角化：退出任何第三方的結盟與情緒夾心</text>
    <text x="15" y="165" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 非暴力溝通四步：觀察事實 ➔ 感受 ➔ 需要 ➔ 清晰請求</text>
    <text x="15" y="200" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 英雄之旅敘事：重寫生命故事，將創傷轉化為救贖恩賜</text>

    <rect x="15" y="240" width="220" height="90" rx="6" fill="#F5F3FF" />
    <text x="25" y="265" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#6B21A8">每日關係檢核：</text>
    <text x="25" y="288" font-family="-apple-system, sans-serif" font-size="10" fill="#7C3AED">「我是否管好了自己的課題，並為對方留出了獨立空間？」</text>
  </g>
  
  <text x="450" y="440" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">EXHIBIT 16 ｜ 落地行動藍圖：行為微步化、思維彈性化、關係邊界化三大支柱</text>
</svg>"""
write_svg("exhibit-16-action-pillars.svg", svg_16)

print("[ALL DONE] 16 vector SVG exhibits generated successfully!")
