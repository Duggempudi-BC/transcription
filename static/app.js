$(document).ready(function() {
    $("#transcribe-button").click(function() {
        if ($(this).text() === "Start Transcribing") {
            $.get('/start_transcription', function(response) {
                if (response === 'success') {
                    $("#transcribe-button").text("Stop Transcribing");
                }
            });
        } else {
            $.get('/stop_transcription', function(response) {
                if (response === 'success') {
                    $("#transcribe-button").text("Start Transcribing");
                }
            });
        }
    });

    setInterval(function() {
        $.get('/transcription_data', function(data) {
            var newLines = data.split("\n");

            // Update the transcription list with new lines
            var transcriptionDiv = document.getElementById("transcription-div");

            // Clear the current content
            transcriptionDiv.innerHTML = "";

            // Add new lines to the div
            for (var i = 0; i < newLines.length; i++) {
                var newLine = newLines[i];
                var newParagraph = document.createElement("p");
                newParagraph.textContent = newLine;
                transcriptionDiv.appendChild(newParagraph);
            }
        });
    }, 1000); // Fetch transcription data every 1 second
});