# AI Text Processing Assistant

## Project Overview

AI Text Processing Assistant is a Natural Language Processing (NLP) application developed using Python, Streamlit, and Hugging Face Transformers. It provides a simple web interface to perform different text processing tasks using pre-trained machine learning models.

## Screenshots

<img width="1199" height="542" alt="Screenshot 2026-10-25 140426" src="https://github.com/user-attachments/assets/3895802a-2f8c-41f0-a8d5-c5421a6bd77e" />

## Features

### 1. Text Summarization
Converts long paragraphs into short and meaningful summaries while preserving the main ideas.

### 2. English to French Translation
Translates text from English into French using a pre-trained translation model.

### 3. Sentiment Analysis
Analyzes text and identifies whether the sentiment is positive or negative, along with a confidence score.

### 4. Question Answering
Provides answers to questions based on the context or passage entered by the user.

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch

## Models Used

- **Summarization:** `sshleifer/distilbart-cnn-12-6`
- **Translation:** `Helsinki-NLP/opus-mt-en-fr`
- **Sentiment Analysis:** `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
- **Question Answering:** `distilbert-base-cased-distilled-squad`

## Project Structure

```text
AI-Text-Processing-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Open the Project Folder

```bash
cd AI-Text-Processing-Assistant
```

### Step 3: Install the Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser.

## How to Use

1. Run the application using Streamlit.
2. Select one of the four available NLP tasks.
3. Enter the required text, passage, or question.
4. Click the corresponding action button.
5. View the generated result on the screen.

## Learning Outcomes

- Understanding Hugging Face Transformers and Pipelines.
- Using pre-trained models for NLP tasks.
- Building an interactive web application using Streamlit.
- Understanding practical applications of Natural Language Processing.

## Conclusion

The AI Text Processing Assistant demonstrates how pre-trained Hugging Face models can be integrated into a Streamlit application to perform common Natural Language Processing tasks through a simple and user-friendly interface.
