from app import create_app
from app.models import Person

app = create_app()

@app.shell_context_processor
def shell_session_context():
    """ Setting up shell context for app testing in the shell """
    return {"person":Person}