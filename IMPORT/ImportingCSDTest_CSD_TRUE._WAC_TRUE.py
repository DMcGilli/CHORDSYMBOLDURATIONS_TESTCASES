from music21 import *
from copy import *

''' IMPORT TEST CSD TRUE'''

'''EXPECTED: First chord is in the first measure'''
'''ACTUAL: This works, and chrds are positioned in the measure and have original duration'''

src = converter.parse('Test Import.xml')

s  = src.parts[0]

harmony.realizeChordSymbolDurations(s)

m = s.recurse().getElementsByClass("ChordSymbol")
for x in m:
    x.writeAsChord = True
    print(x.duration)

s.show("musicxml.png")
s.show('text')
