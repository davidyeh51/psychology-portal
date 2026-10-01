# 🧠 心理學知識庫暨顧問簡報門戶 (Psychology Knowledge Hub & Executive Briefing Portal)

> **系統歸屬**：大衛雲 2.0 ｜ A2. 專業管理 ▸ A2.2 個人成長 ▸ A2.2.4 心理學  
> **視覺規範**：三大管顧巨頭無雜訊簡報系統（McKinsey 深海藍 `#051C2C` × BCG 森綠 `#004F32` × Accenture 科技紫 `#A100FF`）  
> **線上門戶網址**：[https://davidyeh51.github.io/psychology-portal/](https://davidyeh51.github.io/psychology-portal/)  
> **線上互動簡報**：[https://davidyeh51.github.io/psychology-portal/chen-haixian-self-development.html](https://davidyeh51.github.io/psychology-portal/chen-haixian-self-development.html)  
> **PowerPoint 下載**：[`downloads/chen-haixian-self-development-zero-noise.pptx`](./downloads/chen-haixian-self-development-zero-noise.pptx)

---

## 🎯 核心功能與架構特色

1. **支援未來模組化擴充之「心理學門戶首頁」 (`index.html`)**
   - 預設收錄六大心理學領域（自我發展與轉變心理學、認知行為與思維重構、職場心理與職業倦怠、阿德勒個體心理學、正向心理學與心理韌性、家庭系統動力學）。
   - 內建「全景體系架構圖 (SVG)」、「學員四大處境快速分流檢索」與「認知層級切換器 (入門痛點 vs 進階架構)」。

2. **毫秒級全站深層關鍵字檢索引擎 (`search-index.js` + `app.js`)**
   - 支援全站即時模糊搜尋、多關鍵字交集、螢光高亮標記 (`<mark>`)。
   - 點擊任一搜尋卡片立即精準直達簡報單頁（`?q=關鍵字#slide-XX`）。
   - 支援 14 大熱門心理學關鍵詞快速篩選（心理免疫、第二序列改變、成長型思維、應該思維、WOOP、控制兩分法、去三角化、課題分離、非暴力溝通、轉折三部曲、多元可能自我、英雄之旅、埃里克森、過勞倦怠）。

3. **首發旗艦教材：陳海賢《自我發展心理學》（了不起的我）16 頁無雜訊顧問簡報**
   - 遵循前 BCG 顧問森秀明「8 種簡報論法版型」與三大管顧視覺標準。
   - **雙視覺保證**：全 16 頁簡報每一頁皆包含高解析度向量架構圖 (Exhibit 1–16) 與結構化落地行動矩陣表格。
   - **雙層認知鷹架**：
     * **🌱 【入門者解讀】**：直擊日常痛點、生活化隱喻（象與騎象人、心靈煞車、追逃舞步、中性區間）。
     * **⚡ 【進階者模型】**：心理學底層機制與決策矩陣（Kegan 心理免疫四欄表、Watzlawick 控制論、Dweck 心態致勝、Ellis REBT、Bowen 去三角化、Bridges 轉折曲線、Campbell 英雄之旅、Erikson 生命地圖）。
   - **三段式演講備忘錄**：每一頁皆具備 ① 本頁核心結論、② 顧問深度脈絡、③ 下一頁轉場，支援快捷鍵 `N` 隨時開關。

---

## 📊 16 頁無雜訊顧問簡報逐頁架構表

| 頁碼 | 簡報主題 | 選用版型 | 管顧風格 | ① Action Title（本頁核心主張結論） | 核心模型 / 展覽圖 (Exhibit) |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **01** | 封面導讀 | 封面 Cover | McKinsey | 自我發展的核心不是修正個人缺陷，而是升級整個心理系統的運作架構 | [Exhibit 1](./images/exhibit-01-cover.svg) 五維系統模型 |
| **02** | 全景架構 | 版型 3 結合論法 | McKinsey | 人生突破本質為「心理系統升級」，須由行動、思維、關係至人生地圖五維深化支撐 | [Exhibit 2](./images/exhibit-02-combined-tree.svg) 金字塔演繹樹 |
| **03** | 行為改變 | 版型 4 連鎖論法 | BCG | 真正的改變發生在「具體新經驗」的體驗中，而非依賴理性說服情感大象 | [Exhibit 3](./images/exhibit-03-elephant-rider.svg) 象與騎象人迴路 |
| **04** | 心理免疫 | 版型 5 麥肯錫矩陣 | McKinsey | 所有停滯與拖延背後皆有「隱含好處」，須透視心理免疫系統之重大假設 | [Exhibit 4](./images/exhibit-04-kegan-xray.svg) Kegan 四欄 X 光片 |
| **05** | 系統改變 | 版型 6 對立論法 | Accenture | 陷入困境常因「第一序列改變」的徒勞循環，升級遊戲規則方為根本之道 | [Exhibit 5](./images/exhibit-05-order-change.svg) 第一 vs 第二序列改變 |
| **06** | 思維重構 | 版型 8 BCG 2×2 矩陣 | BCG | 擺脫「證明自己」轉向「發展自己」，高抗逆力源於成長探索心態 | [Exhibit 6](./images/exhibit-06-bcg-mindset.svg) Dweck 心智模式矩陣 |
| **07** | 認知解毒 | 版型 6 對立論法 | McKinsey | 痛苦源於把「願望」誤判為「理所當然」，理情反駁是破除防禦的利刃 | [Exhibit 7](./images/exhibit-07-should-thinking-abc.svg) 應該暴政 × Ellis ABC |
| **08** | 行動引擎 | 版型 7 比較論法 | BCG | 樂觀願望需碰撞內在障礙方釋放張力，精力聚焦於可控方能終結內耗 | [Exhibit 8](./images/exhibit-08-woop-stoic.svg) WOOP ∩ 斯多葛控制兩分法 |
| **09** | 關係系統 | 版型 5 麥肯錫矩陣 | McKinsey | 人際困境非單一個人性格缺陷，而是彼此角色互補構建的循環反饋系統 | [Exhibit 9](./images/exhibit-09-relational-system.svg) 語言層次與互補閉環 |
| **10** | 關係解套 | 版型 4 連鎖論法 | Accenture | 焦慮本能拉入第三方形成三角僵局，課題分離是劃清界限之關鍵解方 | [Exhibit 10](./images/exhibit-10-triangulation-adler.svg) 去三角化 × 課題分離 |
| **11** | 高質溝通 | 版型 4 連鎖論法 | BCG | 褪去批判防衛外衣，以「觀察-感受-需要-請求」重建高質量對話 | [Exhibit 11](./images/exhibit-11-nvc-four-steps.svg) 盧森堡 NVC 四步法 |
| **12** | 人生轉折 | 版型 4 連鎖論法 | McKinsey | 改變是外在事件，轉折是內在心理過渡，必經「結束-迷茫-重生」三部曲 | [Exhibit 12](./images/exhibit-12-bridges-transition.svg) Bridges 轉折 U 型曲線 |
| **13** | 生涯轉型 | 版型 8 BCG 2×2 矩陣 | BCG | 轉折期決策不可僅靠「經濟模型」，需以「心理模型」實驗多元可能自我 | [Exhibit 13](./images/exhibit-13-possible-selves-matrix.svg) Ibarra 多元可能自我 |
| **14** | 意義重構 | 版型 3 結合論法 | Accenture | 我們並非經歷的被動產物，而是能透過「救贖敘事」重構人生的英雄作者 | [Exhibit 14](./images/exhibit-14-heros-journey.svg) 坎伯英雄之旅演進樹 |
| **15** | 人生地圖 | 版型 5 麥肯錫矩陣 | McKinsey | 生命由一系列心理社會任務構成，各階段皆有其獨特危機與核心美德 | [Exhibit 15](./images/exhibit-15-erikson-lifemap.svg) 埃里克森四大成年階段 |
| **16** | 落地藍圖 | 版型 2 並列論法 | McKinsey | 啟動自我發展的落地三角：行為微步化、思維彈性化、關係邊界化 | [Exhibit 16](./images/exhibit-16-action-pillars.svg) 三大落地支柱矩陣 |

---

## 🧭 簡報檢視器操作快捷鍵

- `←` / `PageUp`：切換至上一頁簡報
- `→` / `PageDown` / `Space`：切換至下一頁簡報
- `N`：開啟／收合「三段式顧問講稿備忘錄」
- `F`：切換「全螢幕展示模式」
- `H`：返回心理學門戶首頁

---

## ➕ 未來新增心理學主題標準作業流程 (Topics #002 ~ #050)

1. 將主題相關文獻或 PDF 書摘收錄至 `Obsidian/DavidCloud/A2. 專業管理/A2.2 個人成長/A2.2.4 心理學/`。
2. 提煉該領域 10–16 個核心心智模型與無雜訊 Action Title。
3. 撰寫腳本產出高解析度向量展覽圖，並於 `scripts/generate_noisefree_pptx.py` 產出 `.pptx`。
4. 於 `search-index.js` 的 `topics`、`slides` 與 `concepts` 陣列註冊條目，全站毫秒級搜尋與處境分流即自動生效。

---
*大衛雲 2.0 ｜ DavidCloud Executive Knowledge System*
