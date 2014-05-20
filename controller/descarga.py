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
        referer = self.request.referer
        exp = "http://.*\.cuevana\.tv"
        numid = self.request.get('numid')
        tipo = self.request.get('tipo')
        linksub = ''            
        cdef = self.request.get('def')
        if re.match(exp, referer):        
            if tipo == 'series':
                linksub = 'http://sc.cuevana.tv/files/s/sub/'+numid+'_ES.srt'
            if tipo == 'peliculas':
                linksub = 'http://sc.cuevana.tv/files/sub/'+numid+'_ES.srt'
            if tipo == 'series' and cdef != '360':
                linksub = 'http://sc.cuevana.tv/files/s/sub/'+numid+'_ES_'+cdef+'.srt'
            if tipo == 'peliculas' and cdef != '360':
                linksub = 'http://sc.cuevana.tv/files/sub/'+numid+'_ES_'+cdef+'.srt'
        else:
            linksub = 'http://player.zate.tv'+numid+'.srt'

        url = self.request.get('url')

        titulo1 = self.request.get('titulo1')
        titulo2 = self.request.get('titulo2')
        numimg = self.request.get('numimg')
        sinopsis = self.request.get('sinopsis')
        director = self.request.get('director')
        guion = self.request.get('guion')
        produccion = self.request.get('produccion')
        episodio = self.request.get('episodio')
        temporada = self.request.get('temporada')
        genero = self.request.get('genero')
        idioma = self.request.get('idioma')
        duracion = self.request.get('duracion')
        reparto = self.request.get('reparto')

        titulos_tipo = self.request.get('tipo')
        titulos_id = self.request.get('numid')
        servidor = self.request.get('servidor')

        titulo = Titulos.all()
        ti = titulo.filter('numid =', numid).filter('tipo =', tipo).count(1)
        opcion = Opciones.all()
        op = opcion.filter('titulos_id =', titulos_id).filter('titulos_tipo =', titulos_tipo).filter('cdef =', cdef).filter('servidor =', servidor).count(1)
        seri = Series.all()
        ser = seri.filter('titulo =', titulo2).count(1)

        if titulo1 != '' and titulo2 != '' and numid != '' and numimg != '' and genero != '' and idioma != '' and url != '' and tipo != '' and cdef != '' and servidor != '' and re.match(exp, referer):
            if ti == 0:
                t = Titulos()
                t.titulo1 = titulo1
                t.titulo2 = titulo2
                t.numid = numid
                t.numimg = numimg
                t.sinopsis = sinopsis
                t.director = director
                t.guion = guion
                t.produccion = produccion
                t.episodio = episodio
                t.temporada = temporada
                t.genero = genero
                t.idioma = idioma
                t.duracion = duracion
                t.reparto = reparto
                t.tipo = tipo
                t.put()
            else:
                ti2 = titulo.filter('numid =', numid).filter('tipo =', tipo)[0]
                ti2.titulo1 = titulo1
                ti2.titulo2 = titulo2
                ti2.numid = numid
                ti2.numimg = numimg
                ti2.sinopsis = sinopsis
                ti2.director = director
                ti2.guion = guion
                ti2.produccion = produccion
                ti2.episodio = episodio
                ti2.temporada = temporada
                ti2.genero = genero
                ti2.idioma = idioma
                ti2.duracion = duracion
                ti2.reparto = reparto
                ti2.tipo = tipo
                ti2.put()
            if tipo == 'series':
                if ser == 0:
                    s = Series()
                    s.titulo = titulo2
                    s.numimg = numimg
                    s.put()
            if op == 0:
                o = Opciones()
                o.titulos_id = titulos_id
                o.titulos_tipo = titulos_tipo
                o.cdef = cdef
                o.servidor = servidor
                o.url = url
                o.put()
            else:
                op2 = opcion.filter('titulos_id =', titulos_id).filter('titulos_tipo =', titulos_tipo).filter('cdef =', cdef).filter('servidor =', servidor)[0]
                op2.titulos_id = titulos_id
                op2.titulos_tipo = titulos_tipo
                op2.cdef = cdef
                op2.servidor = servidor
                op2.url = url
                op2.put()

        urlv = url
        #ursrt = linksub
        self.response.write(
            template.render('view/descarga.html', {'linkvideo': urlv, 'linksub': linksub}))


application = webapp2.WSGIApplication([('/descarga', DownloadPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
