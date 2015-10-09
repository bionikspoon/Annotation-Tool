# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib.staticfiles import views as staticfiles_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from ..annotation_tool.pubmed.views import (PubmedViewSet, GeneViewSet, PatientOutcomesViewSet, DiseaseViewSet,
    VariantConsequenceViewSet, VariantTypeViewSet, StructureViewSet, MutationTypeViewSet, SyntaxViewSet,
    RuleLevelViewSet)
from ..annotation_tool.users.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('pubmed', PubmedViewSet)
router.register('genes', GeneViewSet)
router.register('lookup-structure', StructureViewSet)
router.register('lookup-mutation-type', MutationTypeViewSet)
router.register('lookup-syntax', SyntaxViewSet)
router.register('lookup-rule-level', RuleLevelViewSet)
router.register('lookup-variant-type', VariantTypeViewSet)
router.register('lookup-variant-consequence', VariantConsequenceViewSet)
router.register('lookup-disease', DiseaseViewSet)
router.register('lookup-patient-outcomes', PatientOutcomesViewSet)

urlpatterns = [url(r'^api/', include(router.urls)), url(r'^api/auth/login/', obtain_jwt_token)]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += patterns('django.contrib.staticfiles.views',
#                         url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index.html'}),
#                         url(r'^(?P<path>(?:assets|css|images|js|scripts|styles)/.*)$', 'serve'))


# TODO Delete this
##############################################################################





# url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
# url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

# # Django Admin# url(r'^admin/', include(admin.site.urls)),## # User management
# url(r'^users/', include("annotation_tool.users.urls", namespace="users")),
# url(r'^accounts/', include('allauth.urls')),

# Your stuff: custom urls includes go here
# if settings.DEBUG:
#     # This allows the error pages to be debugged during development, just visit
#     # these url in browser to see how these error pages look like.
#     urlpatterns += [
#         url(r'^400/$', default_views.bad_request),
#         url(r'^403/$', default_views.permission_denied),
#         url(r'^404/$', default_views.page_not_found),
#         url(r'^500/$', default_views.server_error),
#     ]
