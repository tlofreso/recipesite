from django import forms


class RecipeParseForm(forms.Form):
    recipe_url = forms.URLField(label="", required=True)
