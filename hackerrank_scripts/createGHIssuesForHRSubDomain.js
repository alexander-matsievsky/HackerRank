const {getHRChallengesForHRSubDomain} = require('./getHRChallengesForHRSubDomain');
const {createGHIssueForHRChallenge} = require('./createGHIssueForHRChallenge');

exports.createGHIssuesForHRSubDomain = function (password, hrSubDomain) {
    return getHRChallengesForHRSubDomain(hrSubDomain)
        .then(hrChallenges =>
            Promise.all(hrChallenges.map(hrChallenge =>
                createGHIssueForHRChallenge(password, hrChallenge)
            ))
        )
        .then(console.info.bind(console))
        .catch(console.error.bind(console));
};

exports.createGHIssuesForHRSubDomain(
    'https://github.com/settings/tokens',
    'https://www.hackerrank.com/domains/fp/recursion'
);