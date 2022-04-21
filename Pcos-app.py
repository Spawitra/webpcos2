import streamlit as st
import pandas as pd
import joblib
from joblib import dump, load
from PIL import Image

HairG = Image.open("hairgrowP.jpg")
Skindarken = Image.open("skin darkenP.jpg")


st.header("""แอปพลิเคชั่น
## ประเมินความเสี่ยงโรคถุงน้ำรังไข่หลายใบ

ว่าคุณจะมีความเสี่ยงเป็นโรคถุงน้ำในรังไข่หลายใบหรือไม่
""")
st.write('<<< หากไม่พบแบบประเมิน คลิกลูกศรมุมซ้ายบนเพื่อเปิดทำการประเมินความเสี่ยง')

st.error('''แบบประเมินความเสี่ยง เป็นเพียงการประเมินความเสี่ยงเบื้อต้น
        มิใช้การวินิจฉัยจากแพทย์ หากการประเมินพบว่ามีความเสี่ยง 
        ท่านสามารถไปปรึกษาหรือเข้าพบแพทย์ผู้เชี่ยวชาญ
        ได้ที่คลินิกนรีเวชกรรม หรือ คลินิกสูติ-นรีเวช ตามโรงพยาบาลใกล้บ้าน
        เพื่อสอบถามหรือทำการรักษาต่อไป         
        ศึกษาเกี่ยวกับโรคเพิ่มเติม  
        
        https://www.bangkokhospital.com/content/overweight-women-are-more-likely-to-face-polycystic-ovary-syndrome
         ''') 

st.sidebar.header('แบบประเมินความเสี่ยงโรคถุงน้ำรังไข่หลายใบ')
st.sidebar.subheader('กรอกข้อมูล')
st.sidebar.write('--------------------------------------------------------------------')
# รับ User input feature  X 
def user_input_features():
  
  Age = st.sidebar.slider('อายุเท่าไหร่',0,100,22)
  st.sidebar.write('อายุ', Age,'ปี')
  st.sidebar.write(' # --------------------------------------')
  
  Weight= st.sidebar.slider('น้ำหนัก (Kg)เท่าไหร่',0,150,79)
  st.sidebar.write('น้ำหนัก', Weight, 'กิโลกรัม')
  st.sidebar.write(' # --------------------------------------')
  
  Cycle = st.sidebar.slider('ประจำเดือนมากี่วัน',0,31,7)
  st.sidebar.write('รอบเดือนมา', Cycle, 'วัน')
  st.sidebar.write(' # --------------------------------------')
  
  CycleLength= st.sidebar.slider('ระยะห่างของรอบเดือน ห่างกันกี่วัน',0,60,16)
  st.sidebar.write('ระยะห่างของรอบเดือน', CycleLength, 'วัน')
  st.sidebar.write(' # --------------------------------------')
  st.sidebar.write('### สอบถามอาการ ใช่(1)หรือไม่(0) ')
  hairGrowth = st.sidebar.slider('ขนตามจุดต่างๆเพิ่มขึ้นหรือไม่ ',0,1,1)
  st.sidebar.caption('''สังเกตตามจุดต่างๆบนร่างกาย ว่ามีขนเพิ่มขึ้นหรือไม่ เช่น จากไม่มีขนเลย เพิ่มขึ้นไประดับ1 หรือ มีขนที่ระดับ3แล้วเพิ่มขึ้นไประดับ4 ''')
  st.sidebar.write('ขนเพิ่มขึ้นหรือไม่', hairGrowth)
  st.sidebar.image(HairG, use_column_width = True)
  st.sidebar.write(' # --------------------------------------')
  
  SkinDarkening= st.sidebar.slider('ผิวดำคล้ำตามข้อต่างๆหรือไม่',0,1,0)
  st.sidebar.caption('ผิวคล้ำดำหนา ตามจุด ข้อนิ้ว ข้อศอก คอ หรือ รักแร้ เป็นต้น')
  st.sidebar.image(Skindarken, use_column_width = True)
  st.sidebar.write('ผิวดำคล้ำตามข้อต่างๆ', SkinDarkening)
  st.sidebar.write(' # --------------------------------------')
  

  Pimples= st.sidebar.slider('สิวเพิ่มขึ้นหรือไม่',0,1,1)
  st.sidebar.caption('สังเกตตนเองหากปกติไม่มีสิว แล้วสิวเกิดขึ้นมาเกินไป หากมีสิวขึ้นเยอะอยู่แล้วไม่ได้เพิ่มขึ้นถือว่าปกติ')
  st.sidebar.write('สิวเกิดเพิ่มขึ้น', Pimples)
  st.sidebar.write(' # --------------------------------------')
  

  Fastfood= st.sidebar.slider('รับประทานอาหารที่มีไขมันสูง (Fastfood) ',0,1,0)
  st.sidebar.write('ทานอาหารที่มีไขมันสูงหรือไม่', Fastfood)
  st.sidebar.caption('ชอบรับประทานอาหารที่มีไขมันสูง หรือ ทานบ่อยครั้ง')
  st.sidebar.write(' # --------------------------------------')
  

  FollicleL= st.sidebar.slider('หน้ามันรูขุมขนทางด้านซ้าย กว้างขึ้นหรือไม่',0,1,1)
  st.sidebar.write('หน้ามันและรูขุมขนกว้างทางด้านซ้ายหรือไม่', FollicleL)
  st.sidebar.write(' # --------------------------------------')
  

  FollicleR= st.sidebar.slider('หน้ามันรูขุมขนทางด้านขวา กว้างขึ้นหรือไม่',0,1,1)
  st.sidebar.write('หน้ามันและรูขุมขนกว้างทางด้านขวาหรือไม่' , FollicleR)
  st.sidebar.write(' # --------------------------------------')
  

  WeightGain= st.sidebar.slider( 'ช่วงนี้น้ำหนักเพิ่มขึ้นหรือไม่',0,1,1)
  st.sidebar.caption('น้ำหนักเพิ่มขึ้นแบบรวดเร็วหรือไม่ เช่น จาก60เพิ่มไป 70 ในระยะเวลาสั้นๆ')
  st.sidebar.write('น้ำหนักเพิ่มขึ้น', WeightGain)
  st.sidebar.write(' # --------------------------------------')
  st.sidebar.caption('Ferriman D, Gallwey JD: Clinical assessment of body hair growth in women. Journal of Clinical Endocrinology 1961; 21:1440–1447.')


  
  
  pipe =  { 'Age (yrs)': Age,
             'Weight (Kg)': Weight, 
             'Cycle(R/I)': Cycle,
              'Cycle length(days)': CycleLength,
              'hair growth(Y/N)': hairGrowth, 
               'Skin darkening (Y/N)': SkinDarkening,
               'Pimples(Y/N)': Pimples,
              'Fast food (Y/N)': Fastfood,
               'Follicle No. (L)': FollicleL, 
                'Follicle No. (R)': FollicleR, 
                'Weight gain(Y/N)': WeightGain}

  features = pd.DataFrame(pipe, index=[0])
  return features

app  = load('AppPcosL.joblib')

name = ['''negative

ท่านมีความเสี่ยงน้อย




''', '''possitive

ท่านมีความเสี่ยง 


สามรถดูแลสุขภาพตนเอง  โดยการออกกำลังกาย และรับทานอาหารครบ 5 หมู่
*ควร เลี่ยงทานอาหารที่มีไขมันสูง*  และพบแพทย์ผู้เชี่ยวชาญสำหรับการวินิจฉัยโรค และการรักษาต่อไป
''']


df = user_input_features()

st.subheader('ทำการประเมินความเสี่ยง')
st.write(df)


prediction = app.predict(df)
prediction_proba = app.predict_proba(df)
submit = st.button('ทำการประเมินความเสี่ยง')
if submit:

    st.subheader('ผลการทำนาย (Prediction)')
    if prediction[0]:
        
        st.error(name[1])   

    else:
        st.success(name[0])



    st.subheader('เปอร์เซ็นความเสี่ยง (Prediction Probability)')
    st.write('โอกาสเสี่ยงน้อย','|',  'โอกาสเสี่ยงมาก')
    st.write(prediction_proba)


       


with st.expander('''รบกวนทำแบบสอบถามการใช้งานเว็บไซต์'''):
     st.write("""
         แบบสอบถามประสิทธิภาพของแบบทดสอบ วามีการประเมินได้ถูกต้องมากแค่ไหน
     """)
     st.write("https://forms.gle/u7GK9hvWkpWjJjaD9")


