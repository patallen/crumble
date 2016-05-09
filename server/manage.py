from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_script import prompt, prompt_pass

from app import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app import models


@manager.command
def create_admin():
    email = prompt("Enter an email for this Administrator")
    pass1 = prompt_pass("Enter password")
    pass2 = prompt_pass("Re-enter password")

    if pass1 == pass2:
        admin = models.Admin(email=email)
        admin.password = pass1
        admin.save()
    else:
        print "Passwords do not match. Try again."


if __name__ == '__main__':
    manager.run()
