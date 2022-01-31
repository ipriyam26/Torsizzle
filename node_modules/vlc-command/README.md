# vlc-command [![travis][travis-image]][travis-url] [![npm][npm-image]][npm-url] [![downloads][downloads-image]][downloads-url] [![javascript style guide][standard-image]][standard-url]

[travis-image]: https://img.shields.io/travis/feross/vlc-command/master.svg
[travis-url]: https://travis-ci.org/feross/vlc-command
[npm-image]: https://img.shields.io/npm/v/vlc-command.svg
[npm-url]: https://npmjs.org/package/vlc-command
[downloads-image]: https://img.shields.io/npm/dm/vlc-command.svg
[downloads-url]: https://npmjs.org/package/vlc-command
[standard-image]: https://img.shields.io/badge/code_style-standard-brightgreen.svg
[standard-url]: https://standardjs.com

### Find VLC player command line path

## install

```
npm install vlc-command
```

## usage

```js
var cp = require('child_process')
var vlcCommand = require('vlc-command')

vlcCommand(function (err, cmd) {
  if (err) return console.error('could not find vlc command path')

  if (process.platform === 'win32') {
    cp.execFile(cmd, ['--version'], function (err, stdout) {
      if (err) return console.error(err)
      console.log(stdout)
    })
  } else {
    cp.exec(cmd + ' --version', function (err, stdout) {
      if (err) return console.error(err)
      console.log(stdout)
    })
  }
})
```

## license

MIT. Copyright (c) [Feross Aboukhadijeh](http://feross.org).
