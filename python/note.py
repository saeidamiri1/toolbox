def uppload_via_github(url): 
    import sys
    import os 
    import requests
    r = requests.get(url)
    file_name=os.path.basename(url).split('/')[-1]
    with open(file_name, 'w') as f:
        f.write(r.text)
    exec(f"import {file_name.split('.')[-2]}")

url='https://raw.githubusercontent.com/saeidamiri1/toolbox/main/python/utils.py'
uppload_via_github(url)

# fi=unction in utils: 
# file_parts(path0), reload_frompath(module0,path0)
   
 

