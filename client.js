const socket = new WebSocket("ws://127.0.0.1:8080");

socket.addEventListener('open', function (event) {
  console.log("connected");
});

socket.addEventListener('message', function (event) {
  console.log("Message from server: ", event.data);
});
