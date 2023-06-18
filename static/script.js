// Add JavaScript/jQuery code to show/hide the waiting message when the button is clicked
  document.getElementById('search-button').addEventListener('click', function() {
    var waitingMessage = document.getElementById('waiting-message');
    // hide the button when the loading button is shown
    let btn = document.getElementById('search-button');
    btn.style.display = 'none';
    // visible the waiting message while the button is clicked on
    waitingMessage.style.display = 'block'; // Show the waiting message


    // Simulate a delay to mimic network request
    setTimeout(function() {
      waitingMessage.style.display = 'none'; // Hide the waiting message
    }, 3000 * 3000 * 3000 * 3000); // 3 seconds delay (adjust as needed)
  });
