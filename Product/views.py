from django.shortcuts import render,HttpResponseRedirect
from Product.models import Comment,CommentForm
from django.contrib import messages

# Create your views here.

def comment_add(request,id):
    url=request.META.get('HTTP_REFERER')
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            data=Comment()
            data.subject=form.cleaned_data.get('subject')
            data.comment=form.cleaned_data.get('comment')
            data.rate=form.cleaned_data.get('rate')
            data.ip=request.META.get('REMOTE_ADDR')
            data.product_id=id
            current_user=request.user
            data.user_id=current_user.id
            data.save()
            messages.success(request, 'Your Commetn Has Been Sent !!')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
       