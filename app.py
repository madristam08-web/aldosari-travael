import streamlit as st
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="الدوسري للسفر", page_icon="✈️", layout="centered")

# --- شكل جميل ---
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stButton>button { background: #0068ff; color: white; border-radius: 10px; width: 100%; height: 50px; font-size: 18px; font-weight: bold; }
    .stButton>button:hover { background: #0052cc; }
    .payment-card { background: white; padding: 20px; border-radius: 15px; border: 2px solid #0068ff; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

OWNER_WA = "966553769426"
IBAN = "SA388000000608010167520"
ACC = "608010167520"
NAME = "احمد سعد الدوسري"

st.markdown("<h1 style='text-align:center; color:#0068ff;'>✈️ الدوسري للسفر والسياحة</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>حجوزات مضمونة - تأكيد فوري بعد التحويل</p>", unsafe_allow_html=True)
st.markdown("---")

with st.form("booking_form"):
    st.subheader("📝 بيانات الحجز")
    customer_name = st.text_input("الاسم الكامل *")
    customer_phone = st.text_input("رقم الجوال (واتساب) *")
    destination = st.text_input("الوجهة المطلوبة * مثال: القصيم - القاهرة")
    
    st.markdown("---")
    st.subheader("💳 طريقة الدفع")
    st.markdown(f"""
    <div class="payment-card">
        <h4 style='color:#0068ff; margin:0;'>🏦 مصرف الراجحي</h4>
        <p style='margin:8px 0;'><b>اسم الحساب:</b> {NAME}</p>
        <p style='margin:8px 0;'><b>رقم الحساب:</b> {ACC}</p>
        <p style='margin:8px 0;'><b>الآيبان:</b> {IBAN}</p>
        <p style='margin:8px 0; color:red; font-weight:bold;'>⚠️ لن يتم تأكيد الحجز بدون رفع الإيصال</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    receipt = st.file_uploader("📎 ارفع صورة إيصال التحويل (إجباري) *", type=["jpg", "jpeg", "png", "pdf"])
    
    submit = st.form_submit_button("✈️ إرسال الحجز الآن")

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

        st.balloons()
        st.success(f"✅ تم استلام طلبك {booking_id}")
        st.info("سيتم تأكيد الحجز بعد مطابقة الإيصال مع كشف حساب الراجحي")
        
        st.markdown("---")
        st.subheader(f"📋 تفاصيل الطلب {booking_id}")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"*العميل:* {customer_name}")
            st.write(f"*الجوال:* {customer_phone}")
        with col2:
            st.write(f"*الوجهة:* {destination}")
            st.write(f"*التاريخ:* {booking_time}")
        
        st.link_button(f"📲 فتح واتساب العميل {customer_phone}", wa_link_client)
        st.link_button(f"📤 إرسال الحجز لواتسابك", wa_link_owner)
