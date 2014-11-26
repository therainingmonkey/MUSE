from plugnplay import Interface

class Module(Interface):
	'''
		Base class for MUSE modules. Put trigger strings in the triggers
		list and your functionality in the action() method.
	'''
	triggers = []
	
	def action(self, arg_phrase):
		pass
	
	def check_triggers(self, instruction, arg_phrase):
		pass
