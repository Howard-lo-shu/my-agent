from fastapi import APIRouter

from src.api.schemas import MoveRequest, ToolResult

router = APIRouter()

robot = {"state": "idle", "location": "home"}


@router.get("/tools")
def list_tools():
    return {
        "tools": [
            {"name": "move", "description": "move robot to location"},
            {"name": "status", "description": "get robot status"}
        ]
    }

@router.post("/move", response_model=ToolResult)
def move(req: MoveRequest):
    robot["location"] = req.location
    return {"result": f"Robot moving to {req.location}"}

@router.get("/status", response_model=ToolResult)
def status():
    return {"result": f"Robot {robot['state']} at {robot['location']}"}
