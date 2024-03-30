const WebSocket = require('ws');
const fs = require('fs');

class APIObject {
    constructor(messageType, jsonData) {
        this.messageType = messageType;
        this.json = jsonData;
    }
}

function sendAPIObject(messageType, jsonData) {
    const jsonString = JSON.stringify(jsonData);
    const apiObject = new APIObject(messageType, jsonString);
    const jsonMessage = JSON.stringify(apiObject);
    const socket = new WebSocket('ws://127.0.0.1:11450/api');

    socket.on('open', function (event) {
        socket.send(jsonMessage);
    });

    socket.on('message', function (data) {
        console.log('Message from server:', data);
    });

    socket.on('error', function (error) {
        console.error('WebSocket error:', error);
    });

    socket.on('close', function () {
        console.log('WebSocket connection closed');
    });
}

const iconPath = './logo.png';
const pngByteArray = fs.readFileSync(iconPath);

const messageType = 'SendNotification';
const jsonData = {
    title: 'Cool title',
    body: 'My cool body text!',
    icon: [...pngByteArray]
};

sendAPIObject(messageType, jsonData);
