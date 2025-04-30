import streamlit as st

try:
    import openai
except ImportError:
    st.error(
        "❗️ openai 라이브러리가 설치되지 않았습니다. requirements.txt에 'openai'를 추가해주세요."
    )
    st.stop()

# 사이드바에서 API 키 입력
st.sidebar.title("🔐 OpenAI API setting")
api_key = st.sidebar.text_input("OpenAI API Key 입력", type="password")

# 제목과 설명
st.title("💬 GPT-4.1-mini Chat App")
st.markdown("Get user's question / Print GPT's answer")

# 위젯 1: 사용자 질문 입력
question = st.text_input("💭 enter your question")

# 위젯 2: 토큰 수 조절
max_tokens = st.slider(
    "🔢 maximum token number", min_value=10, max_value=2048, value=300
)

# 위젯 3: GPT 응답 버튼
if st.button("📝 ask to GPT"):
    if not api_key:
        st.warning("🔑 enter your OpenAI API first!")
    elif not question:
        st.warning("❓ ask question!")
    else:
        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",  # 또는 "gpt-4.1-mini"
                messages=[{"role": "user", "content": question}],
                temperature=0.7,
                max_tokens=max_tokens,
            )
            answer = response.choices[0].message.content
            st.success("✅ GPT' answer")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ ERROR: {e}")
