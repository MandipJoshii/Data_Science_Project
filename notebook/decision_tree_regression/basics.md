# Decision Tree — My Understanding

## What is it basically

okay so decision tree is not like linear regression where it finds one formula and applies it to every single student. decision tree is smarter than that. it knows that different groups of students behave differently so instead of one formula it asks questions and keeps splitting students into smaller and smaller groups until each group is similar enough to predict confidently.

think of it like a teacher trying to guess a students grade before seeing results. first question would be something like "did you pass your previous exams?" if yes, probably a good student. if no, probably going to struggle. thats literally a decision tree. we just let the machine do this automatically.

---

## The Structure

```
                    G2 >= 10?              → ROOT NODE (depth 0)
                   ↙         ↘
                 YES           NO          → EDGES (just the paths)
                  ↓             ↓
           G1 >= 12?         G1 >= 7?      → DECISION NODES (depth 1)
            ↙     ↘           ↙    ↘
          YES      NO        YES    NO     → EDGES
           ↓        ↓         ↓      ↓
       Medu>=3?  G3=11.1   G3=8.4  G3=3.9 → depth 2
        ↙    ↘
      YES     NO
       ↓       ↓
    G3=15.2  G3=12.1       → LEAF NODES (final answer, no more questions)
```

**Root Node** → the very first question at the top. only one exists. this is depth 0.

**Decision Node** → any node in the middle that still asks a question and splits further.

**Leaf Node** → the final box at the bottom. no more questions here. just gives the predicted G3 value.

**Edge** → the arrow/path connecting nodes. always represents YES or NO answer to the question above.

**Depth** → how many levels of questions deep you are. root node is depth 0, first split is depth 1 and so on.

---

## How it actually trains — step by step

### Step 1 — hands it all 316 students

when you run model.fit(X_train, Y_train) you are handing 316 students to the model. each student has 4 features (G1, G2, Medu, studytime) and a real G3 score. right now they are all one big mixed group.

### Step 2 — calculates entropy of the whole group

entropy = how confused you would be trying to predict G3 for a random student from this group.

if you pick a random student from all 316 their G3 could be anywhere from 0 to 20. you have no idea. that is HIGH entropy — maximum confusion.

```
HIGH ENTROPY (confused):
G3 values = [2, 5, 8, 11, 14, 17, 20, 3, 9, 16...]
pick any student → G3 could be anything → terrible prediction

LOW ENTROPY (confident):
G3 values = [13, 14, 14, 15, 14, 15, 13...]
pick any student → G3 is probably around 14 → great prediction
```

at the start all 316 students are mixed so entropy is HIGH. the model knows it needs to reduce this confusion by splitting students into cleaner groups.

### Step 3 — tries every possible question on every feature

the model literally brute forces this. it tries every single question it can think of:

```
On G2: "Is G2 >= 1?" , "Is G2 >= 2?" , "Is G2 >= 3?" ... every value
On G1: "Is G1 >= 1?" , "Is G1 >= 2?" ... every value
On Medu: "Is Medu >= 1?" , "Is Medu >= 2?" ... every value
On studytime: "Is studytime >= 1?" , "Is studytime >= 2?" ... every value
```

for each question it temporarily splits students into YES group and NO group and measures how clean each group is.

### Step 4 — calculates information gain for each question

for every question it tried it calculates:

```
Information Gain = how much did this question REDUCE confusion?
                 = Entropy BEFORE split − Entropy AFTER split
```

good question example:
```
BEFORE "Is G2 >= 10?":
  316 students all mixed → very confused → HIGH entropy

AFTER "Is G2 >= 10?":
  YES group: 200 students with decent G3 (10-20) → cleaner
  NO group:  116 students with low G3 (0-9) → cleaner

Information Gain = HIGH → great question!
```

bad question example:
```
BEFORE "Is studytime >= 2?":
  316 students mixed → HIGH entropy

AFTER "Is studytime >= 2?":
  YES group: still totally mixed G3 values
  NO group: also mixed

Information Gain = LOW → useless question
```

### Step 5 — picks the best question → ROOT NODE

after trying hundreds of questions it picks the one with highest information gain. on student data G2 almost always wins because it has 0.9 correlation with G3.

```
"Is G2 >= 10?"       → Information Gain = 0.48  ← WINNER → ROOT NODE
"Is G1 >= 9?"        → Information Gain = 0.35
"Is Medu >= 3?"      → Information Gain = 0.12
"Is studytime >= 2?" → Information Gain = 0.08
```

### Step 6 — splits 316 students into two groups

```
Is G2 >= 10?
      ↙              ↘
    YES                NO
200 students         116 students
G3 avg = 13.5        G3 avg = 6.8
still a bit mixed    still a bit mixed
→ need more splits   → need more splits
```

now instead of one confused group of 316 you have two slightly cleaner groups.

### Step 7 — repeats on EACH group separately

takes the 200 YES students → calculates entropy → tries every question → finds best one → splits again.
takes the 116 NO students → same process → splits again.

```
              Is G2 >= 10?
             ↙              ↘
           YES                NO
       200 students        116 students
            ↓                   ↓
      Is G1 >= 12?         Is G1 >= 7?
       ↙       ↘             ↙       ↘
    150kids   50kids       80kids   36kids
    G3≈15.2  G3≈11.1      G3≈8.4   G3≈3.9
```

4 groups now. each cleaner than before. keeps doing this same process on every group.

### Step 8 — keeps repeating until max_depth=5 (pruning)

```
Depth 0 → 1 group   (316 students)   very messy
Depth 1 → 2 groups  (200, 116)       getting cleaner
Depth 2 → 4 groups                   cleaner
Depth 3 → 8 groups                   cleaner
Depth 4 → 16 groups                  very clean
Depth 5 → 32 groups                  very pure ← STOP HERE
```

why stop at depth 5? because without stopping the tree would go forever:

```
depth 10  → 1024 groups
depth 15  → 32768 groups
eventually → 1 student per group → memorized every student

training R² = 1.0 (perfect!)
test R²     = terrible (it memorized, didnt learn)
```

this is called overfitting. max_depth is the solution — it cuts the tree before it goes too deep. this cutting is called PRUNING. on student data max_depth=5 was the sweet spot giving R²=0.87.

### Step 9 — how the final G3 prediction is found

at depth 5 you have 32 leaf nodes. the predicted G3 for each leaf is just:

```
Predicted G3 = AVERAGE G3 of all students who landed in that leaf
```

example leaf node:
```
Students who answered all 5 questions the same way: 18 students
Their real G3 scores: [14, 15, 14, 16, 15, 14, 15, 14, 16, 15, 14, 15, 13, 15, 14, 16, 15, 14]
Average = 14.7

→ any new student who follows this exact path gets predicted G3 = 14.7
```

no complex formula. just the average G3 of similar students. thats it.

---

## How predicting works (model.predict)

new student arrives with G2=13, G1=11, Medu=2, studytime=3:

```
Question 1 (root): Is G2 >= 10?      → 13 >= 10 → YES → go left
Question 2:        Is G1 >= 12?      → 11 >= 12 → NO  → go right
Question 3:        Is G2 >= 13?      → 13 >= 13 → YES → go left
Question 4:        Is studytime >= 3? → 3 >= 3  → YES → go left
Question 5:        Is Medu >= 3?     → 2 >= 3   → NO  → go right

LEAF NODE reached → Predicted G3 = 11.4
```

student answered 5 questions and landed in a group of similar students. done.

---

## Why MAE, MSE, R² work the same here

these metrics dont care HOW the model predicted. they only care about the difference between predicted and actual:

```
actual G3 = 12,  predicted G3 = 11.4  → error = 0.6
actual G3 = 7,   predicted G3 = 8.2   → error = -1.2

MAE = average of |errors|
MSE = average of errors squared
R²  = how much of the G3 pattern did the model explain
```

same formula whether the prediction came from a line or a tree.

---

## Why decision tree beats linear regression

linear regression: one formula for all 395 students
```
G3 = 0.9×G2 + 0.3×G1 + ...
student with G2=15 and 3 failures → still predicts high G3
WRONG because failures clearly matter separately
```

decision tree: different rules for different groups
```
Is G2 >= 14? YES
Is failures >= 2? YES
→ Predicted G3 = 9  (even though G2 is high, failures bring it down)
```

real students dont all follow one straight formula. they fall into groups. thats why decision tree does better.

---

## Final scores on student dataset

```
Linear Regression  → R²=0.797
Decision Tree      → R²=0.870  (max_depth=5)
```

decision tree wins by 0.073 which is a meaningful improvement just by changing the model and tuning one setting.