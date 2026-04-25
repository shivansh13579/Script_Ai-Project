from sqlmodel import Session, select
from app.db.models import Script,ScriptCreate
from app.core.logger import logger
from typing import List, Optional

def create_script(
        session: Session,
        data: ScriptCreate,
) -> Script:
    """
    Naya script save karo
    """
    
    script = Script(
        **data.dict()
    )
    session.add(script)
    session.commit()
    session.refresh(script)
    logger.info(f"Script saved -- id={script.id} topic={script.topic}")
    return script

def get_all_scripts(
        session: Session,
        offset: int = 0,
        limit: int = 10,
        tone: Optional[str] = None
) -> List[Script]:
     """
    Saare scripts fetch karo
    """
     statement = select(Script)

     if tone:
         statement = statement.where(Script.tone == tone)
    
     statement = (
         statement
         .offset(offset)
         .limit(limit)
         .order_by(Script.created_at.desc())
     )

     return session.exec(statement).all()


def get_script_by_id(
    session: Session,
    script_id: int
) -> Optional[Script]:
    """
    ID se ek script fetch karo
    """
    script = session.get(Script, script_id)
    if not script:
        logger.warning(f"Script not found -- id={script_id}")
    return script

def delete_script(
        session: Session,
        script_id: int
) -> bool:
    """
    Script delete karo
    """
    script = session.get(Script,script_id)
    if not script:
        logger.warning(f"Delete failed -- id={script_id} not found")
        return False
    
    session.delete(script)
    session.commit()
    logger.info(f"Script deleted -- id={script_id}")
    return True

