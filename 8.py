# Write a program to check if all the brackets are closed in a given code snippet.

def areBracketsBalanced(expr):
	stack = []

	for char in expr:
		if char in ["(", "{", "["]:

			stack.append(char)
		else:

			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False

	if stack:
		return False
	return True


if __name__ == "__main__":
	expr = str(input("Expression: "))

	if areBracketsBalanced(expr):
		print("Balanced")
	else:
		print("Not Balanced")