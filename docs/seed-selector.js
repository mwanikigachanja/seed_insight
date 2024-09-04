const seedData = {
    'Lowland Altitude': [
        { crop: 'Maize',variety: 'PH 1', maturity: '75-100', rate: '10', yield: '20', attributes: 'Early maturity, Heat tolerant, Drought resistant' },
        { crop:'Maize',variety: 'PH 4', maturity: '100-120', rate: '10', yield: '26', attributes: 'Heat tolerant, Very sweet tasting' },
        { crop: 'Maize', variety: 'DH08', maturity: '100-120', rate: '10', yield: '26', attributes: 'Short drought tolerance, Good husk cover and stand-ability.' },
        { crop: 'Maize', variety: 'DH04', maturity: '75-100', rate: '10', yield: '24', attributes: 'Semi-dent, Good stand ability, Tolerant to ear rots' },
        
    ],
    'Highland Altitude': [
        { crop: 'Maize', variety: 'H6213', maturity: '150-210', rate: '10', yield: '52', attributes: 'High-yielder, Excellent milling qualities, Resistant to lodging, ear rot, rust, G.L.S,stem and leaf blight.' },
        { crop: 'Maize', variety: 'H629', maturity: '150-210', rate: '10', yield: '48', attributes: 'Sweet tasting variety, Has good density, Has long storage period, Resistant to GLS and Blight' },
        { crop: 'Maize', variety: 'H614D', maturity: '150-210', rate: '10', yield: '38', attributes: 'Resistant to lodging, Has good husk cover, Good storage quality, Resistant to GLS and ear rot.' },
        
        
    ],
    'Dryland Altitude': [
        { crop: 'Maize', variety: 'DH08', maturity: '100-120', rate: '10', yield: '26', attributes: 'Short drought tolerance, Good husk cover and stand-ability.' },
        { crop: 'Maize', variety: 'DH04', maturity: '75-100', rate: '10', yield: '24', attributes: 'Semi-dent, Good stand ability, Tolerant to ear rots' },
        { crop: 'Maize',variety: 'PH 1', maturity: '75-100', rate: '10', yield: '20', attributes: 'Early maturity, Heat tolerant, Drought resistant' },
        { crop:'Maize',variety: 'PH 4', maturity: '100-120', rate: '10', yield: '26', attributes: 'Heat tolerant, Very sweet tasting' },
        
    ],
    'Medium Altitude': [
        { crop: 'Maize', variety: 'H513', maturity: '110-130', rate: '10', yield: '26', attributes: 'Sweet tasting variety, Has good density, Has long storage period, Resistant to GLS and Blight' },
        { crop: 'Maize', variety: 'H516', maturity: '120-150', rate: '10', yield: '30', attributes: 'High-yielder, Excellent milling qualities, Resistant to lodging, ear rot, rust, G.L.S,stem and leaf blight.' },
        { crop: 'Maize', variety: 'H517', maturity: '120-150', rate: '10', yield: '30', attributes: 'Tolerant to foliar diseases and pests, Has better husk cover, tolerant to cob rot and, MSV, Ideal for irrigation' },
    ],
    'Transitional Altitude': [
        { crop: 'Maize', variety: 'H520', maturity: '150-210', rate: '10', yield: '34', attributes: 'Resistant to lodging, Has good husk cover, Good storage quality, Resistant to GLS and ear rot.' },
        { crop: 'Maize', variety: 'H624', maturity: '150-210', rate: '10', yield: '36', attributes: 'High-yielder, Excellent milling qualities, Resistant to lodging, ear rot, rust, G.L.S,stem and leaf blight.' },
    ],
    // Add more ecozones and seed recommendations here
};

document.addEventListener("DOMContentLoaded", function() {
    async function fetchWeather(location = 'Kitale') {
        const apiKey = 'e57fe133456b8c6ab739fbc3900619d0'; // Replace with your actual API key
        const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=metric`);
        const data = await response.json();

        const lat = data.coord.lat;
        const lon = data.coord.lon;
        const altResponse = await fetch(`https://api.open-meteo.com/v1/elevation?latitude=${lat}&longitude=${lon}`);
        const altData = await altResponse.json();
        const elevation = altData.elevation;

        // Determine altitude zone
        let altitudeZone = 'Unknown Altitude';
        if (elevation < 500) {
            altitudeZone = 'Lowland Altitude';
        } else if (elevation >= 500 && elevation < 1400) {
            altitudeZone = 'Dryland Altitude';
        } else if (elevation >= 1401 && elevation < 1500) {
            altitudeZone = 'Medium Altitude';
        } else if (elevation >= 1501 && elevation < 1800) {
            altitudeZone = 'Transitional Altitude';
        } else if (elevation >= 1801 && elevation < 2800) {
            altitudeZone = 'Highland Altitude';
        } else if (elevation >= 2801) {
            altitudeZone = 'Very High Altitude';
        }

        // Display weather and location information
        document.getElementById('weather-location').textContent = `Location: ${location}`;
        document.getElementById('weather-zone').textContent = `Altitude Zone: ${altitudeZone}`;
        document.getElementById('weather-temperature').textContent = `Temperature: ${data.main.temp} °C`;
        document.getElementById('weather-description').textContent = `Weather: ${data.weather[0].description}`;
        document.getElementById('weather-humidity').textContent = `Humidity: ${data.main.humidity}%`;
        document.getElementById('weather-maxtemp').textContent = `Max Temp: ${data.main.temp_max} °C`;
        document.getElementById('weather-mintemp').textContent = `Min Temp: ${data.main.temp_min} °C`;
        document.getElementById('weather-wind').textContent = `Wind Speed: ${data.wind.speed} m/s`;
        document.getElementById('weather-clouds').textContent = `Cloudiness: ${data.clouds.all}%`;
        document.getElementById('weather-lat').textContent = `Latitude: ${lat}`;
        document.getElementById('weather-long').textContent = `Longitude: ${lon}`;
        document.getElementById('weather-alt').textContent = `Elevation: ${elevation}`;

        displaySeedRecommendations(altitudeZone);
    }

    function displaySeedRecommendations(altitudeZone) {
        const seedTable = document.getElementById('seed-table');
        const seedBody = document.getElementById('seed-body');
        seedBody.innerHTML = '';

        const recommendations = seedData[altitudeZone];
        if (recommendations && recommendations.length > 0) {
            seedTable.style.display = '';
            recommendations.forEach(seed => {
                const row = document.createElement('tr');
                row.innerHTML = `<td>${seed.crop}</td><td>${seed.variety}</td><td>${seed.maturity}</td><td>${seed.rate}</td><td>${seed.yield}</td><td>${seed.attributes}</td>`;
                seedBody.appendChild(row);
            });
        } else {
            seedTable.style.display = 'none';
        }
    }

    fetchWeather();

    document.getElementById('locationForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const locationInput = document.getElementById('location-input').value;
        if (locationInput) {
            fetchWeather(locationInput);
        }
    });
});
