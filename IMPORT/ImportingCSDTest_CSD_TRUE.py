from music21 import *
from copy import *

''' IMPORT TEST CSD TRUE'''

'''EXPECTED: First chord is alingned into the first measure'''
'''ACTUAL: First chord is misaligned to the left of clef and all subsequent chords are misaligned.
    There is no viable use case for this outcome. Should behave like writeAsChord appears to. '''

src = converter.parse('Test Import.xml')
s  = src.parts[0]

harmony.realizeChordSymbolDurations(s)

m = s.recurse().getElementsByClass("ChordSymbol")
for x in m:
    print(x.duration)

s.show("musicxml.png")
s.show('text')
