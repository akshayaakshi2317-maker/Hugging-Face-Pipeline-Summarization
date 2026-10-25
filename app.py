import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Text Processing Assistant",
    page_icon=None,
    layout="wide"
)

st.title("AI Text Processing Assistant")
st.write(
    "Summarization, Translation, Sentiment Analysis "
    "and Question Answering using Hugging Face Pipelines"
)

task = st.selectbox(
    "Select a Task",
    [
        "Summarization",
        "Translation",
        "Sentiment Analysis",
        "Question Answering"
    ]
)


@st.cache_resource
def load_model(task_name):

    if task_name == "Summarization":
        return pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6"
        )

    elif task_name == "Translation":
        return pipeline(
            "translation",
            model="Helsinki-NLP/opus-mt-en-fr"
        )

    elif task_name == "Sentiment Analysis":
        return pipeline(
            "sentiment-analysis",
            model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
        )

    elif task_name == "Question Answering":
        return pipeline(
            "question-answering",
            model="distilbert/distilbert-base-cased-distilled-squad"
        )


if task == "Summarization":

    text = st.text_area(
        "Enter a paragraph to summarize"
    )

    if st.button("Generate Summary"):

        if text.strip():
            with st.spinner("Generating summary..."):

                try:
                    model = load_model(task)

                    result = model(
                        text,
                        max_length=100,
                        min_length=20,
                        do_sample=False
                    )

                    st.subheader("Summary")
                    st.write(result[0]["summary_text"])

                except Exception as e:
                    st.error(f"Error: {e}")

        else:
            st.warning("Please enter a paragraph.")


elif task == "Translation":

    text = st.text_area(
        "Enter English text to translate"
    )

    if st.button("Translate"):

        if text.strip():
            with st.spinner("Translating..."):

                try:
                    model = load_model(task)

                    result = model(
                        text,
                        max_length=128
                    )

                    st.subheader("French Translation")
                    st.write(result[0]["translation_text"])

                except Exception as e:
                    st.error(f"Error: {e}")

        else:
            st.warning("Please enter some text.")


elif task == "Sentiment Analysis":

    text = st.text_area(
        "Enter text for sentiment analysis"
    )

    if st.button("Analyze Sentiment"):

        if text.strip():
            with st.spinner("Analyzing sentiment..."):

                try:
                    model = load_model(task)
                    result = model(text)

                    st.subheader("Sentiment Result")
                    st.write(
                        "Label:",
                        result[0]["label"]
                    )

                    st.write(
                        "Confidence:",
                        f'{result[0]["score"]:.2%}'
                    )

                except Exception as e:
                    st.error(f"Error: {e}")

        else:
            st.warning("Please enter some text.")


elif task == "Question Answering":

    context = st.text_area(
        "Enter the passage or context",
        placeholder="Example: Python is a programming language."
    )

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Get Answer"):

        if context.strip() and question.strip():
            with st.spinner("Finding answer..."):

                try:
                    model = load_model(task)

                    result = model(
                        question=question,
                        context=context
                    )

                    st.subheader("Answer")
                    st.write(result["answer"])

                except Exception as e:
                    st.error(f"Error: {e}")

        else:
            st.warning(
                "Please enter both context and question."
            )


st.divider()

st.caption(
    "Built using Python, Streamlit and Hugging Face Pipelines."
)
