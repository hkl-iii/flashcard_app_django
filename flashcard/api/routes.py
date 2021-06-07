
from rest_framework import routers
from .views import *

app_name='flashcard'

router = routers.DefaultRouter()
router.register('card',CardViewSet)



