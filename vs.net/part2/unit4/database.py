class Simpledb():
	def __init__(self, filename):
		self.filename = filename

	def __repr__(self):
		return f'<Simpledb file=\'{self.filename}\'>'

	def insert(self, key, value):
		key_found = False
		f = open(self.filename, 'r+')
		for (row) in f:
			(k, v) = row.split('\t', 1)
			if k == key:
				key_found = True
				break
			else:
				pass
		if key_found==False:
			f.write(key + '\t' + value + '\n')
			f.close()
			return 'inserted'
		else:
			return 'not inserted'


	def select_one(self, key):
		try:
			f = open(self.filename, 'r')
		except:
			return 'This file does not exist'
		for row in f:
			(k, v) = row.split('\t', 1)
			if k == key:
				return v
		else:
			return 'This key could not be found'

		f.close()


	def delete(self, key):
		try:
			f = open(self.filename, 'r')
		except:
			return 'This file does not exist'

		result = open('result.txt', 'w')
		for (row) in f:
			(k, v) = row.split('\t', 1)
			if k != key:
				result.write(row)
		f.close()
		result.close()
		import os
		os.replace('result.txt', self.filename)
		return 'deleted'

	def update(self, key, value):
		try:
			f = open(self.filename, 'r')
		except:
			return 'This file does not exist'
		result = open('result.txt', 'w')
		key_found = False
		for (row) in f:
			(k, v) = row.split('\t', 1)
			if k == key:
				key_found = True
				result.write(key + '\t' + value + '\n')
			else:
				result.write(row)
		f.close()
		result.close()
		import os
		os.replace('result.txt', self.filename)
		if key_found==True:
			return 'updated'
		else:
			return 'key not found'