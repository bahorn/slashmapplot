import pydle

class MyClient(pydle.Client):
    async def on_connect(self):
        await super().on_connect()
        await self.rawmsg('LINKS')
        self._links = []
        
    async def on_unknown(self, msg):
        if msg.command == 364:
            link = (msg.params[1], msg.params[2])
            if link[0] != link[1]:
                self._links.append(link)
        elif msg.command == 365:
            await self.disconnect()

    def links(self):
        return self._links
