import socket
from socket import AF_INET
from socket import SOCK_STREAM

# 创建基于http协议的socket对象.
# AF_INET和SOCK_STREAM是默认值,可以省略不写.
s_http = socket.socket(AF_INET, SOCK_STREAM)

# 主机(域名或ip)和端口.
host = "g.cn"
port = 80

# 使用connect方法连接主机,参数是一个tuple.
s_http.connect((host, port))

# 连接完成后,可以通过getsockname方法得到本机的ip和port.
ip, port = s_http.getsockname()
print("本机ip：{0}和port：{1}".format(ip, port))

# 构建一个http请求:
http_request = "GET / HTTP/1.1\r\nhost:{}\r\n\r\n".format(host)

# 发送 HTTP 请求给服务器
# send 函数只接受 bytes 作为参数
# str.encode 把 str 转换为 bytes, 编码是 utf-8.
request = http_request.encode('utf-8')
print('请求', request)
s_http.send(request)

# 接受服务器的响应数据
# 参数是长度, 这里为 1023 字节
# 所以这里如果服务器返回的数据中超过 1023 的部分你就得不到了.
response = s_http.recv(1023)

# 输出响应的数据, bytes 类型
print('响应', response)
# 转成str类型再输出.
print("响应的str类型格式:\n",response.decode('utf-8'))










