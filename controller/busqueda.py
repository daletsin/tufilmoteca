import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
import json
import conf
import pprint

class BusquedaPage(webapp2.RequestHandler):
    def get(self):
        buscar = self.request.get('buscar')

        buscar = buscar.replace(' ','+')
        
        if self.request.get('pag') == '':
            pagi = 1
        else:
            pagi = int(self.request.get('pag'))
        perpag = 50

        url = "https://yifytorrents.p.mashape.com/list.json?limit="+str(perpag)+"&set="+str(pagi)+"&quality=ALL&rating=0&keywords="+buscar+"&genre=ALL&sort=date,quality&order=desc"


        pelis = urlfetch.fetch(url=url, headers={"X-Mashape-Authorization": conf.MASHAPE_KEY})

        pelis = json.loads(pelis.content)

        
        if "MovieList" in pelis:
            pelis = pelis["MovieList"]
        else:
            pelis = ''

        pagsig = pagi + 1

        buscar_espacio = buscar.replace('+',' ')



        self.response.write(
            template.render('view/busqueda.html',
                            {'pelis': pelis, 'buscar': buscar, 'buscar_espacio':buscar_espacio, 'conf':conf, 'pagsig':pagsig}))

application = webapp2.WSGIApplication([('/busqueda',
                                        BusquedaPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()