document.getElementById("fileInput").addEventListener("change", handleFileSelect);
document.getElementById("convertButton").addEventListener("click", convertFilesToPDF);

let filesToUpload = [];

function handleFileSelect(event) {
    filesToUpload = Array.from(event.target.files);
    displayFiles();
}

function displayFiles() {
    const fileListContainer = document.getElementById("fileList");
    fileListContainer.innerHTML = '<ul>' + filesToUpload.map(file => `<li>${file.name}</li>`).join('') + '</ul>';
}

function convertFilesToPDF() {
    const formData = new FormData();
    filesToUpload.forEach(file => formData.append("files", file));

    fetch("/convert-to-pdf", {
        method: "POST",
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = "converted_files.pdf";
        link.click();
    })
    .catch(error => alert("An error occurred during conversion"));
}
