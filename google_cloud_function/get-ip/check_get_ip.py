# https://github.com/GINK03/google-cloud-function-pythonic/blob/master/gcf-pythonic-ip-shotgun/check_shotgun.py
import concurrent.futures
import os
import json
import subprocess

ips = []

def _map1(nums):
  ip = os.popen('curl -s https://us-central1-machine-learning-173502.cloudfunctions.net/getip').read()
  #sub = subprocess.Popen('curl -s https://us-central1-machine-learning-173502.cloudfunctions.net/getip'.split(), stdout=subprocess.PIPE, stderr=None)
  #ip = sub.communicate()
  #print('ip', nums, ip[0])
  print('ip', nums, ip)
  ips.append(ip)
  return ip

nums = [i for i in range(10)]
# スレッド∈プロセス。conccurent.futuresはスレッドを分割することもできるし、プロセスを分割することもできる。
# ThreadPoolExecutorはスレッドを分ける
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as exe:
  exe.map(_map1, nums)

open('ips.json', 'w').write(json.dumps(ips, indent=2))

