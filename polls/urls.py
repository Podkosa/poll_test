from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('vote', views.VoteView)
router.register('', views.PollView)


urlpatterns = router.urls
