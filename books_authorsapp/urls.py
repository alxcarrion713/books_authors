from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index),
    path("createbook", views.createbook),
    path("book/<bookid>", views.showbook),
    path("addauthor/<bookid>", views.addauthor)
]