import QAItem from "./QAItem";
import type {QAResult} from "./types.tsx";



interface ResultsListProps {
  results: QAResult[];
  onPlayClick: (episode: QAResult) => void;
}

const ResultsList: React.FC<ResultsListProps> = ({ results, onPlayClick }) => {
  // console.log(results)
  return (
    <div className="w-full max-w-3xl mt-8">
      {results.map((r, i) => (
        <QAItem
          key={i}
          result={r}      
          onPlayClick={onPlayClick}  
          />
      ))}
    </div>
  );
};

export default ResultsList;
