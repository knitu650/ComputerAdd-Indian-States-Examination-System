const express = require('express');
const router = express.Router();
const profileController = require('../controllers/profile.controller');
const { authMiddleware } = require('../middleware/auth.middleware');

router.use(authMiddleware);

router.get('/', profileController.getProfile.bind(profileController));
router.put('/', profileController.updateProfile.bind(profileController));
router.post('/avatar', profileController.uploadAvatar.bind(profileController));

module.exports = router;
