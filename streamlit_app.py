import streamlit as st

try:
    import openai
    from openai import OpenAI
except ImportError:
    st.error(
        "❗️ The 'openai' library is not installed. Please add it to requirements.txt."
    )
    st.stop()

# Sidebar: API key input
st.sidebar.title("🔐 OpenAI API Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

st.title("💬 GPT-4.1-mini Chat App")
question = st.text_input("💭 Enter your question:")
max_tokens = st.slider("🔢 Max tokens", 10, 2048, 300)

if st.button("📝 Ask GPT"):
    if not api_key:
        st.warning("🔑 Please enter your OpenAI API key!")
    elif not question:
        st.warning("❓ Please enter a question!")
    else:
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                temperature=0.7,
                max_tokens=max_tokens,
            )
            answer = response.choices[0].message.content
            st.success("✅ GPT's response:")
            st.write(answer)

        except Exception as e:
            st.error("❌ Error occurred. Check console for details.")
            print("🚨 Detailed error log:")
            print(e)  # 콘솔 출력용
