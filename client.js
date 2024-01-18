const socket = new WebSocket("ws://127.0.0.1");

socket.addEventListener('open', function (event) {
  console.log("connected");
});

socket.addEventListener('message', function (event) {
  if (event.data instanceof Blob) {
    // if the data is a Blob (binary data), read it as text
    const reader = new FileReader();
    reader.onload = function() {
      console.log("Message from Server: ", reader.result);
    };
    reader.readAsText(event.data);
  } else {
    // if the data is not a Blob, log it directly
    console.log("Message from server: ", event.data);
  }
});
