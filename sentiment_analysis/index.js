var sentiment = require('sentiment');
var mongoose = require('mongoose');
var async = require('async');
var Tweets = require('./tweets');

var positive = 0;
var neutral = 0;
var negative = 0;

var performAnalysis = function(tweets) {
	async.eachSeries(tweets, function(tweet, done) {
		// if(tweet.score) return done();

		sentiment(tweet.text, function (err, result) {
			if(err) {
				console.error("Error on tweet with id " + tweet._id + ": " + err);
				return done();
			}

			if(result.score <= -2) {
				negative++;
			}else if(result.score >= 2) {
				positive++;
			} else {
				neutral++;
			}
			
			
			done();

		});
	}, function() {
		console.info("Script completed");
		console.log("positive: " + positive);
		console.log("neutral: " + neutral);
		console.log("negative: " + negative);
		process.exit(0);
	});
}

mongoose.connect("mongodb://localhost/tdt4215", function (err, res) {
	if (err) {
		console.error("Database error. Exiting");
		process.exit(1);
	}


	Tweets.find({candidate:"johnkasich"}, function(err, tweets)  {
		performAnalysis(tweets);
	});
});