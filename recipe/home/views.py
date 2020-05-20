from django.shortcuts import render, redirect
from .forms import RecipeParseForm
from .models import RecipeRequests
from recipe_scrapers import WebsiteNotImplementedError as unknown_site
from recipe_scrapers import scrape_me


def home(request):
    if request.method == "POST":
        form = RecipeParseForm(request.POST)
        try:
            if form.is_valid():
                recipe_url = form.cleaned_data.get("recipe_url")
                scraper = scrape_me(recipe_url)
                recipe_tld = scraper.host()
                title = scraper.title()
                ingredients = scraper.ingredients()
                instructions = scraper.instructions()

                # Save result to DB
                row = RecipeRequests(
                    recipe_site_tld=recipe_tld[0:149],
                    recipe_title=title[0:79],
                    recipe_parsed=True,
                )
                row.save()

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
            recipe_tld = message[message.find("(") + 1 : message.find(")")]

            # Save result to DB
            row = RecipeRequests(
                recipe_site_tld=recipe_tld[0:149],
                recipe_title="na",
                recipe_parsed=False,
            )
            row.save()

            return render(request, "home/home.html", {"form": form, "message": message})

    else:
        form = RecipeParseForm()

    return render(request, "home/home.html", {"form": form})
