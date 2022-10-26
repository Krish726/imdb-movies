from django.urls import path,include
#Used for function based api views
#from watchlist_app.api.views import movie_details,movie_list
# Used for class based api views
#from watchlist_app.api.views import MovieDetailAV,MovieListAV
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (WatchListDetailAV,WatchListListAV,StreamPlatformAV,
                                     StreamPlatformDetailAV,ReviewList,ReviewDetails,ReviewCreate,StreamPlatformVS,
                                     UserReview,WatchList)


router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    #path('list/',movie_list,name='movie-list'),
    #path('<int:pk>/', movie_details, name='movie-detail'),
    #path('list/',MovieListAV.as_view(),name='movie-list'),
    #path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),
    
    path('list/',WatchListListAV.as_view(),name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='movie-detail'),
    path('list2/',WatchList.as_view(),name='movie-list'),
    
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('', include(router.urls)),
    
    path('<int:pk>/reviews/', ReviewList.as_view(), name = 'review-list'),
    path('<int:pk>/review/review-create/', ReviewCreate.as_view(), name = 'review-create'),
    path('review/<int:pk>/', ReviewDetails.as_view(), name = 'review-details'),
    #path('reviews/<str:username>/', UserReview.as_view(), name = 'user-review-details')   
    
    path('reviews/', UserReview.as_view(), name = 'user-review-details') 
    # path('review/', ReviewList.as_view(), name = 'review-list'),
    # path('review/<int:pk>/', ReviewDetails.as_view(), name = 'review-details')
    
]