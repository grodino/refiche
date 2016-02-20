"""
	Little tool maid to replace all urls in static
	files by the url given in the settings folder
"""

import re

from refiche import settings
from path import path

def find_static_files(dirs):
	"""
	Find all the js files in the static directory
	"""
	files = []

	for dir in dirs:
		files += [f for f in path(dir).walkfiles('*.js')]

	return files


def replace_urls(files, regex, url):
	"""
	Replace all the urls (always in dev mode) by the one given
	"""

	if url == regex:
		raise ValueError('Url to replace cannot be the same as the url replacing it')


	for file in files:
		with open(file) as f:
			content = f.read()

			while regex in content:
				content = content.replace(regex, url)
				print(file, regex, sep=' : ')

		temp_file = open(file, 'w')
		temp_file.write(content)
		temp_file.close()




if __name__== '__main__':
	static_dirs = settings.STATICFILES_DIRS

	files = find_static_files(static_dirs)
	replace_urls(files, '[REFICHE_URL]', 'refiche.dev:8000')