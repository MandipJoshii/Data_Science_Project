# EDA — Visualization (My Understanding)

EDA is not just about making plots look pretty. The real point is to understand what your data is telling you before you touch any model. Every plot you make should answer a question — if you can't say what question it answers, you probably don't need that plot.

---

## Matplotlib

Matplotlib is the base. Everything else is built on top of it. It gives you full control but sometimes you have to write more to get a decent looking result.

### Scatter Plot

This is for when you want to see if two numeric things are related. You put one on the X axis and one on the Y axis and look at the pattern the dots form. If they go up together, there's a positive relationship. If one goes up while the other goes down, it's negative. If the dots look like someone threw them randomly, there's probably no relationship worth caring about.

### Histogram

This one is for looking at a single feature and understanding how its values are spread out. It groups all the values into buckets and shows you how many fall into each bucket. So for G3 you'd see how many students scored low, how many scored in the middle, how many scored high. It tells you if your data is balanced or leaning heavily to one side, which actually matters later when you're building models.

### Bar Chart

Use this when one of your features is a category — like school type, urban or rural, male or female — and you want to compare a number across those categories. Usually the number is an average. So you'd ask something like, do urban students have a higher average G3 than rural students? The bar chart answers that visually.

### Line Plot

This one is about showing change across a sequence. The X axis needs to have some kind of order to it. In this project the most natural use for a line plot is showing gradient descent — each step the model takes, the error should be going down, and the line plot shows that drop happening over time. It's less about EDA and more about showing your model is actually learning.

### Boxplot

This is one of the most useful plots in EDA and people underuse it. It shows you the full spread of one feature in a single picture — the middle value, where most of your data sits, and anything that falls way outside the normal range which are called outliers. Those outliers matter because they can mess with your model if you don't deal with them. For grouped comparison though, Seaborn's version is easier to use.

---

## Seaborn

Seaborn sits on top of Matplotlib and makes certain things that would take many lines to do in Matplotlib happen in one line. It's especially good for anything involving categories or correlations.

### Heatmap

This is the correlation plot. It shows you every numeric feature in your dataset plotted against every other numeric feature, and the color tells you how related they are. Dark red usually means strong positive relationship, dark blue means strong negative. For this project it's how you figure out which features actually have something to do with G3 and which ones are just noise. This is a core part of feature selection.

### Boxplot (Grouped)

Same idea as Matplotlib's boxplot but now you're comparing the spread of values across categories side by side. So instead of just seeing the distribution of G3 for everyone, you see it separately for urban students and rural students next to each other. Makes comparisons obvious.

### Pairplot

This one is a big picture overview. It takes the features you give it and makes a grid of scatter plots — every feature plotted against every other feature. It's slow to run if you give it too many columns but useful early on when you want to see patterns across many features at once. You usually narrow down which columns you pass into it first.

### Countplot

Simple one. It just counts how many times each category shows up and draws bars. You'd use it to see how many students are from each school, or how the male-female split looks in your dataset. It tells you if your categories are balanced or if one side heavily dominates, which affects how much you can trust comparisons between them.

### Histplot with KDE

This is basically a histogram but with a smooth curve layered on top. That curve is called KDE and it helps you see the shape of your data more clearly than bars alone. A normal bell shape means your data is evenly distributed. A curve leaning to one side means most values are concentrated there. Knowing the shape of your data helps you make decisions later in modeling.

---


