from django.shortcuts import render, get_object_or_404, redirect
from library.models import Post, Comment, Preference, category
from users.models import UserProfile
from accounts.models import MyUser
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from .forms import NewCommentForm
from django.contrib.auth.decorators import login_required

def is_users(post_user, logged_user):
    return post_user == logged_user

PAGINATION_COUNT = 3

# Create your views here.
class CategoryListView(ListView):
        def get(self, request):
                cate = category.objects.all()
                context = {'cate': cate}
                return render(request, 'library/library_home.html', context)



class PostListView(LoginRequiredMixin, ListView):

        def get(self, request):
                return render(request, 'library/index.html')
#     model = Post
#     template_name = 'library/library.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = PAGINATION_COUNT

#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)

#         all_users = []
#         data_counter = Post.objects.values('author')\
#             .annotate(author_count=Count('author'))\
#             .order_by('-author_count')[:6]

#         for aux in data_counter:
#             all_users.append(MyUser.objects.filter(pk=aux['author']).first())
#         # if Preference.objects.get(user = self.request.user):
#         #     data['preference'] = True
#         # else:
#         #     data['preference'] = False
#         data['preference'] = Preference.objects.all()
#         # print(Preference.objects.get(user= self.request.user))
#         data['all_users'] = all_users
#         print(all_users, file=sys.stderr)
#         return data


class PostDetailView(DetailView):
    model = Post
    template_name = 'library/library_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(post_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        data['form'] = NewCommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),
                              author=self.request.user,
                              post_connected=self.get_object())
        new_comment.save()

        return self.get(self, request, *args, **kwargs)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'library/post_delete.html'
    context_object_name = 'post'
    success_url = '/library'

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','description','code_snippet','github','download','images']
    template_name = 'library/post_new.html'
    success_url = '/library'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Add a new post'
        return data


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','description','code_snippet','github','download','images']
    template_name = 'library/post_new.html'
    success_url = '/library'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Edit a post'
        return data

# Like Functionality====================================================================================

@login_required
def postpreference(request, postid, userpreference):
        
        if request.method == "POST":
                eachpost= get_object_or_404(Post, id=postid)

                obj=''

                valueobj=''

                try:
                        obj= Preference.objects.get(user= request.user, post= eachpost)

                        valueobj= obj.value #value of userpreference


                        valueobj= int(valueobj)

                        userpreference= int(userpreference)
                
                        if valueobj != userpreference:
                                obj.delete()


                                upref= Preference()
                                upref.user= request.user

                                upref.post= eachpost

                                upref.value= userpreference


                                if userpreference == 1 and valueobj != 1:
                                        eachpost.likes += 1
                                        eachpost.dislikes -=1
                                elif userpreference == 2 and valueobj != 2:
                                        eachpost.dislikes += 1
                                        eachpost.likes -= 1
                                

                                upref.save()

                                eachpost.save()
                        
                        
                                context= {'eachpost': eachpost,
                                  'postid': postid}

                                return redirect('library:home')

                        elif valueobj == userpreference:
                                obj.delete()
                        
                                if userpreference == 1:
                                        eachpost.likes -= 1
                                elif userpreference == 2:
                                        eachpost.dislikes -= 1

                                eachpost.save()

                                context= {'eachpost': eachpost,
                                  'postid': postid}

                                return redirect('library:home')
                                
                        
        
                
                except Preference.DoesNotExist:
                        upref= Preference()

                        upref.user= request.user

                        upref.post= eachpost

                        upref.value= userpreference

                        userpreference= int(userpreference)

                        if userpreference == 1:
                                eachpost.likes += 1
                        elif userpreference == 2:
                                eachpost.dislikes +=1

                        upref.save()

                        eachpost.save()                            


                        context= {'eachpost': eachpost,
                          'postid': postid}

                        return redirect('library:home')


        else:
                eachpost= get_object_or_404(Post, id=postid)
                context= {'eachpost': eachpost,
                          'postid': postid}

                return redirect('library:home')




