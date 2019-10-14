from django.shortcuts import render, redirect
from .models import Question, Choice
import random

# Create your views here.

def index(request):
    total = Question.objects.all()
    question_id = random.randrange(0, len(total)) 
    question = total[question_id]

    cnt1 = Choice.objects.filter(question =question.id,pick ='1').count()
    cnt2 = Choice.objects.filter(question =question.id,pick ='2').count()
    context ={
        'question':question,
        'cnt1':cnt1,
        'cnt2':cnt2,
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content_a = request.POST.get('content_a')
        content_b = request.POST.get('content_b')

        Question.objects.create(title=title, content_a=content_a, content_b=content_b)

        return redirect('questions:index')

    else:
        return render(request, 'form.html')

def delete(request, id):
    Question.objects.get(id=id).delete()
    return redirect('questions:index')

def comments(request, id):
    question = Question.objects.get(id=id)
    cnt1 = Choice.objects.filter(question =id,pick ='1').count()
    cnt2 = Choice.objects.filter(question =id,pick ='2').count()
    context ={
        'question':question,
        'cnt1':cnt1,
        'cnt2':cnt2,
    }

    if request.method=="POST":
        comment = request.POST.get('comment')
        user_name = request.POST.get('user_name')
        pick = request.POST.get('pick')

        Choice.objects.create(question=question, comment=comment, user_name=user_name, pick=pick)
        return redirect('questions:comments', id)

    else:
        return render(request, 'comments.html', context)
    
def edit(request, id):
    question = Question.objects.get(id=id)
    context = {
        'question': question
    }

    if request.method =='POST':
        title = request.POST.get('title')
        content_a = request.POST.get('content_a')
        content_b = request.POST.get('content_b')
        
        question.title = title
        question.content_a = content_a
        question.content_b = content_b
        question.save()

        return redirect('questions:index')


    else:
        return render(request, 'edit.html', context)

def comments_delete(request, question_id, choice_id):
    choice = Choice.objects.get(id = choice_id)
    choice.delete()


    return redirect('questions:comments', question_id)

        

def lists(request):
    questions = Question.objects.all()
    context = {
        'questions':questions
    }
    return render(request,'lists.html',context)