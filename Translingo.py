import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO

st.title("🌐 TransLingo")
st.caption("Connecting Languages, Simplifying Communication.")

languages = {
    "English": "en",
    "Urdu": "ur",
    "Hindi": "hi",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Turkish": "tr",
    "Dutch": "nl"
}

source_options = ["Auto Detect"] + list(languages.keys())

source = st.selectbox("Source Language", source_options)
target = st.selectbox("Target Language", languages.keys())

text = st.text_area("Enter text")

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    elif source == target:
        st.warning("Please select different languages.")

    else:
        try:
            if source == "Auto Detect":
                source_language = "auto"
            else:
                source_language = languages[source]

            translation = GoogleTranslator(
                source=source_language,
                target=languages[target]
            ).translate(text)

            st.subheader("Translation")
            st.code(translation)

            speech = gTTS(
                text=translation,
                lang=languages[target]
            )

            audio = BytesIO()
            speech.write_to_fp(audio)

            st.subheader("🔊 Listen")
            st.audio(audio.getvalue(), format="audio/mp3")

        except Exception:
            st.error("Translation failed. Please check your internet connection.")   
            