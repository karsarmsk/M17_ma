from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/all_task")
async def get_all_task():
    pass
@router.post("/create")
async def create_task():
    pass
@router.get("/update_task")
async def update_task():
    pass

@router.delete("/delete")
async def delete_task():
    pass