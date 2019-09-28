import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
# from KaggleWord2VecUtility import KaggleWord2VecUtility
import nltk
import re
# import BeautifulSoup
#kaggle



class KaggleWord2VecUtility(object):
    # """KaggleWord2VecUtility is a utility class for processing raw HTML text into segments for further learning"""

    @staticmethod
    def review_to_wordlist( review, remove_stopwords=False ):
        # Function to convert a document to a sequence of words,
        # optionally removing stop words.  Returns a list of words.
        #
        # 1. Remove HTML
        # review_text = BeautifulSoup(review).get_text()
        #
        # 2. Remove non-letters
        review_text = re.sub("[^a-zA-Z]"," ", review)
        #
        # 3. Convert words to lower case and split them
        words = review_text.lower().split()
        #
        # 4. Optionally remove stop words (false by default)
        if remove_stopwords:
            stops = set(stopwords.words("english"))
            words = [w for w in words if not w in stops]
        #
        # 5. Return a list of words
        return(words)

    # Define a function to split a review into parsed sentences
    @staticmethod
    def review_to_sentences( review, tokenizer, remove_stopwords=False ):
        # Function to split a review into parsed sentences. Returns a
        # list of sentences, where each sentence is a list of words
        #
        # 1. Use the NLTK tokenizer to split the paragraph into sentences
        raw_sentences = tokenizer.tokenize(review.decode('utf8').strip())
        #
        # 2. Loop over each sentence
        sentences = []
        for raw_sentence in raw_sentences:
            # If a sentence is empty, skip it
            if len(raw_sentence) > 0:
                # Otherwise, call review_to_wordlist to get a list of words
                sentences.append( KaggleWord2VecUtility.review_to_wordlist( raw_sentence, \
                  remove_stopwords ))
        #
        # Return the list of sentences (each sentence is a list of words,
        # so this returns a list of lists
        return sentences

# if __name__ == '__main__':
train = {"reviews": [
    "The twins effect is a vampire martial arts movie available in Cantonese with English subtitles. It is a Jackie Chan production and he does make a special guest appearance, although it is not for those that liked Shanghai Noon/Knights and the other recent Hollywood flicks he has become known for, this film is a lot more special than that.<br /><br />It was originally called The Vampire Effect but as a very popular Chinese female pop duo called The Twins (Charlene Choi and Gillian Chung) took the two leading roles the title was changed to cash in on their fame.<br /><br />The film will appeal to three types of audience: those who love martial arts films, those who love vampire films and those who loath the rubbish films Hollywood generally churns out.<br /><br />The premise for the film is that vampires are about and a secret society seeks to hunt them down before we all become snacks for the undead. This bloody work is carried out by some martial artists who drink a little vampire blood to give them the edge they need, well it must be thirsty work! Things are going pretty much for the course until a particularly nasty European vamp finds out that he if he obtains a set of keys held by all the vampire princes then he can walk around in sunlight etc and generally eat when ever he wants to. To say anymore on the plot would spoil the enjoyment of watching the film.<br /><br />The twins consist of one assigned vampire slayer (Chung) and the sister (Choi) of another. It is the twins that really make the film; with some of the freshest and funniest acting going. The fight scenes they carry out are fast and furious and well choreographed with a mix of genuine athleticism and wire work. To add the cherry on the cake the twins are both quite lovely to watch too.<br /><br />The direction is crisp and the script is sharp. There are only 3 things that let this film down: the make-up for the vampires is quite poor, Jackie Chan seems to be in the film just for the hell of it and adds nothing to its content, and some of the slapstick comedy attempted by the male vampire hunter is quite lame. Thankfully the twins save the day bringing an originality to the film normally only found in European films. The best scene for me was one of them (Choi) communicating only by screaming, her ability to convey her thoughts through this medium was a comic delight.<br /><br />Their are many other touches of originality in this film - I particularly liked the coffin complete with surround sound stereo and TV screen! And it is the films' many original touches and acting that stops this from being a tired old flop and turns it into a must see movie.",
    "Oh my God... where to begin? \"Chupacabra Terror\" is one of the worst B-Horror movies ever made. This crap makes \"Demon Slayer\" look like \"The Exorcist\". Special note: A Horror B-movie needs to have at least one sex scene. Don't expect even a hot girl in this one. With that inexcusable mistake, I should begin with the complete bash.<br /><br />First of all, if you're going to make a Horror monster movie, you should spend big part of the budget in creating a \"cool\" monster outfit. The monster in this movie looks like a $10 Halloween costume. There is no way the Chupacabras (yes, this is how it is spelled) looks menacing in the movie. It's an actor in a Halloween outfit please!! it looks so cheap it makes me mad. <br /><br />Second, the gore effects are the spinal cord of any direct to video monster Horror movie. Again, the producers decided not to spend for decent gore effects. The blood looks damn fake! Please take a close look at the guy that gets chopped in two. That's probably the best scene in the movie and it lasts for about ten seconds. The ending is a very poor scene that won't leave you satisfied. <br /><br />The acting is the last thing you should expect to have quality in these kind of movies; but in this movie it's beyond terrible. A cast of nobodies with no acting experience make the fool out of themselves for about 85 minutes. Special mention deserves a blonde guy with curly hair that tries to convince SWAT members that he is sick. The coughing he fakes is beyond laughable. He's probably the worst actor ever in a B-Horror movie, no kidding. Also, Captain Peña delivers a terrible performance in the first ten minutes of the flick. <br /><br />The TRUE story behind the Chupacabras is not even told. All you get to know is that the monster sucks goat's blood. Why bother with this piece of crap? Plesae, do not even watch it even if you have the chance. Not even if it airs on cable. <br /><br />I usually support low budget Horror movies because the people involved in them at least try to do something \"different\" than Hollywood but that doesn't means that Horror fans like me should accept this kind of garbage."
    ]}

# nltk.download()
clean_train_reviews = []

for i in range(0, len(train["reviews"])):
    clean_train_reviews += KaggleWord2VecUtility.review_to_wordlist(train['reviews'][i])


vectorizer = CountVectorizer(analyzer = "word",
                            tokenizer = None,
                            preprocessor = None,
                            stop_words = None,
                            max_features =5000)

train_data_features = vectorizer.fit_transform(clean_train_reviews)
train_data_features = train_data_features.toarray()

forest = RandomForestClassifier(n_estimators = 100)
forest = forest.fit(train_data_features, train["sentiment"])

# print(train_data_features)
