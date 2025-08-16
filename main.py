# from dotenv import load_dotenv
# load_dotenv()  # .env에서 OPENAI_API_KEY 읽기

from langchain_openai import ChatOpenAI
import streamlit as st

st.title("박해진의 시:sunglasses:")
content = st.text_input('시의 주제를 제시해주세요.')

chat = ChatOpenAI(model="gpt-4o-mini")  # 모델 명시 권장(저렴)

if st.button("시 작성 요청하기"):
    with st.spinner('Wait for it...'):
        result = chat.invoke(content + "에 대한 3줄 시를 써줘")
        st.write(result.content)


