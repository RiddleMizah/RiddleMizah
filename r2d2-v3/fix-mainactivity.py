from pathlib import Path

path = Path("R2D2-Controller-Android/app/src/main/java/com/riddle/camsr2d2/MainActivity.java")
text = path.read_text(encoding="utf-8")
text = text.replace(
    "private final List<Routine> routines=new ArrayList<>(),draft=new ArrayList<>();private final RoutineRecorder recorder=new RoutineRecorder();",
    "private final List<Routine> routines=new ArrayList<>();private final List<RoutineStep> draft=new ArrayList<>();private final RoutineRecorder recorder=new RoutineRecorder();",
)
text = text.replace(
    'Ui.text(this,"R2-D2 LAB","20",true,"#FFFFFF")',
    'Ui.text(this,"R2-D2 LAB",20,true,"#FFFFFF")',
)
path.write_text(text, encoding="utf-8")
