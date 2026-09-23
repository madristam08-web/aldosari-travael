import streamlit as st
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="الدوسري للسفر", page_icon="✈️", layout="wide")

# --- Secrets آمنة ---
try:
    IBAN = st.secrets["IBAN"]
    ACC = st.secrets["ACC"]
    OWNER_WA = st.secrets["WA"]
except:
    IBAN="SA388000000608010167520"
    ACC="608010167520"
    OWNER_WA="966553769426"
NAME="احمد سعد الدوسري"

ALL_CITIES=["RUH - الرياض","JED - جدة","DMM - الدمام","ELQ - القصيم","MED - المدينة","AHB - أبها","TIF - الطائف","URY - القريات","GIZ - جازان","EAM - نجران","HAS - حائل","AJF - الجوف","TUU - تبوك","BHH - الباحة","DXB - دبي","AUH - أبوظبي","KWI - الكويت","DOH - الدوحة","BAH - المنامة","MCT - مسقط","CAI - القاهرة","AMM - عمّان","BEY - بيروت","BGW - بغداد","TUN - تونس","ALG - الجزائر","RAB - الرباط","IST - إسطنبول","LON - لندن","PAR - باريس","ROM - روما","MAD - مدريد","BER - برلين","NYC - نيويورك","TYO - طوكيو","KUL - كوالالمبور","BKK - بانكوك","SIN - سنغافورة","PEK - بكين"]
ALL_CITIES=sorted(set(ALL_CITIES))

st.markdown("""
<style>
.stApp{background:#0b0b0b; color:white}
.search-box{background:white; padding:20px; border-radius:16px; color:black}
.pay-bar{background:#1e1e1e; padding:12px; border-radius:12px; text-align:center; border:1px solid #444}
.flight-card{background:#151515; border:1px solid #333; padding:16px; border-radius:14px; margin-bottom:12px}
</style>
""",unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center'>✈️ الدوسري للسفر - كل العواصم</h1>",unsafe_allow_html=True)

c1,c2,c3=st.columns(3)
with c1: from_city=st.selectbox("من:",ALL_CITIES)
with c2: to_city=st.selectbox("إلى:",ALL_CITIES,index=5)
with c3: date=st.date_input("التاريخ:",datetime.now())

st.markdown('<div class="pay-bar">💳 مدى | VISA | Mastercard | Apple Pay | stc pay | tabby | تمارا</div>',unsafe_allow_html=True)

flights=[
    {"no":"SV 929","d":f"{to_city} ← {from_city}","price":"329 ر.س"},
    {"no":"SV 121","d":f"{to_city} ← {from_city}","price":"419 ر.س"},
    {"no":"SV 792","d":f"{to_city} ← {from_city} - أعمال","price":"899 ر.س"},
]

for f in flights:
    st.markdown(f'<div class="flight-card"><b>{f["no"]}</b> - {f["d"]} <br><b style="color:#00ff88">{f["price"]}</b></div>',unsafe_allow_html=True)
    if st.button(f"احجز {f['no']}",key=f["no"]):
        st.session_state['sel']=f

if 'sel' in st.session_state:
    f=st.session_state['sel']
    with st.form("booking_form"):
        st.subheader(f"حجز {f['no']} - {f['d']}")
        customer_name=st.text_input("الاسم الكامل *")
        customer_phone=st.text_input("رقم الجوال *")
        st.info(f"*الراجحي*\n\nالاسم: {NAME}\nالحساب: {ACC}\nالآيبان: {IBAN}")
        receipt=st.file_uploader("ارفع الإيصال إجباري *",type=["jpg","jpeg","png","pdf"])
        submit=st.form_submit_button("إرسال الحجز")
    
    if submit:
        if not customer_name or not customer_phone or not receipt:
            st.error("⚠️ عبي كل البيانات وارفع الإيصال صخ")
        else:
            booking_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.warning("✅ تم استلام الإيصال، سيتم التأكيد بعد مطابقة كشف الراجحي")
            st.info("⚠️ لن يتم تأكيد أي حجز بدون مطابقة الإيصال - انتظار رسالة واتساب")
            msg=f"حجز جديد {booking_time}\n{f['no']} {f['d']}\nالعميل:{customer_name}\nالجوال:{customer_phone}"
            link=f"https://wa.me/{OWNER_WA}?text={urllib.parse.quote(msg)}"
            st.link_button("📤 ارسل واتساب",link)
