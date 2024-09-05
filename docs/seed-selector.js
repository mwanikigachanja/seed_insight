const seedData = {
    'Lowland Altitude': [
        { crop: 'Maize',variety: 'PH 1', maturity: '75-100', rate: '10', yield: '20', attributes: 'Early maturity, Heat tolerant, Drought resistant' },
        { crop:'Maize',variety: 'PH 4', maturity: '100-120', rate: '10', yield: '26', attributes: 'Heat tolerant, Very sweet tasting' },
        { crop: 'Maize', variety: 'DH08', maturity: '100-120', rate: '10', yield: '26', attributes: 'Short drought tolerance, Good husk cover and stand-ability.' },
        { crop: 'Maize', variety: 'DH04', maturity: '75-100', rate: '10', yield: '24', attributes: 'Semi-dent, Good stand ability, Tolerant to ear rots' },
        { crop: 'Sorghum', variety: 'Gadam', maturity: '90', rate: '10', yield: '8', attributes: 'Whitish in color, Tolerant to Stem borers, Shoot fly and Foliar diseases, Excellent malting qualities' },
        { crop: 'Finger Millet', variety: 'P224', maturity: '90-120', rate: '10', yield: '12', attributes: 'Soft and excellent herbage, Drought tolerant, Fairly tolerant to Striga, Rust, Leaf blight, and Grey leaf spot' },
        { crop: 'Beans', variety: 'GLP 1127 (New Mwezi Moja)', maturity: '75-90', rate: '30', yield: '8', attributes: 'Large beige or light brown speckled purple with long broad pods, Medium yielder, Performs best in warmer areas' },
    ],
    'Highland Altitude': [
        { crop: 'Maize', variety: 'H614D', maturity: '160-210', rate: '10', yield: '38', attributes: 'Sweet tasting, Good density, Long storage period, Resistant to GLS and Blight' },
        { crop: 'Maize', variety: 'H629', maturity: '150-210', rate: '10', yield: '48', attributes: 'Resistant to lodging, Good husk cover, Good storage quality, Resistant to GLS and ear rot' },
        { crop: 'Maize', variety: 'H6213', maturity: '160-210', rate: '10', yield: '54', attributes: 'High-yielder, Excellent milling qualities, Resistant to lodging, ear rot, rust, GLS, stem and leaf blight' },
        { crop: 'Wheat', variety: 'KS Simba', maturity: '100-120', rate: '50', yield: '18-22', attributes: 'Hard red wheat, Good baking qualities, Moderate resistance to stem rust, High yielding' },
        { crop: 'Sorghum', variety: 'E 1291', maturity: '150-160', rate: '15-20', yield: '22-25', attributes: 'Dual-purpose variety for human and silage consumption, Performs well in high altitude areas' },
        { crop: 'Beans', variety: 'GLP 2 (Rosecoco)', maturity: '75-90', rate: '30', yield: '10', attributes: 'Large beige or light brown speckled purple with long broad pods, Medium yielder, Performs best in warmer areas' },
    ],
    'Dryland Altitude': [
        { crop: 'Maize', variety: 'DH08', maturity: '100-120', rate: '10', yield: '26', attributes: 'Short drought tolerance, Good husk cover and stand-ability.' },
        { crop: 'Maize', variety: 'DH04', maturity: '75-100', rate: '10', yield: '24', attributes: 'Semi-dent, Good stand ability, Tolerant to ear rots' },
        { crop: 'Maize',variety: 'PH 1', maturity: '75-100', rate: '10', yield: '20', attributes: 'Early maturity, Heat tolerant, Drought resistant' },
        { crop:'Maize',variety: 'PH 4', maturity: '100-120', rate: '10', yield: '26', attributes: 'Heat tolerant, Very sweet tasting' },
        { crop: 'Finger Millet', variety: 'Katumani', maturity: '75-85', rate: '10', yield: '7-10', attributes: 'Red seeded variety, Short variety, Drought tolerant' },
        { crop: 'Cowpeas', variety: 'Ken Kunde 1 (KK1)', maturity: '75-90', rate: '20', yield: '6', attributes: 'Dual purpose, Drought tolerant, Performs well in a wide variety of soils' },
        { crop: 'Beans', variety: 'GLP 1127 (New Mwezi Moja)', maturity: '75-90', rate: '30', yield: '8', attributes: 'Large beige or light brown speckled purple with long broad pods, Medium yielder, Performs best in warmer areas' },
    ],
    'Medium Altitude': [
        { crop: 'Maize', variety: 'H513', maturity: '110-130', rate: '10', yield: '26', attributes: 'Very sweet tasting, Good stand ability' },
        { crop: 'Maize', variety: 'H516', maturity: '120-150', rate: '10', yield: '30', attributes: 'Very sweet tasting, Resistant to blight, rust, and lodging' },
        { crop: 'Maize', variety: 'H517', maturity: '120-150', rate: '10', yield: '32', attributes: 'Tolerant to foliar diseases and pests, Better husk cover, Tolerant to cob rot and MSV, Ideal for irrigation' },
        { crop: 'Beans', variety: 'GLP 2 (Rosecoco)', maturity: '75-90', rate: '25', yield: '10', attributes: 'Shiny dark purple or reddish purple seeds, Vigorous plant with slight climbing tendency and flat pods, Performs best in cool areas' },
        { crop: 'Pasture Grass', variety: 'Elmba Rhodes', maturity: '120', rate: '4', yield: '12', attributes: 'High seeding vigor and forage yield, Suited for a wide range of climatic conditions, Does best in light sandy soils, Quick growing, Suited to intensive grazing' },
        { crop: 'Beans', variety: 'GLP 1127 (New Mwezi Moja)', maturity: '75-90', rate: '30', yield: '8', attributes: 'Large beige or light brown speckled purple with long broad pods, Medium yielder, Performs best in warmer areas' },
    ],
    'Transitional Altitude': [
        { crop: 'Maize', variety: 'H520', maturity: '120-150', rate: '10', yield: '34', attributes: 'Double cobbing variety, Very sweet tasting, GLS and MSV tolerant' },
        { crop: 'Maize', variety: 'H624', maturity: '120-150', rate: '10', yield: '36', attributes: 'Double cobbing variety, Very sweet tasting' },
        { crop: 'Beans', variety: 'Wairimu Dwarf', maturity: '75-85', rate: '25', yield: '8', attributes: 'Cream seeds with black-brown spots, Tolerant to halo blight, Prefers medium altitude and is tolerant to drought' },
        { crop: 'Finger Millet', variety: 'P 224', maturity: '75-90', rate: '10', yield: '10-15', attributes: 'Brown seeded variety, Tall type with uniform plant height, Tolerant to lodging and blast' },
        { crop: 'Wheat', variety: 'KS Farasi', maturity: '119 (+/-5)', rate: '50', yield: '17 bags', attributes: 'Tolerant to most foliar diseases, Highly vigorous in growth, Good baking quality' },
        { crop: 'Beans', variety: 'GLP 1127 (New Mwezi Moja)', maturity: '75-90', rate: '30', yield: '8', attributes: 'Large beige or light brown speckled purple with long broad pods, Medium yielder, Performs best in warmer areas' },
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
