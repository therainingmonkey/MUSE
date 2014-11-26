#! /usr/bin/env python

import os, imp, sys
import nltk
import plugnplay
from interfaces import Module

debug = 2

instruction_tags = ["VB", "VBG", "VBP", "VBN"]

def load_modules():
	plugnplay.plugin_dirs = ["./modules"]
	plugnplay.load_plugins()

def tag(intext):
	'''takes a string, returns it in tokenised & POS tagged.'''
	intext = "now, " + intext # Dirty hack to recognise when the first word is a verb
	tagged_sentance = (nltk.pos_tag(nltk.word_tokenize(intext))) #Splits sentence into word/tag tuples
	if debug >= 3: print "parse:", tagged_sentance
	return tagged_sentance

def find_instruction(tagged_sentance):
	'''identifies which part of a phrase is the instruction. '''
	instruction = False
	for i in xrange(0,len(tagged_sentance)):
		if tagged_sentance[i][1] in instruction_tags:
			instruction = tagged_sentance[i][0]
			arg_phrase = tagged_sentance[(i+1):] # rest of the sentance
			if debug >= 2: print "verb found:", instruction
			break
	if not instruction:
	# If no verb found, use first word
		instruction = tagged_sentance[2][0]
		arg_phrase = tagged_sentance[3:]
		if debug >= 1: print "No verb found, best guess is", instruction, "arg:", arg_phrase
	return (instruction, arg_phrase)

def perform_instruction(instruction_tuple):
	'''all modules check whether they're triggered by the instruction.
	EVERY module with the triggger acts, in random order.'''
	instruction = instruction_tuple[0]
	arg_phrase = instruction_tuple[1]
	if debug >= 2: print "checcking modules for trigger:", instruction
	Module.check_triggers(instruction, arg_phrase)
		

def main():
	load_modules()
	
	def listen(intext):
		perform_instruction(find_instruction(tag(intext)))
	
	if len(sys.argv) > 1:
		intext = ""
		for arg in sys.argv[1:]:
			intext += arg
			intext += " "
	else:
		intext = raw_input("How may I serve?: ")
	listen(intext)

if __name__ == '__main__':
	main()
