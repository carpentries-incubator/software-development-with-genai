import sys
import pandas as p
pa = sys.argv[1]
d = p.read_csv(pa)
x = d.set_index("name")[d.columns[2:]].T 
y0 = x.index.astype(int)
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(16, 10))
n = len(x.columns)
cmap = plt.get_cmap("hsv")
for i, c in enumerate(x.columns):
    import numpy as np
    z = p.to_numeric(x[c], errors="coerce").to_numpy()
    z = np.nan_to_num(z, nan=0.0)
    cc = cmap(i / max(1, n - 1))
    ax.plot(
        y0,
        z,
        color=cc,
        linewidth=0.3,
        linestyle="-.",
        alpha=0.9,
    )
    if i % 15 == 0:
        q = np.linspace(0, len(y0) - 1, num=min(6, len(y0)), dtype=int)
        ax.scatter(
            y0[q],
            z[q],
            s=20 + 20 * (i % 5),
            c=[cc],
            marker=["o", "x", "s", "^"][i % 4],
            alpha=0.9,
        )
for v in np.linspace(int(y0.min()), int(y0.max()), num=8, dtype=int):
    ax.axvline(v, color=["k", "grey", "brown"][v % 3], alpha=0.05, linewidth=1.0)
ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
ax.legend(x.columns[:6], loc="upper right", fontsize=8)
x_, y_ = 1950, 0
ax.text(
    x_,
    y_,
    "<-here",
    fontsize=12,
    color="darkred",
    rotation=15,
    bbox=dict(facecolor="yellow", alpha=0.6),
)
plt.tight_layout()
fig.savefig("plot.jpg", dpi=300, bbox_inches="tight")