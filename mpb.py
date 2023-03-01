import ssl

from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'mykeys.json'

SAMPLE_SPREADSHEET_ID = '1ww2UcaIz19H_1MRJLmCLp6UGQMvg1_xg65yrn0uZ0rQ'
SAMPLE_RANGE_NAME = 'Sheet1!A1:E6'

def Test() : 
    # define the scope
    creds = None
    
    ssl._create_default_https_context = ssl._create_unverified_context

    # add credentials to the account
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # authorize the clientsheet 
    service = build('sheets', 'v4', credentials=creds)
	
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
	
    values = result.get('values', [])
	
    print(result)