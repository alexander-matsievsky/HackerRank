const $1 = require('./getHRChallengesForHRSubDomain');
const $2 = require('./createGHIssueForHRChallenge');

module.exports = {
    createGHIssuesForHRSubDomain(password, hrSubDomain, label) {
        return $1.getHRChallengesForHRSubDomain(hrSubDomain)
                 .then(hrChallenges =>
                     Promise.all(hrChallenges.map(hrChallenge =>
                         $2.createGHIssueForHRChallenge(password, hrChallenge, label)
                     ))
                 )
                 .then(console.info.bind(console))
                 .catch(console.error.bind(console));
    }
};

module.exports.createGHIssuesForHRSubDomain(
    '4d99bb8071d4ad297ac716c1fea821615b422347',
    'https://www.hackerrank.com/domains/python/py-introduction',
    {domain: 'Python', subDomain: 'Introduction'}
);
