from django import forms


class RecipeParseForm(forms.Form):
    recipe_url = forms.URLField(label="Recipe Link", required=True)

    # class Meta:
    #     fields = ["email"]
