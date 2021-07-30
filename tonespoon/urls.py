from django.urls import path
from . import views


urlpatterns = [
    path("albums", views.AlbumList.as_view(), name="album_list"),
    path("albums/<int:pk>", views.AlbumDetail.as_view(), name="album_detail"),
    path("reviews", views.ReviewList.as_view(), name="review_list"),
    path("reviews/<int:pk>", views.ReviewDetail.as_view(), name="review_detail"),
]
# urlpatterns = [path("songs", views.song_list, name="song_list")]
