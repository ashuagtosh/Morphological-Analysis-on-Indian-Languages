# Morphological-Analysis-on-Indian-Languages

For Part of Speech Tagger (POS Tagger), we have created lists of Nouns, Verbs, Adjectives and Adverbs. 

For Example: ਮੰਡਾ (Boy) in Punjabi is a Noun and we will select this word and would search in our lists. If the word is found in our Noun List we will classify it as Noun.

Indian languages have rich inflectional morphology and approximately there are 30+ forms of a single word in Punjabi.
For Example: ਮੰਡਾ can be used in various contexts(i.e. ਮੰਡੇ (Boys), ਮੰਡੇਆਂ etc. ). 

For this pupose we did stemming on these words and after that we checked the presence of reduced word in our database. If it is present in our database we will label it correspondingly as Noun or Verb or Adjective or Adverb.

One Major difficulty found while implementing it programatically on Python 2.7 is: Unlike English corresponds to ASCII, Punjabi belongs to Unicode Format (UTF-8). So, special attention is given to this.

Named Entity Recognition (NER): It incorporate classification of entities in various classes. For example: Name of Person, Location Names, Organizations etc. In English, we are provided with large datasets to classify these objects but In Punjabi we are way behind due to lack of Labeled data.
