from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('slides.views',
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^(?P<slug>[-\w.]+)/$', 'present', name='presentation'),
    url(r'^draft/(?P<slug>[-\w.]+)/$', 'present_draft', name='draft_presentation'),
)
