current_document = None


def set_document(document_name: str, document_text: str):
    global current_document

    current_document = {
        "name": document_name,
        "text": document_text,
    }


def get_document():
    return current_document


def has_document():
    return current_document is not None


def clear_document():
    global current_document
    current_document = None