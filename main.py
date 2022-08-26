import stream_chat
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

server_client = stream_chat.StreamChat(api_key="d3es7d8cqtjj", api_secret="6njpt68ewpzr24upawpm4rfx8xt3jx9tewjg3pptxtfa295f9bwbfxk2db4faem9")


class Parameters(BaseModel):
    user_name: str
    id:str

@app.post("/token")
def getPreferences(parameter: Parameters):
    server_client.upsert_user({"id": parameter.id, "name": parameter.user_name})
    token = server_client.create_token(parameter.id)
    return {"token": token}