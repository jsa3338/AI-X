import xlwings as xw
from dotenv import load_dotenv
from openai import OpenAI
from naverOpenai import get_openai_shopping_analysis
load_dotenv()
# 1. excel 열기
wb = xw.Book('genai_rpa.xlsx')

get_openai_shopping_analysis(wb)