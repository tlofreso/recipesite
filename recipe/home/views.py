from django.shortcuts import render, redirect
from .forms import RecipeParseForm
from recipe_scrapers import WebsiteNotImplementedError as unknown_site
from recipe_scrapers import scrape_me


def home(request):
    if request.method == "POST":
        form = RecipeParseForm(request.POST)
        try:
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
        except unknown_site as e:
            message = str(e)

            return render(request, "home/home.html", {"form": form, "message": message})

    else:
        form = RecipeParseForm()

    return render(request, "home/home.html", {"form": form})
