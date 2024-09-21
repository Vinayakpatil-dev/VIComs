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
        cursor.style.left = `${typingTextElement.offsetWidth}px`;
        setTimeout(type, 100);
    } else {
        cursor.style.display = 'none';
    }
}

type();

document.getElementById('delete-selected').addEventListener('click', function() {
    var checkboxes = document.querySelectorAll('.room-checkbox');
    let selectedCount = 0;

    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            selectedCount++;
        }
    });

    if (selectedCount > 0 && confirm(`Are you sure you want to delete ${selectedCount} selected room(s)?`)) {
        for (let i = checkboxes.length - 1; i >= 0; i--) {
            if (checkboxes[i].checked) {
                checkboxes[i].closest('tr').remove();
            }
        }
    }
});
