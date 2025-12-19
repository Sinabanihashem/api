const API = "https://currency.api-sina-free.workers.dev/";

async function fetchCrypto(symbol) {
  try {
    const res = await fetch(`${API}?crypto=${symbol}`);
    const data = await res.json();

    if (data.activ !== 1) {
      console.log("Service inactive");
      return;
    }

    const coin = data.list[0];

    console.log("Name:", coin.name);
    console.log("Symbol:", coin.iso);
    console.log("USD:", coin.price);
    console.log("IRR:", coin.price_rial);
    console.log("Market Cap:", coin.market_cap);
    console.log("Change:", coin.daily_change_percent);
    console.log("Logo:", coin.logo);
    console.log("Updated:", data.time);

  } catch (err) {
    console.error("Network Error:", err);
  }
}

fetchCrypto("eth");
