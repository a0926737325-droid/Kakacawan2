import streamlit as st
import random
from datetime import datetime, date

# ==========================================
# 1. 系統設定 (UIUX-CRF v9.0 認知鎖定)
# ==========================================
st.set_page_config(
    page_title="2026 長濱鄉部落深度旅遊 (星空與海浪版)",
    page_icon="🌊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS 美學 (太平洋藍 x 部落大地色系)
# ==========================================
st.markdown("""
    <style>
    /* 1. 全站背景：淺海浪白，字體深灰藍 */
    .stApp {
        background-color: #F0F8FF; 
        font-family: "Microsoft JhengHei", sans-serif;
        color: #1C2833 !important;
    }
    
    /* 2. 強制一般文字元素為深色 */
    p, div, span, h1, h2, h3, h4, h5, h6, label, .stMarkdown {
        color: #1C2833 !important;
    }

    /* === 3. 核心修復：輸入框與選單白底黑字 === */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="input"] > div, 
    div[data-baseweb="base-input"] {
        background-color: #ffffff !important;
        border: 1px solid #B0C4DE !important;
        color: #1C2833 !important;
    }
    input { color: #1C2833 !important; }
    div[data-baseweb="select"] span { color: #1C2833 !important; }
    ul[data-baseweb="menu"] { background-color: #ffffff !important; }
    li[data-baseweb="option"] { color: #1C2833 !important; }
    svg { fill: #1C2833 !important; color: #1C2833 !important; }

    /* === 4. 日期選單高亮 (海洋風) === */
    div[data-testid="stDateInput"] > label {
        color: #005A9C !important; 
        font-size: 24px !important; 
        font-weight: 900 !important;
        text-shadow: 0px 0px 5px rgba(0, 119, 182, 0.4);
        margin-bottom: 10px !important;
        display: block;
    }
    div[data-testid="stDateInput"] div[data-baseweb="input"] {
        border: 3px solid #0077B6 !important; 
        background-color: #E0F7FA !important;
        border-radius: 10px !important;
        box-shadow: 0 0 15px rgba(0, 119, 182, 0.2); 
    }

    /* 隱藏官方元件 */
    header {visibility: hidden;}
    footer {display: none !important;}
    
    /* 標題區：星空與海洋漸層 */
    .header-box {
        background: linear-gradient(135deg, #003049 0%, #0077B6 100%);
        padding: 30px 20px;
        border-radius: 0 0 30px 30px;
        color: white !important;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0, 119, 182, 0.4);
        margin-top: -60px;
    }
    .header-box h1, .header-box div, .header-box span { color: white !important; }
    .header-title { font-size: 28px; font-weight: bold; text-shadow: 1px 1px 3px rgba(0,0,0,0.5); }
    
    /* 輸入卡片 */
    .input-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 1px solid #B0C4DE;
        margin-bottom: 20px;
    }
    
    /* 按鈕 (大地色/原木色) */
    .stButton>button {
        width: 100%;
        background-color: #D4A373;
        color: white !important;
        border-radius: 50px;
        border: none;
        padding: 12px 0;
        font-weight: bold;
        transition: 0.3s;
        font-size: 18px;
        box-shadow: 0 4px 6px rgba(212, 163, 115, 0.4);
    }
    .stButton>button:hover { background-color: #FAEDCD; color: #D4A373 !important; }
    
    /* 資訊看板 */
    .info-box {
        background-color: #FEFAE0;
        border-left: 5px solid #CCD5AE;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    
    /* 時間軸 */
    .timeline-item {
        border-left: 3px solid #0077B6;
        padding-left: 20px;
        margin-bottom: 20px;
        position: relative;
    }
    .timeline-item::before {
        content: '🌾';
        position: absolute;
        left: -13px;
        top: 0;
        background: #F0F8FF;
        border-radius: 50%;
    }
    .day-header {
        background: #E0F7FA;
        color: #005A9C !important;
        padding: 5px 15px;
        border-radius: 15px;
        display: inline-block;
        margin-bottom: 15px;
        font-weight: bold;
    }
    .spot-title { font-weight: bold; color: #005A9C !important; font-size: 18px; }
    .spot-tag { 
        font-size: 12px; background: #E9ECEF; color: #495057 !important; 
        padding: 2px 8px; border-radius: 10px; margin-right: 5px;
    }
    
    /* 住宿卡片 */
    .hotel-card {
        background: #FAFAFA;
        border-left: 5px solid #D4A373;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .hotel-tag {
        font-size: 11px;
        background: #D4A373;
        color: white !important;
        padding: 2px 6px;
        border-radius: 8px;
        margin-right: 5px;
    }
    
    /* 景點名錄小卡 */
    .mini-card {
        background: white;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #eee;
        font-size: 14px;
        margin-bottom: 8px;
        border-left: 3px solid #00B4D8;
    }
    .feature-badge {
        background: #00B4D8; color: white !important; padding: 1px 5px; border-radius: 4px; font-size: 11px; margin-left: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 核心資料庫 (Custom-CRF v9.0 長濱實體資料)
# ==========================================
all_spots_db = [
    # --- 北長濱 (自然地景與歷史) ---
    {"name": "樟原船型教堂", "region": "北長濱", "type": "文化", "feature": "建築", "fee": "免門票", "desc": "阿美族部落裡的諾亞方舟，具歷史意義。"},
    {"name": "八仙洞遺址", "region": "北長濱", "type": "自然", "feature": "海蝕洞", "fee": "停車費", "desc": "舊石器時代長濱文化發源地，壯觀海蝕洞群。"},
    {"name": "齒草橋休息區", "region": "北長濱", "type": "觀景", "feature": "海景", "fee": "免門票", "desc": "台11線上最美發呆亭，無敵海景第一排。"},
    
    # --- 中長濱 (部落文化與無菜單) ---
    {"name": "長光部落 (金剛大道)", "region": "中長濱", "type": "景觀", "feature": "梯田/單車", "fee": "免門票", "desc": "山海一線的無電線桿大道，梯田四季變化絕美。"},
    {"name": "真柄部落", "region": "中長濱", "type": "部落", "feature": "無菜單料理", "fee": "需預約", "desc": "尋找隱藏版阿美族無菜單料理，體驗山海餽贈。"},
    {"name": "吳若石神父腳底按摩", "region": "中長濱", "type": "舒壓", "feature": "教堂", "fee": "依療程", "desc": "長濱天主堂內，純正腳底按摩發源地，需預約。"},
    {"name": "長濱老街 (巨大書香)", "region": "中長濱", "type": "採買", "feature": "文青/小吃", "fee": "消費", "desc": "逛逛獨立書店「書粥」，品嚐在地小吃。"},

    # --- 南長濱 (漁港與秘境咖啡) ---
    {"name": "烏石鼻漁港", "region": "南長濱", "type": "海鮮", "feature": "黑石/海產", "fee": "免門票", "desc": "火山岩地質，全台最美小漁港，推薦品嚐海鮮。"},
    {"name": "星龍之門", "region": "南長濱", "type": "美食", "feature": "景觀咖啡", "fee": "低消", "desc": "台11線上的天空之鏡，喝咖啡俯瞰太平洋。"},
    {"name": "南竹湖部落", "region": "南長濱", "type": "部落", "feature": "白螃蟹", "fee": "免門票", "desc": "以白螃蟹聞名的阿美族部落，豐富的手作體驗。"},
    {"name": "寧埔休憩區", "region": "南長濱", "type": "觀景", "feature": "踏浪", "fee": "免門票", "desc": "擁有美麗沙灘，適合日落時分漫步。"}
]

hotels_db = [
    {"name": "畫日風尚 Sinasera Resort", "region": "南長濱", "tag": "頂級奢華", "price": 8000, "desc": "附設南法風頂級法式餐廳 Sinasera 24。"},
    {"name": "陽光佈居", "region": "中長濱", "tag": "身心靈", "price": 4000, "desc": "半山腰上的清幽秘境，無敵海景與管家手作早餐。"},
    {"name": "聽風說故事", "region": "北長濱", "tag": "海景", "price": 3500, "desc": "每個房間都能聽海浪入睡的質感民宿。"},
    {"name": "跑者之家", "region": "中長濱", "tag": "溫馨", "price": 2500, "desc": "長光部落內，老闆熱情，適合熱血獨旅與跑者。"},
    {"name": "默憩民宿", "region": "南長濱", "tag": "質感", "price": 3200, "desc": "靜謐舒適，離烏石鼻很近。"},
    {"name": "微風之谷露營區", "region": "北長濱", "tag": "露營", "price": 1200, "desc": "星空下的草地露營，設施完善。"}
]

# ==========================================
# 4. 邏輯核心：動態行程生成演算法 (資源整合路由)
# ==========================================
def generate_dynamic_itinerary(travel_date, days_str, group):
    # 分區篩選
    north_spots = [s for s in all_spots_db if s['region'] == "北長濱"]
    mid_spots = [s for s in all_spots_db if s['region'] == "中長濱"]
    south_spots = [s for s in all_spots_db if s['region'] == "南長濱"]
    
    if "一日" in days_str: day_count = 1
    elif "二日" in days_str: day_count = 2
    else: day_count = 3
    
    itinerary = {}
    
    # --- Day 1: 經典必訪 (金剛大道 & 長濱老街) ---
    d1_spot1 = next((s for s in mid_spots if s['name'] == "長光部落 (金剛大道)"), mid_spots[0])
    d1_spot2 = next((s for s in mid_spots if "老街" in s['name']), mid_spots[1])
    itinerary[1] = [d1_spot1, d1_spot2]
    
    # --- Day 2: 深入北岸或南岸探索 ---
    if day_count >= 2:
        if group in ["長輩同行", "親子家庭"]:
            # 輕鬆好走的北段：八仙洞、船型教堂
            d2_spot1 = next((s for s in north_spots if "八仙洞" in s['name']), north_spots[0])
            d2_spot2 = next((s for s in north_spots if "教堂" in s['name']), north_spots[1])
        else:
            # 追求網美與海鮮的南段：烏石鼻、星龍之門
            d2_spot1 = next((s for s in south_spots if "星龍之門" in s['name']), south_spots[0])
            d2_spot2 = next((s for s in south_spots if "烏石鼻" in s['name']), south_spots[1])
        itinerary[2] = [d2_spot1, d2_spot2]

    # --- Day 3: 部落體驗與身心靈放鬆 ---
    if day_count == 3:
        d3_spot1 = next((s for s in mid_spots if "按摩" in s['name']), mid_spots[2])
        d3_spot2 = next((s for s in south_spots if "南竹湖" in s['name']), south_spots[2])
        itinerary[3] = [d3_spot1, d3_spot2]

    status_title = "🌊 擁抱太平洋的風：長濱慢遊提案"
    return status_title, itinerary

# ==========================================
# 5. 頁面內容
# ==========================================
st.markdown("""
    <div class="header-box">
        <div class="header-title">🌾 2026 長濱鄉部落深度遊</div>
        <div class="header-subtitle">在地部落村長 邀請您感受山海的呼吸 🌊</div>
    </div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        travel_date = st.date_input("📅 出發日期 (必填)", value=date(2026, 7, 15))
    with col2:
        days_str = st.selectbox("🕒 行程天數", ["一日遊 (快閃)", "二日遊 (過夜)", "三日遊 (深度)"])
        group = st.selectbox("👥 出遊夥伴", ["情侶/夫妻", "親子家庭", "長輩同行", "熱血獨旅"])
    
    if st.button("🚀 生成部落村長推薦行程"):
        st.session_state['generated'] = True
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.get('generated'):
    status_title, itinerary = generate_dynamic_itinerary(travel_date, days_str, group)
    
    st.markdown(f"""
    <div class="info-box">
        <h4>{status_title}</h4>
        <p>為您規劃 <b>{travel_date.strftime('%Y/%m/%d')}</b> 出發的 <b>{group}</b> 專屬行程！</p>
    </div>
    """, unsafe_allow_html=True)

    # --- 顯示行程 ---
    for day, spots in itinerary.items():
        st.markdown(f'<div class="day-header">Day {day}</div>', unsafe_allow_html=True)
        
        for i, spot in enumerate(spots):
            time_label = "☀️ 上午" if i == 0 else "🌤️ 下午"
            
            tags_html = f'<span class="spot-tag">{spot["type"]}</span>'
            tags_html += f'<span class="spot-tag">{spot["feature"]}</span>'
            if "部落" in spot['type']: tags_html += '<span class="spot-tag" style="background:#E9DAC1;color:#8B4513!important;">阿美族部落</span>'
            
            st.markdown(f"""
            <div class="timeline-item">
                <div class="spot-title">{time_label}：{spot['name']}</div>
                <div style="margin: 5px 0;">{tags_html}</div>
                <div style="font-size: 14px; color: #555;">
                    💰 {spot['fee']} <br>
                    📝 {spot['desc']}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # --- 住宿推薦 (僅多日遊顯示) ---
    if "一日" not in days_str:
        st.markdown("### 🛖 部落精選住宿")
        
        # 依照選擇族群給予不同推播邏輯
        if group == "頂級享受":
            rec_hotels = [h for h in hotels_db if "奢華" in h['tag']]
        else:
            rec_hotels = hotels_db
            
        for h in random.sample(rec_hotels, min(3, len(rec_hotels))):
            st.markdown(f"""
            <div class="hotel-card">
                <div style="font-weight:bold; color:#005A9C;">{h['name']} <span class="hotel-tag">{h['tag']}</span></div>
                <div style="font-size:13px; color:#666; margin-top:3px;">
                    💲 {h['price']}起 | {h['desc']}
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- 頁尾景點總覽 ---
with st.expander("📖 查看 2026 長濱鄉全域景點名錄"):
    st.markdown("#### 山海景點總覽")
    for region in ["北長濱", "中長濱", "南長濱"]:
        st.markdown(f"**【{region}】**")
        region_spots = [s for s in all_spots_db if s['region'] == region]
        cols = st.columns(2)
        for i, s in enumerate(region_spots):
            with cols[i % 2]:
                st.markdown(f"""
                <div class="mini-card">
                    <b>{s['name']}</b> <span class="feature-badge">{s['feature']}</span><br>
                    <span style="color:#888; font-size:12px;">{s['desc']}</span>
                </div>
                """, unsafe_allow_html=True)
