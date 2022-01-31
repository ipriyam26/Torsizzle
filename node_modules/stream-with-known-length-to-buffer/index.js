/*! stream-with-known-length-to-buffer. MIT License. Feross Aboukhadijeh <https://feross.org/opensource> */
var once = require('once')

module.exports = function getBuffer (stream, length, cb) {
  cb = once(cb)
  var buf = Buffer.alloc(length)
  var offset = 0
  stream
    .on('data', function (chunk) {
      chunk.copy(buf, offset)
      offset += chunk.length
    })
    .on('end', function () { cb(null, buf) })
    .on('error', cb)
}
