import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from text_parser import Parser
from Regex import Regex

if __name__ == "__main__":
    st.title("Regex Checker")

    genre = st.radio(
    "Input type:",
    ["Raw text", "File upload"])
    # captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])
    raw_text = None
    file: UploadedFile = None
    if genre == "Raw text":
        raw_text = st.text_area("Input text:", value = "owais")
    else:
        file = st.file_uploader("Text file:")
    # print(raw_text)
    parser: Parser = Parser(raw_text, file)
    text = parser.getText()
    regex: Regex = Regex(text)
    results: list[list[str]] = regex.detect()
    for result in results:
        st.subheader(result[0])
        for i in range(1, len(result)):
            st.write(i, result[i])