import webapp2
import json
import time
from google.appengine.api import users


def LoginDict(data, uri):
  current_user = users.get_current_user()
  if current_user:
    return { 'data': data, 'logout_url': users.create_logout_url(uri) }
  else:
    return { 'login_url': users.create_login_url(uri) }


def DogDict(name, status):
  return {'name': name, 'status': status }


class GetDogsHandler(webapp2.RequestHandler):
  def get(self):
    # A little delay to see the loading message...
    time.sleep(3)
    self.response.headers['Content-Type'] = 'application/json'
    dog_info = {
      'dogs': [
        DogDict("fido", "good"),
        DogDict("fluffy", "veryGood"),
        DogDict("zappp", "sleepy")
      ]
    }
    self.response.write(json.dumps(LoginDict(dog_info, '/')))


app = webapp2.WSGIApplication([
    ('/api/getdogs', GetDogsHandler),
], debug=True)
