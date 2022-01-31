const { Transform } = require('readable-stream')

class Block extends Transform {
  constructor (size, opts = {}) {
    super(opts)

    if (typeof size === 'object') {
      opts = size
      size = opts.size
    }

    this.size = size || 512

    const { nopad, zeroPadding = true } = opts

    if (nopad) this._zeroPadding = false
    else this._zeroPadding = !!zeroPadding

    this._buffered = []
    this._bufferedBytes = 0
  }

  _transform (buf, enc, next) {
    this._bufferedBytes += buf.length
    this._buffered.push(buf)

    while (this._bufferedBytes >= this.size) {
      this._bufferedBytes -= this.size

      // Assemble the buffers that will compose the final block
      const blockBufs = []
      let blockBufsBytes = 0
      while (blockBufsBytes < this.size) {
        const b = this._buffered.shift()

        if (blockBufsBytes + b.length <= this.size) {
          blockBufs.push(b)
          blockBufsBytes += b.length
        } else {
          // If the last buffer is larger than needed for the block, just
          // use the needed part
          const neededSize = this.size - blockBufsBytes
          blockBufs.push(b.slice(0, neededSize))
          blockBufsBytes += neededSize
          this._buffered.unshift(b.slice(neededSize))
        }
      }

      // Then concat just those buffers, leaving the rest untouched in _buffered
      this.push(Buffer.concat(blockBufs, this.size))
    }
    next()
  }

  _flush () {
    if (this._bufferedBytes && this._zeroPadding) {
      const zeroes = Buffer.alloc(this.size - this._bufferedBytes)
      this._buffered.push(zeroes)
      this.push(Buffer.concat(this._buffered))
      this._buffered = null
    } else if (this._bufferedBytes) {
      this.push(Buffer.concat(this._buffered))
      this._buffered = null
    }
    this.push(null)
  }
}

module.exports = Block
