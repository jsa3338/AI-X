from dotenv import load_dotenv
from decouple import config
import os

# 방법1
load_dotenv()
client_id = os.getenv('Client_ID')
client_key = os.getenv('Client_Secret')
print('1 :',client_id)
# 방법2
client_id = config('Client_ID')
print(' :',client_id)