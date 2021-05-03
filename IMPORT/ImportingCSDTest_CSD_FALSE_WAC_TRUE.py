from music21 import *
from copy import *

''' IMPORT TEST CSD FALSE'''
'''EXPECTED: First chord is in the first measure'''
'''ACTUAL: Chords are visually aligned, default duration of quarter note is used'''

src = converter.parse('Test Import.xml')

s  = src.parts[0]

m = s.recurse().getElementsByClass("ChordSymbol")
for x in m:
    x.writeAsChord = True
    print(x.duration)

s.show("musicxml.png")
s.show('text')
