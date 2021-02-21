// Generate current date
const date = new Date();

// Extract current year
const currentYear = date.getFullYear()

// Inject current year into #year element
document.getElementById('year').innerHTML = currentYear