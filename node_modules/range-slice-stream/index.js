/*
Instance of writable stream.

call .get(length) or .discard(length) to get a stream (relative to the last end)

emits 'stalled' once everything is written

*/
const { Writable, PassThrough } = require('readable-stream')

class RangeSliceStream extends Writable {
  constructor (offset, opts = {}) {
    super(opts)

    this.destroyed = false
    this._queue = []
    this._position = offset || 0
    this._cb = null
    this._buffer = null
    this._out = null
  }

  _write (chunk, encoding, cb) {
    let drained = true

    while (true) {
      if (this.destroyed) {
        return
      }

      // Wait for more queue entries
      if (this._queue.length === 0) {
        this._buffer = chunk
        this._cb = cb
        return
      }

      this._buffer = null
      var currRange = this._queue[0]
      // Relative to the start of chunk, what data do we need?
      const writeStart = Math.max(currRange.start - this._position, 0)
      const writeEnd = currRange.end - this._position

      // Check if we need to throw it all away
      if (writeStart >= chunk.length) {
        this._position += chunk.length
        return cb(null)
      }

      // Check if we need to use it all
      let toWrite
      if (writeEnd > chunk.length) {
        this._position += chunk.length
        if (writeStart === 0) {
          toWrite = chunk
        } else {
          toWrite = chunk.slice(writeStart)
        }
        drained = currRange.stream.write(toWrite) && drained
        break
      }

      this._position += writeEnd

      toWrite = (writeStart === 0 && writeEnd === chunk.length)
        ? chunk
        : chunk.slice(writeStart, writeEnd)

      drained = currRange.stream.write(toWrite) && drained
      if (currRange.last) {
        currRange.stream.end()
      }
      chunk = chunk.slice(writeEnd)
      this._queue.shift()
    }

    if (drained) {
      cb(null)
    } else {
      currRange.stream.once('drain', cb.bind(null, null))
    }
  }

  slice (ranges) {
    if (this.destroyed) return null

    if (!Array.isArray(ranges)) ranges = [ranges]

    const str = new PassThrough()

    ranges.forEach((range, i) => {
      this._queue.push({
        start: range.start,
        end: range.end,
        stream: str,
        last: i === ranges.length - 1
      })
    })

    if (this._buffer) {
      this._write(this._buffer, null, this._cb)
    }

    return str
  }

  destroy (err) {
    if (this.destroyed) return
    this.destroyed = true

    if (err) this.emit('error', err)
  }
}

module.exports = RangeSliceStream
