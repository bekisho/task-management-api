from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterView, TaskViewSet, CategoryViewSet, CommentListCreateView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # User login & token retrieval
    path('', include(router.urls)),
    path('comments/<int:task_id>/', CommentListCreateView.as_view(), name='comment-list-create'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, TaskViewSet, CategoryViewSet, CommentListCreateView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('comments/<int:task_id>/', CommentListCreateView.as_view(), name='task-comments'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/register/', RegisterView.as_view(), name='register'),
]


urlpatterns += router.urls
