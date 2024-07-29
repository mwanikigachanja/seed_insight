function getSeedRecommendations($userLocation) {
    // Fetch weather data for the user's location
    $weatherData = fetchWeatherData($userLocation);

    // Fetch all seeds from the database
    $seeds = fetchAllSeeds();

    // Filter seeds based on weather data
    $recommendedSeeds = [];
    foreach ($seeds as $seed) {
        if ($weatherData['altitude'] >= $seed['altitude_min'] && $weatherData['altitude'] <= $seed['altitude_max']) {
            $recommendedSeeds[] = $seed;
        }
    }

    return $recommendedSeeds;
}

function fetchWeatherData($location) {
    // Call the weather API to get data for the given location
    $apiUrl = "https://api.openweathermap.org/data/2.5/weather?lat={$location['latitude']}&lon={$location['longitude']}&appid=YOUR_API_KEY";
    $response = file_get_contents($apiUrl);
    $data = json_decode($response, true);

    return [
        'altitude' => getAltitude($location),
        'rainfall' => $data['rain']['1h'] ?? 0,
        'humidity' => $data['main']['humidity']
    ];
}

function getAltitude($location) {
    // Call a suitable API to get altitude data based on the location
    $apiUrl = "https://api.example.com/elevation?lat={$location['latitude']}&lon={$location['longitude']}&appid=YOUR_API_KEY";
    $response = file_get_contents($apiUrl);
    $data = json_decode($response, true);

    return $data['altitude'];
}
