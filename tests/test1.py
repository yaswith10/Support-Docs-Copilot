from app.parsers.markdown_parser import MarkdownParser

parser = MarkdownParser()
document = parser.parse("app/data/raw/sample.md")
print(document)