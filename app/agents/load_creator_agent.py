from app.services.creator_loader import load_creator_style

def load_creator_agent(state):
    creator_data = load_creator_style(
        state["creator"]
    )

    print("creator_data",creator_data)

    return {
        "creator_style": creator_data
    }