import unittest
import sys
import app
def test():
    print "++++++++++++++++++++++++++++test+++++++++++++++++++++++++++++++++++"
    tests = unittest.TestLoader().discover('tests', pattern='*_tests.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1

def cleanup():
    pass

def runserver():
    print "++++++++++++++++++++++++++runserver+++++++++++++++++++++++++++++++++"
    app.main()

if __name__ == '__main__':
    _app = sys.modules[__name__]
    func=sys.argv[1]
    if func in dir(_app):
        setattr(_app, 'sh', getattr(_app, func))
        sh()
    else:
        print "No func executed"
