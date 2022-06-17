import uvicorn
from fastapi import FastAPI
from action import Action
a = Action
app = FastAPI()

@app.get("/")
async def add_restrat():
    data = {"Con":"Start"}
    return data

@app.get("/on_off")
async  def get_on_off(status):
    data = Action.get_on_off(status)
    return data

@app.get("/show_stack_all")
async def show_stack_all():
    data = Action.show_stack_all()
    return data

@app.get("/show_stack_coin")
async def show_stack_coin(id):
    data = Action.show_stack_coin(id)
    return data

@app.get("/get_stack_coin_ID")
async def get_stack_coin(id):
    coin = Action.show_stack_coin(id)
    stack_coin = int(coin[0]["stack_coin"])
    stack_coin +=1
    data = Action.get_stack_coin(stack_coin,id)
    return data

@app.get("/reset_stack_coin")
async def reset_stack_coin(id):
    data = Action.reset_stack_coin(id)
    return data

@app.get("/reset_stack_coin_all")
async def reset_stack_coin_all():
    data = Action.reset_stack_coin_all()
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.43.92", port = 80)