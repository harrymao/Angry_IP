import webbrowser
from IP import *
demo_html = 'demo.html'
f = open(demo_html,'w')
str1 = 'http://'+result[0][0]+'/image_monitor1/'
str2 = result[0][1]
message = """
<html>
<head></head>
<body>
<table border="1">
  <tr>
    <th><a href=%s>SN8X0091ホームページ</a></th>
    <th>%s</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>
</body>
</html>
"""%(str1,str2)
f.write(message) 
#关闭文件
f.close()
#运行完自动在网页中显示
webbrowser.open(demo_html,new = 1)