import hashlib

# 計算字符串的SHA-256
data = "Hello, SHA-256!"
hash_object = hashlib.sha256(data.encode())
hex_dig = hash_object.hexdigest()

print(f"SHA-256哈希值: {hex_dig}")