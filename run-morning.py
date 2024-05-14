import os
import datetime
date_str = f"{datetime.datetime.now():%Y-%m-%d}"
print(date_str)
update_str = f'"test update-{date_str}"'
cmds = [
    f'/Users/tuan/miniconda3/envs/ml/bin/python crawl-fl-and-backdoor.py',
    f'git commit -am {update_str}',
    'git push',
]

for cmd in cmds:
    print(cmd)
    os.system(cmd)