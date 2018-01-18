import os
import subprocess
from subprocess import Popen 

cmd1 = 'cd nwdir| wget "https://safebooru.org/index.php?page=post&s=view&id=2429568"'
# os.popenの方はcmd1成功、subprocess.call, Popenだとエラー
#fo = os.popen(cmd1)
fo = Popen(cmd1)
print(fo)

# エラー
#proc = subprocess.call(cmd.strip().split(" "))
