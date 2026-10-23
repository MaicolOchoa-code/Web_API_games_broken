from fastapi import HTTPException
from sqlmodel import Session, select

from models.game import Game
from schemas.game import GameCreate


def create_game(game_data: GameCreate, session: Session):
    game = Game(
        title=game_data.title,
        genre=game_data.genre,
        platform=game_data.platform,
        stock=game_data.stock,
        active=game_data.active
    )

    session.add(game)

    # PISTA: recuerda el orden visto en clase para guardar un objeto
    # y luego recargar los valores generados por la base de datos.
    session.refresh(game)

    return game


def list_games(session: Session):
    statement = select(Game)
    return session.exec(statement).all()


def get_game(game_id: int, session: Session):
    # PISTA: ¿qué debería devolver una API cuando el recurso solicitado no existe?
    return session.get(Game, game_id)


def delete_game(game_id: int, session: Session):
    game = session.get(Game, game_id)

    if not game:
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )

    session.delete(game)

    # PISTA: eliminar un objeto de una sesión no necesariamente significa
    # que la eliminación haya quedado guardada en SQLite.

    return {"message": "Game deleted"}
