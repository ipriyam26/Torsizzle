nodebmc
=================

nodebmc is a client library for xbmc.

## Installation

From npm:

	npm install nodebmc

From source:

	git clone https://github.com/gtuk/nodebmc.git
	npm link


## Usage

``` javascript
// remote video
var browser = require( 'nodebmc' ).createBrowser();
browser.on( 'deviceOn', function( device ) {
    device.play( 'http://remotehost/video.mp4', function() {
        console.info( 'video playing...' );
    });
});
browser.start();
```

For more examples visit test folder