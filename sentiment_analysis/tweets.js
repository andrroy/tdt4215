var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// TODO: Fill in missing fields
var tweetSchema = new Schema({
	_id: { type: String, trim: true, required: true, unique: true },
	text: { type: String, required: true },
	candidate: { type: String, required: true },
	score: {type: Number, required: true}
});

var Tweets = mongoose.model('tweets', tweetSchema);

module.exports = Tweets;