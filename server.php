<?php

// Fetch user IP address (replace with your server-side IP retrieval method)
$userIp = $_SERVER['REMOTE_ADDR']; // Example for demonstration only

// Define API endpoint URL with desired fields
$apiUrl = 'http://ip-api.com/json/' . $userIp . '?fields=country,city,lat,lon';

// Make a request to the API (replace with appropriate library for your server-side language)
$response = file_get_contents($apiUrl);

// Parse the JSON response
$data = json_decode($response, true);

// Check for successful response
if (isset($data['status']) && $data['status'] === 'success') {
  $country = $data['country'];
  $city = $data['city'];
  $latitude = $data['lat'];
  $longitude = $data['lon'];
} else {
  // Handle error scenario (e.g., display a message to the user)
  $errorMessage = 'Geolocation lookup failed.';
}

?>
