import streamlit as st
import pandas as pd
from joblib import dump, load
from PIL import Image

HairG = Image.open("/content/drive/Shareddrives/สัมนาภาวะถุงน้ำในรังไข่หลายใบ/webphoto/unknown (1).png")
Skindarken = Image.open("/content/drive/Shareddrives/สัมนาภาวะถุงน้ำในรังไข่หลายใบ/webphoto/unknown.png")





st.write("""# แอปประเมินความเสี่ยง ว่าคุณจะมีความเสี่ยงเป็นโรคถุงน้ำในรังไข่หลายใบหรือไม่


""")




st.sidebar.header('แบบประเมินความเสี่ยงโรคถุงน้ำรังไข่')

# รับ User input feature  X 
def user_input_features():
  st.sidebar.caption('กรอกข้อมูล')
  Age = st.sidebar.slider('อายุเท่าไหร่',0,100,22)
  st.sidebar.write("อายุ", Age,"ปี")
  st.sidebar.write("--------------------------------------------------------------------")
  Weight= st.sidebar.slider('น้ำหนัก (Kg)',0,150,79)
  st.sidebar.write("น้ำหนัก ", Weight, "กิโลกรัม")
  st.sidebar.write("--------------------------------------------------------------------")
  Cycle = st.sidebar.slider('ประจำเดือนมากี่วัน',0,31,7)
  st.sidebar.write("รอบเดือนมา", Cycle, "วัน")
  st.sidebar.write("--------------------------------------------------------------------")
  CycleLength= st.sidebar.slider('ระยะห่างของรอบเดือน ห่างกันกี่วัน',0,60,16)
  st.sidebar.write("ระยะห่างของรอบเดือน", CycleLength, "วัน") 
  st.sidebar.write("--------------------------------------------------------------------")

  st.sidebar.write("### เลข 0 คือ ไม่  เลข คือ 1ใช่")

  hairGrowth = st.sidebar.slider('ขนเพิ่มขึ้นตามจุดต่างๆ หรือไม่ ',0,1,1)
  st.sidebar.write("ขนเพิ่มขึ้นตามภาพ", hairGrowth)
  st.sidebar.image(HairG, use_column_width = True) 
  st.sidebar.caption("""เช่น ไม่มีขน ไประดับ1 
  หรือ ระดับ3ไประดับ4 
  """)
  st.sidebar.write("--------------------------------------------------------------------")

  SkinDarkening= st.sidebar.slider('ผิวดำคล้ำตามข้อต่างๆหรือไม่',0,1,0)
  st.sidebar.write("ผิวดำคล้ำตามข้อต่างๆ", SkinDarkening)
  st.sidebar.image(Skindarken, use_column_width = True)
  st.sidebar.caption("""ผวิคล้ำดำหนา ตามจุด ข้อนิ้ว ข้อศอก คอ หรือ รักแร้ เป็นต้น""")
  st.sidebar.write("--------------------------------------------------------------------")

  Pimples= st.sidebar.slider('สิวเพิ่มขึ้นหรือไม่',0,1,1)
  st.sidebar.write("สิวเกิดเพิ่มขึ้น", Pimples)
  st.sidebar.write("--------------------------------------------------------------------")

  Fastfood= st.sidebar.slider('รับประทานอาหารที่มีไขมันสูง (Fastfood) ',0,1,0)
  st.sidebar.write("ทานอาหารที่มีไขมันสูงหรือไม่", Fastfood)
  st.sidebar.write("--------------------------------------------------------------------")

  FollicleL= st.sidebar.slider('หน้ามันรูขุมขนทางด้านซ้าย กว้างขึ้นหรือไม่',0,1,1)
  st.sidebar.write("หน้ามันและรูขุมขนกว้างทางด้านซ้ายหรือไม่", FollicleL)
  st.sidebar.write("--------------------------------------------------------------------")

  FollicleR= st.sidebar.slider('หน้ามันรูขุมขนทางด้านขวา กว้างขึ้นหรือไม่',0,1,1)
  st.sidebar.write("หน้ามันและรูขุมขนกว้างทางด้านขวาหรือไม่" , FollicleR)
  st.sidebar.write("--------------------------------------------------------------------")

  WeightGain= st.sidebar.slider( 'ช่วงนี้น้ำหนักเพิ่มขึ้นหรือ ลดน้ำหนักอยากหรือไม่',0,1,1)
  st.sidebar.write("น้ำหนักเพิ่มขึ้น", WeightGain)
  st.sidebar.write("--------------------------------------------------------------------")
  
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



app  = load('PcosApp.joblib') 


name = ['''negative

ท่านมีความเสี่ยงน้อย




''', '''possitive

มีความเสี่ยง 
ท่านสามรถดูแลสุขภาพตนเอง  โดยการออกกำลังกาย และรับทานอาหารครบ 5 หมู่
*ควร เลี่ยงทานอาหารที่มีไขมันสูง*
และพบแพทย์ผู้เชี่ยวชาญสำหรับการวินิจฉัยโรคต่อไป


''']

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

prediction = app.predict(df)
prediction_proba = app.predict_proba(df)


st.subheader('Prediction')
#st.write([prediction])
st.write(name[prediction[0]])

st.subheader('Prediction Probability')
st.write(prediction_proba)


st.write(""" รบกวนทำแบบสอบถามประสิทธิภาพของแบบทดสอบ
 ว่ามีการประเมินได้ถูกต้องมากแค่ไหน """)



if st.button('Say hello'):
     st.write('Why hello there')
else:
  st.write('Goodbye')


st.sidebar.caption("""อ้างอิง 
 [1]  Ferriman-Gallwey
 https://www.researchgate.net/figure/Modified-Ferriman-Gallwey-Score-mFG-score-10_fig1_335003295
 [2] รูปที่ 5แสดงผิวหนังหนาตัว acanthosisnigrican บริเวณต้นคอและรักแร้
 https://he01.tci-thaijo.org/index.php/jmhs/article/view/61311



  
  """)