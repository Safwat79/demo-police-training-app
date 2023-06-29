import streamlit as st  
import pandas as pd



# Remove the hamburger button on the page of streamlit
st.markdown("""
<style> 
.css-nqowgj.e1ewe7hr3
{
    visibility: hidden;
}
</ style>
""", unsafe_allow_html=True)

# Remove the footer on the page of streamlit
st.markdown("""
<style> 
.css-h5rgaw.e1g8pov61
{
    visibility: hidden;
}
</ style>
""", unsafe_allow_html=True)



# Title
st.title('This is not an assessment \n (This is a Police-ops Training session revision )')

st.markdown("--------------------------------------------------------------------------------")


# Image
st.image("intro.jpg", caption='You will be haked so soon', width=500)

# Subheader
st.subheader('Please answer the questions below:')

# multiselect
multi_select = st.multiselect("أذكر أنواع العمليات الشرطية؟؟", options= ("دفاعية", "× صحر اوية", "هجومية"))
st.write(multi_select)

st.markdown("--------------------------------------------------------------------------------")

# multiselect
multi_select1 = st.selectbox("ما هو عدد مراحل التدريب الحركي؟؟", options= (" ", "× 5", "× 3",  "6"))
print(multi_select1)

st.markdown("--------------------------------------------------------------------------------")

# multiselect
multi_select2 = st.selectbox("يعتبر الإقتحام في المناطق الصحراوية من أهم العمليات الدفاعية وأخطرها ؟؟", options= ("", " × أوافق", "لا أوافق", " × أوافق بشدة"))
print(multi_select2)

st.markdown("--------------------------------------------------------------------------------")

# multiselect
multi_select3 = st.selectbox("تعتبر عمليات حماية المنشأت السياحية وتأمينها من أهم عمليات الشرطة الدفاعية ؟؟", options= ("", "أوافق", "× لا أوافق", " × أوافق بشدة"))
print(multi_select3)

st.markdown("--------------------------------------------------------------------------------")

# multiselect
multi_select4 = st.selectbox("من فضلك رتب مراحل التدريب الحركي من وجهة نظر الإستراتيجية التكتيكية ؟؟", options= ("", "الترتيب هو : اللإدراكية - الترابطية - المستقلة", "الترتيب هو : المستقلة - الإدراكية - الترابطية", "الترتيب هو : المستقلة - الترابطية - الإدراكية"))
print(multi_select4)

st.markdown("--------------------------------------------------------------------------------")

st.markdown("**Congrats you have achieved the course and please remember how the picture below is so important for police ops Instructors**")
# Image
st.image("end.jpg", width=500)





