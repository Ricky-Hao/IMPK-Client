from hashlib import md5
from .message import *
from .client import client

def sendChat(to, content):
    client.send(ChatMessage({'to':to, 'content':content}).to_dict())

def sendFriendUpdate():
    client.send(FriendUpdateMessage().to_dict())

def sendFriendRequest(friend_name):
    client.send(FriendRequestMessage({'friend_name':friend_name}).to_dict())

def sendAcceptFriend(friend_name, accept):
    client.send(FriendAcceptMessage({'friend_name':friend_name, 'accept':accept}).to_dict())

def sendAuthMessage(username, password):
    password = md5(password.encode()).hexdigest()
    client.send(AuthMessage({'username':username, 'password':password}).to_dict())
