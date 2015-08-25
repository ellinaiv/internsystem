from cal.rest import (
    EscapeOccupiedViewSet,
    EventViewSet,
    SemesterViewSet,
)
from core.utils import SharedAPIRootRouter

# SharedAPIRootRouter is automatically imported in global urls config
router = SharedAPIRootRouter()
router.register(r'cal/events', EventViewSet, base_name='events')
router.register(r'cal/semesters', SemesterViewSet, base_name='semesters')
router.register(r'cal/escape_occupied', EscapeOccupiedViewSet, base_name='escape_occupied')
