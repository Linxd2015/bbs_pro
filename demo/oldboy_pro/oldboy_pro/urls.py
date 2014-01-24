from django.conf.urls import patterns, include, url

from django.contrib import admin
from bbs.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oldboy_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),

	(r'^$', index),
	(r'^python/$', python_bbs),
	(r'^bbs_detail/$', bbs_detail),
	(r'^addcomment/$', add_comment),
	
)
