import streamlit as st
from openai import OpenAI

st.title("OpenAI GPT model (fixed)")

api_key = st.text_input("OpenAI API Key", type="password")
prompt = st.text_area("User prompt")

if st.button("Ask!", disabled=(len(prompt) == 0)):
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # 또는 "gpt-4"
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300,
        )
        st.write("Answer:")
        st.write(response.choices[0].message.content)
    except Exception as e:
        st.error("Error occurred:")
        st.code(str(e))
