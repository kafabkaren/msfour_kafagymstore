from django.shortcuts import render

def view_blog(request):
    """ A view to render the blog page content """
    
    return render(request, 'blog.html', {})
