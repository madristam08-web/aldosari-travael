import streamlit as st, pandas as pd, requests
from datetime import date

st.set_page_config(page_title="احمد الدوسري للسفر والسياحة", layout="wide")

# هيدر مع الشعار الرسمي
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
.pay-method{
text-align:center; padding:15px; border:1px solid #e5e7eb; border-radius:10px;
}
.pay-method:hover{ border-color:#065f46; background:#f0fdf4; }
</style>
<div class="header">
<img src="https://upload.wikimedia.org/wikipedia/commons/0/0d/Saudi_Arabian_Airlines_Logo.png" width="180" style="background:white; padding:10px; border-radius:10px;">
<h1 style='color:white; margin-top:15px;'>✈️ احمد الدوسري للسفر والسياحة</h1>
<p style='font-size:20px;'>نظام إدارة الحجوزات الذكي - شريك الخطوط السعودية الرسمي</p>
<p style='font-size:14px; background:#065f46; display:inline-block; padding:5px 15px; border-radius:20px;'>💚 شعارنا مستوحى من السيفين والنخلة - لنا جوّنا</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:#065f46; color:white; padding:12px; border-radius:10px; font-weight:bold; text-align:center;">
✈️ SAUDIA: رحلات مباشرة جديدة الرياض - لندن | 🌤️ أجواء مثالية للسفر | 🛫 100 ألف مسافر يومياً من مطار الملك خالد
</div>
""", unsafe_allow_html=True)

# ===== قسم وسائل الدفع الجديد 💳 =====
st.markdown("<div class='payment-box'>", unsafe_allow_html=True)
st.subheader("💳 اختر وسيلة الدفع - وسائل دفع آمنة 100%")

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.markdown("<div class='pay-method'><b>💚 مدى</b><br>Mada</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='pay-method'><b>💳 Visa</b></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='pay-method'><b>💳 Mastercard</b></div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='pay-method'><b> Apple Pay</b></div>", unsafe_allow_html=True)
with col5:
    st.markdown("<div class='pay-method'><b>STC Pay</b></div>", unsafe_allow_html=True)
with col6:
    st.markdown("<div class='pay-method'><b>Tabby</b><br>قسطها</div>", unsafe_allow_html=True)

payment_method = st.selectbox("وسيلة الدفع:", ["مدى - Mada", "Visa", "Mastercard", "Apple Pay", "STC Pay", "Tabby - قسطها على 4", "تحويل بنكي - الراجحي"])

if payment_method == "تحويل بنكي - الراجحي":
    st.info("🏦 البنك: مصرف الراجحي | الاسم: احمد الدوسري للسفر والسياحة | الآيبان: SA00 0000 0000 0000 0000")
else:
    st.success(f"✅ تم اختيار: {payment_method} - دفع آمن ومشفر")

if st.button("💚 تأكيد الدفع والحجز - Confirm & Pay", use_container_width=True, type="primary"):
    st.balloons()
    st.success("✅ تم الحجز بنجاح! سيتم إرسال التذكرة على الواتساب ✈️")
    st.info(f"🧾 طريقة الدفع: {payment_method} | 📅 التاريخ: {date.today()}")

st.markdown("</div>", unsafe_allow_html=True)
# ===== نهاية قسم وسائل الدفع =====
