import streamlit as st

st.set_page_config(page_title="بريق - موافقات مصر EG", page_icon="✈️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700;800;900&display=swap');
* {font-family:'Tajawal', sans-serif !important;}
.stApp {background:#000000;}
h1, h2, h3 {color:white !important; text-align:center;}
.price-box {
    background: linear-gradient(135deg, #1a1a1a 0%, #151515 100%);
    border: 1px solid #2a2a2a;
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 16px;
}
.price-box:hover {border-color: #FFD700;}
.price {color: #FFD700 !important; font-weight: 900; font-size: 20px;}
.label {color: #ccc !important;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>✈️ وكالة بريق للسفر والسياحة</h1>")
st.markdown("<h3 style='color:#FFD700 !important;'>📢 أسعار الموافقات الأمنية لمصر EG</h3><br>", unsafe_allow_html=True)

DATA = {
    "🇸🇩 السوداني": [("شهر - طيران", 276), ("3 أشهر - طيران", 367), ("3 أشهر - برياً", 542)],
    "🇹🇩 التشادي": [("شهر - جواً", 352)],
    "🇱🇾 الليبي": [("شهر - جواً", 295)],
    "🇪🇹 الإثيوبي": [("شهر - جواً", 352)],
    "🇪🇷 الإريتري": [("شهر - جواً", 352)],
    "🇾🇪 اليمني": [("شهر - جواً", 333), ("3 أشهر - جواً", 333)],
    "🇲🇦 المغربي": [("شهر - جواً", 352)],
}

cols = st.columns(3)
for idx, (country, items) in enumerate(DATA.items()):
    with cols[idx % 3]:
        st.markdown(f"<div class='price-box'><h3>{country}</h3>", unsafe_allow_html=True)
        for label, price in items:
            st.markdown(f"<div style='display:flex;justify-content:space-between;background:#222;padding:10px;border-radius:10px;margin:6px 0'><span>{label}</span><span class='price'>{price} درهم</span></div>", unsafe_allow_html=True)
        st.link_button(f"احجز {country} 📲", f"https://wa.me/971501234567?text=اريد {country}", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)