from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import predictor
import utils

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>Sapa Semua - Translator SIBI </h1>
        <p>Websocket endpoint: <code>ws://localhost:8000/ws</code></p>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_json()
            df = utils.records2df(data)
            result = predictor.predict(df)
            await websocket.send_text(result)
        except ValueError:
            await websocket.send_text('Error')
            continue
        except WebSocketDisconnect:
            break
