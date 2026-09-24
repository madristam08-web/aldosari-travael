import streamlit as st
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="الدوسري للسفر والسياحة", page_icon="✈️", layout="wide")

# --- Secrets ---
try:
    IBAN = st.secrets["IBAN"]
    ACC = st.secrets["ACC"]
    OWNER_WA = st.secrets["WA"]
except:
    IBAN="SA3880r000006038010167520"
    ACC="608010124r67520"
    OWNER_WA="934664569426"

NAME="احمد سعد الدوسري"
ADMIN_PASS="Dossary123"

ALL_CITIES=["RUH - الرياض","JED - جدة","DMM - الدمام","ELQ - القصيم","MED - المدينة","AHB - أبها","TIF - الطائف","URY - القريات","GIZ - جازان","EAM - نجران","HAS - حائل","AJF - الجوف","TUU - تبوك","BHH - الباحة","DXB - دبي","AUH - أبوظبي","KWI - الكويت","DOH - الدوحة","BAH - المنامة","MCT - مسقط","CAI - القاهرة","AMM - عمّان","BEY - بيروت","IST - إسطنبول","LON - لندن","PAR - باريس","ROM - روما","MAD - مدريد","NYC - نيويورك","TYO - طوكيو","KUL - كوالالمبور","BKK - بانكوك","SIN - سنغافورة"]
ALL_CITIES=sorted(set(ALL_CITIES))

# --- تصميم فخم وانيق ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;800&display=swap');
* {font-family: 'Tajawal', sans-serif!important;}
.stApp {
    background: radial-gradient(1200px at 20% 0%, #1a2a4a 0%, #0a0f1e 50%, #070a14 100%);
    color:white
}
.header {
    background: linear-gradient(135deg, #0f1c35 0%, #1e3a5f 100%);
    padding: 28px 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    text-align: center;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    margin-bottom: 25px
}
.header h1 {font-weight: 800; font-size: 32px; margin:0; letter-spacing: 0.5px}
.header p {opacity:0.8; margin:8px 0 0 0; font-size:16px}
.search-box {
    background: rgba(255,255,255,0.97);
    padding: 24px;
    border-radius: 20px;
    color: #111;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.2)
}
.pay-bar {
    background: linear-gradient(90deg, #111827, #1f2937);
    padding: 14px;
    border-radius: 14px;
    text-align: center;
    border: 1px solid #2a3441;
    margin: 20px 0;
    font-size: 14px;
    letter-spacing: 1px
}
.flight-card {
    background: linear-gradient(135deg, #121826 0%, #1a2338 100%);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 14px;
    transition: all 0.3s;
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    position: relative;
    overflow: hidden
}
.flight-card:hover {
    transform: translateY(-3px);
    border-color: #2dd4bf;
    box-shadow: 0 12px 35px rgba(45,212,191,0.15)
}
.flight-card::before {
    content: '';
    position: absolute;
    top:0; right:0; width:4px; height:100%;
    background: linear-gradient(#2dd4bf, #3b82f6);
}
.price {color:#2dd4bf; font-size:22px; font-weight:800}
.badge {
    background: rgba(45,212,191,0.15);
    color: #2dd4bf;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 12px;
    border: 1px solid rgba(45,212,191,0.3)
}
.stButton>button {
    background: linear-gradient(90deg, #2dd4bf, #3b82f6)!important;
    color: white!important;
    border: none!important;
    border-radius: 12px!important;
    padding: 10px 22px!important;
    font-weight: 700!important;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# --- لوحة الادارة ---
with st.sidebar:
    st.markdown("### 🔐 إدارة الحجوزات")
    pw=st.text_input("كلمة سر الإدارة",type="password", placeholder="••••••")
    is_admin = pw==ADMIN_PASS

if is_admin:
    st.markdown('<div class="header"><h1>🔧 لوحة تحكم الدوسري</h1><p>تأكيد الحجوزات بعد مطابقة كشف الراجحي</p></div>', unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        bid=st.text_input("رقم الحجز")
        cust_phone=st.text_input("جوال العميل 5xxxxxxxx")
    with c2:
        cust_name=st.text_input("اسم العميل")
        flight_no=st.text_input("رقم الرحلة")
    if st.button("✅ تأكيد وإرسال واتساب للعميل"):
        if cust_phone and bid:
            msg=f"مرحبا {cust_name} ✈️\nتم تأكيد حجزك في الدوسري للسفر والسياحة ✅\nرقم الحجز: {bid}\nالرحلة: {flight_no}\nشكرا لثقتك بنا 🌟"
            link=f"https://wa.me/966{cust_phone.lstrip('0')}?text={urllib.parse.quote(msg)}"
            st.balloons()
            st.link_button(f"📤 ارسل تأكيد للعميل {cust_phone}",link)
        else:
            st.error("عبي البيانات صخ")
    st.stop()

# --- الهيدر الفخم ---
st.markdown(f"""
<div class="header">
    <h1>✈️ شركة أحمد الدوسري للسفر والسياحة</h1>
    <p>AHMED AL-DOSARI TRAVEL & TOURISM • رحلات داخلية ودولية بأفضل الأسعار</p>
    <p style="font-size:13px; opacity:0.6; margin-top:10px">📞 {OWNER_WA} | القصيم - بريدة</p>
</div>
""", unsafe_allow_html=True)

# --- صندوق البحث ---
with st.container():
    st.markdown('<div class="search-box">', unsafe_allow_html=True)
    c1,c2,c3,c4=st.columns([2,2,1.5,1])
    with c1: from_city=st.selectbox("🛫 من:",ALL_CITIES)
    with c2: to_city=st.selectbox("🛬 إلى:",ALL_CITIES,index=3)
    with c3: date=st.date_input("📅 التاريخ:")
    with c4:
        st.markdown("<div style='margin-top:28px'></div>", unsafe_allow_html=True)
        search=st.button("🔍 بحث")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="pay-bar">💳 مدى &nbsp; | &nbsp; VISA &nbsp; | &nbsp; Mastercard &nbsp; | &nbsp; Apple Pay &nbsp; | &nbsp; stc pay &nbsp; | &nbsp; tabby &nbsp; | &nbsp; تمارا &nbsp; | &nbsp; تحويل بنكي</div>',unsafe_allow_html=True)

# --- الرحلات ---
flights=[
    {"no":"SV 929","d":f"{from_city.split('-')[0]} → {to_city.split('-')[0]}","time":"06:25 - 08:10","price":"329","class":"اقتصادية","left":"3 مقاعد"},
    {"no":"SV 121","d":f"{from_city.split('-')[0]} → {to_city.split('-')[0]}","time":"14:30 - 16:15","price":"419","class":"اقتصادية","left":"7 مقاعد"},
    {"no":"SV 792","d":f"{from_city.split('-')[0]} → {to_city.split('-')[0]}","time":"19:45 - 21:20","price":"899","class":"أعمال","left":"مقعدين"},
]

st.markdown("### 🎫 الرحلات المتاحة")
for f in flights:
    col1,col2=st.columns([3,1])
    with col1:
        st.markdown(f"""
        <div class="flight-card">
            <div style="display:flex; justify-content:space-between; align-items:center">
                <div>
                    <b style="font-size:18px">{f['no']}</b> <span class="badge">{f['class']}</span><br>
                    <span style="opacity:0.8">{f['d']}</span> • <span style="opacity:0.6">{f['time']}</span><br>
                    <span style="color:#f59e0b; font-size:12px">⏳ {f['left']} متبقي</span>
                </div>
                <div style="text-align:left">
                    <div class="price">{f['price']} ر.س</div>
                    <div style="font-size:11px; opacity:0.5">شامل الضريبة</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button(f"احجز {f['no']}",key=f["no"]):
            st.session_state['sel']=f

if 'sel' in st.session_state:
    f=st.session_state['sel']
    st.markdown("---")
    with st.form("booking_form"):
        st.markdown(f"#### ✈️ تأكيد حجز {f['no']} - {f['d']}")
        c1,c2=st.columns(2)
        with c1: customer_name=st.text_input("الاسم الكامل مطابق للجواز *")
        with c2: customer_phone=st.text_input("رقم الجوال واتساب *")
        st.info(f"🏦 **التحويل البنكي - مصرف الراجحي**\n\nالاسم: {NAME}\nالحساب: {ACC}\nالآيبان: {IBAN}\n\nالمبلغ: {f['price']} ر.س")
        receipt=st.file_uploader("📎 ارفع صورة الإيصال إجباري *",type=["jpg","jpeg","png","pdf"])
        agree=st.checkbox("أوافق على الشروط والأحكام")
        submit=st.form_submit_button("✅ إرسال الحجز وتأكيد الدفع")

    if submit:
        if not customer_name or not customer_phone or not receipt or not agree:
            st.error("⚠️ عبي كل البيانات وارفع الإيصال ووافق على الشروط صخ")
        else:
            bid=f"AHM-{datetime.now().strftime('%d%H%M%S')}"
            st.success(f"🎉 تم استلام طلبك بنجاح! رقم حجزك: **{bid}**")
            st.warning(f"⏳ جاري مطابقة الإيصال مع كشف الراجحي - سيتم تأكيد حجزك عبر واتساب خلال 10 دقائق")
            msg=f"حجز جديد {bid}\n{f['no']} {f['d']}\nالعميل:{customer_name}\nالجوال:{customer_phone}\nالسعر:{f['price']}"
            link=f"https://wa.me/{OWNER_WA}?text={urllib.parse.quote(msg)}"
            st.link_button("📤 ارسل تفاصيل الحجز للإدارة",link)
