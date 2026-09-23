import streamlit as st
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="الدوسري للسفر", page_icon="✈️", layout="wide")

try:
    IBAN = st.secrets["IBAN"]
    ACC = st.secrets["ACC"]
    OWNER_WA = st.secrets["WA"]
except:
    IBAN="SA388000000608010167520"
    ACC="608010167520"
    OWNER_WA="966553769426"
NAME="احمد سعد الدوسري"
ADMIN_PASS="Dossary123"

ALL_CITIES=["RUH - الرياض","JED - جدة","DMM - الدمام","ELQ - القصيم","MED - المدينة","AHB - أبها","TIF - الطائف","DXB - دبي","AUH - أبوظبي","KWI - الكويت","DOH - الدوحة","CAI - القاهرة","LON - لندن","PAR - باريس","NYC - نيويورك","TYO - طوكيو","KUL - كوالالمبور","BKK - بانكوك"]
ALL_CITIES=sorted(set(ALL_CITIES))

st.markdown("""
<style>
.stApp{background:#0b0b0b; color:white}
.flight-card{background:#151515; border:1px solid #333; padding:16px; border-radius:14px; margin-bottom:12px}
.pay-bar{background:#1e1e1e; padding:12px; border-radius:12px; text-align:center; border:1px solid #444}
</style>
""",unsafe_allow_html=True)

# --- لوحة تحكم المدير ---
with st.sidebar:
    st.markdown("### 🔐 دخول الإدارة")
    pw=st.text_input("كلمة السر",type="password")
    is_admin = pw==ADMIN_PASS

if is_admin:
    st.markdown("<h1 style='text-align:center'>🔧 لوحة تأكيد الحجوزات</h1>",unsafe_allow_html=True)
    st.success("مرحبا احمد - هنا تأكد الحجوزات بعد ما تشيك الراجحي")
    st.markdown("---")
    bid=st.text_input("رقم الحجز مثلا AHM-123456")
    cust_phone=st.text_input("رقم جوال العميل بدون 966 مثلا 5xxxxxxxx")
    cust_name=st.text_input("اسم العميل")
    flight_no=st.text_input("رقم الرحلة")
    
    if st.button("✅ تأكيد الحجز وارسال واتساب للعميل"):
        if cust_phone and bid:
            # رسالة للعميل
            msg_customer=f"مرحبا {cust_name} ✈️\nتم تأكيد حجزك بنجاح ✅\nرقم الحجز: {bid}\nالرحلة: {flight_no}\nالدوسري للسفر يشكرك وتم الحجز\nتواصل معنا: {OWNER_WA}"
            link_customer=f"https://wa.me/966{cust_phone.lstrip('0')}?text={urllib.parse.quote(msg_customer)}"
            st.balloons()
            st.success(f"تم التأكيد - اضغط الزر لإرسال التأكيد للعميل {cust_name}")
            st.link_button(f"📤 ارسل تأكيد للعميل {cust_phone}",link_customer)
        else:
            st.error("عبي رقم الحجز وجوال العميل صخ")
    st.stop()

# --- موقع العملاء العادي ---
st.markdown("<h1 style='text-align:center'>✈️ الدوسري للسفر</h1>",unsafe_allow_html=True)

c1,c2,c3=st.columns(3)
with c1: from_city=st.selectbox("من:",ALL_CITIES)
with c2: to_city=st.selectbox("إلى:",ALL_CITIES,index=3)
with c3: date=st.date_input("التاريخ:",datetime.now())

st.markdown('<div class="pay-bar">💳 مدى | VISA | Mastercard | Apple Pay | tabby | تمارا</div>',unsafe_allow_html=True)

flights=[
    {"no":"SV 929","d":f"{to_city} ← {from_city}","price":"329 ر.س"},
    {"no":"SV 121","d":f"{to_city} ← {from_city}","price":"419 ر.س"},
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
        st.info(f"**الراجحي**\nالاسم: {NAME}\nالحساب: {ACC}\nالآيبان: {IBAN}")
        receipt=st.file_uploader("ارفع الإيصال إجباري *",type=["jpg","jpeg","png","pdf"])
        submit=st.form_submit_button("إرسال الحجز")
    
    if submit:
        if not customer_name or not customer_phone or not receipt:
            st.error("⚠️ عبي كل البيانات وارفع الإيصال صخ")
        else:
            booking_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            bid=f"AHM-{datetime.now().strftime('%H%M%S')}"
            st.warning(f"✅ تم استلام الإيصال {bid}، سيتم التأكيد بعد مطابقة كشف الراجحي خلال دقائق")
            st.info("⚠️ لن يتم تأكيد أي حجز بدون مطابقة الإيصال - انتظر رسالة واتساب للتأكيد")
            msg=f"حجز جديد {bid}\n{f['no']} {f['d']}\nالعميل:{customer_name}\nالجوال:{customer_phone}\nالوقت:{booking_time}"
            link=f"https://wa.me/{OWNER_WA}?text={urllib.parse.quote(msg)}"
            st.link_button("📤 ارسل لواتساب الإدارة",link)
