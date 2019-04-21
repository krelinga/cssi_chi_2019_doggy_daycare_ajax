import webapp2


class GetDogsHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write("hello API!")


app = webapp2.WSGIApplication([
    ('/api/getdogs', GetDogsHandler),
], debug=True)
