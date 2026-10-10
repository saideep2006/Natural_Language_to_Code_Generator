# 🚀 Natural Language to Code Generator

### Week 1 — AI Coding Agent Internship | SkillAudit.ai

A Python-based command-line tool that converts plain-English task descriptions into Python code using Large Language Models (LLMs). It integrates with Groq for cloud-based code generation and supports Ollama for local model inference. Generated code is displayed in the terminal and saved automatically to Python files.

## 📌 Project Overview

Writing code for small programming tasks can be repetitive. This project demonstrates how AI can help developers generate code by describing what they want in natural language.

For example, instead of manually writing a prime-number checker, a user can enter:

`write a function that checks if a number is prime`

The application sends the task to an LLM, receives generated Python code, cleans the response, prints it in the terminal, and saves it to a `.py` file.

## 🎯 Objectives

- Build a Python CLI tool for natural-language-to-code generation.
- Integrate an LLM through the Groq API.
- Support local model inference using Ollama.
- Design a system prompt that requests code-only responses.
- Remove Markdown code fences from generated responses.
- Print generated code to the terminal.
- Automatically save generated code to Python files.
- Demonstrate the generator with eight programming tasks covering strings, mathematics, lists, and dictionaries.

## ✨ Features

- **Natural-language input:** Describe programming tasks using plain English.
- **AI-powered code generation:** Generate Python code using an LLM.
- **Multiple inference options:** Use Groq or configure Ollama for local inference.
- **Code-only prompting:** Instruct the model to return code without explanations or Markdown fences.
- **Response cleanup:** Remove common Markdown code fences when present.
- **Automatic file saving:** Save generated programs as `.py` files.
- **Custom output filename:** Choose an output filename when needed.
- **Demo mode:** Run predefined programming tasks to demonstrate the generator.
- **Command-line interface:** Use the tool directly from the terminal.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Groq API | Cloud-based LLM integration |
| Ollama | Local LLM inference option |
| Python CLI | User interaction through the terminal |
| argparse | Command-line argument handling |
| python-dotenv | Environment variable configuration |
| pathlib | File and path management |
| re | Regular expressions for response cleanup |
| Git | Version control |
| GitHub | Repository hosting and project documentation |
| VS Code | Development environment |

## ⚙️ How It Works

The generator follows this workflow:

1. The user enters a programming task in natural language.
2. The application receives the task through the command line.
3. A system prompt instructs the LLM to return only Python code.
4. The configured model generates a response.
5. The application removes common Markdown code fences.
6. The generated code is printed in the terminal.
7. The generated code is saved to a `.py` file.

```text
Natural-Language Task
        |
        v
Python CLI
        |
        v
System Prompt + User Task
        |
        v
Groq API / Ollama
        |
        v
Generated Python Code
        |
        v
Response Cleanup
        |
        +-------------------+
        |                   |
        v                   v
Terminal Output       Python File
```

## 📂 Project Structure

```text
Natural_Language_to_Code_Generator/
│
├── generator.py
├── generated_output.py
├── generated_output_1.py
├── generated_output_2.py
├── generated_output_3.py
├── generated_output_4.py
├── generated_output_5.py
├── generated_output_6.py
├── generated_output_7.py
├── generated_output_8.py
├── .gitignore
└── README.md
```

The generated output files demonstrate code produced for different programming tasks.

A `.env` file may be used locally for API configuration. It should not be committed to the public repository.

## 🚀 Installation and Setup

### Prerequisites

- Python 3.10 or newer recommended
- pip
- A Groq API key for Groq-based generation
- Ollama installed if you want to use a local model

### 1. Clone the repository

```bash
git clone https://github.com/saideep2006/Natural_Language_to_Code_Generator.git
cd Natural_Language_to_Code_Generator
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install groq python-dotenv
```

### 4. Configure the Groq API key

Create a `.env` file in the project directory:

```dotenv
GROQ_API_KEY=your_actual_groq_api_key_here
```

Get your API key from [Groq Console](https://console.groq.com/).

Keep your API key private. Never commit `.env` to GitHub.

### 5. Generate Python code

Example: generate a prime-number checker.

```bash
python generator.py "write a function that checks if a number is prime"
```

Example: generate a string-reversal function.

```bash
python generator.py "write a function that reverses a string"
```

Example: specify an output filename.

```bash
python generator.py "write a function that reverses a string" --output reverse_string.py
```

### 6. Run the demo

```bash
python generator.py --demo
```

The demo runs the predefined programming tasks supported by the application and saves generated outputs.

**Note:** These commands reflect the current command-line interface. If a command behaves differently in your local environment, check `python generator.py --help` for the available arguments.

## 🧪 Programming Tasks Demonstrated

The project includes eight example tasks covering common Python programming concepts.

| No. | Category | Example task |
|---:|---|---|
| 1 | String handling | Reverse a string |
| 2 | String handling | Check whether a string is a palindrome |
| 3 | String handling | Count vowels in a string |
| 4 | Mathematics | Check whether a number is prime |
| 5 | Mathematics | Calculate a factorial |
| 6 | List operations | Find the largest number in a list |
| 7 | List operations | Remove duplicates from a list |
| 8 | Dictionary operations | Count word frequencies |

These tasks demonstrate the variety of programming requests the generator is designed to handle. Generated results should be reviewed and tested to confirm correctness.

## 💻 Example Output

**Input**

```text
write a function that reverses a string
```

**Possible generated Python code**

```python
def reverse_string(text):
    return text[::-1]
```

**Expected terminal behavior**

```text
Generated Python code:

def reverse_string(text):
    return text[::-1]

Code saved successfully.
```

The exact generated code and terminal messages may vary depending on the model and the implementation.

## ⚡ Efficiency and Benefits

- **Faster first drafts:** Generate an initial implementation from a plain-English instruction.
- **Simple workflow:** No graphical interface is required.
- **Reusable code:** Save generated programs as separate Python files.
- **Flexible input:** Handle different introductory programming tasks using the same CLI.
- **Cloud or local inference:** Choose an API-based model or a compatible local Ollama model.
- **Extensible architecture:** Provides a starting point for more advanced coding-agent capabilities.

### Limitations

- Generated code may contain logical errors or fail edge cases.
- The quality of results depends on the model and prompt.
- Groq generation requires internet connectivity and is subject to API availability and usage limits.
- Local Ollama inference requires Ollama and a compatible model to be installed and running.
- The generator does not independently prove that generated code is correct.
- AI-generated programs should be reviewed and tested before being used in important applications.

This Week 1 project focuses on code generation and saving output. Automated execution, test-driven correction, and multi-file editing are planned for subsequent stages.

## 🔐 Security Considerations

- Store API credentials in environment variables rather than hardcoding them.
- Exclude `.env` and `.venv/` through `.gitignore`.
- Do not publish API keys or other secrets.
- Review generated code before running it.
- Do not treat AI-generated code as trusted solely because it was generated successfully.

## 📚 Key Learnings

Through this project, I explored:

- Integrating LLMs into Python applications.
- Working with API-based code generation.
- Designing system prompts for structured output.
- Handling generated text and Markdown cleanup.
- Building command-line interfaces with `argparse`.
- Managing environment variables with `python-dotenv`.
- Saving generated code to files.
- Organizing and documenting a GitHub project.

## 🔮 Future Improvements

This project is the foundation for developing a more capable AI coding agent.

- **Week 2 — Execute, Observe, Self-Correct:** Execute generated code in a separate subprocess, capture errors, and attempt corrections.
- **Week 3 — Multi-File Context:** Read existing project files and coordinate changes across multiple files.
- **Week 4 — Portfolio Coding Agent:** Combine project analysis, code generation, safe test execution, correction attempts, logging, and a dry-run mode.

The long-term goal is to understand and implement the core workflow behind AI coding agents.

## 👨‍💻 Author

**Sai Deep**

AI Coding Agent Internship — SkillAudit.ai

- **GitHub:** [saideep2006](https://github.com/saideep2006)
- **Project Repository:** [Natural Language to Code Generator](https://github.com/saideep2006/Natural_Language_to_Code_Generator)

## 📄 License

This project is intended for educational and portfolio purposes. A license can be added if the project is distributed for reuse.
