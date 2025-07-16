#!/usr/bin/env python3
"""
Demo script for the FileSystemTool.
This demonstrates the secure file operations of the FileSystemTool.
"""

from tools.file_system_tool import read_file, write_file, read_file_tool, write_file_tool


def demo_file_operations():
    """Demonstrate the FileSystemTool functions."""
    print("=== FileSystemTool Demo ===\n")
    
    # Demo 1: Read existing file
    print("1. Reading existing test file:")
    result = read_file("tests/test_file.txt")
    print(f"Result: {result}\n")
    
    # Demo 2: Write a new file
    print("2. Writing a new demo file:")
    demo_content = "This is demo content created by the FileSystemTool.\nIt demonstrates secure file writing within the project directory."
    result = write_file("tests/demo_output.txt", demo_content)
    print(f"Result: {result}\n")
    
    # Demo 3: Read the newly created file
    print("3. Reading the newly created file:")
    result = read_file("tests/demo_output.txt")
    print(f"Result: {result}\n")
    
    # Demo 4: Try to access file outside project (should fail)
    print("4. Attempting to read file outside project (security test):")
    result = read_file("../../../etc/passwd")
    print(f"Result: {result}\n")
    
    # Demo 5: Try to write file outside project (should fail)
    print("5. Attempting to write file outside project (security test):")
    result = write_file("../malicious_file.txt", "This should not be created")
    print(f"Result: {result}\n")
    
    # Demo 6: Show that the tools are ready for ADK integration
    print("6. ADK Tool objects are ready:")
    print(f"Read tool: {read_file_tool}")
    print(f"Write tool: {write_file_tool}")
    print("These can be integrated into an ADK agent's tools list.")


if __name__ == "__main__":
    demo_file_operations() 