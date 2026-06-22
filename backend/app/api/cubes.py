from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies import get_optional_current_user
from app.models import SolveSession, User
from app.schemas import CubeSolveOut, CubeSolveRequest, CubeValidationOut
from app.services.cube_solver import solve_cube, validate_cube_state

router = APIRouter()


@router.post("/validate", response_model=CubeValidationOut)
def validate_cube(payload: CubeSolveRequest) -> CubeValidationOut:
    errors = validate_cube_state(payload.cube_state)
    return CubeValidationOut(valid=not errors, errors=errors)


@router.post("/solve", response_model=CubeSolveOut)
def solve(
    payload: CubeSolveRequest,
    user: User | None = Depends(get_optional_current_user),
    db: Session = Depends(get_db),
) -> CubeSolveOut:
    result = solve_cube(payload.cube_state)
    if result.valid and payload.save and user is not None:
        session = SolveSession(
            user_id=user.id,
            cube_state=payload.cube_state,
            solution=" ".join(result.solution),
            move_count=result.move_count,
            complexity=result.complexity,
        )
        db.add(session)
        db.commit()
    return result
