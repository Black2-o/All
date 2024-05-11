import random
import ast
from .models import Word
from django.shortcuts import render, redirect





def home(request):
    words = Word.objects.all()
    word = random.choice(words)
    display = []
    wordX = word.name
    lives = 6

    for x in word.name:
        if x == word.name[0]:
            display.append(word.name[0])
        else:
            display.append("_")
    contex = {
        "word": word,
        "display": display,
        "lives": lives,
        "msg": "",
        "game_is_on" : True
    }
    return render(request, "index.html", contex)


def start(request):
    msg = ""
    if request.method == "POST":
        letter = request.POST.get('letter')
        word = request.POST.get('word')
        display = ast.literal_eval(request.POST.get("display"))
        lives = ast.literal_eval(request.POST.get("lives"))
        game_is_on = True
        
        if letter in word:
            if letter in display:
                msg = f"You already guessed {letter}"

            
            for position in range(len(display)):
                wordY = word[position]
                if wordY == letter:
                    display[position] = letter
                    x = ''.join(display)
                    if word == x:
                        word = Word.objects.get(name=word)
                        msg = f"Yeah The Word Is {word} which mean {word.bangla_mean}"
                        game_is_on = False
                        contex = {
                                    "word": word,
                                    "display": display,
                                    "lives": lives,
                                    "msg": msg,
                                    "game_is_on":game_is_on
                                }
                        return render(request, 'index.html', contex)
        elif letter not in display:
            lives -= 1
            print(lives)
            if lives == 0:
                word = Word.objects.get(name=word)
                msg = f"You Lose. The Word Was {word} which mean {word.bangla_mean}"
                game_is_on = False
        contex = {
                    "word": word,
                    "display": display,
                    "lives": lives,
                    "msg": msg,
                    "game_is_on":game_is_on
                }
        return render(request, 'index.html', contex)
    return render(request, "sorry.html")



def add(request):
    if request.method == "POST":
        eng = request.POST.get('eng')
        ban = request.POST.get('ban')
        print(eng)
        print(ban)
        if eng != "" and ban != "":
            word = Word.objects.create(
                name=eng,
                bangla_mean=ban,
            )
        else:
            print("SORRY NOT ADDED.")
    return render(request, "add.html")


def dashboard(request):
    word = words = Word.objects.all()
    contex= {
        "words": word,
    }
    return render(request, "dashboard.html", contex)


def delete(request, id):
    delete_word = Word.objects.get(id=id)
    delete_word.delete()
    word = words = Word.objects.all()
    contex= {
        "words": word,
    }
    return redirect("dashboard")
