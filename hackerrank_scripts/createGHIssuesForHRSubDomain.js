const $1 = require('./getHRChallengesForHRSubDomain');
const $2 = require('./createGHIssueForHRChallenge');

function delay(ms) {
    return () => new Promise(resolve => {
        setTimeout(resolve, ms);
    });
}

module.exports = {
    createGHIssuesForHRSubDomain(password, hrSubDomain, label) {
        return $1.getHRChallengesForHRSubDomain(hrSubDomain)
                 .then(hrChallenges =>
                     hrChallenges.reduce(
                         (chain, hrChallenge) => chain.then(delay(.5E3)).then(() =>
                             $2.createGHIssueForHRChallenge(password, hrChallenge, label)
                         ),
                         Promise.resolve()
                     )
                 )
                 .then(response => {
                     console.info(response.entity);
                 })
                 .catch(response => {
                     console.error(response.status);
                 });
    }
};

module.exports.createGHIssuesForHRSubDomain(
    '4d99bb8071d4ad297ac716c1fea821615b422347',
    'https://www.hackerrank.com/domains/python/py-collections',
    {domain: 'Python', subDomain: 'Collections'}
);
