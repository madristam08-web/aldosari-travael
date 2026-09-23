import streamlit as st
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="الدوسري للسفر", page_icon="✈️", layout="centered")

OWNER_WA = "966553769426"
IBAN = "SA388000000608010167520"
ACC = "608010167520"
NAME = "احمد سعد الدوسري"

st.title("✈️ الدوسري للسفر والسياحة")
st.markdown("---")

with st.form("booking_form"):
    st.subheader("بيانات الحجز")
    customer_name = st.text_input("الاسم الكامل *")
    customer_phone = st.text_input("رقم الجوال (واتساب) * مثال: 0553769426")
    destination = st.text_input("الوجهة المطلوبة * مثال: القصيم - القاهرة")
    
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
        booking_id = f"AHM-{datetime.now().strftime('%H%M%S')}"
        
        msg_for_owner = f"""✈️ حجز جديد - الدوسري للسفر

📅 التاريخ: {booking_time}
🔖 رقم الحجز: {booking_id}
👤 العميل: {customer_name}
📱 جوال العميل: {customer_phone}
🌍 الوجهة: {destination}
🧾 الإيصال: {receipt.name}
"""
        
        encoded_msg = urllib.parse.quote(msg_for_owner)
        wa_link_owner = f"https://wa.me/{OWNER_WA}?text={encoded_msg}"
        
        clean_phone = customer_phone.strip().replace(" ", "")
        if clean_phone.startswith("0"):
            clean_phone = "966" + clean_phone[1:]
        if not clean_phone.startswith("966"):
            clean_phone = "966" + clean_phone.lstrip("0")
        wa_link_client = f"https://wa.me/{clean_phone}"

        st.success(f"✅ تم استلام طلبك {booking_id}")
        st.warning("سيتم تأكيد الحجز بعد التحقق من المبلغ")
        
        st.markdown("---")
        st.subheader(f"📋 تفاصيل الطلب {booking_id}")
        st.write(f"*العميل:* {customer_name}")
        st.write(f"*الجوال:* {customer_phone}")
        st.write(f"*الوجهة:* {destination}")
        
        st.link_button(f"📲 فتح واتساب العميل", wa_link_client)
        st.link_button(f"📤 إرسال الحجز لواتسابك انت", wa_link_owner)
