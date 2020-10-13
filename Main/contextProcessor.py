from Main.models import Text_Post

def TP_content(request):
    posts = Text_Post.objects.all()
    return{"posts":posts}