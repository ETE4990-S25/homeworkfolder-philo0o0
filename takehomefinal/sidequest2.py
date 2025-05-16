import cProfile
import pstats
import io

#Here I will profile the code from quest 1
def profile_code():
    profiler = cProfile.Profile()
    profiler.enable()
#Here I will run both quests in order to profile everything
    run_quest1()
    run_quest2()
    profiler.disable()
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('tottime')
    ps.print_stats()
    
    with open("quest_profiling.log", "w") as f:
        f.write(s.getvalue())
    
    print("Profiling complete. Results saved to quest_profiling.log.")

if __name__ == "__main__":
    profile_code()
