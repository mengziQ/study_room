import zipfile 
import re

# 参考
# https://gist.github.com/GINK03/16a75b5ec160c04bede676b6db4760a9

# まずはtsv一個加工するところから
unziped_file = zipfile.ZipFile('/home/ubuntu/repos/StormRuler/server/download/YSS_AUDIT_LOG_589429-20180112-092307469-92-201709.tsv.zip')
name = unziped_file.namelist().pop()
opened_file = unziped_file.open(name)

# ヘッダ行を取り出し→バイト文字列をutf-8に変換→両端から空白を除去
head = next(opened_file).decode().strip()
#print(head)

# 両端の"を削除
keys = [re.sub('"','',ent) for ent in head.split('"\t"')]

past_event = ""

for f in opened_file:
  line = f.decode().strip()
  vals = [re.sub('"', '', l) for l in line.split('"\t"')]
  # キーバリューの辞書を作る
  obj = {key:val for key, val in zip(keys, vals) if val != '' and key not in ['アカウント名', 'キャンペーン名', 'キーワードID'] }
  account_id = obj['アカウントID']; del obj['アカウントID']
  #print(obj)
  day = obj['日時']; del obj['日時']
  #print(obj) 
  
  # なんでキャンペーンだけtryで囲ったのか
  try:
    campaign_id = obj['キャンペーンID']; del obj['キャンペーンID']
    before = obj['更新前']
  except:
    campaign_id = None
    before = None

  event = obj['イベントタイプ']
  after = obj['更新後']
  
  # キーを'アカウントID', '日時', 'キャンペーンID'にする
  key = (account_id, day, campaign_id)
  # どのようなイベントがあるか見てみます
  if past_event != event:
    print(event, before, after)
  
  past_event = event

  # 差額の計算
  

  

