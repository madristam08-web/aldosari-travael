import streamlit as st
from datetime import datetime

# --- إعداد الصفحة ---
st.set_page_config(page_title="الدوسري للسفر", page_icon="✈️", layout="centered")

# --- بيانات الدفع من Secrets (آمنة) ---
try:
    IBAN = st.secrets["IBAN"]
    ACC = st.secrets["ACC"]
    NAME = "احمد سعد الدوسري"
except:
    IBAN = "SA0000000000000000000000"
    ACC = "0000000000"
    NAME = "احمد سعد الدوسري"

st.title("✈️ الدوسري للسفر والسياحة")
st.markdown("---")

# --- نموذج الحجز ---
with st.form("booking_form"):
    st.subheader("بيانات الحجز")
    customer_name = st.text_input("الاسم الكامل")
    customer_phone = st.text_input("رقم الجوال")
    destination = st.text_input("الوجهة المطلوبة")
    
    st.markdown("---")
    st.subheader("💳 طريقة الدفع")
    
    payment_method = st.selectbox("اختر طريقة الدفع", ["تحويل بنكي - الراجحي"])
    
    st.info(f"""
    *البنك: مصرف الراجحي*
    *اسم الحساب: {NAME}*
    *رقم الحساب: {ACC}*
    *الآيبان: {IBAN}*
    """)
    
    receipt = st.file_uploader("ارفع صورة إيصال التحويل هنا (إجباري)", type=["jpg", "jpeg", "png", "pdf"])
    
    submit = st.form_submit_button("إرسال الحجز")

# --- بعد الضغط ---
if submit:
    if not customer_name or not customer_phone or not receipt:
        st.error("⚠️ الرجاء تعبئة كل البيانات ورفع الإيصال")
    else:
        # حفظ بيانات الحجز مع التاريخ
        booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        st.warning("✅ تم استلام الإيصال، سيتم تأكيد الحجز بعد التحقق من وصول المبلغ في حساب الراجحي خلال دقائق")
        st.info("⚠️ لن يتم تأكيد أي حجز بدون مطابقة الإيصال مع كشف حسابنا البنكي - يرجى انتظار رسالة تأكيد على الواتساب")
        
        st.markdown("---")
        st.write(f"*رقم الطلب:* {booking_time}")
        st.write(f"*العميل:* {customer_name}")
        
        st.success("سيتواصل معك فريق الدوسري قريباً على الواتساب")
