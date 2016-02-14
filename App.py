def getAllIPs():
    import subprocess
    cmd = "arp | awk {'print $1'}"
    sp = subprocess.Popen(cmd, shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    resultList = sp.stdout.readlines()
    resultList.remove('Address\n')
    return resultList

def sendMsg(msg):
    

def isIPAddrUp():


def getPotentialIPs(allIPs):
    for ipAddr in allIPs:
