/*! lt_donthave. MIT License. WebTorrent LLC <https://webtorrent.io/opensource> */
const arrayRemove = require('unordered-array-remove')
const { EventEmitter } = require('events')
const debug = require('debug')('lt_donthave')

module.exports = () => {
  class ltDontHave extends EventEmitter {
    constructor (wire) {
      super()

      this._peerSupports = false
      this._wire = wire
    }

    onExtendedHandshake () {
      this._peerSupports = true
    }

    onMessage (buf) {
      let index
      try {
        index = buf.readUInt32BE()
      } catch (err) {
        // drop invalid messages
        return
      }

      if (!this._wire.peerPieces.get(index)) return
      debug('got donthave %d', index)
      this._wire.peerPieces.set(index, false)

      this.emit('donthave', index)
      this._failRequests(index)
    }

    donthave (index) {
      if (!this._peerSupports) return

      debug('donthave %d', index)
      const buf = Buffer.alloc(4)
      buf.writeUInt32BE(index)

      this._wire.extended('lt_donthave', buf)
    }

    _failRequests (index) {
      const requests = this._wire.requests
      for (let i = 0; i < requests.length; i++) {
        const req = requests[i]
        if (req.piece === index) {
          arrayRemove(requests, i)
          i -= 1 // Check the new value at the same slot
          this._wire._callback(req, new Error('peer sent donthave'), null)
        }
      }
    }
  }

  // Name of the bittorrent-protocol extension
  ltDontHave.prototype.name = 'lt_donthave'

  return ltDontHave
}
