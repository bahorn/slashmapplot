import pydle

class MyClient(pydle.Client):
    mapresp = []

    async def on_connect(self):
        await super().on_connect()
        await self.rawmsg('MAP')
        
    async def on_unknown(self, msg):
        if msg.command == 6:
            self.mapresp.append(msg.params[1])
        elif msg.command == 7:
            await self.disconnect()

    def getmap(self):
        return '\n'.join(self.mapresp)
