# 📄 Doc-Insight-AI

<div align="center">

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-compose-blue.svg)](https://docs.docker.com/compose/)
[![FastAPI](https://img.shields.io/badge/fastapi-0.110+-green.svg)](https://fastapi.tiangolo.com/)

</div>

---

## 🌟 Introduction

Doc-Insight-AI is an AI-powered document question answering system. It allows users to upload documents and ask questions about their content, receiving accurate, context-aware answers. Built with FastAPI and Docker, this project is designed for extensibility and ease of deployment.

## ✨ Key Features

- **📄 Document Upload & Parsing**: Supports various document types for QnA
- **🤖 AI-Powered QnA**: Uses advanced language models for context-aware answers
- **⚡ FastAPI Backend**: High-performance API for handling requests
- **🐳 Dockerized**: Easy deployment and reproducibility
- **🔒 Environment Variables**: Secure management of secrets and configuration

## 📋 Requirements

- Python 3.11+
- Docker & Docker Compose
- Dependencies listed in `requirements.txt`

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone <your-repo-url>.git
cd End-to-End-Doc-QnA
```

### 2. Build and run with Docker Compose
```bash
docker-compose up -d --build
```

The API will be available at [http://localhost:8000](http://localhost:8000).

### 3. (Optional) Local Development
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## 🏗️ Project Structure

```
End-to-End-Doc-QnA/
├── app/
│   ├── models/
│   │   └── schema.py
│   └── ...
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🛠️ Technologies Used

- **[FastAPI](https://fastapi.tiangolo.com/)**: Web framework for building APIs
- **[Docker](https://www.docker.com/)**: Containerization
- **[Python](https://www.python.org/)**: Core programming language
- **[Uvicorn](https://www.uvicorn.org/)**: ASGI server for FastAPI

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <p>💡 Inspired by <a href="https://github.com/cyclostone/MathSolveX">MathSolveX</a></p>
  <p>⭐ Star this repository if you found it useful!</p>
</div>
