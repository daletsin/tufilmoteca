import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
import json
import conf


class Peli(webapp2.RequestHandler):
    def get(self, tipo, numid):
        if tipo =='peliculas' and numid != '':
            url = "https://yifytorrents.p.mashape.com/movie.json?id="+str(numid)
            tit = urlfetch.fetch(url=url, headers={"X-Mashape-Authorization": conf.MASHAPE_KEY})
            tit = json.loads(tit.content)

            self.response.write(
                template.render('view/verfuentes.html',
                            {'tit': tit, 'conf':conf}))
            

application = webapp2.WSGIApplication([('/(?P<tipo>\w+)/(?P<numid>\d+)',
                                        Peli)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
