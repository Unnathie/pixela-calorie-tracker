# 🍽️ Pixela Calorie Tracker

Because if you don’t log it, did those calories even burn? 🔥  

This little Python script hooks into the [Pixela API](https://pixe.la/) to keep track of your daily calorie burn turning your effort into a beautiful graph. 🏃‍♀️📈

---

## ✨ What it Does
- 📊 Creates a Pixela graph to visualize your progress  
- 🔥 Adds daily "pixels" with calories burned  
- ✏️ Lets you update an entry if you typo’d (we’ve all been there)  
- 🗑️ Delete a pixel when you want to pretend that donut never happened  

---

## 🛠 Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/pixela-calorie-tracker.git
   cd pixela-calorie-tracker
   ```

2. **Install the one dependency**

   ```bash
   pip install requests
   ```

3. **Get yourself a Pixela account** (it’s free!)
   👉 [https://pixe.la/](https://pixe.la/)

4. **Export your token** (replace `your_pixela_token` with your real one):

   ```bash
   export TOKEN-ENV=your_pixela_token
   ```

---

## 🚀 Usage

### Add today’s calories

```bash
python main.py
```

You’ll be asked:

```
How many calories did you burn? on <date>
```

Type your number, hit enter, and boom 💥 — logged!

### Other tricks

Inside the script, you’ll also find handy functions:

* `create_user()` – run once to set yourself up
* `create_graph()` – run once to make your calorie graph
* `update_pixel(quantity)` – fix today’s number
* `delete_pixel()` – erase today’s entry (oopsies!)

---

## 🤓 Example Graph

Imagine a pixelated line chart where your calories burned slowly rise as you chase that summer body.

### 🖥️ Console Output
<img width="498" height="132" alt="Console output" src="https://github.com/user-attachments/assets/326e8953-6370-47ee-8a98-9b34c76dcd9c" />

### 📈 Graph View
<img width="1317" height="671" alt="Pixela graph" src="https://github.com/user-attachments/assets/dfe72503-8c24-458a-90f4-f1cd370926f0" />


## ⚠️ Notes

* Your Pixela token lives safely in your environment, not in this repo. Don’t hardcode it!
* Graph ID defaults to `graph4` because… why not? You can change it.

---

## 🥳 Why?

Because tracking makes progress visible, and progress is addictive. Plus, it’s more fun to brag with graphs.

---

Happy pixel logging! 🎉
