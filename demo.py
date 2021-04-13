import webbrowser
#from IP import *
from scapy.all import *
import sys,getopt,socket
#import webbrowser



def get_local_net():
    #获取主机名
    hostname = socket.gethostname()
    #获取主机的局域网ip
    localip = socket.gethostbyname(hostname)
    localipnums = localip.split('.')
    localipnums.pop()
    localipnet = '.'.join(localipnums)
    return localipnet

def get_vlan_ip_and_mac():
    localnet = get_local_net()
    result = []
    for ipFix in range(1,254):
        ip =localnet+"."+str(ipFix)
        #组合协议包
        arpPkt=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
        res = srp1(arpPkt,timeout=1,verbose=0)
        if res:
            if res.hwsrc == "70:66:55:76:65:87":

                #result.append({"localIP":res.psrc,"mac":res.hwsrc})
                result.append([res.psrc,res.hwsrc,"8X0091"])
                #url = res.psrc + '/image_monitor1/'
                #IEPath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                #webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(IEPath))
                #webbrowser.get('chrome').open(url,new=1,autoraise=True)
            if res.hwsrc == "c0:e4:34:b2:81:8b":
                result.append([res.psrc,res.hwsrc,"8X0092"])
            if res.hwsrc == "80:91:33:5d:87:67":
                result.append([res.psrc,res.hwsrc,"8X0093"])
            if res.hwsrc == "70:66:55:76:46:9d":
                result.append([res.psrc,res.hwsrc,"8X0094"])
            if res.hwsrc == "70:66:55:76:5c:01":
                result.append([res.psrc,res.hwsrc,"8X0095"])
                
    return result

result = get_vlan_ip_and_mac()
#print(result)
demo_html = 'demo.html'
f = open(demo_html,'w')
str1 = 'NONE'
str11 = 'NONE'
str111 = 'NONE'
str2 = 'NONE'
str22 = 'NONE'
str222 = 'NONE'
str3 = 'NONE'
str33 = 'NONE'
str333 = 'NONE'
str4 = 'NONE'
str44 = 'NONE'
str444 = 'NONE'
str5 = 'NONE'
str55 = 'NONE'
str555 = 'NONE'

try:
    str1 = 'http://'+result[0][0]+'/image_monitor1/'
    str11 = result[0][1]
    str111 = result[0][2]
    str2 = 'http://'+result[1][0]+'/image_monitor1/'
    str22 = result[1][1]
    str222 = result[1][2]
    str3 = 'http://'+result[2][0]+'/image_monitor1/'
    str33 = result[2][1]
    str333 = result[2][2]
    str4 = 'http://'+result[3][0]+'/image_monitor1/'
    str44 = result[3][1]
    str444 = result[3][2]
    str5= 'http://'+result[4][0]+'/image_monitor1/'
    str55 = result[4][1]
    str555 = result[4][2]
except:
  pass
message = """
<html>
<header>
<h1>Mamos設備一覧</h1>
</header>
<body>
<table border="1">
  <tr>
    <th><a href=%s target='_BLANK'>%s</a></th>
    <th>%s</th>
  </tr>
  <tr>
    <th><a href=%s target='_BLANK'>%s</a></th>
    <th>%s</td>
  </tr>
  <tr>
    <th><a href=%s target='_BLANK'>%s</a></th>
    <th>%s</td>
  </tr>
  <tr>
    <th><a href=%s target='_BLANK'>%s</a></th>
    <th>%s</td>
  </tr>
    <tr>
    <th><a href=%s target='_BLANK'>%s</a></th>
    <th>%s</td>
  </tr>
</table>
</body>
</html>
"""%(str1,str111,str11,str2,str222,str22,str3,str333,str33,str4,str444,str44,str5,str555,str55)
f.write(message) 
#关闭文件
f.close()
#运行完自动在网页中显示
webbrowser.open(demo_html,new = 1)