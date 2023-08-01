# Utils
import sys

print(sys.path)
print(sys.executable)

import time
from typing import List

# Langchain
import langchain
from pydantic import BaseModel

print(f"LangChain version: {langchain.__version__}")

# Vertex AI
from google.cloud import aiplatform
from langchain.chat_models import ChatVertexAI
from langchain.embeddings import VertexAIEmbeddings
from langchain.llms import VertexAI
from langchain.schema import HumanMessage, SystemMessage

print(f"Vertex AI SDK version: {aiplatform.__version__}")