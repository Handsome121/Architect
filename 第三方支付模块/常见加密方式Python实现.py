"""
常见加密方式及Python实现
"""
# print('南北'.encode())
# print(b'\xe5\x8d\x97\xe5\x8c\x97'.decode())

# 利用binascii模块可以将十六进制显示的字节转换成我们在加解密中更常用的显示方式
# import binascii
#
# print(binascii.b2a_hex('南北'.encode()))
# print(binascii.a2b_hex(b'e58d97e58c97'))
# print(binascii.a2b_hex(b'e58d97e58c97').decode())



# URL编码
# from urllib import parse
# quote()方法会自动将str转换成bytes，所以这里传入str和bytes都可以
# print(parse.quote('南北'))
# print(parse.unquote('%E5%8D%97%E5%8C%97'))



# Base64编码
# import base64
# print(base64.b64encode(b'hello world'))
# print(base64.b64decode(b'aGVsbG8gd29ybGQ='))



# MD5(信息-摘要算法)
# 压缩性：任意长度的数据，算出的MD5值长度都是固定的。
# 容易计算：从原数据计算出MD5值很容易。
# 抗修改性：对原数据进行任何改动，哪怕只修改1个字节，所得到的MD5值都有很大区别。
# 强抗碰撞：已知原数据和其MD5值，想找到一个具有相同MD5值的数据（即伪造数据）是非常困难的。
# 不可逆性：每个人都有不同的指纹，看到这个人，可以得出他的指纹等信息，并且唯一对应，但你只看一个指纹，是不可能看到或读到这个人的长相或身份等信息。
# 举个栗子：世界上只有一个我，但是但是妞却是非常非常多的，以一个有限的我对几乎是无限的妞，所以可能能搞定非常多（100+）的妞，这个理论上的确是通的，可是实际情况下....
# import hashlib
#
# # 待加密信息
# str = '这是一个测试'
# # 创建md5对象
# h1=hashlib.md5()
# # 此处必须声明encode
# h1.update(str.encode(encoding='utf-8'))
# print('MD5加密前为 ：' + str)
# print('MD5加密后为 ：' + h1.hexdigest())



# Python加密库PyCryptodome
# import Cryptodome



# DES
# DES算法为密码体制中的对称密码体制，又被称为美国数据加密标准。
# DES是一个分组加密算法，典型的DES以64位为分组对数据加密，加密和解密用的是同一个算法。
# DES算法的入口参数有三个：Key、Data、Mode。其中Key为7个字节共56位，是DES算法的工作密钥；Data为8个字节64位，是要被加密或被解密的数据；Mode为DES的工作方式,有两种:加密或解密。
# 密钥长64位，密钥事实上是56位参与DES运算（第8、16、24、32、40、48、56、64位是校验位，使得每个密钥都有奇数个1），分组后的明文组和56位的密钥按位替代或交换的方法形成密文组。

# 导入DES模块
# from Cryptodome.Cipher import DES
# import binascii

# 导入DES模块
# from Cryptodome.Cipher import DES
# import binascii
#
# # 这是密钥
# key = b'abcdefgh'
# # 需要去生成一个DES对象
# des = DES.new(key, DES.MODE_ECB)
# # 需要加密的数据
# text = 'python spider!'
# text = text + (8 - (len(text) % 8)) * '='
#
# # 加密的过程
# encrypto_text = des.encrypt(text.encode())
# encrypto_text = binascii.b2a_hex(encrypto_text)
# print(encrypto_text)







# 3DES
# 3DES（或称为Triple DES）是三重数据加密算法（TDEA，Triple Data Encryption Algorithm）块密码的通称。它相当于是对每个数据块应用三次DES加密算法。
# 由于计算机运算能力的增强，原版DES密码的密钥长度变得容易被暴力破解。3DES即是设计用来提供一种相对简单的方法，即通过增加DES的密钥长度来避免类似的攻击，而不是设计一种全新的块密码算法。
# 3DES（即Triple DES）是DES向AES过渡的加密算法（1999年，NIST将3-DES指定为过渡的加密标准），加密算法，其具体实现如下：设Ek()和Dk()代表DES算法的加密和解密过程，K代表DES算法使用的密钥，M代表明文，C代表密文，这样：
# 3DES加密过程为：C=Ek3(Dk2(Ek1(M)))
# 3DES解密过程为：M=Dk1(EK2(Dk3(C)))







# AES
# 高级加密标准（英语：Advanced Encryption Standard，缩写：AES），在密码学中又称Rijndael加密法，是美国联邦政府采用的一种区块加密标准。
# 这个标准用来替代原先的DES，已经被多方分析且广为全世界所使用。经过五年的甄选流程，
# 高级加密标准由美国国家标准与技术研究院（NIST）于2001年11月26日发布于FIPS PUB 197，并在2002年5月26日成为有效的标准。2006年，
# 高级加密标准已然成为对称密钥加密中最流行的算法之一。
# from Cryptodome.Cipher import AES
# from Cryptodome import Random
# from binascii import b2a_hex
#
# # 要加密的明文
# data = '南来北往'
# # 密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
# # 目前AES-128足够用
# key = b'this is a 16 key'
# # 生成长度等于AES块大小的不可重复的密钥向量
# iv = Random.new().read(AES.block_size)
#
# # 使用key和iv初始化AES对象, 使用MODE_CFB模式
# mycipher = AES.new(key, AES.MODE_CFB, iv)
# # 加密的明文长度必须为16的倍数，如果长度不为16的倍数，则需要补足为16的倍数
# # 将iv（密钥向量）加到加密的密文开头，一起传输
# ciphertext = iv + mycipher.encrypt(data.encode())
#
# # 解密的话要用key和iv生成新的AES对象
# mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
# # 使用新生成的AES对象，将加密的密文解密
# decrypttext = mydecrypt.decrypt(ciphertext[16:])
#
#
# print('密钥k为：', key)
# print('iv为：', b2a_hex(ciphertext)[:16])
# print('加密后数据为：', b2a_hex(ciphertext)[16:])
# print('解密后数据为：', decrypttext.decode())




# RSA
# RSA加密算法是一种非对称加密算法。在公开密钥加密和电子商业中RSA被广泛使用。
# 该算法基于一个十分简单的数论事实：将两个大素数相乘十分容易，但那时想要对其乘积进行因式分解却极其困难，因此可以将乘积公开作为加密密钥，即公钥，
# 而两个大素数组合成私钥。公钥是可发布的供任何人使用，私钥则为自己所有，供解密之用。
# import rsa
# import binascii
#
# # 使用网页中获得的n和e值，将明文加密
# def rsa_encrypt(rsa_n, rsa_e, message):
#     # 用n值和e值生成公钥
#     key = rsa.PublicKey(rsa_n, rsa_e)
#     # 用公钥把明文加密
#     message = rsa.encrypt(message.encode(), key)
#     # 转化成常用的可读性高的十六进制
#     message = binascii.b2a_hex(message)
#     # 将加密结果转化回字符串并返回
#     return message.decode()
#
# # RSA的公钥有两个值n和e，我们在网站中获得的公钥一般就是这样的两个值。
# # n常常为长度为256的十六进制字符串
# # e常常为十六进制‘10001’
# pubkey_n = '8d7e6949d411ce14d7d233d7160f5b2cc753930caba4d5ad24f923a505253b9c39b09a059732250e56c594d735077cfcb0c3508e9f
# 544f101bdf7e97fe1b0d97f273468264b8b24caaa2a90cd9708a417c51cf8ba35444d37c514a0490441a773ccb121034f29748763c6c4f76eb0303
# 559c57071fd89234d140c8bb965f9725'
# pubkey_e = '10001'
# # 需要将十六进制转换成十进制
# rsa_n = int(pubkey_n, 16)
# rsa_e = int(pubkey_e, 16)
# # 要加密的明文
# message = '南北今天很忙'

# print("公钥n值长度：", len(pubkey_n))
# print(rsa_encrypt(rsa_n, rsa_e, message))



