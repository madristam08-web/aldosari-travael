import streamlit as st

st.set_page_config(page_title="بريق للسفر | Bareeq Travel", page_icon="✈️", layout="wide")

# --- CSS فخم ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
* {font-family:'Tajawal', sans-serif !important;}
.stApp {background: radial-gradient(circle at top, #1a1a1a 0%, #000000 60%) !important;}
.hero {
  background: linear-gradient(135deg, #0f0f0f 0%, #1c1c1c 100%);
  border: 1px solid #2a2a2a; border-radius: 24px; padding: 40px 20px; text-align:center;
  box-shadow: 0 10px 40px rgba(255,215,0,0.08);
}
.hero h1 {font-size:42px; font-weight:900; color:white; margin:0;}
.hero p {color:#FFD700; font-size:18px; margin-top:8px; font-weight:700;}
.badge {background:#FFD700; color:black; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:900; display:inline-block; margin-bottom:10px;}
.card {
  background: linear-gradient(180deg, #171717 0%, #101010 100%);
  border:1px solid #262626; border-radius:20px; padding:20px; height:100%;
  transition:0.3s; position:relative; overflow:hidden;
}
.card:hover {border-color:#FFD700; transform:translateY(-5px); box-shadow:0 12px 30px rgba(255,215,0,0.15);}
.flag {font-size:32px; text-align:center; margin-bottom:8px;}
.country {color:white; font-weight:900; font-size:22px; text-align:center; margin:5px 0;}
.price-row {background:#1e1e1e; border-radius:12px; padding:12px 14px; margin:8px 0; display:flex; justify-content:space-between; align-items:center;}
.price-row span:first-child {color:#aaa; font-size:13px;}
.price {color:#FFD700; font-weight:900; font-size:18px;}
.stButton>button {background: linear-gradient(90deg, #FFD700, #ffb700) !important; color:black !important; border:0 !important; font-weight:900 !important; border-radius:12px !important; height:46px;}
.footer {text-align:center; color:#555; padding:30px 0 10px; font-size:13px; border-top:1px solid #1a1a1a; margin-top:30px;}
</style>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
<div class="hero">
  <div class="badge">✈️ وكالة معتمدة - موافقات مصر EG</div>
  <h1>وكالة بريق للسفر والسياحة</h1>
  <p>📢 أسرع موافقات أمنية لمصر - أسعارنا بالدرهم الإماراتي - إنجاز خلال 48 ساعة</p>
</div>
<br>
""", unsafe_allow_html=True)

# --- البيانات ---
DATA = {
    "🇸🇩 السوداني": [("شهر - طيران ✈️",276,True), ("3 أشهر - طيران",367,False), ("3 أشهر - براً 🚗",542,False)],
    "🇹🇩 التشادي": [("شهر - جواً",352,False)],
    "🇱🇾 الليبي": [("شهر - جواً",295,False)],
    "🇪🇹 الإثيوبي": [("شهر - جواً",352,False)],
    "🇪🇷 الإريتري": [("شهر - جواً",352,False)],
    "🇾🇪 اليمني": [("شهر - جواً",333,False), ("3 أشهر - جواً",333,False)],
    "🇲🇦 المغربي": [("شهر - جواً",352,False)],
    "🇺🇬 الأوغندي": [("شهر - جواً",333,False)],
    "🇳🇵 النيبالي": [("شهر - جواً",333,False)],
}

# --- الشبكة ---
cols = st.columns(3)
for idx, (country, items) in enumerate(DATA.items()):
    with cols[idx % 3]:
        is_popular = any(len(it)>2 and it[2] for it in items)
        badge_html = "<div style='text-align:center'><span style='background:#FFD700;color:black;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:900'>🔥 الأكثر طلباً</span></div>" if "السوداني" in country else ""
        
        st.markdown(f"<div class='card'>{badge_html}<div class='flag'>{country.split()[0]}</div><div class='country'>{country}</div>", unsafe_allow_html=True)
        
        for label, price, _ in items:
            st.markdown(f"<div class='price-row'><span>{label}</span><span class='price'>{price} درهم</span></div>", unsafe_allow_html=True)
        
        wa_text = f"مرحبا وكالة بريق، اريد موافقة مصر {country}"
        st.link_button(f"احجز الآن عبر واتساب 📲", f"https://wa.me/971501234567?text={wa_text}", use_container_width=True)
        st.markdown("</div><br>", unsafe_allow_html=True)

st.markdown("<div class='footer'>© 2026 Bareeq Travel - بريق للسفر والسياحة | جميع الموافقات رسمية ومضمونة<br>للتواصل: واتساب 971501234567+</div>", unsafe_allow_html=True)
