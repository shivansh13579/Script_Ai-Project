from openai import OpenAI
from app.core.config import settings
from app.utils.json_parser import safe_json_loads

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

def critic_agent(state):

    script = state["final_script"]

    creator_style = state.get(
        "creator_style",
        {}
    )

    creator_profile = creator_style.get(
        "creator_profile",
        {}
    )

    pacing_patterns = creator_style.get(
        "pacing_patterns",
        []
    )

    emotion_patterns = creator_style.get(
        "emotion_patterns",
        []
    )

    vocabulary_patterns = creator_style.get(
        "vocabulary_patterns",
        []
    )

    psychological_triggers = creator_style.get(
        "psychological_triggers",
        []
    )

    prompt = f"""
You are an elite viral reel critic.

Your job:
Review this reel script VERY critically.

CREATOR PROFILE:
{creator_profile}

CREATOR PACING STYLE:
{pacing_patterns}

CREATOR EMOTIONAL STYLE:
{emotion_patterns}

CREATOR VOCABULARY:
{vocabulary_patterns}

CREATOR PSYCHOLOGICAL TRIGGERS:
{psychological_triggers}

SCRIPT TO REVIEW:

HOOK:
{script.get("hook", "")}

BODY:
{script.get("body", "")}

CTA:
{script.get("cta", "")}

CHECK VERY CAREFULLY:

1. Is the hook instantly attention grabbing?
2. Is retention high throughout?
3. Does pacing feel dynamic?
4. Does script sound HUMAN?
5. Does emotional flow match creator style?
6. Does vocabulary match creator tone?
7. Does it create curiosity loops?
8. Does CTA feel natural?
9. Does it feel cinematic?
10. Would viewers continue watching?

IMPORTANT:
Be EXTREMELY strict.

If script feels generic:
needs_revision = true

If pacing becomes boring:
needs_revision = true

If creator style is weak:
needs_revision = true

Return STRICT JSON ONLY:

{{
    "score": 0,
    "feedback": [
        "feedback 1",
        "feedback 2"
    ],
    "needs_revision": true
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",

        response_format={
            "type": "json_object"
        },

        temperature=0.4,

        messages=[
            {
                "role": "system",
                "content": """
You are a world-class viral content strategist.

You are brutally honest.

You detect:
- weak hooks
- robotic writing
- weak retention
- poor pacing
- weak creator matching

Never give fake high scores.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = (
        response.choices[0]
        .message.content
    )

    parsed = safe_json_loads(content)

    print("CRITIC RESULT:", parsed)

    return {

        "quality_score": int(
            parsed.get("score", 5)
        ),

        "feedback": parsed.get(
            "feedback",
            []
        ),

        "needs_revision": parsed.get(
            "needs_revision",
            False
        )
    }