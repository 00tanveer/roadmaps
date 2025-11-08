import React, { useState, useRef } from "react";
import SearchBar from "./components/SearchBar";
import ResultsList from "./components/ResultsList";
import PodcastPlayer, {type PodcastPlayerHandle} from "./components/PodcastPlayer";

interface QAResult {
  question: string;
  similarity: number;
  answer: string;
  start_time: number;
}

const sampleEpisode = {
  id: 12345,
  title: "Shopify Distinguished Eng (L10) on Principal+ Engineering, Career Story, Regrets",
  duration: 3027,
  enclosureUrl:
    "https://anchor.fm/s/106346b90/podcast/play/110080260/https%3A%2F%2Fd3ctxlq1ktw2nl.cloudfront.net%2Fstaging%2F2025-9-23%2F409842471-44100-2-6a547111d08f3.mp3",
  image: "https://d3t3ozftmdmh3i.cloudfront.net/staging/podcast_uploaded_episode/43890660/43890660-1761284693123-b5c75ff4e85f1.jpg",
  description: " Ilya Grigorik grew to a Distinguished Engineer (VP-level role) at Shopify and I asked him what it took to get there. We covered his full career including the behind the scenes of his startup getting acquired by Google, his growth to Director at Google, and what it means to operate like a Distinguished engineer.",
};

const App: React.FC = () => {
  const [results, setResults] = useState<QAResult[]>([]);
  const [loading, setLoading] = useState(false);
  const playerRef = useRef<PodcastPlayerHandle>(null);
  const handleSearch = async (query: string) => {
    setLoading(true);
    try {
      const res = await fetch("http://localhost:8000/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      const data = await res.json();
      setResults(data.results || []);
    } catch (err) {
      console.error("Search error:", err);
    } finally {
      setLoading(false);
    }
  };

  const handlePlayClick = (timestamp: number) => {
    console.log('Play clicked')
    console.log("App got timestamp:", timestamp, typeof timestamp);
    if (!playerRef.current) {
      console.warn("Player not mounted yet!");
      return;
    }
    // Convert "hh:mm:ss" or "mm:ss" → seconds
  let seconds = 0;
  if (typeof timestamp === "string") {
    const parts = timestamp.split(":").map(Number);
    if (parts.length === 3) {
      seconds = parts[0] * 3600 + parts[1] * 60 + parts[2];
    } else if (parts.length === 2) {
      seconds = parts[0] * 60 + parts[1];
    } else {
      seconds = Number(timestamp) || 0;
    }
  } else {
    seconds = timestamp;
  }

    console.log("Converted timestamp (seconds):", seconds);
    playerRef.current.seekTo(seconds);
    playerRef.current.play();
  };

  return (
    <div className="w-screen h-screen flex flex-col items-center justify-start py-5 bg-gray-100">
      <h2 className="title text-3xl font-bold mb-6 text-black">🎯 Search for wisdom, across thousands of conversations</h2>
      <SearchBar onSearch={handleSearch} />
      {loading ? (
        <p className="text-gray-600 mt-6">Searching...</p>
      ) : (
        <ResultsList results={results} onPlayClick={handlePlayClick}/>
      )}
      <PodcastPlayer ref={playerRef} episode={sampleEpisode}/>
    </div>
  );
};

export default App;
