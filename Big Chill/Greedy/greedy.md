# How to Think in a Greedy Manner

This is one of the hardest parts of learning greedy algorithms. The key
isn't to memorize solutions---it's to recognize **when a local choice
preserves the most options for the future**.

Let's use the **Lemonade Change** problem as an example.

## Step 1: Ask yourself what decisions you actually have

-   **\$5** --> no decision.
-   **\$10** -->  only one way to give change (`$5`).
-   **\$20** -->  **two choices**:
    1.  `$10 + $5`
    2.  `$5 + $5 + $5`

Whenever there are multiple valid choices, that's usually where a greedy
decision is needed.

## Step 2: Ask which resource is more valuable

Don't think about the current customer.

Think about future customers.

Ask yourself:

> **Which bill is harder to replace?**

For a future **\$10**, you must give one **\$5** bill.

For a future **\$20**, you need either:

-   `$10 + $5`
-   `$5 + $5 + $5`

A **\$5 bill is always required**, while a **\$10 bill is only useful
together with a \$5**.

**Conclusion:** A **\$5 bill is more valuable** than a **\$10 bill**.

## Step 3: Preserve the most valuable resource

Whenever possible:

    20
    ↓
    10 + 5

instead of

    5 + 5 + 5

because using `$10 + $5` preserves more `$5` bills for future customers.

This is the greedy choice.

## Step 4: Form the greedy rule

Once you've identified the valuable resource:

> **Never waste it if another valid solution exists.**

Algorithm:

``` java
if (ten > 0 && five > 0)
    use 10 + 5;
else
    use three 5s;
```

------------------------------------------------------------------------

# General Greedy Thinking Process

For every greedy problem, ask these questions.

## 1. What is my choice?

Examples:

-   **Jump Game:** How far should I jump?
-   **Lemonade Change:** How should I give change?
-   **Interval Scheduling:** Which interval should I keep?

## 2. What resource is limited?

Examples:

-   Money
-   Time
-   Reachable distance
-   Cookies
-   Fuel

## 3. Which resource is hardest to replace?

Examples:

-   **Lemonade Change:** `$5` bills
-   **Jump Game:** Maximum reachable index
-   **Assign Cookies:** Large cookies

## 4. Which local decision keeps the most future options?

Examples:

-   **Lemonade Change:** Use `$10 + $5`.
-   **Jump Game:** Always maximize the farthest reachable index.
-   **Interval Scheduling:** Keep the interval that finishes earliest.

------------------------------------------------------------------------

# A Common Greedy Pattern

Most greedy solutions can be summarized as:

> **Spend the least valuable resource first, and preserve the most
> valuable one.**

  Problem               Preserve
  --------------------- ----------------------------
  Lemonade Change       `$5` bills
  Assign Cookies        Larger cookies
  Jump Game             Maximum reachable distance
  Gas Station           Fuel balance
  Interval Scheduling   Future time
  Meeting Rooms         Earliest finishing room

------------------------------------------------------------------------

# Practice Checklist

Before writing code for a greedy problem, answer these four questions:

1.  Where do I have a choice?
2.  What resource am I managing?
3.  Which resource is hardest to replace or most valuable later?
4.  Which choice preserves that resource for future decisions?

If you consistently practice this thought process, you'll start
recognizing greedy strategies naturally instead of memorizing solutions.
