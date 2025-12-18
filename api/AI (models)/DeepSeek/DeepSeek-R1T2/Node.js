import fetch from "node-fetch";

const text = "What is your name?";
const url = `https://deepseek.api-sina-free.workers.dev/?text=${encodeURIComponent(text)}`;

fetch(url)
  .then(res => res.json())
  .then(data => {
    console.log("🧠 Answer:", data.answer);
    console.log("👤 Creator:", data.creator);
    console.log("📡 Channel:", data.channel);
  })
  .catch(err => {
    console.error("❌ Error:", err);
  });
