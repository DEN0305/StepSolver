from app.services.solver_service import solve_step_by_step
from app.services.tts_service import generate_audio_from_steps

def solve_equation(data):
    equations = data.get("equations", [])
    variables = data.get("variables", [])
    initial_conditions = data.get("initial_conditions", {})

    steps = solve_step_by_step(equations, variables, initial_conditions)

    audio_path = generate_audio_from_steps(steps)

    return {
        "steps": steps,
        "audio_url": "/static/audio/results.mp3"
    }