from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
# Create your views here.
def home(request):
    categories = Category.objects.all() #Categoryモデルから全データを取得
    return render(request, 'home.html', { 'categories' : categories})# categories変数をテンプレートに渡す


def reply(category_name):

    try:
        category = Category.objects.get(name=category_name)
        return category.exp if category.exp else '該当する説明がありません。'
    except Category.DoesNotExist:
        return '該当するカテゴリーが見つかりません。'

def bot_response(request):

  
    category_name = request.POST.get('category')

    if  not category_name:
        return HttpResponse('<h2>空のデータを受け取りました</h2>', status=400)
    
    bot_response = reply(category_name)
    http_response = HttpResponse()
    http_response.write(f"BOT: {bot_response}")

    return http_response
