# Github instruction file for personal projects

Following good practices in Python enhances code readability, maintainability, and efficiency. Here's a summary of key recommendations: 

* Python code should be written with the zen of python in mind.

Zen of Python:
````
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
````


* Follow PEP 8: Adhere to the PEP 8 style guide for Python code, which covers aspects like indentation (4 spaces), line length (maximum 79 characters), blank lines, and naming conventions. If PEP 8 conflicts with the Zen of Python, adherance to PEP 8 is not required.
* Use uv virtual environments: Isolate project dependencies using virtual environments to avoid conflicts between different projects.
* Use uv for packaging and project management.
* Write clean and readable code: 
	* Use descriptive and meaningful names for variables, functions, and classes. 
	* Avoid magic numbers and strings by using constants or variables with clear names. 
	* Break down code into small, reusable modules or functions. 

* Document your code: 
	* Write docstrings to explain the purpose, parameters, and return values of functions and modules. 
	* Add comments to clarify complex logic or non-obvious code sections. 

* Handle errors gracefully: Use try-except blocks to catch and handle potential exceptions, preventing program crashes. 
* Test your code: 
	* Utilize pytest for tests.
	* Write unit tests to verify the correctness of individual components.
	* Use functional tests for higher-level testing of application behavior. 

* Optimize performance: 
	* Use built-in functions and libraries when possible, as they are often optimized for performance. 
	* Consider using list comprehensions and generators for more efficient code. 
	* Profile your code to identify performance bottlenecks and optimize accordingly. 

* Use version control: Employ Git for tracking changes, collaborating with others, and maintaining code integrity. 
* Structure your project: Organize your code into a well-defined project structure for better maintainability and scalability. 
* Use a linter and formatter: Integrate Ruff to automatically format and check your code for style issues and potential errors. 
* Use type hints: Add type hints to improve code readability and enable static analysis, catching type-related errors early on. 
* Avoid global variables: Minimize the use of global variables to prevent unintended side effects and improve code modularity. 
* Log instead of print: Use the logging module for diagnostic messages, allowing for better control and management of output. 
* Choose appropriate data structures: Select the most suitable data structures (lists, dictionaries, sets, etc.) for efficient data organization and manipulation. 
* Keep it simple: Avoid over-engineering and strive for the simplest solution that meets the requirements. 
* Stay updated: Keep learning and exploring new features, libraries, and best practices to enhance your Python skills. 
* Use context managers: Utilize the `with` statement for resource management (e.g., file handling) to ensure proper cleanup and avoid resource leaks.
* Use f-strings for formatting: Prefer f-strings (formatted string literals) for string formatting, as they are more readable and efficient than older methods like `%` formatting or `str.format()`.