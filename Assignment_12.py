1. The PdfFileReader() and PdfFileWriter() File objects should be opened in 'rb' (read binary) and 'wb' (write binary) modes, respectively.

2. To get a Page object for page 5 from a PdfFileReader object, you can use the getPage(4) method, as Python uses zero-based indexing.

3. The numPages variable of a PdfFileReader object stores the number of pages in the PDF document.

4. If the PDF is encrypted with the password 'swordfish', you need to call the decrypt('swordfish') method on the PdfFileReader object before you can obtain Page objects from it.

5. To rotate a page, you can use the rotate(angle) method, where angle is an integer representing the number of degrees to rotate the page (clockwise).

6. A Run object represents a contiguous run of text with the same formatting, while a Paragraph object represents a paragraph of text.

7. To obtain a list of Paragraph objects for a Document object stored in a variable named 'doc', you can use the paragraphs attribute: `doc.paragraphs`.

8. The Text object has bold, underline, italic, strike, and outline variables.

9. For the bold variable, False means the text is not bold, True means the text is bold, and None means the bold formatting is inherited from the style.

10. To create a new Word document, you can use the following code: `from docx import Document` and then `document = Document()`.

11. To add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named 'doc', you can use the following code: `doc.add_paragraph('Hello, there!')`.

12. The levels of headings available in Word documents are represented by the integers 0 (for Heading 1), 1 (for Heading 2), 2 (for Heading 3), and so on.