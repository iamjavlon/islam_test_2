# from .request import get
from app.models import User

def lang(chat_id):
    # user = get(f'users/{chat_id}')
    user = User.object.get(id=chat_id)
    return user['language']