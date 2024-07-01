import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from Regex import Regex
from Matcher import MatchedEntity

if __name__ == "__main__":
    st.title("Regex Checker")

    genre = st.radio(
    "Input type:",
    ["Raw text", "File upload"])
    # captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])
    text = None
    file: UploadedFile = None
    if genre == "Raw text":
        text = st.text_area("Input text:", value = "owais")
    else:
        text = st.file_uploader("Text file:")
    
    regex: Regex = Regex(text)
    extracted: dict[list[MatchedEntity]] = regex.process()
    for key, value in extracted.items():
        st.subheader(key)
        for i in range(len(value)):
            match: MatchedEntity = value[i]
            st.write(str(i + 1) + ". Group = ", match.matched + ", Index = " + str(match.index) + " Length = " + str(match.length))