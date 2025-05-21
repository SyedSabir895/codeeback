require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const bodyParser = require("body-parser");
const userRoutes = require("./routes/userRoutes");

const app = express();

// Middleware
app.use(cors({ origin: "https://codee-git-main-syed-chotus-projects.vercel.app/", credentials: true }));
app.use(express.json()); // Preferred over bodyParser.json()
app.use(bodyParser.urlencoded({ extended: true }));

// Routes
app.use("/api/auth", userRoutes);

// ✅ New route added here
app.get("/api/data", (req, res) => {
  res.json({ message: "This is sample data from the server." });
});

// Connect to MongoDB
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("✅ MongoDB connected"))
  .catch((error) => {
    console.error("❌ MongoDB connection error:", error);
    process.exit(1); // Exit the process if DB fails
  });

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));
