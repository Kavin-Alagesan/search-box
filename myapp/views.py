import requests
from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.

def create(request):  
    if request.method=='POST':
        print('xxxxxxxxxxxxxxxxxxxxxxx create xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        title=request.POST['title']
        post=request.POST['post']
        author=request.POST['author']
        post_regarding=request.POST['post_regarding']
        contact=request.POST['contact']
        brief_about_post=request.POST['brief_about_post']
        image=request.FILES.get('image')
        data={
            'title':title,
            'post':post,
            'author':author,
            'post_regarding':post_regarding,
            'contact':contact,
            'brief_about_post':brief_about_post,
            }
        file={
            'image':image
        }
        url="http://127.0.0.1:8000/api/api/"
        response=requests.post(url, data=data,files=file)
        messages.success(request,("Blog posted successfully"))
        return redirect('create')
    url="http://127.0.0.1:8000/api/api/"
    response=requests.get(url).json()
    print('---------------------------- refresh --------------------------------------------')
    data = response
    return render(request,'sidenav.html',{'data':data})
    
def update(request,id):
    if request.method=='POST':
        title=request.POST['title']
        print(f'==========+============= update ==========================')
        post=request.POST['post']
        author=request.POST['author']
        post_regarding=request.POST['post_regarding']
        contact=request.POST['contact']
        brief_about_post=request.POST['brief_about_post']
        image=request.FILES.get('image')
        data={
            'title':title,
            'post':post,
            'author':author,
            'post_regarding':post_regarding,
            'contact':contact,
            'brief_about_post':brief_about_post,
            }
        file={
            'image':image
        }
        response=requests.put("http://127.0.0.1:8000/api/api/{pk}/".format(pk=id), data=data,files=file)
        messages.success(request,("Blog Edited successfully"))
        return redirect('create')
    print(f'==========+============= update-else ==========================')
    return render(request,'sidenav.html',{'data':data})

def delete(request,id):
    response=requests.delete("http://127.0.0.1:8000/api/api/{pk}/".format(pk=id))
    messages.success(request,("Blog deleted successfully"))
    return redirect('create')

def details(request):
    url="http://127.0.0.1:8000/api/search/"
    response=requests.get(url).json()
    print('----------------search list -----------------')
    data = response
    return render(request,'details/collect_details.html',{'data':data})

    



