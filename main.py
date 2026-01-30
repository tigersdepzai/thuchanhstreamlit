import streamlit as st
st.set_page_config(page_title = "Trắc Nghiệm tính cách", page_icon = ":question:" , layout = "wide")
st.title("hãy chọn một con vật mà bạn thích nhất")
col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    button1 = st.button("con mèo")
with col2:
    button2 = st.button("con chó")
with col3:
    button3 = st.button("con sư tử")
with col4:
    button4 = st.button("con ngựa")
with col5:
    button5 = st.button("Thiên nga")
if button1:
    with st.expander("bạn đã chọn con mèo"):
        st.write("bạn là người rất tinh tế ,thông minh và nhanh nhẹn")
if button2:
    with st.expander("bạn đã chọn con chó"):
        st.write("bạn là người rất trung thành ,dũng cảm và biết bảo vệ mọi người xung quanh")
if button3:
    with st.expander("bạn đã chọn con sư tử"):
        st.write("bạn là người rất mạnh mẽ ,tự tin và có khả năng lãnh đạo")
if button4:
    with st.expander("bạn đã chọn con ngựa"):
        st.write("bạn là người rất nhiệt huyết ,yêu tự do và có tinh thần phóng khoáng")
if button5:
    with st.expander("bạn đã chọn con thiên nga"):
        st.write("bạn là người rất thanh lịch ,duyên dáng và có gu thẩm mỹ cao")
with st.sidebar:
    st.header("")