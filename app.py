import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment or .env file.")


app = Flask(__name__)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.3
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=GEMINI_API_KEY
)

RAG_PROMPT_TEMPLATE = """
You are an expert AI assistant providing accurate answers based on the provided document context.

Context:
{context}

Question:
{question}

Answer concisely and accurately based ONLY on the context above. If the context does not contain enough information to answer, state clearly that you do not know based on the provided context.
"""

prompt = ChatPromptTemplate.from_template(RAG_PROMPT_TEMPLATE)
output_parser = StrOutputParser()

rag_chain = prompt | llm | output_parser

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "Flask Gemini RAG API is up and running."
    }), 200


@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        if not data or 'question' not in data:
            return jsonify({"error": "Missing required field 'question' in JSON payload"}), 400

        user_question = data.get('question')
        provided_context = data.get('context', "No specific context provided.")

        response = rag_chain.invoke({
            "context": provided_context,
            "question": user_question
        })

        return jsonify({
            "success": True,
            "question": user_question,
            "answer": response
        }), 200

    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)