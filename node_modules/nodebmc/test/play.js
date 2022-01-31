xbmc = require('../');

var browser = new xbmc.Browser();

browser.on('deviceOn', function(device){
     device.play('http://commondatastorage.googleapis.com/gtv-videos-bucket/big_buck_bunny_1080p.mp4', function(){
        console.log('Playing in xbmc!');
    });
});