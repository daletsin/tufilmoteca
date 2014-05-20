import webapp2
import urllib
import re
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template



class DownloadPage(webapp2.RequestHandler):
    def get(self):
        error = 'NO SE RECIBIO NINGUN DATO'
        self.response.write(
            template.render('view/error.html', {'error': error}))

    def post(self):                
        linksub = self.request.get('numid')     
        url = self.request.get('url')   
        urlv = url
        self.response.write(
            template.render('view/descargacuevana.html', {'linkvideo': urlv, 'linksub': linksub}))


application = webapp2.WSGIApplication([('/descargacuevana', DownloadPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
