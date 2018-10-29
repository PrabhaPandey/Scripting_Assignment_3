if "diff" in str:
		match_with=content[1]
		if isfile(content[1]) and isfile(content[2]):
			added=[]
			change=[]
			delete=[]
			nochange=[]
			with open(content[1], 'r') as f:
				with open(content[2],'r') as o:
					c=0
					# t=0
					while(1):
						# is_added=0
						is_change=0
						line_from_2=o.readline()
						if line_from_2=='':
							break
						c=c+1
						t=0
						f.seek(0,0)
						while(1):
							line_from_1=f.readline()
							t=t+1
							if line_from_1 =='':
								break
							if line_from_1==line_from_2:
								is_change=1
								if c==t:
									nochange.append(line_from_1)
									break
								if c!=t:
									change.append('< '+line_from_1)
									break
						if is_change==0:
							added.append('> '+line_from_2)
			with open(content[1], 'r') as f:
				while (1):
					line_from_1=f.readline()
					if line_from_1=='':
							break
					if '< '+line_from_1 in change or line_from_1 in nochange:
						continue
					delete.append('< '+line_from_1)
			print'----------------'
			print '\033[91m {}{}\033[00m'.format('Added in ',content[1])
			print'----------------'

			for i in added:
				print i.strip()
			print'----------------'
			print '\033[91m {}{}\033[00m'.format('Change line location in ',content[1])
			
			print'----------------'

			for i in change:
				print i.strip()
			print'----------------'
			print '\033[91m {}{}\033[00m'.format('Delete from ',content[1])
			
			print'----------------'
			for i in delete:
				print i.strip()

		else:
			print "Invalid File"