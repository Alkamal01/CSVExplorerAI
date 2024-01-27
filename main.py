from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        st.error("OPENAI_API_KEY is not set. Please set the API key.")
        st.stop()

    st.set_page_config(page_title="Ask your CSV", page_icon=":bar_chart:")
    st.title("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")

    if csv_file is not None:
        agent = create_csv_agent(OpenAI(temperature=0), csv_file, verbose=True)

        user_question = st.text_input("Ask a question about your CSV:")

        if user_question:
            with st.spinner("In progress..."):
                result = agent.run(user_question)
                st.success("Done!")
                st.write(result)

if __name__ == "__main__":
    main()
