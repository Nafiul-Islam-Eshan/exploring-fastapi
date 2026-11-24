from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

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
        "id": 5,
        "term": "tuple",
        "defination": "An ordered, immutable collection of items.",
        "js_equivalent": "No direct equivalent",
        "tags": ["python", "data-structures"],
        "learned": False,
    },
    {
        "id": 6,
        "term": "set",
        "defination": "An unordered collection of unique elements.",
        "js_equivalent": "Set",
        "tags": ["python", "data-structures"],
        "learned": False,
    },
    {
        "id": 7,
        "term": "loop",
        "defination": "A control structure that repeats a block of code.",
        "js_equivalent": "for / while",
        "tags": ["python", "control-flow"],
        "learned": True,
    },
    {
        "id": 8,
        "term": "None",
        "defination": "A special value representing the absence of a value.",
        "js_equivalent": "null",
        "tags": ["python", "basics"],
        "learned": False,
    },
]

class Note(BaseModel):
    term : str 
    defination : str
    js_equivalent: str | None = None
    tags : list[str] = []    
    learned : bool = False    
    

class NoteUpdate(BaseModel):
    term: str  | None = None
    defination : str | None = None
    js_equivalent : str | None = None
    tags : list[str] | None = None
    learned : bool | None = None


@app.get("/")
def root():
    return {"message": "Learning notebook api is running."}


@app.get("/terms")
def get_terms(tag: str | None = None, term: str | None=None):
    result = []
    for note in notes:
        if tag and tag not in note["tags"]:
            continue
        if term and term.lower() not in note["term"].lower():
            continue
        result.append(note)
    return result


@app.get("/terms/random")
def random_term():
    if not notes:
        raise HTTPException(status_code=404, message="No term available")
    return random.choice(notes)


@app.get("/terms/{terms_id}")
def get_terms(terms_id:int):
    for note in notes:
        if note["id"] == terms_id:
            return note
    raise HTTPException(status_code=404, detail="term not found")


@app.post("/terms", status_code=201)
def add_term(note : Note):
    for existing in notes:
        if existing["term"].lower() == note.term.lower():
            raise HTTPException(status_code=409, detail="term already exists")
            
    new_id = 1
    for exist in notes:
        if exist["id"] >= new_id:
            new_id = exist["id"] + 1
    new_node = {"id" : new_id}
    new_node.update(note.model_dump())
    notes.append(new_node)        
    return new_node



@app.patch("/terms/{term_id}")
def update_term(term_id : int, changes : NoteUpdate):
    for note in notes:
        if term_id == note["id"]:
            note.update(changes.model_dump(exclude_unset=True))
            return note
    raise HTTPException(status_code=404, detail="term not found")
        


@app.delete("/terms/{term_id}", status_code=204)
def delete_term(term_id : int):
    
    for note in notes:
        if note["id"] == term_id:
            notes.remove(note)
            return {"message": "Term deleted successfully"}
    raise HTTPException(status_code=404, detail="term not found")



    

