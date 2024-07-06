from crewai import Agent, Task, Crew, Process
from crewai_tools import SccrapeWebsiteTool, SerperDevTool
import os 
import streamlit as st
from dotenv import load_dotenv
from docx import Document
from io import BytesIO
import base64


load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

