import stream_chat
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

server_client = stream_chat.StreamChat(api_key="d3es7d8cqtjj", api_secret="6njpt68ewpzr24upawpm4rfx8xt3jx9tewjg3pptxtfa295f9bwbfxk2db4faem9")


class Parameters(BaseModel):
    user_name: str

@app.post("/token")
def getPreferences(parameter: Parameters):
    token = server_client.create_token(parameter.user_name)
    return {"token": token}