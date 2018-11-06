import glob 
import sys

for f in glob.glob('./csv/50_new/*'):
    in_f = open(f, 'r')
    file_name = './num/50_new/revise_' + f.replace('./csv/50_new/', '')
    out_f = open(file_name, 'w')

    obj = in_f.readlines()
    for i, o in enumerate(obj):
        splited = o.split(',')
        if len(splited) != 3:
            print(i)
            sys.exit()
        print(splited[2])
        num = splited[2].replace('\n', '')
        out_f.write(num + '\n')
        
