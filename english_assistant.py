#!/usr/bin/env python3
"""
English Assignment Assistant
A tool to save and manage suggestions and prompts for English assignments.
"""

import json
import os
from datetime import datetime
from typing import List, Dict


class EnglishAssistant:
    """Manages suggestions and prompts for English assignments."""
    
    def __init__(self, data_file: str = "english_data.json"):
        """Initialize the assistant with a data file."""
        self.data_file = data_file
        self.data = self._load_data()
    
    def _load_data(self) -> Dict:
        """Load data from JSON file or create new structure."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: Could not read {self.data_file}, starting fresh.")
        
        return {
            "suggestions": [],
            "prompts": []
        }
    
    def _save_data(self) -> None:
        """Save data to JSON file."""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        print(f"Data saved to {self.data_file}")
    
    def add_suggestion(self, text: str, category: str = "general") -> None:
        """Add a new suggestion."""
        suggestion = {
            "id": len(self.data["suggestions"]) + 1,
            "text": text,
            "category": category,
            "timestamp": datetime.now().isoformat(),
        }
        self.data["suggestions"].append(suggestion)
        self._save_data()
        print(f"Added suggestion #{suggestion['id']}")
    
    def add_prompt(self, text: str, category: str = "general") -> None:
        """Add a new prompt."""
        prompt = {
            "id": len(self.data["prompts"]) + 1,
            "text": text,
            "category": category,
            "timestamp": datetime.now().isoformat(),
        }
        self.data["prompts"].append(prompt)
        self._save_data()
        print(f"Added prompt #{prompt['id']}")
    
    def list_suggestions(self, category: str = None) -> None:
        """List all suggestions, optionally filtered by category."""
        suggestions = self.data["suggestions"]
        if category:
            suggestions = [s for s in suggestions if s["category"] == category]
        
        if not suggestions:
            print("No suggestions found.")
            return
        
        print("\n=== Suggestions ===")
        for s in suggestions:
            print(f"#{s['id']} [{s['category']}] {s['text']}")
            print(f"   Added: {s['timestamp']}")
    
    def list_prompts(self, category: str = None) -> None:
        """List all prompts, optionally filtered by category."""
        prompts = self.data["prompts"]
        if category:
            prompts = [p for p in prompts if p["category"] == category]
        
        if not prompts:
            print("No prompts found.")
            return
        
        print("\n=== Prompts ===")
        for p in prompts:
            print(f"#{p['id']} [{p['category']}] {p['text']}")
            print(f"   Added: {p['timestamp']}")
    
    def list_all(self) -> None:
        """List all suggestions and prompts."""
        self.list_suggestions()
        print()
        self.list_prompts()
    
    def get_categories(self) -> Dict[str, List[str]]:
        """Get all unique categories."""
        suggestion_cats = set(s["category"] for s in self.data["suggestions"])
        prompt_cats = set(p["category"] for p in self.data["prompts"])
        return {
            "suggestions": sorted(list(suggestion_cats)),
            "prompts": sorted(list(prompt_cats))
        }


def main():
    """Main interactive interface."""
    import sys
    
    assistant = EnglishAssistant()
    
    if len(sys.argv) < 2:
        print("English Assignment Assistant")
        print("\nUsage:")
        print("  python english_assistant.py add-suggestion <text> [category]")
        print("  python english_assistant.py add-prompt <text> [category]")
        print("  python english_assistant.py list-suggestions [category]")
        print("  python english_assistant.py list-prompts [category]")
        print("  python english_assistant.py list-all")
        print("  python english_assistant.py categories")
        print("\nExamples:")
        print('  python english_assistant.py add-suggestion "Use active voice" grammar')
        print('  python english_assistant.py add-prompt "Describe a sunset in 100 words" creative-writing')
        print('  python english_assistant.py list-suggestions grammar')
        return
    
    command = sys.argv[1]
    
    if command == "add-suggestion":
        if len(sys.argv) < 3:
            print("Error: Please provide suggestion text")
            return
        text = sys.argv[2]
        category = sys.argv[3] if len(sys.argv) > 3 else "general"
        assistant.add_suggestion(text, category)
    
    elif command == "add-prompt":
        if len(sys.argv) < 3:
            print("Error: Please provide prompt text")
            return
        text = sys.argv[2]
        category = sys.argv[3] if len(sys.argv) > 3 else "general"
        assistant.add_prompt(text, category)
    
    elif command == "list-suggestions":
        category = sys.argv[2] if len(sys.argv) > 2 else None
        assistant.list_suggestions(category)
    
    elif command == "list-prompts":
        category = sys.argv[2] if len(sys.argv) > 2 else None
        assistant.list_prompts(category)
    
    elif command == "list-all":
        assistant.list_all()
    
    elif command == "categories":
        cats = assistant.get_categories()
        print("\n=== Categories ===")
        print(f"Suggestion categories: {', '.join(cats['suggestions']) if cats['suggestions'] else 'None'}")
        print(f"Prompt categories: {', '.join(cats['prompts']) if cats['prompts'] else 'None'}")
    
    else:
        print(f"Unknown command: {command}")
        print("Run without arguments to see usage.")


if __name__ == "__main__":
    main()
