const API = "https://football.api-sina-free.workers.dev/news";

async function getNews() {
  const res = await fetch(API);
  const data = await res.json();
  console.log(data.data);
}

getNews();
