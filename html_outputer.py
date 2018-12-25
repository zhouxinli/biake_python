# -*-coding:utf-8 -*-
import codecs
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        fout=codecs.open('output.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            print(data)
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")


        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        #print(self.datas)
        fout.close()