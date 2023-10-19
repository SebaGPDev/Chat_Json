from fastapi import FastAPI
from pydantic import BaseModel
from langchain.document_loaders import JSONLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


class Query(BaseModel):
    prompt: str


@app.post("/query")
async def run_query(query: Query):
    # Crear una instancia de JSONLoader y cargar el archivo JSON
    loader = JSONLoader(
        file_path="./data.json", jq_schema=".campos[]", text_content=False
    )
    documents = loader.load()

    # Dividir los documentos en fragmentos de texto
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    # Crear embeddings y Chroma para la búsqueda de documentos
    embeddings = OpenAIEmbeddings()
    docsearch = Chroma.from_documents(texts, embeddings)

    # Crear una instancia de QA para la recuperación de respuestas
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=docsearch.as_retriever(search_kwargs={"k": 1}),
    )

    # Usar 'qa' para hacer preguntas y obtener respuestas basadas en los documentos
    result = qa.run(query.prompt)

    print(query.prompt)

    return {"result": result}
