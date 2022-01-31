var util = require( 'util' );
var events = require('events');
var http = require('http');

var Device = function(options){
    events.EventEmitter.call(this);
    var self = this;
    self.config = options;
    this.init();
};

var jsonRpcQuery = function(host, port, method, callback) {
    var params = method;
    var paramsString = JSON.stringify(params);

    var headers = {
        'Content-Type': 'application/json',
        'Content-Length': paramsString.length
    };

    var options = {
        host: host,
        port: port,
        path: '/jsonrpc',
        method: 'POST',
        headers: headers
    };
    var req = http.request(options, function(res) {
        res.setEncoding('utf-8');
        var response = '';
        res.on('data', function(data) {
            response += data;
        });
        res.on('end', function() {
            var result;
            try {
                result = JSON.parse(response);
            } catch (err) {
                callback({status: 'error'});
            }
            if( !('result' in result) && result.result !== 'ok' ) {
                callback({status: 'error'});
            }
            else {
                callback({status: 'success'});
            }
        });
    });

    req.on('error', function(e) {
        callback({status: 'error'});
    });

    req.write(paramsString);
    req.end();
};

exports.Device = Device;
util.inherits( Device, events.EventEmitter );

Device.prototype.init = function(){
    var self = this;
    self.host = self.config.addresses[0];
    self.port = self.config.port;
    self.name = self.config.name;
    self.playing = false;
};

Device.prototype.play = function(resource, callback){
    var self = this;
    var method = {"jsonrpc": "2.0","id": "1","method": "Player.Open","params": {"item": {"file": resource}}};

    jsonRpcQuery(self.host, self.port, method, function(result) {
        if( result.status !== 'error' ) {
            self.playing = true;
            if(callback){
                callback(result.status);
            }
        }
    });
};

Device.prototype.input = function(resource, callback){
    var self = this;
    var method = {"jsonrpc": "2.0","id": "1","method": resource};

    jsonRpcQuery(self.host, self.port, method, function(result) {
        if( result.status !== 'error' ) {
            if(callback){
                callback(result.status);
            }
        }
    });
};

Device.prototype.player = function(resource, callback){
    var self = this;
    var method = {"jsonrpc": "2.0", "method": resource, "params": { "playerid": 0 }, "id": 1};

    jsonRpcQuery(self.host, self.port, method, function(result) {
        if( result.status !== 'error' ) {
            if(callback){
                callback(result.status);
            }
        }
    });
};