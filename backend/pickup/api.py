from ninja import NinjaAPI
from users.api import router as users_router
from board.api import router as board_router

api = NinjaAPI()

api.add_router("/users/", users_router)
api.add_router("/board/", board_router)
