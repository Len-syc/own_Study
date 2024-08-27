import hashlib

from pyexpat import model

"""
1.md5
2.sha1
3.sha256
4.sha512
"""
"""ep
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
"""
def Return_Hash(Data,model = "md5"):
    if model == "md5":
        return hashlib.md5(Data.encode("utf-8")).hexdigest()
    elif model == "sha1":
        return hashlib.sha1(Data.encode("utf-8")).hexdigest()
    elif model == "sha256":
        return hashlib.sha256(Data.encode("utf-8")).hexdigest()
    elif model == "sha512":
        return hashlib.sha512(Data.encode("utf-8")).hexdigest()


def main():
    while True:
        User_Data = input("Enter Data:")
        if User_Data == "exit":
            break
        User_Model =input("Enter Model:")
        print(Return_Hash(User_Data,User_Model))
if __name__ == '__main__':
    main()