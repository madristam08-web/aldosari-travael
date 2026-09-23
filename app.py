import streamlit as st
from fpdf import FPDF
import random, string
from datetime import datetime

def create_pdf(name, phone, dest, bid, date):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(0, 10, "Aldosari Travel", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    
    map_dest = {"جدة":"Jeddah", "الرياض":"Riyadh", "دبي":"Dubai", "القاهرة":"Cairo"}
    dest_en = map_dest.get(dest, "Jeddah")
    name_en = name.encode('ascii', 'ignore').decode() or "Customer"

    pdf.cell(0, 10, f"Name: {name_en}", ln=True)
    pdf.cell(0, 10, f"Phone: {phone}", ln=True)
    pdf.cell(0, 10, f"Destination: {dest_en}", ln=True)
    pdf.cell(0, 10, f"Booking ID: {bid}", ln=True)
    pdf.cell(0, 10, f"Date: {date}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

st.title("الدوسري للسفريات")
st.write("احجز رحلتك بسهولة")

name = st.text_input("الاسم")
phone = st.text_input("رقم الجوال")
dest = st.selectbox("الوجهة", ["جدة", "الرياض", "دبي", "القاهرة"])

if st.button("تأكيد الحجز"):
    if name and phone:
        bid = "AHM-" + ''.join(random.choices(string.digits, k=6))
        t = datetime.now().strftime("%Y-%m-%d %H:%M")
        pdf_bytes = create_pdf(name, phone, dest, bid, t)
        st.success(f"تم الحجز! رقم حجزك {bid}")
        st.download_button("تحميل التذكرة PDF", pdf_bytes, file_name=f"{bid}.pdf", mime="application/pdf")
    else:
        st.error("عبي الاسم والجوال")
