#!/usr/bin/env node

var cp = require('child_process')
var vlcCommand = require('./')

var arg = process.argv[2]

if (!arg || arg === '--help' || arg === '-h') {
  console.log(`
Usage:
    vlc-command <option>

Options:
    --open, -o     Open VLC.
    --path, -p     Print VLC path.
    --help, -h     Print usage information.
    --version, -v  Print version.
  `)
}

if (arg === '--path' || arg === '-p') {
  vlcCommand(function (err, command) {
    if (err) throw err
    console.log(command)
  })
}

if (arg === '--open' || arg === '-o') {
  vlcCommand(function (err, command) {
    if (err) throw err
    if (process.platform === 'win32') {
      cp.execFile(command, onExit)
    } else {
      cp.exec(command, onExit)
    }
  })
}

function onExit (err, stdout, stderr) {
  console.log(stdout)
  console.error(stderr)
  if (err) throw err
}

if (arg === '--version' || arg === '-v') {
  console.log(require('./package.json').version)
}
