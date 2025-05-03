document.getElementById('symptomForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent the form from submitting normally

    // Show loading spinner
    document.getElementById('loading').style.display = 'block';

    // Get the symptoms entered by the user
    var symptoms = document.getElementById('symptoms').value;

    // Send an AJAX request to the server to get the diagnosis
    fetch('/diagnose', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symptoms: symptoms })
    })
    .then(response => response.json())
    .then(data => {
        // Hide loading spinner
        document.getElementById('loading').style.display = 'none';

        // Show the diagnosis result
        document.getElementById('result').innerHTML = `<h2>Diagnosis Result: ${data.result}</h2>`;
    })
    .catch(error => {
        // Hide loading spinner in case of error
        document.getElementById('loading').style.display = 'none';
        document.getElementById('result').innerHTML = '<h2>Sorry, something went wrong!</h2>';
    });
});
