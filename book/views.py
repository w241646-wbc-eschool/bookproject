from django.contrib.auth.mixins import LoginRequiredMixin #コード追記（5-10（P.249））
from django.core.exceptions import PermissionDenied #コード追記（5-11（P.254））
from django.shortcuts import render, redirect #コード追記（5-5（P.193））

# Create your views here.
## from django.contrib.auth import logout #コード追記（5-5（P.193））
from django.urls import reverse, reverse_lazy #コード追記（4-9（P.157））（5-7（P.228））
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView #コード追記（4-5）（4-6）（4-9）（4-10（P.159））（4-11（P.159））
from .models import Book, Review #コード追記（4-5）（5-7（P.216））
from django.db.models import Avg #コード追記（5-12（P.260））

from django.core.paginator import Paginator #コード追記（5-14（P.270））
from .consts import ITEM_PER_PAGE #コード追記（5-14（P.270））

class LBView(LoginRequiredMixin, ListView): #コード追記（4-5）（5-10（P.249））
  template_name = 'book/book_list.html' #コード追記（4-5）
  model = Book #コード追記（4-5）
  paginate_by = ITEM_PER_PAGE #コード追記（5-14（P.277））

class DBView(LoginRequiredMixin, DetailView): #コード追記（4-6）（5-10（P.249））
  template_name = 'book/book_detail.html' #コード追記（4-6）
  model = Book #コード追記（4-6）

class CBView(LoginRequiredMixin, CreateView): #コード追記（4-9）（5-10（P.249））
  template_name = 'book/book_create.html' #コード追記（4-9）
  model = Book #コード追記（4-9）
  fields = ('title', 'text', 'category', 'thumbnail') #コード追記（4-9）コード修正（5-8）
  success_url = reverse_lazy('list-book') #コード追記（4-9（P.157））

  #コード修正（5-11（P.258））
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DelBView(LoginRequiredMixin, DeleteView): #コード追記（4-10（P.159））（5-10（P.249））
  template_name = 'book/book_confirm_delete.html' #コード追記（4-10）
  model = Book #コード追記（4-10）
  success_url = reverse_lazy('list-book') #コード追記（4-10）

  #コード追記（5-11（P.258））
  def get_object(self, queryset=None):
    obj = super().get_object(queryset)

    if obj.user != self.request.user:
      raise PermissionDenied

    return obj

class UBView(LoginRequiredMixin, UpdateView): #コード追記（4-11（P.162））（5-10（P.249））
  template_name = 'book/book_update.html' #コード追記（4-11）
  model = Book #コード追記（4-11）
  fields = ('title', 'text', 'category', 'thumbnail') #コード追記（4-11）コード修正（5-8）
  # success_url = reverse_lazy('list-book') #コード追記（4-11）コード削除（5-11(p.256)）

  #コード追記（5-11（P.254））
  def get_object(self, queryset=None):
    obj = super().get_object(queryset)

    if obj.user != self.request.user:
      raise PermissionDenied

    return obj

  #コード追記（5-11（P.256））
  def get_success_url(self):
    return reverse('detail-book', kwargs={'pk':self.object.id})


from django.core.paginator import PageNotAnInteger, EmptyPage

#コード追記（5-2（P.175））
def index_view(request):
  # print('index_view is called')
  # return render(request, 'book/index.html', {'somedata': 100})
  # object_list = Book.objects.all() #コード追記（5-3（P.179））
  object_list = Book.objects.order_by('-id') #コード追記（5-3（P.182））コード修正（5-11（P.259））
  ranking_list = Book.objects.annotate(avg_rating = Avg('review__rate')).order_by('-avg_rating') #コード追記（5-12（P.260））  

  # コード追記（5-14（P.270））
  paginator = Paginator(ranking_list, ITEM_PER_PAGE)
  page_number = request.GET.get('page', 1)

  try:
    page_obj = paginator.page(page_number)
  except PageNotAnInteger:
    page_obj = paginator.page(1)
  except EmptyPage:
    page_obj = paginator.page(paginator.num_pages)

  # query = request.GET['number']
  # print(query)

  return render(
    request,
    'book/index.html',
    {'object_list': object_list, 'ranking_list': ranking_list, 'page_obj':page_obj }) #コード追記（5-3（P.179）） コード修正（5-12（P.260））コード修正（5-14（P.270））
  
#コード追記（5-5（P.193））
'''
def logout_view(request):
  logout(request)
  return redirect('index')
'''

#コード追記（5-7（P.216））
class CRView(CreateView):
  model = Review
  fields = ('book', 'title', 'text', 'rate')
  template_name = 'book/review_form.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
    ## print(context)
    return context

#コード追記（5-7（P.227））
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

#コード追記（5-7（P.229））
  def get_success_url(self):
    return reverse('detail-book', kwargs={'pk': self.object.book.id})



# オリジナルコード
def my_view(request):
    return render(request, 'my_template.html', {
        'item_per_page': ITEM_PER_PAGE
    })