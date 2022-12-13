from clearsight_3 import utils
from clearsight_3.patternmatching import pattern

from nltk import pos_tag
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import wordnet
from nltk.corpus import opinion_lexicon
from math import sqrt

def singleTargetIdentify(l, t):
    out = []
    current = []
    for i in l:
        if i[1] == t:
            current.append(i)
        else:
            out.append(current)
            current = []
    return [i for i in out if len(i) > 0]

def multipleTargetIdentify(l, ts):
    out = []
    current = []
    for i in l:
        if i[1] in ts:
            current.append(i)
        else:
            out.append(current)
            current = []
    return [i for i in out if len(i) > 0]

def number(l):
    return [(l[x], x) for x in range(len(l))]

tagset = [
    "$", # dollar
         # $ -$ --$ A$ C$ HK$ M$ NZ$ S$ U.S.$ US$
    "\'\'", # closing quotation mark
            # ' ''
    "(", # opening parenthesis
         # ( [ {
    ")", # closing parenthesis
         # ) ] }
    ",", # comma
         # ,
    "--", # dash
          # --
    ".", # sentence terminator
         # . ! ?
    ", #", # colon or ellipsis
           # , # ; ...
    "CC", # conjunction, coordinating
          # & 'n and both but either et for less minus neither nor or plus so
          # therefore times v. versus vs. whether yet
    "CD", # numeral, cardinal
          # mid-1890 nine-thirty forty-two one-tenth ten million 0.5 one forty-
          # seven 1987 twenty '79 zero two 78-degrees eighty-four IX '60s .025
          # fifteen 271,124 dozen quintillion DM2,000 ...
    "DT", # determiner
          # all an another any both del each either every half la many much nary
          # neither no some such that the them these this those
    "EX", # existential there
          # there
    "FW", # foreign word
          # gemeinschaft hund ich jeux habeas Haementeria Herr K'ang-si vous
          # lutihaw alai je jour objets salutaris fille quibusdam pas trop Monte
          # terram fiche oui corporis ...
    "IN", # preposition or conjunction, subordinating
          # astride among uppon whether out inside pro despite on by throughout
          # below within for towards near behind atop around if like until below
          # next into if beside ...
    "JJ", # adjective or numeral, ordinal
          # third ill-mannered pre-war regrettable oiled calamitous first separable
          # ectoplasmic battery-powered participatory fourth still-to-be-named
          # multilingual multi-disciplinary ...
    "JJR", # adjective, comparative
           # bleaker braver breezier briefer brighter brisker broader bumper busier
           # calmer cheaper choosier cleaner clearer closer colder commoner costlier
           # cozier creamier crunchier cuter ...
    "JJS", # adjective, superlative
           # calmest cheapest choicest classiest cleanest clearest closest commonest
           # corniest costliest crassest creepiest crudest cutest darkest deadliest
           # dearest deepest densest dinkiest ...
    "LS", # list item marker
          # A A. B B. C C. D E F First G H I J K One SP-44001 SP-44002 SP-44005
          # SP-44007 Second Third Three Two * a b c d first five four one six three
          # two
    "MD", # modal auxiliary
          # can cannot could couldn't dare may might must need ought shall should
          # shouldn't will would
    "NN", # noun, common, singular or mass
          # common-carrier cabbage knuckle-duster Casino afghan shed thermostat
          # investment slide humour falloff slick wind hyena override subhumanity
          # machinist ...
    "NNP", # noun, proper, singular
           # Motown Venneboerger Czestochwa Ranzer Conchita Trumplane Christos
           # Oceanside Escobar Kreisler Sawyer Cougar Yvette Ervin ODI Darryl CTCA
           # Shannon A.K.C. Meltex Liverpool ...
    "NNPS", # noun, proper, plural
            # Americans Americas Amharas Amityvilles Amusements Anarcho-Syndicalists
            # Andalusians Andes Andruses Angels Animals Anthony Antilles Antiques
            # Apache Apaches Apocrypha ...
    "NNS", # noun, common, plural
           # undergraduates scotches bric-a-brac products bodyguards facets coasts
           # divestitures storehouses designs clubs fragrances averages
           # subjectivists apprehensions muses factory-jobs ...
    "PDT", # pre-determiner
           # all both half many quite such sure this
    "POS", # genitive marker
           # ' 's
    "PRP", # pronoun, personal
           # hers herself him himself hisself it itself me myself one oneself ours
           # ourselves ownself self she thee theirs them themselves they thou thy us
    "PRP$", # pronoun, possessive
            # her his mine my our ours their thy your
    "RB", # adverb
          # occasionally unabatingly maddeningly adventurously professedly
          # stirringly prominently technologically magisterially predominately
          # swiftly fiscally pitilessly ...
    "RBR", # adverb, comparative
           # further gloomier grander graver greater grimmer harder harsher
           # healthier heavier higher however larger later leaner lengthier less-
           # perfectly lesser lonelier longer louder lower more ...
    "RBS", # adverb, superlative
           # best biggest bluntest earliest farthest first furthest hardest
           # heartiest highest largest least less most nearest second tightest worst
    "RP", # particle
          # aboard about across along apart around aside at away back before behind
          # by crop down ever fast for forth from go high i.e. in into just later
          # low more off on open out over per pie raising start teeth that through
          # under unto up up-pp upon whole with you
    "SYM", # symbol
           # % & ' '' ''. ) ). * + ,. < = > @ A[fj] U.S U.S.S.R * ** ***
    "TO", # "to" as preposition or infinitive marker
          # to
    "UH", # interjection
          # Goodbye Goody Gosh Wow Jeepers Jee-sus Hubba Hey Kee-reist Oops amen
          # huh howdy uh dammit whammo shucks heck anyways whodunnit honey golly
          # man baby diddle hush sonuvabitch ...
    "VB", # verb, base form
          # ask assemble assess assign assume atone attention avoid bake balkanize
          # bank begin behold believe bend benefit bevel beware bless boil bomb
          # boost brace break bring broil brush build ...
    "VBD", # verb, past tense
           # dipped pleaded swiped regummed soaked tidied convened halted registered
           # cushioned exacted snubbed strode aimed adopted belied figgered
           # speculated wore appreciated contemplated ...
    "VBG", # verb, present participle or gerund
           # telegraphing stirring focusing angering judging stalling lactating
           # hankerin' alleging veering capping approaching traveling besieging
           # encrypting interrupting erasing wincing ...
    "VBN", # verb, past participle
           # multihulled dilapidated aerosolized chaired languished panelized used
           # experimented flourished imitated reunifed factored condensed sheared
           # unsettled primed dubbed desired ...
    "VBP", # verb, present tense, not 3rd person singular
           # predominate wrap resort sue twist spill cure lengthen brush terminate
           # appear tend stray glisten obtain comprise detest tease attract
           # emphasize mold postpone sever return wag ...
    "VBZ", # verb, present tense, 3rd person singular
           # bases reconstructs marks mixes displeases seals carps weaves snatches
           # slumps stretches authorizes smolders pictures emerges stockpiles
           # seduces fizzes uses bolsters slaps speaks pleads ...
    "WDT", # WH-determiner
           # that what whatever which whichever
    "WP", # WH-pronoun
          # that what whatever whatsoever which who whom whosoever
    "WP$", # WH-pronoun, possessive
           # whose
    "WRB", # Wh-adverb
           # how however whence whenever where whereby whereever wherein whereof why
    "``" # opening quotation mark
]

nounTags = [
    "NN", # noun, common, singular or mass
    "NNP", # noun, proper, singular
    "NNPS", # noun, proper, plural
    "NNS" # noun, common, plural
]

commonNounTags = [
    "NN", # noun, common, singular or mass
    "NNS" # noun, common, plural
]

properNounTags = [
    "NNP", # noun, proper, singular
    "NNPS" # noun, proper, plural
]

verbTags = [
    "VB", # verb, base form
    "VBD", # verb, past tense
    "VBG", # verb, present participle or gerund
    "VBN", # verb, past participle
    "VBP", # verb, present tense, not 3rd person singular.
    "VBZ", # verb, present tense, 3rd person singular
    "RB", # adverb
    "RBR", # adverb, comparative
    "RBS" # adverb, superlative
]

adjectiveTags = [
    "JJ", # adjective or numeral, ordinal
    "JJR", # adjective, comparative
    "JJS" # adjective, superlative
]

objectTags = [
    "NN", # noun, common, singular or mass
    "NNP", # noun, proper, singular
    "NNPS", # noun, proper, plural
    "NNS", # noun, common, plural
    "JJ", # adjective or numeral, ordinal
    "JJR", # adjective, comparative
    "JJS" # adjective, superlative
]

properObjectTags = [
    "NNP", # noun, proper, singular
    "NNPS", # noun, proper, plural
    "JJ", # adjective or numeral, ordinal
    "JJR", # adjective, comparative
    "JJS" # adjective, superlative
]

actionTags = [
    "VB", # verb, base form
    "VBD", # verb, past tense
    "VBG", # verb, present participle or gerund
    "VBN", # verb, past participle
    "VBP", # verb, present tense, not 3rd person singular.
    "VBZ", # verb, present tense, 3rd person singular
    "RB", # adverb
    "RBR", # adverb, comparative
    "RBS", # adverb, superlative
    "JJ", # adjective or numeral, ordinal
    "JJR", # adjective, comparative
    "JJS" # adjective, superlative
]

stopwordTags = [
    "LS", # list item marker
]

def tag(string):
    return pos_tag(word_tokenize(string))

# Still gets confused about "Hello". Fix that?
class Tokenization:
    def __init__(self, string):
        self.string = string
        self.sent = sent_tokenize(string)
        self.word = word_tokenize(string)
        self.pos = pos_tag(self.word)

        self.nouns = multipleTargetIdentify(self.pos, nounTags)
        self.objects = multipleTargetIdentify(self.pos, objectTags)
        self.properObjects = multipleTargetIdentify(self.pos, properObjectTags)

        self.verbs = multipleTargetIdentify(self.pos, verbTags)
        self.actions = multipleTargetIdentify(self.pos, actionTags)

        self.adjectives = multipleTargetIdentify(self.pos, adjectiveTags)

        self.negative = [x for x in self.word if x in opinion_lexicon.negative()]
        self.positive = [x for x in self.word if x in opinion_lexicon.positive()]

        for item in self.pos:
            s = item[0]
            pos = item[1]

    def __str__(self):
        return "[clearsight_3.tokenization] Tokenization: " + \
            "\n  String: \"" + self.string + "\"" + \
            "\n  Determined components:" + \
            "\n    Determined nouns: " + str(self.nouns) + \
            "\n    Determined objects: " + str(self.objects) + \
            "\n    Determined proper objects: " + str(self.properObjects) + \
            "\n    Determined verbs: " + str(self.verbs) + \
            "\n    Determined actions: " + str(self.actions) + \
            "\n    Determined adjectives: " + str(self.adjectives) + \
            "\n  Part-of-speech tagging: " + str(self.pos) + \
            "\n  Sentence tokenization: " + str(self.sent) + \
            "\n  Word tokenization: " + str(self.word)

    def convert(self):
        return pattern.Pattern(
            pattern.PatternComponent(self.string),
            pattern.PatternComponent(*self.nouns),
            pattern.PatternComponent(*self.objects),
            pattern.PatternComponent(*self.properObjects),
            pattern.PatternComponent(*self.verbs),
            pattern.PatternComponent(*self.actions),
            pattern.PatternComponent(*self.adjectives),
            pattern.PatternComponent(*self.pos),
            pattern.PatternComponent(*self.sent),
            pattern.PatternComponent(*self.word)
        )

def tokenize(string):
    return Tokenization(string)

class Object:
    def __init__(self, postagList):
        self.postagList = postagList

        self.nouns = multipleTargetIdentify(postagList, commonNounTags)
        self.properNouns = multipleTargetIdentify(postagList, properNounTags)
        self.adjectives = multipleTargetIdentify(postagList, adjectiveTags)

class Action:
    def __init__(self, postagList):
        self.postagList = postagList

        self.verbs = multipleTargetIdentify(postagList, verbTags)
        self.adjectives = multipleTargetIdentify(postagList, adjectiveTags)
