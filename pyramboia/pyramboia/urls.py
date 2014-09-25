from django.conf.urls import patterns, include, url
from django.contrib import admin
from tasks.views import runTask
from tasks.views import ProjectListView, ProjectCreateView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView, HeaderListView, HeaderCreateView, HeaderDetailView, HeaderUpdateView, HeaderDeleteView, TargetListView, TargetCreateView, TargetDetailView, TargetUpdateView, TargetDeleteView, ArgumentListView, ArgumentCreateView, ArgumentDetailView, ArgumentUpdateView, ArgumentDeleteView, TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView
#from tasks.api import TasksResource

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Pyramboia.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'tasks.views.home', name='home'),
                       # Project URLS
                       url(r'^projects$',
                           ProjectListView.as_view(),
                           name='project-list'),
                       url(r'^project/add/$',
                           ProjectCreateView.as_view(),
                           name='project-create'),
                       url(r'^project/(?P<pk>[\w\d]+)/$',
                           ProjectDetailView.as_view(),
                           name='project-detail'),
                       url(r'^project/(?P<pk>[\w\d]+)/edit/$',
                           ProjectUpdateView.as_view(),
                           name='project-update'),
                       url(r'^project/(?P<pk>[\w\d]+)/delete/$',
                           ProjectDeleteView.as_view(),
                           name='project-delete'),
                       # Header URLS
                       url(r'^headers$',
                           HeaderListView.as_view(),
                           name='header-list'),
                       url(r'^header/add/$',
                           HeaderCreateView.as_view(),
                           name='header-create'),
                       url(r'^header/(?P<pk>[\w\d]+)/$',
                           HeaderDetailView.as_view(),
                           name='header-detail'),
                       url(r'^header/(?P<pk>[\w\d]+)/edit/$',
                           HeaderUpdateView.as_view(),
                           name='header-update'),
                       url(r'^header/(?P<pk>[\w\d]+)/delete/$',
                           HeaderDeleteView.as_view(),
                           name='header-delete'),
                       # Target URLS
                       url(r'^targets$',
                           TargetListView.as_view(),
                           name='target-list'),
                       url(r'^target/add/$',
                           TargetCreateView.as_view(),
                           name='target-create'),
                       url(r'^target/(?P<pk>[\w\d]+)/$',
                           TargetDetailView.as_view(),
                           name='target-detail'),
                       url(r'^target/(?P<pk>[\w\d]+)/edit/$',
                           TargetUpdateView.as_view(),
                           name='target-update'),
                       url(r'^target/(?P<pk>[\w\d]+)/delete/$',
                           TargetDeleteView.as_view(),
                           name='target-delete'),
                       # Argument URLS
                       url(r'^arguments$',
                           ArgumentListView.as_view(),
                           name='argument-list'),
                       url(r'^argument/add/$',
                           ArgumentCreateView.as_view(),
                           name='argument-create'),
                       url(r'^argument/(?P<pk>[\w\d]+)/$',
                           ArgumentDetailView.as_view(),
                           name='argument-detail'),
                       url(r'^argument/(?P<pk>[\w\d]+)/edit/$',
                           ArgumentUpdateView.as_view(),
                           name='argument-update'),
                       url(r'^argument/(?P<pk>[\w\d]+)/delete/$',
                           ArgumentDeleteView.as_view(),
                           name='argument-delete'),
                       # Task URLS
                       url(r'^tasks$',
                           TaskListView.as_view(),
                           name='task-list'),
                       url(r'^task/(?P<id>\d+)/run/$',
                           runTask, name='runTask'),
                       # url(r'^task/(?P<pk>[\w\d]+)/run/$',
                       #                           runTask, name='runTask'),
                       url(r'^task/add/$',
                           TaskCreateView.as_view(),
                           name='task-create'),
                       url(r'^task/(?P<pk>[\w\d]+)/$',
                           TaskDetailView.as_view(),
                           name='task-detail'),
                       url(r'^task/(?P<pk>[\w\d]+)/edit/$',
                           TaskUpdateView.as_view(),
                           name='task-update'),
                       url(r'^task/(?P<pk>[\w\d]+)/delete/$',
                           TaskDeleteView.as_view(),
                           name='task-delete'),
                       )