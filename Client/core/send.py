from hashlib import md5
from Client.message import *
from Client.core import client, crypto

def sendChat(to, ciphertext, signature):
    client.send(ChatMessage({'to_user':to, 'ciphertext':ciphertext, 'signature':signature}).to_dict())

def sendFriendUpdate():
    client.send(FriendUpdateMessage().to_dict())

def sendFriendRequest(friend_name):
    client.send(FriendRequestMessage({'friend_name':friend_name}).to_dict())

def sendAcceptFriend(friend_name, accept):
    client.send(FriendAcceptMessage({'friend_name':friend_name, 'accept':accept}).to_dict())

def sendAuthMessage(username, password):
    password = md5(password.encode()).hexdigest()
    client.send(AuthRequestMessage({'username':username, 'password':password}).to_dict())

def sendRegisterMessage(username, password):
    password = md5(password.encode()).hexdigest()
    client.send(RegisterRequestMessage({'username':username, 'password':password}).to_dict())

def sendCertificateSigningRequestMessage(csr):
    client.send(CertificateSigningRequestMessage({'csr':csr}).to_dict())

def sendCertificateRequestMessaage(username):
    client.send(CertificateRequestMessage({'request_user':username}))
