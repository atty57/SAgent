
---

```markdown
# 🧠 StudyAgent

> An AI-powered assistant that extracts key concepts from academic PDFs, generates study guides, quizzes, and personalized study plans.

---

## ✨ Features

- 🔍 **PDF Parsing:** Extracts and chunks PDF text into semantic clusters.
- 📝 **Content Generation:** Uses specialized AI agents to produce summaries, quiz questions, and study guides.
- 📈 **Validation:** Evaluates output quality with BERTScore.
- 🗓️ **Study Planner:** Optionally generates study calendars in iCalendar format.
- 📚 Perfect for students and researchers!

---

## 🧰 Tech Stack

- **CrewAI:** Multi-agent framework
- **LLaMA 3 via Ollama:** Language model integration
- **Sentence Transformers:** For text embeddings and clustering
- **BERTScore:** For validating summaries
- **Python, Jupyter, VS Code**

---

## 🚀 Quickstart

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/studyagent.git
cd studyagent
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📓 Usage

### Running the Jupyter Notebook in VS Code

1. **Open the Project in VS Code:**  
   Open the folder containing the project.

2. **Activate the Virtual Environment:**  
   Use the integrated terminal to activate your virtual environment (see Quickstart above).

3. **Run the Notebook:**  
   - Open `notebooks/Study_Assistant.ipynb` in VS Code.
   - Use the built-in Jupyter extension to run the cells sequentially.
   - **Note:** Ensure that the environment variable `OLLAMA_HOST` is set correctly (see next section).

---

## 🖥️ Running on Windows

For Windows users, follow these steps:

1. **Install VS Code & Python:**  
   Download and install [Visual Studio Code](https://code.visualstudio.com/) and [Python](https://www.python.org/downloads/).

2. **Clone the Repository and Set Up the Environment:**  
   Follow the Quickstart instructions above to clone the repo, create a virtual environment, and install dependencies.

3. **Install and Run Ollama on Windows:**  
   - Visit [https://ollama.com/download](https://ollama.com/download) and download the Windows installer (`OllamaSetup.exe`).
   - Run the installer and follow the setup wizard.
   - After installation, open a new Command Prompt or PowerShell window and run:
     ```powershell
     ollama pull llama3
     ollama run llama3
     ```
   - **Keep this terminal running** as it starts the Ollama server at `http://127.0.0.1:11434`. The StudyAgent project will connect to this server.

4. **Run the Notebook:**  
   Open `Study_Assistant.ipynb` in VS Code and run the cells. Your notebook should now process PDFs and run your multi-agent workflow using the locally running Ollama server.

---

---

## 🙌 Contribution

Contributions are welcome! Fork the repo, create a branch, and submit a pull request with your improvements.

---

## 📜 License

This project is licensed under the MIT License.

