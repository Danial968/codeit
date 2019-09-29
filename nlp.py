import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import torch
# import flair
# flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
# import nltk
nltk.download('stopwords')
# nltk.download('movie_reviews')
# nltk.download('punkt')
# import nltk.classify.util
# from nltk.classify import NaiveBayesClassifier
# from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    # my_dict = dict([(word, True) for word in useful_words])
    # return my_dict
    return useful_words

# def write_to_file(filename,result):
#     with open(filename,'w+') as f:
#         for line in result:
#             f.write(line + '\n')

def sentiment(sentences):

    # response = []

    # neg_reviews = []

    # for fileid in movie_reviews.fileids('neg'):
    #     words = movie_reviews.words(fileid)
    #     neg_reviews.append((create_word_features(words), "negative"))
    #     write_to_file('negative',create_word_features(words))

    # pos_reviews = []
    # for fileid in movie_reviews.fileids('pos'):
    #     words = movie_reviews.words(fileid)
    #     pos_reviews.append((create_word_features(words), "positive"))
    
    # train_set = neg_reviews[:750] + pos_reviews[:750]
    # test_set =  neg_reviews[750:] + pos_reviews[750:]

    # classifier = NaiveBayesClassifier.train(train_set)

    # accuracy = nltk.classify.util.accuracy(classifier, test_set)

    # for sentence in sentences:
    #     words = word_tokenize(sentence)
    #     words = create_word_features(words)
    #     classifier.classify(words)
    #     if classifier.classify(words) == "positive":
    #         response.append("positive")
    #     else:
    #         response.append("negative")

    response = []

    for sentence in sentences:
        # flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
        # s = flair.data.Sentence(sentence)
        # flair_sentiment.predict(s)
        # total_sentiment = s.labels
        # total_sentiment
        words = word_tokenize(sentence)
        words = create_word_features(words)
        new_sentence = " ".join(words)
        sid = SentimentIntensityAnalyzer()
        print(sid.polarity_scores(sentence))
        if sid.polarity_scores(sentence)["neg"] < sid.polarity_scores(sentence)["pos"]:
            response.append("positive")
        else:
            response.append("negative")
    
    return ""

test = {'reviews': ["What we have here the standard Disney direct to DVD sequel, where I would expect cots are cut in all areas resulting in an okay animated movie that falls well short of the original. That is not to say that this is a terrible movie it is just that it is a very mediocre movie full of the preachy messages intended to show children the virtues of friendship and being nice to one another and unless done subtly (which it is not here) can quickly become grating for adults. The film has a very thin plot line with Kronk trying to win the approval of his father, and ending up finding the true meaning of wealth and success. This has it's comedy moments but is really nor enough to carry a full length film.", "Magnificent, original, beautiful movie. The acting is great, the settings en decors are superb (Paris at its best- but then the real Paris, not the famous settings) and the music will do also. A brilliant storie, very detailed, which I just very much love.<br /><br />The best French movie I've seen (and French cinema is very good)!", '***SPOILERS*** Well made and interesting film about the alienated youth of America back in the 1950\'s. Back in those days many parents caught up with making big bucks and living high on the hog forget that their children, especially teen-agers, needed a lot more then a car and and hefty allowance in order to feel part of the family. They also needed love and attention, to their growing up problems, which is what 16 year-old Hal Ditmar, James MacArthur never got from his successful movie producer dad Mr.Tom Ditmar, James Daly.<br /><br />Never really connecting with his dad Hal grows more and more distant from both him and his caring mom Helen Ditmar, Kim Hunter, as well as from society. After his dad put Hal down about him wanting to borrow his car, a late model luxury sedan, he and his friend Jerry, Jeffery Silver, drive in Hal\'s beat up and barley operational 1930\'s jalopy to the local treater to catch the latest western flick.<br /><br />Feeling like striking out at the world Hal acts like a real first-class jerk sticking his smelly feet almost into the faces of a couple, Eddie Ryder & Jean Corbett, sitting in front of him and Jerry trying to watch the movie. This leads Hal, as well as his friend Jerry, to not only be kicked out of the theater but with him belting the theater manager Mr. Grebbs, Whit Bissell. It turned out that at least Hal was willing to leave the theater, without even getting his money back, but when Grebbs tries to grab him Hal wheeled around and belted him right in the kisser.<br /><br />Hal now in real hot water, he\'s charged with assault and battery, put\'s on his "James Dean" act, at the local police station, making like he\'s either too cool or just plain stupid to realize what he\'s done; almost knocked Mr. Grebbs teeth out. It\'s when Sgt.Shipley, James Gergory, tells Hal that his dad is coming to pick him up when he finally sobers up to the fact of what he\'s done.<br /><br />The rest of the film has Hal try to straighten himself out but is unable to do that because the low esteem that his dad has of him. Begging his father to understand that what he did, in belting Mr. Grebbs, was in self-defense Hal\'s father acts as if he\'s been there, at the theater, and saw the whole incident with his son Hal acting like a street thug instead of of a young man being grabbed and pushed without provocation.<br /><br />Not excusing what Hal did, in laying out Mr. Grebbs, he in fact was willing to admit his hooligan behavior but he wanted both Mr. Grebbs and his dad to at least treat him with an iota of consideration; Gebbs in the fact that he provoked Hal and Mr. Ditmas in not even bothering to hear him out! Feeling like a wanted criminal without anyone, but his mom, to really turn too Hal slowly loses it only to later have both Sgt. Shipley and Mr. Grabbs agree to drop the assault charge.You would think that by now Hal\'s has finally learned his lesson but the real lesson, more then a stretch behind bars, that Hal\'s so desperately needed was a lesson that his father totally ignored! Being there when his son needed him most and in that Mr. Ditmar failed with flying colors.<br /><br />Things do in fact straighten out for everyone in the movie only after Mr. Grebbs gets belted, ending up with a butte of a shiner, again by Hal who, going back to Grebbs theater, tries to get him to phone his dad and tell him that Hal was only defending himself when he first, not the second time around, clobbered him. In the end Hal learned a real lesson in getting along with people an not letting his problems become other peoples problems. But most of all Hal\'s father Mr. Ditmar learned the most valuable lesson of all in how to understand his frustrated and alienated son and act like a father toward him instead of a combination jail-keeper and a sugar daddy. Like the song says "All you need s Love" to get things on the right track and it was both love and understanding for his son Hal that Mr. Ditmar, until the very end of the movie, lacked the most off.', "This is a great, dark, offbeat little film, a modern day adaptation of the quest for the Holy Grail myth. It's a sleeper if there ever was one. I saw it on cable some years ago and taped it. I've loaned it to many of my friends and everyone loved it.", "I chose this movie really for my husband-who works in radio broadcasting. I thought that it would be more of a movie that he would enjoy and relate too, though it was from the eighties-so it was a little dated. This movie really draws you in. At times you just want to strangle the host, Barry. At times you just want to send some of the bigots who call in to a true concentration camp. At times you really feel sorry for Barry, because he has truly gotten too big for his jeans if you know what I mean. It was on the Drama channel on Encore-so I am thinking this is a true story. If you truly love dramas you will love this, even if you don't know all the ins and outs of the broadcasting business. If you are an Alec Baldwin fan and are watching it to see him, you shouldn't. His part is really a bit part in this movie.", "Don't worry when looking at the cover of the DVD, Sandra Bullock only appears at most 5 minutes in total in this cult classic. The entertainment value here is very high. <br /><br />To name but a few of the many highlights that should be paid attention to:<br /><br />- The doubled evil voices of the chief bad guys - The special gun cam - The weird masks and outfits of the hit killers - The showy ways to catch a bullet and hit the ground - The abundance of bottom-up shots - The spacey scene in which Bullock falls unconscious on the street - The over-cliché Italian mob guy Moe (LaMotta) - The cheap synthesizer background music - The mesmerizing overdone gun fetishism<br /><br />And last but not least: the super corny fist-fight scenes. Wish there would have been more of those...<br /><br />Extra point for the successful attempt at making me laugh out loud.", "When all we have anymore is pretty much reality TV shows with people making fools of themselves for whatever reason be it too fat or can't sing or cook worth a damn than I know Hollywood has run out of original ideas. I can not recall a time when anything original or intelligent came out on TV in the last 15 years. What is our obsession with watching bums make fools of themselves? I would have thought these types of programs would have run full circle but every year they come up with something new that is more strange then the one before. OK so people in this one need to lose weight...most Americans need to lose weight. I just think we all to some degree enjoy watching people humiliated. Maybe it makes us feel better when we see someone else looking like a jerk. I don't know but I just wish something intelligent would come out that did not insult your intelligence.", 'Although compared with "Mad Max", this film is in a league of its own.Set in post apocalyptic Paris, this film is about man\'s struggle for survival, he has lost his ability to speak, and there is a remarkable shortage of women. CONGRATULATIONS LUC BESSON!', 'I checked this out for free at the library, and I still feel ripped off. Yes, Sandra Bullock is actually in it, but only in five scenes totaling up to barely 5 minutes, and even those are fairly painful to watch. The rest of the movie is so bad that you\'ll spend most of the time hoping it will end soon, but only if you\'re one of those people who have to finish a movie once they start it. Everyone else will just turn it off. Don\'t worry, you aren\'t going to miss anything. Bullock\'s lines (assuming that you were tricked into watching this because her name is plastered on the case) are essentially just parroting of other characters lines, like this dialog:<br /><br />Lisa (Bullock) - "Danny, please tell me what is going on."<br /><br />Danny - "I don\'t know." <br /><br />Lisa - "Whaddaya mean you don\'t know?" <br /><br />Danny - "I don\'t know - it\'s something to do with my Dad." <br /><br />Lisa - "Whaddaya mean your Dad?" <br /><br />Danny - "I don\'t know - he ****ed up or something." <br /><br />Lisa - "Why am I here?" <br /><br />Danny - "I\'m sorry Lisa. I don\'t know." <br /><br />(moments later) Danny - "Some army buddies of my Dad . . . " <br /><br />Lisa - "Whaddaya mean army buddies?"<br /><br />See what I mean? <br /><br />Bottom line - Just say no.']}
print(sentiment(test["reviews"]))