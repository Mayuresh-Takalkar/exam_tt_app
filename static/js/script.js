document.addEventListener("DOMContentLoaded", function() {

    // -------------------- DARK MODE --------------------
    const darkToggle = document.getElementById("darkModeToggle");
    if(darkToggle){
        darkToggle.addEventListener("click", ()=>{
            document.body.classList.toggle("dark-mode");
        });
    }

    // -------------------- SCREENSHOT --------------------
    const screenshotBtn = document.getElementById("screenshotBtn");
    if(screenshotBtn){
        screenshotBtn.addEventListener("click", ()=>{
            html2canvas(document.body).then(canvas=>{
                const link = document.createElement("a");
                link.download = "screenshot.png";
                link.href = canvas.toDataURL();
                link.click();
            });
        });
    }

    // -------------------- NOTEPAD SAVE / CLEAR --------------------
    const notepad = document.getElementById("notepad");
    const saveBtn = document.getElementById("saveNote");
    const clearBtn = document.getElementById("clearNote");

    if(notepad && saveBtn && clearBtn){
        // Load saved note
        const savedText = localStorage.getItem("userNote");
        if(savedText) notepad.value = savedText;

        // Save note
        saveBtn.addEventListener("click", ()=>{
            localStorage.setItem("userNote", notepad.value);
            alert("Note saved!");
        });

        // Clear note with confirmation
        clearBtn.addEventListener("click", ()=>{
            if(confirm("Are you sure you want to clear your notes?")) {
                notepad.value = "";
                localStorage.removeItem("userNote");
            }
        });
    }

});
