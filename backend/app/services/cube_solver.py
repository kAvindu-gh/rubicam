from collections import Counter

from app.schemas import CubeSolveOut

ALLOWED_STICKERS = set("URFDLB")
SOLVED_STATE = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"


def validate_cube_state(cube_state: str) -> list[str]:
    errors: list[str] = []
    if len(cube_state) != 54:
        errors.append("Cube state must contain exactly 54 stickers.")
        return errors

    invalid = sorted(set(cube_state) - ALLOWED_STICKERS)
    if invalid:
        errors.append(f"Invalid stickers found: {', '.join(invalid)}.")

    counts = Counter(cube_state)
    for sticker in sorted(ALLOWED_STICKERS):
        if counts[sticker] != 9:
            errors.append(f"Sticker {sticker} appears {counts[sticker]} times; expected 9.")

    centers = cube_state[4] + cube_state[13] + cube_state[22] + cube_state[31] + cube_state[40] + cube_state[49]
    if set(centers) != ALLOWED_STICKERS:
        errors.append("Each face center must contain a unique cube color.")

    return errors


def solve_cube(cube_state: str) -> CubeSolveOut:
    errors = validate_cube_state(cube_state)
    if errors:
        return CubeSolveOut(valid=False, errors=errors)

    if cube_state == SOLVED_STATE:
        return CubeSolveOut(valid=True, solution=[], move_count=0, complexity="solved")

    try:
        import kociemba
    except ImportError:
        return CubeSolveOut(
            valid=False,
            errors=[
                "The optimal solver package is not installed for this Python version. "
                "Use Python 3.11 or 3.12 and install requirements again to enable solving."
            ],
        )

    try:
        solution_text = kociemba.solve(cube_state)
        moves = solution_text.split() if solution_text else []
    except Exception as exc:
        return CubeSolveOut(
            valid=False,
            errors=[f"Solver rejected this cube state: {exc}"],
        )

    move_count = len(moves)
    complexity = "easy" if move_count <= 12 else "medium" if move_count <= 20 else "hard"
    return CubeSolveOut(valid=True, solution=moves, move_count=move_count, complexity=complexity)
