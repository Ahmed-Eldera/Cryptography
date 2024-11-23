from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import binascii

# RSA Key Generation (Private and Public)
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# RSA Encryption
def encrypt_rsa(public_key, plaintext):
    public_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return binascii.hexlify(ciphertext).decode()  # Return as hex string

# RSA Decryption
def decrypt_rsa(private_key, ciphertext):
    private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key)
    ciphertext = binascii.unhexlify(ciphertext.encode())
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode()

# Example Usage
#private_key, public_key = generate_rsa_keys()
private_key= (
    '-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAuBQj1ziaIqL8iaSDu5yJvlL1QoHANGiZp4orywiBBbNxAfpP\nIX0WxKe5UVfuTWF5MuN00C7RCVfAAfzT/xhGN5suV80HPTged3rfwUvAq263t2gC\nBsJ+1cH4+/LXwJ49XoQD+27sThvuZNEwF1N1YyR7lR51zG463QUVw7sq45WfYx0M\neoYRyanf3pqzFxsIu5g1XRpXk/VG/hK8j1B9MSQnOY841leSEPTJEcMWR3EI4HSa\ntfWcNNTGeNeutoJwKKrxDK0m\n'
    '4oueVF+KD6vy37/kPxMrBd1qoTjkreN/63AjjY31\nsUNy8KwtWl7VPbcWEy4Vk/yZpEcv66YX0WeSawIDAQABAoIBAA+0bYJf1Taon9HB\nHsQTjOTsqvlrnHxcLY/P\n'
    'sqt1zvGE56/617l3CfQ+jbRU7i3dPRE3EAZFmEFVzTne\nL4VktXOVDRUh7EDa2C6VZcsArYVywsB7t9XfziEVQCrZWHLvN959IOHYtYHMfEBP\nC0Kniiz/4H35GqUVr\n'
    '8v03RsqjXQxG1QqL0JDhcKbWixi18ls0EI8ekjMgfuqB7gS\neK20OO+eUni1sMs1nPix9hCCeW8VJvXHnL13O67l6RR8y07JetvT6PQGbsu0XRKA\nisIzTaeg8KQT7P\n'
    'JQE3KaVKGFjqblRm4m8U+haZsx/omBIqSPP85cT9lRlkB0eBS/\nmr1LmdECgYEAz/8Gt6SQ6aB6ENBJgjbS5W8tmweepPlD8ZcAH7wfRKruu+POVvpQ\nBWqKEQJ058\n'
    'uf72TLJW3Ltg/+WXJa8Fk8r4IQAKxbL0gOVUSvHk3mqfMnAICuHAlD\ng/s3GLcARB+b8Z5ZA7zkPbyQT8qIyxraiKg93bXcsqB268y4Jjn4zn0CgYEA4pAA\nkGWgTPd\n'
    'aI71p/6EpkWEEO+WjvTfy5UkPOHyGiPX1WLLvHhJP4bRqOfIpT9XlJsd0\nuGojMTm79ouygTbt8+5sFIyrFquHiUYCCz0Fe3V3ssSgScORLqcV4r3cet4OAbvN\ntX3w\n'
    'OqOwtcBxw21nmbS9FPc9nxG60GlryOSkMQcCgYEAtQ+R72coZte1qtFGTD4h\nVGx1zNDTP1Vl2fbSus1ugr4x2Am0424/Hpfh3HDBB87wSNr7JHfxr2k4xvCPTU7B\nTx\n'
    '7vg0aGkiAtqfiCYOT7eNIcD4n1Bp7h0RBso+0aJDNH8wse/ev+2+c70NnEPtn/\nhpq+UDQyDKU3IIkzfMNWXZkCgYB/ex+WIFjOde/WZGIcYIaPMtO7ED/N3Ilj0nQq\n\n'
    'CId60Uq4GhbKCOvByE5tRIFSVryV0W0vxyj+LcpBs+FBK7NAqktOVMh//QxKhYXo\n5PEMwtATWugGGXC7m3CJIOPKjt+6wf3BvZdKp4hq/FoG6Kx+pGAwR934f3Vqh6cK\n'
    '\nZvysSQKBgQCAA+h0oNUiln7M8lZKnJYoFodc0K7GYGyvDFT1v8wEG/guvoRaMIGr\nEzXlNcyIPsYES2BdEv2RyZ7uRSvz0fCMmgh+fSI4WXzK3dUtWPyTIjarI9GYY\n'
    '4sK\nVOY2CVHkPbjVmzh4j/e99hhsNQeSYfDJIo+W2+QH1mTQjpAQbJENUQ==\n-----END RSA PRIVATE KEY----- ')
public_key= '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuBQj1ziaIqL8iaSDu5yJ\nvlL1QoHANGiZp4orywiBBbNxAfpPIX0WxKe5UVfuTWF5MuN00C7RCVfAAfzT/xhG\nN5suV80HPTged3rfwUvAq263t2gCBsJ+1cH4+/LXwJ49XoQD+27sThvuZNEwF1N1\nYyR7lR51zG463QUVw7sq45WfYx0MeoYRyanf3pqzFxsIu5g1XRpXk/VG/hK8j1B9\nMSQnOY841leSEPTJEcMWR3EI4HSatfWcNNTGeNeutoJwKKrxDK0m4oueVF+KD6vy\n37/kPxMrBd1qoTjkreN/63AjjY31sUNy8KwtWl7VPbcWEy4Vk/yZpEcv66YX0WeS\nawIDAQAB\n-----END PUBLIC KEY----- '
bolbol = encrypt_rsa(public_key.encode(),"adeek t2ol m5adt4")
print(decrypt_rsa(private_key.encode(),bolbol))