import asyncio
from Client.core.client import Client

client = Client(asyncio.get_event_loop())
client.start()

__all__ = ['client', 'send', 'route', 'crypto']