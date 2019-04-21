import webapp2
import json
import time


class GetDogsHandler(webapp2.RequestHandler):
  def get(self):
    # A little delay to see the loading message...
    time.sleep(3)
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(json.dumps({'message': 'hello json!'}))


app = webapp2.WSGIApplication([
    ('/api/getdogs', GetDogsHandler),
], debug=True)
