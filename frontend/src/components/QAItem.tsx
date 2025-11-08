import { useState } from "react";
import { Play } from "lucide-react"; // icon

interface QAItemProps {
  question: string;
  answer: string;
  similarity?: number;
  start_time: number;
  onPlayClick: (timestamp: number) => void;
}

const QAItem: React.FC<QAItemProps> = ({ question, answer, similarity, start_time, onPlayClick }: QAItemProps) => {
  const [isExpanded, setIsExpanded] = useState(false);

  const truncatedAnswer = !isExpanded && answer.length > 300 
    ? answer.slice(0, 300) + "..." 
    : answer;

  return (
    <div className="w-full bg-white rounded-xl shadow-sm border border-gray-200 p-4 mb-4 hover:shadow-md transition">
      <div className="flex items-center justify-between mb-2">
        <h3 className="font-semibold text-gray-900 text-lg">{question}</h3>
        <button 
          onClick={() => onPlayClick(start_time)} 
          className="p-2 rounded-full hover:bg-gray-100 transition"
        >
          <Play className="w-5 h-5 text-gray-700" />
        </button>
      </div>

      <p className="text-gray-700 text-sm leading-relaxed">{truncatedAnswer}</p>

      {answer.length > 300 && (
        <button 
          onClick={() => setIsExpanded(!isExpanded)}
          className="text-blue-500 text-xs mt-2 hover:underline"
        >
          {isExpanded ? "Show less" : "Show more"}
        </button>
      )}

      {similarity && (
        <p className="text-xs text-gray-500 mt-2">Similarity: {similarity.toFixed(4)}</p>
      )}
    </div>
  );
}

export default QAItem;