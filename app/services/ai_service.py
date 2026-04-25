from openai import OpenAI
from app.core.config import settings
import json

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_script_ai(topic: str, tone: str, context: dict) -> dict:

    facts_text = "\n".join(context.get("facts", []))

    prompt = f"""
    Tu ek viral reel creator hai.

    Topic: {topic}
    Tone: {tone}

    Use these facts:
    {facts_text}

    Output STRICT JSON:

    {{
      "hook": "...",
      "body": "...",
      "cta": "...",
      "hashtags": ["#ai", "#news"]
    }}

    Rules:
    - Hinglish
    - engaging
    - use facts naturally
    - no extra text
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a viral reel script writer"},
            {"role": "user", "content": prompt}
        ]
    )

    script_text = response.choices[0].message.content

    try:
        content = script_text.strip()
        if content.startswith("```"):
            content = content.replace("```json", "").replace("```", "").strip()
        parsed = json.loads(script_text)
    except:
        parsed = {
            "hook": script_text[:100],
            "body": script_text,
            "cta": "Follow for more",
            "hashtags": ["#viral"]
        }

    return {
        "script": {
            "hook": parsed.get("hook"),
            "body": parsed.get("body"),
            "cta": parsed.get("cta")
        },
        "hashtags": parsed.get("hashtags"),
        "sources": parsed.get("sources"),
        "quality_score": calculate_score(parsed)
    }

def calculate_score(script: dict) -> float:
    score = 0

    if len(script.get("hook", "")) > 20:
        score += 3
    if len(script.get("body", "")) > 100:
        score += 3
    if "?" in script.get("hook", ""):
        score += 2
    if "follow" in script.get("cta", "").lower():
        score += 2

    return min(score, 10)

def format_script(script: dict) -> str:
    return f"""
🎯 HOOK:
{script.get("hook")}

📖 BODY:
{script.get("body")}

📢 CTA:
{script.get("cta")}
"""