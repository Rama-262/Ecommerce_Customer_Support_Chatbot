# 🛒 Simple Help Chat (E-commerce Chatbot)

## What this project is

This is a small web chatbot.
It helps people ask common questions like:

* Where is my order?
* How to cancel order?
* What is return policy?

The bot gives answers from saved questions and answers.

---

## How it works (simple idea)

User types a message →
System checks similar question →
Best answer is shown.

It does not think like a human, but it can match similar sentences.

---

## What is used

* Python
* Flask (to show web page)
* Simple text matching method (TF-IDF)

---

## Files inside

```
app.py        → main program
faq.json      → questions and answers
templates/    → webpage (chat screen)
```

---

## How to run

1. Open project folder
2. Install needed things:

```
pip install flask scikit-learn
```

3. Run:

```
python app.py
```

4. Open browser and go to:

```
http://127.0.0.1:5000
```

---

## Try asking

* track my order
* cancel order
* payment options
* return product

---

## Small notes

* If question is very different, bot may not answer correctly
* You can add more questions in `faq.json`

---

## Idea for future

* Add voice input
* Save chat history
* Make design better

---

## Made by

Rama Yangaldas


If this helps you, you can use it and improve it 🙂
