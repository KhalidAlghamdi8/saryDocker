from rest_framework import routers
from .views import stack_viewset

router=routers.DefaultRouter()
router.register('stack', stack_viewset)