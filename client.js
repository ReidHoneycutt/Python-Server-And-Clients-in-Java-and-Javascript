const socket = new WebSocket("ws://127.0.0.1:8080");

socket.addEventListener('open', function (event) {
    console.log("Connected");
});

socket.addEventListener('message', function (event) {
    if (event.data instanceof Blob) {
        // If the data is a Blob (binary data), read it as text
        const reader = new FileReader();
        reader.onload = function() {
            console.log("Message from server: ", reader.result);
        };
        reader.readAsText(event.data);
    } else {
        // If the data is not a Blob, log it directly
        console.log("Message from server: ", event.data);
    }
});
