const { Crop, Ecozone } = require('../models');

// Fetch crops by ecozone
exports.getCropsByEcozone = async (req, res) => {
    try {
        const ecozone = await Ecozone.findOne({ where: { name: req.params.ecozone } });
        if (!ecozone) {
            return res.status(404).json({ message: 'Ecozone not found' });
        }

        const crops = await Crop.findAll({ where: { ecozone_id: ecozone.id } });
        res.json(crops);
    } catch (error) {
        res.status(500).json({ message: 'Server error' });
    }
};
