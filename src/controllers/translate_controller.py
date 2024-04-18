from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET"])
def translate():
    languages = LanguageModel.list_dicts()
    params = {
        "languages": languages,
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated": "What do you want to translate?",
    }
    return render_template("index.html", **params)


@translate_controller.route("/", methods=["POST"])
def translate_post():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    params = {
        "text_to_translate": text_to_translate,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "translated": translated,
    }

    languages = LanguageModel.list_dicts()

    return render_template("index.html", languages=languages, **params)


@translate_controller.route("/reverse", methods=["POST"])
def reverse_translate():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    reversed_text = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    params = {
        "text_to_translate": reversed_text,
        "translate_from": translate_to,
        "translate_to": translate_from,
        "translated": text_to_translate,
    }

    languages = LanguageModel.list_dicts()

    return render_template("index.html", languages=languages, **params)
