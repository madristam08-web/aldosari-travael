import streamlit as st, random, urllib.parse
from datetime import date
st.set_page_config(page_title="احمد الدوسري للسفر",layout="wide")
IBAN="SA38 8000 0000 6080 1016 7520";ACC="608010167520";WA="966553769426"
SAUDI=["الرياض - RUH","جدة - JED","الدمام - DMM","القصيم - ELQ"]
WORLD=["دبي - DXB","القاهرة - CAI","لندن - LHR","اسطنبول - IST"]
st.title("✈️ احمد الدوسري للسفر")
c1,c2,c3=st.columns(3)
with c1: f=st.selectbox("من:",SAUDI+WORLD,key="from_city")
with c2: t=st.selectbox("إلى:",WORLD+SAUDI,key="to_city")
with c3: dt=st.date_input("التاريخ:",date.today())
if st.button("بحث",type="primary",use_container_width=True):
 st.session_state.s=True
 st.session_state.fc=f;st.session_state.tc=t;st.session_state.dt=str(dt)
 st.session_state.fl=[
  {"fl":f"SV {random.randint(100,999)}","cls":"اقتصادي بدون شنط","p":random.randint(800,1000)},
  {"fl":f"SV {random.randint(100,999)}","cls":"اقتصادي مع شنطة","p":random.randint(1100,1350)},
  {"fl":f"SV {random.randint(100,999)}","cls":"رجال اعمال","p":random.randint(1450,1800)}
 ]
 st.session_state.pay=False;st.session_state.c=False;st.session_state.has_receipt=False

if st.session_state.get("s"):
 st.markdown("### 💳 مدى | VISA | Mastercard | Apple Pay | stc pay | tabby | الراجحي")
 for i,x in enumerate(st.session_state.fl):
  with st.container(border=True):
   st.write(f"*{x['fl']}* | {x['cls']} | {st.session_state.fc}→{st.session_state.tc} | {x['p']} ر.س | {st.session_state.dt}")
   if st.button("احجز الآن",key=f"book_{i}",type="primary"):
    st.session_state.sp=x['p'];st.session_state.sf=x['fl'];st.session_state.cls=x['cls']
    st.session_state.pay=True;st.session_state.c=False;st.rerun()

if st.session_state.get("pay") and not st.session_state.get("c"):
 with st.container(border=True):
  st.subheader(f"💳 ادفع لـ {st.session_state.sf} - {st.session_state.sp} ر.س - {st.session_state.cls}")
  pay_method = st.selectbox("اختر وسيلة الدفع:",["تحويل بنكي - الراجحي","مدى - Mada","Visa","Mastercard","Apple Pay","STC Pay","Tabby"],key="pay_method_select")
  if pay_method=="تحويل بنكي - الراجحي":
   st.warning(f"🏦 احمد الدوسري\nالحساب: {ACC}\nالآيبان: {IBAN}\nالمبلغ: {st.session_state.sp} ر.س")
  
  up=st.file_uploader("📸 ارفع صورة إيصال التحويل (إجباري):",type=["jpg","jpeg","png","pdf"],key="receipt_uploader")
  if up:
   st.session_state.has_receipt=True
   st.success("✅ تم رفع الإيصال")
   if up.type!="application/pdf": st.image(up, width=300)
  else:
   st.session_state.has_receipt=False
   st.error("⚠️ لازم ترفع الإيصال عشان نعرف الفلوس وصلت")

  can = st.session_state.has_receipt
  if st.button("💚 تأكيد الدفع والحجز",type="primary",use_container_width=True,disabled=not can,key="confirm_pay"):
   st.session_state.bk=f"AHM-{random.randint(10000,99999)}"
   st.session_state.final_pay=pay_method
   st.session_state.c=True
   st.balloons()
   st.rerun()
  if not can:
   st.caption("زر التأكيد بيتفعل بعد رفع الإيصال 👆")

if st.session_state.get("c"):
 b=st.session_state.bk
 msg=f"حجز جديد {b} {st.session_state.sf} {st.session_state.cls} {st.session_state.fc}->{st.session_state.tc} {st.session_state.sp} ر.س {st.session_state.final_pay} - الزبون رفع الإيصال شيك الراجحي {ACC}"
 link=f"https://wa.me/{WA}?text={urllib.parse.quote(msg)}"
 st.success(f"✅ تم الحجز {b} عبر {st.session_state.final_pay}")
 st.warning(f"حسابي {ACC} - تم استلام إيصالك سنراجع وصول {st.session_state.sp} ر.س في تطبيق الراجحي")
 st.link_button("📱 ارسل الحجز + الإيصال لواتسابي 0553769426",link,type="primary",use_container_width=True)
 st.download_button("🖨️ طباعة التذكرة",msg,file_name=f"{b}.txt",use_container_width=True)
 if st.button("حجز جديد",key="new_search"): 
  st.session_state.s=False;st.session_state.pay=False;st.session_state.c=False;st.session_state.has_receipt=False;st.rerun()
