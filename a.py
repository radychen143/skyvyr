import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        artist="Skyvyr",
        producer="Rady In",
        tagline="Dark Aura Phonk • Slowed • Headphone Tuned",
        bio=(
            "Skyvyr delivers a dark aura phonk sound with slowed tempo and "
            "clean, controlled 808s tuned specifically for headphones. "
            "Deep sub presence without harsh distortion, hypnotic atmosphere, "
            "and smooth stereo depth create an immersive, heavy-bass experience "
            "built for long listening sessions."
        )
    )

if __name__ == "__main__":
    # REQUIRED for Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
