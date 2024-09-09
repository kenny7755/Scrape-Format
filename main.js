eel.expose(testFunction)

function testFunction() {
    const fileInput = document.getElementById('userinput');
    fileInput.onchange = () => {
      const selectedFile = fileInput.files[0];
      console.log(selectedFile);
    }
        document.getElementById("resultplace").innerHTML = response;
}