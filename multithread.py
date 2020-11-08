from threading import Thread

def New_Thread(compressor_funk, path):
	t1 = Thread(target=compressor_funk, args=(path))
	t2 = Thread(target=compressor_funk, args=(path))

	t1.start()
	t2.start()
	t1.join()
	t2.join()