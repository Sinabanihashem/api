import fetch from "node-fetch";

const API_URL = "https://gemini.api-sina-free.workers.dev/";
const text = "What is artificial intelligence?";

fetch(`${API_URL}?text=${encodeURIComponent(text)}`)
  .then(res => res.json())
  .then(data => {
    console.log("🤖 Gemini Answer:", data.answer);
    console.log("👤 Creator:", data.creator);
    console.log("📡 Channel:", data.channel);
  })
  .catch(err => {
    console.error("❌ API Error:", err);
  });
