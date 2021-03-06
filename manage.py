from app import create_app
from flask_script import Manager, Server
import unittest
# Create an app instance to manipulate
app = create_app('development')


manager = Manager(app)
manager.add_command('server', Server)
@manager.command
def test():
    """Run the unit tests."""

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



if __name__ == '__main__':
    manager.run()