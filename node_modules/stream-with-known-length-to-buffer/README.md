# stream-with-known-length-to-buffer [![travis][travis-image]][travis-url] [![npm][npm-image]][npm-url] [![downloads][downloads-image]][downloads-url] [![javascript style guide][standard-image]][standard-url]

[travis-image]: https://img.shields.io/travis/feross/stream-with-known-length-to-buffer/master.svg
[travis-url]: https://travis-ci.org/feross/stream-with-known-length-to-buffer
[npm-image]: https://img.shields.io/npm/v/stream-with-known-length-to-buffer.svg
[npm-url]: https://npmjs.org/package/stream-with-known-length-to-buffer
[downloads-image]: https://img.shields.io/npm/dm/stream-with-known-length-to-buffer.svg
[downloads-url]: https://npmjs.org/package/stream-with-known-length-to-buffer
[standard-image]: https://img.shields.io/badge/code_style-standard-brightgreen.svg
[standard-url]: https://standardjs.com

#### Convert a Readable Stream with a known length into a Buffer

[![Sauce Test Status](https://saucelabs.com/browser-matrix/stream-with.svg)](https://saucelabs.com/u/stream-with)

This package converts a Readable Stream into a Buffer, with just one Buffer
allocation (excluding allocations done internally by the streams implementation).

This is lighter-weight choice than
[`stream-to-array`](https://github.com/stream-utils/stream-to-array) when the
total stream length is known in advance. This whole package is 15 lines.

This module is used by [WebTorrent](https://webtorrent.io).

### install

```
npm install stream-with-known-length-to-buffer
```

### usage

```js
var toBuffer = require('stream-with-known-length-to-buffer')

toBuffer(fs.createReadStream('file.txt'), 1000, function (err, buf) {
  if (err) return console.error(err.message)
  console.log(buf)
})
```

### license

MIT. Copyright (c) [Feross Aboukhadijeh](http://feross.org).
