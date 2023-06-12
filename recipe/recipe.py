from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer

def parse_ingredients(ingredients):
    parsed_ingredients = []
    lemmatizer = WordNetLemmatizer()

    for ingredient in ingredients:
        tokens = word_tokenize(ingredient)
        tagged_tokens = pos_tag(tokens)

        parsed_tokens = []
        for token, pos in tagged_tokens:
            if pos.startswith('N') or pos.startswith('J'):
                parsed_tokens.append(lemmatizer.lemmatize(token.lower()))

        parsed_ingredients.append(' '.join(parsed_tokens))

    return parsed_ingredients

# Example usage
ingredients = [
    "2 cups all-purpose flour",
    "1 teaspoon baking powder",
    "1/2 teaspoon salt",
    "1/2 cup unsalted butter, softened",
    "1 cup granulated sugar",
    "2 large eggs",
    "1 teaspoon vanilla extract",
    "1/2 cup milk",
    "1 cup chocolate chips"
]

parsed_ingredients = parse_ingredients(ingredients)
for ingredient in parsed_ingredients:
    print(ingredient)
