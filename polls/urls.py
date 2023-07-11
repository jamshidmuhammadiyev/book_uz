from django.urls import path
from .views import (AllCreateBookView,DetailBookView,AuthorView,DetailAuthorView,CreateAuthorView,UpdateAuthorView,
                    DetailUpdateDeleteApiView)
urlpatterns = [
    path('',AllCreateBookView.as_view()),
    path('<pk>/',DetailUpdateDeleteApiView.as_view())
]