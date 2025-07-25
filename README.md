

# 🤖 Agentic AI ChatBot

A conversational AI chatbot built to provide intelligent responses and engaging user interactions.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-Latest-green.svg)

## 🌟 Features

- **📄 ChatBot**: Ask anything to this,and it will use its llm knowledge to answer your query.
- **🌐 Web Search Integration**: Real-time information retrieval via Tavily API
- **⚡ Fast LLM Inference**: Powered by Groq's high-speed language models

## 🏗️ Architecture

### Tou can select any of the below three options:
- **Basic Chatbot**: Ask any query
- **Chabot with Web**: Current events, recent information, time-sensitive queries
- **AI News**: Get Daily, Weekly or Monthly news on AI

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Groq API Key ([Get here](https://console.groq.com/))
- Tavily API Key ([Get here](https://tavily.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/arshjitsingh224/chatbot.git
   cd chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Configure API Keys**
   - Enter your Groq API key in the sidebar
   - Enter your Tavily API key in the sidebar

5. **Start Chatting!**
   - Ask questions and watch the answers


## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Orchestration** | LangGraph | Workflow management and conditional routing |
| **UI Framework** | Streamlit | Interactive web interface |
| **LLM** | Groq (Llama 3 70B) | Fast language model inference |
| **Web Search** | Tavily API | Real-time information retrieval |


## ⚙️ Configuration

### Model Configuration
```python
# In app.py - modify these constants
GROQ_MODEL = "llama3-70b-8192"
```
```

### Search Parameters
```python

# Web search
max_results = 2
```

```


## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**




## 🐛 Troubleshooting

### Common Issues

**API Key Errors**
```
Solution: Verify your Groq and Tavily API keys are valid and have sufficient credits
```


**Network Errors**
```
Solution: Check internet connection for web search functionality
```

## 🙏 Acknowledgments

- **LangGraph** for orchestration framework
- **Streamlit** for the amazing UI framework
- **Groq** for fast LLM inference
- **Tavily** for web search capabilities


⭐ **Star this repository if you found it helpful!**

Made with ❤️ by [Arshjit Singh](https://github.com/arshjitsingh224)
