# Radix sort 
# Joe Johnston <jjohn@taskboy.com>

class RadixSort:

	def __init__(self,radix=10, keysize=10):
		self.radix = radix
		self.keysize = keysize
		
	def init_bases(self):
		bases = []
		idx = 0
		while (idx < self.radix):
			bases.append([])
			idx = idx + 1
				
		self.bases = bases

	def sort_list(self, list):
		if (list == None):
			return
			
		pos = self.keysize - 1
		while (pos >= 0):
			self.partition_by_position(list, pos)
			list = self.merge_bases()
			pos = pos - 1
		return list
				
	def partition_by_position(self, list, pos):
		self.init_bases()
		for el in list:
			idx = 0
			s = str(el)
			if (len(s) > pos):
				idx = s[pos:(pos + 1)]
			self.bases[ int(idx) ].append(el)
							 
	def merge_bases(self):
		list = []
		idx = 0
		while (idx < self.radix):
			for el in self.bases[ idx ]:
				list.append(el)
			idx = idx + 1
		return list