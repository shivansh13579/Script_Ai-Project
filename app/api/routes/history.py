from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session
from app.db.database import get_session
from app.services.script_service import (
    get_all_scripts,
    get_script_by_id,
    delete_script
)

router = APIRouter()

@router.get("/")
def get_scripts(
    offset: int = 0,
    limit: int = 10,
    tone: str = None,
    session: Session = Depends(get_session)
):
    return get_all_scripts(session, offset, limit, tone)

@router.get("/{script_id}")
def get_script(script_id: int, session: Session = Depends(get_session)):
    script = get_script_by_id(session,script_id)
    if not script:
        raise HTTPException(status_code=404, detail="Script not found")
    return script

@router.delete("/{script_id}")
def delete(script_id: int, session: Session = Depends(get_session)):
    success = delete_script(session,script_id)

    if not success:
        raise HTTPException(status_code=404, detail="Script not found")
    
    return {"message": "Deleted successfully"}