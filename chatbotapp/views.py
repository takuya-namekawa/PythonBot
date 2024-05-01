from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
#AutoModelForQuestionAnsweringは質問応答する機能
#BertJapaneseTokenizerは日本語のテキストをトークン化
from transformers import AutoModelForQuestionAnswering, BertJapaneseTokenizer
import torch
from django.views.generic import TemplateView

#KoichiYasuoka/bert-base-japanese-wikipedia-ud-headのモデルを利用して質問応答することを設定しています。
model_name = 'KoichiYasuoka/bert-base-japanese-wikipedia-ud-head'
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Create your views here.
def home(request):
    categories = Category.objects.all() #Categoryモデルから全データを取得
    return render(request, 'home.html', { 'categories' : categories})# categories変数をテンプレートに渡す


def reply(categories):

    tokenizer = BertJapaneseTokenizer.from_pretrained(model_name)
    print(categories)
    if categories == "通信費":
        context = '通信費は2000円'
    elif categories == "固定費":
        context = '固定費は5000円'
    else:
        context = 'その他'


    inputs = tokenizer.encode_plus(context , add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]
    output = model(**inputs)
    answer_start = torch.argmax(output.start_logits)
    answer_end = torch.argmax(output.end_logits) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
    answer = answer.replace(' ', '')

    return answer


def bot_response(request):

  
    category_name = request.POST.get('category')

    if  not category_name:
        return HttpResponse('<h2>空のデータを受け取りました</h2>', status=400)
    
    bot_response = reply(category_name)
    http_response = HttpResponse()
    http_response.write(f"BOT: {bot_response}")

    return http_response
