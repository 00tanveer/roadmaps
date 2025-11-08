// src/api/getEpisode.ts
import axios from "axios";

const PODCAST_INDEX_API = "https://api.podcastindex.org/api/1.0";
const API_KEY = "ZTVKK68Z44PLBQKXTHRW";
const API_SECRET = "aSUPDdSknCpZkhy$eDLyrzZZJ68hteXXbf^h7syW";

// ---- HELPER: SHA1 HASH FUNCTION ----
async function sha1(message: string): Promise<string> {
  const encoder = new TextEncoder();
  const data = encoder.encode(message);
  const hashBuffer = await crypto.subtle.digest("SHA-1", data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
  return hashHex;
}
const apiHeaderTime = Math.floor(Date.now() / 1000);
const dataToHash = API_KEY + API_SECRET + apiHeaderTime;
const hash4Header = await sha1(dataToHash);

const headers = {
    "User-Agent": "StoriesPodPlayer/1.0",
    Authorization: hash4Header,
    "X-Auth-Date": apiHeaderTime.toString(),
    "X-Auth-Key": API_KEY,
};

/**
 * Fetch a single episode by its ID from Podcast Index
 * @param episodeId - numeric ID of the episode
 */
export async function getEpisode(episodeId: number) {
  try {
    const response = await axios.get(`${PODCAST_INDEX_API}/episodes/byid?id=${episodeId}`, {
      headers,
    });

    const ep = response.data?.episode;

    return {
      id: ep?.id,
      title: ep?.title,
      duration: ep?.duration,
      enclosureUrl: ep?.enclosureUrl,
      image: ep?.image || ep?.feedImage,
      description: ep?.description,
    };
  } catch (err) {
    console.error("❌ Error fetching episode:", err);
    return null;
  }
}
