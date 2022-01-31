var browser = require( '../' ).createBrowser();

var media = {
    url : 'http://commondatastorage.googleapis.com/gtv-videos-bucket/big_buck_bunny_1080p.mp4',
    subtitles: [{
        language: 'en-US',
        url: 'http://carlosguerrero.com/captions_styled.vtt',
        name: 'English',
    }],
}

console.log('Trying to play Big Buck Bunny. Turn on your AppleTV...');
browser.on( 'deviceOn', function( device ) {
    console.log('AppleTV detected! Starting playback...');
    device.simpleplay(media , 0, function() {
        console.info( 'Success. Video should be playing...' );
    });
});
browser.start();

