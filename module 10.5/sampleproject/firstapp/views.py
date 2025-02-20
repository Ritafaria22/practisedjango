from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author' : 'faria', 'age': 20, 'list' : [1,2,3], 'val' : ['monday','sun','bad'],
         'cap': 'chistmas', 'slash': "i'm hungry", 'students' : [
             {'name' : 'zakia'},
             {'name' : 'hasan'},
             {'name' : 'abdullah'}
         ], 'tag' : "<p>This <em>should be</em> fun!</p>" , 
         'fruits': ['mango','banana', 'apple'], 'names': "abdullah",
         'line' : "one\n two\n three",
         'up': 'today is friday', 'low' : 'I Am Ready', 'tytle': 'its a new dress',
          'randomm': ['blue','black','red'], 'centerr':"hello", 'cutt' : "hello adnan",
          'birthday': datetime.datetime.now(), 'size': 4432,'join':["red","silk","purple"],
          'time': datetime.datetime(2025, 2, 6, 9, 35),
          'posttime': datetime.datetime(2025, 2, 4, 8, 35),'now': datetime.datetime.now(),
          'var': "<p>This is a <strong>bold</strong> paragraph with <strong>emphasized</strong> text.</p>",
          'count': 4
         }
    return render(request, "home.html", d)


def about(request):
    return render(request, 'firstapp/about.html')
def contact(request):
    return render(request, 'firstapp/contact.html')
