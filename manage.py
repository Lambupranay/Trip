from app import app, db
from flask_migrate import Migrate
from flask.cli import with_appcontext
import click

# Initialize Migrate
migrate = Migrate(app, db)

# Define the main entry point for Flask's CLI to use the migration commands
@app.cli.command("db")
@with_appcontext
def db_commands():
    """Runs database migrations."""
    from flask_migrate import upgrade, migrate, init

    # Initialize migrations
    init()
    # Create migration files based on changes in models
    migrate()
    # Apply migrations to the database
    upgrade()

if __name__ == '__main__':
    app.run(debug=True)
