import React from "react";

interface QAResult {
  question: string;
  similarity: number;
  answer?: string; // optional for now
}

interface ResultsDisplayProps {
  results: QAResult[];
}

const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ results }) => {
  if (results.length === 0)
    return <p className="text-gray-500 text-center">No results yet.</p>;

  return (
    <div className="grid grid-cols-2 gap-8 w-11/12 mx-auto">
      {/* Left Column - Similar Questions */}
      <div>
        <h2 className="text-xl font-semibold mb-3 text-black">Similar Questions</h2>
        <ul className="space-y-3">
          {results.map((item, i) => (
            <li key={i} className="p-3 border rounded-lg bg-gray-50">
              <p className="font-medium text-black">{item.question}</p>
              <p className="text-sm text-gray-500">
                Similarity: {item.similarity.toFixed(4)}
              </p>
            </li>
          ))}
        </ul>
      </div>

      {/* Right Column - Answers */}
      <div>
        <h2 className="text-xl font-semibold mb-3 text-black">Answers</h2>
        <ul className="space-y-3">
          {results.map((item, i) => (
            <li key={i} className="p-3 border rounded-lg bg-gray-50">
              <p className="text-gray-700 italic">
                {item.answer || "No answer loaded yet."}
              </p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default ResultsDisplay;
