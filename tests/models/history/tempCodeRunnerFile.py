import json
from models.history_model import HistoryModel


# Req. 7
def sample_history_data():
    return [
        {
            "text": "Hello World",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text": "Goodbye World",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]


def test_request_history():
    dict_1 = sample_history_data()[0]
    dict_2 = sample_history_data()[1]

    history = json.loads(HistoryModel.list_as_json())
    assert dict_1 in history
    assert dict_2 in history
    assert len(history) == 2
