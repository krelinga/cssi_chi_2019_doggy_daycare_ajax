import webapp2
import json
import time

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
    self.response.write(json.dumps(dog_info))


app = webapp2.WSGIApplication([
    ('/api/getdogs', GetDogsHandler),
], debug=True)
