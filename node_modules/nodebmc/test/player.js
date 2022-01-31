xbmc = require('../');

var browser = new xbmc.Browser();

browser.on('deviceOn', function(device){
    device.player('Player.PlayPause', function(){
    });
});