require('urijs/src/URITemplate');
const rest = require('rest');
const errorCode = require('rest/interceptor/errorCode');
const mime = require('rest/interceptor/mime');
const URI = require('urijs');

exports.getHRChallengesForHRSubDomain = function (hrSubDomain) {
    hrSubDomain = new URI(hrSubDomain);
    const client = rest.wrap(errorCode, {code: 500})
                       .wrap(mime, {mime: 'application/json'});
    return client({
        path: URI.expand(
            'https://www.hackerrank.com/rest/contests/master/categories{/category}/challenges{?page*}',
            {
                category: `${hrSubDomain.segment(1)}|${hrSubDomain.segment(2)}`,
                page: {offset: 0, limit: 1000}
            }
        ).href(),
        headers: {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
        }
    })
        .then(response =>
            response.entity.models.map(model => ({
                title: model.name,
                description: model.preview,
                href: URI.expand('https://www.hackerrank.com/challenges{/challenge}', {
                    challenge: model.slug
                }).href(),
            }))
        )
        .catch(console.error.bind(console));
};