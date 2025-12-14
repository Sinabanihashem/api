import fetch from "node-fetch";
import fs from "fs";

const url = "https://photo-text.api-sina-free.workers.dev/Hello";

fetch(url)
  .then(res => res.arrayBuffer())
  .then(buf => fs.writeFileSync("hello.png", Buffer.from(buf)))
  .then(() => console.log("🖼 Image saved!"));
