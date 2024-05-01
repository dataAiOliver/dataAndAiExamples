import streamlit as st
import os
import os.path

from dotenv import load_dotenv
from llama_index.core.response.pprint_utils import pprint_response
from llama_index.llms.openai import OpenAI
from llama_index.core import SQLDatabase, ServiceContext

from llama_index.core.query_engine import NLSQLTableQueryEngine

from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, select


def get_engine(user = 'postgres', password = 'dummy', host = 'localhost', port = '5432', dbname = 'sqlrag'):

    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    return create_engine(connection_string)

engine = get_engine()
include_tables=["employees", "worked_hours"]
sql_database = SQLDatabase(engine=engine, include_tables=include_tables)
query_engine = NLSQLTableQueryEngine(sql_database=sql_database, tables = include_tables, verbose=True)

query = "Give ma a table of all employees and worked hours."
r = query_engine.query(query)
print(r)