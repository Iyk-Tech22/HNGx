from app import create_app
from app.models import Person

app = create_app()

@app.shell_context_processor
def shell_context():
    return {"person":Person}