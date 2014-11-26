from interfaces import Module
from defaultmodule import defaultModule

import plugnplay

import subprocess

class Google(defaultModule):
	implements = [Module]
	
	triggers = ["Google", "google", "Search", "search", " google"]
	
	def action(self, arg_phrase):
		print "arg_phrase:", arg_phrase
		url = "http://www.google.com/search?q="
		for tagged_word in arg_phrase:
			url += tagged_word[0]
			url += "+"
		subprocess.call(["xdg-open", url])
