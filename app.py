import streamlit as st
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="الدوسري للسفر", page_icon="✈️", layout="wide")

OWNER_WA = "966553769426"
IBAN = "SA388000000608010167520"
ACC = "608010167520"
NAME = "احمد سعد الدوسري"

ALL_CITIES = [
    "ELQ - القصيم", "RUH - الرياض", "JED - جدة", "DMM - الدمام", 
    "MED - المدينة", "AHB - أبها", "TIF - الطائف", "URY - القريات",
    "CAI - القاهرة", "DXB - دبي", "KWI - الكويت"
]

st.markdown("""
<style>
    .search-btn>button { background: #ff2040 !important; color: white !important; border-radius: 12px; width: 100%; height: 55px; font-weight: bold; font-size: 19px; border:none; }
    .pay-bar { background: linear-gradient(90deg, #1e1e1e, #2a2a2a); padding: 15px; border-radius: 12px; color: white; text-align: center; font-size: 16px; margin: 20px 0; border: 1px solid #444; letter-spacing: 0.5px; }
    .flight-card { background: #121212; border: 1px solid #333; padding: 16px; border-radius: 14px; margin-bottom: 12px; }
    .stApp { background: #0a0a0a; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center; color:white;'>✈️ الدوسري للسفر والسياحة</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    from_city = st.selectbox("من:", ALL_CITIES, index=1)
with col2:
    to_city = st.selectbox("إلى:", ALL_CITIES, index=0)
with col3:
    date = st.date_input("التاريخ:", datetime.now())

st.markdown('<div class="search-btn">', unsafe_allow_html=True)
st.button("بحث 🔍")
st.markdown('</div>', unsafe_allow_html=True)

# شريط الدفع الكامل
st.markdown("""
<div class="pay-bar">
💳 مدى | VISA | Mastercard | Apple Pay | stc pay | tabby | تمارا | الراجحي | الأهلي | الإنماء
</div>
""", unsafe_allow_html=True)

flights = [
    {"no": "SV 929", "time": f"{date} 08:41", "route": f"{to_city} قادمة {from_city} - اقتصادي بدون شنط"},
    {"no": "SV 121", "time": f"{date} 11:54", "route": f"{to_city} قادمة {from_city} - اقتصادي مع شنطة"},
    {"no": "SV 792", "time": f"{date} 14:54", "route": f"{to_city} قادمة {from_city} - رجال اعمال"},
    {"no": "F3 123", "time": f"{date} 18:20", "route": f"{to_city} قادمة {from_city} - اقتصادي"},
]

for f in flights:
    st.markdown(f"<div class='flight-card'><p style='color:#bbb; margin:0;'>✈️ {f['no']} | {f['time']} | {f['route']}</p></div>", unsafe_allow_html=True)
    if st.button(f"احجز الآن - {f['no']}", key=f['no']):
        st.session_state['selected_flight'] = f"{f['no']} - {f['route']}"
        st.rerun()

if 'selected_flight' in st.session_state:
    st.markdown("---")
    st.subheader(f"📝 حجز: {st.session_state['selected_flight']}")
    with st.form("booking_form"):
        customer_name = st.text_input("الاسم الكامل *")
        customer_phone = st.text_input("رقم الجوال واتساب *")
        st.info(f"🏦 مصرف الراجحي\nالاسم: {NAME}\nالحساب: {ACC}\nالآيبان: {IBAN}")
        receipt = st.file_uploader("ارفع صورة إيصال التحويل (إجباري) *", type=["jpg","jpeg","png","pdf"])
        submit = st.form_submit_button("✈️ تأكيد وإرسال الحجز")
    if submit:
        if not customer_name or not customer_phone or not receipt:
            st.error("⚠️ عبي كل البيانات وارفع الايصال صخ")
        else:
            booking_id = f"AHM-{datetime.now().strftime('%H%M%S')}"
            msg = f"✈️ حجز جديد\n🔖 {booking_id}\n✈️ {st.session_state['selected_flight']}\n👤 {customer_name}\n📱 {customer_phone}"
            wa_link = f"https://wa.me/{OWNER_WA}?text={urllib.parse.quote(msg)}"
            st.balloons()
            st.success(f"✅ تم الحجز {booking_id}")
            st.link_button("📤 إرسال لواتسابك", wa_link)
