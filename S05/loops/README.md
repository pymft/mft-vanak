## loops

### `while` is a repetitive-`if` :cool:

قراره یه کارکتر چند بار تکرار بشه. می تونیم رشته رو در یه عدد ضرب کنیم. 

فرض کنین قراره اولین بار خود رشته (کاراکتر) چاپ بشه، خط بعدش دو بار ، خط بعدش سه بار و ...  

```python
character = "+"

repeats = 1
print(character * repeats)

repeats = 2
print(character * repeats)

repeats = 2
print(character * repeats)
```

ولی بهتره هر بار مقدار متغیر ست نشه. یعنی میشه از مقدار فعلی مقدار جدیدی که باید بازنویسی کنیم و ست کنیم. هر بار مقدار قبلی به اضافه عدد یک (۱). پس باید اینجوری بشه:

```python
character = "+"

repeats = 0

repeats = repeats + 1
print(character * repeats)

repeats = repeats + 1
print(character * repeats)

repeats = repeats + 1
print(character * repeats)

```

پس یک الگویی ایجاد شد که عینا (کدی که می‌نویسیم، کاراکتر به کارکتر مشابه چیزیه که در خط‌های قبل هم تکرار شده) منظورم این دو خطه:

```python
repeats = repeats + 1
print(character * repeats)
```

فرض کنین یه ورودی داریم که مشخص می کنه باید چند خط همین الگو تکرار بشه 
ولی همین الگوی تکراری هر بار با دستور شرطی چک کنه تعداد تکرار به حد نهایی تکرار رسیده یا  نه!‌


```python
character = "+"
limit = 2

repeats = 0

if repeats < limit:
    repeats = repeats + 1
    print(character * repeats)

if repeats < limit:
    repeats = repeats + 1
    print(character * repeats)

if repeats < limit:
    repeats = repeats + 1
    print(character * repeats)

if repeats < limit:
    repeats = repeats + 1
    print(character * repeats)

if repeats < limit:
    repeats = repeats + 1
    print(character * repeats)

if repeats < limit:
    repeats = repeats + 1
    print(character * repeats)

if repeats < limit:
    repeats = repeats + 1
    print(character * repeats)

```

حالا الگوی تکرای ما این شکلی شده: 

```python
if repeats < limit:
    repeats = repeats + 1
    print(character * repeats)
```

نتیجه چی میشه؟ حتی اگه یک میلیون بار هم این الگو کپی-پیست بشه، نتیجه تفاوتی نداره. چون شرطی که چک میشه از یه جایی به بعد دیگه درست نیست. 

### `while`

ولی دستور حلقه زیر همون مفهوم و پیاده سازی می کنه. یعنی تا جایی که شرط درست باشه دوباره همون کار رو تکرار می‌کنه و وقتی که شرط دیگه درست نباشه از  حلقه میاد بیرون. 

چند خط اول برنامه به اضافه الگویی که تکرار می‌شد این پایین نوشته شده  `if` تبدیل به `while` شده

```python
character = "+"
limit = 2

repeats = 0

while repeats < limit:
    repeats = repeats + 1
    print(character * repeats)

```