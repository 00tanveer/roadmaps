import React, { useState } from "react";
import SearchBar from "./components/SearchBar";
import ResultsList from "./components/ResultsList";
import PodcastPlayer from "./components/PodcastPlayer";
import type { QAResult } from "./components/types";

const App: React.FC = () => {
  const [results, setResults] = useState<QAResult[]>([]);
  const [loading, setLoading] = useState(false);
  
  // Podcastplayer state to pass as props
  const [currentEpisode, setCurrentEpisode] = useState<QAResult | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [seekTime, setSeekTime] = useState<number | null>(null);

  const handleSearch = async (query: string) => {
    setLoading(true);
    try {
      const res = await fetch("http://localhost:8000/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      const data = await res.json();
      const docs = data.results.metadatas[0];
      setResults(docs || []);
    } catch (err) {
      console.error("Search error:", err);
    } finally {
      setLoading(false);
    }
  };

  const handlePlayClick = (episode: QAResult) => {
    console.log(episode.start)
    setCurrentEpisode(episode);
    setSeekTime({ time: episode.start, token: Date.now() });
    setIsPlaying(true);
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
      <PodcastPlayer 
        episode={currentEpisode}
        seekTime={seekTime}
        isPlaying={isPlaying}
        onPlayStateChange={setIsPlaying}
        onSeekChange={setSeekTime}
        onEnded={() => setIsPlaying(false)}
        />
    </div>
  );
};

export default App;
