from .models import *
import re

def logged_user_name(request):
    username = "user not logged"
    try:
        username = request.user.username
        return {"logged_username" : username}
    except:
        pass


def get_current_path(request):
    path = request.get_full_path()
    path = re.sub("[^0-9]", "", path)

    return {
       'current_path': path,
     }