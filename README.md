# WildLife-Vision

**An AI system that spots wild animals in dark footage and announces what it sees.**



## The problem

Wildlife cameras struggle at night, which is when many animals are most active. Dark footage hides animals from both people and detection models, and watching a live feed all day is slow and tiring.



## What it does

1. **Takes in camera frames**, from day or night video.
2. **Brightens dark frames** with a GAN that turns low-light images into daytime-quality ones.
3. **Detects animals** with YOLOv8 and names the species.
4. **Announces the species** through an LLM-powered alert, by voice and by text, so nobody has to stare at the feed.
5. **Stores every detection** in a database through SQLAlchemy.
6. **Shows reports** in a Flask web app.


## Results

| Claim | Number | How it was measured |
|---|---|---|
| Detection accuracy in low-light and night conditions | 95% 
| Species recognition gain from the GAN enhancer | 50% 
| Report generation time after SQLAlchemy optimisation | 73%

Only keep a row if you can fill the third column honestly.

## Screenshots

Add your own real outputs to a `screenshots/` folder:

- `before_after_gan.png`: a dark frame next to its enhanced version
- `detection_example.png`: YOLOv8 boxes and species labels on a real frame
- `report_page.png`: the Flask report view

## Tech stack

Python, PyTorch, YOLOv8, OpenCV, GAN, Flask, SQLAlchemy, LLM-based alerts.

## Run it

```bash
git clone [FILL IN: repo URL]
cd [FILL IN: folder]
pip install -r requirements.txt
python [FILL IN: entry file, e.g. app.py]
```

Model weights and sample footage: [FILL IN: where to download them, or say they are not included].

## Author

Kollu Vijay, B.Tech CSE, KL University.
