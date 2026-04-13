import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# ---------------- CHAT PAGE ----------------
@login_required
def chat_page(request):
    return render(request, "chat.html")


# ---------------- CHAT API ----------------
@csrf_exempt
@login_required
def chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower().strip()

        # -----------------------------
        # SMART RULE-BASED AI RESPONSES
        # -----------------------------

        # Greetings
        if user_message in ["hi", "hello", "hii", "hey"]:
            reply = "Hello 👋 How can I help you today?"

        elif "good morning" in user_message:
            reply = "Good morning ☀️ Have a wonderful day ahead!"

        elif "good afternoon" in user_message:
            reply = "Good afternoon 🌤️ Hope your day is going well!"

        elif "good evening" in user_message:
            reply = "Good evening 🌙 Relax and enjoy your time!"

        elif "good night" in user_message:
            reply = "Good night 🌙 Sweet dreams!"

        # Thanks
        elif "thank" in user_message:
            reply = "You're welcome 😊 Happy to help you!"

        # Name
        elif "your name" in user_message:
            reply = "I am SmartChat AI 🤖 built with Django"

        # How are you
        elif "how are you" in user_message:
            reply = "I'm doing great 😊 What about you?"

        # Bye
        elif user_message in ["bye", "goodbye", "see you"]:
            reply = "Goodbye 👋 Take care!"

        # Django
        elif "django" in user_message:
            reply = "Django is a powerful Python web framework 🚀 used for web apps"

        # Python
        elif "python" in user_message:
            reply = "Python is a popular programming language 🐍 easy and powerful"

        # AI
        elif "ai" in user_message:
            reply = "AI means Artificial Intelligence 🤖 like ChatGPT and Gemini"

        # Motivation
        elif "motivate" in user_message or "motivation" in user_message:
            reply = "Believe in yourself 💪 You can achieve anything!"

        # Time / Help
        elif "help" in user_message:
            reply = "I can answer greetings, Django, Python, AI, motivation etc."

        # Default response
        else:
            reply = "🤖 I'm still learning. Try: hi, good morning, django, python, ai"

        return JsonResponse({"reply": reply})

    return JsonResponse({"reply": "Invalid request method"})