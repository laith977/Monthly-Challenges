from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

monthly_challenges = {
    "january": "Try a new hobby or skill and practice it weekly!",
    "february": "Write down three things you're grateful for every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Commit to drinking at least 2 liters of water daily!",
    "may": "Walk for at least 10,000 steps every day!",
    "june": "Spend 30 minutes reading every day!",
    "july": "Try a new recipe each week and share it with friends or family!",
    "august": "Meditate for 10 minutes every day!",
    "september": "Declutter one area of your home each week!",
    "october": "Commit to a fitness routine 4 times a week!",
    "november": "Take a photo each day to capture moments of joy!",
    "december": "Spend 20 minutes reflecting on the year and planning goals for the next!"
}


# Create your views here.

# def january(request):
#     return  HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return  HttpResponse("Walk for at least 20 minutes every day!")

# def march(request):
#     return  HttpResponse("Learn Django for at least 20 minutes every day!")


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")