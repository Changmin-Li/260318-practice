import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import plotly.express as px
from io import StringIO

# 한글 폰트 설정
font_path = '/workspaces/260318-practice/fonts/NanumGothic-Regular.ttf'
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

st.title("데이터 시각화 예시")

# 데이터 입력 섹션
st.sidebar.header("데이터 입력")
option = st.sidebar.selectbox("데이터 소스 선택", ["샘플 데이터", "파일 업로드", "텍스트 입력"])

data = None

if option == "샘플 데이터":
    # 샘플 데이터 생성
    data = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [10, 20, 15, 25, 30],
        'category': ['A', 'B', 'A', 'B', 'A']
    })
    st.sidebar.write("샘플 데이터를 사용합니다.")

elif option == "파일 업로드":
    uploaded_file = st.sidebar.file_uploader("CSV 파일 업로드", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.sidebar.write("파일이 업로드되었습니다.")
    else:
        st.sidebar.write("CSV 파일을 업로드하세요.")

elif option == "텍스트 입력":
    text = st.sidebar.text_area("데이터를 CSV 형식으로 입력하세요 (예: x,y,category\n1,10,A\n2,20,B)")
    if text:
        try:
            data = pd.read_csv(StringIO(text))
            st.sidebar.write("텍스트 데이터가 로드되었습니다.")
        except Exception as e:
            st.sidebar.error(f"데이터 파싱 오류: {e}")
    else:
        st.sidebar.write("CSV 형식의 데이터를 입력하세요.")

# 데이터 표시 및 시각화
if data is not None:
    st.header("데이터 미리보기")
    st.dataframe(data.head())

    st.header("시각화 예시")

    # 사용 가능한 컬럼 확인
    columns = data.columns.tolist()

    # 막대 그래프
    if len(columns) >= 2:
        st.subheader("막대 그래프")
        x_col = st.selectbox("X축 선택", columns, key="bar_x")
        y_col = st.selectbox("Y축 선택", columns, key="bar_y")
        if x_col and y_col:
            fig, ax = plt.subplots()
            ax.bar(data[x_col], data[y_col])
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            st.pyplot(fig)

    # 선 그래프
    if len(columns) >= 2:
        st.subheader("선 그래프")
        x_col = st.selectbox("X축 선택", columns, key="line_x")
        y_col = st.selectbox("Y축 선택", columns, key="line_y")
        if x_col and y_col:
            fig, ax = plt.subplots()
            ax.plot(data[x_col], data[y_col])
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            st.pyplot(fig)

    # 산점도
    if len(columns) >= 2:
        st.subheader("산점도")
        x_col = st.selectbox("X축 선택", columns, key="scatter_x")
        y_col = st.selectbox("Y축 선택", columns, key="scatter_y")
        if x_col and y_col:
            fig = px.scatter(data, x=x_col, y=y_col, title="산점도")
            st.plotly_chart(fig)

    # 히스토그램
    if len(columns) >= 1:
        st.subheader("히스토그램")
        col = st.selectbox("컬럼 선택", columns, key="hist")
        if col:
            fig, ax = plt.subplots()
            ax.hist(data[col])
            ax.set_xlabel(col)
            ax.set_ylabel("빈도")
            st.pyplot(fig)

    # 카테고리별 막대 그래프 (Plotly)
    if len(columns) >= 2:
        st.subheader("카테고리별 막대 그래프")
        cat_col = st.selectbox("카테고리 컬럼 선택", columns, key="cat_bar_cat")
        val_col = st.selectbox("값 컬럼 선택", columns, key="cat_bar_val")
        if cat_col and val_col:
            fig = px.bar(data, x=cat_col, y=val_col, title="카테고리별 막대 그래프")
            st.plotly_chart(fig)

else:
    st.write("데이터를 입력하여 다양한 시각화 예시를 확인하세요.")