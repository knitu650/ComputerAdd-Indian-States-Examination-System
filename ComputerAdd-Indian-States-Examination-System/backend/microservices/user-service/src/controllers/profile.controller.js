const User = require('../models/User');

class ProfileController {
  async getProfile(req, res) {
    try {
      const user = await User.findById(req.user.id);
      if (!user) {
        return res.status(404).json({ success: false, message: 'User not found' });
      }
      res.json({ success: true, data: user });
    } catch (error) {
      res.status(500).json({ success: false, message: error.message });
    }
  }

  async updateProfile(req, res) {
    try {
      const user = await User.findByIdAndUpdate(
        req.user.id,
        { $set: { profile: req.body } },
        { new: true, runValidators: true }
      );
      res.json({ success: true, data: user });
    } catch (error) {
      res.status(500).json({ success: false, message: error.message });
    }
  }

  async uploadAvatar(req, res) {
    try {
      const avatarUrl = req.file.path; // Assuming multer middleware
      const user = await User.findByIdAndUpdate(
        req.user.id,
        { 'profile.avatar': avatarUrl },
        { new: true }
      );
      res.json({ success: true, data: { avatar: user.profile.avatar } });
    } catch (error) {
      res.status(500).json({ success: false, message: error.message });
    }
  }
}

module.exports = new ProfileController();
