function playSong(songUrl) {
    var audioPlayer = document.getElementById('audio-player');
    var audioSource = document.getElementById('audio-source');
    audioSource.src = songUrl;
    audioPlayer.load();
    audioPlayer.play();
}