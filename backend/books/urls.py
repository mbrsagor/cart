from .views import LibraryViewSet, BookViewSet, AuthorViewSet, InvitationsViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('libraries', LibraryViewSet)
router.register('author', AuthorViewSet)
router.register('book', BookViewSet)
router.register('invitations', InvitationsViewSet)


urlpatterns = router.urls
