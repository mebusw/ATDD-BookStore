from django.conf.urls import patterns, url

from book import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^book/(?P<book_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
#    url(r'^(?P<book_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
#    url(r'^(?P<book_id>\d+)/vote/$', views.vote, name='vote'),

    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^search/$', views.search_view, name='search'),
    url(r'^pick/$', views.pick_view, name='pick'),    
    url(r'^adjust/$', views.adjust_view, name='adjust'),    
    url(r'^cart/$', views.cart_view, name='cart'),    
    url(r'^checkout/$', views.checkout_view, name='checkout'),     
    url(r'^confirm/$', views.confirm_view, name='confirm'),     
)



#with below, 
# Now delelte index(), detail() and results() views from polls/views.py as they can be replacesd by generic views
# for ListView, the automatically generated context variable is poll_list for model(Poll)
# for DetailView, the automatically generated context variable is poll for model(Poll)


'''
urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote', name='vote'),
)
'''
