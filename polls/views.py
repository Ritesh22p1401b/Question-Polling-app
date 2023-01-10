from django.shortcuts import render,redirect
from .forms import QuestionForm
from .models import Question
from django.contrib.auth import get_user_model

User=get_user_model()



def home_main(request):
    questions=Question.objects.all()
    context={'questions':questions}
    if request.user.is_authenticated:
        return render(request,'Home/home.html',context)
    else:
        return render(request,'main.html',context)

        

        


# def home(request):

#     questions=Question.objects.all()
#     context={'questions':questions}
#     return render(request,'Home/home.html',context)


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
