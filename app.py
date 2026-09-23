import streamlit as st
from datetime import datetime
import urllib.parse

# --- إعداد الصفحة ---
st.set_page_config(page_title="الدوسري للسفر", page_icon="✈️", layout="centered")

# --- بياناتك الثابتة ---
OWNER_WA = "966553769426" # رقمك انت
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

with st.form("booking_form"):
    st.subheader("بيانات الحجز")
    customer_name = st.text_input("الاسم الكامل *")
    customer_phone = st.text_input("رقم الجوال (واتساب) * مثال: 0553769426")
    destination = st.text_input("الوجهة المطلوبة *")
    
    st.markdown("---")
    st.subheader("💳 طريقة الدفع")
    st.info(f"""
    *البنك: مصرف الراجحي*
    *اسم الحساب: {NAME}*
    *رقم الحساب: {ACC}*
    *الآيبان: {IBAN}*
    """)
    
    receipt = st.file_uploader("ارفع صورة إيصال التحويل هنا (إجباري) *", type=["jpg", "jpeg", "png", "pdf"])
    
    submit = st.form_submit_button("إرسال الحجز")

if submit:
    if not customer_name or not customer_phone or not destination or not receipt:
        st.error("⚠️ الرجاء تعبئة كل البيانات ورفع الإيصال")
    else:
        booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # تجهيز رسالة واتساب لك انت
        msg_for_owner = f"حجز جديد ✈️\nالوقت: {booking_time}\nالاسم: {customer_name}\nجوال العميل: {customer_phone}\nالوجهة: {destination}\nالعميل رفع إيصال: {receipt.name}\n\n⚠️ تأكد من وصول المبلغ في الراجحي قبل التأكيد"
        encoded_msg = urllib.parse.quote(msg_for_owner)
        wa_link_owner = f"https://wa.me/{OWNER_WA}?text={encoded_msg}"
        
        # رابط واتساب العميل لك
        clean_phone = customer_phone.replace("0", "", 1) if customer_phone.startswith("0") else customer_phone
        if not clean_phone.startswith("966"):
            clean_phone = "966" + clean_phone.lstrip("0")
        wa_link_client = f"https://wa.me/{clean_phone}"

        st.warning("✅ تم استلام الإيصال، سيتم تأكيد الحجز بعد التحقق من وصول المبلغ في حساب الراجحي خلال دقائق")
        st.info("⚠️ لن يتم تأكيد أي حجز بدون مطابقة الإيصال مع كشف حسابنا - يرجى انتظار رسالة تأكيد على الواتساب")
        
        st.markdown("---")
        st.subheader("📋 تفاصيل الطلب (للمسؤول فقط)")
        st.write(f"*رقم الطلب:* {booking_time}")
        st.write(f"*العميل:* {customer_name}")
        st.write(f"*جوال العميل:* {customer_phone}")
        
        st.link_button(f"📲 فتح واتساب العميل {customer_phone}", wa_link_client)
        st.link_button(f"📤 إرسال تفاصيل الحجز لواتسابك انت ({OWNER_WA})", wa_link_owner)
        
        st.success("اضغط الزر الأخير عشان توصلك بيانات العميل على واتسابك وتحفظ رقمه صخ")
