window.onload = () => {
    document.getElementById('send-button').addEventListener('click', sendFunction);
}

const url = 'http://localhost:5000';
const endpoint = 'api';
const sendFunction = async () => {
    const messageInput = document.getElementById('message-input');
    const imageUpload = document.getElementById('image-upload');
    const chatbox = document.getElementById('chatbox');

    if (imageUpload.files.length > 0) {
        const reader = new FileReader();
        reader.onloadend = function() {
            let base64data = reader.result;

            // If an image was uploaded, add it to the chatbox
            if (base64data) {
                const image = document.createElement('img');
                image.src = base64data;
                image.style.maxHeight = '300px';
                image.style.maxWidth = '300px';
                chatbox.appendChild(image);
            } else {
                console.error("NULL base 64 data");
            }

            // Add the message to the chatbox
            const messageDiv = document.createElement('div');
            messageDiv.textContent = '👤 ' + messageInput.value;
            chatbox.appendChild(messageDiv);

            // Clear the input and file upload
            messageInput.value = '';
            imageUpload.value = '';

            // Scroll to the bottom of the chatbox
            chatbox.scrollTop = chatbox.scrollHeight;

            // Prepare the data to be sent
            const data = {
                message: messageDiv.textContent,
                image: base64data,
            };

            const pendingDiv = document.createElement('div');
            pendingDiv.textContent = '🤖 pending';
            chatbox.appendChild(pendingDiv);

            // Use Fetch API to send the data
            fetch(`${url}/${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(response => {
                chatbox.removeChild(pendingDiv);

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(responseData => {
                console.log("RESPONSE: "+responseData);
                const robotMessageDiv = document.createElement('div');
                robotMessageDiv.textContent = '🤖 ' + responseData.txtMessage;
                chatbox.appendChild(robotMessageDiv);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation: ', error);
                chatbox.removeChild(pendingDiv);
            });
        };
        reader.readAsDataURL(imageUpload.files[0]);
    }
}