from music21 import *

theStreamMeta = metadata.Metadata()
myStream = stream.Stream()

def DoStreamLabel(theStream):
    """ This labels the tests for reference on visual output"""
    theStreamMeta.title = theTestTitle
    theStream.insert(0,theStreamMeta)

theChordList = ["A7", "D7","G7", "CM9", "Bmin7","E7#9"]
SymbolList = list(map(harmony.ChordSymbol, theChordList))

theTestTitle = "writeAsChord:FALSE \n CSDuration:TRUE \n No Rests"

for x in SymbolList:
    myMeasure = stream.Measure()
    x.duration = duration.Duration("half")
    myMeasure.append(x)
    harmony.realizeChordSymbolDurations(myStream)  # toggle as needed for behaviors
    myStream.append(myMeasure)
DoStreamLabel(myStream)
myStream.show('musicxml.png')






