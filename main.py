import pandas as pd
import requests
from io import StringIO 
import re
from mail import send_email


try:

    i = 308


    while i <= 13947:
        url = f'https://iwms.wbb.gov.lk/household/list?province_id=1&district_id=1&division_id=1&gnd_id={i}&lang=en&action=view'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            try:
                tables = pd.read_html(StringIO(response.text))
                
                if tables:
                    combined_table = pd.concat(tables, ignore_index=True)
                    name = list(combined_table['GN'])

                    if name and len(name) > 1:  
                        sanitized_name = re.sub(r'[\\/*?:"<>|]', "", name[3]) 
                        combined_table.to_excel(f"{i}_{sanitized_name}.xlsx", index=False)
                        print(f"Data exported to {i}_{sanitized_name}.xlsx")
                    else:
                        print("No valid GN column data found.")
                else:
                    print("No tables found on the page.")
            except ValueError:
                print("Failed to parse the HTML or no tables found.")
        else:
            print(f"Failed to access the page. Status code: {response.status_code}")
        
        i += 1
except:
    send_email(f"Extraction STOPPED",f"data extraction stopped last GND  is {i}!", "thilacramesh@gmail.com")
