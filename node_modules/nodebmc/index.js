var util = require( 'util' );
var events = require( 'events' );
var Device = require('./device').Device;
var mdns = require('mdns-js');

var Browser = function( options ) {
    events.EventEmitter.call( this );
    this.init( options );
};

util.inherits( Browser, events.EventEmitter );

exports.Browser = Browser;

Browser.prototype.init = function( options ) {
    var self = this;

    var mdnsBrowser = mdns.createBrowser(mdns.tcp('xbmc-jsonrpc-h'));

    mdnsBrowser.on('ready', function () {
        mdnsBrowser.discover();
    });

    mdnsBrowser.on('update', function (device) {
        console.log(device);
        var dev_config = {addresses: device.addresses, port: device.port, name: device.type[0].name};
        self.device = new Device(dev_config);
        self.emit('deviceOn', self.device);
    });

};