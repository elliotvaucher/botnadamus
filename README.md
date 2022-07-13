# Botnadamus

### [botnadamus](https://twitter.com/botnadamus) is a twitter bot that predicts your future 🤖🔮👀

----
- [About](#about)
- [Services](#services)
- [Credits](#credits)

## About

This is how @botnadamus presents himself on Twitter : 

> 👋 Hello. I’m a bot. A bot that knows your future. 
> What is it you wanna know ? 
> Formulate your question precisely in your head. Meditate on your question. Is it the right one ?
> Once your question is clear enough, ask it. Don’t forget the 
> @botnadamus mention.

You can test it [here](https://twitter.com/botnadamus) !

Under the robotic hood is a simple program that performs the following instructions : 

- Look for new mentions on his timeline (@botnadamus)
- If new mention : fetches a random gif from [Giphy](https://giphy.com/) / posts it in reply to the orginal tweet.
- If no new mention : sleeps and starts back. 

As you can see, the program is amazingly simple. Yet, the results are powerful. **Because human mind always seeks to generate meaning**. Even the simplest form of randomized message is interpreted as a sign of some powerful symbolic divinity. 

When I asked him "what I was doing wrong", on the very day where I managed to resolve all issues and finally make him work autonomously on a [Heroku Dyno](https://www.heroku.com/dynos), he gave me this answer : 

https://user-images.githubusercontent.com/67040832/163135240-0f56c20f-f8b9-46a2-9aa8-54fdbfa171d7.mp4

This is how our brains work : it **secretes meaning**. The intelligence we perceive in machines and progams is a transfer of our own power of imagination. 

Go ahead, ask botnadamus anything. And try to pretend you didn't attached meaning to the pure randomness of his answer.

## Services

The main program uses the following services : 

- [Twitter API](https://developer.twitter.com/en/docs/twitter-api) : Twitter API provides you with all the necessary tools and credentials to authenticate your bot.  
- [Tweepy](https://www.tweepy.org/) : The Tweepy library gives you the Python syntax used to acess the Twitter API (*note : I mainly used the mentions_timeline method*). 
- [Giphy API](https://developers.giphy.com/) : Giphy API provides you with all the necessary tools and credentials to communicate with the Giphy powerful platform.
- [Heroku](https://dashboard.heroku.com/) : Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. (*note : the have a free pricing plan called "Free and Hobby", which I used for this bot*). 

## Credits 

The main building blocks to create a Twitter bot were taken from this tutorial : https://realpython.com/twitter-bot-python-tweepy/. 
The step by step guide for deploying a Twitter bot on Heroku comes from here : https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39. Note : I skipped the steps involving the creation of a Flask web server, and used the [Heroku Redis](https://devcenter.heroku.com/articles/heroku-redis) option instead. 

## Important Disclaimer 

Botnadamus is an art project. It's not optimized for large-scale development. Sometimes, Heroku are doing maintenance on their servers, and it happens that Botnadamus retweets answers he already posted on your solicitations. It's not a big deal I suppose. It will only get you more Twitter activity ;). But thanks for the understanding. I will find a way to optimize this issue in the future. 
