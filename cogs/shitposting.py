import discord
from discord.ext import commands


class shitposts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message):
        await bot.process_commands(message)
        if message.author == bot.user:
            return None
        if "the senate" in message.content.lower():
            output = "**Did you ever hear the tragedy of Darth Plagueis the Wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic, he could save others from death, but not himself.** \n\nhttps://imgur.com/8KPtRjS.png"
            await message.channel.send(output)
        if "alpha" in message.content.lower():
            output = "I am the ultimate alpha male. I only climax for 1 of 2 reasons. I either climax for the purpose of reproduction with a beautiful woman (because that's the only kind of woman worthy of me) or I climax for the purpose of free protein. I need immense protein to maintain my ultimate alpha male body, and 4-5 cum loads a day is sufficient for me. It's not gay if it's mine, but I wouldn't expect you pathetic beta males to understand. I bet you waste your seed into napkins, tissue, and tube socks. How sad, wasting all that protein. Wasting all those offspring. Its optimal for me to masturbate with my legs over my head so I can practice stretching before my workout while I obtain my protein. All the gym betas in the locker room just look away in disgust, but again, I wouldn't be offended by an asshole who only focus on vanity muscles. You beta losers better start acting like real men."
            await message.channel.send(output)
        if "based" in message.content.lower():
            output = "Based? Based on what? In your dick? Please shut the fuck up and use words properly you fuckin troglodyte, do you think God gave us a freedom of speech just to spew random words that have no meaning that doesn't even correllate to the topic of the conversation? Like please you always complain about why no one talks to you or no one expresses their opinions on you because you're always spewing random shit like poggers based cringe and when you try to explain what it is and you just say that it's funny like what? What the fuck is funny about that do you think you'll just become a stand-up comedian that will get a standing ovation just because you said \"cum\" in the stage? HELL NO YOU FUCKIN IDIOT, so please shut the fuck up and use words properly you dumb bitch"
            await message.channel.send(output)
        if "meow" in message.content.lower():
            output = """leash and treated like a domestic animal then that’s called a fetish, not “quirky” or “cute”. What part of you seriously thinks that any part of acting like a feline establishes a reputation of appreciation? Is it your lack of any defining aspect of personality that urges you to resort to shitty representations of cats to create an illusion of meaning in your worthless life? Wearing “cat ears” in the shape of headbands further notes the complete absence of human attribution to your false sense of personality, such as intelligence or charisma in any form or shape. Where do you think this mindset’s gonna lead you? You think you’re funny, random, quirky even? What makes you think that acting like a fucking cat will make a goddamn hyena laugh? I, personally, feel extremely sympathetic towards you as your only escape from the worthless thing you call your existence is to pretend to be an animal. But it’s not a worthy choice to assert this horrifying fact as a dominant trait, mainly because personality traits require an initial personality to lay their foundation on. You’re not worthy of anybody’s time, so go fuck off, “cat-girl”."""
            await message.channel.send(output)
        if "weed" in message.content.lower():
            output = """h-hewwo...owunce of weed pwease >///< arigato... dealer-kun puts weedie-chan in bong and inhales waaah!! (╯✧▽✧)╯ daisuki cannabis desu~! (^ ω ^ )uwaaa! weedie-chan i feel so kimochi!!(〃°ω°〃)"""
            await message.channel.send(output)
        if "gamer" in message.content.lower():
            output = """So the other day, I was playing rainbow six siege, and I heard one of my teammates make a callout in the voice chat. It was a real life gamer girl. God, I kid you not, I just stopped playing and pulled my dick out. “fuck, Fuck!” I was yelling in voice chat. I just wanted to hear her voice again. “Please,” I moaned. But she left the lobby. I was crying and covered in my own cum, but I remembered that I could find recent teammates in the ubiplay friends tab. I frantically closed down siege and opened the tab, to find out she had TTV IN HER NAME!!! She was streaming, and only had 100 viewers!!! The competition was low, so I made the first move and donated my months rent to her. I was already about to pre. She read my donation in the chat. God this is the happiest I’ve been in a long time. I did a little research, and found out where she goes to school, but I am a little nervous to talk to her in person, and need support. Any advice before my Uber gets to her middle school?"""
            await message.channel.send(output)
        if "bourgeoisie" in message.content.lower():
            output = ["""Folks, the bourgeois, they're no good, more and more people are saying it. All these workers— the biggest, we have the biggest workers— very handsome workers come up to me and say, Comrade Trump there is a specter haunting Europe, and you know what, they're right. These bourgeois are very nasty people, very very rude, and very unfair to the workers. They are stealing our surplus value and no one is doing anything about it. The proletariat comes up to me every day and says, Comrade Trump will you lead the revolution? And I gotta turn to them and say look, the instruments of capitalism will be used to bring about its destruction, believe me. The means of production, Obama never wanted to seize them. Well guess what? I'm seizing them. Landlords? They're done for folks. Everyone told me— they said, Comrade Trump you won't be the vanguard of the revolution and they would laugh, the media laughed the democrats laughed, guess who's laughing now?""",
                      """And then you have these capitalists, those are real beauties! This is their new hoax- they take a piece of machine, a big beautiful shiny new means of production, and they buy it and y'know, they own it, it's a big beautiful shiny new machine, all the bells and whistles, bing bing bing, and then they have the workers- who are totally not being treated fairly in this country, folks, BELIEVE ME, totally exploited, and they have these workers-and they pay them a certain amount, could beee... $20 per hour, could be TEN, could be FIVE, could be TWELVE, they pay them a certain amount, okay, and with their labor they build the product.""",
                      """And the owner of the machine, of the capital, "Capitalist" they turn around and sell the product at a yuge markup, they call it "profit." ok, so they call it profit! They don't sell it at the cost it took to make it, okay, so what do they do with this extra, you know what I call it? I call it surplus value. I call it surplus value, and do they share the surplus value with the people whose labor PROVIDED the value it took to make that product? I don't think so, folks.""",
                      """They stick in a bank and then they say "ohhhh I can't afford to pay you more!" Bad- BAD people. It's totally phony, folks. Raw deal, our proletariat are getting a raw deal. But not for long! We're gonna- and by the way it never occurs the workers to pool their resources and buy the big beautiful machine in order to share the profit that they created in the first place with their labour! And you know why? Because the capitalists pay the workers such a low wage they can't afford to then invest and pool their money and share in ownership... of the means of production! Can't do it! This is the biggest scam on the planet, folks! Boy, I've heard some real beauties but that one, WOW, that's a doozy. That's a real beauty. But we're gonna fix it, folks, we're gonna fix it, okay? and you know what the laborers are going to do? They're gonna WIN.""",
                      """Folks, what we did in 1917–the Revolution I call it, with a capital R–it's never been done before. So many big beautiful red flags, you couldn't even–now that, folks, that's a flag we stand up for, we don't kneel for our terrific red flag–and you couldn't even see the Winter Palace, you know. You know the Mensheviks, you take a look at what they said, and they were a, uh, a failed party, and Renegade Kautsky, very nasty to me but that's okay, they said we couldn't do it! They said, "Oh, Vlad, the material conditions are bad, we have to have a bourgeois republic to develop the forces of production." You know what that means, right? Semi-feudal economy! Okay, you get Semi-Feudal, and I said, I told them we can't have Semi-Feudal. Well, look at where we are now, Julius. We are going to develop the forces of production so fast it'll make your head spin. We are going to do in a generation what it took them many, many years to do. BELIEVE ME."""]
            for line in output:
                await message.channel.send(line)
        if "legos" in message.content.lower():
            output = """You know it isn't "Legos". You've had FUCKING YEARS to adjust to the actual, correct way to say the term. It's Lego. Lego bricks, Lego sets, Lego kits, Lego mini-figures, Lego City. There are no such things as "Legos". They don't exist. "Lego" refers to the COMPANY THAT MAKES THE TOY, and thus the shortening Lego is acceptable. Saying "I'm playing with my Lego" works because it's referring to the sets themselves: The individuals aspects that make of the toy from the bricks to the mini-figures to the electronics to the other little parts. It isn't claiming that the fucking square bricks are each a Lego. THE ENTIRE THING IS. If you were to say "I'm playing with my Legos" that implies that you're playing with at least two different types of Lego set at once, i.e. Lego City and Bionicle. Still saying LEGOS after all these years makes you look like an assclown. Here in Europe, the continent responsible for this toy (no, it wasn't made by America, no matter how much your capitalistic toy industry wants you to think), you'd be laughed out of the room if you said that."""
            await message.channel.send(output)
        if "grilled cheese" in message.content.lower():
            output = ["""A grilled cheese consists of only these following items. Cheese. Bread with spread (usually butter). This entire subreddit consist of "melts". Almost every "grilled cheese" sandwich i see on here has other items added to it. The fact that this subreddit is called "grilledcheese" is nothing short of utter blasphemy. Let me start out by saying I have nothing against melts, I just hate their association with sandwiches that are not grilled cheeses. Adding cheese to your tuna sandwich? It's called a Tuna melt. Totally different. Want to add bacon and some pretentious bread crumbs with spinach? I don't know what the hell you'd call that but it's not a grilled cheese. I would be more than willing to wager I've eaten more grilled cheeses in my 21 years than any of you had in your entire lives. I have one almost everyday and sometimes more than just one sandwich. Want to personalize your grilled cheese? Use a mix of different cheeses or use sourdough or french bread.""",
                      """But if you want to add some pulled pork and take a picture of it, make your own subreddit entitled "melts" because that is not a fucking grilled cheese. I'm not a religious man nor am I anything close to a culinary expert. But as a bland white mid-western male I am honestly the most passionate person when it comes to grilled cheese and mac & cheese. All of you foodies stay the hell away from our grilled cheeses and stop associating your sandwich melts with them. Yet again, it is utter blasphemy and it rocks me to the core of my pale being. Shit, I stopped lurking after 3 years and made this account for the sole purpose of posting this. I've seen post after post of peoples "grilled cheeses" all over reddit and it's been driving me insane. The moment i saw this subreddit this morning I finally snapped. Hell, I may even start my own subreddit just because I know this one exists now. You god damn heretics. Respect the grilled cheese and stop changing it into whatever you like and love it for it what it is. Or make your damn melt sandwich and call it for what it is. A melt."""]
            for line in output:
                await message.channel.send(line)
        if "epstein" in message.content.lower():
            output = ["""JOSH: Drake... where's Epstein?""",
                      """DRAKE: He’s right in there. See, I put him on suicide watch.""",
                      """[laugh track]""",
                      """JOSH: You were supposed to monitor him constantly.""",
                      """DRAKE: Dude, I'm gonna!""",
                      """JOSH: Oh really?""",
                      """DRAKE: Yes!""",
                      """JOSH: So go check on him!""",
                      """DRAKE: Okay, I will! tcch""",
                      """[laugh track]""",
                      """[rattles the door, peeps through the door, turns around]""",
                      """DRAKE: ...I see the problem.""",
                      """JOSH: Oh do ya?"""]
            for line in output:
                await message.channel.send(line)
        if "drugs" in message.content.lower():
            output = """We should not be arrested for drugs if we are just vibing. If we are just vibing, it's our vibe, drugs a vibe so we should be able to vibe, it's part of our identity"""
            await message.channel.send(output)
        if "paris" in message.content.lower() or "venice" in message.content.lower():
            output = """You know Paris? In English, it's pronounced "Paris" but everyone else pronounces it without the "s" sound, like the French do. But with Venezia, everyone pronouces it the English way – "Venice". Like The Merchant of Venice or Death in Venice. WHY, THOUGH!? WHY ISN'T THE TITLE DEATH IN VENEZIA!? ARE YOU FUCKING KIDDING ME!? IT TAKES PLACE IN ITALY, SO USE THE ITALIAN WORD, DAMMIT! THAT SHIT PISSES ME OFF! BUNCH OF DUMBASSES!"""
            await message.channel.send(output)
        if "attack helicopter" in message.content.lower():
            output = """I sexually Identify as the "I sexually identify as an attack helicopter" joke. Ever since I was a child, I've dreamed of flippantly dismissing any concepts or discussions regarding gender that don't fit in with what I learned in 8th grade bio. People say to me that this joke hasn't been funny since 2014 and please at least come up with a new one, but I don't care, I'm hilarious. I'm having a plastic surgeon install Ctrl, C, and V keys on my body. From now on I want you guys to call me "epic kek dank meme tr***ies owned with facts and logic" and respect my right to shit up social media. If you can't accept me you're a memeophobe and need to check your ability-to-critically-think privilege. Thank you for being so understanding."""
            await message.channel.send(output)
        if "kfc" in message.content.lower():
            output = """One time I was asked if I was a legs man or a breasts man, I said I was into shaved pussy and anal and now I’m “banned from KFC” and “a possible sex offender”"""
            await message.channel.send(output)
        if "cat" in message.content.lower():
            output = """cat"""
            await message.channel.send(output)
        if "loli" in message.content.lower():
            output = ["""1. A fetish does not make you a creep. For instance, people can be turned on by incest porn, but not want to fuck their own sister. Furries don't often want to fuck animals. And PLENTY of people like porn that involves cheating or rape, but would NEVER do those. Just so, loli fans aren't just a bunch of pedos (though statistically maybe a few probably are, but you could say that about any fetish). For instance, I'm a loli fan myself, but I have an 8 year old daughter who regularly brings friends over, and not ONCE (I swear) have I seen a single one of them in a sexual light. I'm attracted to the cute designs and innocent attitudes of lolis, that doesn't mean I'm gonna go fuck children, that's obviously fucking disgusting. Not to mention, most lolis are legal, it's the design, NOT the age that makes a loli.?""",
                      """2. Anime style video games, and games from Japan always have the "cute" option when picking love interests. Usually some young, innocent girl with a shy attitude. And yes, I'm well aware Futaba kinda falls in that category too, but she can also fall under the "geeky girl" concept, which is also typically a separate option from the "cute" one. And since the twins are explained multiple times to be much older, that really does just make them cute, and nothing more. It's a very normal thing for a game like this to make them dateable.""",
                      """3. THEY'RE FUCKING VIRTUAL. At the end of the day, if my first two points didn't make you feel stupid, this one should. If you can't accept that people can have a fetish without becoming a creep, or that these are normal, long time tropes in Japanese games, then at least accept the fact that there's no point attacking people for wanting VIRTUAL CHARACTERS to be dateable. After all, who the hell is that hurting? Sure as hell not any kids, that's for sure. So why even bother getting pissy? What, cuz YOU don't wanna date em? Then don't! Simple as that!"""]
            for line in output:
                await message.channel.send(line)
        if "america" in message.content.lower() or "amerika" in message.content.lower() or "united states" in message.content.lower():
            output = """death to amerika"""
            await message.channel.send(output)


def setup(bot):
    bot.add_cog(shitposts(bot))