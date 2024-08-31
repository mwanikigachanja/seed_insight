import React, { useState, useEffect } from 'react';
import axios from 'axios';
import SeedTable from './components/SeedTable';

function App() {
    const [location, setLocation] = useState('Kitale');
    const [crops, setCrops] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(`http://localhost:5000/api/crops/${location}`);
                setCrops(response.data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, [location]);

    const handleLocationChange = (event) => {
        setLocation(event.target.value);
    };

    return (
        <div>
            <h1>SeedInsight - Crop Recommendations</h1>
            <input type="text" value={location} onChange={handleLocationChange} placeholder="Enter location..." />
            <SeedTable crops={crops} />
        </div>
    );
}

export default App;
