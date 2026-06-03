# 📰 AI News Summarizer - Email Automation

An AI-powered news summarization tool that fetches the latest news articles and generates concise, readable summaries using Google's Gemini model through LangChain. This project helps users quickly grasp the key information from news articles without having to read lengthy content.

## 🚀 Features

* Fetches real-time news articles using News API
* AI-powered summarization using Google Gemini
* Generates concise and informative summaries
* Simple command-line interface
* Secure API key management with environment variables
* Lightweight and easy to set up

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **Google Gemini API**
* **News API**
* **python-dotenv**
* **Requests**

## 📦 Dependencies

```txt
langchain
langchain-google-genai
python-dotenv
requests
```

## 📂 Project Structure

```bash
AI_News_Summarizer/
│
├── main.py              # Main application script
├── simple_ai.py         # Gemini AI summarization logic
├── send_email.py        # Email delivery functionality
├── .env                 # API keys and credentials (not included)
├── requirements.txt     # Project dependencies
├── .gitignore
└── README.md
```


## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shantanu-25/AI_News_Summarizer.git
cd AI_News_Summarizer
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_news_api_key
```

## ▶️ Running the Project

```bash
python main.py
```

Enter a topic or keyword, and the application will fetch relevant news articles and generate AI-powered summaries.

## 🎯 Use Cases

* Stay updated with current events quickly
* Summarize multiple news articles efficiently
* Research and information gathering
* Content curation and analysis

## 🔮 Future Improvements

* Multi-article comparative summaries
* Sentiment analysis
* Web interface
* Multi-language support
* Summary export to PDF or text files

