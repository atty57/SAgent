
# 🧠 StudyAgent

> An AI-powered Jupyter-based assistant that extracts key concepts from academic PDFs, generates study guides, quizzes, and even study plans.

---

## ✨ Features

- 🔍 **PDF Parsing** and key concept extraction
- 📄 **Summarization** and **Quiz generation** via LLMs
- 🧪 **Validation** with BERTScore
- 🗓️ **Study Planner** with optional .ics export
- 📚 Ideal for students and researchers

---

## 🧰 Tech Stack

- [CrewAI](https://github.com/joaomdmoura/crewai)
- [Langchain + Ollama](https://ollama.com)
- Sentence Transformers (for chunking)
- BERTScore (for summary validation)
- Python, Jupyter, VS Code

---

## 🚀 Quickstart

```bash
git clone https://github.com/yourusername/studyagent.git
cd studyagent
pip install -r requirements.txt
```

---

## 📓 Usage

Run the `Study_Assistant.ipynb` notebook.  
Upload your own PDF and follow the instructions.

---

## 📸 Screenshots

Add these in `/assets` and show agent flow, PDF chunks, results, and calendar generation.

---

## 🙌 Contribution

PRs are welcome! Fork the repo and submit improvements.

---

## 📜 License

MIT


---
## 📸 Visual Walkthrough
Below are some screenshots to showcase the StudyAgent outputs:

### 🧠 Multi-Agent Execution
![Agent Flow](assets/agents_flow.png)

### 🧾 Structured Content from PDFs
![Content Chunking](assets/content_chunking.png)

### 📚 Summary & Quiz Output
![Study Output](assets/summary_output.png)

### 🗓️ Study Plan Calendar
![Calendar](assets/calendar_plan.png)
