const text = "வருக அண்ணா, உங்கள் நாள் எப்படி போகிறது?";
const typingTextElement = document.getElementById("typingText");
let index = 0;
const cursor = document.createElement('span');
cursor.className = 'cursor';
document.querySelector('.typing-container').appendChild(cursor);

function type() {
  if (index < text.length) {
    typingTextElement.textContent += text.charAt(index);
    index++;
    cursor.style.left = `${typingTextElement.offsetWidth}px`; // Move cursor with text
    setTimeout(type, 100); // Adjust the typing speed here
  } else {
    cursor.style.display = 'none'; // Hide cursor after typing is done
  }
}

// Start typing
type();