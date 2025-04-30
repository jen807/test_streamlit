import streamlit as st
import openai

# 사이드바: API 키 입력
st.sidebar.title("🔐 OpenAI API 설정")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# 제목
st.title("💬 GPT-4.1-mini Chat with Streamlit")

# 사용자 질문 입력
user_input = st.text_input("💭 당신의 질문을 입력하세요")

# 최대 토큰 수 설정
max_tokens = st.number_input("🧮 최대 토큰 수", min_value=10, max_value=2048, value=300)

# 응답 버튼
if st.button("📝 답변 받기"):
    if not api_key:
        st.warning("⚠️ 먼저 OpenAI API 키를 입력해주세요.")
    elif not user_input:
        st.warning("⚠️ 질문을 입력해주세요.")
    else:
        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",  # 또는 gpt-4.1-mini
                messages=[{"role": "user", "content": user_input}],
                temperature=0.7,  # 기본값 고정
                max_tokens=max_tokens,
            )
            answer = response.choices[0].message.content
            st.success("✅ GPT의 응답:")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ 오류 발생: {e}")
