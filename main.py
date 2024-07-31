import sys
from fastapi import FastAPI, Response, Request

from src.algorithm.cave_gen import gen_puzzle

# import justpy as jp
# from src.algorithm.vizualization import make_table

# jp.justpy(make_table, host="0.0.0.0", start_server=False)
# server = jp.app

app = FastAPI()


@app.options("/gen-cave")
def preflight(request: Request, response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return request.body


@app.get("/gen-cave")
def build_cave(field_size: int, response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return gen_puzzle(field_size)
