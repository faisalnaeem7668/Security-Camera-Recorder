from sqlalchemy.sql.expression import except_all
import streamlit as st
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database import Recording
from my_project import recording

def opendb():
    engine = create_engine('sqlite:///project.db')
    Session = sessionmaker(bind=engine)
    return Session()

st.title("Security Camera Recorder🎥")

os.mkdir("Recordings") if not  os.path.exists("Recordings") else print("Recording Folder Found")
total_files = os.listdir("Recordings")
total_files = [os.path.join("Recordings",file) for file in total_files]

with st.form('form_new'):
    
    rec_choices=['30 Seconds','2 Minutes','5 Minutes','10 Minutes','30 Minutes','1 Hour','2 Hours']

    rec_drt=st.selectbox("Approx Recording Durations",rec_choices)
     
    rec_clipname=st.text_input("Enter The Name For Recording Clip")
    
    btn=st.form_submit_button("Start Recording")



if btn and rec_drt and rec_clipname:
    if not os.path.exists(os.path.join("Recordings",rec_clipname)+".avi"):
        clip = os.path.join("Recordings",rec_clipname)
        st.write('Recording Will Be Saved By The Name:', clip)
        st.write(f"Recording Is Started For {rec_drt} From Now!!!")
        st.success("Recording Started Successfully")

        if rec_drt ==rec_choices[0]:
            t=30
            path = recording(clip,t)
            db = opendb()
            db.add(Recording(path=path))
            db.commit()
            db.close()

        elif rec_drt==rec_choices[1]:
            t=2*60
            path = recording(clip,t)
            db = opendb()
            db.add(Recording(path=path))
            db.commit()
            db.close()

        elif rec_drt==rec_choices[2]:
            t=5*60
            path = recording(clip,t)
            db = opendb()
            db.add(Recording(path=path))
            db.commit()
            db.close()

        elif rec_drt==rec_choices[3]:
            t=10*60
            path = recording(clip,t)
            db = opendb()
            db.add(Recording(path=path))
            db.commit()
            db.close()

        elif rec_drt==rec_choices[4]:
            t=30*60
            path = recording(clip,t)
            db = opendb()
            db.add(Recording(path=path))
            db.commit()
            db.close()
        
        elif rec_drt==rec_choices[5]:
            t=60*60
            path = recording(clip,t)
            db = opendb()
            db.add(Recording(path=path))
            db.commit()
            db.close()
        elif rec_drt==rec_choices[6]:
            t=120*60
            path = recording(clip,t)
            db = opendb()
            db.add(Recording(path=path))
            db.commit()
            db.close()

    else:
        st.error("Recording Already Exists, Please Change File Name")
btn1=st.button("View All Previous Recordings")
if btn1:
    try:
        db = opendb()
        videos = db.query(Recording).all()
        for vid in videos:
            st.markdown(f'''
            ## {vid.id}. {vid.path}
            `Video Is Available At Given Path`
            ''')
    except:
        pass
    else:
        db.close()
    



    