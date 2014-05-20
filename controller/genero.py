import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
import json
import conf


class GeneroPage(webapp2.RequestHandler):
    def get(self, genero):
        
        if self.request.get('pag') == '':
            pagi = 1
        else:
            pagi = int(self.request.get('pag'))
        perpag = 50

        genero = genero.replace('_','-')

        url = "https://yifytorrents.p.mashape.com/list.json?limit="+str(perpag)+"&set="+str(pagi)+"&quality=ALL&rating=0&keywords=&genre="+genero+"&sort=date,quality&order=desc"

        pelis = urlfetch.fetch(url=url, headers={"X-Mashape-Authorization": conf.MASHAPE_KEY})

        pelis = json.loads(pelis.content)

        if 'MovieList' in pelis:
            pelis = pelis["MovieList"]
        else:
            pelis = ''    


        pagsig = pagi + 1

        genero = genero.replace('-',' ')

        self.response.write(
            template.render('view/genero.html',
                            {'pelis': pelis, 'pagsig': pagsig, 'genero': genero, 'conf':conf}))

application = webapp2.WSGIApplication([('/genero/peliculas/(?P<genero>\w+)',
                                        GeneroPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()