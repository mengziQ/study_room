import glob
import pickle
import random

def main():
  tag_freq = {}
  
  # ひまわりのパス/mnt/sda/alt-i2v/datasetdownload/imgs/*.txt
  for name in glob.glob('/mnt/sda/alt-i2v/datasetdownload/imgs/*.txt')[:500000]:
    for tag in open(name).read().split():
      if tag_freq.get(tag) is None:
        tag_freq[tag] = 0
      tag_freq[tag] += 1

  tag_idx = {}
  tags = [tag for tag, freq in sorted(tag_freq.items(), key=lambda x:x[1]*-1)[:5000]]
  random.shuffle(tags)

  for tag in tags:
    tag_idx[tag] = len(tag_idx)

  open('tag_idx.pkl', 'wb').write(pickle.dumps(tag_idx))


if __name__ == '__main__':
  main()
