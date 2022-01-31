/*! load-ip-set. MIT License. WebTorrent LLC <https://webtorrent.io/opensource> */
const fs = require('fs')
const get = require('simple-get')
const IPSet = require('ip-set')
const Netmask = require('netmask').Netmask
const once = require('once')
const split = require('split')
const zlib = require('zlib')

// Match single IPs and IP ranges (IPv4 and IPv6), with or without a description
const ipSetRegex = /^\s*(?:[^#].*?\s*:\s*)?([a-f0-9.:]+)(?:\s*-\s*([a-f0-9.:]+))?\s*$/

// Match CIDR IPv4 ranges in the form A.B.C.D/E, with or without a description
const cidrRegex = /^\s*(?:[^#].*?\s*:\s*)?([0-9.:]+)\/([0-9]{1,2})\s*$/

function loadIPSet (input, opts, cb) {
  if (typeof opts === 'function') return loadIPSet(input, {}, opts)
  cb = once(cb)

  if (Array.isArray(input) || !input) {
    process.nextTick(() => {
      cb(null, new IPSet(input))
    })
  } else if (/^https?:\/\//.test(input)) {
    opts.url = input
    get(opts, (err, res) => {
      if (err) return cb(err)
      onStream(res)
    })
  } else {
    let f = fs.createReadStream(input).on('error', cb)
    if (/.gz$/.test(input)) f = f.pipe(zlib.Gunzip())
    onStream(f)
  }

  function onStream (stream) {
    const blocklist = []
    stream
      .on('error', cb)
      .pipe(split())
      .on('data', line => {
        let match = ipSetRegex.exec(line)
        if (match) {
          blocklist.push({ start: match[1], end: match[2] })
        } else {
          match = cidrRegex.exec(line)
          if (match) {
            const range = new Netmask(`${match[1]}/${match[2]}`)
            blocklist.push({ start: range.first, end: range.broadcast || range.last })
          }
        }
      })
      .on('end', () => {
        cb(null, new IPSet(blocklist))
      })
  }
}

module.exports = loadIPSet
