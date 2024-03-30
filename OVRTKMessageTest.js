const WebSocket = require('ws');

class APIObject {
    constructor(messageType, json) {
        this.messageType = messageType;
        this.json = json;
    }
}

function sendAPIObject(messageType, jsonData) {
    const apiObject = new APIObject(messageType, jsonData);
    const jsonMessage = JSON.stringify(apiObject);
    const socket = new WebSocket('ws://127.0.0.1:11450/api');

    socket.on('open', function (event) {
        console.log('WebSocket connected');
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

const messageType = 'SendNotification';
const jsonData = {
    title: 'Test Title',
    body: 'my balls itch',
    icon: null
};

const jsonString = JSON.stringify(jsonData);

sendAPIObject(messageType, jsonString);
