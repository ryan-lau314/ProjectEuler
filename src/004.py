from util.string import is_palindrome

if __name__ == "__main__":
    max_palindrome = 0
    for i in reversed(range(100, 1000)):
        for j in reversed(range(i + 1, 1000)):
            product = i * j

            if product < max_palindrome:
                break

            if is_palindrome(product):
                if product > max_palindrome:
                    print(f"Large palindrome found: {i} * {j} = {product}")
                    max_palindrome = product

    print(f"Maximum palindrome is {max_palindrome}")

