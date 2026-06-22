from statistics import mean

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models import SolveSession, User
from app.schemas import AnalyticsOut, SolveSessionOut

router = APIRouter()


@router.get("", response_model=list[SolveSessionOut])
def list_history(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[SolveSessionOut]:
    rows = (
        db.query(SolveSession)
        .filter(SolveSession.user_id == user.id)
        .order_by(SolveSession.created_at.desc())
        .limit(50)
        .all()
    )
    return [
        SolveSessionOut(
            id=row.id,
            cube_state=row.cube_state,
            solution=row.solution.split(),
            move_count=row.move_count,
            complexity=row.complexity,
            created_at=row.created_at,
        )
        for row in rows
    ]


@router.get("/analytics", response_model=AnalyticsOut)
def analytics(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> AnalyticsOut:
    rows = db.query(SolveSession).filter(SolveSession.user_id == user.id).all()
    move_counts = [row.move_count for row in rows]
    return AnalyticsOut(
        total_solved=len(rows),
        average_move_count=round(mean(move_counts), 2) if move_counts else 0,
        best_move_count=min(move_counts) if move_counts else None,
        daily_streak=0,
    )

