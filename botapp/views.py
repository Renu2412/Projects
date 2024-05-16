from django.shortcuts import render, redirect
from django.views import View
from botapp.forms import RecipeForm
from botapp.langchain import askChefbot
# Create your views here.

class Home(View):
    def get(self,request):
        ai_recipe = request.session.get('ai_recipe','')
        form = RecipeForm()
        return render(request,'botapp/home.html',
                      {'form':form,'ai_recipe':ai_recipe})
    
    def post(self,request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipeMsg = form.cleaned_data['recipeMsg']
            ai_res_recipe = askChefbot(recipeMsg)
            request.session['ai_recipe'] = ai_res_recipe
        form = RecipeForm()
        return redirect('/')
