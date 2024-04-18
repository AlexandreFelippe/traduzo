from flask import Blueprint, render_template
from models.language_model import LanguageModel

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET"])
def translate():
    languages = LanguageModel.list_dicts()
    params = {
        "languages": languages,
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated": "What do you want to translate?"
    }
    return render_template("index.html", **params)
