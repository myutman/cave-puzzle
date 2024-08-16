import sys
from fastapi import FastAPI, Response, Request

from src.algorithm.cave_gen import gen_puzzle
from src.algorithm.check_solved import check_solved
from src.schemas.solution import Solution


app = FastAPI()


@app.options("/gen-cave")
def preflight(request: Request, response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Connection"] = "keep-alive"
    return request.body


@app.get("/gen-cave")
def build_cave(field_size: int, response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Connection"] = "keep-alive"
    return gen_puzzle(field_size)


@app.options("/check-solution")
def preflight(request: Request, response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Connection"] = "keep-alive"
    return request.body


@app.post("/check-solution")
def build_cave(data: Solution, response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Content-Type"] = "application/json"
    response.headers["Connection"] = "keep-alive"

    sys.stderr.write("Got request")

    return {"solved": check_solved(field=data.field, occupied=data.field_colors)}
