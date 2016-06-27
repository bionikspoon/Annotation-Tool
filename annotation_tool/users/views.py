from __future__ import absolute_import, unicode_literals

from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User
from .serializers import UserSerializer, ProfileSerializer


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs=dict(username=self.request.user.username))


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail", kwargs={
            "username": self.request.user.username
        })

    # noinspection PyMethodOverriding
    def get_object(self):
        """
        :param django.views.generic.UpdateView self)
        :return:
        """
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProfileRetrieveAPIView(RetrieveAPIView):
    user = NotImplemented
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    # authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        self.user = request.user
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return self.user
