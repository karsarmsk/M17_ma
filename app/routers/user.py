from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/all_user")
async def get_all_user():
    pass
@router.post("/create")
async def create_user():
    pass
@router.get("/update_user")
async def update_user():
    pass

@router.delete("/delete")
async def delete_user():
    pass