# from selenium import webdriver
# from PIL import Image
# from imooc_selenium.ShowapiRequest import ShowapiRequest
# import time
#
# #
# driver = webdriver.Chrome()
# driver.get('http://ht.test.by-998.com/index/login')
# driver.implicitly_wait(10)
# driver.maximize_window()
# #输入用户名密码登录
# title = driver.title
# print(title)
# # time.sleep(3)
# # driver.find_element_by_name('username').send_keys('leon2017')
# #
# # driver.find_element_by_name('password').send_keys('passnew2017')
# #
# # driver.find_element_by_id('login').click()
# # time.sleep(2)
# # driver.find_element_by_class_name('layui-layer-btn0').click()
#
# print(driver.find_element_by_class_name('login-box-msg').text)
# #
#
# # #保存网站中的图片
# # driver.save_screenshot('E:/LX_selenium/imgs.png')
# # #定位到验证码的元素
# # code_element = driver.find_element_by_id('registerYzmImg2')
# # #获取到验证码的坐标
# # print(code_element.location)
# # left = code_element.location['x']
# # top = code_element.location['y']
# # #获取到验证码的长度高度
# # print(code_element.size)
# # height = code_element.size['height']+top
# # right = code_element.size['width']+left
# # #进行定位切割取出验证码图片
# # im = Image.open('E:/LX_selenium/imgs.png')
# # img = im.crop((left,top,right,height))
# # img.save('E:/LX_selenium/code.png')
# # #调用第三方api识别验证码
# # r = ShowapiRequest("http://route.showapi.com/184-4","98314","ce1063b0ba9f4f9297aef637eb905c95" )
# # r.addBodyPara("image", "")
# # r.addBodyPara("typeId", "34")
# # r.addBodyPara("convert_to_jpg", "0")
# # r.addBodyPara("needMorePrecise", "0")
# # r.addFilePara("image", "E:/LX_selenium/code.png") #文件上传时设置
# # res = r.post()
# # # print(type(res.text)) # 返回信息
# # result = res.json()['showapi_res_body']['Result']
# # print(result)
# # time.sleep(3)
# # driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[3]/input').send_keys(result)
#
#
#
#
#
# #关闭浏览器,不然每次打开浏览器都会占内存使打开变慢
# driver.close()

# import xlrd
#
# data = xlrd.open_workbook(r'E:\LX_selenium\config\case.xls')
# sheet = data.sheet_by_index(0)
# print(sheet.nrows)
# print(sheet.row_values(1))

key = 'element=class>layui-layer-content'
by = key.split('=')

print(by)










