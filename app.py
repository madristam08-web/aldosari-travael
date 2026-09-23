import streamlit as st
from datetime import date

st.set_page_config(page_title="احمد الدوسري للسفر والسياحة", layout="wide", initial_sidebar_state="collapsed")

# حل مشكلة الوضع الليلي + تصميم فخم
st.markdown("""
<style>
/* اجبار الخلفية بيضاء والكلام اسود */
.stApp { background-color: #f5f7fa !important; }
.header{
background: linear-gradient(135deg, #065f46 0%, #10b981 100%);
padding:35px 20px; border-radius:20px; text-align:center; color:white !important; margin-bottom:20px;
box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}
.ticket-card{
background: white !important; border-radius:15px; padding:20px; 
border-left: 5px solid #065f46;
box-shadow: 0 4px 15px rgba(0,0,0,0.08); margin-bottom:15px;
color: #111 !important;
}
.payment-section{
background: white !important; border:2px solid #065f46; border-radius:20px; 
padding:25px; margin-top:25px; box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.pay-icon{
background: #f9fafb; border:1px solid #e5e7eb; border-radius:12px;
padding:15px 5px; text-align:center; font-weight:bold; color:#111 !important;
}
h2, h3, p, label, span { color: #111 !important; }
</style>
<div class="header">
<h1 style='color:white !important; margin:0;'>✈️ احمد الدوسري للسفر والسياحة</h1>
<p style='color:white !important; font-size:18px; margin-top:10px;'>نظام إدارة الحجوزات الذكي - شريك الخطوط السعودية الرسمي</p>
<p style='background:rgba(255,255,255,0.2); display:inline-block; padding:5px 15px; border-radius:20px; color:white !important;'>💚 لنا جوّنا - ثقة 100 ألف مسافر</p>
</div>
""", unsafe_allow_html=True)

# ===== البحث =====
st.markdown("### 🔍 البحث عن تذاكر الطيران")
c1, c2, c3, c4 = st.columns(4)
with c1: from_city = st.selectbox("من:", ["الرياض - RUH", "جدة - JED", "الدمام - DMM", "القصيم - ELQ"])
with c2: to_city = st.selectbox("إلى:", ["لندن - LHR", "دبي - DXB", "القاهرة - CAI", "اسطنبول - IST"])
with c3: travel_date = st.date_input("تاريخ السفر:", date.today())
with c4: passengers = st.number_input("المسافرين:", 1, 10, 1)

if st.button("✈️ بحث عن الرحلات المتاحة الآن", use_container_width=True, type="primary"):
    st.session_state['searched'] = True

# ===== عرض التذاكر =====
if st.session_state.get('searched'):
    st.markdown("### 🎫 أفضل 3 رحلات لك")
    flights = [
        {"flight": "SV 110", "time": "08:30 - 12:45", "price": 1250, "duration": "4h 15m"},
        {"flight": "SV 102", "time": "14:20 - 18:35", "price": 1890, "duration": "4h 15m"},
        {"flight": "SV 118", "time": "22:10 - 02:30", "price": 1450, "duration": "4h 20m"},
    ]
    for f in flights:
        st.markdown(f"<div class='ticket-card'>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([2,2,1,1])
        col1.markdown(f"*✈️ {f['flight']}*\n\n🕐 {f['time']}\n\n⏱️ {f['duration']}")
        col2.markdown(f"*{from_city} → {to_city}*\n\n📅 {travel_date}\n\n💺 مباشر")
        col3.markdown(f"<h2 style='color:#065f46 !important;'>{f['price']} ر.س</h2>", unsafe_allow_html=True)
        if col4.button(f"احجز الآن", key=f['flight'], type="primary", use_container_width=True):
            st.session_state['selected_flight'] = f
            st.session_state['show_payment'] = True
        st.markdown("</div>", unsafe_allow_html=True)

    # ===== وسائل الدفع - تظهر دائماً بعد البحث =====
    st.markdown("<div class='payment-section'>", unsafe_allow_html=True)
    st.markdown("### 💳 وسائل الدفع الآمنة - ادفع بأمان 100%")
    
    p1,p2,p3,p4,p5,p6 = st.columns(6)
    p1.markdown("<div class='pay-icon'>💚<br>مدى</div>", unsafe_allow_html=True)
    p2.markdown("<div class='pay-icon'>💳<br>Visa</div>", unsafe_allow_html=True)
    p3.markdown("<div class='pay-icon'>💳<br>Mastercard</div>", unsafe_allow_html=True)
    p4.markdown("<div class='pay-icon'><br>Apple Pay</div>", unsafe_allow_html=True)
    p5.markdown("<div class='pay-icon'>📱<br>STC Pay</div>", unsafe_allow_html=True)
    p6.markdown("<div class='pay-icon'>🟣<br>Tabby</div>", unsafe_allow_html=True)
    
    st.write("")
    pay = st.selectbox("اختر طريقة الدفع:", ["مدى - Mada", "Visa", "Mastercard", "Apple Pay", "STC Pay", "Tabby - قسطها على 4", "تحويل بنكي - الراجحي"])
    
    if pay == "تحويل بنكي - الراجحي":
        st.warning("🏦 مصرف الراجحي - الآيبان: SA6080000 - باسم: احمد الدوسري للسفر")
    
    if st.button("💚 تأكيد الحجز والدفع الآن", use_container_width=True, type="primary"):
        st.balloons()
        st.success("✅ تم الحجز بنجاح! تذكرتك بتنرسل واتساب خلال دقائق ✈️")
    st.markdown("</div>", unsafe_allow_html=True)
