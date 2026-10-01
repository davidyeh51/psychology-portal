/**
 * 心理學知識庫暨顧問簡報門戶 (Psychology Portal) — 核心互動與檢索引擎 (app.js)
 * 支援功能：
 * 1. 門戶首頁 (index.html)：毫秒級全站跨書／跨簡報頁關鍵字即時檢索、標記高亮、認知層級篩選
 * 2. 簡報檢視器 (chen-haixian-self-development.html)：鍵盤導航 (←/→/Space)、全螢幕 (F)、講稿備忘錄 (N)、快速跳轉
 */

(function () {
  "use strict";

  // 工具函式：跳脫正規表達式特殊字元
  function escapeRegExp(str) {
    return (str || "").replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  // 工具函式：關鍵字螢光高亮標記
  function highlightText(text, query) {
    if (!query || !text) return text || "";
    const terms = query
      .trim()
      .split(/\s+/)
      .filter(Boolean)
      .map(escapeRegExp);
    if (!terms.length) return text;
    const regex = new RegExp("(" + terms.join("|") + ")", "gi");
    return String(text).replace(regex, '<mark class="search-hl">$1</mark>');
  }

  /* ========================================================================
     PART A: 門戶首頁邏輯 (index.html)
     ======================================================================== */
  function initPortalPage() {
    const searchInput = document.getElementById("globalSearchInput");
    const searchResultsPanel = document.getElementById("searchResultsPanel");
    const searchResultsGrid = document.getElementById("searchResultsGrid");
    const searchResultCount = document.getElementById("searchResultCount");
    const btnClearSearch = document.getElementById("btnClearSearch");
    const kwChips = document.querySelectorAll(".kw-chip");
    const cogPills = document.querySelectorAll(".cog-pill");
    const topicCards = document.querySelectorAll(".topic-card");

    if (!searchInput) return;

    let activeCogLevel = "all"; // 'all' | 'beginner' | 'advanced'

    function performGlobalSearch(rawQuery) {
      const q = (rawQuery || "").trim().toLowerCase();
      if (!q) {
        if (searchResultsPanel) searchResultsPanel.classList.remove("active");
        topicCards.forEach((c) => (c.style.display = ""));
        if (btnClearSearch) btnClearSearch.style.display = "none";
        return;
      }

      if (btnClearSearch) btnClearSearch.style.display = "block";
      const terms = q.split(/\s+/).filter(Boolean);

      const db = window.PSYCHOLOGY_SEARCH_INDEX;
      if (!db) return;

      const matchedSlides = [];
      const matchedTopics = [];
      const matchedConcepts = [];

      // 1. 檢索 16 頁簡報
      (db.slides || []).forEach((slide) => {
        const fullContent = [
          slide.title,
          slide.actionTitle,
          slide.beginnerTakeaway,
          slide.advancedModel,
          slide.category,
          slide.layout,
          ...(slide.keywords || []),
        ]
          .join(" ")
          .toLowerCase();

        const match = terms.every((t) => fullContent.includes(t));
        if (match) {
          // 認知層級過濾
          if (activeCogLevel === "beginner" && !slide.beginnerTakeaway) return;
          if (activeCogLevel === "advanced" && !slide.advancedModel) return;
          matchedSlides.push(slide);
        }
      });

      // 2. 檢索主題領域
      (db.topics || []).forEach((tp) => {
        const content = [tp.title, tp.author, tp.category, tp.summary, ...(tp.tags || [])]
          .join(" ")
          .toLowerCase();
        if (terms.every((t) => content.includes(t))) {
          matchedTopics.push(tp);
        }
      });

      // 3. 檢索粒度概念庫
      (db.concepts || []).forEach((cp) => {
        const content = [cp.term, cp.category, cp.def].join(" ").toLowerCase();
        if (terms.every((t) => content.includes(t))) {
          matchedConcepts.push(cp);
        }
      });

      // 渲染搜尋結果
      renderSearchResults(q, matchedSlides, matchedTopics, matchedConcepts);
    }

    function renderSearchResults(q, slides, topics, concepts) {
      if (!searchResultsPanel || !searchResultsGrid) return;
      const totalCount = slides.length + topics.length + concepts.length;

      searchResultCount.textContent = `找到 ${totalCount} 個與「${q}」高度相關之結果（簡報頁：${slides.length} ｜ 主題：${topics.length} ｜ 核心概念：${concepts.length}）`;
      searchResultsPanel.classList.add("active");

      let html = "";

      if (totalCount === 0) {
        html = `
          <div style="grid-column: 1 / -1; padding: 2rem; text-align: center; color: var(--text-muted);">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔍</div>
            <p>未找到符合「<strong>${q}</strong>」的相關內容。</p>
            <p style="font-size: 0.85rem; margin-top: 0.5rem;">建議嘗試其他熱門關鍵字：心理免疫、第二序列改變、成長型思維、應該思維、WOOP、課題分離、非暴力溝通、英雄之旅。</p>
          </div>
        `;
      } else {
        // 渲染簡報命中項目
        slides.forEach((s) => {
          html += `
            <div class="search-card">
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
                  <span class="slide-category-badge">投影片 #${s.number} ｜ ${highlightText(s.category, q)}</span>
                  <span style="font-size:0.75rem; color:#64748B;">${s.layout}</span>
                </div>
                <h4 style="font-size:1.05rem; font-weight:700; color:var(--primary-navy); margin-bottom:0.5rem;">
                  ${highlightText(s.actionTitle, q)}
                </h4>
                <div style="font-size:0.85rem; color:var(--text-body); margin-bottom:0.6rem; background:#FFFFFF; padding:0.6rem; border-radius:6px; border:1px solid #E2E8F0;">
                  <strong style="color:#15803D;">【入門痛點】</strong> ${highlightText(s.beginnerTakeaway, q)}
                </div>
                <div style="font-size:0.85rem; color:var(--text-body); margin-bottom:0.6rem; background:#FFFFFF; padding:0.6rem; border-radius:6px; border:1px solid #E2E8F0;">
                  <strong style="color:#0369A1;">【進階模型】</strong> ${highlightText(s.advancedModel, q)}
                </div>
              </div>
              <div style="margin-top:0.75rem; display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:0.75rem; color:#94A3B8;">風格：${s.style.toUpperCase()}</span>
                <a href="${s.anchor}" class="btn-card btn-card-gold" style="font-size:0.8rem; padding:0.35rem 0.75rem;">
                  直達此簡報頁 →
                </a>
              </div>
            </div>
          `;
        });

        // 渲染主題領域
        topics.forEach((t) => {
          html += `
            <div class="search-card" style="border-left: 4px solid var(--royal-blue);">
              <div>
                <span class="topic-badge badge-featured">主題領域</span>
                <h4 style="font-size:1.05rem; font-weight:700; color:var(--primary-navy); margin-bottom:0.3rem;">
                  ${highlightText(t.title, q)}
                </h4>
                <p style="font-size:0.825rem; color:#64748B; margin-bottom:0.5rem;">${highlightText(t.author, q)} ｜ ${t.category}</p>
                <p style="font-size:0.85rem; color:var(--text-body);">${highlightText(t.summary, q)}</p>
              </div>
              <div style="margin-top:0.75rem;">
                <a href="${t.deckUrl}" class="btn-card btn-card-primary" style="font-size:0.8rem; padding:0.35rem 0.75rem;">
                  進入教材門戶 →
                </a>
              </div>
            </div>
          `;
        });

        // 渲染核心概念
        concepts.forEach((cp) => {
          html += `
            <div class="search-card" style="border-left: 4px solid var(--accent-gold);">
              <div>
                <span class="slide-category-badge" style="background:#FEF3C7; color:#B45309;">核心概念詞條</span>
                <h4 style="font-size:1rem; font-weight:700; color:var(--primary-navy); margin:0.3rem 0;">
                  ${highlightText(cp.term, q)}
                </h4>
                <p style="font-size:0.85rem; color:var(--text-body);">${highlightText(cp.def, q)}</p>
              </div>
              <div style="margin-top:0.75rem; font-size:0.75rem; color:#64748B;">
                分類：${cp.category}
              </div>
            </div>
          `;
        });
      }

      searchResultsGrid.innerHTML = html;
      searchResultsPanel.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }

    // 防抖輸入事件
    let debounceTimer;
    searchInput.addEventListener("input", (e) => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        performGlobalSearch(e.target.value);
      }, 250);
    });

    if (btnClearSearch) {
      btnClearSearch.addEventListener("click", () => {
        searchInput.value = "";
        performGlobalSearch("");
        searchInput.focus();
      });
    }

    // 快捷標籤點擊
    kwChips.forEach((chip) => {
      chip.addEventListener("click", () => {
        const kw = chip.getAttribute("data-kw") || chip.textContent.trim();
        searchInput.value = kw;
        performGlobalSearch(kw);
      });
    });

    // 認知層級切換
    cogPills.forEach((pill) => {
      pill.addEventListener("click", () => {
        cogPills.forEach((p) => p.classList.remove("active"));
        pill.classList.add("active");
        activeCogLevel = pill.getAttribute("data-level") || "all";
        performGlobalSearch(searchInput.value);
      });
    });

    // 鍵盤按下 '/' 聚焦搜尋框
    window.addEventListener("keydown", (e) => {
      if (e.key === "/" && document.activeElement !== searchInput) {
        e.preventDefault();
        searchInput.focus();
      }
    });
  }

  /* ========================================================================
     PART B: 簡報檢視器邏輯 (chen-haixian-self-development.html)
     ======================================================================== */
  function initDeckPage() {
    const slides = (window.PSYCHOLOGY_SEARCH_INDEX && window.PSYCHOLOGY_SEARCH_INDEX.slides) || [];
    if (!slides.length) return;

    let currentIndex = 0;

    const btnPrev = document.getElementById("btnPrevSlide");
    const btnNext = document.getElementById("btnNextSlide");
    const slideCounter = document.getElementById("slideCounter");
    const quickJumpSelect = document.getElementById("quickJumpSelect");
    const btnToggleNotes = document.getElementById("btnToggleNotes");
    const btnFullscreen = document.getElementById("btnFullscreen");
    const notesDrawer = document.getElementById("speakerNotesDrawer");
    const thumbContainer = document.getElementById("thumbGridContainer");

    // 取得各顯示欄位
    const slideActionTitle = document.getElementById("slideActionTitle");
    const slideCategoryBadge = document.getElementById("slideCategoryBadge");
    const slideLayoutTag = document.getElementById("slideLayoutTag");
    const slideExhibitImg = document.getElementById("slideExhibitImg");
    const exhibitCaption = document.getElementById("exhibitCaption");
    const beginnerContent = document.getElementById("beginnerContent");
    const advancedContent = document.getElementById("advancedContent");
    const actionTableWrap = document.getElementById("actionTableWrap");
    const slideFooterSource = document.getElementById("slideFooterSource");

    // 講稿備忘欄位
    const noteConclusion = document.getElementById("noteConclusion");
    const noteExplanation = document.getElementById("noteExplanation");
    const noteTransition = document.getElementById("noteTransition");

    // 解析初始 URL Hash (例如 #slide-04)
    function parseHash() {
      const hash = window.location.hash;
      if (hash && hash.startsWith("#slide-")) {
        const num = parseInt(hash.replace("#slide-", ""), 10);
        if (!isNaN(num) && num >= 1 && num <= slides.length) {
          return num - 1;
        }
      }
      return 0;
    }

    // 載入指定簡報頁
    function goToSlide(idx) {
      if (idx < 0) idx = 0;
      if (idx >= slides.length) idx = slides.length - 1;
      currentIndex = idx;

      const s = slides[idx];
      const slideNumFormatted = String(idx + 1).padStart(2, "0");

      // 更新 URL Hash (不觸發重複跳轉)
      history.replaceState(null, "", `#slide-${slideNumFormatted}`);

      // 更新導覽欄與計數
      if (slideCounter) slideCounter.textContent = `${idx + 1} / ${slides.length}`;
      if (quickJumpSelect) quickJumpSelect.value = idx;

      if (btnPrev) btnPrev.disabled = idx === 0;
      if (btnNext) btnNext.disabled = idx === slides.length - 1;

      // 更新主畫面內容
      if (slideActionTitle) slideActionTitle.textContent = s.actionTitle;
      if (slideCategoryBadge) slideCategoryBadge.textContent = s.category;
      if (slideLayoutTag) slideLayoutTag.textContent = `${s.layout}  ｜  ${s.style.toUpperCase()} Style`;

      if (slideExhibitImg) {
        slideExhibitImg.src = s.exhibit;
        slideExhibitImg.alt = s.actionTitle;
      }
      if (exhibitCaption) {
        exhibitCaption.textContent = `EXHIBIT ${idx + 1} ｜ ${s.title} 核心架構圖`;
      }

      if (beginnerContent) beginnerContent.textContent = s.beginnerTakeaway;
      if (advancedContent) advancedContent.textContent = s.advancedModel;
      if (slideFooterSource) {
        slideFooterSource.textContent = `Source: 陳海賢《了不起的我：自我發展的心理學》 ｜ 投影片 #${idx + 1} ｜ 大衛雲 2.0 A2.2.4`;
      }

      // 載入講稿備忘錄
      loadSpeakerNotes(idx);

      // 動態產生結構化落地行動矩陣表格
      renderActionTable(idx);

      // 更新縮圖活動狀態
      updateThumbnailActive(idx);
    }

    // 載入三段式顧問講稿
    function loadSpeakerNotes(idx) {
      // 講稿取自 search-index 延伸資料或預設模板
      const notesData = [
        {
          conclusion: "自我發展的核心不是『修正個人缺陷』，而是『升級整個心理系統的運作架構』。",
          explanation: "本份簡報萃取陳海賢博士 50 講精華，以頂尖顧問公司無雜訊標準製作，旨在為入門者提供痛點破解方案，為進階者建立系統性心智模型。",
          transition: "首先，讓我們透過全景架構圖，鳥瞰自我發展的五大進階維度。"
        },
        {
          conclusion: "自我發展絕非修修補補，而是整個心智操作系統由下而上的結構性升級。",
          explanation: "很多人改變失敗，以為是自己自律不足，實際上是因為行動、思維與關係的系統沒有連動。只有系統同步升級，改變才能持久。",
          transition: "接著，我們深入模組一，探討行為改變的深層動力機制。"
        },
        {
          conclusion: "推動行為改變的根本密碼，是為感性大象創造『切身體會到的新經驗』。",
          explanation: "入門者常誤以為改變靠咬牙堅持，進階者則懂得設計環境場與微型第一步，讓大象在沒有阻力的情況下嚐到甜頭，自發向前走。",
          transition: "然而，當我們想採取新行動時，常遭遇內在頑固的阻抗，這就是羅伯特·凱根提出的心理免疫系統。"
        },
        {
          conclusion: "表面上的拖延不是意志力缺陷，而是心理免疫系統在忠實保護我們的安全感。",
          explanation: "當我們看見相反行為背後的『競爭性承諾』與『重大假設』時，內疚與自責就會消解，轉而能用科學實驗的心態去檢驗那些過時的假設。",
          transition: "在診斷完免疫系統後，我們必須區分兩種截然不同的改變層次：第一序列改變與第二序列改變。"
        },
        {
          conclusion: "當現有的解決方式無效時，再加大劑量只會毒害系統；唯有跳到系統之外，才能引發第二序列改變。",
          explanation: "入門者常陷入『加倍努力』的旋渦，進階者則會退後一步審視：我正在玩的遊戲規則到底是什麼？如何重新定義問題？",
          transition: "要實現第二序列改變，我們必須進入第二模組，徹底檢視我們的大腦操作系統——心智模式。"
        },
        {
          conclusion: "僵固型思維追求『證明自己』，成長型思維專注『發展自己』；後者讓挫折從『身分判決』轉變為『學習數據』。",
          explanation: "對角線的僵固防禦與成長探索呈現完全對立的人生軌跡。只要改變詮釋挫折的視角，犯錯就從恥辱變成了成長的養分。",
          transition: "除了心智模式，思維中最常見的內耗元兇，就是強加在自己與世界身上的『應該思維』。"
        },
        {
          conclusion: "應該思維是企圖用主觀願望霸凌客觀現實；破除它的關鍵是把『我應該』換成『我希望，但我也能接納不如意』。",
          explanation: "當我們將 A-B-C 框架熟練運用於日常，我們就奪回了對情緒的自主權——事件無法傷害我們，是我們對事件的信念在傷害我們。",
          transition: "瓦解了無效思維後，我們要如何將內在張力轉化為澎湃的行動力？這需要 WOOP 與控制兩分法。"
        },
        {
          conclusion: "盲目的正向思考是無效的糖衣；真正的行動力來自『看見障礙（WOOP）』與『收斂至可控（控制兩分法）』的結合。",
          explanation: "左邊提供推進的引擎動力，右邊提供聚焦的導航羅盤。中央的交集正是顧問界最強調的『執行意圖閉環』。",
          transition: "個人的行為與思維理順之後，我們必須將視角擴展到人際網絡——進入模組三：關係的改變。"
        },
        {
          conclusion: "自我不是孤立的島嶼，而是在關係中被定義的節點。看懂系統互補，就沒有絕對的受害者與加害者。",
          explanation: "當我們從線性因果切換到循環因果，我們就擁有了改變關係的主動權——因為只要我們停止原有的舞步，整場雙人舞就必須重編。",
          transition: "在所有關係病理中，最常見且具破壞性的，便是將第三方捲入衝突的『三角化』與黏稠的糾纏。"
        },
        {
          conclusion: "三角化是關係焦慮的止痛藥，卻是系統健康的慢性毒藥。唯有課題分離，才能將每個人歸還給自己。",
          explanation: "當我們不再做他人的情緒垃圾桶或代罪羔羊，我們才能在邊界分明的基礎上，展開真正有愛而獨立的互動。",
          transition: "劃清了界限之後，我們要如何開口溝通？馬歇爾·盧森堡的『非暴力溝通』給出了精準的操作範本。"
        },
        {
          conclusion: "所有的指責都是未獲滿足需要的悲劇表達；NVC 讓我們繞過防禦機制，直達彼此的心靈核心。",
          explanation: "入門者常把觀點當事實，把命令當請求。依序落實四步，就能將攻擊性的辯駁轉化為建設性的合作對話。",
          transition: "在掌握了行為、思維與關係後，人生難免會遭遇劇烈變故與重大轉向——我們進入模組四：轉折期的改變。"
        },
        {
          conclusion: "外在的改變發生在一瞬間，但內在的心理轉折需要經過漫長的哀傷、等待與孵化。",
          explanation: "人們最害怕中性區間的迷茫，但迷茫正是創新的溫床。進階者懂得陪伴自己在中性區間沉澱，而不是慌忙抓住下一個救命稻草。",
          transition: "在轉折期面臨重大職涯或人生選擇時，我們該依據什麼模型來做決策？"
        },
        {
          conclusion: "職業轉型的真正祕訣不是『先想清楚再行動』，而是『先行動起來，在實踐中看見可能的自己』。",
          explanation: "對角線呈現了傳統保守困局與現代多元自我的鮮明對立。透過平行實驗，我們得以在保障生存的同時，給新自我充足的生長時間。",
          transition: "當我們穿越轉折的試煉，我們又是如何詮釋這段旅程？這涉及到敘事心理學與坎伯的英雄之旅。"
        },
        {
          conclusion: "事件本身沒有絕對意義，是我們講述故事的方式定義了人生。從『污染故事』轉向『救贖故事』，人就成為了英雄。",
          explanation: "英雄之旅不是神話，而是每個人自我演化的必經儀式。苦難若無領悟，就只是創傷；苦難若伴隨救贖，就成為無價的生命恩賜。",
          transition: "最後，將視角拉伸至整個人生維度——我們進入模組五：人生發展階段與人生地圖。"
        },
        {
          conclusion: "人生不是一場有標準答案的競速賽，而是一幅依序展開的生命地圖；每個年齡段都有其不可替代的心靈使命。",
          explanation: "很多人在中年焦慮或晚年空虛，往往是因為前期任務未解。看懂地圖，我們就能寬容地對待自己的年齡，專注於當下階段的核心課題。",
          transition: "綜觀全書五大模組，我們如何將這些深刻的心理學智慧落實為日常行動？我們看最後一頁的總結行動藍圖。"
        },
        {
          conclusion: "自我發展不是一場一蹴而就的風暴，而是一場潤物無聲的系統演化。",
          explanation: "從行為的小步開始，以思維的彈性維持張力，在關係的邊界中守護自我，最後在轉折與歲月中走出屬於自己的英雄之旅。",
          transition: "願每位讀者都能看懂自己的心理系統，成為『了不起的自己』！感謝聆聽。"
        }
      ];

      const note = notesData[idx] || notesData[0];
      if (noteConclusion) noteConclusion.textContent = note.conclusion;
      if (noteExplanation) noteExplanation.textContent = note.explanation;
      if (noteTransition) noteTransition.textContent = note.transition;
    }

    // 產生結構化落地行動矩陣表格
    function renderActionTable(idx) {
      if (!actionTableWrap) return;
      const tables = [
        // 1
        { headers: ["層級維度", "核心目標", "落地檢核標準"], rows: [["頂層願景", "心理系統全面升級", "打破舊有行為、思維與關係之循環瓶頸"], ["中層支柱", "三位一體協同", "行動創造新經驗 ＋ 思維彈性反駁 ＋ 關係界限分明"], ["底層場景", "穿越生命轉折", "耐受中性區間迷茫，完成生命週期使命"]] },
        // 2
        { headers: ["系統模組", "關鍵心理模型", "進階思考架構"], rows: [["行動系統", "象與騎象人 × 心理免疫", "以新經驗的好處覆蓋舊經驗，小步反證重大假設"], ["心智系統", "成長型思維 × WOOP", "區分學習目標與表現目標，100% 精力收斂於可控"], ["關係系統", "系統動力學 × 課題分離", "看穿話外音與互補閉環，退出三角化，非暴力溝通"]] },
        // 3
        { headers: ["執行階段", "入門白話痛點", "進階顧問操作策略"], rows: [["01 理性引導", "懂得很多道理卻做不到", "騎象人明確定義具體目標，不追求一次性大飛躍"], ["02 情感喚醒", "不斷自責導致大象癱瘓", "停止道德批判，營造安全感，以期待激發大象好奇心"], ["03 小步環境", "意志力耗竭而半途而廢", "奇蹟提問倒推最小一步；指定單一物理空間綁定微習慣"]] },
        // 4
        { headers: ["診斷維度", "職場典型案例", "破局實踐要領"], rows: [["改變目標", "爭取領導跨部門專案", "確認發自內心渴望，而非盲目迎合外在應該"], ["相反行為", "會議中低頭、推託責任", "將相反行為視為客觀調查數據，不對自己進行道德羞辱"], ["競爭承諾", "承諾保護自己不成為靶子", "看清隱含好處，感謝防禦系統過去對脆弱自我的保護"], ["重大假設", "「若我主動失敗就證明我無能」", "設計低風險安全小測試，在現實中驗證該假設是否必定成立"]] },
        // 5
        { headers: ["比較維度", "第一序列改變 (狀態微調)", "第二序列改變 (規則重構) ★"], rows: [["本質特徵", "More of the same (更多同樣的努力)", "Reframing (改變系統邊界與遊戲規則)"], ["典型閉環", "失眠時逼自己睡，越逼越焦慮", "坦然接納清醒，起床看書，消除對失眠的恐懼"], ["適用情境", "常規、線性、既有軌道正常運轉時", "反覆努力無效、陷入死循環、需質變躍遷時"]] },
        // 6
        { headers: ["思維類型", "對待錯誤態度", "終身發展結果"], rows: [["僵固型思維", "錯誤 = 自我價值的宣判 (極力隱瞞)", "脆弱高自尊，迴避挑戰，天花板過早鎖死"], ["成長型思維", "錯誤 = 高價值的客觀學習數據 (積極迭代)", "高心理韌性，主動犯可承受的小錯，終身複利成長"]] },
        // 7
        { headers: ["Ellis 步驟", "非理性應該信念 (盲區)", "理性情緒反駁介入 (D) ★"], rows: [["A (事件)", "重要提案被老闆退件修正", "客觀描述退件事實，不加主觀災難化想像"], ["B (信念)", "「他看不起我，我永遠做不好」", "反駁：「退件代表格式需調整，何以證明看不起我？」"], ["C ➔ E", "自暴自棄、冷戰消極怠工", "有效新信念：接納現實，專注吸收回饋並迅速修正"]] },
        // 8
        { headers: ["工具名稱", "核心心法", "落地對接方案"], rows: [["WOOP 引擎", "心理對比創造不可遏制的張力", "Wish ➔ Outcome ➔ Obstacle (內在障礙) ➔ Plan"], ["控制兩分法", "100% 精力收斂於完全可控領域", "將可控行動填入 WOOP 的 If-Then 執行意圖中！"]] },
        // 9
        { headers: ["維度層次", "個體孤島視角 (盲點)", "系統動力視角 (顧問深度) ★"], rows: [["語言解讀", "執著於表面「內容資訊」講道理", "聽懂「關係資訊」：話外音中的身分與權力爭奪"], ["角色因果", "單向歸因：「因為你冷漠我才吵」", "循環互補：「你追越緊我逃越遠，你越追」"], ["重構策略", "試圖強行改變對方", "主動改變自身舞步，打破反饋鏈，引領關係演化"]] },
        // 10
        { headers: ["演進階段", "三角化僵局特徵", "課題分離處方"], rows: [["焦慮產生", "雙人衝突難以直面承擔", "承認核心矛盾，停止拉入第三方分擔壓力"], ["夾心毒害", "第三方成為代罪羔羊或情緒盟友", "堅定退出結盟：「這是你們的課題，請直接對話」"], ["邊界重組", "情緒糾纏不清，互相情緒勒索", "黃金法則：誰承受直接後果誰承擔，劃清責任線"]] },
        // 11
        { headers: ["NVC 步驟", "錯誤溝通模式 (攻擊與評判)", "非暴力溝通典範 (正向推進) ★"], rows: [["1. 觀察", "「你開會總是漫不經心遲到！」", "「這週三次會議，你在開場後15分鐘進入」"], ["2. 感受", "「我覺得你根本不重視團隊！」", "「當會議延遲開始時，我感到沮喪與焦慮」"], ["3. 需要", "忽視需求，直接指責發洩情緒", "「因為我非常需要團隊能保持節奏一致」"], ["4. 請求", "「請你以後態度認真一點！」", "「明早九點專案會，你能否提前5分鐘上線準備？」"]] },
        // 12
        { headers: ["轉折階段", "心理狀態特徵", "核心演化任務"], rows: [["結束 (Endings)", "喪失感、角色瓦解、悲傷", "允許哀傷，舉辦告別儀式，正式脫離舊自我"], ["迷茫 (Neutral)", "混沌真空、空虛、缺乏安全感", "耐受空白，避免慌忙抓錯稻草，孵化新可能"], ["重生 (Beginnings)", "內在指南針校準、萌發新熱情", "重整個人價值觀優先序，以微步行動啟程"]] },
        // 13
        { headers: ["決策模式", "一刀切豪賭", "平行小步試驗 (多元可能自我) ★"], rows: [["經濟模型", "盲目裸辭換賽道，財務壓力反噬新自我", "純功利副業，雖分散風險但缺乏熱情與自我更新"], ["心理模型", "空想職涯規劃，陷入沉沒成本不敢動", "保留生存底線，在實踐中孵化新身分，安全過渡"]] },
        // 14
        { headers: ["英雄之旅階段", "心靈演化考驗", "救贖敘事轉化"], rows: [["啟程 (Departure)", "跨越日常邊界，回應內在召喚", "不再做被動受害者，主動承擔探索未知之責任"], ["深淵 (Initiation)", "遭遇嚴酷挫折，舊自我粉碎瓦解", "「正是這段深淵，賦予我前所未有的慈悲與韌性」"], ["回歸 (Return)", "帶著超凡智慧與良藥重返生活", "以導師姿態陪伴他人，將苦難昇華為生命的恩賜"]] },
        // 15
        { headers: ["生命階段", "核心心理衝突", "獲得心靈美德"], rows: [["青春期", "同一性 vs. 角色混亂 (我是誰？)", "【忠誠 Fidelity】確立真實自我方向與邊界"], ["成年早期", "親密感 vs. 孤獨感 (敢於愛人與立業)", "【愛 Love】在深刻連結中保有獨立主體性"], ["中年期", "繁殖/創生感 vs. 停滯感 (教養傳承)", "【關懷 Care】超越個人私利，滋養下一代"], ["晚年期", "自我整合 vs. 絕望 (審視一生得失)", "【智慧 Wisdom】以超然坦然接納生命終局"]] },
        // 16
        { headers: ["落地支柱", "核心心理工具", "每日微習慣實踐檢核"], rows: [["行為微步化", "小步子原理 ＋ 環境場 ＋ 第二序列", "「今天我是否為大象創造了一個愉悅微小的新經驗？」"], ["思維彈性化", "WOOP 引擎 ＋ 控制兩分法 ＋ ABC反駁", "「我正在為證明自己焦慮，還是為發展自己探索？」"], ["關係邊界化", "課題分離 ＋ 去三角化 ＋ NVC溝通", "「我是否管好了自己的課題，並為他人留出獨立空間？」"]] }
      ];

      const tData = tables[idx] || tables[0];
      let html = `<table class="slide-action-table"><thead><tr>`;
      tData.headers.forEach((h) => {
        html += `<th>${h}</th>`;
      });
      html += `</tr></thead><tbody>`;
      tData.rows.forEach((r) => {
        html += `<tr>`;
        r.forEach((c) => {
          html += `<td>${c}</td>`;
        });
        html += `</tr>`;
      });
      html += `</tbody></table>`;
      actionTableWrap.innerHTML = html;
    }

    // 初始化縮圖列表
    function initThumbnails() {
      if (!thumbContainer) return;
      let html = "";
      slides.forEach((s, i) => {
        html += `
          <div class="thumb-item ${i === currentIndex ? "active" : ""}" data-idx="${i}">
            <div class="thumb-num">#${s.number}</div>
            <div class="thumb-title">${s.title}</div>
          </div>
        `;
      });
      thumbContainer.innerHTML = html;

      const thumbItems = thumbContainer.querySelectorAll(".thumb-item");
      thumbItems.forEach((item) => {
        item.addEventListener("click", () => {
          const idx = parseInt(item.getAttribute("data-idx"), 10);
          goToSlide(idx);
        });
      });
    }

    function updateThumbnailActive(idx) {
      if (!thumbContainer) return;
      const items = thumbContainer.querySelectorAll(".thumb-item");
      items.forEach((it, i) => {
        if (i === idx) it.classList.add("active");
        else it.classList.remove("active");
      });
    }

    // 初始化快速跳轉下拉選單
    function initQuickJumpSelect() {
      if (!quickJumpSelect) return;
      let html = "";
      slides.forEach((s, i) => {
        html += `<option value="${i}">#${s.number} ｜ ${s.title}</option>`;
      });
      quickJumpSelect.innerHTML = html;
      quickJumpSelect.addEventListener("change", (e) => {
        goToSlide(parseInt(e.target.value, 10));
      });
    }

    // 事件監聽綁定
    if (btnPrev) btnPrev.addEventListener("click", () => goToSlide(currentIndex - 1));
    if (btnNext) btnNext.addEventListener("click", () => goToSlide(currentIndex + 1));

    if (btnToggleNotes) {
      btnToggleNotes.addEventListener("click", () => {
        if (notesDrawer) notesDrawer.classList.toggle("open");
      });
    }

    if (btnFullscreen) {
      btnFullscreen.addEventListener("click", () => {
        const stage = document.querySelector(".slide-stage");
        if (!document.fullscreenElement) {
          if (stage && stage.requestFullscreen) stage.requestFullscreen();
        } else {
          if (document.exitFullscreen) document.exitFullscreen();
        }
      });
    }

    // 鍵盤導航快捷鍵
    window.addEventListener("keydown", (e) => {
      // 避免在輸入框打字時誤觸
      if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;

      if (e.key === "ArrowRight" || e.key === "PageDown" || e.key === " ") {
        e.preventDefault();
        goToSlide(currentIndex + 1);
      } else if (e.key === "ArrowLeft" || e.key === "PageUp") {
        e.preventDefault();
        goToSlide(currentIndex - 1);
      } else if (e.key === "f" || e.key === "F") {
        e.preventDefault();
        if (btnFullscreen) btnFullscreen.click();
      } else if (e.key === "n" || e.key === "N") {
        e.preventDefault();
        if (btnToggleNotes) btnToggleNotes.click();
      } else if (e.key === "h" || e.key === "H") {
        window.location.href = "index.html";
      }
    });

    // 監聽 URL Hash 變更
    window.addEventListener("hashchange", () => {
      goToSlide(parseHash());
    });

    // 啟動初始化
    initQuickJumpSelect();
    initThumbnails();
    goToSlide(parseHash());
  }

  // 頁面加載完成後自動分流執行
  document.addEventListener("DOMContentLoaded", () => {
    initPortalPage();
    initDeckPage();
  });
})();
