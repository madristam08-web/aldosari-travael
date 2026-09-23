import streamlit as st
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="الدوسري للسفر", page_icon="✈️", layout="wide")

OWNER_WA = "966553769426"
IBAN = "SA388000000608010167520"
ACC = "608010167520"
NAME = "احمد سعد الدوسري"

st.markdown("""
<style>
    .search-btn>button { background: #ff2040 !important; color: white !important; border-radius: 10px; width: 100%; height: 50px; font-weight: bold; font-size: 18px; border:none; }
    .pay-bar { background: #1e1e1e; padding: 12px; border-radius: 10px; color: white; text-align: center; font-size: 18px; margin: 15px 0; border: 1px solid #333; }
    .flight-card { background: #111; border: 1px solid #333; padding: 15px; border-radius: 12px; margin-bottom: 8px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center;'>✈️ الدوسري للسفر والسياحة</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    from_city = st.selectbox("من:", ["ELQ - القصيم", "RUH - الرياض", "JED - جدة"])
with col2:
    to_city = st.selectbox("إلى:", ["CAI - القاهرة", "ELQ - القصيم", "RUH - الرياض"])
with col3:
    date = st.date_input("التاريخ:", datetime.now())

st.markdown('<div class="search-btn">', unsafe_allow_html=True)
st.button("بحث")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""<div class="pay-bar">💳 مدى | VISA | Mastercard | Apple Pay | stc pay | tabby | الراجحي</div>""", unsafe_allow_html=True)

flights = [
    {"no": "SV 929", "time": "0841 23-09-2026", "route": "CAI - القاهرة قادمة ELQ - اقتصادي بدون شنط | القصيم"},
    {"no": "SV 121", "time": "1154 23-09-2026", "route": "CAI - القاهرة قادمة ELQ - اقتصادي مع شنطة | القصيم"},
    {"no": "SV 792", "time": "1454 23-09-2026", "route": "CAI - القاهرة قادمة ELQ - رجال اعمال | القصيم"},
]

for f in flights:
    st.markdown(f"<div class='flight-card'><p style='color:#aaa; margin:0;'>ر.س | {f['time']} | {f['route']} | {f['no']}</p></div>", unsafe_allow_html=True)
    if st.button(f"احجز الآن", key=f['no']):
        st.session_state['selected_flight'] = f"{f['no']} - {f['route']}"

if 'selected_flight' in st.session_state:
    st.markdown("---")
    st.subheader(f"📝 حجز: {st.session_state['selected_flight']}")
    with st.form("booking_form"):
        customer_name = st.text_input("الاسم الكامل *")
        customer_phone = st.text_input("رقم الجوال واتساب *")
        st.info(f"🏦 مصرف الراجحي\nالاسم: {NAME}\nالحساب: {ACC}\nالآيبان: {IBAN}")
        receipt = st.file_uploader("ارفع صورة إيصال التحويل (إجباري) *", type=["jpg","jpeg","png","pdf"])
        submit = st.form_submit_button("✈️ إرسال الحجز")
    if submit:
        if not customer_name or not customer_phone or not receipt:
            st.error("⚠️ عبي كل البيانات وارفع الايصال")
        else:
            booking_id = f"AHM-{datetime.now().strftime('%H%M%S')}"
            msg = f"✈️ حجز جديد\n🔖 {booking_id}\n✈️ {st.session_state['selected_flight']}\n👤 {customer_name}\n📱 {customer_phone}\n🧾 {receipt.name}"
            wa_link = f"https://wa.me/{OWNER_WA}?text={urllib.parse.quote(msg)}"
            st.balloons()
            st.success(f"✅ تم الحجز {booking_id}")
            st.link_button("📤 إرسال الحجز لواتسابك", wa_link)
