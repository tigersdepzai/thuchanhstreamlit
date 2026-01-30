import streamlit as st
import time 
st.title(" xây dựng trang đăng ký tài khoản")


tai_khoan = st.text_input("nhập tài khoản của bạn:")

mat_khau1 = st.text_input("nhập mật khẩu của bạn:", type="password")

mat_khau2 = st.text_input("nhập lại mật khẩu của bạn:", type="password")

ten_ngouoi_dung = st.text_input("nhập tên người dùng của bạn:")

email = st.text_input("nhập email của bạn:")
tien_do = st.progress(0)
if st.button("submit"):
    time.sleep(1)
    for i in range(100):
        tien_do.progress(i + 1)

st.write(f"tài khoản của bạn là: {tai_khoan}")
st.write(f"mật khẩu của bạn là: {mat_khau1}")
st.write(f"tên người dùng của bạn là: {ten_ngouoi_dung}")
st.write(f"email của bạn là: {email}")
