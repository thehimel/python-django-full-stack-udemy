

# ----------------------------------------------------------------------------
## In urlpatterns of urls.py, while declaring url, for class based view, we need to use as_view().
urlpatterns = [
	url(r'^about/$', views.AboutView.as_view(), name='about')
]

# ----------------------------------------------------------------------------
## In views.py, we use decorators for function based views and mixins for class based views.
# Import
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Declaration
class CreatePostView(LoginRequiredMixin, CreateView):
	login_url = '/login/'
	redirect_field_name = 'blog/post_detail.html'
	form_class = PostForm
	model = Post
