import streamlit as st
from fpdf import FPDF
import datetime
import random

st.set_page_config(page_title="الدوسري للسفريات")

def create_pdf(name, phone, dest, booking_id, time_str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 15, f"AL-DOSARI TRAVEL - {booking_id}", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Date: {time_str}", ln=True)
    pdf.cell(0, 10, f"Name: {name}", ln=True)
    pdf.cell(0, 10, f"Phone: {phone}", ln=True)
    pdf.cell(0, 10, f"Destination: {dest}", ln=True)
    pdf.cell(0, 10, f"Bank: 608010167520 Al Rajhi", ln=True)
    return pdf.output()

st.title("الدوسري للسفريات")
st.markdown("احجز رحلتك بسهولة")

name = st.text_input("الاسم")
phone = st.text_input("رقم الجوال")
dest = st.selectbox("الوجهة", ["جدة", "الرياض", "مكة", "المدينة", "أبها"])

if st.button("تأكيد الحجز"):
    if name and phone:
        bid = f"AHM-{random.randint(10000,99999)}"
        t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        pdf_bytes = create_pdf(name, phone, dest, bid, t)
        st.success(f"تم الحجز! رقم الحجز: {bid}")
        st.download_button(
            label="تحميل التذكرة PDF",
            data=pdf_bytes,
            file_name=f"{bid}.pdf",
            mime="application/pdf"
        )
    else:
        st.error("عبي الاسم والجوال")
