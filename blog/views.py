from django.shortcuts import render


#Tinymce





# Create your views here.

from blog.models import Post,PostextraImages

from math import ceil
from django.shortcuts import render, get_object_or_404


# Create your views here.
def blogHome(request): 

    allProds = []
    catprods = Post.objects.values('category', 'sno')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Post.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])


    params = {'allProds': allProds}
    return render(request, 'blog/blogHome.html', params)
    ''' allPosts= Post.objects.all()
   context={'allPosts': allPosts}
   return render(request, "blog/blogHome.html", context)
    '''

def blogPost(request, slug): 

    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blog/blogPost.html", context)




    #return HttpResponse(f'This is blogPost : {slug}')

'''
def detail_view(request,sno):
    post = get_object_or_404(Post, sno=sno)
    photos = .objects.filter(post=post)
    return render(request, 'blog/blogDetails4.html', {
        'post':post,
        'photos':photos
    })'''

'''
def blogProjects(request): 

    allProds = []
    catprods = Projects.objects.values('category', 'sno')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Projects.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])


    params = {'allProds': allProds}
    return render(request, 'blog/blogProjectsHome.html', params)


def blogProjectsPost(request, slugP): 

    post=Projects.objects.filter(slug=slugP).first()
    context={"post":post}
    return render(request, "blog/blogProjectsPost.html", context)

    #return HttpResponse(f'This is blogPost : {slug}')

def Projectsdetail_view(request,sno):
    post = get_object_or_404(PostTest, sno=sno)
    photos = realProjectsImage.objects.filter(post=post)
    return render(request, 'blog/blogProjectsDetails.html', {
        'post':post,
        'photos':photos
    })
'''
