# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from dejavu import Dejavu
from dejavu.recognize import MicrophoneRecognizer
import urllib2
import tempfile
#from os.path import abspath
#import multiprocessing
djv = Dejavu({
	"database": {
		"host": "127.0.0.1",
		"user": "root",
		"passwd": "qwertyuiop",
		"db": "dejavu"
	}
})
#nprocesses=None
#try: nprocesses = nprocesses or multiprocessing.cpu_count()
#except NotImplementedError: nprocesses=1
#else: nprocesses=1 if nprocesses<=0 else nprocesses
#pool = multiprocessing.Pool(nprocesses)
def czycyfra(char):
	#print char
	assert type(char)=='str' or type(char)==str or len(char)==1
	try: intchar=int(char) ; print intchar
	except ValueError: return False
	return intchar in range(0,10)
q = raw_input('Daj do wyszukiwania:')
import soundcloud
scclient = soundcloud.Client(client_id='7b48f9baee211d4cc93fb489b0834f50')
search = scclient.get('/tracks',q=q,limit=3)
for track in search:
	print "Trying: ",track.title #," — ",track.artist
	urlstr = str(track.stream_url)
	print urlstr
	urlnuml = []
	bylynum = False
	for char in list(urlstr):
		if czycyfra(char): 
			urlnuml.append(char)
			bylynum = True
	if not bylynum: raise ValueError('nie bylo num w url')
	if bylynum: urlnum = str(''.join(urlnuml))
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
