import React, {
  useRef,
  useState,
  useEffect,
  useImperativeHandle,
  forwardRef,
} from "react";

interface Episode {
  id: number;
  title: string;
  duration: number;
  enclosureUrl: string;
  image?: string;
}

export interface PodcastPlayerHandle {
  seekTo: (seconds: number) => void;
  play: () => void;
  pause: () => void;
}

interface Props {
  episode: Episode | null;
}

const formatTime = (seconds: number): string => {
  if (isNaN(seconds)) return "00:00";
  const m = Math.floor(seconds / 60);
  const s = Math.floor(seconds % 60);
  return `${m.toString().padStart(2, "0")}:${s.toString().padStart(2, "0")}`;
};

const PodcastPlayer = forwardRef<PodcastPlayerHandle, Props>(
  ({ episode }, ref) => {
    const audioRef = useRef<HTMLAudioElement | null>(null);
    const [progress, setProgress] = useState(0);
    const [isPlaying, setIsPlaying] = useState(false);
    const [currentTime, setCurrentTime] = useState(0);
    const [duration, setDuration] = useState(0);

    const handleTimeUpdate = () => {
      if (audioRef.current) {
        const { currentTime, duration } = audioRef.current;
        setCurrentTime(currentTime);
        setDuration(duration);
        setProgress((currentTime / duration) * 100 || 0);
      }
    };

    const handleSeek = (e: React.ChangeEvent<HTMLInputElement>) => {
      if (audioRef.current) {
        const newTime =
          (parseFloat(e.target.value) / 100) * audioRef.current.duration;
        audioRef.current.currentTime = newTime;
        setProgress(parseFloat(e.target.value));
      }
    };

    const togglePlay = () => {
      if (!audioRef.current) return;
      if (isPlaying) {
        audioRef.current.pause();
      } else {
        audioRef.current.play();
      }
      setIsPlaying(!isPlaying);
    };

    const skip = (seconds: number) => {
      if (audioRef.current) {
        audioRef.current.currentTime = Math.min(
          Math.max(audioRef.current.currentTime + seconds, 0),
          audioRef.current.duration
        );
      }
    };

    // ✅ Expose methods for external control
    useImperativeHandle(ref, () => ({
      seekTo: (seconds: number) => {
        if (!audioRef.current) {
            console.warn("⚠️ Audio ref not ready yet.");
            return;
        }
        if (typeof seconds !== "number" || !isFinite(seconds)) {
            console.error("❌ Invalid seek time:", seconds);
            return;
        }
        if (audioRef.current) {
            console.log('Seeking to', seconds)
          audioRef.current.currentTime = seconds;
        }
      },
      play: () => {
        audioRef.current?.play();
        setIsPlaying(true);
      },
      pause: () => {
        audioRef.current?.pause();
        setIsPlaying(false);
      },
    }));

    useEffect(() => {
      const audio = audioRef.current;
      if (audio) {
        audio.addEventListener("timeupdate", handleTimeUpdate);
        audio.addEventListener("loadedmetadata", handleTimeUpdate);
      }
      return () => {
        if (audio) {
          audio.removeEventListener("timeupdate", handleTimeUpdate);
          audio.removeEventListener("loadedmetadata", handleTimeUpdate);
        }
      };
    }, []);

    if (!episode) return null;

    return (
      <div className="fixed bottom-0 left-0 w-full bg-neutral-900 text-white h-[150px] flex items-center px-6 shadow-2xl">
        {episode.image && (
          <img
            src={episode.image}
            alt={episode.title}
            className="w-20 h-20 rounded-lg object-cover mr-6"
          />
        )}

        <div className="flex flex-col flex-1">
          <h2 className="text-lg font-semibold truncate">{episode.title}</h2>
          <p className="text-xs text-neutral-400 mb-2">
            {Math.round(episode.duration / 60)} min
          </p>

          {/* Custom progress bar */}
          <div className="flex items-center mb-3">
            <span className="text-xs text-neutral-400 w-10 text-right mr-3">
              {formatTime(currentTime)}
            </span>
            <input
              type="range"
              value={progress}
              onChange={handleSeek}
              className="flex-1 h-1 bg-neutral-700 rounded-lg appearance-none cursor-pointer accent-red-500"
            />
            <span className="text-xs text-neutral-400 w-10 ml-3">
              {formatTime(duration)}
            </span>
          </div>

          {/* Controls */}
          <div className="flex justify-center items-center space-x-8 mt-2">
            <button
              onClick={() => skip(-10)}
              className="text-white hover:text-red-400 transition"
            >
              ⏪ 10s
            </button>

            <button
              onClick={togglePlay}
              className="bg-red-500 hover:bg-red-600 rounded-full w-10 h-10 flex items-center justify-center text-white text-lg"
            >
              {isPlaying ? "❚❚" : "▶"}
            </button>

            <button
              onClick={() => skip(10)}
              className="text-white hover:text-red-400 transition"
            >
              10s ⏩
            </button>
          </div>
        </div>

        <audio ref={audioRef} src={episode.enclosureUrl} preload="metadata" />
      </div>
    );
  }
);

export default PodcastPlayer;
