from django.urls import path, include
from watchlist_app.api.views import (WatchDetailAV, WatchListAV,
                                     ReviewList, ReviewDetail,
                                     ReviewCreate, StreamPlatformVS,
                                     UserReview, WatchListGV,
                                     StreamPlatformAV, StreamPlatformDetailAV)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),

    path('', include(router.urls)),
    path('<int:pk>/review-create/',
         ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(),
         name='review-list'),  # List of all the reviews
    # get the review detail  and edit or delete the review
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    # get the reviews published by particular user
    path('reviews/', UserReview.as_view(),
         name='user-review-detail'),

    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    # path('review/', ReviewList .as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
