# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.db.models import F, Q
from book.models import Book, Comment, Author

'''
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
    #return HttpResponse("Hello, world. You're at the poll index.")


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})  
    #return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
    
    
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
'''
def index(request):
    books = Book.objects.all() 
    return render(request, 'book/index.html', {'books': books})

    
def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book/detail.html', {'book': book})  


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['cart'] = {}
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('book:index'))
        else:
            # Return a 'disabled account' error message
            pass
    else:
        # Return an 'invalid login' error message.        
        return render(request, 'book/index.html', {'error_message': "Wrong username or password!"})  

        
def logout_view(request):
    logout(request)        
    return HttpResponseRedirect(reverse('book:index'))

def search_view(request):
    if request.GET.has_key('q'):
        kw = request.GET['q']
    else:
        kw = ''
    b1 = Book.objects.filter(title__contains=kw)
    b2 = Book.objects.filter(authors__name__icontains=kw)
    books = set(b1) | set(b2)
    ### this may cause duplicate records for which has many authors
    ##books = Book.objects.filter(Q(title__contains=request.GET['q']) | Q(authors__name__icontains=request.GET['q']))
    return render(request, 'book/search.html', {'books': books})

def pick_view(request):
    book_id = request.POST['book_id']
    print type(book_id)
    if request.session['cart'].has_key(book_id):
        qty = int(request.session['cart'][book_id]) + 1
    else:  
        qty = 1  
    request.session['cart'][book_id] = qty
    request.session.modified = True
    return HttpResponseRedirect(reverse('book:index', args=()))

def adjust_view(request):
    book_id = request.POST['book_id']
    qty = int(request.POST['qty'])
    if request.session['cart'].has_key(book_id):
        request.session['cart'][book_id] = qty
    if qty <= 0:
        del request.session['cart'][book_id]       
    request.session.modified = True    
    return HttpResponseRedirect(reverse('book:cart', args=()))


def cart_view(request):
    boughtItems = []
    for (book_id, qty) in request.session['cart'].iteritems():
        boughtItems.append({'book': Book.objects.get(pk=book_id), 'qty': qty})   
    return render(request, 'book/cart.html', {'boughtItems': boughtItems})

def checkout_view(request):
    totalPrice = 0
    for (book_id, qty) in request.session['cart'].iteritems():
        totalPrice += Book.objects.get(pk=book_id).price * qty
    request.session['totalPrice'] = totalPrice
    request.session.modified = True 
    return render(request, 'book/bills.html', {'totalPrice': totalPrice})

def confirm_view(request):
    request.session['cart'] = {}
    return HttpResponseRedirect(reverse('book:index', args=()))

