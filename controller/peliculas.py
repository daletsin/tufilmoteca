import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
import json


class PelisPage(webapp2.RequestHandler):
    def get(self):
        pagi = 1
        titulo = Titulos.all()
        
        if self.request.get('pag') == '':
            pagi = 1
        else:
            pagi = int(self.request.get('pag'))
        perpag = 50

        url = "https://yifytorrents.p.mashape.com/list.json?limit="+str(perpag)+"&set="+str(pagi)+"&quality=ALL&rating=0&keywords=&genre=ALL&sort=date,quality&order=desc"


        pelis = urlfetch.fetch(url=url, headers={"X-Mashape-Authorization": "tV9ehv8er2EJPrK0DeBTmc8JkBk10iB8"})

        pelis = json.loads(pelis.content)

        pelis = pelis["MovieList"]

        pagsig = pagi + 1
        self.response.write(
            template.render('view/peliculas.html',
                            {'pelis': pelis, 'pagsig': pagsig}))

application = webapp2.WSGIApplication([('/peliculas',
                                        PelisPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
