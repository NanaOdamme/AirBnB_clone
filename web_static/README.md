# HTML and CSS Fundamentals Readme

## Table of Contents
1. [What is HTML](#what-is-html)
2. [How to Create an HTML Page](#how-to-create-an-html-page)
3. [What is a Markup Language](#what-is-a-markup-language)
4. [What is the DOM](#what-is-the-dom)
5. [What is an Element/Tag](#what-is-an-element-tag)
6. [What is an Attribute](#what-is-an-attribute)
7. [How Does the Browser Load a Webpage](#how-does-the-browser-load-a-webpage)
8. [What is CSS](#what-is-css)
9. [How to Add Style to an Element](#how-to-add-style-to-an-element)
10. [What is a Class](#what-is-a-class)
11. [What is a Selector](#what-is-a-selector)
12. [How to Compute CSS Specificity Value](#how-to-compute-css-specificity-value)
13. [Box Properties in CSS](#box-properties-in-css)

## What is HTML
HTML (HyperText Markup Language) is the standard language used to create and design web pages. It provides a structure for web content by using a system of markup tags that describe the structure of a document, such as headings, paragraphs, links, and images.

**Example:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>My First HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a simple HTML page.</p>
</body>
</html>
```

## How to Create an HTML Page
To create an HTML page, you need a simple text editor like Notepad or a specialized code editor like Visual Studio Code. Write the HTML code, save the file with an `.html` extension, and open it in a web browser to see the result.

**Example:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>My First HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a simple HTML page.</p>
</body>
</html>
```

## What is a Markup Language
A markup language is a system for annotating a document in a way that is syntactically distinguishable from the text. HTML is a markup language that uses tags to define elements within a document.

## What is the DOM
The DOM (Document Object Model) is a programming interface for web documents. It represents the structure of a document as a tree of objects, allowing programming languages like JavaScript to manipulate the content, structure, and style of a webpage dynamically.

## What is an Element/Tag
In HTML, an element or tag is a basic building block that defines a specific part of a webpage's content. Elements are enclosed in angle brackets, and they often come in pairs (opening and closing tags) to surround content.

**Example:**
```html
<p>This is a paragraph element.</p>
<a href="https://www.example.com">Visit Example.com</a>
```

## What is an Attribute
Attributes provide additional information about HTML elements and are always included in the opening tag. They modify the default behavior of the element or provide metadata.

**Example:**
```html
<a href="https://www.example.com" target="_blank">Visit Example.com in a new tab</a>
```

## How Does the Browser Load a Webpage
When a browser loads a webpage, it follows a series of steps known as the critical rendering path. This includes parsing HTML to create the DOM, interpreting CSS to create the CSSOM, combining both to create the render tree, and finally, rendering the webpage on the screen.

## What is CSS
CSS (Cascading Style Sheets) is a style sheet language used for describing the presentation of a document written in HTML. It defines how elements should be displayed on the screen, in print, or in other media.

## How to Add Style to an Element
You can add style to an HTML element by using inline styles directly within the HTML tag, internal styles within the `<style>` tag in the document head, or external styles by linking to a separate CSS file.

**Example:**
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        h1 {
            color: blue;
        }
    </style>
</head>
<body>
    <h1>This is a styled heading.</h1>
</body>
</html>
```

## What is a Class
A class in CSS is a way to apply styles to multiple elements on a page. By assigning the same class to multiple elements, you can easily apply a consistent style to all of them.

**Example:**
```html
<style>
    .highlight {
        background-color: yellow;
    }
</style>

<p class="highlight">This paragraph is highlighted.</p>
```

## What is a Selector
Selectors in CSS determine which elements the styles will be applied to. They can target elements based on their type, class, ID, or other attributes.

**Example:**
```css
/* Selecting elements by type */
p {
    color: green;
}

/* Selecting elements by class */
.highlight {
    background-color: yellow;
}
```

## How to Compute CSS Specificity Value
CSS specificity is a set of rules that determine which style declarations are applied to an element. Specificity is calculated based on the type of selector used and whether styles are defined inline, internally, or externally.

## Box Properties in CSS
Box properties in CSS refer to the dimensions and spacing of an element. These properties include width, height, margin, padding, and border, and they collectively define the box model of an element on a webpage.

**Example:**
```css
.box {
    width: 200px;
    height: 100px;
    margin: 20px;
    padding: 10px;
    border: 2px solid black;
}
```
