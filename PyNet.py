from subprocess import Popen, PIPE
import subprocess
#cmd = 'arp | awk {"print $1"}'
cmd="ls"
#sp = subprocess.Popen("arp | awk {'print $1'}", stdout=PIPE)
sp = subprocess.Popen(cmd, stdout=PIPE)
resultList = sp.stdout.readlines()
print resultList
