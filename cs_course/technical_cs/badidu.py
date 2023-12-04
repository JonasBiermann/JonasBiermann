def parse(text):
    stack = []
    for elem in text:
        if elem in ["ba", "di", "du"]:
            stack.append(char)
        else:
            raise ValueError("Ungültiges Zeichen: " + elem)

  if len(stack) != 1:
    raise ValueError("Unvollständiges Wort")

  return words


def main():
  text = ['du', 'du', 'ba', 'ba', 'du', 'du', 'ba', 'ba', 'du', 'du']
  return parse(text)


if __name__ == "__main__":
  print(main())
