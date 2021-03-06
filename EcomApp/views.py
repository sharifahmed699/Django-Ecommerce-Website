from django.shortcuts import render,HttpResponse,redirect, HttpResponseRedirect,reverse
from EcomApp.models import Setting,ContactMessage,ContactForm,FAQ
from Product.models import Product,Images,Category,Comment
from .forms import SearchForm
from OrderApp.models import ShopCart

# Create your views here.
def Home(request):
    current_user=request.user
    cart_product=ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for p in cart_product:
        total_amount+=p.product.new_price*p.quantity

    total_quan = 0
    for p in cart_product:
        total_quan += p.quantity

    category=Category.objects.all()
    setting=Setting.objects.get(id=1)
    slider=Product.objects.all().order_by('id')[:3]
    new_product=Product.objects.all().order_by('-id')
    featured_product=Product.objects.all()
    context={
        'setting': setting,
        'slider':slider,
        'new_product':new_product,
        'featured_product':featured_product,
        'category':category,
        'cart_product':cart_product,
        'total_amount':total_amount,
        'total_quan':total_quan,
    
    }
    return render(request,'home.html',context)


def Single_product(request,id):
    category=Category.objects.all()
    setting=Setting.objects.get(id=1)
    single_product=Product.objects.get(id=id)
    images=Images.objects.filter(product_id=id)
    products=Product.objects.all().order_by('id')[:4]
    comment_show=Comment.objects.filter(product_id=id,status='True')
    context={
        'setting': setting,
        'single_product':single_product,
        'images':images,
        'products':products,
        'category':category,
        'comment_show':comment_show,
    }
    return render(request,'single_product.html',context)


def category_product(request,id,slug):
    category=Category.objects.all()
    setting=Setting.objects.get(id=1)
    product_cat=Product.objects.filter(category_id=id)
    slider=Product.objects.all().order_by('id')[:3]
    context={
        'product_cat':product_cat,
        'setting': setting,
        'category':category,
        'slider':slider
    }
    return render(request,'category_product.html',context)

def About(request):
    category=Category.objects.all()
    setting=Setting.objects.get(id=1)
    context={
        'setting': setting,
        'category':category,
    }
    return render(request,'about.html',context)

def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Profile details updated.')

            return redirect('contact_dat')

    form = ContactForm
    category=Category.objects.all()
    setting=Setting.objects.get(id=1)

    context = {
        'form': form,
        'category':category,
        'setting': setting,
    }
    return render(request, 'contact_form.html', context)

def SearchView(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(
                    title__icontains=query, category_id=cat_id)
            category = Category.objects.all()
            slider = Product.objects.all().order_by('id')[:2]
            setting = Setting.objects.get(pk=1)
            context = {
                'category': category,
                'query': query,
                'product_cat': products,
                'slider': slider,
                'setting': setting,
            }
            return render(request, 'category_product.html', context)
    return HttpResponseRedirect('category_product')



def Faq_details(request):
    category=Category.objects.all()
    setting=Setting.objects.get(id=1)
    faq=FAQ.objects.filter(status=True).order_by('created_at')

    context = {
        'faq': faq,
        'category':category,
        'setting': setting,
    }
    return render(request, 'faq.html', context)
