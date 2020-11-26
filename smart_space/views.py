from django.shortcuts import render

# Create your views here.

def index(request):
    
    context = {
        'id' : 1
    }
    return render(request, 'smart_space/index.html', context)


"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request))

    #It’s a very common idiom to load a template, 
    #fill a context and return an HttpResponse object with the result of the rendered template.
    return render(request, 'polls/index.html', context)
"""