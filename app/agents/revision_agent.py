from openai import OpenAI
from app.core.config import settings
from app.utils.json_parser import safe_json_loads
import json

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

def revision_agent(state):
    feedback = "\n".join(
        state.get("feedback", [])
    )

    print("RETRY COUNT:", state.get("retry_count"))

    old_script = state["final_script"]

    prompt = f"""
Improve this reel script.

OLD SCRIPT:

HOOK:
{old_script.get("hook")}

BODY:
{old_script.get("body")}

CTA:
{old_script.get("cta")}

CRITIC FEEDBACK:
{feedback}

Rules:
- Improve weak areas
- Keep cinematic Hinglish
- Make hook stronger
- Improve retention
- Keep emotional pacing

Return STRICT JSON:

{{
   "hook": "",
   "body": "",
   "cta": ""
}}
"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        temperature=0.9,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    parsed = safe_json_loads(content)

    print("parsed",parsed)

    return {
        "hook": parsed.get("hook", ""),
        "body": parsed.get("body", ""),
        "cta": parsed.get("cta", ""),

        "final_script": parsed,

        "retry_count": state.get(
            "retry_count",
            0
        ) + 1
    }

