from PIL import Image
import glob
import pickle
import numpy as np
import os
import math
import json

def main():
  tag_idx = pickle.loads(open('tag_idx.pkl', 'rb').read())
  target_size = (224, 224)
  
  # ひまわりで動かす想定のパス: '/mnt/sda/alt-i2v/datasetdownload/imgs/*'
  for name in glob.glob('/mnt/sda/alt-i2v/datasetdownload/imgs/*.txt')[:500000]:
    img_name = name.replace('.txt', '.jpg')

    if not os.path.exists(img_name):
      continue

    pkl_name = '/home/asano/repos/illustration2vec/pkl/{}.pkl'.format(img_name.split('/').pop().replace('.jpg', ''))

    if os.path.exists(pkl_name):
      continue
    try:
      img = Image.open(img_name)
      img = img.convert('RGB')
    except OSError as e:
      continue

    w, h = img.size

    if w > h:
      blank = Image.new('RGB', (w, w))
    elif h >= w:
      blank = Image.new('RGB', (h, h))

    blank.paste(img, (0, 0))
    blank = blank.resize(target_size)
    img_array = np.asarray(blank)
    img_array = img_array / 255.0
    freq_list = [0.0]*len(tag_idx)    

    for tag in open(name).read().split():
      if tag_idx.get(tag) is None:
        continue

      freq_list[tag_idx[tag]] = 1.0
      
      if all(map(lambda x:x==0.0, freq_list)):
        continue

    # ひまわりで実行する場合はパスを変更する
    with open(pkl_name , 'wb') as pkl:
      pkl.write(pickle.dumps((img_array, freq_list)))


if __name__ == '__main__':
  main()


