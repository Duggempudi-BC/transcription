$(document).ready(function () {
    var recognition;
    var currentTranscript = '';  // Variable to store the current transcript
    var finalTranscript = '';  // Variable to store the final transcript
    var wholeTranscription = '';  // Variable to store the whole conversation transcription

    function startRecording() {
        currentTranscript = '';
        finalTranscript = '';
        recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
        recognition.interimResults = true;
        recognition.maxAlternatives = 1;

        recognition.onstart = function () {
            console.log('Recording started');
        };

        recognition.onresult = function (event) {
            var transcript = event.results[event.results.length - 1][0].transcript;
            currentTranscript = transcript;  // Update the current transcript with the latest words spoken
            $('#transcription').text(currentTranscript);  // Update the live transcription
        };

        recognition.onend = function () {
            console.log('Recording ended');
            finalTranscript += currentTranscript;  // Append the current transcript to the final transcript
            $('#spoken-text').append('<p>' + currentTranscript + '</p>');  // Append the spoken statement as a paragraph

            wholeTranscription += currentTranscript + '\n';  // Append the current transcript to the whole conversation transcription
            $('#whole-transcription').text(wholeTranscription);  // Update the whole conversation transcription

            startRecording();  // Restart the recognition when it ends
        };

        recognition.onerror = function (event) {
            console.error('Recognition error:', event.error);
        };

        recognition.start();
    }

    function stopRecording() {
        recognition.stop();
    }

    $("#record-btn").click(function () {
        if (recognition && recognition.recording) {
            stopRecording();
        } else {
            startRecording();
        }
    });
});