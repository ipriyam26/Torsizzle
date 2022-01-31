xbmc = require('../');

var browser = new xbmc.Browser();

browser.on('deviceOn', function(device){
    device.input('Input.Back', function(){
    });
});

/*browser.on('deviceOn', function(device){
    device.input('Input.ContextMenu', function(){
    });
});

browser.on('deviceOn', function(device){
    device.input('Input.Down', function(){
    });
});

browser.on('deviceOn', function(device){
    device.input('Input.Home', function(){
    });
});

browser.on('deviceOn', function(device){
    device.input('Input.Info', function(){
    });
});

browser.on('deviceOn', function(device){
    device.input('Input.Left', function(){
    });
});

browser.on('deviceOn', function(device){
    device.input('Input.Right', function(){
    });
});

browser.on('deviceOn', function(device){
    device.input('Input.Select', function(){
    });
});

browser.on('deviceOn', function(device){
    device.input('Input.ShowCodec', function(){
    });
});

browser.on('deviceOn', function(device){
    device.input('Input.ShowOSD', function(){
    });
});

browser.on('deviceOn', function(device){
    device.input('Input.Up', function(){
    });
})*/
