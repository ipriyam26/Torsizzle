# stream-to-blob-url [![travis][travis-image]][travis-url] [![npm][npm-image]][npm-url] [![downloads][downloads-image]][downloads-url] [![javascript style guide][standard-image]][standard-url]

[travis-image]: https://img.shields.io/travis/feross/stream-to-blob-url/master.svg
[travis-url]: https://travis-ci.org/feross/stream-to-blob-url
[npm-image]: https://img.shields.io/npm/v/stream-to-blob-url.svg
[npm-url]: https://npmjs.org/package/stream-to-blob-url
[downloads-image]: https://img.shields.io/npm/dm/stream-to-blob-url.svg
[downloads-url]: https://npmjs.org/package/stream-to-blob-url
[standard-image]: https://img.shields.io/badge/code_style-standard-brightgreen.svg
[standard-url]: https://standardjs.com

#### Convert a Readable Stream to a Blob URL

[![Sauce Test Status](https://saucelabs.com/browser-matrix/stream-to-blob-url.svg)](https://saucelabs.com/u/stream-to-blob-url)

This package converts a Readable Stream into a Blob URL.

This package is used by [WebTorrent](https://webtorrent.io).

## install

```
npm install stream-to-blob-url
```

## usage

```js
const toBlobURL = require('stream-to-blob-url')
const fs = require('fs')

const blobUrl = await toBlobURL(fs.createReadStream('file.txt'))
console.log(url)
```

## api

### promise = toBlobURL(stream, [mimeType], callback)

Convert the Readable `stream` into a W3C `Blob` URL (`blob:...`), optionally,
with the given `mimeType`.

Returns a `Promise` which resolves to a `string` on success. Otherwise, rejects
with an `Error`.

## license

MIT. Copyright (c) [Feross Aboukhadijeh](https://feross.org).
