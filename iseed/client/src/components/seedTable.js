import React from 'react';

function SeedTable({ crops }) {
    return (
        <table>
            <thead>
                <tr>
                    <th>Crop</th>
                    <th>Variety</th>
                    <th>Maturity Period (days)</th>
                    <th>Seed Rate (kg/acre)</th>
                    <th>Yield (bags/acre)</th>
                    <th>Attributes</th>
                </tr>
            </thead>
            <tbody>
                {crops.map(crop => (
                    <tr key={crop.id}>
                        <td>{crop.name}</td>
                        <td>{crop.variety}</td>
                        <td>{crop.maturity_period}</td>
                        <td>{crop.seed_rate_per_acre}</td>
                        <td>{crop.yield_per_acre}</td>
                        <td>{crop.attributes}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
}

export default SeedTable;
