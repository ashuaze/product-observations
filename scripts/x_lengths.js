// Offline wrapper around the unmodified official twitter-text distribution.
const fs = require('fs');
const twitterText = require('../vendor/twitter-text-3.1.0.js');
const posts = JSON.parse(fs.readFileSync(0, 'utf8'));
if (!Array.isArray(posts) || posts.some(post => typeof post !== 'string')) {
  throw new TypeError('Expected an array of post strings');
}
process.stdout.write(JSON.stringify(posts.map(post => {
  const parsed = twitterText.parseTweet(post);
  return { weightedLength: parsed.weightedLength, valid: parsed.valid };
})));
