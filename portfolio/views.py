from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import feedback
from django.template import loader
from django.shortcuts import render,redirect,reverse
from django.views.generic import TemplateView
from .models import feedbackform, Signupform, Profile, Profileform
from django.contrib.auth import authenticate, login, logout
"""
def index(request):
    feedback_list = feedback.objects.all()
    template = loader.get_template('portfolio/index.html')
    context = {
        'feedback_list': feedback_list,
    }
    return HttpResponse(template.render(context, request))
"""
class index(TemplateView):
    template_name = 'portfolio/index.html'

#def feedback_view(request, feedback_id):
#    feedback_list = feedback.objects.all()
#    fb = feedback.objects.get(pk=feedback_id)
#    return render(request, 'porfolio/feedback.html', {'feedback': fb})
"""
def feedback_view(request):
    return render(request, 'portfolio/feedback.html')
    """

class feedbackView(TemplateView):
    template_name = 'portfolio/feedback.html'
    def post(self, request):
        fb = feedbackform(request.POST)
        if fb.is_valid():
            text = fb.cleaned_data['feedback']
            fb.save()
            return redirect('index/')

        args = {'feedback': fb, 'text': text}
        return render(request, self.template_name, args)
"""
class signupView(TemplateView):
    template_name = 'portfolio/signup.html'
    def post(self, request):
        sg = Signupform(request.POST)
        if sg.is_valid():
            text = sg.cleaned_data['username']
            sg.save()
            return redirect('index/')

        args = {'signup': sg, 'text': text}
        return render(request, self.template_name, args)
  """

def signup(request):
    template_name = 'portfolio/signup.html'
    context ={}
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            form.save()
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('account/')

        return render(request, template_name)
    else:
        form = Signupform()
        return render(request, 'portfolio/signup.html', {"signup": form})

def user_login(request):
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passw')
        myUsers = authenticate(request, username = username, password = password)
        if myUsers:
            login(request,myUsers)
            return redirect('account/')
        else:
            context["error"] = "Invalid credentials"
            return render(request, "portfolio/login.html", context)
    else:
        return render(request, "portfolio/login.html", context)

def login_success(request):
    context={}
    project_form = Profileform()
    user = request.user
    temp = Profile.objects.filter(members = user)
    print ("user id is :")
    print(request.user.id)
    # temp.save()
    #print(temp)
    #print(temp.members.all())
    #project_form.save()
    #print(project_form.user.all())
    #project_form.objects.all()
    context['user'] = request.user
    context['project_form'] = project_form
    context['projects'] = temp
    return render(request, "portfolio/account.html", context)

def user_logout(request):
    context={}
    if request.method == 'POST':
        logout(request)
        return render(request, "portfolio/login.html", context)


class profile_view(TemplateView):
    template_name = 'portfolio/account.html'
    def post(self, request):
        fb = Profileform(request.POST)
        if fb.is_valid():
            text = fb.cleaned_data['project_name']
            fb.save()
            #print(fb.members.objects.all())
            return redirect('../../portfolio/login/account/')

        args = {'project_name': fb, 'text': text}
        return render(request, self.template_name, args)

    def get(self,request):
        return redirect('account/')


"""
def feedbackView(request):
    if request.method == 'POST':
        fb = feedback(request.POST)
        fb.save()
        fb.refresh_from_db
        if fb.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/index/')

            """