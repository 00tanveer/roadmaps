import QAItem from "./QAItem";

interface Result {
  question: string;
  answer: string;
  similarity?: number;
  audioUrl?: string;
  start_time: number;
}

interface ResultsListProps {
  results: Result[];
  onPlayClick: (timestamp: number) => void;
}

const ResultsList: React.FC<ResultsListProps> = ({ results, onPlayClick }) => {
  return (
    <div className="w-full max-w-3xl mt-8">
      {results.map((r, i) => (
        <QAItem
          key={i}
          question={r.question}
          answer={r.answer}
          start_time={r.start_time}
          onPlayClick={onPlayClick}
        />
      ))}
    </div>
  );
};

export default ResultsList;
