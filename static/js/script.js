const chatBox = document.getElementById("chat-box");
const input = document.getElementById("userInput");

function displayMessage(msg, sender="bot") {
    const div = document.createElement("div");
    div.className = sender;
    div.textContent = msg;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage(message) {
    displayMessage(message, "user");
    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message, user_id: "user123" })
    })
    .then(res => res.json())
    .then(data => displayMessage(data.response))
    .catch(() => displayMessage("Error connecting to server."));
}

input.addEventListener("keydown", function(e) {
    if(e.key === "Enter" && input.value.trim() !== "") {
        sendMessage(input.value);
        input.value = "";
    }
});
