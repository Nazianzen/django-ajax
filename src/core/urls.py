from django.urls import path
from core.views import (
    index_view,
    post_friend,
    check_nickname,
)

urlpatterns = [
    path('', index_view),
    path('post/ajax/friend', post_friend, name = "post_friend"),
    path('get/ajax/validate/nickname', check_nickname, name = "validate_nickname")
]
