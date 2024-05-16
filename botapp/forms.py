from django import forms

class RecipeForm(forms.Form):
    recipeMsg = forms.CharField(max_length=255, 
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Enter dish name'}
                                ))