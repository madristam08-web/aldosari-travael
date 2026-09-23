import streamlit as st, pandas as pd, requests
from datetime import date

st.set_page_config(page_title="احمد الدوسري للسفر والسياحة", layout="wide")

# هيدر
st.markdown("""
<style>
.header{
background: linear-gradient(rgba(0,0,0,.65),rgba(0,0,0,.65)), url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05');
background-size:cover; background-position:center;
padding:30px 20px; border-radius:20px; text-align:center; color:white; margin-bottom:10px;
}
.payment-box{
background:white; border:2px solid #065f46; border-radius:15px; 
padding:20px; margin:20px 0; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.ticket-card{
background:white; border-radius:15px; padding:20px; border:1px solid #e5e7eb; margin-bottom:15px;
}
</style>
<div class="header">
<img src="https://upload.wikimedia.org/wikipedia/commons/0/0d/Saudi_Arabian_Airlines_Logo.png" width="180" style="background:white; padding:10px; border-radius:10px;">
<h1 style='color:white; margin-top:15px;'>✈️ احمد الدوسري للسفر والسياحة</h1>
<p style='font-size:20px;'>نظام إدارة الحجوزات الذكي - شريك الخطوط السعودية الرسمي</p>
</div>
""", unsafe_allow_html=True)

# ===== 1- قسم البحث عن التذاكر =====
st.subheader("🔍 البحث عن تذاكر الطيران")

col1, col2, col3, col4 = st.columns(4)
with col1:
    from_city = st.selectbox("من:", ["الرياض - RUH", "جدة - JED", "الدمام - DMM", "القصيم - ELQ"])
with col2:
    to_city = st.selectbox("إلى:", ["لندن - LHR", "دبي - DXB", "القاهرة - CAI", "اسطنبول - IST"])
with col3:
    travel_date = st.date_input("تاريخ السفر:", date.today())
with col4:
    passengers = st.number_input("عدد المسافرين:", 1, 10, 1)

if st.button("✈️ بحث عن الرحلات", use_container_width=True, type="primary"):
    st.session_state['searched'] = True

# ===== 2- عرض التذاكر =====
if st.session_state.get('searched'):
    st.markdown("### 🎫 الرحلات المتاحة")
    
    flights = [
        {"flight": "SV 110", "time": "08:30 - 12:45", "price": 1250, "airline": "الخطوط السعودية"},
        {"flight": "SV 102", "time": "14:20 - 18:35", "price": 1890, "airline": "الخطوط السعودية"},
        {"flight": "SV 118", "time": "22:10 - 02:30", "price": 1450, "airline": "الخطوط السعودية"},
    ]
    
    for f in flights:
        with st.container():
            c1, c2, c3, c4 = st.columns([2,2,1,1])
            c1.markdown(f"*{f['flight']}* - {f['airline']}\n\n🕐 {f['time']}")
            c2.markdown(f"*{from_city} → {to_city}*\n\n📅 {travel_date}")
            c3.markdown(f"### {f['price']} ر.س")
            if c4.button(f"احجز {f['flight']}", key=f['flight']):
                st.session_state['selected_flight'] = f
                st.session_state['show_payment'] = True
                st.rerun()

# ===== 3- قسم وسائل الدفع (يظهر بعد اختيار رحلة) =====
if st.session_state.get('show_payment'):
    f = st.session_state['selected_flight']
    st.divider()
    st.markdown(f"<div class='payment-box'>", unsafe_allow_html=True)
    st.subheader(f"💳 إتمام حجز الرحلة {f['flight']} - {f['price']} ر.س")
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1: st.markdown("<div style='text-align:center; border:1px solid #ddd; border-radius:10px; padding:10px;'><b>💚 مدى</b></div>", unsafe_allow_html=True)
    with col2: st.markdown("<div style='text-align:center; border:1px solid #ddd; border-radius:10px; padding:10px;'><b>Visa</b></div>", unsafe_allow_html=True)
    with col3: st.markdown("<div style='text-align:center; border:1px solid #ddd; border-radius:10px; padding:10px;'><b>Mastercard</b></div>", unsafe_allow_html=True)
    with col4: st.markdown("<div style='text-align:center; border:1px solid #ddd; border-radius:10px; padding:10px;'><b> Apple Pay</b></div>", unsafe_allow_html=True)
    with col5: st.markdown("<div style='text-align:center; border:1px solid #ddd; border-radius:10px; padding:10px;'><b>STC Pay</b></div>", unsafe_allow_html=True)
    with col6: st.markdown("<div style='text-align:center; border:1px solid #ddd; border-radius:10px; padding:10px;'><b>Tabby</b></div>", unsafe_allow_html=True)
    
    payment_method = st.selectbox("اختر وسيلة الدفع:", ["مدى - Mada", "Visa", "Mastercard", "Apple Pay", "STC Pay", "Tabby", "تحويل بنكي - الراجحي"])
    
    if payment_method == "تحويل بنكي - الراجحي":
        st.info("🏦 الراجحي - احمد الدوسري للسفر - SA00 0000 0000")
    
    if st.button("💚 تأكيد الدفع والحجز", use_container_width=True, type="primary"):
        st.balloons()
        st.success(f"✅ تم حجز {f['flight']} بنجاح! بـ {payment_method} - التذكرة بترسل واتساب")
    
    st.markdown("</div>", unsafe_allow_html=True)
