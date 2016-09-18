const rest = require('rest');
const basicAuth = require('rest/interceptor/basicAuth');
const errorCode = require('rest/interceptor/errorCode');
const mime = require('rest/interceptor/mime');

exports.createGHIssueForHRChallenge = function (password, hackerRankChallenge) {
    const {description, href, title} = hackerRankChallenge;
    const client = rest.wrap(errorCode, {code: 500})
                       .wrap(mime, {mime: 'application/vnd.github.v3+json'})
                       .wrap(basicAuth, {
                           username: 'alexander-matsievsky',
                           password: password
                       });
    return client({
        method: 'POST',
        path: 'https://api.github.com/repos/alexander-matsievsky/HackerRank/issues',
        headers: {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
        },
        entity: {
            "title": title,
            "body": `[${title}](${href})${description ? `\n${description}` : ''}`,
            "assignees": [],
            "milestone": 2,
            "labels": ["Functional Programming"]
        }
    })
        .then(console.info.bind(console))
        .catch(console.error.bind(console));
};