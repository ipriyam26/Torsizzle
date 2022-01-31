# chunk-store-stream [![ci][ci-image]][ci-url] [![npm][npm-image]][npm-url] [![downloads][downloads-image]][downloads-url] [![javascript style guide][standard-image]][standard-url]

[ci-image]: https://img.shields.io/github/workflow/status/feross/chunk-store-stream/ci/master
[ci-url]: https://github.com/feross/chunk-store-stream/actions
[npm-image]: https://img.shields.io/npm/v/chunk-store-stream.svg
[npm-url]: https://npmjs.org/package/chunk-store-stream
[downloads-image]: https://img.shields.io/npm/dm/chunk-store-stream.svg
[downloads-url]: https://npmjs.org/package/chunk-store-stream
[standard-image]: https://img.shields.io/badge/code_style-standard-brightgreen.svg
[standard-url]: https://standardjs.com

#### Convert an [abstract-chunk-store](https://github.com/mafintosh/abstract-chunk-store) store into a readable or writable stream

[![abstract chunk store](https://cdn.rawgit.com/mafintosh/abstract-chunk-store/master/badge.svg)](https://github.com/mafintosh/abstract-chunk-store)

Read/write data from/to a chunk store, with streams.

## Install

```
npm install chunk-store-stream
```

## Usage

### Create a read stream

``` js
const { ChunkStoreReadStream } = require('chunk-store-stream')
const FSChunkStore = require('fs-chunk-store') // any chunk store will work

const chunkLength = 3
const store = new FSChunkStore(chunkLength)

// ... put some data in the store

const stream = new ChunkStoreReadStream(store, chunkLength, { length: 6 })
stream.pipe(process.stdout)
```

### Create a write stream

```js
const { ChunkStoreWriteStream } = require('chunk-store-stream')
const FSChunkStore = require('fs-chunk-store') // any chunk store will work
const fs = require('fs')

const chunkLength = 3
const store = new FSChunkStore(chunkLength)

const stream = new ChunkStoreWriteStream(store, chunkLength)
fs.createReadStream('file.txt').pipe(stream)
```

## License

MIT. Copyright (c) [Feross Aboukhadijeh](https://feross.org).
