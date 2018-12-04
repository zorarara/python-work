import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,x,y):
        x = int(x)
        y = int(y) if y is not None else x

        html='''
        <html>
          <body>
            <table>
        '''
        for i in range(1,x+1):
            html += '<TR>'
            for j in range(1,y+1):
                html += '<TD>%d</TD>' % (str(i)+'*'+str(j)+'='+str(i*j))
            html +='</TR>' 

        html+='''
           </table>
          </body>
        </html>
        '''
    self.write(html)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
