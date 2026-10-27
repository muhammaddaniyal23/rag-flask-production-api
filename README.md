# RAG Flask API
A Retrieval-Augmented Generation API built with Flask, FAISS, HuggingFace embeddings, and the Groq LLM.
## Overview
This backend provides REST endpoints for document management (upload, list, delete) and retrieval-augmented query answering over uploaded PDF and text documents.
## API Reference
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/upload` | Ingests a PDF or TXT file into the FAISS vector index |
| `GET` | `/documents` | Lists stored files and metadata |
| `DELETE` | `/delete/<filename>` | Removes a document from storage |
| `GET` | `/health` | Health check endpoint |

1. **Clone repository**
   ```bash
   git clone https://github.com/muhammaddniyal23/rag-flask-production-api.git
   cd rag-flask-production-api

