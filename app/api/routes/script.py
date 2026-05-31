from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session
from app.db.database import get_session
from app.db.models import ScriptResponse,ScriptGenerateRequest,ScriptCreate
from app.services.script_service import create_script
from app.services.ai_service import format_script
from app.graph.workflow import graph

router = APIRouter()

@router.post("/generate", response_model=ScriptResponse)
def generate_script(
    data: ScriptGenerateRequest,
    session: Session = Depends(get_session)
):
    """
    Generate script using AI + save to DB
    """
    print("data",data.topic,data.tone)
    try:
        
        ai_result = graph.invoke({
            "topic": data.topic,
            "tone": data.tone,
            "creator":  data.creator,
            "retry_count": 0
        })
        
        print("ai_result",ai_result)

        script_data = ScriptCreate(
            topic=data.topic,
            tone=data.tone,
            script=ai_result["final_script"],
            sources=ai_result.get("sources",[]),
            quality_score=ai_result.get("quality_score"),
            hashtags=",".join(ai_result.get("hashtags", [])),
            formatted_script=format_script(
            ai_result["final_script"]
            )
        )
        print("script_data",script_data)

        script = create_script(session,script_data)
        print("script",script)

        return script
    
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))