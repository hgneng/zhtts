import zhtts
import socket
import time 

tts = zhtts.TTS() # use fastspeech2 by default

# 创建一个TCP/IP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器地址和端口号
server_address = ('localhost', 20501)
sock.bind(server_address)

# 监听端口，最大连接数为1
sock.listen(1)

while True:
    print('等待连接...')
    connection, client_address = sock.accept()
    try:
        print('连接来自:', client_address)
        #while True:
        data = connection.recv(1024)
        if data:
            try:
                content = data.decode()
                print('收到数据:', content)
                beginTime = time.time()
                filepath = "/tmp/zhttsOutput.wav"
                tts.text2wav(content, filepath)
                endTime = time.time()
                print('耗时：', endTime - beginTime)
                connection.sendall(filepath.encode())  # 发送数据给客户端
            except UnicodeDecodeError as e:
                print("Caught UnicodeDecodeError:", e)
    finally:
        # 清理连接
        connection.close()
