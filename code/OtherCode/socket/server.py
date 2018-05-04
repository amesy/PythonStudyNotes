import socket

# 运行这个程序后, 浏览器打开 localhost:4000 就能访问了.

# 服务器的 host 为空字符串, 表示接受任意 ip 地址的连接.
# 指定端口为4000
host = ""
port = 4000

# 创建一个socket实例.
s = socket.socket()

# bind方法用于绑定host和port，参数是一个tuple.
s.bind((host, port))

# 使用无限循环来持续接收客户端的请求.
while True:
    # 限制一个时刻服务器最多接收的客户端数量.
    s.listen(5)

    print("等待客户端连接中...")

    # 当有客户端过来连接的时候, s.accept 函数就会返回 2 个值,分别是 连接 和 客户端 ip 地址.
    connection, address = s.accept()
    # recv方法用来接收客户端发送过来的数据,参数是要接收的字节数,返回值是一个 bytes 类型.
    request = connection.recv(1024)
    print("ip and request, {}\n{}".format(address,request.decode()))
    # 处理http请求,通过sendall方法发送给客户端.
    response = b"HTTP/1.1 200 hao\r\n\r\n<h1>Hello World!</h1>"
    connection.sendall(response)
    # 关闭连接.
    connection.close()