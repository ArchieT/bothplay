from dejavu import Dejavu as djlv
from dejavu.recognize import MicrophoneRecognizer
djv = djlv({
	"database": {
		"host": "127.0.0.1",
		"user": "root",
		"passwd": "qwertyuiop",
		"db": "dejavu"
	}
})
song = djv.recognize(MicrophoneRecognizer,seconds=10)
print song