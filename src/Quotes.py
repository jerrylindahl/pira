import random


class Quotes:
    def __init__(self):
        self.qs = [
            "You are disoriented. Blackness swims toward you like a school of eels who have just seen something that "
            "eels like a lot.",

            "Driving a Porsche in London is like bringing a Ming vase to a football game.",

            "The idea that Bill Gates has appeared like a knight in shining armour to lead all customers out of a mire "
            "of technological chaos neatly ignores the fact that it was he, by peddling second rate technology, led "
            "them into it in the first place, and continues to do so today.",

            "We don't have to save the world. The world is big enough to look after itself. What we have to be "
            "concerned about is whether or not the world we live in will be capable of sustaining us in it.",

            "If it looks like a duck, and quacks like a duck, we have at least to consider the possibility that we "
            "have a small aquatic bird of the family Anatidae on our hands.",

            "It can hardly be a coincidence that no language on Earth has ever produced the expression "
            "\"As pretty as an airport.\"",

            "...he had a tremendous propensity for getting lost when driving. This was largely because of his \"Zen\" "
            "method of navigation, which was simply to find any car that looked as if it knew where it was going and "
            "follow it. The results were more often surprising than successful, but he felt it was worth it for the "
            "sake of the few occasions when it was both.",

            "(Ford) \"you'd better be prepared for the jump into hyperspace. It's unpleasantly like being drunk.\""
            "(Arthur) \"What's so unpleasant about being drunk?\""
            "(Ford) \"Ask a glass of water.\"",

            "Arthur looked up. \"Ford!\" he said, \"there's an infinite number of monkeys outside who want to talk to"
            "us about this script for Hamlet they've worked out.\"",

            "To summarize: it is a well known fact that those people who most want to rule people are, ipso facto, "
            "those least suited to do it. To summarize the summary: anyone who is capable of getting themselves made "
            "President should on no account be allowed to do the job. To summarize the summary of the summary: "
            "people are a problem.",

            "The major difference between a thing that might go wrong and a thing that cannot possibly go wrong is "
            "that when a thing that cannot possibly go wrong goes wrong it usually turns out to be impossible to get "
            "at or repair.",
        ]

    def get_random(self):
        return random.choice(self.qs) + " -- Douglas Adams"

