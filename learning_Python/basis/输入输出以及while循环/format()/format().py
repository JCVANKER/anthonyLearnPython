import math
print('{}网址： "{}!"'.format('走走行', 'www.gogowell.com'))
#位置参数
print('{0}网址： "{1}!"'.format('走走行', 'www.gogowell.com'))
print('"{1}!"： {0}网址'.format('走走行', 'www.gogowell.com'))
#关键字参数
print('{name}网址： "{web}!"'.format(name='走走行',web='www.gogowell.com'))
#位置及关键字参数可以任意的结合
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Gogowell',
                                                       other='Taobao'))
print("-------------------------------------")

# '!a'(使用 ascii()), '!s'(使用 str()) 和 '!r'(使用 repr())可以用于在格式化
# 某个值之前对其进行转化
print('常量 PI 的值近似为： {!r}。'.format(math.pi))

#更多参见：http://www.runoob.com/python3/python3-inputoutput.html
