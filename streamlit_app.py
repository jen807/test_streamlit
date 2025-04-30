import streamlit as st
import openai

st.title("Minimal GPT Chat App")

api_key = st.text_input("Enter your OpenAI API Key", type="password")
question = st.text_input("Your question:")

if st.button("Ask"):
    if not api_key or not question:
        st.warning("Please enter both API key and question.")
    else:
        try:
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                temperature=0.7,
                max_tokens=200,
            )
            st.success("Answer:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error("❌ Error:")
            st.code(str(e))
