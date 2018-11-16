from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from github import Github
import json
from .forms import UserForm
from Access_API.Access import getLangSkills, getRepoDetails

class userView(TemplateView):
    loginTemplate = 'User/login.html'
    userViewTemplate = 'User/userView.html'
    form_class = UserForm

    def get(self, request):
        context = {
            'form' : self.form_class
        }
        return render(request, self.loginTemplate, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid:
            try:
                g = Github(form.data['userName'], form.data['password'])
                #lang_info = getLangSkills(g) 
                
                context = {
                    'user_login' : g.get_user(),
                    'lang_info' : getLangSkills(g)
                }
                return render(request, self.userViewTemplate, context)
            except:
                messages.add_message(request, messages.ERROR, 'Invalid Github details.')  
        return render(request, self.loginTemplate)

