# 🚀 ARC Checker – Autonomous Regulatory Compliance Checker

An AI-powered compliance assistant that scans code or configuration files for regulatory violations (HIPAA, SOC2, CMS CoPs, CFR Part 2, etc.) and suggests fixes via GitHub Pull Requests.

ARC Checker helps developers and compliance officers automatically detect sensitive data patterns like SSNs, API keys, passwords, and other potential violations — then explains them in plain English and opens PRs with suggested remediations.

---

## ✅ Features

- 🔍 Scans individual files or entire directories for compliance issues
- 🧠 Uses OpenAI's GPT to analyze if an issue is a real violation
- 📝 Explains findings in simple terms
- 🛠 Suggests fixes based on regulatory guidelines
- 🌐 Opens automated GitHub Pull Requests with the fix
- 🔄 Unique branch naming to avoid conflicts during repeated runs
- ⚙️ Configurable via `config.py` (OpenAI key, GitHub token, standard)
- 📁 Supports multiple compliance standards (HIPAA, SOC2, CMS CoPs)

---

## 📦 Folder Structure

```
arc-checker/
├── main.py                  # Entry point – runs full compliance check
├── config.py                # Stores API keys, repo name, and current compliance standard
├── test_code.py             # Sample file used for testing
│
├── knowledge/
│   ├── regulation_loader.py # Loads JSON rules for each standard
│   └── regulations/
│       ├── hipaa.json
│       ├── soc2.json
│       └── cms_cops.json
│
├── scanner/
│   └── file_scanner.py      # Scans files for keyword matches and secrets
│
└── gh_interface/
    └── pr_generator.py      # Creates GitHub PRs with suggested fixes
```

---

## 🧪 Example Usage

### 1. Set up environment variables:
```bash
# config.py
OPENAI_API_KEY = "your-openai-api-key"
GITHUB_TOKEN = "your-github-token"
REPO_NAME = "your-username/your-repo-name"
COMPLIANCE_STANDARD = "HIPAA"  # or "SOC2", "CMS_CoPs"
```

### 2. Run the checker:
```bash
python main.py
```

### 3. Output:
```
📄 Loading compliance rules for: HIPAA
🔍 Scanning file: test_code.py

🧠 AI Analysis:
Yes, this appears to be a HIPAA violation...

📝 Explanation & Suggested Fix:
According to HIPAA Rule 164.312(a)(1), all electronic protected health information (ePHI) must be encrypted at rest unless stored in a secure environment...

🔗 Suggested Fix Created:
https://github.com/ganelltubbs501/arc-checker/pull/2
```

---

## ⚙ Requirements

Before running, make sure you have installed:

```bash
pip install langchain langgraph langchain-openai pygithub openai detect-secrets
```

Also ensure:
- ✅ You have a GitHub account and repo created
- ✅ Your GitHub token has `repo` permissions
- ✅ You're using Python 3.10+ (LangChain v0.3.x compatible)

---

## 🧩 Configuration

All settings are managed in `config.py`:

```python
OPENAI_API_KEY = "sk-your-openai-key-here"
GITHUB_TOKEN = "ghp-your-github-token-here"
REPO_NAME = "ganelltubbs501/arc-checker"
COMPLIANCE_STANDARD = "HIPAA"
```

You can easily switch to another standard by updating `COMPLIANCE_STANDARD`.

---

## 🧱 Supported Standards

| Standard | Status |
|---------|--------|
| HIPAA   | ✅ Done |
| SOC2    | Coming soon |
| CMS CoPs | Coming soon |
| CFR Part 2 | Coming soon |

Each standard defines its own:
- Keywords to scan for
- Description of the rule
- Checklist of required controls

---

## 🚀 Roadmap

| Feature | Planned |
|--------|----------|
| 📁 Add directory scanning support | Week 2 |
| 📜 Support multiple compliance standards | Week 3 |
| 🧠 Improve LLM prompt for better explanations | Week 3 |
| 💡 Add logging and traceability | Week 4 |
| 🧪 Write unit tests | Week 4 |
| 🌐 Create web interface (Streamlit or FastAPI) | Week 5 |
| 🧩 Integrate into GitHub Actions for CI/CD | Week 6 |

---

## 🤝 Contributing

Contributions are welcome! If you'd like to help improve or expand support for more standards, feel free to fork, submit PRs, or report issues.

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 👥 Contact

Ganell Tubbs – [@ganelltubbs501](https://github.com/ganelltubbs501)

Project Link: https://github.com/ganelltubbs501/arc-checker

---

> 🎯 Let me know if you want me to generate badges (like license, build status), add installation instructions, or include contribution guidelines — I’ll update the README accordingly!

Would you like me to:
1. Add badges (license, build, version)?
2. Include a "Getting Started" section?
3. Generate a `.gitignore` and `requirements.txt`?

Let me know how you’d like to proceed — I’m here to guide you every step of the way!
