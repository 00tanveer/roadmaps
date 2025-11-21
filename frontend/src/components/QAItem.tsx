import { useState } from "react";
import { Play } from "lucide-react"; // icon
import type { QAResult } from "./types.tsx";


interface QAItemProps {
  result: QAResult;
  onPlayClick: (episode: QAResult) => void;
}

const QAItem: React.FC<QAItemProps> = ({ result, onPlayClick }: QAItemProps) => {
  const [isExpanded, setIsExpanded] = useState(false);

  const truncatedAnswer = !isExpanded && result.answer.length > 300 
    ? result.answer.slice(0, 300) + "..." 
    : result.answer;

  const handlePlay = () => {
    console.log("QAItem play clicked:", result.id, result.title, result.start, result.end);
    onPlayClick(result); // send the full episode/result up
    
  }
  return (
    <div className="w-full bg-white rounded-xl shadow-sm border border-gray-200 p-4 mb-4 hover:shadow-md transition">
      <div className="flex items-center justify-between mb-2">
        <h3 className="font-semibold text-gray-900 text-lg">{result.question}</h3>
        <button 
          onClick={handlePlay} 
          className="p-2 rounded-full hover:bg-gray-100 transition"
        >
          <Play className="w-5 h-5 text-gray-700" />
        </button>
      </div>

      <p className="text-gray-700 text-sm leading-relaxed">{truncatedAnswer}</p>

      {result.answer.length > 300 && (
        <button 
          onClick={() => setIsExpanded(!isExpanded)}
          className="text-blue-500 text-xs mt-2 hover:underline"
        >
          {isExpanded ? "Show less" : "Show more"}
        </button>
      )}

      {/* {similarity && (
        <p className="text-xs text-gray-500 mt-2">Similarity: {similarity.toFixed(4)}</p>
      )} */}
    </div>
  );
}

export default QAItem;