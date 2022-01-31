/* global self */

const Rusha = require('rusha')
const rushaWorkerSha1 = require('./rusha-worker-sha1')

const rusha = new Rusha()
const scope = typeof window !== 'undefined' ? window : self
const crypto = scope.crypto || scope.msCrypto || {}
let subtle = crypto.subtle || crypto.webkitSubtle

function sha1sync (buf) {
  return rusha.digest(buf)
}

// Browsers throw if they lack support for an algorithm.
// Promise will be rejected on non-secure origins. (http://goo.gl/lq4gCo)
try {
  subtle.digest({ name: 'sha-1' }, new Uint8Array()).catch(function () {
    subtle = false
  })
} catch (err) { subtle = false }

function sha1 (buf, cb) {
  if (!subtle) {
    if (typeof window !== 'undefined') {
      rushaWorkerSha1(buf, function onRushaWorkerSha1 (err, hash) {
        if (err) {
          // On error, fallback to synchronous method which cannot fail
          cb(sha1sync(buf))
          return
        }

        cb(hash)
      })
    } else {
      queueMicrotask(() => cb(sha1sync(buf)))
    }
    return
  }

  if (typeof buf === 'string') {
    buf = uint8array(buf)
  }

  subtle.digest({ name: 'sha-1' }, buf)
    .then(function succeed (result) {
      cb(hex(new Uint8Array(result)))
    },
    function fail () {
      // On error, fallback to synchronous method which cannot fail
      cb(sha1sync(buf))
    })
}

function uint8array (s) {
  const l = s.length
  const array = new Uint8Array(l)
  for (let i = 0; i < l; i++) {
    array[i] = s.charCodeAt(i)
  }
  return array
}

function hex (buf) {
  const l = buf.length
  const chars = []
  for (let i = 0; i < l; i++) {
    const bite = buf[i]
    chars.push((bite >>> 4).toString(16))
    chars.push((bite & 0x0f).toString(16))
  }
  return chars.join('')
}

module.exports = sha1
module.exports.sync = sha1sync
