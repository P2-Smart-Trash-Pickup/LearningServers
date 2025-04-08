document.addEventListener('DOMContentLoaded', function() {
    const speakButton = document.getElementById('speakButton');
    const text = document.querySelector('.content p').textContent;
    const title = document.querySelector('.content h1').textContent;
    
    // Speech synthesis setup
    const synth = window.speechSynthesis;
    
    speakButton.addEventListener('click', function() {
        // Cancel any ongoing speech
        synth.cancel();
        
        // Create a new utterance for the title
        const titleUtterance = new SpeechSynthesisUtterance(title);
        titleUtterance.lang = 'da-DK'; // Danish language
        
        // Create a new utterance for the paragraph
        const paragraphUtterance = new SpeechSynthesisUtterance(text);
        paragraphUtterance.lang = 'da-DK'; // Danish language
        
        // Speak the title first, then the paragraph
        synth.speak(titleUtterance);
        synth.speak(paragraphUtterance);
        
        // Change button text while speaking
        speakButton.textContent = 'Reading...';
        
        // When finished speaking
        paragraphUtterance.onend = function() {
            speakButton.textContent = 'Read Aloud';
        };
    });
    
    // Add a button to stop speech
    const stopButton = document.createElement('button');
    stopButton.textContent = 'Stop Reading';
    stopButton.style.marginLeft = '10px';
    stopButton.addEventListener('click', function() {
        synth.cancel();
        speakButton.textContent = 'Read Aloud';
    });
    
    speakButton.parentNode.insertBefore(stopButton, speakButton.nextSibling);
});