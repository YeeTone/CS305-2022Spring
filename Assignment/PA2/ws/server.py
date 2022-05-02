import asyncio
import websockets


class DanmakuServer:
    Connecting = []

    """
    Receive danmakus from clients, reply them correctly
    """

    def __init__(self):
        pass

    async def reply(self, websocket):
        '''
        建立连接后就直接和所有可用的websocket进行广播
        :param websocket: 新传入的websocket用户
        :return: None
        '''
        DanmakuServer.Connecting.append(websocket)
        try:
            while True:
                #if not websocket.closed:
                message = await websocket.recv()
                    # print(message)
                websockets.broadcast(DanmakuServer.Connecting, message)
        finally:
            '''
            处理完成后就关闭相应的连接
            '''
            DanmakuServer.Connecting.remove(websocket)
            websocket.close()
        # raise NotImplementedError

'''
未作修改
'''
if __name__ == "__main__":
    server = DanmakuServer()
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(server.reply, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()
