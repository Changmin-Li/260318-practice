import streamlit as st

st.set_page_config(page_title="자기 소개 페이지", layout="wide")

st.title("👋 안녕하세요! 자기 소개 페이지입니다")

st.header("이름")
st.write("홍길동")

st.header("소개")
st.write("안녕하세요! 저는 개발을 사랑하는 스트리머입니다. 새로운 기술을 배우고 사람들과 아이디어를 공유하는 것을 즐깁니다.")

st.header("기술 스택")
st.write("- Python\n- Streamlit\n- 데이터 분석 (Pandas, NumPy)\n- 웹 개발 (HTML/CSS, JavaScript)")

st.header("취미")
st.write("- 독서\n- 사이클링\n- 음악 감상")

st.header("연락처")
st.write("- 이메일: example@example.com\n- 깃허브: https://github.com/your-username")

st.success("자기 소개 페이지가 업데이트되었습니다!")
