// SENDING A POST REQUEST TO FLASK
var xhr = new XMLHttpRequest();
var form = document.getElementById('the-form');

form.onsubmit = function() {
  var formData = new FormData(form);
  formData.append('file', file);

  // xhr.open('POST', form.getAttribute('action'), true);
  xhr.open('POST', "http://127.0.0.1:5000/post", true);
  xhr.send(formData);

};


// TOGGLE BUTTON FOR IMAGE PLOT

// Show an element
var show = function (elem) {
	elem.classList.add('is-visible');
};

// Hide an element
var hide = function (elem) {
	elem.classList.remove('is-visible');
};

// Toggle element visibility
var toggle = function (elem) {
	elem.classList.toggle('is-visible');
};

// Listen for click events
document.addEventListener('click', function (event) {

	// Make sure clicked element is our toggle
	if (!event.target.classList.contains('toggle')) return;

	// Prevent default link behavior
	event.preventDefault();

	// Get the content
	var content = document.querySelector(event.target.hash);
	if (!content) return;

	// Toggle the content
	toggle(content);

}, false);
