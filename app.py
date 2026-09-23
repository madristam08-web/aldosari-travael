import streamlit as st
from datetime import datetime
import urllib.parse
from fpdf import FPDF
import os

OWNER_WA = "966553769426"
IBAN = "SA388000000608010167520"
ACC = "608010167520"
NAME = "احمد سعد الدوسري"

def create_pdf_fancy(name, phone, dest, booking_id, time):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    if os.path.exists("Amiri-Regular.ttf"):
        pdf.add_font("Amiri", "", "Amiri-Regular.ttf", uni=True)
        pdf.set_font("Amiri", "", 16)
    else:
        pdf.set_font("Arial", 'B', 16)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 18, f"  AL-DOSARI TRAVEL  -  {booking_id}  ", ln=True, align='C', fill=True)
    pdf.ln(5)
    pdf.set_text_color(0,0,0)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Booking Confirmation / PENDING", ln=True, align='C')
    pdf.ln(5)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 8, f"Date: {time}", ln=True)
    pdf.cell(0, 8, f"Customer Name: {name}", ln=True)
    pdf.cell(0, 8, f"Phone: {phone}", ln=True)
    pdf.cell(0, 8, f"Destination: {dest}", ln=True)
    pdf.cell(0, 8, f"Booking ID: {booking_id}", ln=True)
    pdf.ln(5)
    pdf.set_fill_color(240,240,240)
    pdf.cell(0, 10, f"  Payment Details - Rajhi Bank  ", ln=True, fill=True)
    pdf.cell(0, 8, f"  Account Name: {NAME}", ln=True)
    pdf.cell(0, 8, f"  Account No: {ACC}", ln=True)
    pdf.cell(0, 8, f"  IBAN: {IBAN}", ln=True)
    pdf.ln(10)
    pdf.set_text_color(200,0,0)
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 8, "IMPORTANT: Booking will be confirmed after verifying payment in Rajhi app", ln=True, align='C')
    pdf.ln(15)
    pdf.set_text_color(100,100,100)
    pdf.set_font("Arial", 'I', 9)
    pdf.cell(0, 8, "Aldosari Travel - Buraydah - 0553769426", ln=True, align='C')
    return bytes(pdf.output())

st.set_page_config(page_title="الدوسري للسفر", page_icon="✈️", layout="centered")
st.title("✈️ الدوسري للسفر والسياحة")
st.markdown("---")
with st.form("booking_form"):
    customer_name = st.text_input("الاسم الكامل *")
    customer_phone = st.text_input("رقم الجوال (واتساب) *")
    destination = st.text_input("الوجهة المطلوبة * مثال: ELQ - CAI")
    receipt = st.file_uploader("ارفع صورة إيصال التحويل *", type=["jpg","jpeg","png","pdf"])
    submit = st.form_submit_button("إرسال الحجز")
if submit:
    if not all([customer_name, customer_phone, destination, receipt]):
        st.error("⚠️ عب كل البيانات")
    else:
        booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        booking_id = f"AHM-{datetime.now().strftime('%H%M%S')}"
        st.success(f"✅ تم الاستلام - رقم حجزك {booking_id}")
        st.warning("⚠️ سيتم التأكيد بعد التحقق من وصول المبلغ في الراجحي")
        pdf_data = create_pdf_fancy(customer_name, customer_phone, destination, booking_id, booking_time)
        st.download_button("🖨️ تحميل وطباعة التذكرة PDF", data=pdf_data, file_name=f"{booking_id}.pdf", mime="application/pdf", type="primary")
        msg = f"✈️ حجز جديد {booking_id}\nالعميل: {customer_name}\nالوجهة: {destination}\nجوال: {customer_phone}"
        wa_link = f"https://wa.me/{OWNER_WA}?text={urllib.parse.quote(msg)}"
        st.link_button("📤 إرسال تفاصيل الحجز لواتسابك", wa_link)
