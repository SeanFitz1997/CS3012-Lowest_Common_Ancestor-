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
                response = [{'Name': 'User', 'Total': 7056362, 'JavaScript': 4959458, 'HTML': 243166, 'CSS': 1733424, 'PHP': 2436, 'Python': 79858, 'C': 7626, 'Java': 25736, 'C++': 4658}, {'Name': 'CryptoDonator', 'Total': 2608215, 'JavaScript': 2021614, 'HTML': 108772, 'CSS': 476611, 'PHP': 1218}, {'Name': 'SoftwareEngineeringProject', 'Total': 2608215, 'JavaScript': 2021614, 'HTML': 108772, 'CSS': 476611, 'PHP': 1218}, {'Name': 'CS3012_SoftwareEngineering', 'Total': 867977, 'Python': 18336, 'CSS': 390069, 'JavaScript': 458115, 'HTML': 1457}, {'Name': 'DNS_Validator_API', 'Total': 7626, 'C': 7626}, {'Name': 'EBII1819--Trinity_Module_Review', 'Total': 896728, 'Python': 25270, 'HTML': 23210, 'CSS': 390133, 'JavaScript': 458115}, {'Name': 'ItunesPlaylist_Parser', 'Total': 4275, 'Python': 4275}, {'Name': 'python_machine_learning', 'Total': 31977, 'Python': 31977}, {'Name': 'Snake', 'Total': 26691, 'Java': 25736, 'HTML': 955}, {'Name': 'Socket-GET-request', 'Total': 4658, 'C++': 4658}]
                user_lang_info = response[0]
                user_repo_info = response[1:]
                repo_len = len(user_repo_info)

                context = {
                    'user_login' : g.get_user(),
                    'user_lang_info' : user_lang_info,
                    'user_repo_info' : user_repo_info,
                    'range' : range(repo_len)
                }
                return render(request, self.userViewTemplate, context)
            except:
                messages.add_message(request, messages.ERROR, 'Invalid Github details.')  
        return render(request, self.loginTemplate)

