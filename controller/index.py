import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
import json
import conf


class PelisPage(webapp2.RequestHandler):
    def get(self):
        pagi = 1
        
        if self.request.get('pag') == '':
            pagi = 1
        else:
            pagi = int(self.request.get('pag'))
        perpag = 50

        url = "https://yifytorrents.p.mashape.com/list.json?limit="+str(perpag)+"&set="+str(pagi)+"&quality=ALL&rating=0&keywords=&genre=ALL&sort=date,quality&order=desc"


        pelis = urlfetch.fetch(url=url, headers={"X-Mashape-Authorization": conf.MASHAPE_KEY})

        pelis = json.loads(pelis.content)

        pelis = pelis["MovieList"]

        pagsig = pagi + 1


        self.response.write(
            template.render('view/peliculas.html',
                            {'pelis': pelis, 'pagsig': pagsig, 'conf':conf}))

application = webapp2.WSGIApplication([('/',
                                        PelisPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
