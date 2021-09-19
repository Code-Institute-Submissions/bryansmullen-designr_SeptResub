// Generate current date
var date = new Date();

// Extract current year
var currentYear = date.getFullYear();

// Inject current year into #year element
document.getElementById('year').innerHTML = currentYear;