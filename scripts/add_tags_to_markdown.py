"""
Script to automatically add relevant tags to markdown files in the markdownpages directory.
Maximum of 6 tags per document based on content, filename, and location.
Also updates the date in frontmatter to the current date when modifying files.
"""

import os
import re
from pathlib import Path
from typing import List, Set
from datetime import datetime
import frontmatter

# Define tag mappings based on keywords and context
TAG_KEYWORDS = {
    # Version
    'Profit9': ['profit9', 'profit 9'],
    'Profit8': ['profit8', 'profit 8'],
    'Profit7': ['profit7', 'profit 7'],
    'Profit6': ['profit6', 'profit 6'],
    'Profit5': ['profit5', 'profit 5'],
    'Profit4': ['profit4', 'profit 4'],
    'Profit3': ['profit3', 'profit 3'],

    # HTTP Methods
    'GetConnector': ['get', 'getconnector'],
    'UpdateConnector': ['post', 'put', 'delete', 'updateconnector'],

    # Technical
    'AppConnector': ['appconnector', 'app connector'],
    'Partner': ['partner', 'partners'],
    'IntegrationId': ['integrationid'],
    'Integration': ['integration', 'integratie', 'koppeling', 'certificering'],
    'Configuration': ['configuration', 'config', 'setup', 'instellingen', 'inrichting', 'tokens'],
    'Authentication': ['authentication', 'auth', 'token', 'login', 'credential', 'security'],
    'Authorization': ['authorization', 'permission', 'role', 'access', 'rights'],
    
    # Domain areas
    'Finance': ['finance', 'financial', 'grootboek', 'journaal', 'invoice', 'factuur', 'debit', 'credit', 'payment', 'betaling'],
    'Hr': ['hr', 'hrm', 'employee', 'employees', 'medewerker', 'medewerkers', 'absence', 'verlof', 'salary', 'salaris', 'applicant', 'applicants', 'sollicitant', 'sollicitanten'],
    'Payroll': ['payroll', 'loonadministratie', 'loonheffingen', 'looncomponent', 'looncomponenten'],
    'Crm': ['crm', 'contact', 'customer', 'klant', 'debtor', 'debiteur', 'creditor', 'crediteur', 'organisatie', 'persoon', 'organization', 'person'],
    'Order Management': ['sales', 'order', 'bestelling', 'purchase', 'inkoop', 'delivery', 'levering', 'goods'],
    'Projects': ['project', 'hour', 'hours', 'uur', 'uren', 'registration', 'urenregistratie'],
    'Taxes': ['fiscaal', 'ib', 'tax', 'vpb', 'aangifte'],
    'Construction': ['bouw', 'construction'],
    'Flex': ['flex', 'flexmodule', 'flex module', 'plaatsing', 'plaatsingen', 'kanditdaat', 'kandidaten', 'uitzendkracht', 'uitzendkrachten'],
                 
    # Specific entities
    'Dossier': ['subject', 'dossier', 'bijlage'],
    'Organization': ['organization', 'organisation', 'organisatie', 'company', 'bedrijf'],
    'Person': ['person', 'persoon', 'people', 'individual'],
    
    # Functional
    'Tutorial': ['tutorial', 'guide', 'how-to', 'howto', 'stappenplan'],
    'Reference': ['reference', 'spec', 'specification', 'documentation'],
}

def extract_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from markdown content using python-frontmatter."""
    try:
        post = frontmatter.loads(content)
        return post.metadata, post.content
    except Exception:
        return {}, content


def generate_tags(filepath: Path, content: str, frontmatter: dict) -> List[str]:
    """Generate relevant tags based on file location, name, and content."""
    # Step 1: Get existing tags from frontmatter
    existing_tags = frontmatter.get('tags', [])
    if isinstance(existing_tags, str):
        # Handle comma-separated string
        existing_tags = [tag.strip() for tag in existing_tags.split(',') if tag.strip()]
    elif isinstance(existing_tags, list):
        # Handle YAML list
        existing_tags = [str(tag).strip() for tag in existing_tags if tag]
    else:
        existing_tags = []
    
    # Step 2: Analyze content and filename for keywords to generate new tags
    text_to_analyze = (content + ' ' + filepath.stem + ' ' + frontmatter.get('title', '')).lower()
    
    # Keep track of generated tags in order they appear in TAG_KEYWORDS
    generated_tags = []
    generated_tags_set = set()
    
    for tag, keywords in TAG_KEYWORDS.items():
        # Skip if we already have this tag
        if tag in generated_tags_set:
            continue
            
        # Check if any keyword appears as a whole word in text
        for keyword in keywords:
            # Use word boundary regex to match whole words only
            pattern = r'\b' + re.escape(keyword) + r'\b'
            if re.search(pattern, text_to_analyze):
                generated_tags.append(tag)
                generated_tags_set.add(tag)
                break
    
    # Step 3: Remove existing tags that are also in generated tags (case-insensitive)
    generated_tags_lower = {tag.lower() for tag in generated_tags}
    filtered_existing_tags = [tag for tag in existing_tags if tag.lower() not in generated_tags_lower]
    
    # Step 4: Define priority tags
    priority_tags_list = [
        'Profit7', 
        'Partner', 
        'IntegrationId',
        'Tutorial', 
        'GetConnector', 
        'UpdateConnector', 
        'Setup']
    
    # Separate tags into three categories
    prioritized_tags = []
    remaining_generated_tags = []
    
    for tag in generated_tags:
        if tag in priority_tags_list:
            prioritized_tags.append(tag)
        else:
            remaining_generated_tags.append(tag)
    
    # Sort prioritized tags by their priority order
    prioritized_tags.sort(key=lambda x: priority_tags_list.index(x) if x in priority_tags_list else 999)
    
    # Step 5: Combine in order: priority tags -> existing tags -> remaining generated tags
    final_tags = prioritized_tags + filtered_existing_tags + remaining_generated_tags
    
    # Step 6: Remove any duplicates while preserving order, and capitalize first letter
    seen = set()
    unique_tags = []
    for tag in final_tags:
        tag_lower = tag.lower()
        if tag_lower not in seen:
            seen.add(tag_lower)
            # Capitalize first letter of the tag
            capitalized_tag = tag[0].upper() + tag[1:] if len(tag) > 0 else tag
            unique_tags.append(capitalized_tag)
    
    # Step 7: Limit to 6 tags
    return unique_tags[:6]


def add_frontmatter_to_file(filepath: Path, base_path: Path) -> bool:
    """Add or update tags in the frontmatter of a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if file is empty or too short
        if len(content.strip()) < 10:
            print(f"⊘ Skipping (too short): {filepath.name}")
            return False
        
        # Parse the markdown file
        post = frontmatter.loads(content)
        
        # Generate tags
        tags = generate_tags(filepath, post.content, post.metadata)
        
        # Skip if no meaningful tags could be generated
        if not tags:
            print(f"⊘ Skipping (no tags): {filepath.name}")
            return False
        
        # Update metadata with tags as comma-separated string
        post.metadata['tags'] = ', '.join(tags)
        
        # Update date to current date as a date object (not string) to avoid quotes
        current_date = datetime.now().date()
        post.metadata['date'] = current_date
        
        # Convert back to markdown with frontmatter
        new_content = frontmatter.dumps(post)
        
        # Write back to file with UTF-8 encoding
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        tags_str = ', '.join(tags)
        try:
            rel_path = filepath.relative_to(base_path)
        except ValueError:
            rel_path = filepath.name
        print(f"✓ Updated: {rel_path} → [{tags_str}]")
        return True
        
    except Exception as e:
        print(f"✗ Error processing {filepath.name}: {e}")
        return False


def process_directory(base_path: Path):
    """Process all markdown files in the /profit directory only."""
    profit_path = base_path / 'profit'
    
    if not profit_path.exists():
        print(f"Error: Profit directory {profit_path} does not exist!")
        return
    
    markdown_files = list(profit_path.rglob('*.md'))
    
    # Filter out README files
    markdown_files = [
        f for f in markdown_files 
        if f.name.lower() != 'readme.md'
    ]
    
    print(f"\nFound {len(markdown_files)} markdown files to process in /profit directory\n")
    
    processed = 0
    skipped = 0
    
    for filepath in sorted(markdown_files):
        result = add_frontmatter_to_file(filepath, base_path)
        if result:
            processed += 1
        else:
            skipped += 1
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  ✓ Processed: {processed}")
    print(f"  ⊘ Skipped:   {skipped}")
    print(f"  (Only /profit directory processed)")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    # Get the script's directory
    script_dir = Path(__file__).parent
    
    # Go up to OASContent and then into markdownpages
    base_path = script_dir.parent / 'markdownpages'
    
    if not base_path.exists():
        print(f"Error: Directory {base_path} does not exist!")
        exit(1)
    
    print(f"Processing markdown files in: {base_path}\n")
    process_directory(base_path)
