from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session
from app.db.database import get_session
from app.db.models import ScriptResponse,ScriptGenerateRequest,ScriptCreate
from app.services.script_service import create_script
from app.services.ai_service import generate_script_ai
from app.services.ai_service import format_script
from app.agents.research_agent import research_topic

router = APIRouter()

@router.post("/generate", response_model=ScriptResponse)
def generate_script(
    data: ScriptGenerateRequest,
    session: Session = Depends(get_session)
):
    """
    Generate script using AI + save to DB
    """
    try:
        research = research_topic(data.topic)

        ai_result = generate_script_ai(data.topic,data.tone,context=research)

        script_data = ScriptCreate(
            topic=data.topic,
            tone=data.tone,
            script=ai_result["script"],
            sources=",".join(research["sources"]),
            quality_score=ai_result("quality_score"),
            hashtags=",".join(ai_result.get("hashtags", [])),
            formatted_script=format_script(ai_result["script"])
        )

        script = create_script(session,script_data)

        return script
    
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))