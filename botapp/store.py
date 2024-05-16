from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from pymongo import MongoClient
import dbconnection

embeddings = OpenAIEmbeddings(openai_api_key = dbconnection.openai_key)

client = MongoClient(dbconnection.mongodb_conn_string)
collection = client[dbconnection.db_name][dbconnection.collection_name]

docs = MongoDBAtlasVectorSearch.from_documents(embeddings,collection)

