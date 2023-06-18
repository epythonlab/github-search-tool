document.querySelector('.search-button').addEventListener('click', function() {
  var topicSelect = document.getElementById('topic-select');
  var ratingSelect = document.getElementById('rating-select');

  var selectedTopic = topicSelect.value;
  var selectedRating = ratingSelect.value;

  // Perform the search based on the selected values
  // Add your search logic here

  console.log("Selected Topic:", selectedTopic);
  console.log("Selected Rating:", selectedRating);
});

function toggleDropdown() {
  var dropdownContent = document.getElementById("topic-dropdown");
  dropdownContent.style.display = "block";
}


$(document).ready(function() {
  $('#search-button').click(function() {
    var $progressContainer = $('#progress-container');
    $progressContainer.toggleClass('show');

    // Simulating a delay of 3 seconds for demonstration purposes
    setTimeout(function() {
      $progressContainer.removeClass('show');
    }, 3000);
  });
});
