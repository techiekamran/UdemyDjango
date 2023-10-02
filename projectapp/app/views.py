from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

#static 
# def Jan(request):
#     return HttpResponse("January")

# def Feb(request):
#     return HttpResponse("This work Feb!")


monthly_challenge_dic =  {
    "January": "Jan",
    "February":"Feb",
    "March":"Mar",
    "April":"Apr",
    "May":"May",
    "June":"June",
    "July":"July",
    "August":"Aug",
    "September":"Sep",
    "October":"Oct",
    "November":"Nov",
    "December":"Dec", 
}

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenge_dic.keys())
    if month >len(months):
        return HttpResponseNotFound("Invalid Month!")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/app/" + redirect_month)

    # monthly_text=None
    # if month == 1:
    #     monthly_text = "This is the month of january"
    # elif month==2:
    #     monthly_text = "This is the month of  february"
    # elif month== 3:
    #     monthly_text = "This is the month of March"
    # else:
    #     return HttpResponseNotFound("This month number is not supported!")
    # return HttpResponse(monthly_text)


#dynamic
def monthly_challenge(request,month):
    monthly_text = monthly_challenge_dic
    try:
        months =  monthly_text[month.capitalize()]
        return HttpResponse(months)
    except:
        return HttpResponseNotFound("Month is not correct")    
    # if month == "january":
    #     monthly_text = "This is the month of " + month
    # elif month=="february":
    #     monthly_text = "This is the month of " + month
    # elif month == "March":
    #     monthly_text = "This is the month of " + month
    # else:
    #     return HttpResponseNotFound("This month is not supported!")
    # return HttpResponse(monthly_text)

    