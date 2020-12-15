from .views import LibraryViewSet, BookViewSet, AuthorViewSet, InvitationsViewSet, ContactViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('libraries', LibraryViewSet)
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('invitations', InvitationsViewSet)
router.register('contacts', ContactViewSet)


urlpatterns = router.urls
