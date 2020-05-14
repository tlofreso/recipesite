from django.shortcuts import render
from .forms import RecipeParseForm
from recipe_scrapers import scrape_me


def home(request):
    if request.method == "POST":
        form = RecipeParseForm(request.POST)
        if form.is_valid():
            recipe_url = form.cleaned_data.get("recipe_url")
            scraper = scrape_me(recipe_url)
            title = scraper.title()
            ingredients = scraper.ingredients()
            instructions = scraper.instructions()

        return render(
            request,
            "home/home.html",
            {
                "form": form,
                "title": title,
                "ingredients": ingredients,
                "instructions": instructions,
            },
        )

    else:
        form = RecipeParseForm()

    return render(request, "home/home.html", {"form": form})
