# encoding: UTF-8
__author__ = 'bakabie'
import requests
import flask,re
global ex

app = flask.Flask(__name__)
ex = requests.session()
cookies = {
	"ipb_pass_hash":"006bbeab8da391965efa9b72157a7ca7",
	"ipb_member_id":"2257599",
	"igneous":"010f4032c4a6db2ee8b8488ee9766b611c262d96b293fd1"
}
headers = {
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",
	"cookie":"ipb_member_id=2257599; ipb_pass_hash=006bbeab8da391965efa9b72157a7ca7; igneous=cf7951cc3f66fd9f8536aba36aaee30d917c91805189ceed2b94523524deff1c8a7b50800ccc2f2bd010f4032c4a6db2ee8b8488ee9766b611c262d96b293fd1; uconfig=tl_m-uh_y-rc_0-cats_0-xns_0-ts_m-tr_2-prn_y-dm_l-ar_0-rx_0-ry_0-ms_n-mt_n-cs_a-to_a-pn_0-sc_0-sa_y-oi_n-qb_n-tf_n-hp_-hk_-xl_; lv=1438142149-1438230004",
	"hosts":"exhentai.org"
}
def url(reg,web):#正则表达式运用部分
	'''reg = "<a href=.http://exhentai.org/g/.+? onmouseover=.+? onmouseout=.+?>.+?</a></div>"'''
	print reg
	reg_href = re.compile(reg)
	allpost = reg_href.findall(web,re.S)
	my_web = ""
	for i in range(len(allpost)):
		my_web = my_web+allpost[i]+'\r\n'
		print allpost[i].encode('utf-8')
	return my_web
@app.route('/')
def index():#首页部分
	web = ex.get("http://exhentai.org",headers=headers).text
	web = url("<a href=.http://exhentai.org/g/.+? onmouseover=.+? onmouseout=.+?>.+?</a></div>",web)
	web = web.replace("exhentai.org",'127.0.0.1')#127.0.0.1替换成自己的域名
	return web.encode('utf-8')

@app.route('/Search/')
def Search():#搜索页面部分
	web = ex.get("http://exhentai.org/?f_search="+flask.request.args.get('key','')).text
	return url("<a href=.http://exhentai.org/g/.+? onmouseover=.+? onmouseout=.+?>.+?</a></div>",web).encode("utf-8")
@app.route('/g/<iid>/<hassh>/')
def g(iid,hassh):#缩略图页面部分
	web = ex.get("http://exhentai.org/g/"+iid+"/"+hassh+"/",headers=headers).text
	return url("<a href=.http://exhentai.org/s/.+?>",web).encode('utf-8')

if __name__ == '__main__':
	app.run(port=80)
