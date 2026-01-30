import matplotlib.pyplot as plt

# Tạo hình vẽ
fig, ax = plt.subplots(1, 3, figsize=(12, 4))

# --- Kí hiệu điểm ---
ax[0].scatter([0.5], [0.5], s=400, color="red", marker="*")
ax[0].set_title("Kí hiệu điểm\n(Thành phố, mỏ, núi)", fontsize=10)
ax[0].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[0].axis("off")

# --- Kí hiệu đường ---
ax[1].plot([0.1, 0.9], [0.2, 0.8], color="blue", linewidth=3)
ax[1].plot([0.1, 0.9], [0.8, 0.2], color="green", linestyle="--", linewidth=2)
ax[1].set_title("Kí hiệu đường\n(Sông, đường, biên giới)", fontsize=10)
ax[1].set_xlim(0, 1)
ax[1].set_ylim(0, 1)
ax[1].axis("off")

# --- Kí hiệu diện tích ---
ax[2].fill_between([0, 1], 0, 1, color="lightgreen")
ax[2].text(0.5, 0.5, "Rừng", fontsize=12, ha="center", va="center")
ax[2].set_title("Kí hiệu diện tích\n(Rừng, hồ, ruộng)", fontsize=10)
ax[2].set_xlim(0, 1)
ax[2].set_ylim(0, 1)
ax[2].axis("off")

plt.tight_layout()
plt.show()
