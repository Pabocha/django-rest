from django.urls import path
from .views import *

urlpatterns = [
    # path('', api_view, name="api_view"),
    # path('<int:pk>/', DetailApiView.as_view()),
    # path('create/', CreateApiView.as_view()),
    # path('<int:pk>/update/', UpdateApiView.as_view()),
    # path('<int:pk>/delete/', DeleteApiView.as_view()),
    path('create/', ProductMixinsView.as_view()),
    path('list/', ProductMixinsView.as_view()),
    path('<int:pk>/detail/', ProductMixinsView.as_view()),
    path('<int:pk>/update/', ProductMixinsView.as_view()),
    path('<int:pk>/delete/', ProductMixinsView.as_view()),

]
