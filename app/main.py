# app/main.py

from app.config import DATA_DIR
from core.reader import read_exercises
from core.workout import Workout
from core.logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Workout Builder startar")

    exercises = read_exercises(DATA_DIR / "exercises.txt")

    if not exercises:
        print("Inga övningar hittades.")
        logger.error("Ingen data hittades")
        return

    muscle = input("Vad vill du träna? (ben, bröst, rygg, axlar): ").strip().lower()

    if muscle not in {"ben", "bröst", "rygg", "axlar"}:
        print("Ogiltigt val.")
        logger.warning("Ogiltig muskelgrupp")
        return

    workout = Workout(exercises)
    session = workout.create_workout(muscle)

    print("\nDitt träningspass:")
    for ex in session:
        print("-", ex["name"])

    logger.info(f"Träningspass skapat för {muscle}")

if __name__ == "__main__":
    main()
