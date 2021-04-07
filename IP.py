from scapy.all import *
import sys,getopt,socket
import sys
import webbrowser

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
        res = srp1(arpPkt,timeout=0.2,verbose=0)
        if res:
            if res.hwsrc == "70:66:55:76:65:87":
                #result.append({"localIP":res.psrc,"mac":res.hwsrc})
                result.append([res.psrc,res.hwsrc])
                #url = res.psrc + '/image_monitor1/'
                #IEPath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                #webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(IEPath))
                #webbrowser.get('chrome').open(url,new=1,autoraise=True)
                
    return result

result = get_vlan_ip_and_mac()

print(result[0][0])
