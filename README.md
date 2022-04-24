# webpcos2

เป้าหมาย
   ประเมินความเสี่ยงในการเกิดโรคภาวะถุงน้ำในรังไข่หลายใบจากผู้ใช้งาน ทำการประเมินจากข้อมูลสุขภาพส่วนตัวของผู้ใช้งาน โดยเลือกข้อมูลของ อายุ น้ำหนัก ส่วนสูง การมาของประจำเดือน การเกิดสิว ผิวมัน และขนที่เกิดขึ้นมากกว่าปกติหรือไม่ โดยผู้ใช้งานต้องทำการสำรวจตนเองแล้วมาทำการประเมิน
ข้อจำกัด
1) ข้อมูลสุขภาพที่ใช้ในการประเมินต้องเป็นข้อมูลผู้ใช้งานสามารถตรวจได้ด้วยตนเอง
2) ข้อมูลสุขภาพบางประเภทที่ผู้ใช้งานต้องใช้การสังเกตในการวัดเอง

ฐานของมูล 
PCOS_inFertility.csv
data_without_infertility.csv
https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos


แอปพลิเคชั่น แบบประเมิน (Streamlit)
Pcos-app.py

หากผู้พํฒนา อยากออกแบบหน้าเว็บไซตื เพิ่มเติม : https://docs.streamlit.io/

โมเดลจาก CoLab 
PcosApp.joblib
ผู้ศึกษาได้ ทำการวัดประสิทธิภาพ และ เลือก โมเดลการถดถอยโลจิสติก 
โดย ค่าของจุดแบ่ง อยู่ ที่ 0.60 

รูปภาพ 
hairgrowP.jpg : วาดโดย P1(ปวิตรา สาริวงษ์) โดยอ้างอิงจาก  Ferriman D, Gallwey JD: Clinical assessment of body hair growth in women.Journal of Clinical Endocrinology 1961; 21:1440–1447.
skin darkenP.jpg : วาดโดย P1(ปวิตรา สาริวงษ์)

** โปรดตรวจสอบ เวอร์ชั่นของ ภาษา python
runtime.txt

การนำไปปรับใช้กับ Heroku 
1) ผ่าน Command line โดยดาวน์โหลดแอป Heroku CLI : https://devcenter.heroku.com/articles/heroku-cli  
2) ผ่าน GitHub ท่านสามารถเชื่องโยงกับ GitHub ของท่าน บนเว็บ Heroku และ สามารถ นำไฟล์อัปโหลดและ Deploy ได้เลย 


