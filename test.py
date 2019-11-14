#import pytesseract
#from PIL import Image
#p=pytesseract.image_to_string(Image.open("123.jpg"),lang="eng")
#print(p)


import win32api,win32con

win32api.MessageBox(0, "垫片告警", "警告",win32con.MB_OK|win32con.MB_ICONSTOP)

print('111111111111')
# import pyttsx3
# import time
# # 模块初始化
# engine = pyttsx3.init()
#
# print('准备开始语音播报...')
#
# # 设置要播报的Unicode字符串
# engine.say("垫片报警")
# time.sleep(0.3)
# engine.say("垫片报警")
# time.sleep(0.3)
# engine.say("垫片报警")
#
#
#
# # 等待语音播报完毕
# engine.runAndWait()
