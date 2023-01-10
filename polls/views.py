from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import QuestionForm
from .models import Question


User=get_user_model()


def home_main(request):
    questions=Question.objects.all()
    context={'questions':questions}
    if request.user.is_authenticated:
        return render(request,'Home/home.html',context)
    else:
        return render(request,'main.html',context)


def create_question(request):  
    form=QuestionForm()
    if request.method == 'POST':
        form=QuestionForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'Home/create-question.html',context)


def user_profile(request,pk):
    user=User.objects.get(id=pk)
    questions=user.question_set.all()
    context={'user':user,'questions':questions}
    return render(request,'Home/profile.html',context)

def vote(request):
    pass

# if request.method == 'POST':
#         print(request.POST)
#         questions=QuesModel.objects.all()
#         score=0
#         wrong=0
#         correct=0
#         total=0
#         for q in questions:
#             total+=1
#             print(request.POST.get(q.question))
#             print(q.ans)
#             print()
#             if q.ans ==  request.POST.get(q.question):
#                 score+=10
#                 correct+=1
#             else:
#                 wrong+=1
#         percent = score/(total*10) *100
#         context = {
#             'score':score,
#             'time': request.POST.get('timer'),
#             'correct':correct,
#             'wrong':wrong,
#             'percent':percent,
#             'total':total
#         }
#         return render(request,'Quiz/result.html',context)
#     else:
#         questions=QuesModel.objects.all()
#         context = {
#             'questions':questions
#         }
#         return render(request,'Quiz/home.html',context)

