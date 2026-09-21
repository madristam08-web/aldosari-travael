["الرياض", "جدة", "دبي", "القاهرة", "لندن", "اسطنبول"])
    travel_date = st.date_input("تاريخ الرحلة", value=date.today())
    price = {"الرياض":450, "جدة":600, "دبي":1200, "القاهرة":900, "لندن":2500, "اسطنبول":1800}
    st.info(f"💰 سعر التذكرة: {price[dest]} ريال")
    if st.button("تأكيد الحجز ✈️", type="primary", use_container_width=True):
        if name:
            st.session_state.bookings.append({"الاسم": name, "الوجهة": dest, "التاريخ": str(travel_date), "السعر": f"{price[dest]} ريال"})
            st.success(f"تم الحجز للعميل {name}")
            st.balloons()
        else:
            st.warning("ادخل اسم العميل")

st.write("### 📋 سجل الحجوزات")
if st.session_state.bookings:
    st.dataframe(pd.DataFrame(st.session_state.bookings), use_container_width=True)
    st.download_button("⬇️ تحميل التقرير Excel", pd.DataFrame(st.session_state.bookings).to_csv(index=False).encode('utf-8-sig'), "bookings.csv", "text/csv")
else:
    st.info("لا يوجد حجوزات حالياً")

st.markdown("---")
st.markdown("<center>© 2026 احمد الدوسري للسفر والسياحة | جميع الحقوق محفوظة ✈️🇸🇦</center>", unsafe_allow_html=True)
