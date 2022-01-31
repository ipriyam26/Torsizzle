/*! stream-to-blob-url. MIT License. Feross Aboukhadijeh <https://feross.org/opensource> */
module.exports = getBlobURL

const getBlob = require('stream-to-blob')

async function getBlobURL (stream, mimeType) {
  const blob = await getBlob(stream, mimeType)
  const url = URL.createObjectURL(blob)
  return url
}
