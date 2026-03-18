import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit UI Demo", layout="wide")

st.title("🔧 Streamlit 기본 컴포넌트 데모")
st.write("이 데모 페이지는 Streamlit에서 자주 쓰는 기본 요소를 보여줍니다.")

st.header("1) 텍스트/마크다운")
st.caption("`st.write`, `st.markdown`, `st.subheader`, `st.latex` 사용 예시")
st.write("안녕하세요, Streamlit 앱입니다!")
st.markdown("**굵은 텍스트**와 *기울임 텍스트*, `코드`, [링크](https://streamlit.io)")
st.subheader("서브헤더")
st.latex(r"E = mc^2")

st.header("2) 인풋 위젯")
col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input("이름")
    age = st.number_input("나이", min_value=0, max_value=120, value=25)
with col2:
    color = st.color_picker("선호 색")
    agree = st.checkbox("이용 약관에 동의함")
with col3:
    option = st.selectbox("옵션 선택", ["옵션 A", "옵션 B", "옵션 C"])
    choice = st.radio("라디오 선택", ["예", "아니오"])

if st.button("결과 보기"):
    st.success(f"{name}님({age}세), 선택 값: {option}, 라디오: {choice}, 색: {color}, 동의: {agree}")

st.header("3) 데이터 및 테이블")

df = pd.DataFrame({
    "날짜": pd.date_range("2023-01-01", periods=5, freq="D"),
    "값": np.random.randint(10, 100, size=5),
})

st.dataframe(df)
st.table(df)

st.header("4) 차트")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
st.bar_chart(chart_data)

st.header("5) 레이아웃 & 상호작용")
with st.expander("숨김 정보 펼치기"):
    st.write("여기에 추가 설명을 넣을 수 있습니다.")

with st.spinner("로딩 중..."):
    import time
    time.sleep(0.5)

st.success("모든 컴포넌트 데모가 준비되었습니다!")
