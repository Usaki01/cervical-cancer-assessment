import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import joblib
import numpy as np
import pandas as pd
from Home import defaults

st.set_page_config(
    page_title="Cervical Cancer Risk Assessment",
    page_icon=":ribbon:",
    #layout="wide", # or centered (auto)
    initial_sidebar_state="collapsed", # or auto/expanded
    menu_items={
        'Report a bug': "https://www.facebook.com/profile.php?id=100007066686160",
        'About': '''เว็บแอพพลิเคชันนี้เป็นส่วนหนึ่งของรายวิชา *Senior Project* ของนักศึกษาปี 4 คณะวิศวกรรมคอมพิวเตอร์ มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี 
                \n **แบบประเมินนี้เป็นเพียงแนวทางในการประเมินความเสี่ยงโรคมะเร็งปากมดลูกเบื้องต้น หากมีข้อสงสัยหรือความกังวล ควรปรึกษาแพทย์ผู้เชี่ยวชาญ** '''
    },
)


st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

if 'age' not in st.session_state:
    defaults()

for key in st.session_state.KEEPERS:
    st.session_state[key]=st.session_state[key]

#Machine Learning Function
def load_and_pre(input_data):
    #load the pre-trained model
    model = joblib.load('isolation_forest_model_final.pkl')

    #Assuming input_data is a NumPy array or a list
    input_data = np.array(input_data).reshape(1,-1)

    #Make predictions using the loaded model
    predictions = model.predict(input_data)
    return predictions


#Change st.session_state to Calculated Variables
if st.session_state.cigarette == "ไม่เคยสูบ":
    cal_cigarette = 0
elif st.session_state.cigarette == "เคยทดลองสูบบ้างแต่ไม่ได้สูบเป็นประจำ":
    cal_cigarette = 1
elif st.session_state.cigarette == "เคยสูบและปัจจุบันยังสูบอยู่":
    cal_cigarette = 2
elif st.session_state.cigarette == "เคยสูบและปัจจุบันเลิกสูบแล้ว":
    cal_cigarette = 3
#------------------------------------------------------------------------------
if st.session_state.alcohol == "ไม่เคยดื่มเลย":
    cal_alcohol = 0
elif st.session_state.alcohol == "ดื่มนานๆครั้ง (น้อยกว่า 1ครั้งต่อเดือน)":
    cal_alcohol = 1
elif st.session_state.alcohol == "เคยดื่ม(หยุดมานานมากกว่า 1 ปี)":
    cal_alcohol = 2
elif st.session_state.alcohol == "ยังดื่มเป็นประจำ":
    cal_alcohol = 3
#------------------------------------------------------------------------------
if st.session_state.excrete == "ปกติ (ขับถ่ายปกติได้วันละครั้ง)":
    cal_excrete = 1
elif st.session_state.excrete == "ขับถ่ายไม่ปกติ(ท้องเสีย ถ่ายแข็ง)":
    cal_excrete = 2
#------------------------------------------------------------------------------
if st.session_state.menses_age == "99":
    st.session_state.menses_age = 14  # median
else:
    num = int(st.session_state.menses_age)
#------------------------------------------------------------------------------
if st.session_state.status == "โสด":
    cal_status = 1
elif st.session_state.status == "สมรส":
    cal_status = 2
elif st.session_state.status == "หม้าย/หย่า/แยกกันอยู่":
    cal_status = 3
#------------------------------------------------------------------------------
if st.session_state.menses == "ยังมีประจำเดือน":
    cal_menses = 1
elif st.session_state.menses == "หมดประจำเดือนแล้ว":
    cal_menses = 2
#------------------------------------------------------------------------------
if st.session_state.pills == "ไม่เคย":
    cal_pills = 0
elif st.session_state.pills == "เคย":
    cal_pills = 1
#------------------------------------------------------------------------------
if st.session_state.menses_char == "มาตรงเวลา สม่ำเสมอ":
    cal_menses_char = 1
elif st.session_state.menses_char == "มาไม่สม่ำเสมอ":
    cal_menses_char = 2
#------------------------------------------------------------------------------
if st.session_state.sex == "ไม่เคย":
    cal_sex = 0
elif st.session_state.sex == "เคย":
    cal_sex = 1
#------------------------------------------------------------------------------
if st.session_state.sex_partner == "ไม่":
    cal_sex_partner = 0
elif st.session_state.sex_partner == "ใช่":
    cal_sex_partner = 1
#------------------------------------------------------------------------------
if st.session_state.protection == "ไม่เคย":
    cal_protection = 0
elif st.session_state.protection == "เคย":
    cal_protection = 1
#------------------------------------------------------------------------------
if st.session_state.protection_now == "ไม่ได้คุมกำเนิด":
    cal_protection_now = 0
elif st.session_state.protection_now == "คุมกำเนิด":
    cal_protection_now = 1
#------------------------------------------------------------------------------
if st.session_state.pregnancy == "ไม่เคย":
    cal_pregnancy = 0
elif st.session_state.pregnancy == "เคย":
    cal_pregnancy = 1
#------------------------------------------------------------------------------
if st.session_state.condom == "ไม่เคยทำเลย":
    cal_condom = 0
elif st.session_state.condom == "ทำบางครั้ง":
    cal_condom = 1
elif st.session_state.condom == "ใช้ทุกครั้ง":
    cal_condom = 2
elif st.session_state.condom == "ไม่เคยมีเพศสัมพันธ์":
    cal_condom = 9
#------------------------------------------------------------------------------
if st.session_state.hpv_check == "ไม่เคย":
    cal_hpv_check = 0
elif st.session_state.hpv_check == "เคย":
    cal_hpv_check = 1
#------------------------------------------------------------------------------
if st.session_state.sex_pain == "ไม่เคย":
    cal_sex_pain = 0
elif st.session_state.sex_pain == "เคย":
    cal_sex_pain = 1
#------------------------------------------------------------------------------
if st.session_state.sex_blood == "ไม่เคย":
    cal_sex_blood = 0
elif st.session_state.sex_blood == "เคย":
    cal_sex_blood = 1
#------------------------------------------------------------------------------
if st.session_state.cervical_blood == "ไม่เคย":
    cal_cervical_blood = 0
elif st.session_state.cervical_blood == "เคย":
    cal_cervical_blood = 1
#------------------------------------------------------------------------------
if st.session_state.pelvic_pain == "ไม่เคย":
    cal_pelvic_pain = 0
elif st.session_state.pelvic_pain == "เคย":
    cal_pelvic_pain = 1
#------------------------------------------------------------------------------
if st.session_state.vagina_discharge == "ไม่มี":
    cal_vagina_discharge = 0
elif st.session_state.vagina_discharge == "มี":
    cal_vagina_discharge = 1
#------------------------------------------------------------------------------
if st.session_state.vagina_discharge_char == "ตกขาวปกติ สีขาวใสไม่มีกลิ่น":
    cal_vagina_discharge_char = 0
elif st.session_state.vagina_discharge_char == "ตกขาวผิดปกติ มีสีเขียว เหลือง แดง เทา มีกลิ่น":
    cal_vagina_discharge_char = 1    
#------------------------------------------------------------------------------
if st.session_state.irritation == "ไม่เคย":
    cal_irritation = 0
elif st.session_state.irritation == "เคย":
    cal_irritation = 1
#------------------------------------------------------------------------------
if st.session_state.tumor == "ไม่เคย":
    cal_tumor = 0
elif st.session_state.tumor == "เคย":
    cal_tumor = 1
#------------------------------------------------------------------------------
if st.session_state.wart == "ไม่เคย":
    cal_wart = 0
elif st.session_state.wart == "เคย":
    cal_wart = 1
#------------------------------------------------------------------------------
if st.session_state.herpes == "ไม่เคย":
    cal_herpes = 0
elif st.session_state.herpes == "เคย":
    cal_herpes = 1
#------------------------------------------------------------------------------
if st.session_state.syphilis == "ไม่เคย":
    cal_syphilis = 0
elif st.session_state.syphilis == "เคย":
    cal_syphilis = 1
#------------------------------------------------------------------------------
if st.session_state.pus == "ไม่เคย":
    cal_pus = 0
elif st.session_state.pus == "เคย":
    cal_pus = 1
#------------------------------------------------------------------------------


#create DataFrame from list
df = pd.DataFrame(columns=['age', 'menses_age', 'cal_pills', 'cal_sex', 'sex_age', 'cal_sex_partner', 'cal_protection', 'cal_protection_now', 'cal_pregnancy', 'cal_hpv_check', 'cal_sex_pain', 'cal_sex_blood', 'cal_cervical_blood', 'cal_pelvic_pain', 'cal_vagina_discharge', 'cal_vagina_discharge_char', 'cal_irritation', 'cal_tumor', 'cal_wart', 'cal_herpes', 'cal_syphilis', 'cal_pus', 'cigarette_0', 'cigarette_1', 'cigarette_2', 'cigarette_3', 'alcohol_0', 'alcohol_1', 'alcohol_2', 'alcohol_3', 'excrete_1', 'excrete_2', 'status_1', 'status_2', 'status_3','menses_1', 'menses_2', 'menses_char_1', 'menses_char_2', 'condom_0', 'condom_1', 'condom_2', 'condom_9'])

data = {
    'age': st.session_state.age,
    'menses_age': st.session_state.menses_age,
    'cal_pills': cal_pills,
    'cal_sex': cal_sex,
    'sex_age': st.session_state.sex_age,
    'cal_sex_partner': cal_sex_partner,
    'cal_protection': cal_protection,
    'cal_protection_now': cal_protection_now,
    'cal_pregnancy': cal_pregnancy,
    'cal_hpv_check': cal_hpv_check,
    'cal_sex_pain': cal_sex_pain,
    'cal_sex_blood': cal_sex_blood,
    'cal_cervical_blood': cal_cervical_blood,
    'cal_pelvic_pain': cal_pelvic_pain,
    'cal_vagina_discharge': cal_vagina_discharge,
    'cal_vagina_discharge_char': cal_vagina_discharge_char,
    'cal_irritation': cal_irritation,
    'cal_tumor': cal_tumor,
    'cal_wart': cal_wart,
    'cal_herpes': cal_herpes,
    'cal_syphilis': cal_syphilis,
    'cal_pus': cal_pus,
    'cigarette_0': 1 if cal_cigarette == 0 else 0,
    'cigarette_1': 1 if cal_cigarette == 1 else 0,
    'cigarette_2': 1 if cal_cigarette == 2 else 0,
    'cigarette_3': 1 if cal_cigarette == 3 else 0,
    'alcohol_0': 1 if cal_alcohol == 0 else 0,
    'alcohol_1': 1 if cal_alcohol == 1 else 0,
    'alcohol_2': 1 if cal_alcohol == 2 else 0,
    'alcohol_3': 1 if cal_alcohol == 3 else 0,
    'excrete_1': 1 if cal_excrete == 1 else 0,
    'excrete_2': 1 if cal_excrete == 2 else 0,
    'status_1': 1 if cal_status == 1 else 0,
    'status_2': 1 if cal_status == 2 else 0,
    'status_3': 1 if cal_status == 3 else 0,
    'menses_1': 1 if cal_menses == 1 else 0,
    'menses_2': 1 if cal_menses == 2 else 0,
    'menses_char_1': 1 if cal_menses_char == 1 else 0,
    'menses_char_2': 1 if cal_menses_char == 2 else 0,
    'condom_0': 1 if cal_condom == 0 else 0,
    'condom_1': 1 if cal_condom == 1 else 0,
    'condom_2': 1 if cal_condom == 2 else 0,
    'condom_9': 1 if cal_condom == 9 else 0
}

#Add Data in DataFrame
df.loc[len(df)] = data

#st.write(df)


#Use Machine Learning Function
predictions = load_and_pre(df)
#st.write(f'การทำนาย: {predictions}')


#Visual Result by Predictions
if predictions == -1 : #If use testing_oneclasssvm_rbf.pkl or testing_oneclasssvm_linear.pkl
    st.markdown("## ท่านมีความเสี่ยงสูงที่จะเป็นมะเร็งปากมดลูก")
    st.write("อย่างไรก็ตาม นั้นยังไม่ได้หมายความว่าท่านเป็นมะเร็งปากมดลูก แต่เนื่องจากท่านมีพฤติกรรมเสี่ยงและอาการที่อาจบ่งถึงมะเร็งปากมดลูกได้ แนะนำพบแพทย์เพื่อ**รับการตรวจภายในและตรวจคัดกรองมะเร็งปากมดลูกทันที** ")
    st.write("โดยท่านสามารถใช้สิทธิการตรวจได้ ตามสิทธิการรักษาของท่าน")
 
    st.write("การตรวจคัดกรองมะเร็งปากมดลูกได้ถูกบรรจุเป็นสิทธิประโยชน์กองทุนหลักประกันสุขภาพแห่งชาติ สำหรับหญิงไทยอายุ 30-59 ปี ทุกคน ทุกสิทธิการรักษา")
    st.write(''' - ติดต่อหน่วยบริการหรือสถานพยาบาลในระบบสปสช.
            \n - จองคิวผ่านแอปเป๋าตัง
            \n - ขอรับชุดตรวจคัดกรองมะเร็งปากมดลูกที่หน่วยบริการ ที่เข้าร่วม เช่น ร้านยา คลินิกการพยาบาล ฯลฯ
            \n **ติดต่อเพิ่มเติม สายด่วน สปสช. 1330**''')
    st.image('risk_factors.jpg',
        caption = 'https://www.facebook.com/chulabhornhospital/photos/a.1122349241168719/1455172234553083/')  
else:
    st.markdown("## ท่านมีความเสี่ยงต่ำที่จะเป็นมะเร็งปากมดลูก")
    st.write("ข้อแนะนำสำหรับกลุ่มความเสี่ยงต่ำ ")
    st.write(''' 1. ฉีดวัคซีนป้องกันเชื้อเอชพีวี (HPV: Human papilloma virus)
        \n 2. มีเพศสัมพันธ์ที่ปลอดภัย มีคู่นอนคนเดียว
        \n 3. แนะนำตรวจคัดกรองมะเร็งปากมดลูก''')
    st.write('''ผู้หญิงที่**ไม่**เคยมีเพศสัมพันธ์แนะนำเริ่มตรวจที่อายุ 30 ปี
          \n ผู้หญิงที่เคยมีเพศสัมพันธ์ แนะนำเริ่มตรวจที่ตั้งแต่อายุ 21 ปี หรือ หลังมีเพศสัมพันธ์ครั้งแรก 3 ปี''')
    st.write('''***การตรวจคัดกรองมะเร็งปากมดลูก แนะนำตรวจ***
             \n 1. การตรวจหาเชื้อเอชพีวี (HPV) ตรวจทุก 5 ปี และ/หรือ
             \n 2. การตรวจเซลล์ปากมดลูก ตรวจทุก 1-2 ปี 
             \n ปัจจุบันแนะนำตรวจเชื้อ HPV เป็นหลัก เนื่องจากมีความไวในการตรวจหามะเร็งปากมดลูกมากกว่าร้อยละ 95 เมื่อเทียบกับการตรวจเซลล์ปากมดลูกซึ่งมีความไวเพียงร้อยละ 50 ''')
    st.image('risk_factors.jpg',
        caption = 'อ้างอิง: https://www.facebook.com/chulabhornhospital/photos/a.1122349241168719/1455172234553083/')   
    st.write("---------------------------------------------------")


#Button Home
columns_back_home = st.columns((2, 1, 2))
button_back_home = columns_back_home[1].button("กลับไปหน้าแรก")
if button_back_home:
    switch_page("home")
    


