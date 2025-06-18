CSV to JSON Converter
=====================

📁 Features
-----------

*   Read and parse a CSV file
    
*   Convert the content into JSON
    
*   Optionally save the JSON to a file
    
*   Supports pretty-printed or compact JSON
    
*   Handles common errors (e.g., missing files)
    

🧑‍💻 Usage
-----------

### 1\. Configure the script

*   Open the script and set your file paths and options:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Copyinput_csv = "data.csv"       # Path to your input CSV file  output_json = "data.json"    # Path for output JSON file (set to None to return JSON object)  json_indent = 4              # Indentation for pretty JSON (set to None for compact)   `

### 2\. Run the script

*   Run the following command:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python csv_to_json.py   `

### 3\. Output

*   If output\_json is specified, the JSON is saved to the given file.
    
*   If output\_json is None, the JSON data is printed to the console.
    

🔧 Function Reference
---------------------

csv\_to\_json(csv\_file\_path, json\_file\_path=None, indent=4)

### Parameters:

*   csv\_file\_path (str): Path to the input .csv file.
    
*   json\_file\_path (str, optional): Path to save the output .json file. If None, data is returned.
    
*   indent (int): Number of spaces for indentation in the JSON output. Use None for compact format.
    

### Returns:

*   dict: JSON data (if json\_file\_path is None)
    
*   str: Output file path (if saved to file)
    
*   None: On error
    

📦 Example
----------

Given a data.csv:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   name,age,city  Alice,30,New York  Bob,25,San Francisco   `

The resulting data.json will look like:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   [      {          "name": "Alice",          "age": "30",          "city": "New York"      },      {          "name": "Bob",          "age": "25",          "city": "San Francisco"      }  ]   `

⚠️ Error Handling
-----------------

*   Displays an error if the CSV file doesn't exist.
    
*   Prints exception messages for unexpected issues.
