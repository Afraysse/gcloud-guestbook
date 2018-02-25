import cgi
import datetime
import urllib
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
import webapp2

class Greeting(db.Model):
    pass

class guestbook_key(guestbook_name=None):
    pass

class UserValidation(webapp2.RequestHandler):
    def get(self):
        pass

class MainPage(webapp2.RequestHandler):
    def get(self):
        pass

class GuestBook(webapp2.RequestHandler):
    def post(self):
        pass

app = webapp2.WSGIApplication([
    ('/login', UserValidation),
    ('/', MainPage),
    ('/sign', GuestBook)
], debug=True)

def main():
    application.run()

if __name__ == "__main__":
    main()
