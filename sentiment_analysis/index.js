var sentiment = require('sentiment');
var mongoose = require('mongoose');
var async = require('async');
var Tweets = require('./tweets');

var performAnalysis = function(tweets) {
	async.eachSeries(tweets, function(tweet, done) {
		// console.info("Processing tweet with id " + tweet._id);
		// if(tweet.score) return done();

		sentiment(tweet.text, function (err, result) {
			if(err) {
				console.error("Error on tweet with id " + tweet._id + ": " + err);
				return done();
			}
			
			console.log({
				score: result.score,
				candidate: tweet.candidate
			});
			return done();
			// tweet.score = result.score;

			// console.log(tweet._id);
			// console.log(tweet.score);
			// Tweets.findOneAndUpdate(tweet._id, {score: tweet.score}, function(err, doc){
			// 	if(err) console.error('Error when updating tweet with id ' + tweet._id + ": " + err);
			// 	console.log(doc.score);
			// 	return done();
			// });
			// tweet.save(function(err) {
			// 	console.log("ERROR: " + err);
			// 	if(err) console.error('Error when updating tweet with id ' + tweet._id + ": " + err);
			// 	return done();
			// });
		});
	}, function() {
		console.info("Script completed");
		process.exit(0);
	});
}

mongoose.connect("mongodb://localhost/tdt4215", function (err, res) {
	if (err) {
		console.error("Database error. Exiting");
		process.exit(1);
	}

	Tweets.find({}, function(err, tweets)  {
		performAnalysis(tweets);
	});
});