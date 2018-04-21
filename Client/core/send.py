from hashlib import md5
from Client.message import *
from Client.core import client

def sendChat(to, content):
    client.send(ChatMessage({'to_user':to, 'content':content}).to_dict())

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
