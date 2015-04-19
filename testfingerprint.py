# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from dejavu import Dejavu
import urllib2
djv = Dejavu({
	"database": {
		"host": "127.0.0.1",
		"user": "root",
		"passwd": "qwertyuiop",
		"db": "dejavu"
	}
})
def dajcyfry(text):
	def czycyfra(char):
		#print char
		assert type(char)=='str' or type(char)==str or len(char)==1
		try: intchar=int(char) ; print intchar
		except ValueError: return False
		return intchar in range(0,10)
	bylynum = False ; lista = []
	for char in list(text):
		if czycyfra(char): lista.append(char) ; bylynum = True
	assert bylynum ; return ''.join(lista)
q = raw_input('Daj do wyszukiwania:')
import soundcloud
scclient = soundcloud.Client(client_id='7b48f9baee211d4cc93fb489b0834f50')
search = scclient.get('/tracks',q=q,limit=3)
for track in search:
	print "Trying: ",track.title #," — ",track.artist
	urlstr = str(track.stream_url)
	print urlstr
	urlnum = dajcyfry(urlstr)
	track = urllib2.urlopen(scclient.get(track.stream_url,allow_redirects=False).location)
	#temp = tempfile.NamedTemporaryFile()
	#tf = temp.file
	#tf.write(track.read())
	#tf.close()
	#tp = temp.name
	tf = open('/tmp/temp.music','w')
	tf.write(track.read())
	tf.close()
	djv.fingerprint_file('/tmp/temp.music',song_name=urlnum)
#song = djv.recognize(MicrophoneRecognizer,seconds=10)
