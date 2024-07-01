// Fetch geolocation data from server-side script (replace with your actual API endpoint)
fetch('/api/geolocation')
  .then(response => response.json())
  .then(data => {
    const geolocationElement = document.getElementById('geolocation');

    if (data.status === 'success') {
      geolocationElement.textContent = `Country: ${data.country}`;

      if (data.city) {
        geolocationElement.textContent += `, City: ${data.city}`;
      }
    } else {
      geolocationElement.textContent = 'Geolocation lookup failed.';
    }
  })
  .catch(error => {
    console.error(error);
    geolocationElement.textContent = 'Geolocation lookup failed.';
  });
