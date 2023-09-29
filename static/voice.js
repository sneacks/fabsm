var startBtn = document.getElementById('start-btn');
var audioPlayer = document.getElementById('audio-player');
var mediaRecorder;
var chunks = [];
var checked = 0;

// При нажатии на кнопку "Start"
startBtn.addEventListener('click', function() {
    if (checked == 0) {
        startBtn.addEventListener('click', function() {
            chunks = [];
            checked = 1;
            navigator.mediaDevices.getUserMedia({audio: true})
            .then(function(stream) {
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.start();
                mediaRecorder.addEventListener('dataavailable', function(event) {
                    chunks.push(event.data);
                });
            });
        });
    } else {
        startBtn.addEventListener('click', function() {
        mediaRecorder.stop();
        mediaRecorder.addEventListener('stop', function() {
            var audioBlob = new Blob(chunks, { type: 'audio/wav' });
            var form_data = new FormData();
            checked = 0;
            form_data.append('audio_data', audioBlob);
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/upload');
            xhr.onload = function(event) {
                if (xhr.status == 200) {
                    console.log(xhr.responseText);
                    audioPlayer.style.display = 'block';
                    audioPlayer.getElementsByTagName('source')[0].setAttribute('src', xhr.responseText);
                    audioPlayer.getElementsByTagName('audio')[0].load();
                } else {
                    console.log('Error:', xhr.responseText);
                }
            };
            xhr.send(form_data);
        });
    });
    }
}
// При нажатии на кнопку "Stop"
stopBtn.addEventListener('click', function() {
    startBtn.disabled = false;
    stopBtn.disabled = true;
    mediaRecorder.stop();
    mediaRecorder.addEventListener('stop', function() {
        var audioBlob = new Blob(chunks, { type: 'audio/wav' });
        var form_data = new FormData();
        form_data.append('audio_data', audioBlob);
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/upload');
        xhr.onload = function(event) {
            if (xhr.status == 200) {
                console.log(xhr.responseText);
                audioPlayer.style.display = 'block';
                audioPlayer.getElementsByTagName('source')[0].setAttribute('src', xhr.responseText);
                audioPlayer.getElementsByTagName('audio')[0].load();
            } else {
                console.log('Error:', xhr.responseText);
            }
        };
        xhr.send(form_data);
    });
});