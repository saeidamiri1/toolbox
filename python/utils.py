def uppload_via_github(url): 
    import sys
    import os 
    import requests
    url = 'https://raw.githubusercontent.com/saeidamiri1/toolbox/blob/main/python/general.py'
    r = requests.get(url)
    file_name=os.path.basename(url).split('/')[-1]
    with open(file_name, 'w') as f:
        f.write(r.text)
    import file_name.split('.')[-2]
    
