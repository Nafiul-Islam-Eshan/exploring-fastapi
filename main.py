from fastapi import FastAPI

app = FastAPI()

notes = [
    {
        "id": 1,
        "term": "variable",
        "defination": "A name that stores values in a program.",
        "js_equivalent": "let / const",
        "tags": ["python", "basics"],
        "learned": True,
    },
    {
        "id": 2,
        "term": "list",
        "defination": "An ordered, mutable collection of items.",
        "js_equivalent": "Array",
        "tags": ["python", "data-structures"],
        "learned": True,
    },
    {
        "id": 3,
        "term": "dict",
        "defination": "Key-value pairs, like a javascript object.",
        "js_equivalent": "Object",
        "tags": ["python", "data"],
        "learned": False,
    },
    {
        "id": 4,
        "term": "function",
        "defination": "A reusable block of code defined with def.",
        "js_equivalent": "function",
        "tags": ["python", "basics"],
        "learned": False,
    },
    {
        "id": 6,
        "term": "tuple",
        "defination": "An ordered, immutable collection of items.",
        "js_equivalent": "No direct equivalent",
        "tags": ["python", "data-structures"],
        "learned": False,
    },
    {
        "id": 7,
        "term": "set",
        "defination": "An unordered collection of unique elements.",
        "js_equivalent": "Set",
        "tags": ["python", "data-structures"],
        "learned": False,
    },
    {
        "id": 8,
        "term": "loop",
        "defination": "A control structure that repeats a block of code.",
        "js_equivalent": "for / while",
        "tags": ["python", "control-flow"],
        "learned": True,
    },
    {
        "id": 9,
        "term": "None",
        "defination": "A special value representing the absence of a value.",
        "js_equivalent": "null",
        "tags": ["python", "basics"],
        "learned": False,
    },
]


@app.get("/")
def root():
    return {"message": "Learning notebook api is running."}


@app.get("/terms")
def get_terms():
    return notes



