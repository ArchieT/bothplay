# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from dejavu import Dejavu
from dejavu.recognize import MicrophoneRacognizer
import urllib2
import tempfile
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
q = raw_input('Daj do wyszukiwania:')
import soundcloud
scclient = soundcloud.Client(client_id='7b48f9baee211d4cc93fb489b0834f50')
search = scclient.get('/tracks',q=q,limit=3)
for track in search:
	print "Trying: ",track.title #," — ",track.artist
	print track.stream_url
	track = urllib2.urlopen(scclient.get(track.stream_url,allow_redirects=False).location)
	temp = tempfile.NamedTemporaryFile()
	tf = temp.file
	tf.write(track.read())
	tf.close()
	tp = temp.name
	djv.fingerprint_file(tp,song_name=track.stream_url)
	song = djv.recognize(MicrophoneRecognizer,seconds=10)
