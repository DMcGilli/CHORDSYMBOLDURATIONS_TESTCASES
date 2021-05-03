from music21 import *

theStreamMeta = metadata.Metadata()

def DoStreamLabel(theStream):
    """ This labels the tests for reference on visual output"""
    theStreamMeta.title = theTestTitle
    theStream.insert(0,theStreamMeta)

theChordList = ["A7", "D7","G7", "CM9", "Bmin7","E7#9"]
SymbolList = list(map(harmony.ChordSymbol, theChordList))
myStream = stream.Stream()

theTestTitle = "writeAsChord:FALSE \n CSDuration:TRUE \n 1 REST"

for x in SymbolList:
    myMeasure = stream.Measure()
    x.duration = duration.Duration("half")
    myMeasure.append(x)
    myMeasure.append(note.Rest(duration=duration.Duration('half')))
    harmony.realizeChordSymbolDurations(myStream)  # toggle as needed for behaviors
    myStream.append(myMeasure)
DoStreamLabel(myStream)
myStream.show('musicxml.png')






