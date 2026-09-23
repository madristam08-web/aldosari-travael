{"no":"XY 456","t":f"{date} 22:10","d":f"{to_city} ← {from_city} - اقتصادي","price":"349 ر.س"},
]

for f in flights:
    st.markdown(f'<div class="flight-card"><b>{f["no"]}</b> | {f["t"]}<br><span style="color:#aaa">{f["d"]}</span><br><b style="color:#00ff88">{f["price"]}</b></div>',unsafe_allow_html=True)
    if st.button(f"احجز الآن - {f['no']}",key=f['no']):
        st.session_state['sel']=f

if 'sel' in st.session_state:
    st.markdown("---")
    f=st.session_state['sel']
    st.subheader(f"📝 حجز: {f['no']} - {f['d']}")
    with st.form("book"):
        name=st.text_input("الاسم الكامل *")
        phone=st.text_input("رقم الجوال واتساب *")
        st.info(f"🏦 الراجحي\nالاسم: {NAME}\nالحساب: {ACC}\nالآيبان: {IBAN}")
        rec=st.file_uploader("ارفع إ…
